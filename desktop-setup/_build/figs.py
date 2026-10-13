#!/usr/bin/env python3
"""Figures for 'Running Persistent AI Worlds' (October 2026 edition). Hand-built SVG, IBM Plex embedded."""
import base64
import csv
import html
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "figures")

# dataviz reference chrome (light) and categorical slots, fixed order
SURF, INK, INK2, MUTED, GRID, BASE = "#ffffff", "#1b2430", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
S = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
NAVY = "#14365c"


def font_css():
    def b64(name):
        with open(os.path.join(HERE, "fonts", name), "rb") as f:
            return base64.b64encode(f.read()).decode()
    latin = ("U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,"
             "U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD")
    return (f"@font-face{{font-family:'Plex';font-weight:100 700;src:url(data:font/woff2;base64,{b64('plexsans-latin.woff2')}) "
            f"format('woff2');unicode-range:{latin};}}"
            f"@font-face{{font-family:'Plex';font-weight:100 700;src:url(data:font/woff2;base64,{b64('plexsans-greek.woff2')}) "
            f"format('woff2');unicode-range:U+0370-03FF;}}"
            f"@font-face{{font-family:'PlexMono';font-weight:500;src:url(data:font/woff2;base64,{b64('plexmono-500.woff2')}) format('woff2');}}"
            "text{font-family:'Plex',sans-serif;} .m{font-family:'PlexMono',monospace;}")


class Fig:
    def __init__(self, w, h, title):
        self.w, self.h, self.o = w, h, []
        self.title = title

    def t(self, x, y, s, size=15, anchor="start", weight=400, fill=INK, mono=False, ls=None, rotate=None, halo=None):
        extra = (' class="m"' if mono else "") + (f' letter-spacing="{ls}"' if ls else "")
        if halo:
            extra += f' stroke="{halo}" stroke-width="3.2" paint-order="stroke" stroke-linejoin="round"'

        if rotate is not None:
            extra += f' transform="rotate({rotate} {x:.1f} {y:.1f})"'
        self.o.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}" '
                      f'fill="{fill}"{extra}>{html.escape(str(s))}</text>')

    def line(self, pts, color, w=2, dash=None, cap="round", opacity=None):
        d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        self.o.append(f'<polyline points="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="{cap}" '
                      f'stroke-linejoin="round"' + (f' stroke-dasharray="{dash}"' if dash else "")
                      + (f' opacity="{opacity}"' if opacity else "") + "/>")

    def rect(self, x, y, w, h, fill, stroke="none", sw=1, rx=0, dash=None, opacity=None, title=None):
        tt = f"<title>{html.escape(title)}</title>" if title else ""
        self.o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" '
                      f'stroke="{stroke}" stroke-width="{sw}"' + (f' stroke-dasharray="{dash}"' if dash else "")
                      + (f' opacity="{opacity}"' if opacity else "") + f">{tt}</rect>")

    def circle(self, x, y, r, fill, stroke=SURF, sw=2, title=None):
        tt = f"<title>{html.escape(title)}</title>" if title else ""
        self.o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}">{tt}</circle>')

    def arrow(self, x1, y1, x2, y2, color=INK2, w=1.8, head=9, dash=None):
        self.line([(x1, y1), (x2, y2)], color, w, dash=dash)
        a = math.atan2(y2 - y1, x2 - x1)
        p1 = (x2 - head * math.cos(a - 0.42), y2 - head * math.sin(a - 0.42))
        p2 = (x2 - head * math.cos(a + 0.42), y2 - head * math.sin(a + 0.42))
        self.o.append(f'<polygon points="{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{color}"/>')

    def save(self, name):
        os.makedirs(FIG, exist_ok=True)
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}">'
               f"<title>{html.escape(self.title)}</title><defs><style>{font_css()}</style></defs>"
               f'<rect width="{self.w}" height="{self.h}" fill="{SURF}"/>' + "".join(self.o) + "</svg>")
        with open(os.path.join(FIG, name), "w", encoding="utf-8") as f:
            f.write(svg)


