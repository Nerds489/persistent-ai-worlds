#!/usr/bin/env python3
"""Summarise and compare Section 7 conditions across every column of log.csv.

The shipped summarise.py covers 14 columns; the Section 7 experiments also need mean_energy,
policy_complexity, novelty, change and the event count, so this reads the logs directly.

    python3 analyse_s7.py base none half                  # first condition is the baseline for t
    python3 analyse_s7.py base ../experiment-s7-wall/runs/wall --last 100
    python3 analyse_s7.py --csv s7_summary.csv base none half calm e20k e45k big

A condition is given either as a bare id (runs/<id>) or as a path to a run folder.
Standard library only.
"""
import argparse, csv, glob, math, os, statistics as st

COLS = ["population", "pop_west", "pop_east", "crossings", "mean_energy", "nutrients", "detritus",
        "river_load", "max_generation", "gene_lifespan", "gene_repro", "gene_mutation", "gene_alpha",
        "gene_eps", "q_states", "policy_complexity", "signal_entropy", "dialect_jsd", "novelty",
        "ecology_entropy", "change", "archive_size"]


def resolve(cond):
    return cond if os.path.isdir(cond) else os.path.join("runs", cond)


def seed_rows(log):
    with open(log, newline="") as f:
        return [r for r in csv.DictReader(f) if None not in r.values() and r.get("energy_drift")]


def seed_stats(log, last, at=None):
    rows = seed_rows(log)
    if not rows:
        return None
    if at is not None:                       # compare arms at the same simulated year, not at each one's end
        rows = [r for r in rows if int(r["year"]) <= at]
        if not rows or int(rows[-1]["year"]) < at:
            return None
    live = [r for r in rows if r["population"] not in ("", "0")]
    out = {c: st.mean(float(r[c]) for r in live[-last:]) for c in COLS if live}
    out["year"] = int(rows[-1]["year"])
    out["events"] = sum(1 for r in rows if r["event"])
    out["max_drift"] = max(abs(float(r["energy_drift"])) for r in rows)
    out["extinct_year"] = next((int(r["year"]) for r in rows if r["population"] in ("", "0")), "")
    out["bank_gap"] = abs(out["pop_west"] - out["pop_east"]) / out["population"] if out["population"] else float("nan")
    return out


def condition(cond, last, at=None):
    path = resolve(cond)
    seeds = {}
    for log in sorted(glob.glob(os.path.join(path, "*", "log.csv")),
                      key=lambda p: int(os.path.basename(os.path.dirname(p)).split("-")[-1])):
        s = seed_stats(log, last, at)
        if s:
            seeds[os.path.basename(os.path.dirname(log))] = s
    return seeds


def mean_se(vals):
    m = st.mean(vals)
    se = math.sqrt(st.variance(vals) / len(vals)) if len(vals) > 1 else 0.0
    return m, se


def welch(a, b):
    ma, sea = mean_se(a)
    mb, seb = mean_se(b)
    se = math.hypot(sea, seb)
    return ma, sea, mb, seb, ((ma - mb) / se if se > 0 else float("nan"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("conditions", nargs="+")
    ap.add_argument("--last", type=int, default=100, help="average over this many final logged years")
    ap.add_argument("--at", type=int, help="average the last --last years ENDING at this simulated year, so arms "
                                           "of different lengths are compared at the same age")
    ap.add_argument("--csv", help="write the per-seed table here")
    args = ap.parse_args()

    data, table = {}, []
    for cond in args.conditions:
        seeds = condition(cond, args.last, args.at)
        name = os.path.basename(resolve(cond).rstrip("/"))
        if not seeds:
            print(f"{cond}: no logs yet")
            continue
        data[name] = seeds
        years = {s["year"] for s in seeds.values()}
        dead = {n: s["extinct_year"] for n, s in seeds.items() if s["extinct_year"] != ""}
        print(f"\n{name}: {len(seeds)} seeds, year {min(years)}"
              + (f" to {max(years)}" if len(years) > 1 else "")
              + f", mean of the last {args.last} years"
              + (f"  EXTINCT: {dead}" if dead else ""))
        for n, s in seeds.items():
            table.append({"condition": name, "seed": n, **{k: v for k, v in s.items()}})

    if not data:
        return
    keys = COLS + ["bank_gap", "events", "max_drift"]
    base = args.conditions[0]
    bname = os.path.basename(resolve(base).rstrip("/"))
    others = [k for k in data if k != bname]
    w = max(len(k) for k in keys) + 1
    head = f"{'column':>{w}}  {bname + ' (baseline)':>26}" + "".join(f"  {k:>26}  {'t':>7}" for k in others)
    print("\n" + head)
    print("-" * len(head))
    for k in keys:
        row = f"{k:>{w}}  "
        bm, bse = mean_se([s[k] for s in data[bname].values()])
        row += f"{bm:>14.5g} +/- {bse:<8.3g}"
        for o in others:
            _, _, mo, seo, t = welch([s[k] for s in data[bname].values()], [s[k] for s in data[o].values()])
            row += f"  {mo:>14.5g} +/- {seo:<8.3g}  {t:>7.2f}"
        print(row)
    print(f"\n16 seeds a side: |t| above about 2 is worth a look, below that it is seed noise."
          + (f"  Compared at year {args.at}." if args.at else ""))

    if args.csv and table:
        with open(args.csv, "w", newline="") as f:
            wr = csv.DictWriter(f, fieldnames=list(table[0].keys()))
            wr.writeheader()
            wr.writerows(table)
        print(f"wrote {args.csv}")


if __name__ == "__main__":
    main()
