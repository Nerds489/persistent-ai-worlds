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

- ***River World on the Desktop*** (`desktop-setup/`): text, figures, findings and logs under CC BY 4.0, code under
  the MIT License. See `desktop-setup/README.md`. Published on Zenodo as
  [10.5281/zenodo.23337944](https://doi.org/10.5281/zenodo.23337944).
- **Everything else** (*Running Persistent AI Worlds*, `sim/`, `_source/`, `_archive/`): no licence chosen yet, so all
  rights are reserved for now. See `PUBLISHING.md` Part 0.3.
- The IBM Plex fonts keep their own SIL Open Font License.
