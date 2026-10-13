## 2. River world: Scenarios A and B in one world

The research paper ran its two scenarios separately. Scenario A put two learning agents in a forest that never ends; Scenario B sealed an evolving population in a box with a fixed amount of energy. River world joins them: every agent learns during its life, as in A, inside a population that evolves under a fixed energy budget, as in B. A river runs down the middle.

![Figure 1. River world after 300 simulated years (seed 1, learning inherited). The river runs north to south and wraps round, so it has no source and no mouth; tan bars are the three fords. Agents are coloured by bank: west orange, east blue. Paler land holds more nutrients; the river darkens where it carries more silt.](figures/fig-river-map.png)

### 2.1 What comes from Scenario A

- **Terrain** from the same smoothed-noise generator: forest, clearings (about 22% of the land) and rock (5%), which nothing can enter.
- **Time.** A day is 20 ticks, the last 40% of it night; a season is 100 ticks; a year is 400. Moving at night costs a quarter more.
- **A 2-bit signal channel.** Every action pairs a move (stay, north, east, south or west) with a signal (silent, 1, 2 or 3), 20 actions in all. An agent hears the loudest signal in the eight cells around it, one tick later. Speaking costs 0.05 energy.
- **Learning in a lifetime.** Each agent is a tabular Q-learner over 240 states: the direction of the richest neighbouring cell (5), its own energy band (3), day or night (2), the signal it hears (4) and whether it is within four cells of the water (2). The reward is the change in its own energy. Ties between untried actions are broken at random.

### 2.2 What comes from Scenario B

- **A sealed energy budget.** The world holds 30,000 energy units by default, and none is ever created or destroyed. The total is asserted after every tick.
- **Bodies and death.** Resting costs 0.5 a tick and moving 0.9; an agent eats up to 4 a tick from its cell and holds at most 150. It dies of starvation or of old age, and its body becomes detritus where it falls.
- **Heritable genomes.** Five genes: lifespan, the energy needed to reproduce, the mutation scale, the learning rate and the exploration rate. A parent above its threshold splits its energy with a child whose genes are mutated. Evolution can therefore tune *how* agents learn, which is the Baldwin effect that Hinton and Nowlan demonstrated in 1987 [@hinton1987].
- **What the child learns from the parent** is a switch, `--inherit`: `copy` hands over the parent's Q-table (learning passes down, Lamarckian in effect), `half` hands it over at half strength, and `none` starts every child blank, so only the genes for learning are inherited.

### 2.3 What the river adds

- **Two banks.** The world wraps north to south but has walls east and west, so it is a cylinder and the river cuts it in two. The channel is three cells wide and meanders up to about 11 cells either side of the centre line. Agents can cross only at three fords, at rows 16, 48 and 80.
- **A moving store of nutrients.** Each tick the river erodes 0.2% of the nutrients on its banks, carries a fifth of each stretch's load one row downstream, and lays 1% back down as silt on the banks. Because the river is a closed loop, everything it carries comes back.
- **Seasons and events.** Silt deposition rises two and a half times in spring. At the start of each season the world may roll an event: a spring flood (one year in four: six times the silt, three times the erosion, for 40 ticks), a summer drought (about one in seven: the river slows to a quarter and drops less silt), or a fire (a 12% chance at the start of each summer and autumn: a circle of radius 6 burns, nutrients become detritus, and agents caught in it lose half their energy). `--no-events` switches them off.

### 2.4 The energy ledger

![Figure 2. Where the energy goes. Four pools hold all 30,000 units; arrows are the only ways energy moves between them. Events change the rates on the arrows, never the total.](figures/fig-energy-flow.svg)

Decomposition turns detritus back into nutrients in place, at 5% a tick in forest, 3.5% in clearings and 2% on fords, and seasonally: a fifth faster in spring, under half as fast in winter. Nutrients also spread 2% a tick to each neighbouring land cell, never into rock or deep water. The full parameter list is in Appendix A.

> **Key insight:** Because nothing is created, every pattern in the population has to be paid for out of the same 30,000 units. Rich banks mean poorer land somewhere else; a boom on one side of the river is energy that is not available on the other.
