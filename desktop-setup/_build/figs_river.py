#!/usr/bin/env python3
"""Figures for the river world setup paper, in the same hand-built SVG style as the research paper."""
import csv
import glob
import os
import statistics as st
import sys

from figs import BASE, GRID, INK, INK2, MUTED, S, SURF, Fig, nice_ticks

HERE = os.path.dirname(os.path.abspath(__file__))


def box(f, x, y, w, h, title, sub, color):
    f.rect(x, y, w, h, SURF, stroke=color, sw=2.2, rx=8)
    f.rect(x, y, 7, h, color, rx=3)
    f.t(x + 22, y + 34, title, 19, weight=600)
    for i, line in enumerate(sub):
        f.t(x + 22, y + 60 + i * 20, line, 14, fill=INK2)


def label(f, x, y, lines, anchor="middle", color=INK):
    for i, s in enumerate(lines):
        f.t(x, y + i * 18, s, 13.5 if i else 14, anchor=anchor, weight=600 if i == 0 else 400,
            fill=color if i == 0 else INK2, halo=SURF)


def fig_energy_flow():
    f = Fig(1000, 560, "Where the energy goes: the four pools of river world")
    box(f, 60, 60, 270, 112, "Nutrients on land", ["food for agents; spreads 2%", "a tick to each land neighbour"], S[2])
    box(f, 640, 60, 300, 112, "Agent bodies", ["up to 150 energy each", "split in two at reproduction"], S[1])
    box(f, 640, 330, 300, 132, "Detritus", ["waste and bodies, where they fell;", "a fire turns the nutrients it burns", "into detritus too"], S[6])
    box(f, 60, 330, 270, 112, "River load", ["nutrients in the water", "a closed loop, flowing south"], S[0])
    f.arrow(338, 130, 630, 130, S[2], 2.6, 12)
    label(f, 484, 96, ["eating", "up to 4 a tick, shared in crowds"], color=S[2])
    f.arrow(790, 180, 790, 320, S[1], 2.6, 12)
    label(f, 774, 222, ["metabolism and death", "0.5 resting, 0.9 moving, +25% at night,", "+0.05 to speak; whole bodies at death"], anchor="end", color=S[1])
    f.arrow(632, 352, 345, 178, S[6], 2.6, 12)
    label(f, 485, 384, ["decomposition", "5% a tick in forest, 3.5% in clearings,", "x1.2 in spring down to x0.4 in winter"], color=S[6])
    f.arrow(150, 180, 150, 322, S[2], 2.4, 11)
    label(f, 136, 236, ["erosion", "0.2% of bank", "nutrients a tick"], anchor="end", color=S[2])
    f.arrow(250, 322, 250, 180, S[0], 2.4, 11)
    label(f, 266, 222, ["silt", "1% of the load", "a tick, x2.5", "in spring"], anchor="start", color=S[0])
    f.line([(105, 446), (105, 478), (290, 478), (290, 452)], S[0], 2.2)
    f.arrow(290, 466, 290, 450, S[0], 2.2, 10)
    f.t(198, 502, "each tick 20% of every stretch's load", 13.5, anchor="middle", fill=INK2)
    f.t(198, 520, "moves one row south", 13.5, anchor="middle", fill=INK2)
    f.t(640, 512, "Total = nutrients + bodies + detritus + river load", 14.5, weight=600)
    f.t(640, 532, "= 30,000, asserted after every tick", 14.5, weight=600)
    f.save("fig-energy-flow.svg")


def series(cond, col):
    """Per-year mean and per-seed values of one column across a condition's seeds."""
    logs = sorted(glob.glob(os.path.join(cond, "seed-*", "log.csv")))
    data = []
    for log in logs:
        rows = [r for r in csv.DictReader(open(log)) if r["population"] not in ("", "0")]
        data.append({int(r["year"]): float(r[col]) for r in rows})
    years = sorted(set.intersection(*(set(d) for d in data)))
    return years, [st.mean(d[y] for d in data) for y in years], [[d[y] for y in years] for d in data]


