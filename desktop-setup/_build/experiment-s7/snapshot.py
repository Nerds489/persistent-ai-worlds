#!/usr/bin/env python3
"""Draw a river_world checkpoint as a PNG map: terrain, nutrients, the river and every agent.

    python3 snapshot.py runs/main/seed-1                    # writes runs/main/seed-1/map-year-N-side.png
    python3 snapshot.py runs/main/seed-1 --colour signal    # colour agents by their favourite signal
    python3 snapshot.py runs/main/seed-1 --colour generation --scale 8

Agents are coloured by bank (west orange, east sky blue) unless --colour says otherwise. NumPy only:
the PNG is written with zlib from the standard library.
"""
import argparse
import os
import struct
import sys
import zlib

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import river_world as rw  # noqa: E402

TERRAIN = {rw.FOREST: (38, 92, 52), rw.CLEARING: (141, 168, 96), rw.ROCK: (120, 117, 112),
           rw.RIVER: (42, 110, 190), rw.FORD: (190, 168, 120)}
SIDE = [(255, 138, 61), (120, 220, 255)]           # west orange, east sky blue
SIGNAL = [(250, 250, 250), (235, 104, 52), (27, 175, 122), (237, 161, 0)]


def write_png(path, rgb):
    h, w, _ = rgb.shape
    raw = b"".join(b"\x00" + rgb[y].astype(np.uint8).tobytes() for y in range(h))
    chunk = lambda tag, data: struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data))
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
                + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


def render(world, scale=6, colour="side"):
    s = world.size
    img = np.zeros((s, s, 3))
    for code, c in TERRAIN.items():
        img[world.terrain == code] = c
    # nutrients brighten the land: the richer the cell, the lighter its green
    land = world.land & (world.terrain != rw.FORD)
    n = np.clip(world.nutrients / max(np.percentile(world.nutrients[land], 99), 1e-9), 0, 1)
    img[land] = img[land] * (0.55 + 0.45 * n[land, None]) + (1 - (0.55 + 0.45 * n[land, None])) * 18
    # the river darkens where it carries more silt
    load = world.load / max(world.load.max(), 1e-9)
    river = world.terrain == rw.RIVER
    img[river] = img[river] * (1 - 0.35 * load[np.nonzero(river)[0], None])
    big = np.kron(img, np.ones((scale, scale, 1)))
    idx = np.flatnonzero(world.alive)
    if colour == "signal":                          # each agent's favourite signal over the last full year
        col = np.array(SIGNAL)[world.fav_sig[idx]]
    elif colour == "generation":
        g = world.gen[idx] / max(int(world.gen[idx].max(initial=0)), 1)
        col = np.stack([255 * g, 220 * (1 - g) + 30, 80 + 0 * g], 1)
    else:
        col = np.array(SIDE)[world.side[idx]]
    r0 = scale // 4
    for (r, c), k in zip(world.pos[idx], col):
        y, x = r * scale + scale // 2, c * scale + scale // 2
        big[y - r0:y + r0 + 1, x - r0:x + r0 + 1] = k
    return big


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run", help="a run folder (holding checkpoint.pkl) or the checkpoint itself")
    ap.add_argument("--scale", type=int, default=6, help="pixels per cell")
    ap.add_argument("--colour", choices=("side", "signal", "generation"), default="side")
    ap.add_argument("--out", help="output PNG (default: map-year-N-COLOUR.png in the run folder)")
    args = ap.parse_args()
    ckpt = args.run if args.run.endswith(".pkl") else os.path.join(args.run, "checkpoint.pkl")
    world = rw.load(ckpt)
    year = world.tick // rw.YEAR
    out = args.out or os.path.join(os.path.dirname(ckpt), f"map-year-{year}-{args.colour}.png")
    write_png(out, render(world, args.scale, args.colour))
    print(f"{out}: year {year}, {int(world.alive.sum())} agents")


if __name__ == "__main__":
    main()