def nice_ticks(lo, hi, n=5):
    span = hi - lo
    step = 10 ** math.floor(math.log10(span / n))
    for m in (1, 2, 2.5, 5, 10):
        if span / (step * m) <= n:
            step *= m
            break
    start = math.floor(lo / step) * step
    ticks, v = [], start
    while v <= hi + 1e-9:
        if v >= lo - 1e-9:
            ticks.append(round(v, 10))
        v += step
    return ticks


def panel(f, x0, y0, w, h, xs, ys, title, xlabel, ylabel, color, kind="line", ymin=0, ymax=None, fmt="{:,.0f}",
          note=None):
    """One small-multiple panel: single series, one axis, recessive grid, direct end label."""
    ymax = ymax or max(ys) * 1.12
    xmin, xmax = min(xs), max(xs)
    X = lambda v: x0 + (v - xmin) / (xmax - xmin) * w
    Y = lambda v: y0 + h - (v - ymin) / (ymax - ymin) * h
    f.t(x0, y0 - 34, title, 17, weight=600)
    if note:
        f.t(x0, y0 - 14, note, 13.5, fill=INK2)
    for tv in nice_ticks(ymin, ymax, 4):
        f.line([(x0, Y(tv)), (x0 + w, Y(tv))], GRID, 1, cap="butt")
        f.t(x0 - 8, Y(tv) + 5, fmt.format(tv), 13, anchor="end", fill=MUTED, mono=True)
    for tv in nice_ticks(xmin, xmax, 6):
        f.line([(X(tv), y0 + h), (X(tv), y0 + h + 5)], BASE, 1, cap="butt")
        f.t(X(tv), y0 + h + 22, f"{tv:g}", 13, anchor="middle", fill=MUTED, mono=True)
    f.line([(x0, y0 + h), (x0 + w, y0 + h)], BASE, 1.2, cap="butt")
    f.t(x0 + w / 2, y0 + h + 46, xlabel, 13.5, anchor="middle", fill=INK2)
    f.t(x0 - 54, y0 + h / 2, ylabel, 13.5, anchor="middle", fill=INK2, rotate=-90)
    if kind == "bar":
        bw = max(2.0, w / len(xs) - 2)
        for xv, yv in zip(xs, ys):
            hh = Y(ymin) - Y(yv)
            f.rect(X(xv) - bw / 2, Y(yv), bw, hh, color, rx=min(2, bw / 2), title=f"{xlabel} {xv:g}: {fmt.format(yv)}")
    else:
        f.line([(X(a), Y(b)) for a, b in zip(xs, ys)], color, 2.2)
        for a, b in zip(xs, ys):
            f.o.append(f'<circle cx="{X(a):.1f}" cy="{Y(b):.1f}" r="7" fill="transparent"><title>{xlabel} {a:g}: '
                       f"{fmt.format(b)}</title></circle>")
        f.circle(X(xs[-1]), Y(ys[-1]), 4.5, color)
        f.t(X(xs[-1]) - 6, Y(ys[-1]) - 12, fmt.format(ys[-1]), 13.5, anchor="end", weight=600)


