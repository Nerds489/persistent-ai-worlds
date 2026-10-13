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
### 11.2 E1 and E2: should learning be inherited?

![Figure 4. Three inheritance rules over 2,000 simulated years, sixteen seeds each. Bold lines are the mean of the sixteen; faint lines are the individual seeds. The learning-rate gap that Section 6 measured at year 300 is real, and it is narrowing. The middle rule is not a middle world.](figures/fig-s7-inherit.svg)

**Table 9.** The last 100 years of each arm at year 2,000, mean of sixteen seeds (± standard error),
with Welch's *t* for `copy` against `none`.

| Measure | `copy` | `half` | `none` | *t* |
|---|---|---|---|---|
| Population | 1,151 ± 9 | 1,102 ± 6 | 1,105 ± 6 | 4.2 |
| Learning rate (gene, started at 0.2) | 0.061 ± 0.004 | 0.033 ± 0.001 | 0.033 ± 0.001 | 6.4 |
| Exploration rate (gene, started at 0.1) | 0.031 ± 0.002 | 0.045 ± 0.002 | 0.015 ± 0.001 | 9.2 |
| Situations met (of 240) | 135.1 ± 3.6 | 136.1 ± 3.5 | 66.4 ± 0.2 | 19.0 |
| Policy complexity (of 20) | 19.78 ± 0.04 | 18.96 ± 0.01 | 18.14 ± 0.01 | 41.0 |
| Deepest lineage (generations) | 540 ± 16 | 461 ± 9 | 382 ± 8 | 8.6 |
| Signal entropy (bits; 2.0 = random) | 1.828 ± 0.013 | 1.806 ± 0.006 | 1.9968 ± 0.0001 | −13.3 |
| Bank imbalance (\|west − east\| / population) | 0.268 ± 0.027 | 0.065 ± 0.012 | 0.053 ± 0.012 | 7.3 |
| Difference between the banks' signals (`dialect_jsd`) | 0.0060 ± 0.0018 | 0.00046 ± 0.00007 | 0.00016 ± 0.00001 | 3.2 |
| Behaviour diversity (`ecology_entropy`, bits) | 4.81 ± 0.09 | 3.95 ± 0.04 | 4.12 ± 0.04 | 6.7 |
| Crossings a year | 232 ± 16 | 280 ± 9 | 319 ± 17 | −3.7 |
| Lifespan (gene, started at 1,200 ticks) | 3,712 ± 48 | 3,891 ± 26 | 3,888 ± 41 | −2.8 |
| Energy to reproduce (gene, started at 70) | 21.41 ± 0.02 | 21.22 ± 0.01 | 21.17 ± 0.01 | 13.5 |
| Distinct behaviours ever seen (of 2,048) | 751 ± 31 | 672 ± 34 | 671 ± 33 | 1.8 |

**The Section 6 result survives, and shrinks.** Learning is still turned down when it is not passed on,
at sixteen seeds and 2,000 years, with *t* = 6.4. But the size of the effect is a property of when you
look at it. Both arms fall; the inherited one just falls later:

Values in the stated year, mean of sixteen seeds; Tables 9 and 14 use the mean of the last 100 years instead.

| Simulated year | 10 | 50 | 100 | 300 | 500 | 1,000 | 1,500 | 2,000 |
|---|---|---|---|---|---|---|---|---|
| `copy` | 0.195 | 0.222 | 0.214 | 0.157 | 0.143 | 0.084 | 0.068 | 0.057 |
| `none` | 0.174 | 0.094 | 0.080 | 0.042 | 0.041 | 0.034 | 0.032 | 0.033 |
| ratio | 1.1 | 2.4 | 2.7 | 3.7 | 3.5 | 2.5 | 2.1 | 1.7 |

The ratio peaks near year 300, which is exactly where Section 6 stopped, and decays to 1.7 by year
2,000. The front page of this paper quotes "0.18 vs 0.05 after 300 years"; that is true and it is the
high-water mark. At 2,000 years the inheriting world's learning rate, 0.057, has fallen to between where the blank-slate world stood at years 100 and 300 (0.080 and 0.042). Section 6 called the result "a result to test on sixteen seeds
and longer runs, not a law", and this is what testing it did: the direction held, the magnitude did not.
Carried on to year 10,000 (Section 11.7), the ratio keeps falling, to 1.20, and drops inside seed noise.

**A halfway rule is not a halfway world.** `half` was added as E1's third arm on the assumption that it
would land between the other two. It does not land anywhere consistent. It matches `copy` on situations
met (*t* = −0.20) and on signal entropy (*t* = 1.6); it matches `none` on the learning-rate gene
(*t* = 0.17) and on bank imbalance (*t* = 0.69); and on exploration and behaviour diversity it is
outside the range of both, with the highest exploration of the three arms and the lowest diversity.
Only policy complexity and lineage depth order the three arms monotonically.

The reason is in one line of `river_world.py`:

```python
elif self.inherit == "half":
    self.Q[ch], self.visited[ch] = 0.5 * self.Q[p], self.visited[p]
```

