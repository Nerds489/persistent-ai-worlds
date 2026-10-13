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
