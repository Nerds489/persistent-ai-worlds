## 9. Scenario A: two AIs in a never-ending forest

### 9.1 The design

The first edition proposed two learning agents in a procedurally generated forest that never ends. This edition keeps the idea, implements a minimal version that runs on a laptop, and reports what it actually did.

The reference implementation, `forest_world.py` (Appendix B), uses only Python and NumPy:

- **World.** A 64 × 64 wrap-around grid, generated from smoothed noise into forest (70%), clearing (15%), rock (5%) and water (10%). Water and rock are impassable.
- **Food** grows on forest and clearing cells. An eaten cell cannot regrow for 50 ticks; after that, regrowth is random, at seasonal rates: fastest in summer, slowest in winter.
- **Time.** A day is 100 ticks, with the last 40% night; a season is 30 days; a year is 12,000 ticks.
- **Bodies.** Each agent has up to 100 energy, spends 1 per tick by day and 1.5 by night, and gains up to 20 by eating. At zero it dies and is reborn somewhere random.
- **Senses.** Each agent sees the direction of the nearest food and of the other agent within 4 cells by day and 2 by night, plus its own energy, the season, the time of day and the other agent's last signal.
- **Actions.** Move in one of four directions or stay, while emitting one of four signals (a 2-bit channel), or eat.
- **Learning.** Each agent is a tabular Q-learner. Its table survives death, so learning accumulates across lifetimes, and exploration decays a little after every death.
- **Persistence.** The whole world and both agents are checkpointed atomically every 20,000 ticks, and the run resumes from the checkpoint when restarted.

### 9.2 What happened

![Figure 4. Forest world, reference run on a laptop CPU. Left: deaths per 10,000 ticks fall from 38 in the first year to low single figures as the agents' Q-tables accumulate across lifetimes; spikes come in lean seasons. Right: food eaten per 10,000 ticks more than doubles.](figures/fig-forest-results.svg)

In a 400,000-tick run (33 simulated years, 117 seconds on the laptop), deaths fell from 38 per 10,000 ticks in the first window to between 1 and 12 per 10,000 ticks after that, and food eaten per 10,000 ticks rose from 1,682 to over 4,000. The two Q-tables grew to about 1,300 visited states each. The agents learned to survive the seasons.

They did *not* learn to communicate or cooperate in this run. The entropy of their signals stayed near the 2-bit maximum, which means the signals carried no information, and they spent only 0 to 3% of their time near each other. Nothing in a tabular learner with two agents and abundant food rewards either behaviour. That is a useful negative result: emergence needs pressure and capacity, and this scaffold supplies neither.

### 9.3 Making emergence likely

The research in Sections 2 to 4 suggests what to change to make richer behaviour likely, roughly in order of evidence:

1. **More agents, and competition for scarce resources.** Hide-and-seek's tool use came from team competition at large scale [@baker2020]; exchange and tolerated theft emerged when agents shared downtime around a campfire [@garbus2023].
2. **A reason to talk.** Communication emerges when one agent knows something another needs: put food where only one agent can see it, or require two agents to act together to gain a reward.
3. **Function approximation instead of tables**: a small recurrent network trained with PPO, which generalises across states and can remember.
4. **More experience.** Expect millions to billions of steps, not hundreds of thousands. Moving the world into JAX or PufferLib makes that affordable on one GPU (Section 7.5).
5. **An evolutionary outer loop** over reward weights, learning rates and network sizes, as in Capture the Flag [@jaderberg2019].

**Table 11.** Behaviours to expect in a scaled-up forest, with the strength of the evidence.

| Behaviour | Precondition | Evidence |
|---|---|---|
| Foraging and seasonal survival | Any learner | Observed in the reference run |
| Territoriality, niche separation | Several agents, patchy resources | Good: niche formation reported in Neural MMO [@suarez2019] |
| Incidental cooperation in abundance | Abundant food, shared space | Moderate |
| Stockpiling before winter | A way to store food, plus memory | Plausible; not demonstrated in this scaffold |
| Communication | Information asymmetry and a shared reward | Moderate in MARL; strong in LLM populations [@boldt2024; @ashery2025] |
| Tool use, environment modification | Movable objects and competitive pressure | Strong, at large scale [@baker2020] |
| Division of labour | Many agents and a group goal | Strong in LLM agents [@sid2024]; weaker in RL |