`half` does not give a child half of its parent's table. It gives the whole visited mask and every value
halved, and the halving compounds down the generations. Reading all forty-eight year-2,000 checkpoints:

**Table 10.** What an agent actually carries at year 2,000, mean of sixteen seeds (± standard error).

| Arm | Visited states (of 240) | Mean \|Q\| over visited states | Mean best Q | Share of visited cells still exactly 0 |
|---|---|---|---|---|
| `copy` | 135.1 ± 3.6 | 0.4476 ± 0.018 | 3.044 ± 0.21 | 0.360 ± 0.017 |
| `half` | 136.1 ± 3.5 | 0.00390 ± 0.00016 | 0.4469 ± 0.008 | 0.408 ± 0.015 |
| `none` | 66.35 ± 0.21 | 0.00617 ± 0.00016 | 0.3428 ± 0.0061 | 0.698 ± 0.001 |

A `half` agent claims to have met more situations than a `copy` agent and holds values 115 times
weaker, weaker even than what a blank-slate agent learns for itself in one life. Halving preserves
which action is best, so the parent's policy does transmit, which is why signalling still becomes
structured; it does not preserve how strongly that action is preferred, and after hundreds of
generations of halving the preference is worth less than a single reward. Evolution reads that
correctly and tunes the learning rate as if nothing were inherited.

> **`q_states` is not a measure of inherited knowledge.** Table 6 notes that inherited visits count under `copy` and `half` alike;
> under `half` the flag outlives the knowledge entirely. Anyone using `q_states` to compare inheritance rules should read Table 10 first, or use
> `policy_complexity`, which does order the three arms.

**Section 6's table replicates at sixteen seeds.** Read at year 300, the arms here give a learning rate
of 0.162 ± 0.013 against 0.043 ± 0.002, where four seeds gave 0.186 ± 0.033 against 0.049 ± 0.005; and
situations met of 136.2 against 65.3, where four seeds gave 137 against 65. The four-seed numbers were
right; sixteen seeds mostly tightened them, and lifted *t* on the learning rate from 4.1 to 8.9.

**Two things Section 6 did not report, and both grow with time.** Neither is new at year 2,000, and
that is the point: each was already measurable at year 300 and each is several times larger by the end.

- **Inherited learning makes signalling structured.** Signal entropy under `copy` falls from 1.9598
  bits at year 300 to 1.828 at year 2,000, while `none` sits at 1.9976 and then 1.9968, four
  ten-thousandths off a perfectly random 2.0 and never moving. The gap widens from 0.038 bits to 0.169,
  with *t* going from −9.6 to −13.3. A blank-slate world never leaves random signalling, because
  nothing about how to signal survives its user.
- **Inherited learning makes the banks fill unevenly.** The imbalance between the banks under `copy`
  runs 0.187 of the population at year 300 and 0.268 at year 2,000, against 0.049 and 0.053 under
  `none`, *t* = 4.4 then 7.3. Which bank wins is seed-dependent (seed 7 ends 845 west to 327 east, seed
  12 ends 418 to 773), and nothing in the code favours a bank. It is the compounding of one bank's
  inherited tables, and it is absent in both arms where inheritance is effectively switched off.

Finally, a result that only sixteen seeds could reach: population does separate. 1,151 against 1,105,
*t* = 4.2. Four seeds a side could not see a 4% difference and Section 6 reported none; the energy
budget still sets the order of magnitude, but inherited learning is worth about forty agents.
### 11.3 E3: is the river a barrier to culture?

