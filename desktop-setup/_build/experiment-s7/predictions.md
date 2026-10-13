# Section 7 experiments: predictions, written before the runs started

11 October 2026, 14:04 AWST. Written and timestamped **before** any of the runs below existed, because
Section 7.1 says so: emergence only means something against a prediction, and a prediction is only a
prediction if it could have been wrong.

## The machine

One point of order first. The paper says its measured numbers come from "the laptop this paper was
built on", and Table 1 describes the desktop as a target with estimated numbers. That is wrong. The
box these runs are on, and the box the Section 6 runs were on, reports:

| Check | Value |
|---|---|
| CPU | AMD Ryzen 9 5950X, 16 cores / 32 threads |
| Memory | 62 GiB usable |
| DMI chassis type | 3 (desktop) |
| Board | Gigabyte B550M DS3H AC |
| Batteries in `/sys/class/power_supply/` | none |
| OS | Linux Mint 22.3 (Zena) |
| Kernel | 7.0.0-38-generic (Table 1 says 6.17) |
| Python | 3.12.3, NumPy 1.26.4, no venv needed |

So this is the desktop of the title, and Section 6 was measured on it, not on a laptop. The new
section will say so and Table 1's kernel will be corrected.

## Baseline: what Section 6 actually measured

Means across 4 seeds, last 50 of 300 years, from `_build/experiment/runs/`. Every prediction below is
anchored to these, and the Section 6 runs are left untouched.

| Column | inherit copy (base) | inherit none |
|---|---|---|
| population | 1012 ± 48 | 1024 ± 53 |
| mean_energy | 0.476 | 0.466 |
| max_generation | 116 | 77 |
| gene_repro | 21.51 | 21.29 |
| gene_lifespan | 3178 ± 515 | 3213 ± 625 |
| gene_alpha | 0.186 | 0.049 |
| gene_eps | 0.0409 | 0.0177 |
| q_states | 137 | 65 |
| policy_complexity | 19.83 | 18.04 |
| signal_entropy | 1.961 | 1.998 |
| dialect_jsd | 0.00058 | 0.00014 |
| novelty | 0.025 | 0.040 |
| ecology_entropy | 6.07 | 4.30 |
| change | 0.359 | 0.199 |
| archive_size | 738 | 601 |
| crossings | 320 | 317 |
| pop_west / pop_east | 582 / 430 | 518 / 506 |
| nutrients / detritus | 4524 / 24,970 | 4284 / 25,220 |

Two facts from that table drive several predictions. Agents hold almost nothing: 1012 agents at a mean
body energy of 0.48 is about 480 of the 30,000 units, and 25,000 units sit in detritus. The world is
therefore limited by how fast detritus decays back into nutrients, not by how much energy exists. And
`gene_repro` has settled at 21.5 against a hard floor of 20, so it has nowhere left to fall.

## Conditions

Nine conditions, 16 seeds each, one change against the defaults (size 96, energy 30,000, capacity 2000,
inherit copy, events on).

| id | Change | Serves |
|---|---|---|
| `base` | none | E1, E2, E4, E5 baseline; E3 three-ford arm |
| `none` | `--inherit none` | E1, E2 |
| `half` | `--inherit half` | E1, E2 |
| `calm` | `--no-events` | E4 |
| `e20k` | `--energy 20000` | E5 |
| `e45k` | `--energy 45000 --capacity 3000` | E5 |
| `big` | `--size 128 --energy 53000 --capacity 3500` | E6 |
| `ford1` | one ford, code edit in a copied folder | E3 |
| `wall` | no fords, code edit in a copied folder | E3 |

Capacity is scaled with energy in `e45k` and `big` so the hard agent cap stays as far from binding as it
is in `base` (2000 against about 1000 agents). The cap is a guard rail, not a treatment: letting it bind
in one arm only would confound the comparison. Everything else is the stock kit, byte for byte, and the
two ford arms differ from it by exactly one line each (verified: two diff lines per copy).

## E1. Does handing learning down help?

1. **Survival does not care.** `population` differs by less than 10 per cent across `copy`, `half` and
   `none`, with |t| < 2 for every pairwise comparison. Inheriting learning changes what agents are, not
   how many the world holds.
2. **Knowledge is strictly ordered.** `q_states` comes out `copy` > `half` > `none`, every pairwise
   |t| > 4. At 2,000 years: `copy` between 140 and 220, `half` between 85 and 140, `none` between 58 and 78.
3. `policy_complexity` in `copy` exceeds `none` by at least 1.3 of its 20 points, with `half` between.
4. **Falsifier:** `none` reaching a `q_states` mean above 90, or `half` landing outside the other two.

## E2. Does evolution tune how agents learn (the Baldwin effect)?

