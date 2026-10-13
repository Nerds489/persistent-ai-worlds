#!/usr/bin/env python3
"""Is a seed the same world on the laptop and on the desktop?

Compares the laptop's Section 6 logs (tests/laptop-reference) with the first 300 years of the same
seeds run here, column by column. energy_drift is reported separately: it is floating-point residue.

    cd data && python3 ../tests/scripts/repro_check.py
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(HERE, "..", "laptop-reference")
PAIRS = [("inherit-copy", "base"), ("inherit-none", "none")]

bad = 0
for laptop, desk in PAIRS:
    for s in range(1, 5):
        a = list(csv.DictReader(open(os.path.join(REF, laptop, f"seed-{s}", "log.csv"))))
        b = list(csv.DictReader(open(os.path.join("runs", desk, f"seed-{s}", "log.csv"))))[:len(a)]
        cols = [c for c in a[0] if c != "energy_drift"]
        diff = [(r["year"], c) for r, q in zip(a, b) for c in cols if r[c] != q[c]]
        drift = max(float(r["energy_drift"]) for r in a), max(float(q["energy_drift"]) for q in b)
        bad += len(diff)
        print(f"{laptop:12s} vs {desk:4s} seed {s}: {len(a)} years x {len(cols)} columns, "
              f"{len(diff)} differences; max energy_drift laptop {drift[0]:.2e}, desktop {drift[1]:.2e}")
print("IDENTICAL" if bad == 0 else f"{bad} DIFFERENCES")