![Figure 5. The river experiment, sixteen seeds an arm over 5,000 simulated years. The three worlds differ by one line of code, the number of fords. Crossings fall from about 200 a year to about 60 to none, and the difference between the banks' signalling does not move with them.](figures/fig-s7-river.svg)

No. Cutting the river off completely leaves the two banks signalling exactly as alike as they do with
three fords open.

The three arms are the defaults with three fords (`base`), one ford (`ford1`) and none (`wall`), each a
one-line edit of `self.fords` in a copied folder, sixteen seeds a side, scored at year 5,000 as
pre-registered.

**Table 11.** E3 at year 5,000: the mean over years 4,901 to 5,000, sixteen seeds an arm, with Welch's
*t* against `base`.

| | three fords | one ford | *t* | no fords | *t* |
|---|---|---|---|---|---|
| Crossings a year | 193 | 62 | 7.7 | 0 | 13.1 |
| `dialect_jsd`, bits | 0.0086 | 0.0090 | −0.15 | 0.0083 | 0.12 |
| Bank imbalance, \|west − east\| / population | 0.253 | 0.216 | 0.85 | 0.255 | −0.03 |
| Seeds with imbalance above 0.25 | 8 of 16 | 7 of 16 | | 6 of 16 | |
| Signal entropy, bits | 1.739 | 1.753 | −0.52 | 1.790 | −1.72 |
| Behaviour diversity, bits | 4.27 | 4.27 | 0.04 | 4.48 | −1.09 |
| Population | 1,177 | 1,198 | −1.46 | 1,180 | −0.22 |
| Smallest bank in any year, any seed | 153 | 135 | | 141 | |

The treatment worked as built: the walled world logged zero crossings in every seed and every one of its
80,000 seed-years, and one ford cut traffic to a third. Nothing downstream of the treatment followed it.
The between-bank divergence is 0.0086, 0.0090 and 0.0083 bits, *t* = 0.12 for complete isolation against
open fords. The arms never order the way contact would predict. Checked every 500 years from 2,000 on, the
walled world is the highest of the three at one of the seven checkpoints (4,000) and the lowest at
three (3,000, 3,500 and 5,000); the one-ford world is the lowest at 2,000, 2,500 and 4,000 and the
highest at 4,500 and 5,000. Every arm drifts upward together, from about 0.001 at year 500 to about 0.009 at
5,000, which is a property of the world ageing, not of its geography.

The interim reading at year 2,000 had found the connected world's banks differing
*more* than the isolated ones, and read it as one bank's inheriting lineage dominating and spilling
across the fords. By 5,000 that difference has gone and so has the link: across all 48 seeds, a seed's
bank imbalance and its divergence are uncorrelated (*r* = −0.01), and so are its divergence and the size
of its smaller bank (*r* = 0.07). The interim gap was seed noise of the kind 16 seeds a side produces at
*t* = 2.

**Why there is nothing for isolation to separate.** The answer is in what the agents say, and mostly it
is nothing. Reading the final world state of every seed, the agent's favourite signal over its last
year is silence for 79 to 80% of agents on both banks with three fords open, and 75 to 76% on both banks
with none. The other three symbols split the rest almost evenly, 5 to 9% each, on both banks of both
worlds. Speaking costs 0.05 energy a tick whichever symbol is used and silence costs nothing, so selection
pushes every population towards silence identically, and among the three spoken symbols there is
nothing to choose: they cost the same and the model gives no one of them a meaning the others lack. A
dialect needs an arbitrary convention for two isolated populations to settle on differently. This
channel has a cost gradient instead, and a cost gradient points the same way on both banks. Signal
entropy falls steadily in every arm (from 2.0 at year 1 to about 1.75 at 5,000) as the channel goes
quiet, and it falls slowest in the walled world, *t* = −1.7 by 5,000: if anything, contact speeds the
drift into silence.

What `dialect_jsd` measures in this world, then, is the sampling wobble of two near-identical, mostly
silent distributions. The largest value any seed reached in any single year of any arm was 0.074, and
that in the walled world; the paper's threshold of 0.2 was never approached.

**Against the paper's own worked example.** Section 7 predicted "with three fords `dialect_jsd` stays
under 0.05; with one ford it climbs above 0.2 within 2,000 years". The first half holds by a factor of
six. The second is wrong by a factor of a hundred: one ford stood at 0.0020 at year 2,000, below the
three-ford world, and its single highest seed-year in 5,000 years was 0.052. The pre-registered
falsifier for the river as a barrier, "`wall` staying below 0.01: signals are driven by terrain and
season, not by contact", is triggered at 0.0083, and the reading it names is the right one, sharpened:
signals here are driven by their cost.

The experiment worth running next is the one that gives the channel something to diverge on. Make the
three spoken symbols carry different information (one heard as "food here", say, by tying it to a
nutrient threshold in `observe`) or make a symbol's use pay only when a neighbour answers in kind, and
then compare `wall` against `base`. Until the model has a convention to break, isolating its banks
cannot break one. Whether ten thousand years of drift changes that verdict for the river arms is in
Section 11.7.
### 11.4 E4: does disturbance keep the world interesting?

![Figure 6. Disturbance, energy and size, sixteen seeds an arm over 2,000 simulated years. Top left: switching fires, floods and droughts off changes nothing measurable (11.4). Top right and bottom left: population tracks total energy more than proportionally while the nutrients standing on the land do not move at all (11.5). Bottom right: a world nearly twice the size explores barely more behaviours (11.6).](figures/fig-s7-world.svg)

No. Not as the three disturbances are currently sized.

`calm` is the defaults with `--no-events`. Against `base` at year 2,000, sixteen seeds a side, every
measure in the log falls inside seed noise. The largest |*t*| among the twenty-two columns is 1.9, and
the two that come closest both point the wrong way for the hypothesis: the calm world has slightly
*more* behaviour diversity (5.00 against 4.81 bits, *t* = −1.6) and slightly *more* structured
signalling (1.859 against 1.828 bits, *t* = −1.9). Population, lineage depth, the five genes, the
archive and `change` are all flat. The only column that separates is the treatment itself: 1,037 events
in 2,000 years against 0.

That is a negative result, so it is worth showing that the instrument was not asleep. Two checks inside
`base` itself:

- **Years with an event look like years without.** Over years 500 to 2,000 and sixteen seeds, the annual
  change in population averages +0.060% in the 12,485 year-slots carrying an event and −0.029% in the
  11,515 that do not, with standard deviations of 1.540 and 1.536.
- **Events add no volatility.** The standard deviation of the annual change, `base` against `calm`:
  population 1.537 against 1.521, nutrients 2.287 against 2.252, detritus 0.417 against 0.406, mean
  energy 6.407 against 6.291. Ratios of 1.01 to 1.03. The two columns that move at all, `q_states` at
  1.19 and signal entropy at 1.11, are the smallest numbers on the list in absolute terms.

The reason is arithmetic, and it is in the pools the events touch. A fire burns a disc of radius 6, so
about 113 of the world's 8,520 land cells. It moves the nutrients under that disc into detritus, about
60 of the 4,544 units on land, which decay back at 5% a tick; and it takes half the body energy of the
agents standing in it, about fifteen agents holding about 0.45 each, so roughly 3 units. Floods and
droughts change erosion, flow and deposition for 40 and 100 ticks, and all three of those act on the
river's load, which holds **24 units of the world's 30,000**. Every disturbance in the model is working
on 0.1% of the world's energy, in a world where 25,000 of the 30,000 units sit in
detritus and are rained back onto the land continuously.

So E4's question is not answered by this run; it is deferred until the disturbances are large enough to
answer it. A rerun worth doing on the desktop: scale fire's radius with the world (radius 20 burns 12%
of the land rather than 1.3%), make drought suppress decomposition rather than river flow, since
decomposition is the pipe the whole world feeds through, and only then compare against `calm`. The
prediction to write first is the one this run can already falsify: that a disturbance confined to 0.1%
of the energy budget cannot move a population of 1,100.
### 11.5 E5: starvation or crowding?

