# Prediction scorecard

Filled in as each condition lands. The prediction column is copied from `predictions.md` above its
correction line and is not edited. Verdicts: RIGHT, WRONG, PARTLY, or UNTESTED.

| # | Prediction (as pre-registered) | Measured | Verdict |
|---|---|---|---|
| T1 | Aggregate throughput 3 to 5 simulated years a second | 17.5 (1.095 per process x 16) | WRONG |
| E1.1 | `population` within 10 per cent across copy/half/none, every pairwise abs(t) < 2 | copy 1,151, half 1,102, none 1,105; all within 4 per cent, but copy vs half t = 4.54 and copy vs none t = 4.15 | PARTLY |
| E1.2 | `q_states` ordered copy > half > none, every pairwise abs(t) > 4; copy 140-220, half 85-140, none 58-78 | copy 135.1, half 136.1, none 66.4. Not ordered: half equals copy (t = -0.20) because half inherits the visited mask whole. copy range 140-220 missed | WRONG |
| E1.3 | `policy_complexity` copy exceeds none by at least 1.3 of 20, half between | 19.78 / 18.96 / 18.14, monotonic, copy over none by 1.64, every pairwise abs(t) > 20 | RIGHT |
| E2.1 | `gene_alpha` copy at or above 0.20, none at or below 0.055, abs(t) > 4 | copy 0.0607 at year 2,000, not >= 0.20; none 0.0327, below 0.055; t = 6.43 | WRONG |
| E2.2 | `gene_eps` copy above 0.035, none below 0.025, abs(t) > 3 | copy 0.0310 (not above 0.035), half 0.0446, none 0.0151 (below 0.025). copy vs none t = 9.21 | PARTLY |
| E2.3 | `half` between copy and none on both genes, nearer copy on alpha | half is not between: it equals none on alpha (t = 0.17), equals copy on q_states and signal entropy, and exceeds both on eps (0.0446) | WRONG |
| E2.4 | Evolution turns learning down when it is not passed on | none below copy at every year from 50 onward, t = 6.43 at year 2,000, but the ratio peaks at 3.7 near year 300 and decays to 1.7 | RIGHT, with the size of it overstated by Section 6 |
| E3.1 | `base` three fords, 5,000 years: `dialect_jsd` below 0.005 | 0.0086 at year 5,000 (0.0060 at 2,000), rising slowly in every arm alike | WRONG |
| E3.2 | `ford1`: crossings 60-160 a year; jsd above 3x base but below 0.05 | crossings 62 at 5,000 (88 at 2,000); jsd 0.0090, 1.05x base (t = -0.15), below 0.05 | PARTLY: traffic and ceiling right, the 3x rise absent |
| E3.3 | `wall`: crossings exactly 0; jsd above 0.05 by year 2,000; bank gap above 0.25 in at least half the seeds | crossings 0 in all 80,000 seed-years; jsd 0.0042 at 2,000 and 0.0083 at 5,000 (t = 0.12 vs base); gap above 0.25 in 6 of 16 | WRONG (only the built-in clause held) |
| E3.4 | No seed extinct in any arm; at most 2 of 16 `wall` seeds lose a bank | no extinction; smallest population 318, smallest wall bank 141, no bank lost | RIGHT |
| E3.5 | The paper's own worked example (one ford above 0.2 within 2,000 years) is wrong | ford1 0.0020 at 2,000; highest single seed-year in 5,000 years 0.052 | RIGHT |
| E4.1 | `calm` logs exactly 0 events against about 150 per 300 years in base | calm 0 events; base 1,037 in 2,000 years, 156 per 300 | RIGHT |
| E4.2 | `ecology_entropy` calm lower than base by at least 0.3 bits, archive by at least 50 | calm ecology 5.00 against base 4.81, HIGHER not lower, t = -1.59; archive 740 against 751, a gap of 11 not 50 | WRONG, direction and size |
| E4.3 | `change` calm lower than base by at least 0.05 | calm change 0.131 against base 0.147, a gap of 0.016 not 0.05, t = 0.88 | WRONG |
| E4.4 | `population` calm 2 to 8 per cent higher than base | calm 1,130 against base 1,151, 1.8% LOWER not 2 to 8% higher, t = 1.33 | WRONG, direction |
| E4.5 | `novelty` does not separate the arms, abs(t) < 2 | novelty exactly 0 in both arms | RIGHT, and the measure is dead |
| E5.1 | `e20k` 0.72-0.85x base; `e45k` 1.15-1.40x base, strictly below 1.5x | e20k 584 = 0.51x base (predicted 0.72-0.85x); e45k 2,066 = 1.80x base (predicted 1.15-1.40x and strictly below 1.5x). Super-proportional, not sub | WRONG, both arms, direction of the error reversed |
| E5.2 | `gene_repro` between 20.5 and 22.5 in all three arms, every pairwise abs(t) < 3 | 21.28 / 21.41 / 21.48, all inside 20.5 to 22.5, but t = 5.64 and -2.76, not all under 3 | PARTLY |
| E5.3 | `mean_energy` rises with energy but stays below 1.0 in all three | 0.489 / 0.451 / 0.422: mean_energy FALLS as total energy rises; all below 1.0 | PARTLY, direction wrong |
| E5.4 | `gene_lifespan` does not order cleanly, abs(t) < 2 | 3,645 / 3,712 / 3,815, t = 0.76 and -1.60 | RIGHT |
| E6.1 | `big` archive at least 15 per cent above base, ecology at least 0.2 bits above | archive 805 against 751, +7.2% not +15%, t = -1.42; ecology 4.840 against 4.805, t = -0.28 | WRONG, both halves |
| E6.2 | `big` dialect_jsd at least twice base | dialect_jsd 0.0029 against base 0.0060: LOWER, not twice as high, t = 1.51 | WRONG, direction |
| E6.3 | `big` population 1.4 to 1.9x base | 2,019 against 1,151, a ratio of 1.755 against 1.79 times the cells | RIGHT |
| E6.4 | Falsifier: archive failing to rise would indict the 2,048-cell ceiling, not the world | archive did fail to rise, and the ceiling is NOT what stopped it: 805 of 2,048 cells used | RIGHT, and it indicts the world, not the ceiling |

