#!/usr/bin/env python3
"""Summarise river_world runs: one line per seed, then the mean and spread across seeds.

    python3 summarise.py runs/main                  # one condition
    python3 summarise.py runs/main runs/darwin      # compare conditions, seed by seed
    python3 summarise.py runs/main --last 100       # average over the last 100 logged years (default 50)

Writes summary.csv beside the runs. Standard library only.
"""
import argparse
import csv
import glob
import math
import os
import statistics as st

KEYS = ["population", "pop_west", "pop_east", "crossings", "max_generation", "gene_repro", "gene_alpha",
        "gene_eps", "gene_lifespan", "q_states", "signal_entropy", "dialect_jsd", "ecology_entropy", "archive_size"]


def read(path):
    """All complete rows; a row still being written (missing fields) is skipped."""
    with open(path, newline="") as f:
        return [r for r in csv.DictReader(f) if None not in r.values() and r.get("energy_drift")]


def window(rows, last):
    live = [r for r in rows if r["population"] not in ("", "0")]
    out = {}
    for k in KEYS:
        vals = [float(r[k]) for r in live[-last:] if r.get(k) not in (None, "")]
        out[k] = st.mean(vals) if vals else float("nan")
    out["year"] = int(rows[-1]["year"])
    out["extinct_year"] = next((int(r["year"]) for r in rows if r["population"] in ("", "0")), "")
    out["max_drift"] = max(abs(float(r["energy_drift"])) for r in rows)
    out["events"] = sum(1 for r in rows if r["event"])
    return out


def summarise(cond, last):
    seeds = {}
    for log in sorted(glob.glob(os.path.join(cond, "*", "log.csv"))):
        rows = read(log)
        if rows:
            seeds[os.path.basename(os.path.dirname(log))] = window(rows, last)
    return seeds


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("conditions", nargs="+", help="run folders, each holding seed-N/log.csv")
    ap.add_argument("--last", type=int, default=50, help="average over this many final years")
    args = ap.parse_args()
    show = ["year", "population", "pop_west", "pop_east", "crossings", "max_generation", "gene_repro",
            "gene_alpha", "gene_eps", "dialect_jsd", "ecology_entropy", "max_drift"]
    table = []
    for cond in args.conditions:
        seeds = summarise(cond, args.last)
        if not seeds:
            print(f"{cond}: no logs yet")
            continue
        print(f"\n{cond}  ({len(seeds)} seeds, mean of the last {args.last} years)")
        print("  " + "  ".join(f"{h[:12]:>12}" for h in ["seed"] + show))
        for name, v in seeds.items():
            print("  " + "  ".join([f"{name:>12}"] + [f"{v[h]:>12.4g}" for h in show]))
            table.append({"condition": cond, "seed": name, **v})
        dead = {n: v["extinct_year"] for n, v in seeds.items() if v["extinct_year"] != ""}
        if dead:
            print("  extinct: " + ", ".join(f"{n} in year {y}" for n, y in dead.items())
                  + " (their figures above are from the years they were alive)")
        print("  " + "  ".join([f"{'mean':>12}"] + [f"{st.mean(v[h] for v in seeds.values()):>12.4g}" for h in show]))
        if len(seeds) > 1:
            print("  " + "  ".join([f"{'sd':>12}"] + [f"{st.stdev(v[h] for v in seeds.values()):>12.4g}" for h in show]))
    if len(args.conditions) > 1 and table:
        print(f"\ncomparison (mean ± standard error across seeds; Welch t for the first two conditions)")
        groups = {c: [r for r in table if r["condition"] == c] for c in args.conditions}
        a, b = (groups[c] for c in args.conditions[:2])
        for k in KEYS:
            xa, xb = [r[k] for r in a], [r[k] for r in b]
            if len(xa) > 1 and len(xb) > 1:
                ma, mb = st.mean(xa), st.mean(xb)
                se = math.sqrt(st.variance(xa) / len(xa) + st.variance(xb) / len(xb))
                t = (ma - mb) / se if se > 0 else float("nan")
                print(f"  {k:>16}: {ma:>10.4g} ± {math.sqrt(st.variance(xa) / len(xa)):<8.3g}"
                      f" vs {mb:>10.4g} ± {math.sqrt(st.variance(xb) / len(xb)):<8.3g}  t = {t:6.2f}")
    if table:
        out = os.path.join(os.path.dirname(os.path.abspath(args.conditions[0])), "summary.csv")
        with open(out, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(table[0].keys()))
            w.writeheader()
            w.writerows(table)
        print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