Neither. The land is grazed to the same standing crop whatever the world contains, and everything else
is stored as detritus.

**Table 12.** Three worlds differing only in how much energy they hold, at year 2,000, mean of sixteen
seeds (± standard error), with Welch's *t* against `base`.

| Measure | `e20k` (20,000) | *t* | `base` (30,000) | `e45k` (45,000) | *t* |
|---|---|---|---|---|---|
| Population | 584 ± 5 | 54.5 | 1,151 ± 9 | 2,066 ± 22 | −39.2 |
| Nutrients on land | 4,558 ± 18 | −0.4 | 4,544 ± 33 | 4,610 ± 29 | −1.5 |
| Standing crop a land cell | 0.5350 | | 0.5334 | 0.5411 | |
| Detritus | 15,133 ± 18 | 224.5 | 24,913 ± 40 | 39,490 ± 33 | −280.7 |
| Energy in bodies | 286 | | 519 | 872 | |
| `mean_energy` | 0.489 ± 0.004 | −4.9 | 0.451 ± 0.007 | 0.422 ± 0.004 | 3.7 |
| Energy to reproduce (gene) | 21.28 ± 0.01 | 5.6 | 21.41 ± 0.02 | 21.48 ± 0.02 | −2.8 |
| Learning rate (gene) | 0.069 ± 0.010 | −0.8 | 0.061 ± 0.004 | 0.041 ± 0.002 | 4.1 |
| Exploration rate (gene) | 0.049 ± 0.003 | −5.6 | 0.031 ± 0.002 | 0.0226 ± 0.0009 | 4.6 |
| Lifespan (gene) | 3,645 ± 74 | 0.8 | 3,712 ± 48 | 3,815 ± 43 | −1.6 |
| Deepest lineage | 530 ± 16 | 0.4 | 540 ± 16 | 533 ± 12 | 0.3 |
| Situations met | 131.8 ± 3.0 | 0.7 | 135.1 ± 3.6 | 135.2 ± 4.5 | −0.0 |
| Distinct behaviours ever seen | 557 ± 21 | 5.2 | 751 ± 31 | 994 ± 45 | −4.5 |
| Behaviour diversity (bits) | 4.36 ± 0.14 | 2.7 | 4.81 ± 0.09 | 4.53 ± 0.08 | 2.2 |

**Nutrients do not move.** Across a 2.25-fold range of world energy, the standing crop on land is 0.5350,
0.5334 and 0.5411 units a land cell. Taking 10,000 units out of `base` took 9,780 from detritus, 233 from
bodies and nothing from the land. Adding 15,000 put 14,577 into detritus. The land is grazed down to
the same density every time, and the rest of the world's energy is a reservoir sitting in the soil.

**So population is more than proportionally sensitive to energy, not less.** Over the measured range the
relation is close to a straight line, population ≈ 0.0594 × energy − 614, which means about 10,300
units of overhead before the world supports a single agent and about 59 agents for each 1,000 units
after that. Section 5.2's rule of thumb, "doubling `--energy` roughly doubles the population", is close
at the top of this range and wrong at the bottom: 20,000 to 45,000 is 2.25 times the energy and 3.5
times the population.

