#!/usr/bin/env python3
"""Figures for Section 11, in the same hand-built SVG style as the rest of the paper.

    python3 figs_s7.py inherit      E1 and E2: the three inheritance arms
    python3 figs_s7.py river        E3: three fords, one ford, no fords
    python3 figs_s7.py world        E4, E5 and E6: events, energy and size
    python3 figs_s7.py long         the 10,000-year runs
    python3 figs_s7.py all
"""
import csv
import glob
import os
import statistics as st
import sys

from figs import INK, INK2, S, SURF, Fig
from figs_river import multi_panel

HERE = os.path.dirname(os.path.abspath(__file__))
S7 = os.path.join(HERE, "experiment-s7")


def runs(cond):
    """Run folder for a condition id, including the two code-edited sibling folders."""
    if cond in ("ford1", "wall"):
        return os.path.join(HERE, f"experiment-s7-{cond}", "runs", cond)
    return os.path.join(S7, "runs", cond)


def series(cond, col, until=None):
    """Per-year mean and per-seed values; col may be a name or a function of the row.

    until clips every arm to the same final year, so an arm that was carried on for longer does not
    stretch the axis under the others."""
    get = col if callable(col) else (lambda r: float(r[col]))
    data = []
    for log in sorted(glob.glob(os.path.join(runs(cond), "seed-*", "log.csv"))):
        rows = [r for r in csv.DictReader(open(log)) if r["population"] not in ("", "0") and r.get("energy_drift")]
        if rows:
            data.append({int(r["year"]): get(r) for r in rows if until is None or int(r["year"]) <= until})
    if not data:
        raise SystemExit(f"no logs yet for {cond} ({runs(cond)})")
    years = sorted(set.intersection(*(set(d) for d in data)))
    return years, [st.mean(d[y] for d in data) for y in years], [[d[y] for y in years] for d in data]


