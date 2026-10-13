# River World on the Desktop

A setup paper, 11 October 2026: Scenarios A and B of *Running Persistent AI Worlds* in one sealed world, with a river
down the middle, set up to run on the Ryzen 9 5950X desktop.

| File | What it is |
|---|---|
| `River-World-Desktop-Setup.pdf` | The paper, screen edition (35 pages, with Section 11: the six experiments run on the desktop) |
| `River-World-Desktop-Setup_print.pdf` | The same, laid out for double-sided A4 printing |
| `River-World-Desktop-Setup.md` | The full text in Markdown; figures load from `figures/` |
| `river-world/` | **The kit to copy to the desktop**: `river_world.py`, `run_seeds.sh`, `summarise.py`, `snapshot.py`, `README.md` |
| `findings-and-tests/` | **Everything measured and run on the desktop**, 11 to 13 October 2026: findings, predictions and scorecard, test outputs, the scripts, and the per-year logs of all 144 runs. Start with its `README.md` |
| `figures/` | The map, the energy diagram, the results chart and the Section 11 figures |
| `_build/` | How the paper was made: its sections, figure script and build script, the tests, and the Section 6 experiment (`_build/experiment/runs/`, logs and checkpoints of 8 runs x 300 years, resumable) |

Start with Section 4 of the paper: a one-minute smoke test that also measures the desktop's real speed.

Rebuild the paper: `cd _build && python3 figs_river.py flow && python3 build_paper.py out screen && python3 build_paper.py out print`
(needs Python 3 with `markdown`, and Google Chrome). The build stops if any figure or table number is out of order
or any `@@` value is unfilled.

## Licence

*River World on the Desktop*, its text, figures, findings and logs, are licensed under CC BY 4.0
(`LICENSE-CC-BY-4.0.txt`). The code (`river-world/` and the scripts under `_build/` and `findings-and-tests/`) is
licensed under the MIT License (`LICENSE-MIT.txt`, and `river-world/LICENSE`). The IBM Plex fonts in
`_build/fonts/` keep their own SIL Open Font License. Copyright (c) 2026 Lachlan Bremner.

Cite as: Bremner, L. (2026). *River World on the Desktop*. Zenodo. <https://doi.org/10.5281/zenodo.23337944>