## The second pre-registration (16:35, with e45k still running)

| # | Prediction | Measured | Verdict |
|---|---|---|---|
| P2.1 | Nutrients within 2% of 4,550; crop within 2% of 0.535 a cell | 4,610 (+1.3%); 0.5411 a land cell (+1.1% on 0.535) | RIGHT |
| P2.2 | Detritus about 39,000 | 39,490 | RIGHT |
| P2.3 | Population 1,600 to 2,000 (line gives 2,002) | 2,066 | WRONG, 3.3% above the interval; the point estimate was 3.2% low |
| P2.4 | mean_energy below base's 0.451 | 0.4221 | RIGHT |
| P2.falsifier | Nutrients rising with the world's total energy | 4,558 / 4,544 / 4,610 across a 2.25x range | NOT TRIGGERED |

## The third pre-registration (9:44 pm on 12 October, the 10,000-year runs). Scored 6:30 am, 13 October: 5 right, 4 wrong.

| # | Prediction | Measured | Verdict |
|---|---|---|---|
| L1 | Learning-rate ratio copy/none 1.0-1.4 at year 10,000, abs(t) < 3 | 1.20, t = 2.33 (t first below 3 at year 9,000) | RIGHT |
| L2 | `none` gene_alpha 0.028-0.040, signal_entropy above 1.99 | 0.0326, 1.9965 | RIGHT |
| L3 | `base` signal_entropy 1.65-1.78 at year 10,000 | 1.654 (flat since 7,000, slope t = -0.6) | RIGHT, at the edge |
| L4 | `base` bank_gap 0.20-0.35 | 0.173 | WRONG |
| L5 | `base` population 1,150-1,260; max_generation 2,400-3,000 | 1,198; 2,462 | RIGHT |
| L6 | dialect_jsd ordered base < ford1 < wall at every checkpoint from 2,000 | ordered at only 2 of the nine 1,000-year checkpoints (9,000 and 10,000), all inside noise | WRONG |
| L7 | `wall` above 0.10 at year 10,000 | 0.0130 (t = 0.98 vs base 0.0098); no seed above 0.10 | WRONG |
| L8 | No seed extinct in any of the four arms | none; smallest population 318 | RIGHT |
| L9 | 64 processes within 5% of 20.15 years/s | 15.56, 23% slower | WRONG |

## E3 final, year 5,000 (1:20 am, 13 October)

| | base (3 fords) | ford1 | wall |
|---|---|---|---|
| crossings a year | 193 | 62 | 0 |
| dialect_jsd | 0.0086 | 0.0090 (t = -0.15) | 0.0083 (t = 0.12) |
| bank_gap | 0.253 | 0.216 | 0.255 |
| signal_entropy | 1.739 | 1.753 | 1.790 (t = -1.7) |
| favourite signal = silence, W / E | 0.80 / 0.79 | | 0.75 / 0.76 |

E3 falsifier "wall staying below 0.01" TRIGGERED at 0.0083; falsifier "ford1 above 0.2" not triggered.
L6 (ordering base < ford1 < wall at every checkpoint from 2,000) is WRONG already: not ordered at any of
2,000 to 5,000. Mechanism: silence is the favourite signal of three-quarters or more of agents on both
banks in both worlds; the three spoken symbols cost the same and carry no distinct meaning, so there is
no convention for isolation to split. Correlation of jsd with bank gap across 48 seeds r = -0.01, with
smaller-bank size r = 0.07: the interim dominance reading does not survive.

## E3 interim, year 2,000 (10:25 pm, 12 October). Superseded by the final block above.

| | base (3 fords) | ford1 | wall | |
|---|---|---|---|---|
| crossings a year | 232 | 88 | 0 | as built |
| dialect_jsd | 0.0060 | 0.0020 (t = 2.1) | 0.0042 (t = 0.9) | NOT ordered base < ford1 < wall |
| bank_gap | 0.268 | 0.185 | 0.136 (t = 3.4) | isolation BALANCES the banks |
| signal_entropy | 1.828 | 1.857 | 1.873 (t = -2.9) | contact makes signalling MORE structured |
| ecology_entropy | 4.81 | 5.13 (t = -2.4) | 5.07 (t = -2.1) | less contact, more behavioural variety |
| smallest bank ever, wall | | | 318 | no bank lost in any seed |

Reading so far: cutting the river off does not breed dialects by year 2,000; the isolated world's banks
differ LESS than the connected world's. The E3 falsifier written before the runs ("wall staying below
0.01: signals are driven by terrain and season, not by contact") is currently triggered at 0.0042. The
connected world's larger bank difference rides on its bank imbalance: one bank's inheriting lineage
dominates and spills across the fords. Whether drift eventually separates the isolated banks is what
years 2,000 to 10,000 are for.
