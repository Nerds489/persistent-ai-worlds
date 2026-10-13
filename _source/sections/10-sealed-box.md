## 10. Scenario B: AIs sealed in a box for 1,000 years

### 10.1 The design

The second scenario is a digital terrarium: a closed system with a fixed amount of energy, in which agents must survive by cycling it. The reference implementation, `sealed_box.py` (Appendix B), enforces the closure exactly.

- **Three energy pools.** Energy moves between nutrients on the grid, agents' bodies, and detritus (waste and corpses). It is never created or destroyed. The program asserts after every tick that the total is unchanged; over 1,000 simulated years it drifted by 3.4 × 10⁻⁷ out of 60,000, which is floating-point rounding.
- **Metabolism.** Moving costs 1 energy per tick and resting 0.6. The cost is deposited as detritus where the agent stands.
- **Feeding.** An agent takes up to 4 units of nutrients from its cell. When several agents share a cell, they eat in random order.
- **Decomposition.** Detritus returns to nutrients at 5% per tick, and nutrients diffuse slowly across the grid.
- **Death.** An agent dies when it starves or exceeds its heritable lifespan, and its body becomes detritus.
- **Reproduction.** When an agent's energy exceeds its heritable threshold, it splits that energy with a child whose genome is mutated at the parent's own, heritable mutation rate. The box has a hard capacity of 1,200 agents.
- **Genome.** A linear policy from seven senses to five actions, plus the lifespan, reproduction threshold and mutation rate. Every trait is free to evolve.
- **Time.** One "year" is 100 ticks.

### 10.2 What happened in 1,000 years

![Figure 5. Sealed box, reference run of 1,000 simulated years on a laptop CPU (4.5 minutes). Left: the heritable lifespan rose by 71%. Centre: the energy needed to reproduce halved. Right: the deepest lineage alive reached generation 571; the dip near year 550 is the deepest lineage dying out.](figures/fig-box-results.svg)

The run took about 4.5 minutes. Selection was visible in every heritable trait:

**Table 12.** Population means in the sealed box at selected years.

| Year | Lifespan gene (ticks) | Reproduction threshold (energy) | Mutation rate | Deepest generation | Genome diversity |
|---|---|---|---|---|---|
| 1 | 300 | 60.0 | 0.050 | 5 | 0.50 |
| 100 | 320 | 55.6 | 0.051 | 71 | 0.56 |
| 250 | 367 | 49.3 | 0.054 | 165 | 0.63 |
| 500 | 414 | 37.8 | 0.055 | 313 | 0.83 |
| 750 | 487 | 33.5 | 0.054 | 424 | 0.84 |
| 1,000 | 514 | 30.7 | 0.052 | 571 | 0.91 |

Lineages evolved to live longer and to reproduce earlier with less energy: more, smaller offspring over a longer life. The mutation rate drifted only slightly, so it was close to neutral. Genome diversity kept rising rather than collapsing. Around year 550 the deepest lineage died out, and the maximum generation dropped from 344 to 307 before climbing again.

Two honest caveats belong with these results. First, in this configuration the hard capacity of 1,200 bound before the energy budget did, so crowding rather than starvation set the population. In an energy-limited variant (24,000 total energy, capacity 3,000), the population settled around 450 and fluctuated between 378 and 501, and the same trends appeared. Second, rising *genome* diversity is not the same as rising *behavioural* novelty. Measuring that needs behavioural descriptors and MODES-style statistics (Section 8.4). This scaffold is a starting point, not an open-ended system.

### 10.3 What to expect over longer and richer runs

The first edition offered a confident century-by-century timeline. The evidence supports something more conditional:

**Table 13.** Expected dynamics in a richer sealed box, with the evidence behind each stage.

| Stage | Expected dynamics | Evidence |
|---|---|---|
| Early | Rapid adaptation to the energy budget; initial die-offs; stabilisation near carrying capacity | Observed in the reference runs |
| Arms races | Parasitism, immunity, hyper-parasitism and cheating, if organisms can exploit each other's code or bodies | Strong in Tierra [@ray1991] |
| Niche formation | Coexisting strategies when resources are patchy and varied | Moderate; Flow-Lenia shows species competing in one world [@plantec2025] |
| Plateau | Convergence or cycling; novelty slows | The default outcome in every system in this paper [@hughes2024] |
| Punctuated change | Long stasis broken by rapid change after a perturbation or a key innovation | Plausible; seen in Avida's step-wise evolution of complex functions [@lenski2003] |

To make long runs worth watching, the box needs ways for organisms to interact beyond competing for food: predation, parasitism, signalling, building. It also needs the anti-stagnation levers of Section 8.3, and above all richer genomes than a linear policy. Self-replicating programs in the style of BFF, which arise from random code with no fitness function [@aguera2024], are the most interesting candidate for a box that might surprise its builder.