1. **The gap widens with time.** At 300 years `gene_alpha` was 0.186 against 0.049. At 2,000 years I
   predict `copy` at or above 0.20 and `none` at or below 0.055, |t| > 4.
2. `gene_eps` also separates, `copy` above 0.035 and `none` below 0.025, |t| > 3.
3. `half` sits between on both genes, and closer to `copy` than to `none` on `gene_alpha`.
4. **The mechanism claim:** evolution turns learning *down* when learning is not passed on, because a
   lifetime's learning that dies with the agent is pure metabolic cost.
5. **Falsifier:** `gene_alpha` in `none` rising above 0.10, or the two conditions converging rather than
   separating further between year 300 and year 2,000.

## E3. Is the river a barrier to culture?

The paper's own worked example predicts "with three fords `dialect_jsd` stays under 0.05; with one ford
it climbs above 0.2 within 2,000 years". I think the first half is right and the second half is wrong by
about two orders of magnitude, and I am saying so before the runs.

1. `base`, three fords, 5,000 years: `dialect_jsd` stays below **0.005**, not merely below 0.05.
2. `ford1`: `crossings` falls to between 60 and 160 a year (from 320). `dialect_jsd` rises to more than
   three times `base` but **stays below 0.05**. The paper's 0.2 is not reached by year 2,000.
3. `wall`: `crossings` is exactly 0 in every seed and every year. `dialect_jsd` exceeds 0.05 by year
   2,000. The banks drift apart demographically: |pop_west - pop_east| / population above 0.25 in at
   least half the 16 seeds.
4. No seed goes extinct in any arm; at most 2 of 16 `wall` seeds lose one bank completely.
5. **Falsifier:** `ford1` above 0.2 (the paper is right and I am wrong), or `wall` staying below 0.01
   (signals are driven by terrain and season, not by contact, and the river is not a cultural barrier
   at all).

## E4. Does disturbance keep the world interesting?

1. `calm` logs exactly 0 events, against roughly 150 per 300 years in `base`.
2. `ecology_entropy` in `calm` is lower than `base` by at least 0.3 bits, and `archive_size` by at least 50.
3. `change` in `calm` is lower than `base` by at least 0.05.
4. `population` in `calm` is 2 to 8 per cent **higher** than `base`: fire and drought cost agents energy
   they would otherwise have eaten.
5. **A prediction about the instrument, not the world:** `novelty` will *not* separate the conditions,
   |t| < 2, because it has already fallen to 0.025 a year by year 300 as the 2,048-cell descriptor space
   fills. Section 7.2 says as much; this is the test of it. If `novelty` does separate the conditions at
   2,000 years, that measure is better than the paper gives it credit for.

## E5. Starvation or crowding?

1. **Population is sub-proportional to energy**, because the extra energy mostly ends up in the detritus
   pool rather than in bodies. `e20k` lands between 0.72x and 0.85x `base`; `e45k` between 1.15x and
   1.40x `base`, that is strictly below the 1.5x that proportionality would give.
2. `gene_repro` stays between 20.5 and 22.5 in all three arms, |t| < 3 for every pair: it is pinned
   against its floor of 20 and more energy does not move it.
3. `mean_energy` rises with total energy but stays below 1.0 in all three arms.
4. `gene_lifespan` does not order cleanly, |t| < 2, because its across-seed spread (±515 at 300 years) is
   larger than any effect energy has on it.
5. **Falsifier:** `e45k` population at or above 1.5x `base` (the world is simply energy-limited and my
   detritus-sink reading is wrong), or `gene_repro` moving outside 20.5 to 22.5.

## E6. Does a bigger world sustain more variety?

1. `archive_size` in `big` exceeds `base` by at least 15 per cent, and `ecology_entropy` by at least
   0.2 bits.
2. `dialect_jsd` in `big` is at least twice `base`: the river is longer and the three fords are further
   apart in absolute terms.
3. `population` lands between 1.4x and 1.9x `base` (1.78x the cells and 1.78x the energy).
4. **Falsifier:** `archive_size` failing to rise, which would say the 2,048-cell descriptor ceiling, not
   the world, is what bounds the measured variety.

## Throughput

A single process ran 0.99 simulated years a second in the Section 4 smoke test, and 8 processes ran 0.32
each over 300 years. With 16 processes on 16 physical cores I predict an aggregate of 3 to 5 simulated
years a second, so 16 seeds x 2,000 years in 1.8 to 3.0 hours per condition.

---

## Correction, 14:12 AWST, before any result was read

The "The machine" section above is wrong, and the paper was right. I had concluded that Section 6 was
measured on this box. The evidence says otherwise, and it was in the run logs the whole time:

- `run_seeds.sh` sets `JOBS=nproc/2`. The Section 6 logs say **"(4 at a time)"**, so `nproc` was 8 on the
  machine that produced them. This box reports `nproc` 32 and the new runs say "(16 at a time)".
