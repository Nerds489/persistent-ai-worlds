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
