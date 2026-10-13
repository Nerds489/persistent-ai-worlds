# Running Persistent AI Worlds

Multi-agent simulations with progressive learning and emergent behaviour. **Second edition, 10 October 2026**: a complete rewrite of the February 2026 first edition, with every claim re-checked against primary sources.

## What is here

| File | What it is |
|---|---|
| `AI-Simulations-With-Progressive-Learning.pdf` | Screen edition, 49 pages. Dark cover, coloured callouts, clickable source links. |
| `AI-Simulations-With-Progressive-Learning_print.pdf` | Print edition, 50 pages. White cover, no background fills, mirrored margins and outer-corner page numbers for double-sided A4. |
| `AI-Simulations-With-Progressive-Learning.md` | The full text in Markdown with numbered references. Figures load from `figures/`. |
| `figures/` | Figures 1 to 5 as SVG (vector) and PNG. |
| `sim/forest_world.py` | Scenario A (Section 9): two Q-learning agents in a seasonal forest that never ends. |
| `sim/sealed_box.py` | Scenario B (Section 10): an evolving population sealed in a fixed energy budget. |
| `artificial-life-simulators.md` | Separate list of artificial-life simulators, carried over unchanged. |
| `_archive/` | The February 2026 first edition, unchanged. |
| `_source/` | Everything needed to rebuild the paper (see below). |
| `desktop-setup/` | *River World on the Desktop* (11 to 13 October 2026): Scenarios A and B in one world with a river, a setup paper for the Ryzen 9 5950X desktop, the `river-world/` kit, and Section 11's six experiments with all their logs, findings and tests. Start with its own `README.md`. |
| `PUBLISHING.md` | Where both papers can be published and how, step by step: Zenodo, OSF, arXiv, the ALIFE conference, the *Artificial Life* journal and JOSS. |

## On GitHub

Filed in the AI store, `otmof-ops/codex-division-2`, at `neural-evolution/artificial-life-simulation/progressive-learning/`: both PDFs, the Markdown text, the five figures and the two simulations, renamed to the store's conventions (`otm-2026-running-persistent-ai-worlds.pdf` and `-print.pdf`). Pull request: <https://github.com/otmof-ops/codex-division-2/pull/13>. The research notes and the build kit stay here.

*River World on the Desktop* is filed beside it at `neural-evolution/artificial-life-simulation/river-world/`: both PDFs, the Markdown, seven figures, the kit, the findings and a 31 MB archive of the logs and tests. Pull request: <https://github.com/otmof-ops/codex-division-2/pull/14>.

## Not in this repository

- **Run checkpoints** (`checkpoint.pkl`, 155 files, 6.4 GB): only needed to resume a run, and every measured number is in the logs beside them. They stay on the machines that made them; `PUBLISHING.md` Part 1 archives them on Zenodo.
- `desktop-setup.7z` and the desktop sync zip: bundles of files that are already here.

## Licence

None chosen yet, so all rights are reserved for now. One is decided before this repository or anything in it goes public; see `PUBLISHING.md` Part 0.3.

## Contents of the paper

1. The science of never-ending learning
2. Landmark experiments, re-checked
3. Foundation models meet open-endedness, 2023 to 2026
4. Societies of language-model agents
5. World models: when the simulator itself is learned
6. Progressive learning: forgetting, plasticity and memory
7. The toolkit in October 2026
8. Building a persistent multi-agent world
9. Scenario A: two AIs in a never-ending forest
10. Scenario B: AIs sealed in a box for 1,000 years
11. Safety, ethics and validity
12. Getting started: an eight-week path
13. Outlook: what to watch through 2027
14. Conclusion

Appendices: A, corrections to the first edition; B, the reference simulations; C, install commands for Linux Mint 22.3 and Python 3.12; D, artificial-life simulators you can run; E, glossary. Then 248 numbered references.

## Running the simulations

Python 3.10 or newer and NumPy. Nothing else.

```bash
python3 sim/forest_world.py --ticks 400000 --fresh   # new forest, about 33 simulated years
python3 sim/forest_world.py --ticks 400000           # carry on from the checkpoint
python3 sim/sealed_box.py --years 1000 --fresh       # 1,000 years, about 4.5 minutes on a 2019 laptop CPU
python3 sim/sealed_box.py --years 300 --fresh --energy 24000 --capacity 3000   # energy-limited box
```

Each run writes `checkpoint.pkl` and `log.csv` into `forest_run/` or `box_run/` under the current directory (`--dir` changes it). Stop a run at any point and the same command resumes it. `sealed_box.py` asserts after every tick that total energy is conserved.

## Rebuilding the paper

Needs Python 3 with the `markdown` package (3.x) and Google Chrome.

```bash
cd _source
python3 figs.py arch forest box timeline scale cover   # figures, drawn from the logs in runs/
python3 build_paper.py out screen                      # out/paper.md and out/paper.pdf
python3 build_paper.py out print                       # out/paper-print.pdf
```

- `sections/` holds the text, one file per chapter. Cite with `[@key]`; every key is defined in `refs.py`.
- The build stops on an unknown citation key, and on figure or table numbers that skip or repeat.
- `research/` holds the notes behind each chapter, including the claim-by-claim audit of the first edition (`09-factcheck.md`), and `arxiv_meta.json`, the arXiv metadata the references are built from. `python3 arxiv_meta.py` refreshes it and adds any newly cited arXiv paper.
- `runs/` holds the reference runs behind Figures 4 and 5 (`forest2`, `box1000`) and the 250-year energy-limited run quoted in Section 10 (`box_lean`).
- Fonts are IBM Plex, under the SIL Open Font License 1.1 (`fonts/OFL.txt`).

## Limits

- Search coverage was partial for parts of the 2026 sweep, so "none found" in the notes is weaker evidence than a positive finding. In the paper, anything that could not be confirmed from a primary source is labelled as an estimate, a vendor claim or unverified, or left out.
- `artificial-life-simulators.md` was not re-verified for this edition; Appendix D of the paper is the checked list.