# --------------------------------------------------------------------------- Figure: architecture
def fig_architecture():
    f = Fig(1000, 600, "Architecture of a persistent multi-agent world")

    def box(x, y, w, h, title, lines, fill="#f3f7fc", edge=NAVY, tcol=NAVY):
        f.rect(x, y, w, h, fill, stroke=edge, sw=1.4, rx=8)
        f.t(x + 14, y + 26, title, 15.5, weight=600, fill=tcol)
        for i, ln in enumerate(lines):
            f.t(x + 14, y + 50 + i * 20, ln, 13.2, fill=INK2)

    # safety envelope
    f.rect(16, 16, 968, 568, "none", stroke="#b45309", sw=1.4, rx=14, dash="7 5")
    f.t(34, 42, "SAFETY ENVELOPE", 12.5, weight=600, fill="#b45309", ls=1.6)
    f.t(34, 60, "sandbox · no network unless needed · compute and token budgets · kill switch · full logs", 12.5,
        fill="#8a5a1f")
    # world
    box(46, 86, 300, 190, "World (persistent state)", ["terrain, resources, seasons", "conserved energy / carrying capacity",
                                                        "other agents as part of the world", "serialisable every tick"])
    # agents
    box(430, 86, 300, 190, "Agents", ["observe → decide → act → feedback", "policy: network, genome or LLM",
                                      "memory: recurrent state, replay,", "or an LLM memory stream"])
    # generator
    box(46, 330, 300, 152, "World generator", ["procedural or foundation-model", "generated tasks and terrain",
                                               "perturbations against stagnation"], fill="#f1faf5", edge="#1f8a4c",
        tcol="#1f8a4c")
    # learning loops
    box(430, 330, 300, 152, "Two learning loops", ["inner: learning within a lifetime", "(RL, in-context, plasticity)",
                                                   "outer: selection across generations", "(evolution, quality-diversity)"],
        fill="#f6f3fc", edge="#4a3aa7", tcol="#4a3aa7")
    # persistence + observer column
    box(790, 86, 170, 190, "Persistence", ["checkpoints:", "world, weights,", "optimiser, RNG", "atomic writes"],
        fill="#fdf5ec", edge="#b45309", tcol="#b45309")
    box(790, 330, 170, 152, "Observer", ["metrics: novelty,", "diversity, complexity", "dashboards, replays"],
        fill="#fdf5ec", edge="#b45309", tcol="#b45309")
    # arrows
    f.arrow(346, 150, 428, 150, NAVY)
    f.t(387, 140, "observation", 12, anchor="middle", fill=INK2)
    f.arrow(430, 210, 348, 210, NAVY)
    f.t(389, 230, "action", 12, anchor="middle", fill=INK2)
    f.arrow(196, 330, 196, 278, "#1f8a4c")
    f.t(206, 310, "new tasks, shocks", 12, fill="#1f8a4c")
    f.arrow(580, 330, 580, 278, "#4a3aa7")
    f.t(590, 310, "updated policies", 12, fill="#4a3aa7")
    f.arrow(430, 420, 348, 420, "#4a3aa7", dash="5 4")
    f.t(389, 410, "difficulty", 12, anchor="middle", fill="#4a3aa7")
    f.t(389, 444, "signal", 12, anchor="middle", fill="#4a3aa7")
    f.arrow(732, 180, 788, 180, "#b45309")
    f.arrow(875, 278, 875, 328, "#b45309")
    f.t(46, 530, "The loop that matters: agents change the world, the generator keeps it learnable, and the outer loop "
                 "selects what survives.", 14, fill=INK)
    f.t(46, 554, "Everything is checkpointed so a run can last months of wall-clock time and survive crashes.", 14,
        fill=INK2)
    f.save("fig-architecture.svg")


# --------------------------------------------------------------------------- Figure: forest results
def fig_forest(log):
    rows = list(csv.DictReader(open(log)))
    yr = [float(r["year"]) for r in rows]
    deaths = [int(r["deaths_A"]) + int(r["deaths_B"]) for r in rows]
    eaten = [int(r["eaten_A"]) + int(r["eaten_B"]) for r in rows]
    f = Fig(1000, 420, "Forest world: learning across lifetimes")
    panel(f, 80, 70, 380, 250, yr, deaths, "Deaths per 10,000 ticks (both agents)", "simulated year", "deaths",
          S[7], kind="bar", note="Q-tables persist across deaths")
    panel(f, 580, 70, 380, 250, yr, eaten, "Food eaten per 10,000 ticks (both agents)", "simulated year", "items",
          S[0], kind="line", note="seasonal scarcity, 4 seasons a year")
    f.t(80, 408, "Reference run: forest_world.py, seed 7, 64 × 64 world, 400,000 ticks (33 simulated years) in 117 s on an "
                 "Intel i7-8665U laptop CPU.", 13, fill=INK2)
    f.save("fig-forest-results.svg")


