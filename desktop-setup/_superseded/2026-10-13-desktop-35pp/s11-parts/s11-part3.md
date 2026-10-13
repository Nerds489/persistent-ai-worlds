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