def thin(years, mean, seeds, n=150):
    step = max(1, len(years) // n)
    sel = list(range(0, len(years), step))
    if sel[-1] != len(years) - 1:
        sel.append(len(years) - 1)
    return ([years[i] for i in sel], [mean[i] for i in sel], [[s[i] for i in sel] for s in seeds])


def panels(name, title, footer, spec, size=(1000, 860), pos=None, until=None):
    """spec: one entry a panel: (column, title, note, ylabel, fmt, ymin, ymax, [(label, cond, colour), ...])"""
    f = Fig(size[0], size[1], title)
    pos = pos or [(110, 90), (590, 90), (110, 500), (590, 500)]
    for (col, t, note, yl, fmt, ymin, ymax, arms), (x, y) in zip(spec, pos):
        curves = []
        for label, cond, colour in arms:
            yrs, mean, seeds = thin(*series(cond, col, until))
            curves.append({"name": label, "color": colour, "years": yrs, "mean": mean, "seeds": seeds})
        multi_panel(f, x, y, 300, 250, t, note, curves, yl, fmt, ymin, ymax)
    lines = [footer] if isinstance(footer, str) else footer
    for i, line in enumerate(lines):
        f.t(110, size[1] - 14 - 17 * (len(lines) - 1 - i), line, 13, fill=INK2)
    f.save(name)


GAP = lambda r: abs(float(r["pop_west"]) - float(r["pop_east"])) / max(float(r["population"]), 1)


def fig_inherit():
    arms = [("copy", "base", S[0]), ("half", "half", S[3]), ("none", "none", S[1])]
    panels("fig-s7-inherit.svg", "Inheriting learning: three arms, sixteen seeds each",
           ["Bold lines: the mean of sixteen seeds; faint lines: each seed. copy = a child starts with its parent's "
            "Q-table, half = that table with every value halved, none = blank. Everything else is at the defaults."],
           [("q_states", "Situations each agent has met", "of 240; inherited visits count", "states", "{:,.0f}", 0, None, arms),
            ("gene_alpha", "Learning rate", "population mean of the gene, started at 0.2", "alpha", "{:.2f}", 0, None, arms),
            ("gene_eps", "Exploration rate", "population mean of the gene, started at 0.1", "epsilon", "{:.3f}", 0, None, arms),
            ("signal_entropy", "Signal entropy", "bits; 2.0 means all four signals equally often", "bits", "{:.2f}", None, 2.05, arms),
            (GAP, "How unevenly the banks fill", "|west - east| / population", "share", "{:.2f}", 0, None, arms),
            ("population", "Population", "agents alive at the year's end", "agents", "{:,.0f}", 0, None, arms)],
           size=(1540, 900),
           pos=[(110, 90), (585, 90), (1060, 90), (110, 500), (585, 500), (1060, 500)], until=2000)


def fig_river():
    arms = [("3 fords", "base", S[0]), ("1 ford", "ford1", S[3]), ("no fords", "wall", S[1])]
    panels("fig-s7-river.svg", "Is the river a barrier to culture? Sixteen seeds an arm, 5,000 years",
           "Bold lines: the mean of sixteen seeds; faint lines: each seed. The arms differ by one line of code: how "
           "many fords cross the river.",
           [("dialect_jsd", "Do the banks signal differently?", "Jensen-Shannon divergence, bits", "bits", "{:.3f}", 0, None, arms),
            ("crossings", "Crossings a year", "agents changing bank", "crossings", "{:,.0f}", 0, None, arms),
            (GAP, "How unevenly the banks fill", "|west - east| / population", "share", "{:.2f}", 0, None, arms),
            ("signal_entropy", "Signal entropy", "bits; 2.0 means all four signals equally often", "bits", "{:.2f}", None, 2.05, arms)],
           until=5000)


def fig_world():
    ev = [("events on", "base", S[0]), ("no events", "calm", S[2])]
    en = [("20,000", "e20k", S[4]), ("30,000", "base", S[0]), ("45,000", "e45k", S[6])]
    sz = [("96 x 96", "base", S[0]), ("128 x 128", "big", S[5])]
    panels("fig-s7-world.svg", "Disturbance, energy and size: E4, E5 and E6",
           ["Bold lines: the mean of sixteen seeds; faint lines: each seed. Each panel changes one thing against the",
            "defaults: whether fires, floods and droughts happen; how much energy the world holds; how big it is."],
           [("ecology_entropy", "Behaviour diversity, with and without disturbance", "entropy across descriptors, bits", "bits", "{:.1f}", None, None, ev),
            ("population", "Population against total energy", "the world's energy is fixed and conserved", "agents", "{:,.0f}", 0, None, en),
            ("nutrients", "Nutrients standing on the land", "the same three worlds; the lines lie on each other", "units", "{:,.0f}", 0, None, en),
            ("archive_size", "Distinct behaviours ever seen", "of 2,048, in a world of each size", "descriptors", "{:,.0f}", 0, None, sz)],
           until=2000)


def fig_long():
    inh = [("copy", "base", S[0]), ("none", "none", S[1])]
    riv = [("3 fords", "base", S[0]), ("1 ford", "ford1", S[3]), ("no fords", "wall", S[1])]
    panels("fig-s7-long.svg", "Ten thousand years: the four conditions carried on",
           ["Bold lines: the mean of sixteen seeds; faint lines: each seed. copy is the defaults; none starts every child",
            "with a blank Q-table; the river arms differ only in how many fords cross the river."],
           [("gene_alpha", "Learning rate, inheriting or not", "population mean of the gene, started at 0.2", "alpha", "{:.3f}", 0, None, inh),
            ("signal_entropy", "Signal entropy", "bits; 2.0 means all four signals equally often", "bits", "{:.2f}", None, 2.05, inh),
            ("dialect_jsd", "Do the banks signal differently?", "Jensen-Shannon divergence, bits", "bits", "{:.3f}", 0, None, riv),
            ("population", "Population, inheriting or not", "agents alive at the year's end", "agents", "{:,.0f}", 0, None, inh)],
           until=10000)


if __name__ == "__main__":
    which = sys.argv[1:] or ["all"]
    if "inherit" in which or "all" in which:
        fig_inherit()
    if "river" in which or "all" in which:
        fig_river()
    if "world" in which or "all" in which:
        fig_world()
    if "long" in which or "all" in which:
        fig_long()
    print("ok", which)
