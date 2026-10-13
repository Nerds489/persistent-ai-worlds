## 11. The six experiments, run

Section 7 set out six experiments and asked for a prediction before each one. This section runs all six
on the desktop and keeps that bargain. Twenty-nine numbered items, twenty-six predictions and three falsifiers scored with the predictions they guard, were written into `_build/experiment-s7/predictions.md` and timestamped before the first world existed, and
two more blocks were added before later runs began; Section 11.8 scores all of them without editing
them, and two were dead before the first condition finished.

Nine conditions, sixteen seeds each, one change against the defaults. Section 6 ran four seeds for 300
years on the laptop; this is sixteen seeds for 2,000 years, with the four conditions that were still
moving or still unanswered carried on to 10,000 (Section 11.7), on the machine the paper was written
for. In all, 800,000 seed-years.

**Table 7.** The nine conditions. Anything not named is at the stock default: 96 × 96 cells, 30,000
energy units, a 2,000-agent cap, learning inherited in full, events on.

| Condition | Change | Experiments it serves | Years |
|---|---|---|---|
| `base` | none | E1, E2, E4, E5 baseline; E3's three-ford arm | 10,000 |
| `none` | `--inherit none` | E1, E2 | 10,000 |
| `half` | `--inherit half` | E1, E2 | 2,000 |
| `calm` | `--no-events` | E4 | 2,000 |
| `e20k` | `--energy 20000` | E5 | 2,000 |
| `e45k` | `--energy 45000 --capacity 3000` | E5 | 2,000 |
| `big` | `--size 128 --energy 53000 --capacity 3500` | E6 | 2,000 |
| `ford1` | one ford instead of three | E3 | 10,000 |
| `wall` | no fords at all | E3 | 10,000 |

Two notes on that table. The agent cap is a guard rail rather than a treatment: it sits at about twice
the expected population in `base`, and it is scaled with the energy in `e45k` and `big` so that it stays
equally far from binding instead of quietly capping one arm and not the others. And the two river arms
run from copied folders, `_build/experiment-s7-ford1` and `-wall`, each differing from the kit by
exactly one line, as Section 7 instructs; their terrain was checked before they ran, giving 27 ford
cells with three fords, 9 with one and 0 with none.

### 11.1 The desktop, measured

Section 5.2 estimated the desktop's throughput from the laptop's and said to treat it as a guess. It was
a good guess.

**Table 8.** Throughput: the Section 5.2 estimate against sixteen seeds actually run.

| | Laptop, measured | Desktop, estimated in Section 5.2 | Desktop, measured here |
|---|---|---|---|
| All cores busy, one condition | 0.32 years/s per process, 8 processes | about 1.1 years/s per process, 16 processes | **1.095 years/s per process** (range 1.06 to 1.15), 17.5 years/s in total |
| Two conditions at once, 32 processes | | not estimated | 0.630 years/s per process, **20.15 years/s in total** |
| 16 seeds × 1,000 years | about 1.7 hours | about 15 minutes | **15.2 minutes** |
| 16 seeds × 2,000 years | | | 31 minutes 23 seconds, wall clock |
| 16 seeds for a week | | about 700,000 simulated years each | about 662,000 |
| Temperature, all cores busy | | under 85 °C wanted | 49 to 51 °C |

The estimate was good to 0.5% on the figure that matters. The chip never came close to
needing `JOBS=12`: sixteen busy cores held it at about 50 °C, 35 degrees under the comfort line in
Section 5.3, and thirty-two held it at the same temperature. Memory was never a factor either.

**The second thread is worth 14%, which is more than "little".** Section 5.1 sets `JOBS` to `nproc / 2`
on the grounds that "the second thread of each core adds little to NumPy work like this". Measured
directly, with two conditions running and one of them frozen with `SIGSTOP` for the comparison window
rather than killed, over matched 180-second windows at the same simulated years:

| Processes | Aggregate |
|---|---|
| 16, one condition | 17.688 years/s |
| 32, two conditions | 20.153 years/s |
| 64, four conditions | 15.56 years/s |

A gain of 1.139. The direction of Section 5.1's claim is right, since doubling the processes buys 14%
rather than anything like 100%, and any single condition still finishes fastest on sixteen. But the
practical reading is different from the one the launcher implies. A condition has only sixteen seeds,
so the choice is never "16 jobs or 32" for one condition; it is whether to run a second condition
alongside it or queue it behind. **Two conditions run together finish about 12% sooner than the same two run one after the other**, at the cost of each individual seed running 43% slower, so taking 74% longer. Over a week that is most
of a day. The experiment programme in this section used it: `ford1` and `wall` were run side by side.

**And past the thread count it goes backwards.** Four conditions at once, 64 processes on 32 threads,
ran at 15.56 years a second: slower than 32 processes by a quarter and slower even than sixteen. Each
process carries about 77 MB of Q-tables, so 64 of them ask the caches and memory bus for five gigabytes
of working set at once, and time-slicing makes it worse. The rule for this machine is one process per
logical thread, never more: two conditions at a time, and a queue for the rest.

**The world is reproducible across machines.** Section 6's runs were made on the laptop, and their own
logs say "4 at a time", which is `nproc / 2` on a 4-core i7-8665U. Running `base` here regenerates seeds
1 to 4 of that same condition from scratch on the 5950X, and for all 300 years the two machines agree on
every one of the 24 columns of `log.csv`, byte for byte, with a single exception: `energy_drift`, the
floating-point residue of the conservation check, which differs in its last digits and reaches the same
9.78 × 10⁻⁹ maximum. A seed is a world, on either machine. That is what makes the rest of this section
legitimate rather than merely new: the 2,000-year arms here begin by reproducing the 300-year arms
there, and the Section 6 figures can be read as the first 300 years of Figure 4.

One correction while the machine is in view: Table 1 gives the kernel as 6.17, and this desktop runs
7.0.0-38-generic. Mint 22.3 and Python 3.12 are right.
