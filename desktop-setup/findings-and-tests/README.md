# Findings and tests: River World on this desktop

Everything that was measured, run and concluded on this machine (Ryzen 9 5950X, 32 threads, 62 GB,
Linux Mint 22.3, kernel 7.0.0-38) between 11 and 13 October 2026, gathered in one place. Start with
`findings/FINDINGS.md`.

This folder holds copies. The originals stay in `_build/`, where the paper build and the resumable
runs depend on them, so nothing here has to be kept in step with them.

## What is where

```
findings-and-tests/
├── findings/
│   ├── FINDINGS.md                      every result in two pages: start here
│   ├── section-11-six-experiments.md    the full write-up as it appears in the paper (Section 11)
│   ├── predictions.md                   the three pre-registrations, timestamped, unedited
│   ├── scorecard.md                     each prediction against what happened
│   ├── status-log.md                    the running status notes kept during the programme
│   └── figures/                         Figures 4 to 7 (SVG)
├── tests/
│   ├── scripts/                         the tools that ran and analysed everything
│   ├── river-world-edits/               the one-line code edits for the river arms (unified diffs)
│   ├── laptop-reference/                the laptop's Section 6 logs, for the reproducibility check
│   └── logs/                            run logs, test outputs and every comparison table
└── data/
    └── runs/<condition>/seed-N/log.csv  one row per simulated year, 9 conditions x 16 seeds
```

## The tests that ran

| Test | What it answered | Output |
|---|---|---|
| Throughput, 16 / 32 / 64 processes | Section 5.2's speed estimate; the optimum process count | `tests/logs/throughput_tests.txt` |
| SMT test (`smt_test.sh`) | What the second thread per core is worth: 1.139x | `tests/logs/throughput_tests.txt` |
| Reproducibility (`repro_check.py`) | Laptop and desktop give byte-identical worlds for the same seed | `tests/logs/repro_check.txt` |
| E1, E2: `base`, `half`, `none` to 2,000 years | Does inheriting learning change how this world learns? | `tests/logs/inherit_2000.txt` |
| E3: `base`, `ford1`, `wall` to 5,000 years | Is the river a barrier to culture? | `tests/logs/river_5000.txt` |
| E4: `base`, `calm` to 2,000 years | Does disturbance keep the world interesting? | `tests/logs/events_2000.txt` |
| E5: `e20k`, `base`, `e45k` to 2,000 years | Starvation or crowding? | `tests/logs/energy_2000.txt` |
| E6: `base`, `big` to 2,000 years | Does a bigger world explore more? | `tests/logs/size_2000.txt` |
| Long runs: `base`, `none`, `ford1`, `wall` to 10,000 years | Do the 2,000-year answers hold? | `tests/logs/copy_vs_none_10000.txt`, `river_10000.txt`, `score_long_10000.txt` |

`tests/logs/driver.log` is the timestamped record of every stage of every run.

## The nine conditions

Anything not named is the stock default: 96 x 96 cells, 30,000 energy units, a 2,000-agent cap,
learning inherited in full, fires, floods and droughts on, three fords.

| Condition | Change | Years |
|---|---|---|
| `base` | none (also called `copy`) | 10,000 |
| `none` | `--inherit none` | 10,000 |
| `half` | `--inherit half` | 2,000 |
| `calm` | `--no-events` | 2,000 |
| `e20k` | `--energy 20000` | 2,000 |
| `e45k` | `--energy 45000 --capacity 3000` | 2,000 |
| `big` | `--size 128 --energy 53000 --capacity 3500` | 2,000 |
| `ford1` | one ford instead of three (`tests/river-world-edits/ford1.diff`) | 10,000 |
| `wall` | no fords (`tests/river-world-edits/wall.diff`) | 10,000 |

## Re-running the analysis

The analysis tools run straight from this folder, from inside `data/`, with nothing but Python 3:

```bash
cd data
python3 ../tests/scripts/analyse_s7.py base ford1 wall --last 100 --at 5000   # Table 11
python3 ../tests/scripts/analyse_s7.py base none --last 100 --at 10000        # Table 14
python3 ../tests/scripts/score_long.py 10000                                  # the long-run predictions
python3 ../tests/scripts/repro_check.py                                       # laptop against desktop
```

All four were run from here when the folder was made, and their output matches the paper.

The run drivers (`run_seeds.sh`, `drive.sh`, `resume.sh`, `run10k.sh`, `watch_until.sh`, `sample.sh`,
`smt_test.sh`) and `figs_s7.py` are here as the record of how things were run and drawn. They expect
the layout under `_build/`, so run them there, not here:

- Simulations and the model: `_build/experiment-s7/` (with `-ford1` and `-wall` beside it).
  `./resume.sh 20000 base none` would carry two conditions on to year 20,000 from where they stopped.
- Figures: `python3 _build/figs_s7.py long` (or `inherit`, `river`, `world`).
- The paper: `_build/experiment-s7/assemble.sh` rebuilds both PDFs.

## What is not copied

The 144 end-of-run world states (`checkpoint.pkl`, 6.1 GB in total) stay in `_build/experiment-s7*/runs/`.
They are what lets a run resume and what `snapshot.py` draws maps from. The per-year logs here hold every
measured number.

## One thing to know when comparing numbers

The learning-rate ratio at year 2,000 appears as 1.7 in Section 11.2's year-by-year table and as 1.86
in Table 14. Both are right; they average differently. Section 11.2's table takes the value in the
year itself (copy 0.057, none 0.033), while Table 14 and every `--last 100` figure use the mean of the
last 100 years (0.061 and 0.033). Because the inheriting world's learning rate is still falling, the
100-year mean sits slightly higher. Since the 13 October corrections the paper labels each window: the
Section 11.2 year-by-year table and Section 11.7's ratio series say which they use.
