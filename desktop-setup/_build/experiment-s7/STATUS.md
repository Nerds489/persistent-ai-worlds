# Section 7 experiment programme: status

**6:25 am, 13 October: THE PROGRAMME IS FINISHED AND THE PAPER IS BUILT.** All four long conditions
reached 10,000 years at 6:16 am, every seed alive. Section 11.7 (Table 14, Figure 7) is written, the
third pre-registration is scored (5 right, 4 wrong), Table 15 carries all 39 predictions (17 right, 5
partly, 17 wrong), and `./assemble.sh` built the 35-page screen and print PDFs at the top level of
`desktop-setup`. Headlines: the learning-rate gap closes to 1.20 (t = 2.33), so it was speed, not
destination; only an inheriting lineage ever learns that speaking costs energy (83% silent against 33%);
inheritance feeds 7.8% more agents; the river arms still do not separate (t = 0.98).

**1:25 am, 13 October: E3 is finished and written up.** At year 5,000 the three river arms are
indistinguishable on dialect (0.0086 / 0.0090 / 0.0083, t = 0.12 for no fords against three): the
river is not a cultural barrier because three-quarters of agents on both banks favour silence and the
three spoken symbols are interchangeable. `s11-part3.md` (11.3, Table 11, Figure 5 rendered to 5,000)
is drafted, the E3 rows in the scorecard and Table 15 are filled, and L6 is already wrong. Left for
the morning: 11.7 (the 10,000-year results), L1-L5, L7, L8, the tally, `./assemble.sh`. Measured rate is 33 years a minute a seed, so `base` and `none` reach 10,000 about 3:50 am and `ford1` and `wall` about 6:20 am, an hour later than first estimated.

**Updated 12 October 2026, 9:52 pm AWST. The 10,000-year runs are going.** `run10k.sh`, launched under
`setsid`, runs the four conditions still worth running two at a time (32 processes, the measured optimum)
and survives a closed terminal:

1. `ford1` and `wall` to year 5,000, about 1.8 hours
2. `base` and `none` to year 10,000, about 3.5 hours; E3 is complete when `base` passes 5,000
3. `ford1` and `wall` from 5,000 to 10,000, about 2.2 hours

Expect it all done around 5:20 am on 13 October. `tail driver.log` shows each stage; `10K PROGRAMME
FINISHED` is the last line. If the machine restarts, `./run10k.sh` again resumes every seed exactly where
it saved (each stage is a `resume.sh` to a target year, so nothing is redone).

`half`, `calm`, `e20k`, `e45k` and `big` stop at 2,000: a trend test over years 1,500 to 2,000 found them
flat or settled. Predictions for the long runs are the third block in `predictions.md`, written before
launch.

## What is finished

Seven of the nine conditions are complete at 2,000 years, 16 seeds each, and analysed. E1, E2, E4, E5
and E6 are answered and written up.

| Condition | State |
|---|---|
| `base` `none` `half` `calm` `e20k` `e45k` `big` | done at 2,000 years, analysed, written up |
| `ford1` `wall` | stopped mid-run with checkpoints, see the table at the top |
| `base` to 5,000 | not started |

## What is left

1. **E3 only.** Compare `base`, `ford1` and `wall` at year 5,000. Predictions E3.1 to E3.5 in
   `predictions.md` are the ones still open. Already known: `wall` has logged exactly 0 crossings in
   every seed and every year; `ford1` runs about 104 crossings a year against `base`'s ~350.
2. **Write `s11-part3.md`** (Section 11.3), the only missing part of the new section.
3. **Figure 5**, `python3 ../figs_s7.py river`, which needs all three arms at 5,000.
4. **Possible Figure 7:** a signal-coloured map of the `wall` world,
   `cd ../experiment-s7-wall && python3 snapshot.py runs/wall/seed-1 --colour signal`. Worth including
   only if the two banks visibly separate by colour at year 5,000; at year 300 they did not.
5. **`./assemble.sh`**, which concatenates the eight parts into `sections/11-six-experiments.md`,
   renames `11-appendices.md` to `12-appendices.md`, patches the front matter in four places and
   rebuilds both PDFs. All four patch targets were verified against the current front matter.

## Files here

| File | What it is |
|---|---|
| `predictions.md` | 27 predictions pre-registered before the first run, plus a correction written before any result, plus a second 4-part pre-registration made mid-programme. Never edit above the correction lines. |
| `scorecard.md` | Running verdicts. 10 right, 4 partly, 11 wrong, 5 pending (all E3). |
| `s11-part1,2,4,5,6,7,8.md` | Section 11, drafted. `part3` (E3) is the gap. |
| `analyse_s7.py` | All 24 log columns with Welch *t*; `--at YEAR` compares arms of different lengths at the same age. Reproduces the paper's published Table 4 exactly. |
| `drive.sh` | Condition runner, takes additional years. |
| `resume.sh` | Carries conditions to an exact target year, computing each seed's own top-up. Use this, not `drive.sh`, after an interrupted run. |
| `smt_test.sh` | The SIGSTOP A/B that measured the second-thread gain at 1.139x. |
| `assemble.sh` | Folds Section 11 in and rebuilds. Idempotent. |
| `../figs_s7.py` | Figures 4, 5 and 6 in the paper's own SVG style. |

## Findings already banked

- Throughput 1.095 years/s per process at 16 processes, 20.15 years/s aggregate at 32. Section 5.2's
  desktop estimate was good to 0.5%. The second thread is worth 14%, not "little".
- The world is reproducible across the two machines: all four seeds shared with Section 6 match on
  every logged column for 300 years except the `energy_drift` residue.
- The Section 6 learning-rate result holds in direction and shrinks in size: the ratio peaks at 3.7
  near year 300, where Section 6 stopped, and is 1.7 by year 2,000.
- `--inherit half` is not halfway. It copies the visited mask whole and halves every value, which
  compounds to nothing, so `q_states` measures a bookkeeping flag rather than knowledge.
- E4 is a null because the disturbances touch 0.1% of the energy budget.
- The standing crop on land is pinned near 0.534 units a cell across a 2.25x range of energy and across
  a 1.79x change of world size. Population is super-proportional to energy, not sub.
- Two defects in the paper to fix while folding the section in: Table 1's kernel (6.17 against this
  machine's 7.0.0-38-generic), and Table 3's desktop column, which can stop being an estimate.
