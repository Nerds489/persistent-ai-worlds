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

| Simulated year | 10 | 50 | 100 | 300 | 500 | 1,000 | 1,500 | 2,000 |
|---|---|---|---|---|---|---|---|---|
| `copy` | 0.195 | 0.222 | 0.214 | 0.157 | 0.143 | 0.084 | 0.068 | 0.057 |
| `none` | 0.174 | 0.094 | 0.080 | 0.042 | 0.041 | 0.034 | 0.032 | 0.033 |
| ratio | 1.1 | 2.4 | 2.7 | 3.7 | 3.5 | 2.5 | 2.1 | 1.7 |

The ratio peaks near year 300, which is exactly where Section 6 stopped, and decays to 1.7 by year
2,000. The front page of this paper quotes "0.18 vs 0.05 after 300 years"; that is true and it is the
high-water mark. At 2,000 years the inheriting world's learning rate, 0.057, has fallen to about where
the blank-slate world's was at year 300. Section 6 called the result "a result to test on sixteen seeds
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

> **`q_states` is not a measure of inherited knowledge.** Table 6 notes that inherited visits count
> under `--inherit copy`. They count under `half` too, and there the flag outlives the knowledge
> entirely. Anyone using `q_states` to compare inheritance rules should read Table 10 first, or use
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