This is the one place where a prediction written mid-run earned its keep. With `e20k` finished and
`e45k` still running, the pool decomposition above was used to pre-register four numbers for the
unfinished arm (`predictions.md`, 16:35). Nutrients, detritus and `mean_energy` all landed inside their
stated bounds. The population interval, 1,600 to 2,000, did not: the answer was 2,066, although the
straight line that generated the interval gave 2,002.

**What the richer world does not buy.** Lineage depth is flat across all three arms (530, 540, 533), so
generations are not energy-limited; nor are situations met (132, 135, 135). What a richer world does buy
is behaviours: the archive runs 557, 751, 994. And what it costs is learning, with both learning and
exploration genes falling as the world gets richer. A denser population shares the same fixed standing
crop, so each agent holds less (`mean_energy` 0.489, 0.451, 0.422) and lives a shorter, more crowded
life in which learning pays less.
### 11.6 E6: does a bigger world sustain more variety?

No. It sustains more agents, at the same density, doing the same things.

`big` is 128 × 128 cells with 53,000 energy units, which is the same energy a cell as the default, and a
3,500-agent cap so that the cap cannot bind. At year 2,000 it holds 2,019 ± 13 agents against `base`'s
1,151 ± 9. The world has 1.79 times the land cells and 1.77 times the energy, and it holds 1.76 times
the population.

**Table 13.** The bigger world against the default, at year 2,000, mean of sixteen seeds
(± standard error), with Welch's *t*.

| Measure | `base` (96 × 96) | `big` (128 × 128) | Ratio | *t* |
|---|---|---|---|---|
| Land cells | 8,520 | 15,243 | 1.789 | |
| Population | 1,151 ± 9 | 2,019 ± 13 | 1.755 | −54.1 |
| Nutrients on land | 4,544 ± 33 | 8,175 ± 69 | 1.799 | −47.7 |
| Standing crop a land cell | 0.5334 | 0.5363 | 1.005 | |
| Detritus | 24,913 ± 40 | 43,870 ± 75 | 1.761 | −223.1 |
| `mean_energy` | 0.451 ± 0.007 | 0.457 ± 0.005 | 1.013 | −0.7 |
| Distinct behaviours ever seen (of 2,048) | 751 ± 31 | 805 ± 23 | 1.072 | −1.4 |
| Behaviour diversity (bits) | 4.805 ± 0.094 | 4.840 ± 0.086 | 1.007 | −0.3 |
| Difference between the banks' signals | 0.0060 ± 0.0018 | 0.0029 ± 0.0009 | 0.483 | 1.5 |
| Signal entropy (bits) | 1.8284 ± 0.0127 | 1.8298 ± 0.0120 | 1.001 | −0.1 |
| Policy complexity (of 20) | 19.783 ± 0.038 | 19.770 ± 0.057 | 0.999 | 0.2 |
| Deepest lineage | 540 ± 16 | 613 ± 22 | 1.135 | −2.6 |
| Learning rate (gene) | 0.061 ± 0.004 | 0.047 ± 0.004 | 0.777 | 2.4 |

**The standing crop is invariant across size as well as across energy.** 0.5334 units a land cell in the
default world and 0.5363 in the big one, a difference of 0.5%. Section 11.5 found the same
constant across a 2.25-fold range of energy. Two different ways of changing the world, and the land is
grazed to the same density in all of them. That is the steadiest number in this section.

**Nothing about variety improves.** Behaviour diversity is identical to three significant figures. The
archive rises 7%, which is inside seed noise at *t* = −1.4. The two banks' signals actually diverge
*less* in the bigger world, not more as predicted, though at *t* = 1.5 that is not a result either. The
only measures that move are population, which scales with the world, and lineage depth, which is 14%
deeper.

And this is a fact about the world rather than about the measure, which is the one thing E6 was set up
to distinguish. The archive sits at 805 of its 2,048 cells, so 1,243 descriptors have never been seen
and the ceiling is nowhere near binding. A world nearly twice the size, running the same 2,000 years,
simply does not produce behaviours it was not already producing. Section 7.2 worried that `novelty`
would saturate because the descriptor space fills; the truth is less flattering to the world and more
flattering to the measure. The space does not fill. The world stops exploring it.
### 11.7 Ten thousand years

![Figure 7. The four conditions carried on to year 10,000, sixteen seeds each. Top left: the learning-rate gap between inheriting and not inheriting closes to within seed noise. Top right: only the inheriting world ever structures its signalling. Bottom left: the river arms stay together for the whole run. Bottom right: inheriting what was learned supports 8% more agents, permanently.](figures/fig-s7-long.svg)

Four of the nine conditions were carried on from 2,000 to 10,000 years, chosen by a trend test rather
than by taste. Over years 1,500 to 2,000 `base` was still moving (signal entropy falling, *t* = −3.2;
population rising, *t* = 2.7); `ford1` and `wall` were E3 and unfinished; `none` is the control without
which the learning-rate question cannot be read. The other five were flat and stop at 2,000. Nine more
predictions were written before the long runs started (Section 11.8, L1 to L9). The run took eight and a
half hours overnight, 32 processes at a time, and every one of the 64 seeds finished.

