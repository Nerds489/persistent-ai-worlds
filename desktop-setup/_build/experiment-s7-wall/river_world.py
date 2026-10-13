#!/usr/bin/env python3
"""River world: Scenario A and Scenario B in one persistent, sealed world, with a river down the middle.

From Scenario A (the forest): terrain, seasons, day and night, a 2-bit signal channel, and agents that
learn during their lives with tabular Q-learning.
From Scenario B (the sealed box): a fixed, conserved amount of energy, heritable genomes, reproduction
by splitting energy, death by starvation or old age, and evolution over thousands of generations.
New here: a river runs north to south through the middle of the world. North and south wrap, so the
river is a closed loop; east and west are walls, so the river splits the land into two banks that
meet only at three fords. The river carries nutrients: it erodes them from its banks, moves them
downstream and lays them down again as silt, more in the spring flood.

Energy lives in four pools and is never created or destroyed:
    nutrients (on land) -> agent bodies -> detritus -> nutrients, and banks <-> river load
The total is asserted after every tick. Optional events (fire, flood, drought) only move energy
between pools. The run checkpoints atomically and resumes from where it stopped. NumPy only.

    python3 river_world.py --years 50 --fresh       # new world
    python3 river_world.py --years 50               # carry on from the checkpoint
    python3 river_world.py --years 500 --inherit none --dir runs/darwin   # learning not inherited
"""
import argparse
import csv
import math
import os
import pickle
import signal
import time

import numpy as np

# terrain codes
FOREST, CLEARING, ROCK, RIVER, FORD = 0, 1, 2, 3, 4
# time: a day is 20 ticks (the last 40% is night), a season 100 ticks, a year 400 ticks
DAY, SEASON = 20, 100
YEAR = 4 * SEASON
SEASONS = ("spring", "summer", "autumn", "winter")
# agents
MOVES = np.array([(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)])    # stay, N, E, S, W
N_ACT = len(MOVES) * 4                                             # move x signal (0 = silent, 1-3)
N_STATE = 5 * 3 * 2 * 4 * 2                                        # food dir x energy band x night x heard x near river
MAX_E, FEED, GAMMA = 150.0, 4.0, 0.95
# genome: lifespan (ticks), reproduction threshold, mutation scale, learning rate, exploration rate
LIFESPAN, REPRO, SIGMA, ALPHA, EPS = range(5)
G_SCALE = np.array([80.0, 8.0, 0.01, 0.05, 0.03])
G_MIN = np.array([100.0, 20.0, 0.005, 0.01, 0.0])
G_MAX = np.array([4000.0, MAX_E - 5, 0.3, 1.0, 0.5])


def value_noise(size, rng, octaves=4):
    """Smooth 2-D noise from bilinearly upsampled random lattices (the same generator as Scenario A)."""
    out = np.zeros((size, size))
    for o in range(octaves):
        cells = 2 ** (o + 2)
        lattice = rng.random((cells + 1, cells + 1))
        xs = np.linspace(0, cells, size, endpoint=False)
        i = xs.astype(int)
        f = xs - i
        f = f * f * (3 - 2 * f)
        a, b = lattice[np.ix_(i, i)], lattice[np.ix_(i, i + 1)]
        c, d = lattice[np.ix_(i + 1, i)], lattice[np.ix_(i + 1, i + 1)]
        top, bot = a + (b - a) * f[None, :], c + (d - c) * f[None, :]
        out += (top + (bot - top) * f[:, None]) / 2 ** o
    return (out - out.min()) / (out.max() - out.min())


def shift(a, dr, dc, fill=0):
    """Value of the neighbour at (row + dr, col + dc) for every cell: rows wrap, columns do not."""
    out = np.roll(a, -dr, axis=0)
    if dc == 0:
        return out
    res = np.full_like(out, fill)
    if dc > 0:
        res[:, :-dc] = out[:, dc:]
    else:
        res[:, -dc:] = out[:, :dc]
    return res


def entropy(counts):
    p = np.asarray(counts, float)
    p = p[p > 0] / max(p.sum(), 1e-12)
    return float(-(p * np.log2(p)).sum())


