# Findings: River World on the Ryzen 9 5950X desktop

Everything below was measured on this machine between 2:04 pm on 11 October and 6:16 am on 13 October
2026: nine conditions, sixteen seeds each, 800,000 seed-years in total. The full write-up, with tables
and figures, is `section-11-six-experiments.md`; this is the short version. Numbers are the mean of
sixteen seeds over the last 100 years before the stated year, with Welch's *t* where two arms are
compared. Sixteen seeds a side: |*t*| above about 2 is worth a look, above 4 is a result.

## The desktop itself

- **Throughput:** 1.095 simulated years a second per process with 16 processes (17.7 in total),
  against Section 5.2's estimate of about 1.1. With 32 processes, 20.15 in total; with 64, 15.56.
  One process per logical thread is the optimum, never more.
- **The second thread per core is worth 14%** (1.139x for twice the processes), measured with one
  condition frozen by `SIGSTOP` over matched 180-second windows.
- **Temperature:** 49 to 51 °C with all cores busy, 53 °C at 64 processes. Memory was never a limit.
- **Reproducible across machines:** the first 300 years of seeds 1 to 4 run here match the laptop's
  Section 6 logs on every column, byte for byte, in both `base` and `none`. Only the floating-point
  conservation residue differs, in its last digits (`tests/logs/repro_check.txt`).
- **Paper correction:** Table 1 gives the kernel as 6.17; this machine runs 7.0.0-38-generic.

## The six experiments

**E1 and E2, inheriting learning (`copy` = `base`, `half`, `none`).** At year 2,000 learning is still
turned down when it is not passed on: learning-rate gene 0.061 against 0.033, *t* = 6.4. But the gap
peaks near year 300, exactly where Section 6 stopped, and shrinks from then on. `--inherit half` is not
a middle world: it halves the Q-values but copies the visited-states mask whole, so it matches `copy`
on situations met and `none` on the learning-rate gene.

**E3, the river (3 fords, 1 ford, no fords).** The river is not a cultural barrier. At year 5,000 the
difference between the banks' signalling is 0.0086, 0.0090 and 0.0083 (*t* = 0.12, no fords against
three) despite crossings of 193, 62 and 0 a year. At 10,000 it is 0.0098, 0.0100 and 0.0130
(*t* = 0.98). The reason: 75 to 83% of agents on both banks mostly stay silent, because speaking costs
energy, and the three spoken symbols cost the same and mean nothing different, so there is no
convention for isolated banks to split. Section 7's worked example (one ford above 0.2 within 2,000
years) is wrong by a factor of about 100.

**E4, disturbance (events on, `calm`).** Switching off fires, floods and droughts changes nothing
measurable at 2,000 years; the largest |*t*| across all columns is 1.9. Every disturbance acts on about
0.1% of the world's energy, so the experiment needs larger disturbances before it can answer.

**E5, energy (20,000, 30,000, 45,000 units).** Population is more than proportional to energy: 0.51x
at 20,000 and 1.80x at 45,000, roughly population = 0.0594 × energy − 614. The nutrients standing on
the land stay pinned at about 0.534 a land cell whatever the total; the extra energy sits in detritus.

**E6, size (96 × 96 against 128 × 128).** A bigger world is a scaled copy: 1.755x the population,
barely more behaviour diversity (+0.035 bits, inside noise), and half the bank difference, not double.

## Ten thousand years (`base`, `none`, `ford1`, `wall`)

- **The learning-rate gap closes.** Inheriting over not: 3.7 at year 300, 1.37 at 5,000, 1.20 at
  10,000, *t* = 2.33. Both worlds reach the same low learning rate; inheritance changes how fast, not
  where it ends up.
- **Only a lineage learns silence.** With inheritance, 83% of agents favour silence by year 10,000.
  Without it, 33% (chance is 25%), from year 1 to year 10,000. The cost of speaking is too small for
  one lifetime to detect and large enough for 2,400 generations to.
- **Inheritance feeds 7.8% more agents** (1,198 against 1,111, *t* = 9.8), and the inheriting world was
  still improving its grazing when it stopped; the blank world was flat from year 2,000.
- **Signal entropy in `base` levels off** at about 1.65 bits from year 7,000.
- **No seed died out** in any arm in 10,000 years; after year 2,000 no bank fell below 172 agents.

## Predictions

39 predictions were written down, timestamped, before the runs they cover (`predictions.md`, never
edited above its correction lines). 17 were right, 5 partly right, 17 wrong (`scorecard.md`). Of the 26
written before any world existed, 9 were right; of the 9 written at year 2,000 for the long runs, 5.