**Table 14.** Copy against none at year 10,000: the mean over years 9,901 to 10,000, sixteen seeds a
side, Welch's *t*. The year-2,000 values are from Section 11.2.

| | copy, year 2,000 | none, year 2,000 | copy, year 10,000 | none, year 10,000 | *t* at 10,000 |
|---|---|---|---|---|---|
| `gene_alpha` (learning rate) | 0.0607 | 0.0327 | 0.0391 | 0.0326 | 2.33 |
| Ratio, copy over none | 1.86 | | 1.20 | | |
| `gene_eps` (exploration) | 0.0310 | 0.0151 | 0.0212 | 0.0145 | 5.74 |
| Signal entropy, bits | 1.828 | 1.997 | 1.654 | 1.997 | −8.90 |
| Agents whose favourite signal is silence | | | 83% | 33% | |
| Population | 1,151 | 1,105 | 1,198 | 1,111 | 9.81 |
| Generations deep | 540 | 382 | 2,462 | 1,793 | 14.40 |
| Nutrients standing on the land | 4,544 | 4,154 | 4,839 | 4,155 | 15.18 |
| Crossings a year | 232 | 319 | 183 | 318 | −4.65 |

**The Baldwin gap was a transient.** The learning-rate ratio, inheriting over not, as 100-year means, went 3.7 at year 300,
2.6 at 1,000, 1.86 at 2,000, 1.37 at 5,000 and 1.20 at 10,000, and *t* fell below 3 for the first time
at year 9,000. Section 6 read the year-300 gap as evolution turning learning down when learning is not
passed on. Over ten thousand years it looks the other way round: both worlds are heading to the same
low learning rate, and the world that starts each child blank simply gets there in a few hundred years
while the world that hands down its Q-tables takes thousands. The `none` arm reached 0.034 by year 1,000
and has sat at 0.032 to 0.034 ever since. Inheritance does not change where the learning rate ends up; it changes how
long the journey takes. The exploration gene still separates at *t* = 5.7, so not every learning trait
has converged, but it too has narrowed, from a ratio of 2.1 to 1.5.

**What inheritance does do, permanently, is three things.**

- **It is the only route to a signalling habit.** Without inheritance, signal entropy sits at 1.997 bits
  from year 1 to year 10,000: the four signals are used almost exactly equally, and silence is the
  favourite of 33% of agents against the 25% that chance would give. With inheritance, silence is the
  favourite of 83% by year 10,000. Speaking costs 0.05 energy a tick, a cost too small for one lifetime of
  Q-learning to detect against the noise of feeding, and large enough to show up once the estimate is
  carried down 2,400 generations. This is the one result in Section 11 that is cultural in the full
  sense: a behaviour no individual can learn, which a lineage learns. It is also why Section 11.3 found
  no dialects. The only thing inheritance teaches about the channel is to leave it quiet, and that
  lesson is the same on both banks.
- **It feeds more agents.** 1,198 against 1,111, 7.8% more, *t* = 9.8, and the gap was still there at
  every 1,000-year checkpoint from 2,000 on. The inheriting world also leaves more nutrients standing on
  the land and holds more energy in each body, so the extra agents come from grazing better, not from
  grazing harder, and the margin is still growing. The blank world's standing crop has sat at 4,153 to
  4,155 units from year 2,000 to 10,000 and its mean body energy at 0.43; the inheriting world's crop has
  risen from 4,544 to 4,839 and its body energy from 0.451 to 0.483. Section 11.5 found the standing crop
  pinned at about 0.534 a land cell across three energy levels at year 2,000. That holds across energy
  but not across time: an inheriting world keeps getting better at grazing for all ten thousand years,
  and a blank one is pinned from the start.
- **It turns generations over faster.** 2,462 generations against 1,793, so a generation lasts 4.1 years
  in the inheriting world and 5.6 in the blank one. Inheriting agents also wander across the river less,
  183 crossings a year against 318.

**The banks and the river.** Signal entropy in `base` fell from 1.828 at 2,000 to 1.666 at 7,000 and
then stopped: over the last 2,000 years its trend is −0.006 bits a millennium, *t* = −0.6. The drift into
silence has found its floor at about 1.65 bits. Bank imbalance in `base` drifted down, from 0.268 at
2,000 to 0.173 at 10,000, and population crept up throughout, 1,151 to 1,198.

The river arms did not change their verdict. At year 10,000 `dialect_jsd` is 0.0098 with three fords,
0.0100 with one and 0.0130 with none, *t* = 0.98 for no fords against three. The walled world has been
the highest of the three at each of the last three checkpoints, and at 9,000 and 10,000 all three arms
line up in the order contact predicts for the first time. That is the direction isolation would
predict, but the margin is about a third and inside seed noise; no seed in any arm is above 0.10 at the end, and the
largest single seed-year in any arm in ten thousand years was 0.096, in the walled world at year 6,193. If drift is separating the walled banks, it
is doing it at something like 0.001 bits a thousand years, and the paper's 0.2 would arrive somewhere
beyond year 100,000. One river measure leans: the walled world's signal entropy is 1.752 against 1.654
(*t* = −2.4), below the |*t*| = 4 bar Section 11.9 sets for a result, but in the same direction at
2,000, 5,000 and 10,000. If it is real, contact speeds the drift into silence. The obvious mechanism is that a fully silent lineage on one bank can recolonise the other
across a ford, and behind a wall it cannot.