class World:
    def __init__(self, size=96, capacity=2000, total_energy=30_000.0, seed=0, inherit="copy", events=True):
        self.rng = rng = np.random.default_rng(seed)
        self.size, self.cap, self.E = size, capacity, float(total_energy)
        self.inherit, self.events = inherit, events
        # terrain: forest and clearings from noise, a little rock, then the river carved down the middle
        n = value_noise(size, rng)
        q = np.quantile(n, [0.05, 0.27])
        t = np.full((size, size), FOREST, np.int8)
        t[n < q[1]] = CLEARING
        t[n < q[0]] = ROCK
        rows = np.arange(size)
        ph = rng.uniform(0, 2 * math.pi)
        self.cx = np.rint(size / 2 + 0.09 * size * np.sin(2 * math.pi * rows / size + ph)
                          + 0.03 * size * np.sin(6 * math.pi * rows / size + 2 * ph)).astype(int)
        for r in rows:
            t[r, self.cx[r] - 1:self.cx[r] + 2] = RIVER
        self.fords = []                                # E3: no fords, the river is a wall
        for f in self.fords:
            for r in (f - 1, f, f + 1):
                t[r % size][t[r % size] == RIVER] = FORD
        self.terrain = t
        self.land = np.isin(t, (FOREST, CLEARING, FORD))
        cols = np.arange(size)[None, :]
        dist = np.abs(cols - self.cx[:, None])
        self.near = (dist <= 4) & self.land                          # within reach of the water: a state bit
        self.bank = (dist == 2) & self.land                          # cells the river erodes and silts
        self.bank_rows = [np.flatnonzero(self.bank[r]) for r in rows]
        self.decay_rate = np.select([t == FOREST, t == CLEARING, t == FORD], [0.05, 0.035, 0.02], 0.0)
        # pools
        fert = np.select([t == FOREST, t == CLEARING, t == FORD], [1.0, 0.6, 0.3], 0.0) * (0.5 + rng.random((size, size)))
        self.detritus = np.zeros((size, size))
        self.load = np.zeros(size)                                   # nutrients in transit, per river row
        # agents
        self.alive = np.zeros(capacity, bool)
        self.pos = np.zeros((capacity, 2), int)
        self.energy = np.zeros(capacity)
        self.age = np.zeros(capacity, int)
        self.gen = np.zeros(capacity, int)
        self.genome = np.zeros((capacity, 5))
        self.Q = np.zeros((capacity, N_STATE, N_ACT), np.float32)
        self.visited = np.zeros((capacity, N_STATE), bool)
        self.sig_count = np.zeros((capacity, 4), np.int32)           # this year's signals, per agent
        self.moves = np.zeros(capacity, np.int32)
        self.fav_sig = np.zeros(capacity, np.int8)                  # last year's favourite signal, per agent
        n0 = min(300, capacity)
        land_cells = np.argwhere(self.land & (t != FORD))
        start = land_cells[rng.choice(len(land_cells), n0)]
        self.alive[:n0] = True
        self.pos[:n0] = start
        self.energy[:n0] = 40.0
        self.genome[:n0] = [1200.0, 70.0, 0.05, 0.2, 0.1]
        self.side = (self.pos[:, 1] > self.cx[self.pos[:, 0]]).astype(np.int8)
        self.nutrients = fert / fert.sum() * (self.E - self.energy.sum())
        self.sig_grid = np.zeros((size, size), np.int8)
        # bookkeeping
        self.tick = 0
        self.crossings = 0
        self.event, self.event_left, self.event_kind = "", 0, ""
        self.archive = set()
        self.genome_hist = []

    # ------------------------------------------------------------------ helpers
    def total(self):
        return self.nutrients.sum() + self.detritus.sum() + self.load.sum() + self.energy[self.alive].sum()

    def season(self):
        return (self.tick // SEASON) % 4

    def night(self):
        return (self.tick % DAY) >= DAY * 0.6

    def observe(self, idx):
        """Encode each agent's situation as one of N_STATE discrete states."""
        s, r, c = self.size, self.pos[idx, 0], self.pos[idx, 1]
        here = self.nutrients[r, c]
        cand = np.full((len(idx), 5), -np.inf)
        cand[:, 0] = here * 1.1 + 0.5
        for k in range(1, 5):
            rr, cc = (r + MOVES[k, 0]) % s, c + MOVES[k, 1]
            ok = (cc >= 0) & (cc < s)
            cc = np.clip(cc, 0, s - 1)
            ok &= self.land[rr, cc]
            cand[:, k] = np.where(ok, self.nutrients[rr, cc], -np.inf)
        food = (cand + self.rng.random(cand.shape) * 1e-9).argmax(1)    # random tie-breaks, as for actions
        band = np.digitize(self.energy[idx], (30.0, 70.0))
        heard = np.zeros(len(idx), np.int8)
        g = self.sig_grid
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr or dc:
                    heard = np.maximum(heard, shift(g, dr, dc)[r, c])
        return (((food * 3 + band) * 2 + int(self.night())) * 4 + heard) * 2 + self.near[r, c]

    # ------------------------------------------------------------------ one tick
    def step(self):
        rng, s = self.rng, self.size
        idx = np.flatnonzero(self.alive)
        n = len(idx)
        if n:
            st = self.observe(idx)
            # ties (untried actions all sit at 0) are broken at random: a plain argmax would always pick the
            # lowest index, and the action order would then push every agent the same way
            greedy = (self.Q[idx, st].astype(np.float64) + rng.random((n, N_ACT)) * 1e-9).argmax(1)
            explore = rng.random(n) < self.genome[idx, EPS]
            act = np.where(explore, rng.integers(0, N_ACT, n), greedy)
            mv, sig = act // 4, act % 4
            # movement: rock, deep water and the east/west walls block; fords let agents across
            r0, c0 = self.pos[idx, 0], self.pos[idx, 1]
            r1, c1 = (r0 + MOVES[mv, 0]) % s, c0 + MOVES[mv, 1]
            ok = (c1 >= 0) & (c1 < s)
            c1 = np.clip(c1, 0, s - 1)
            ok &= self.land[r1, c1]
            r1, c1 = np.where(ok, r1, r0), np.where(ok, c1, c0)
            moved = (r1 != r0) | (c1 != c0)
            self.pos[idx, 0], self.pos[idx, 1] = r1, c1
            self.moves[idx] += moved
            side = (c1 > self.cx[r1]).astype(np.int8)
            self.crossings += int((side != self.side[idx]).sum())
            self.side[idx] = side
            # metabolism: moving and night cost more, speaking a little; the cost becomes detritus underfoot
            before = self.energy[idx].copy()
            cost = (np.where(moved, 0.9, 0.5) * (1.25 if self.night() else 1.0) + 0.05 * (sig > 0))
            cost = np.minimum(cost, self.energy[idx])
            self.energy[idx] -= cost
            np.add.at(self.detritus, (r1, c1), cost)
            # feeding: crowded cells are shared in proportion to what each agent asks for
            cell = r1 * s + c1
            demand = np.minimum(FEED, MAX_E - self.energy[idx])
            tot = np.bincount(cell, weights=demand, minlength=s * s)
            avail = np.maximum(self.nutrients.ravel()[cell], 0.0)
            take = demand * np.minimum(1.0, avail / np.maximum(tot[cell], 1e-12))
            self.nutrients -= np.bincount(cell, weights=take, minlength=s * s).reshape(s, s)
            self.energy[idx] += take
            # signals: written to the grid, heard by neighbours next tick
            self.sig_grid[:] = 0
            np.maximum.at(self.sig_grid, (r1, c1), sig.astype(np.int8))
            np.add.at(self.sig_count, (idx, sig), 1)
            # learning: one Q-learning update per agent, reward = change in energy
            reward = self.energy[idx] - before
            st2 = self.observe(idx)
            a = self.genome[idx, ALPHA].astype(np.float32)
            q_sa = self.Q[idx, st, act]
            target = reward + GAMMA * self.Q[idx, st2].max(1)
            self.Q[idx, st, act] = q_sa + a * (target - q_sa)
            self.visited[idx, st] = True

        self.step_environment()

        # death: starvation or old age; the body becomes detritus where it lies
        idx = np.flatnonzero(self.alive)
        self.age[idx] += 1
        dead = idx[(self.energy[idx] <= 0.01) | (self.age[idx] > self.genome[idx, LIFESPAN])]
        np.add.at(self.detritus, (self.pos[dead, 0], self.pos[dead, 1]), self.energy[dead])
        self.energy[dead] = 0.0
        self.alive[dead] = False
        # reproduction: split energy with a mutated child; what it has learned passes on per --inherit
        idx = np.flatnonzero(self.alive)
        ready = rng.permutation(idx[self.energy[idx] > self.genome[idx, REPRO]])
        free = np.flatnonzero(~self.alive)
        k = min(len(ready), len(free))
        if k:
            p, ch = ready[:k], free[:k]
            half = self.energy[p] / 2
            self.energy[p] -= half
            self.energy[ch] = half
            self.alive[ch], self.age[ch], self.gen[ch] = True, 0, self.gen[p] + 1
            self.pos[ch], self.side[ch] = self.pos[p], self.side[p]
            sigma = self.genome[p, SIGMA][:, None]
            g = self.genome[p] + rng.normal(0, 1, (k, 5)) * (sigma / 0.05) * G_SCALE
            self.genome[ch] = np.clip(g, G_MIN, G_MAX)
            if self.inherit == "copy":
                self.Q[ch], self.visited[ch] = self.Q[p], self.visited[p]
            elif self.inherit == "half":
                self.Q[ch], self.visited[ch] = 0.5 * self.Q[p], self.visited[p]
            else:
                self.Q[ch], self.visited[ch] = 0.0, False
            self.sig_count[ch], self.moves[ch] = 0, 0
        self.tick += 1

    def step_environment(self):
        s, season = self.size, self.season()
        flood = self.event_left > 0 and self.event_kind == "flood"
        drought = self.event_left > 0 and self.event_kind == "drought"
        # decomposition: detritus returns to nutrients in place, fastest in forest and slowest in winter
        dec = self.detritus * self.decay_rate * (1.2, 1.0, 0.8, 0.4)[season]
        self.detritus -= dec
        self.nutrients += dec
        # diffusion across land only (never into rock or deep water, never over the east/west walls)
        L = self.land.astype(float)
        N = self.nutrients
        flows = []
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            out = 0.02 * np.maximum(N, 0) * L * shift(L, dr, dc)
            flows.append((dr, dc, out))
        for dr, dc, out in flows:
            N -= out
            N += shift(out, -dr, -dc)
        # the river: erosion from the banks, transport downstream (south), silt laid back on the banks
        erode = 0.002 * (3.0 if flood else 1.0)
        taken = self.nutrients * self.bank * erode
        self.nutrients -= taken
        self.load += taken.sum(1)
        flow = 0.05 if drought else 0.2
        moving = self.load * flow
        self.load += np.roll(moving, 1) - moving
        dep_rate = 0.01 * (2.5 if season == 0 else 1.0) * (6.0 if flood else 1.0) * (0.25 if drought else 1.0)
        dep = self.load * min(dep_rate, 1.0)
        self.load -= dep
        for r in range(s):
            b = self.bank_rows[r]
            if len(b):
                self.nutrients[r, b] += dep[r] / len(b)
            else:                                   # no bank on this row (rock): the silt stays in the water
                self.load[r] += dep[r]
        if self.event_left > 0:
            self.event_left -= 1

    # ------------------------------------------------------------------ events
    def maybe_event(self):
        """At the start of each season, perhaps a fire, a flood or a drought. Energy only changes pools."""
        if not self.events or self.tick % SEASON:
            return ""
        rng, season = self.rng, self.season()
        roll = rng.random()
        if season == 0 and roll < 0.25:
            self.event_kind, self.event_left = "flood", 40
            return "flood"
        if season == 1 and roll < 0.15:
            self.event_kind, self.event_left = "drought", SEASON
            return "drought"
        if season in (1, 2) and roll > 0.88:
            forest = np.argwhere(self.terrain == FOREST)
            r0, c0 = forest[rng.integers(len(forest))]
            rr, cc = np.ogrid[:self.size, :self.size]
            dr = np.minimum(np.abs(rr - r0), self.size - np.abs(rr - r0))
            burn = (dr ** 2 + (cc - c0) ** 2 <= 36) & np.isin(self.terrain, (FOREST, CLEARING))
            self.detritus[burn] += self.nutrients[burn]
            self.nutrients[burn] = 0.0
            idx = np.flatnonzero(self.alive)
            hit = idx[burn[self.pos[idx, 0], self.pos[idx, 1]]]
            lost = self.energy[hit] * 0.5
            self.energy[hit] -= lost
            np.add.at(self.detritus, (self.pos[hit, 0], self.pos[hit, 1]), lost)
            return "fire"
        return ""

    # ------------------------------------------------------------------ yearly metrics
    def year_row(self, drift):
        a = np.flatnonzero(self.alive)
        y = self.tick // YEAR
        if not len(a):
            return [y, 0] + [""] * 21 + [f"{drift:.2e}", self.event]
        g = self.genome[a]
        mean_g = g.mean(0)
        self.genome_hist.append(mean_g)
        old = self.genome_hist[-11] if len(self.genome_hist) > 10 else self.genome_hist[0]
        change = float(np.linalg.norm((mean_g - old) / G_SCALE))
        # behaviour descriptor: learning rate, exploration, reproduction threshold, favourite signal, mobility, bank
        mob = self.moves[a] / np.maximum(np.minimum(self.age[a], YEAR), 1)
        desc = np.stack([np.digitize(g[:, ALPHA], (0.1, 0.25, 0.5)), np.digitize(g[:, EPS], (0.05, 0.1, 0.2)),
                         np.digitize(g[:, REPRO], (50, 70, 90)), self.sig_count[a].argmax(1),
                         np.digitize(mob, (0.25, 0.5, 0.75)), self.side[a]], 1)
        keys = [tuple(d) for d in desc.tolist()]
        novelty = sum(1 for k in set(keys) if k not in self.archive)
        self.archive.update(keys)
        _, counts = np.unique(desc, axis=0, return_counts=True)
        visited = self.visited[a]
        greedy = self.Q[a].argmax(2)
        complexity = float(np.mean([len(np.unique(greedy[i][visited[i]])) for i in range(len(a))]))
        sig_tot = self.sig_count[a].sum(0)
        west, east = self.side[a] == 0, self.side[a] == 1
        pw = self.sig_count[a][west].sum(0) + 1.0
        pe = self.sig_count[a][east].sum(0) + 1.0
        pw, pe = pw / pw.sum(), pe / pe.sum()
        m = (pw + pe) / 2
        dialect = float(0.5 * (pw * np.log2(pw / m)).sum() + 0.5 * (pe * np.log2(pe / m)).sum())
        row = [y, len(a), int(west.sum()), int(east.sum()), self.crossings,
               round(float(self.energy[a].mean()), 2), round(float(self.nutrients.sum()), 1),
               round(float(self.detritus.sum()), 1), round(float(self.load.sum()), 1), int(self.gen[a].max()),
               round(float(mean_g[LIFESPAN]), 1), round(float(mean_g[REPRO]), 2), round(float(mean_g[SIGMA]), 4),
               round(float(mean_g[ALPHA]), 4), round(float(mean_g[EPS]), 4),
               round(float(visited.sum(1).mean()), 1), round(complexity, 2), round(entropy(sig_tot), 3),
               round(dialect, 4), novelty, round(entropy(counts), 3), round(change, 3), len(self.archive),
               f"{drift:.2e}", self.event]
        self.fav_sig[a] = self.sig_count[a].argmax(1)
        self.sig_count[a] = 0
        self.moves[a] = 0
        self.crossings = 0
        self.event = ""
        return row


HEADER = ["year", "population", "pop_west", "pop_east", "crossings", "mean_energy", "nutrients", "detritus",
          "river_load", "max_generation", "gene_lifespan", "gene_repro", "gene_mutation", "gene_alpha", "gene_eps",
          "q_states", "policy_complexity", "signal_entropy", "dialect_jsd", "novelty", "ecology_entropy",
          "change", "archive_size", "energy_drift", "event"]


def advance(world):
    """One tick: roll for a seasonal event, step the world, check the energy books."""
    ev = world.maybe_event()
    if ev:
        world.event = (world.event + "+" + ev).strip("+")
    world.step()
    drift = world.total() - world.E
    assert abs(drift) < 1e-6 * world.E, f"energy not conserved: drift {drift}"
    return drift


def save(world, path):
    """Atomic checkpoint: write a temporary file, then rename it over the old one."""
    with open(path + ".tmp", "wb") as f:
        pickle.dump({"format": 1, "state": world.__dict__}, f, protocol=pickle.HIGHEST_PROTOCOL)
    os.replace(path + ".tmp", path)


def load(path):
    """Read a checkpoint into a World. Plain arrays only, so any script can open it (see snapshot.py)."""
    with open(path, "rb") as f:
        data = pickle.load(f)
    world = World.__new__(World)
    world.__dict__.update(data["state"])
    return world


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--years", type=float, default=100, help="years to run this time (a year is 400 ticks)")
    ap.add_argument("--dir", default="river_run", help="run folder: checkpoint.pkl and log.csv live here")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--fresh", action="store_true", help="start a new world even if a checkpoint exists")
    ap.add_argument("--size", type=int, default=96)
    ap.add_argument("--energy", type=float, default=30_000.0, help="total conserved energy")
    ap.add_argument("--capacity", type=int, default=2000, help="hard cap on simultaneous agents")
    ap.add_argument("--inherit", choices=("copy", "half", "none"), default=None,
                    help="what a child gets of its parent's Q-table: copy (default), half, or none (learning is not "
                         "inherited). Fixed when the world is created")
    ap.add_argument("--no-events", action="store_true", default=None,
                    help="switch off fires, floods and droughts. Fixed when the world is created")
    ap.add_argument("--save-every", type=int, default=10, help="checkpoint every N years")
    args = ap.parse_args()

    os.makedirs(args.dir, exist_ok=True)
    ckpt, log = os.path.join(args.dir, "checkpoint.pkl"), os.path.join(args.dir, "log.csv")
    if os.path.exists(ckpt) and not args.fresh:
        world = load(ckpt)
        print(f"resumed {args.dir} at year {world.tick // YEAR:,}")
        if (args.inherit and args.inherit != world.inherit) or (args.no_events and world.events):
            print(f"  note: this world keeps its own settings (inherit={world.inherit}, events={world.events}); "
                  "use --fresh or a new --dir to change them")
        if os.path.exists(log):                     # drop log rows written after the checkpoint (a crash or kill)
            with open(log, newline="") as f:
                rows = list(csv.reader(f))
            keep = [rows[0]] + [r for r in rows[1:] if r and r[0].isdigit() and int(r[0]) <= world.tick // YEAR]
            if len(keep) != len(rows):
                with open(log + ".tmp", "w", newline="") as f:
                    csv.writer(f).writerows(keep)
                os.replace(log + ".tmp", log)
                print(f"  trimmed {len(rows) - len(keep)} log rows written after the checkpoint")
    else:
        world = World(args.size, args.capacity, args.energy, args.seed, args.inherit or "copy", not args.no_events)
        if os.path.exists(log):
            os.remove(log)
    new = not os.path.exists(log)
    lf = open(log, "a", newline="")
    w = csv.writer(lf)
    if new:
        w.writerow(HEADER)

    stop = {"now": False}
    signal.signal(signal.SIGINT, lambda *_: stop.update(now=True))
    signal.signal(signal.SIGTERM, lambda *_: stop.update(now=True))
    start, end, t0 = world.tick, world.tick + int(args.years * YEAR), time.time()
    while world.tick < end and not stop["now"]:
        drift = advance(world)
        if world.tick % YEAR == 0:
            w.writerow(world.year_row(drift))
            lf.flush()
            if not world.alive.any():
                print("extinction")
                break
            if (world.tick // YEAR) % args.save_every == 0:
                save(world, ckpt)
    # stop only on a year boundary so the log and the checkpoint always agree
    while world.tick % YEAR and world.alive.any():
        drift = advance(world)
        if world.tick % YEAR == 0:
            w.writerow(world.year_row(drift))
    save(world, ckpt)
    lf.close()
    yrs = (world.tick - start) / YEAR
    a = world.alive
    print(f"{args.dir}: year {world.tick // YEAR:,}  population {int(a.sum())} "
          f"(west {int(((world.side == 0) & a).sum())}, east {int(((world.side == 1) & a).sum())})  "
          f"max generation {int(world.gen[a].max()) if a.any() else 0}  "
          f"({yrs / max(1e-9, time.time() - t0):,.2f} years/s)  energy conserved to {abs(world.total() - world.E):.1e}")


if __name__ == "__main__":
    main()
