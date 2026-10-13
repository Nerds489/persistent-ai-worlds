#!/usr/bin/env python3
"""A digital terrarium: evolving agents sealed in a box with a fixed, conserved amount of energy.

Energy moves between three pools and is never created or destroyed:
    nutrients (on the grid)  ->  agent bodies  ->  detritus (waste, corpses)  ->  nutrients
Agents carry a heritable genome: a small linear policy, a lifespan, a reproduction threshold and a
mutation rate. Reproduction splits the parent's energy with a mutated child. The run checks the
conservation law every tick and checkpoints so it can be resumed indefinitely. NumPy only.

    python3 sealed_box.py --years 50            # resumes from the checkpoint if present
    python3 sealed_box.py --years 50 --fresh
"""
import argparse
import csv
import os
import pickle
import time

import numpy as np

TICKS_PER_YEAR = 100            # one "year" = 100 ticks; a typical lifespan is a few years
N_SENSE = 7                     # bias, own energy, nutrient here, nutrient gradient (4 directions)
N_ACT = 5                       # stay, N, E, S, W
MOVES = np.array([(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)])
G_POLICY = N_SENSE * N_ACT
G_LEN = G_POLICY + 3            # + lifespan, reproduction threshold, mutation rate


class Box:
    def __init__(self, size=48, capacity=1200, total_energy=60_000.0, seed=0):
        self.rng = np.random.default_rng(seed)
        self.size, self.cap, self.E = size, capacity, total_energy
        self.nutrients = np.full((size, size), 0.0)
        self.detritus = np.zeros((size, size))
        self.alive = np.zeros(capacity, bool)
        self.pos = np.zeros((capacity, 2), int)
        self.energy = np.zeros(capacity)
        self.age = np.zeros(capacity, int)
        self.gen = np.zeros(capacity, int)
        self.genome = np.zeros((capacity, G_LEN))
        self.tick = 0
        n0 = 200
        self.alive[:n0] = True
        self.pos[:n0] = self.rng.integers(0, size, (n0, 2))
        self.energy[:n0] = 40.0
        self.genome[:n0, :G_POLICY] = self.rng.normal(0, 0.5, (n0, G_POLICY))
        self.genome[:n0, G_POLICY] = 300.0                       # lifespan in ticks
        self.genome[:n0, G_POLICY + 1] = 60.0                    # energy needed to reproduce
        self.genome[:n0, G_POLICY + 2] = 0.05                    # mutation scale
        # all remaining energy starts as nutrients, spread with a little patchiness
        patch = 0.5 + self.rng.random((size, size))
        self.nutrients = patch / patch.sum() * (self.E - self.energy.sum())

    def total(self):
        return self.nutrients.sum() + self.detritus.sum() + self.energy[self.alive].sum()

    def step(self):
        s, idx = self.size, np.flatnonzero(self.alive)
        r, c = self.pos[idx, 0], self.pos[idx, 1]
        nb = lambda dr, dc: self.nutrients[(r + dr) % s, (c + dc) % s]
        sense = np.stack([np.ones(len(idx)), self.energy[idx] / 100.0, nb(0, 0),
                          nb(-1, 0) - nb(0, 0), nb(0, 1) - nb(0, 0), nb(1, 0) - nb(0, 0), nb(0, -1) - nb(0, 0)], 1)
        W = self.genome[idx, :G_POLICY].reshape(-1, N_SENSE, N_ACT)
        act = np.einsum("ns,nsa->na", sense, W).argmax(1)
        self.pos[idx] = (self.pos[idx] + MOVES[act]) % s

        # metabolism: moving costs more than resting; the cost becomes detritus where the agent stands
        cost = np.where(act == 0, 0.6, 1.0)
        cost = np.minimum(cost, self.energy[idx])
        self.energy[idx] -= cost
        np.add.at(self.detritus, (self.pos[idx, 0], self.pos[idx, 1]), cost)

        # feeding: take up to 4 units from the cell; crowded cells are shared in arrival order
        order = self.rng.permutation(idx)
        for a in order:
            cell = (self.pos[a, 0], self.pos[a, 1])
            take = min(4.0, self.nutrients[cell])
            self.nutrients[cell] -= take
            self.energy[a] += take

        # decomposition: detritus slowly returns to nutrients and diffuses a little
        dec = self.detritus * 0.05
        self.detritus -= dec
        self.nutrients += dec
        self.nutrients = 0.9 * self.nutrients + 0.025 * (np.roll(self.nutrients, 1, 0) + np.roll(self.nutrients, -1, 0)
                                                         + np.roll(self.nutrients, 1, 1) + np.roll(self.nutrients, -1, 1))

        # death: starvation or old age; the body becomes detritus
        self.age[idx] += 1
        dead = idx[(self.energy[idx] <= 0.01) | (self.age[idx] > self.genome[idx, G_POLICY])]
        np.add.at(self.detritus, (self.pos[dead, 0], self.pos[dead, 1]), self.energy[dead])
        self.energy[dead] = 0.0
        self.alive[dead] = False

        # reproduction: split energy with a mutated child in a free slot (the box has a hard capacity)
        idx = np.flatnonzero(self.alive)
        ready = idx[self.energy[idx] > self.genome[idx, G_POLICY + 1]]
        free = np.flatnonzero(~self.alive)
        for p, ch in zip(ready, free):
            half = self.energy[p] / 2
            self.energy[p] -= half
            self.energy[ch] = half
            self.alive[ch], self.age[ch], self.gen[ch] = True, 0, self.gen[p] + 1
            self.pos[ch] = self.pos[p]
            sigma = max(0.005, self.genome[p, G_POLICY + 2])
            g = self.genome[p] + self.rng.normal(0, sigma, G_LEN) * np.r_[np.ones(G_POLICY), 60.0, 10.0, 0.01]
            g[G_POLICY] = max(20.0, g[G_POLICY])
            g[G_POLICY + 1] = max(10.0, g[G_POLICY + 1])
            g[G_POLICY + 2] = float(np.clip(g[G_POLICY + 2], 0.005, 0.5))
            self.genome[ch] = g
        self.tick += 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--years", type=float, default=100)
    ap.add_argument("--dir", default="box_run")
    ap.add_argument("--seed", type=int, default=3)
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--energy", type=float, default=60_000.0, help="total conserved energy in the box")
    ap.add_argument("--capacity", type=int, default=1200, help="hard cap on simultaneous agents")
    args = ap.parse_args()
    os.makedirs(args.dir, exist_ok=True)
    ckpt, log = os.path.join(args.dir, "checkpoint.pkl"), os.path.join(args.dir, "log.csv")
    if os.path.exists(ckpt) and not args.fresh:
        with open(ckpt, "rb") as f:
            box = pickle.load(f)
        print(f"resumed at year {box.tick / TICKS_PER_YEAR:,.1f}")
    else:
        box = Box(capacity=args.capacity, total_energy=args.energy, seed=args.seed)
        if os.path.exists(log):
            os.remove(log)
    new = not os.path.exists(log)
    lf = open(log, "a", newline="")
    w = csv.writer(lf)
    if new:
        w.writerow(["year", "population", "mean_energy", "mean_lifespan_gene", "mean_repro_threshold",
                    "mean_mutation_rate", "max_generation", "genome_diversity", "energy_drift"])
    start, end, t0 = box.tick, box.tick + int(args.years * TICKS_PER_YEAR), time.time()
    while box.tick < end:
        box.step()
        drift = box.total() - box.E
        assert abs(drift) < 1e-6 * box.E, f"energy not conserved: drift {drift}"
        if box.tick % TICKS_PER_YEAR == 0:
            a = box.alive
            n = int(a.sum())
            if n == 0:
                w.writerow([box.tick // TICKS_PER_YEAR, 0, "", "", "", "", "", "", f"{drift:.2e}"])
                print("extinction")
                break
            g = box.genome[a]
            w.writerow([box.tick // TICKS_PER_YEAR, n, round(float(box.energy[a].mean()), 2),
                        round(float(g[:, G_POLICY].mean()), 1), round(float(g[:, G_POLICY + 1].mean()), 1),
                        round(float(g[:, G_POLICY + 2].mean()), 4), int(box.gen[a].max()),
                        round(float(g[:, :G_POLICY].std(0).mean()), 4), f"{drift:.2e}"])
        if box.tick % (10 * TICKS_PER_YEAR) == 0:
            with open(ckpt + ".tmp", "wb") as f:
                pickle.dump(box, f)
            os.replace(ckpt + ".tmp", ckpt)
    with open(ckpt + ".tmp", "wb") as f:
        pickle.dump(box, f)
    os.replace(ckpt + ".tmp", ckpt)
    lf.close()
    yrs = (box.tick - start) / TICKS_PER_YEAR
    print(f"year {box.tick / TICKS_PER_YEAR:,.0f}  population {int(box.alive.sum())}  "
          f"max generation {int(box.gen[box.alive].max()) if box.alive.any() else 0}  "
          f"({yrs / max(1e-9, time.time() - t0):,.1f} years/s)  energy conserved to {abs(box.total() - box.E):.1e}")


if __name__ == "__main__":
    main()