**Survival.** No seed died out in any of the four arms in 10,000 years. The smallest population ever
recorded was 318, in the founding years, and the smallest single bank 135; after year 2,000 no bank in
any seed fell below 172. The world is robust over a horizon fifty times longer than Section 6 tested.
### 11.8 The predictions, scored

Twenty-six predictions were written before the first world existed (twenty-nine numbered items, three of them falsifiers scored with the predictions they guard), plus four more written
mid-programme when `e20k` had landed and `e45k` had not, and nine more before the four long runs were
carried past year 2,000. None has been edited since. The full text sits
in `_build/experiment-s7/predictions.md`, above a correction line that records what was already wrong
before any result came in.

**Table 15.** Every pre-registered prediction and what happened. PARTLY means one clause of a compound
prediction held and another did not.

| # | Prediction | What happened | |
|---|---|---|---|
| T1 | Aggregate throughput 3 to 5 years/s | 17.5, and 20.2 with two conditions at once | wrong |
| E1.1 | Population within 10% across the three arms, all \|*t*\| < 2 | within 4%, but *t* = 4.5 and 4.2 | partly |
| E1.2 | `q_states` ordered copy > half > none, all \|*t*\| > 4 | 135 / 136 / 66: `half` equals `copy` | wrong |
| E1.3 | `policy_complexity` copy over none by at least 1.3 of 20 | 19.78 / 18.96 / 18.14, gap 1.64, ordered | right |
| E2.1 | `gene_alpha` copy at or above 0.20, none at or below 0.055 | 0.061 and 0.033 | wrong |
| E2.2 | `gene_eps` copy above 0.035, none below 0.025, \|*t*\| > 3 | 0.031 and 0.015, *t* = 9.2 | partly |
| E2.3 | `half` between the other two on both genes | not between on either, and outside both on `gene_eps` | wrong |
| E2.4 | Evolution turns learning down when it is not passed on | holds at every year from 50 on, *t* = 6.4 | right |
| E3.1 | Three fords, 5,000 years: `dialect_jsd` below 0.005 | 0.0086, rising in all three arms alike | wrong |
| E3.2 | `ford1`: 60 to 160 crossings a year, jsd above 3× base but below 0.05 | 62 crossings; jsd 0.0090, equal to `base` (*t* = −0.15) | partly |
| E3.3 | `wall`: 0 crossings, jsd above 0.05, bank gap above 0.25 in half the seeds | 0 crossings; jsd 0.0083, equal to `base`; 6 of 16 | wrong |
| E3.4 | No seed extinct; at most 2 of 16 `wall` seeds lose a bank | none extinct, no bank lost, smallest bank 141 | right |
| E3.5 | Section 7's own example, one ford above 0.2 by year 2,000, is wrong | 0.0020 at year 2,000; never above 0.052 in any seed-year | right |
| E4.1 | `calm` logs 0 events, `base` about 150 per 300 years | 0 and 156 | right |
| E4.2 | `calm` diversity lower by at least 0.3 bits, archive by at least 50 | diversity *higher* by 0.20, archive lower by 11 | wrong |
| E4.3 | `calm` `change` lower by at least 0.05 | lower by 0.016 | wrong |
| E4.4 | `calm` population 2 to 8% higher | 1.8% lower | wrong |
| E4.5 | `novelty` does not separate the arms | 0 in both | right |
| E5.1 | `e20k` 0.72 to 0.85×, `e45k` 1.15 to 1.40× and below 1.5× | 0.51× and 1.80× | wrong |
| E5.2 | `gene_repro` 20.5 to 22.5 everywhere, all \|*t*\| < 3 | 21.28 to 21.48, but *t* = 5.6 | partly |
| E5.3 | `mean_energy` rises with energy, stays below 1.0 | falls with energy; below 1.0 | partly |
| E5.4 | `gene_lifespan` does not order cleanly | *t* = 0.8 and −1.6 | right |
| E6.1 | `big` archive at least 15% up, diversity at least 0.2 bits up | 7.2% and 0.035 bits, both inside noise | wrong |
| E6.2 | `big` `dialect_jsd` at least twice `base` | half of `base` | wrong |
| E6.3 | `big` population 1.4 to 1.9× `base` | 1.755× | right |
| E6.4 | A flat archive would indict the 2,048-cell ceiling, not the world | archive flat, ceiling nowhere near binding at 805 | right |
| P2.1 | `e45k` nutrients within 2% of 4,550, crop within 2% of 0.535 | 4,610 and 0.5411 | right |
| P2.2 | `e45k` detritus about 39,000 | 39,490 | right |
| P2.3 | `e45k` population 1,600 to 2,000 | 2,066 | wrong |
| P2.4 | `e45k` `mean_energy` below 0.451 | 0.4221 | right |
| L1 | The learning-rate gap closes: ratio 1.0 to 1.4 at year 10,000, \|*t*\| < 3 | 1.20, *t* = 2.33 | right |
| L2 | `none` flat: `gene_alpha` 0.028 to 0.040, signal entropy above 1.99 | 0.0326 and 1.9965 | right |
| L3 | `base` signal entropy falls to 1.65 to 1.78 by year 10,000 | 1.654, flat since 7,000 | right |
| L4 | `base` bank imbalance stays 0.20 to 0.35 | fell to 0.173 | wrong |
| L5 | `base` population 1,150 to 1,260, 2,400 to 3,000 generations | 1,198 and 2,462 | right |
| L6 | `dialect_jsd` ordered base < ford1 < wall at every checkpoint from 2,000 | ordered at 2 of nine checkpoints, the last two, inside noise | wrong |
| L7 | `wall` `dialect_jsd` above 0.10 at year 10,000 | 0.0130 | wrong |
| L8 | No seed extinct in 10,000 years | none; smallest population 318 | right |
| L9 | 64 processes within 5% of 20.15 years/s | 15.56, 23% slower | wrong |