def multi_panel(f, x0, y0, w, h, title, note, curves, ylabel, fmt="{:,.0f}", ymin=None, ymax=None):
    """Two series on one axis, seed spread as faint lines, means bold, labels at the right end."""
    allv = [v for c in curves for s in c["seeds"] for v in s] + [v for c in curves for v in c["mean"]]
    lo = min(allv) if ymin is None else ymin
    hi = max(allv) * 1.08 if ymax is None else ymax
    if lo > 0 and ymin is None:
        lo = lo * 0.9
    xs = curves[0]["years"]
    xmin, xmax = min(xs), max(xs)
    X = lambda v: x0 + (v - xmin) / (xmax - xmin) * w
    Y = lambda v: y0 + h - (v - lo) / (hi - lo) * h
    f.t(x0, y0 - 34, title, 17, weight=600)
    f.t(x0, y0 - 14, note, 13.5, fill=INK2)
    for tv in nice_ticks(lo, hi, 4):
        f.line([(x0, Y(tv)), (x0 + w, Y(tv))], GRID, 1, cap="butt")
        f.t(x0 - 8, Y(tv) + 5, fmt.format(tv), 13, anchor="end", fill=MUTED, mono=True)
    for tv in nice_ticks(xmin, xmax, 5):
        f.line([(X(tv), y0 + h), (X(tv), y0 + h + 5)], BASE, 1, cap="butt")
        f.t(X(tv), y0 + h + 22, f"{tv:g}", 13, anchor="middle", fill=MUTED, mono=True)
    f.line([(x0, y0 + h), (x0 + w, y0 + h)], BASE, 1.2, cap="butt")
    f.t(x0 + w / 2, y0 + h + 46, "simulated year", 13.5, anchor="middle", fill=INK2)
    f.t(x0 - 58, y0 + h / 2, ylabel, 13.5, anchor="middle", fill=INK2, rotate=-90)
    ends = []
    for c in curves:
        for sv in c["seeds"]:
            f.line([(X(a), Y(b)) for a, b in zip(xs, sv)], c["color"], 1.1, opacity=0.28)
        f.line([(X(a), Y(b)) for a, b in zip(xs, c["mean"])], c["color"], 2.4)
        f.circle(X(xs[-1]), Y(c["mean"][-1]), 4.5, c["color"])
        ends.append([Y(c["mean"][-1]), c])
    ends.sort(key=lambda e: e[0])
    for i in range(1, len(ends)):                       # keep end labels at least 17 px apart
        if ends[i][0] - ends[i - 1][0] < 17:
            ends[i][0] = ends[i - 1][0] + 17
    for yv, c in ends:
        f.t(X(xs[-1]) + 10, yv + 5, f'{c["name"]} {fmt.format(c["mean"][-1])}', 13.5, weight=600, fill=INK, halo=SURF)


def fig_results(copy_dir, none_dir, spec):
    f = Fig(1000, 860, "River world, learning inherited or not: four seeds each")
    pos = [(110, 90), (590, 90), (110, 500), (590, 500)]
    for (col, title, note, yl, fmt, ymin, ymax), (x, y) in zip(spec, pos):
        curves = []
        for name, d, color in (("copy", copy_dir, S[0]), ("none", none_dir, S[1])):
            yrs, mean, seeds = series(d, col)
            step = max(1, len(yrs) // 150)
            sel = list(range(0, len(yrs), step))
            if sel[-1] != len(yrs) - 1:
                sel.append(len(yrs) - 1)
            curves.append({"name": name, "color": color, "years": [yrs[i] for i in sel],
                           "mean": [mean[i] for i in sel], "seeds": [[s[i] for i in sel] for s in seeds]})
        multi_panel(f, x, y, 300, 250, title, note, curves, yl, fmt, ymin, ymax)
    f.t(110, 846, "Bold lines: the mean of four seeds; faint lines: each seed. copy = a child inherits its parent's "
                  "Q-table; none = it starts blank.", 13, fill=INK2)
    f.save("fig-river-results.svg")


DEFAULT_SPEC = [
    ("population", "Population", "agents alive at the year's end", "agents", "{:,.0f}", 0, None),
    ("gene_repro", "Energy to reproduce", "population mean of the gene", "energy", "{:,.0f}", None, None),
    ("q_states", "Situations each agent has met", "of 240; inherited visits count under copy", "states", "{:,.0f}", 0, None),
    ("dialect_jsd", "Do the two banks signal differently?", "Jensen-Shannon divergence, bits", "bits", "{:.3f}", 0, None),
]

if __name__ == "__main__":
    which = sys.argv[1:] or ["flow"]
    if "flow" in which:
        fig_energy_flow()
    if "results" in which:
        i = which.index("results")
        fig_results(which[i + 1], which[i + 2], DEFAULT_SPEC)
    print("ok", which)
