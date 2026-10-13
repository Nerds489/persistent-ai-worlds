## 6. The first experiment: should learning be inherited?

The one design choice river world forces on you is what a child gets from its parent's learning. The first experiment compares the two ends: `copy`, where a child starts with its parent's Q-table, and `none`, where it starts blank and inherits only the genes that set how it learns. Everything else was left at the defaults. Each condition ran four seeds for 300 simulated years on the laptop, eight processes at once, about 16 minutes in all.

```bash
./run_seeds.sh 4 300 inherit-copy
./run_seeds.sh 4 300 inherit-none --inherit none
python3 summarise.py runs/inherit-copy runs/inherit-none
```

![Figure 3. The two conditions over 300 simulated years. Population ends the same at four seeds, but the genes for learning go different ways: when learning is not inherited, evolution turns the learning rate and exploration down. Bold lines are the mean of four seeds; faint lines are the individual seeds.](figures/fig-river-results.svg)

**Table 4.** The last 50 years of each run, mean of four seeds (± standard error), with Welch's *t*.

| Measure | `copy` | `none` | *t* |
|---|---|---|---|
| Population | 1,012 ± 24 | 1,024 ± 27 | −0.3 |
| Learning rate (gene, started at 0.2) | 0.186 ± 0.033 | 0.049 ± 0.005 | 4.1 |
| Exploration rate (gene, started at 0.1) | 0.041 ± 0.005 | 0.018 ± 0.002 | 4.0 |
| Situations met (of 240) | 137 ± 6 | 65 ± 1 | 12.3 |
| Deepest lineage (generations) | 116 ± 7 | 77 ± 6 | 4.3 |
| Signal entropy (bits; 2.0 = random) | 1.961 ± 0.006 | 1.998 ± 0.000 | −5.9 |
| Behaviour diversity (`ecology_entropy`, bits) | 6.07 ± 0.17 | 4.30 ± 0.17 | 7.4 |
| Difference between the banks' signals (`dialect_jsd`) | 0.0006 | 0.0001 | 5.6 |
| Lifespan (gene, started at 1,200 ticks) | 3,178 ± 257 | 3,213 ± 313 | −0.1 |

### 6.1 What happened

**Both worlds filled up the same way.** Population rose from 300 to about 700 within ten years and settled near 1,000 in both conditions; the energy budget, not the inheritance rule, decides how many agents the river world feeds. (Sixteen seeds do separate them, by 4% at year 2,000 and 7.8% at 10,000: Sections 11.2 and 11.7.) Both populations also evolved the same strategy: the energy needed to reproduce fell from 70 to about 21, close to its floor of 20, and lifespans stretched from 1,200 to about 3,200 ticks. Evolution chose many small agents that split as soon as they can and then live long, hungry lives: the mean agent holds about half a unit of energy. Neither of those results was designed in.

**The genes for learning went different ways.** When children inherit their parents' Q-tables, the learning rate stays near where it started (0.19) and exploration falls slowly, from 0.10 to 0.04. When every child starts blank, evolution turns learning down: the learning rate falls steadily to 0.05 and exploration to 0.02. All four seeds agree. One reading is that a blank Q-table learned over a short, hungry life is mostly noise, and that noise costs energy, so selection quietens it; whereas an inherited table is worth updating carefully. That is the Baldwin effect's question, how learning and evolution shape each other [@hinton1987], answered here in one specific way for one specific world. It is a result to test on sixteen seeds and longer runs (Section 7, E2), not a law.

**Inherited learning carries more of the world.** Agents under `copy` had met 137 of the 240 situations, twice as many as under `none`, because each table carries its ancestors' experience. They also kept a more varied population (6.1 bits of behaviour diversity against 4.3) and their lineages ran deeper.

**No dialects yet.** Signals stayed close to random in both conditions (entropy 1.96 and 2.00 bits out of 2), and the two banks used them almost identically: under `copy`, `dialect_jsd` peaked at 0.005 around year 25 and ended below 0.001. With three fords and about 300 crossings a year, 300 years is too short and too well connected for the banks to drift apart. That is exactly what Section 7's experiment E3 is for, on the desktop's sixteen cores and over thousands of years.

> **Note:** Four seeds a side is enough to see the large effects here (|t| above 4), but not to trust the small ones. The desktop runs sixteen seeds in the time the laptop ran four; run E1 and E2 there before building on any of this.