**The tally.** Of the thirty-nine scored in Table 15, 17 were right, 5 partly right and 17 wrong.
Split by when they were written: of the twenty-six scored rows written before any world existed, 9 were
right, 5 partly and 12 wrong; of the four made mid-programme with one result in hand, 3 were right; of the nine made at
year 2,000 with every short run analysed, 5 were right. The predictions got better as the evidence
behind them grew, which is how it should go, and the ones that failed at every stage failed where the
model's mechanism was not what the paper said it was: the river (E3, L6, L7), the disturbances (E4) and
the energy budget (E5.1).

**What the wrong ones were worth.** The four E4 predictions failed together and in the same direction,
and that pattern is what sent us to look at how big the disturbances actually are; a single wrong
prediction would have looked like noise. E1.2 and E2.3 failed because `half` is not what its name says,
and chasing that disagreement is what produced Table 10. E5.1 failed in the opposite direction from the
reasoning behind it: the energy really does pile up in detritus as predicted, but the fixed standing
crop makes population more than proportionally sensitive rather than less, and finding that out is what
made the mid-run prediction P2 possible, three-quarters of which then held on an arm that had not yet
finished.

Being wrong on paper costs nothing. Being wrong without having written it down first costs the result,
because there is then no way to tell a finding from a story told afterwards.
### 11.9 What this section does not show

**Everything here is about river world.** Nine conditions on one simulation with one parameter set. The
Baldwin-style result in 11.2 is a fact about these agents in this world, as Section 6 said of its own;
nothing here generalises to learning and evolution in anything else.

**Where you stop decides what you find.** That is the sharpest lesson of 11.2 and 11.7. The
learning-rate ratio peaks at 3.7 near year 300, is 1.7 by year 2,000 and 1.2 by year 10,000. Stopped at
300 it is a large permanent effect; stopped at 10,000 it is a difference in speed. Even 10,000 years is
one horizon: the inheriting world's standing crop and body energy were still rising when it stopped.
A measurement at one horizon is a measurement at one horizon.

**Sixteen seeds and twenty-two columns means some of these *t* values are chance.** Each comparison in
this section tests about twenty-two columns at once. With |*t*| above 2 as the bar, roughly one column
a comparison will clear it by luck alone. Everything claimed here as a result sits above |*t*| = 4, and
most above 6; the numbers quoted near 2, such as the archive in Table 9 or behaviour diversity in
Table 12, are noted but not leaned on.

**The measures are cruder than the numbers look.** `novelty` reaches exactly 0 by year 300 in every arm
and stays there, with the archive saturated around 750 of its 2,048 cells, so it discriminates nothing
after the first few centuries. `q_states` counts a visited flag and, as Table 10 shows, that flag can
outlive the knowledge behind it entirely. `ecology_entropy` and `archive_size` both inherit the same
six-part descriptor, and Section 7.2's warning about it stands: these are the observer, and a better
observer would see a different world.

**Two arms are not quite the same program.** `ford1` and `wall` each differ from the shipped kit by one
line. The terrain was checked, and nothing else in those folders differs, but they are copies and
should be read as such.

**E4 is unanswered rather than answered.** The null in 11.4 is a fact about disturbances that touch a
0.1% of the energy budget. It says nothing about whether disturbance would matter if it
were large enough to notice.

**And the most useful warning of the lot:** check what a treatment does in the code before building an
experiment on its name. `--inherit half` sounds like a halfway point between the other two arms, and
E1 added it on that basis. It is not one. One line of reading would have caught it before 31 minutes of
compute, and the only reason it became a result rather than a wasted arm is that the three arms
disagreed in a pattern strange enough to send us back to the source.
