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