- Section 5.2 names the build machine outright: an **i7-8665U**, 4 cores and 8 threads. That matches.
- The first 134 years of the new runs measure **1.15 simulated years a second per process with 16
  processes**, against the 0.32 the laptop managed with 8. A single machine does not get 3.6 times
  faster per process when you double the number of processes on it.

So: the paper was built and Section 6 measured on the i7-8665U laptop, and this box is the 5950X desktop
of the title. The one real defect left in Table 1 is the kernel, given as 6.17 against this machine's
**7.0.0-38-generic**; Mint 22.3 and Python 3.12 are right.

**And my throughput prediction is already wrong.** I predicted 3 to 5 simulated years a second in
aggregate; the measured figure is about **18.4** (16 processes x 1.15). I extrapolated from the laptop's
all-cores figure instead of from Section 5.2's own estimate for the desktop, which said "about 1.1
years/s per process, 16 processes" and was very nearly exact. Table 3's estimate column can become a
measured column.

Everything above the line stands as pre-registered. Nothing in it has been edited.

---

## A second pre-registration, 16:35 AWST, with `e45k` still running

`e20k` has landed and `e45k` has not. The `e20k` result suggests a mechanism, and a mechanism is only
worth anything if it predicts the arm that has not finished, so this is written now.

Removing 10,000 energy units from the world between `base` and `e20k` took:

| Pool | Change | Standing value |
|---|---|---|
| Detritus | -9,780 | 24,913 to 15,133 |
| Agent bodies | -233 | 519 to 286 |
| Nutrients on land | +14 | 4,544 to 4,558 |

The standing crop on land does not move: 0.5350 units a land cell in `base`, 0.5366 in `e20k`. The land
is grazed to the same density whatever the world contains, all spare energy is stored as detritus, and
the population is set by the size of the detritus reservoir rather than by the total.

If that is right, `e45k` at year 2,000 should show:

1. **Nutrients within 2% of 4,550**, and a standing crop within 2% of 0.535 a land cell.
2. **Detritus about 39,000**, absorbing nearly all of the extra 15,000.
3. **Population between 1,600 and 2,000.** The straight line through `e20k` and `base` is
   population = 0.0567 x energy - 550, which gives 2,002; the arm is capped at 3,000 agents, so the cap
   cannot be what stops it.
4. **`mean_energy` below `base`'s 0.451**, continuing to fall as the world is given more energy, because
   a denser population shares the same standing crop.

Falsifier for the lot: nutrients rising with the world's total energy, which would mean the land is not
grazed to a fixed point and the detritus-reservoir reading is wrong.

---

## A third pre-registration: the 10,000-year runs, 12 October 2026, 21:44 AWST

Four conditions go on to year 10,000: `base`, `none`, `ford1` and `wall`. Chosen because they were the
ones still moving or still unanswered: over years 1,500 to 2,000, `base` signal entropy was still falling
(trend t = -3.2) and its population still rising (t = 2.7); `ford1` and `wall` are E3, unfinished; `none`
is the control without which the learning-rate question cannot be read. `half`, `calm`, `e20k`, `e45k`
and `big` were flat or settled and stop at 2,000. Written before any of the four has run past its
current year (`base` and `none` at 2,000, `ford1` at 968-1,019, `wall` at 764-818).

**The Baldwin question.** The learning-rate ratio, `copy` over `none`, went 3.7 at year 300, 2.5 at
1,000, 2.1 at 1,500, 1.7 at 2,000.

1. **The gap closes.** At year 10,000 the ratio is between 1.0 and 1.4, and copy against none on
   `gene_alpha` no longer clears |t| = 3. If it is still above 1.4 with |t| > 3, inheriting learning has
   a permanent effect on how this world learns; if it closes, the Section 6 result was a transient.
2. `none` stays flat: `gene_alpha` within 0.028 to 0.040, `signal_entropy` above 1.99.

**Signalling and the banks, `base`.**
3. `signal_entropy` keeps falling, to between 1.65 and 1.78 bits at year 10,000 (1.828 at 2,000).
4. `bank_gap` stays between 0.20 and 0.35 (0.268 at 2,000, trend flat).
5. `population` between 1,150 and 1,260; `max_generation` between 2,400 and 3,000.

**E3, the river.** E3.1 to E3.5 above stand as written. Two additions for the long horizon:
6. Ordering `base` < `ford1` < `wall` on `dialect_jsd` at every checkpoint from year 2,000 on.
7. `wall` above 0.10 at year 10,000.

**Survival.** 8. No seed goes extinct in any of the four arms in 10,000 years.

**Throughput.** 9. All four together is 64 processes on 32 threads. The second thread is already used
at 32, so the aggregate stays within 5% of the measured 20.15 years a second, and the whole run takes
7 to 8 hours.
