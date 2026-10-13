#!/usr/bin/env python3
"""Two learning agents in a never-ending forest: a minimal, persistent, resumable world.

Runs on a CPU-only laptop with Python 3.10+ and NumPy. Each agent is a tabular Q-learner that keeps
its table across deaths, so learning accumulates over many lifetimes. The world has terrain, food
that regrows by season, a day-night cycle and a 2-bit signal channel the agents may learn to use.
State is checkpointed so a run can be stopped and resumed indefinitely.

    python3 forest_world.py --ticks 200000            # run (resumes from the checkpoint if present)
    python3 forest_world.py --ticks 200000 --fresh    # start a new world
"""
import argparse
import csv
import os
import pickle
import signal
import time

import numpy as np

# terrain codes
FOREST, CLEARING, WATER, ROCK = 0, 1, 2, 3
MOVES = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]          # stay, N, E, S, W
N_ACTIONS = len(MOVES) * 4 + 1                               # move x signal(0-3), plus eat
EAT = N_ACTIONS - 1
DAY, SEASON_DAYS = 100, 30                                   # ticks per day, days per season
MAX_ENERGY = 100.0
YEAR = DAY * SEASON_DAYS * 4                                  # 12,000 ticks


def value_noise(size, rng, octaves=4):
    """Smooth 2-D noise from bilinearly upsampled random lattices (no external noise library)."""
    out = np.zeros((size, size))
    for o in range(octaves):
        cells = 2 ** (o + 2)
        lattice = rng.random((cells + 1, cells + 1))
        xs = np.linspace(0, cells, size, endpoint=False)
        i = xs.astype(int)
        f = xs - i
        f = f * f * (3 - 2 * f)
        a = lattice[np.ix_(i, i)]
        b = lattice[np.ix_(i, i + 1)]
        c = lattice[np.ix_(i + 1, i)]
        d = lattice[np.ix_(i + 1, i + 1)]
        top = a + (b - a) * f[None, :]
        bot = c + (d - c) * f[None, :]
        out += (top + (bot - top) * f[:, None]) / 2 ** o
    return (out - out.min()) / (out.max() - out.min())


