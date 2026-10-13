"""Run a world and its exact left-right mirror image side by side: a bank that wins in both is a bias in the code."""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "river-world"))
import river_world as rw  # noqa: E402


def run(w, years=6):
    out = []
    for t in range(years * rw.YEAR):
        w.step()
        if (t + 1) % rw.YEAR == 0:
            a = w.alive
            out.append((int(((w.side == 0) & a).sum()), int(((w.side == 1) & a).sum())))
    return out


for seed in (1, 3):
    w = rw.World(seed=seed, events=False)
    m = rw.World(seed=seed, events=False)
    s = m.size
    for k in ("terrain", "land", "near", "bank", "decay_rate", "nutrients", "detritus"):
        setattr(m, k, getattr(m, k)[:, ::-1].copy())
    m.cx = s - 1 - m.cx
    m.bank_rows = [np.flatnonzero(m.bank[r]) for r in range(s)]
    m.pos[:, 1] = s - 1 - m.pos[:, 1]
    m.side = (m.pos[:, 1] > m.cx[m.pos[:, 0]]).astype(np.int8)
    m.rng = np.random.default_rng(99)
    w.rng = np.random.default_rng(99)
    print("seed", seed, "original (west, east):", run(w)[-3:], "| mirrored:", run(m)[-3:])