# --------------------------------------------------------------------------- Figure: sealed box results
def fig_box(log):
    rows = [r for r in csv.DictReader(open(log)) if r["population"] not in ("", "0")]
    yr = [float(r["year"]) for r in rows]
    life = [float(r["mean_lifespan_gene"]) for r in rows]
    thr = [float(r["mean_repro_threshold"]) for r in rows]
    gen = [float(r["max_generation"]) for r in rows]
    step = max(1, len(yr) // 200)
    idx = list(range(0, len(yr), step))
    if idx[-1] != len(yr) - 1:
        idx.append(len(yr) - 1)
    yr, life, thr, gen = [yr[i] for i in idx], [life[i] for i in idx], [thr[i] for i in idx], [gen[i] for i in idx]
    f = Fig(1000, 430, "Sealed box: evolution in a closed energy budget")
    panel(f, 80, 70, 250, 250, yr, life, "Heritable lifespan (ticks)", "simulated year", "mean gene", S[0],
          ymin=min(life) * 0.9, ymax=max(life) * 1.06, note="population mean")
    panel(f, 410, 70, 250, 250, yr, thr, "Energy to reproduce", "simulated year", "mean gene", S[1],
          ymin=min(thr) * 0.85, ymax=max(thr) * 1.08, fmt="{:,.0f}", note="population mean")
    panel(f, 740, 70, 220, 250, yr, gen, "Deepest lineage", "simulated year", "generation", S[6],
          note="maximum generation alive")
    f.t(80, 418, "Reference run: sealed_box.py, seed 3, 48 × 48 box, capacity 1,200 agents, 60,000 energy units; total "
                 "energy checked every tick (drift 3.4 × 10⁻⁷ after 1,000 years).", 13, fill=INK2)
    f.save("fig-box-results.svg")


# --------------------------------------------------------------------------- Figure: timeline
TIMELINE = [
    ("Artificial life", [(1987.7, "ALife I, Los Alamos"), (1991.5, "Tierra"), (2003.4, "Avida EQU (Nature)"),
                         (2019.3, "Lenia"), (2020.1, "Growing NCA"), (2022.95, "Flow-Lenia"),
                         (2024.5, "Self-replicators from noise"), (2026.02, "Digital Red Queen")]),
    ("Multi-agent RL", [(2019.05, "POET"), (2019.4, "Capture the Flag"), (2019.7, "Hide-and-seek"),
                        (2019.83, "AlphaStar"), (2021.57, "XLand"), (2023.05, "AdA"), (2023.87, "JaxMARL"),
                        (2026.64, "EVE Online project")]),
    ("LLM agent societies", [(2023.3, "Generative Agents"), (2024.3, "GovSim"), (2024.83, "Project Sid"),
                             (2024.92, "OASIS"), (2025.12, "AgentSociety"), (2025.49, "Project Vend"),
                             (2026.08, "Moltbook"), (2026.45, "Emergence World")]),
    ("World models", [(2018.24, "World Models"), (2019.88, "MuZero"), (2023.03, "DreamerV3"), (2024.15, "Genie"),
                      (2024.66, "GameNGen"), (2025.6, "Genie 3"), (2025.75, "Dreamer 4"), (2026.08, "Project Genie"),
                      (2026.41, "Cosmos 3")]),
    ("Open-endedness", [(2011.0, "Novelty search"), (2015.3, "MAP-Elites"), (2019.4, "AI-GAs"), (2023.95, "FunSearch"),
                        (2024.38, "OMNI-EPIC"), (2024.5, "Open-endedness defined"), (2025.37, "AlphaEvolve"),
                        (2025.42, "Darwin Gödel Machine"), (2026.23, "AI Scientist (Nature)")]),
]


def fig_timeline():
    W, LANE, TOP, NR, RH = 1000, 132, 30, 4, 15
    x0, x1, xb = 150, 985, 300            # piecewise axis: 1985-2015 compressed, 2015-2027 expanded
    def X(y):
        if y <= 2015:
            return x0 + (y - 1985) / 30 * (xb - x0)
        return xb + (y - 2015) / 12 * (x1 - xb)
    H = TOP + LANE * len(TIMELINE) + 70
    f = Fig(W, H, "Milestones in persistent AI worlds, 1986 to 2026")
    CW = 6.5
    for i, (lane, items) in enumerate(TIMELINE):
        yc = TOP + i * LANE + LANE / 2
        bg = "#f7f9fc" if i % 2 == 0 else SURF
        f.rect(0, TOP + i * LANE, W, LANE, bg)
        f.t(14, yc + 5, lane, 14.5, weight=600, fill=INK)
        f.line([(x0, yc), (x1, yc)], BASE, 1.2, cap="butt")
        col = S[i]
        occ = {(sd, r): [] for sd in ("up", "dn") for r in range(NR)}
        marks = []
        for yr, lab in sorted(items):
            x = X(yr)
            w = len(lab) * CW + 8
            best = None
            for kmax in (2, 6, 14):
                for r in range(NR):
                    for side in ("up", "dn"):
                        for k in range(0, kmax):
                            for sign in ((0,) if k == 0 else (-1, 1)):
                                c = x + sign * k * 10
                                lo, hi = c - w / 2, c + w / 2
                                if lo < x0 - 12 or hi > W - 4:
                                    continue
                                if all(hi < a - 6 or lo > d + 6 for a, d in occ[(side, r)]):
                                    best = (side, r, lo, hi)
                                    break
                            if best:
                                break
                        if best:
                            break
                    if best:
                        break
                if best:
                    break
            if not best:
                print("timeline: unplaced", lane, lab)
                continue
            side, r, lo, hi = best
            occ[(side, r)].append((lo, hi))
            ty = yc - 12 - RH * r if side == "up" else yc + 22 + RH * r
            marks.append((x, lo, hi, ty, side, r, lab, yr))
        for x, lo, hi, ty, side, r, lab, yr in marks:
            inside = lo + 3 <= x <= hi - 3
            if r or not inside:
                y_row = ty - 4 if side == "up" else ty - 9
                pts = [(x, yc + (-7 if side == "up" else 7)), (x, y_row)]
                if not inside:
                    pts.append((lo - 2 if x < lo else hi + 2, y_row))
                f.line(pts, "#9aa3ae", 1.1)
        for x, lo, hi, ty, side, r, lab, yr in marks:
            f.circle(x, yc, 5.5, col, title=f"{lane}: {lab} ({int(yr)})")
            f.t((lo + hi) / 2, ty, lab, 11.8, anchor="middle", fill=INK, halo=bg)
    ya = TOP + LANE * len(TIMELINE) + 8
    f.line([(x0, ya), (x1, ya)], INK2, 1.2, cap="butt")
    for yr in (1985, 1995, 2005, 2015, 2017, 2019, 2021, 2023, 2025, 2027):
        f.line([(X(yr), ya), (X(yr), ya + 6)], INK2, 1, cap="butt")
        f.t(X(yr), ya + 22, str(yr), 12.5, anchor="middle", fill=MUTED, mono=True)
    f.o.append(f'<path d="M{xb-6},{ya-9} l6,6 l-6,6 M{xb},{ya-9} l6,6 l-6,6" stroke="{INK2}" stroke-width="1.2" fill="none"/>')
    f.t(xb + 12, ya + 46, "The axis changes scale at 2015: 30 years to the left of the break, 12 to the right.", 12, fill=INK2)
    f.save("fig-timeline.svg")


# --------------------------------------------------------------------------- Figure: society scale
SOCIETIES = [("Generative Agents (2023)", 25, 0), ("Project Sid, analysed (2024)", 500, 0), ("1,000 People (2024)", 1052, 0),
             ("AgentSociety, ACL version (2025)", 30000, 0), ("OASIS (2024)", 1_000_000, 0),
             ("Moltbook, registered agents (2026)", 1_500_000, 2), ("AgentTorch (2025)", 8_400_000, 1),
             ("Light Society, claimed (2025)", 1_000_000_000, 1)]


def fig_society_scale():
    W, H = 1000, 470
    x0, x1, top, rowh = 330, 960, 92, 40
    lo, hi = 1, 10
    X = lambda v: x0 + (math.log10(v) - lo) / (hi - lo) * (x1 - x0)
    f = Fig(W, H, "Agents in language-model societies")
    kinds = [("one LLM-driven agent each", S[0]), ("shared or distilled models", S[1]), ("real platform, not a simulation", S[2])]
    lx = 150
    for lab, col in kinds:
        f.circle(lx, 40, 6.5, col)
        f.t(lx + 14, 45, lab, 13.5, fill=INK2)
        lx += len(lab) * 7.4 + 48
    for p in range(lo, hi + 1):
        f.line([(X(10 ** p), top - 14), (X(10 ** p), top + rowh * len(SOCIETIES))], GRID, 1, cap="butt")
        lab = {1: "10", 2: "100", 3: "1,000", 4: "10k", 5: "100k", 6: "1M", 7: "10M", 8: "100M", 9: "1B", 10: "10B"}[p]
        f.t(X(10 ** p), top + rowh * len(SOCIETIES) + 22, lab, 12.5, anchor="middle", fill=MUTED, mono=True)
    f.t((x0 + x1) / 2, top + rowh * len(SOCIETIES) + 48, "number of agents (logarithmic scale)", 13.5, anchor="middle",
        fill=INK2)
    for i, (name, n, kind) in enumerate(SOCIETIES):
        y = top + i * rowh + rowh / 2
        f.t(x0 - 18, y + 5, name, 13.5, anchor="end", fill=INK)
        f.line([(x0, y), (X(n), y)], GRID, 2, cap="butt")
        f.circle(X(n), y, 7.5, kinds[kind][1], title=f"{name}: {n:,} agents")
        val = f"{n:,}" if n < 1_000_000 else (f"{n/1e6:g} million" if n < 1e9 else f"{n/1e9:g} billion")
        f.t(X(n) + 14, y + 5, val, 13, fill=INK2, weight=600)
    f.save("fig-society-scale.svg")


def fig_cover_art(light=False):
    W, H = 1000, 560
    x0, x1, xb = 190, 960, 330
    def X(y):
        if y <= 2015:
            return x0 + (y - 1985) / 30 * (xb - x0)
        return xb + (y - 2015) / 12 * (x1 - xb)
    dark = S[:5] if light else ["#3987e5", "#d95926", "#199e70", "#c98500", "#d55181"]
    line_c, lab_c, yr_c = ("#cfd6df", INK, MUTED) if light else ("#2b4565", "#c9d6e8", "#7f97b5")
    o = []
    lane_h = 88
    top = 40
    for i, (lane, items) in enumerate(TIMELINE):
        yc = top + i * lane_h + lane_h / 2
        o.append(f'<line x1="{x0}" y1="{yc}" x2="{x1}" y2="{yc}" stroke="{line_c}" stroke-width="1.4"/>')
        o.append(f'<text x="{x0 - 18}" y="{yc + 5}" font-size="15" text-anchor="end" fill="{lab_c}" font-weight="500">'
                 f'{html.escape(lane)}</text>')
        for yr, lab in items:
            x = X(yr)
            o.append(f'<circle cx="{x:.1f}" cy="{yc}" r="13" fill="{dark[i]}" opacity="{0.12 if light else 0.18}"/>')
            o.append(f'<circle cx="{x:.1f}" cy="{yc}" r="6" fill="{dark[i]}"/>')
    ya = top + lane_h * len(TIMELINE) + 18
    for yr in (1985, 2000, 2015, 2019, 2023, 2027):
        o.append(f'<text x="{X(yr):.1f}" y="{ya}" font-size="13" text-anchor="middle" fill="{yr_c}" class="m">{yr}</text>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
           f"<title>Five research lines, 1986 to 2026</title><defs><style>{font_css()}</style></defs>" + "".join(o) + "</svg>")
    open(os.path.join(FIG, "cover-art-light.svg" if light else "cover-art.svg"), "w", encoding="utf-8").write(svg)


if __name__ == "__main__":
    which = sys.argv[1:] or ["arch"]
    if "arch" in which:
        fig_architecture()
    if "forest" in which:
        fig_forest(os.path.join(HERE, "runs", "forest2", "log.csv"))
    if "box" in which:
        fig_box(os.path.join(HERE, "runs", "box1000", "log.csv"))
    if "timeline" in which:
        fig_timeline()
    if "scale" in which:
        fig_society_scale()
    if "cover" in which:
        fig_cover_art()
        fig_cover_art(light=True)
    print("ok", which)