class World:
    def __init__(self, size=64, seed=0):
        self.rng = np.random.default_rng(seed)
        n = value_noise(size, self.rng)
        q = np.quantile(n, [0.10, 0.15, 0.30])                # 10% water, 5% rock, 15% clearing, 70% forest
        self.terrain = np.full((size, size), FOREST, dtype=np.int8)
        self.terrain[n < q[2]] = CLEARING
        self.terrain[n < q[1]] = ROCK
        self.terrain[n < q[0]] = WATER
        self.size = size
        self.food = (self.rng.random((size, size)) < 0.08) & np.isin(self.terrain, (FOREST, CLEARING))
        self.regrow = np.zeros((size, size), dtype=np.int32)  # ticks until a bare cell may regrow
        self.tick = 0

    def season(self):
        return (self.tick // (DAY * SEASON_DAYS)) % 4          # 0 spring, 1 summer, 2 autumn, 3 winter

    def night(self):
        return (self.tick % DAY) >= DAY * 0.6

    def step_food(self):
        self.regrow -= 1
        fertile = np.isin(self.terrain, (FOREST, CLEARING)) & ~self.food & (self.regrow <= 0)
        p = (0.004, 0.006, 0.003, 0.0005)[self.season()]       # winter is lean
        self.food |= fertile & (self.rng.random(self.food.shape) < p)

    def passable(self, r, c):
        return self.terrain[r % self.size, c % self.size] not in (WATER, ROCK)


class Agent:
    def __init__(self, name, rng, alpha=0.1, gamma=0.97):
        self.name, self.rng = name, rng
        self.q = {}                                              # state -> action values, kept across deaths
        self.alpha, self.gamma, self.eps = alpha, gamma, 0.2
        self.reset_body(None)
        self.lifetimes = 0
        self.eaten_total = 0

    def reset_body(self, world):
        self.energy, self.age, self.sig = 100.0, 0, 0
        if world is not None:
            while True:
                r, c = self.rng.integers(0, world.size, 2)
                if world.passable(r, c):
                    self.pos = (int(r), int(c))
                    return
        self.pos = (0, 0)

    def qrow(self, s):
        if s not in self.q:
            self.q[s] = np.zeros(N_ACTIONS)
        return self.q[s]

    def act(self, s):
        if self.rng.random() < self.eps:
            return int(self.rng.integers(N_ACTIONS))
        row = self.qrow(s)
        return int(self.rng.choice(np.flatnonzero(row == row.max())))

    def learn(self, s, a, r, s2, done):
        target = r if done else r + self.gamma * self.qrow(s2).max()
        self.qrow(s)[a] += self.alpha * (target - self.qrow(s)[a])


def direction_to(world, pos, mask, radius):
    """Coarse direction (0 none, 1 N, 2 E, 3 S, 4 W) to the nearest True cell within radius."""
    r0, c0 = pos
    best, bd = 0, None
    for dr in range(-radius, radius + 1):
        for dc in range(-radius, radius + 1):
            if mask[(r0 + dr) % world.size, (c0 + dc) % world.size]:
                d = abs(dr) + abs(dc)
                if bd is None or d < bd:
                    bd = d
                    best = 0 if d == 0 else (1 if abs(dr) >= abs(dc) and dr < 0 else 3 if abs(dr) >= abs(dc)
                                             else 2 if dc > 0 else 4)
    return best


def observe(world, me, other):
    radius = 2 if world.night() else 4
    food_dir = direction_to(world, me.pos, world.food, radius)
    om = np.zeros_like(world.food)
    om[other.pos] = True
    other_dir = direction_to(world, me.pos, om, radius)
    energy_b = min(3, int(me.energy // 40))
    return (energy_b, food_dir, other_dir, int(world.night()), world.season(), other.sig)


def save(path, world, agents, stats):
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        pickle.dump({"world": world, "agents": agents, "stats": stats}, f)
    os.replace(tmp, path)                                        # atomic: a crash never corrupts the checkpoint


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ticks", type=int, default=100_000)
    ap.add_argument("--size", type=int, default=64)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--dir", default="forest_run")
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--save-every", type=int, default=20_000)
    args = ap.parse_args()
    os.makedirs(args.dir, exist_ok=True)
    ckpt, log = os.path.join(args.dir, "checkpoint.pkl"), os.path.join(args.dir, "log.csv")

    if os.path.exists(ckpt) and not args.fresh:
        with open(ckpt, "rb") as f:
            st = pickle.load(f)
        world, agents, stats = st["world"], st["agents"], st["stats"]
        print(f"resumed at tick {world.tick:,} (year {world.tick / YEAR:.2f})")
    else:
        world = World(args.size, args.seed)
        agents = [Agent("A", np.random.default_rng(args.seed + 1)), Agent("B", np.random.default_rng(args.seed + 2))]
        for ag in agents:
            ag.reset_body(world)
        stats = {"deaths": [0, 0], "eaten": [0, 0], "signals": np.zeros((2, 4), dtype=int), "near": 0, "life": []}
        if os.path.exists(log):
            os.remove(log)

    stop = {"now": False}
    signal.signal(signal.SIGINT, lambda *_: stop.update(now=True))
    new_log = not os.path.exists(log)
    lf = open(log, "a", newline="")
    w = csv.writer(lf)
    if new_log:
        w.writerow(["tick", "year", "season", "energy_A", "energy_B", "eaten_A", "eaten_B", "deaths_A", "deaths_B",
                    "lifetimes_A", "lifetimes_B", "mean_life", "states_A", "states_B", "near_frac", "signal_entropy"])

    t0, end = time.time(), world.tick + args.ticks
    window = 10_000
    while world.tick < end and not stop["now"]:
        world.step_food()
        obs = [observe(world, agents[i], agents[1 - i]) for i in range(2)]
        acts = [agents[i].act(obs[i]) for i in range(2)]
        rewards, done = [0.0, 0.0], [False, False]
        for i, ag in enumerate(agents):
            a = acts[i]
            cost = 1.0 + (0.5 if world.night() else 0.0)       # nights are colder: dearer to stay alive
            if a == EAT:
                if world.food[ag.pos]:
                    world.food[ag.pos] = False
                    world.regrow[ag.pos] = 50
                    gain = min(20.0, MAX_ENERGY - ag.energy)      # a full stomach wastes food
                    ag.energy += gain
                    rewards[i] += gain / 20.0
                    stats["eaten"][i] += 1
                    ag.eaten_total += 1
            else:
                mv, sig = divmod(a, 4)
                ag.sig = sig
                stats["signals"][i, sig] += 1
                dr, dc = MOVES[mv]
                nr, nc = (ag.pos[0] + dr) % world.size, (ag.pos[1] + dc) % world.size
                if world.passable(nr, nc):
                    ag.pos = (nr, nc)
            ag.energy -= cost
            ag.age += 1
            rewards[i] += 0.01
            if ag.energy <= 0:
                rewards[i] -= 1.0
                done[i] = True
        if abs(agents[0].pos[0] - agents[1].pos[0]) + abs(agents[0].pos[1] - agents[1].pos[1]) <= 4:
            stats["near"] += 1
        obs2 = [observe(world, agents[i], agents[1 - i]) for i in range(2)]
        for i, ag in enumerate(agents):
            ag.learn(obs[i], acts[i], rewards[i], obs2[i], done[i])
            if done[i]:
                stats["deaths"][i] += 1
                stats["life"].append(ag.age)
                ag.lifetimes += 1
                ag.eps = max(0.02, ag.eps * 0.97)                   # explore less as experience accumulates
                ag.reset_body(world)
        world.tick += 1

        if world.tick % window == 0:
            p = stats["signals"].sum(0) / max(1, stats["signals"].sum())
            ent = float(-(p[p > 0] * np.log2(p[p > 0])).sum())
            w.writerow([world.tick, round(world.tick / YEAR, 3), world.season(),
                        round(agents[0].energy, 1), round(agents[1].energy, 1), stats["eaten"][0], stats["eaten"][1],
                        stats["deaths"][0], stats["deaths"][1], agents[0].lifetimes, agents[1].lifetimes,
                        round(float(np.mean(stats["life"])), 1) if stats["life"] else "",
                        len(agents[0].q), len(agents[1].q), round(stats["near"] / window, 3), round(ent, 3)])
            stats.update(eaten=[0, 0], deaths=[0, 0], near=0, life=[])
            stats["signals"][:] = 0
        if world.tick % args.save_every == 0:
            save(ckpt, world, agents, stats)

    save(ckpt, world, agents, stats)
    lf.close()
    rate = args.ticks / max(1e-9, time.time() - t0)
    print(f"tick {world.tick:,}  year {world.tick / YEAR:.2f}  ({rate:,.0f} ticks/s)  "
          f"lifetimes A={agents[0].lifetimes} B={agents[1].lifetimes}  "
          f"states A={len(agents[0].q)} B={len(agents[1].q)}  checkpoint {ckpt}")


if __name__ == "__main__":
    main()
