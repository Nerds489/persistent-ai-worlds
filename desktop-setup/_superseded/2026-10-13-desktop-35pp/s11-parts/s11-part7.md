### 11.8 The predictions, scored

Twenty-seven predictions were written before the first world existed, plus four more written
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
