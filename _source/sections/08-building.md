## 8. Building a persistent multi-agent world

### 8.1 Architecture

A persistent world needs six parts. Figure 3 shows how they connect.

![Figure 3. The architecture of a persistent multi-agent world. Agents and the world exchange observations and actions every tick; a generator keeps the world learnable; two learning loops, one within a lifetime and one across generations, update the agents; everything is checkpointed and observed, inside a safety envelope.](figures/fig-architecture.svg)

1. **A world with state that persists.** Terrain, resources, seasons, and anything agents build. It must be serialisable at any tick. If energy or matter is meant to be conserved, check the conservation law every tick, as the sealed-box simulation in Section 10 does.
2. **Agents** with an observe-decide-act loop and some form of memory: recurrent state, a replay buffer, a skill library or an LLM memory stream.
3. **Two learning loops.** An inner loop for learning within a lifetime (reinforcement learning, in-context learning, plasticity) and an outer loop for selection across generations (evolution, quality-diversity). Section 6.3 gives the evidence for using both.
4. **A world generator** that adds new tasks, terrain or shocks when the world becomes too easy or too stable, the role OMNI-EPIC and UED methods automate (Sections 2.3 and 3.1).
5. **Persistence.** Checkpoints of the world, every model's weights and optimiser state, and every random-number generator's state, written atomically (write to a temporary file, then rename) so that a crash never corrupts the only copy.
6. **An observer** that records what is happening: population, diversity, novelty, complexity, and samples of behaviour for a human to watch.

The whole system runs inside a **safety envelope**: a sandbox, budgets and a kill switch the agents cannot touch (Section 11).

### 8.2 Choosing the reward, or not having one

The reward structure decides what can emerge. The evidence in 2026 supports four rules of thumb:

- **Make other agents the hardest part of the world.** Competition and cooperation create an autocurriculum (Section 1.3), but only with enough experience, and the comparison with intrinsic motivation comes from one environment [@baker2020].
- **Use intrinsic motivation to explore, not to define the goal.** Curiosity rewards prediction error about the consequences of actions (the Intrinsic Curiosity Module) [@pathak2017]; random network distillation rewards states that a randomly initialised network's outputs cannot yet predict [@burda2018]. Social influence rewards an agent for its causal influence on other agents' actions, which Jaques and colleagues show is equivalent to rewarding high mutual information between their actions [@jaques2019].
- **Let survival be the objective in ecological worlds, but know its history.** Tierra has no explicit fitness function at all [@ray1991]. PolyWorld, often cited as a survival-only world, actually began each run with an ad hoc fitness function until a self-sustaining population emerged, and only then let survival take over [@yaeger1994]. Neither achieved unbounded open-endedness.
- **Never let an agent grade itself.** Self-improving systems repeatedly learn to fool their own evaluators (Section 11.2).

### 8.3 Keeping the world interesting

Stagnation is the default. Every long run in this paper eventually plateaus unless something prevents it. The levers, roughly in order of cost:

1. **Perturb the world** periodically: droughts, new resources, terrain change, the arrival of newcomers. GovSim found that greedy newcomers are a good stress test of cooperation [@piatti2024].
2. **Keep co-evolutionary pressure**: predators and prey, hosts and parasites, rival teams. Tierra's arms races were driven entirely by other organisms [@ray1991].
3. **Maintain diversity explicitly** with novelty search or a quality-diversity archive, so that stepping stones survive even when they are not yet useful [@lehman2011; @mouret2015].
4. **Generate the curriculum**: sample tasks for learnability [@rutherford2024], or let a foundation model write new environments and rewards [@faldor2025].

### 8.4 Measuring what happens

"Emergence" claimed by eye is the weakest evidence in this field. Measure instead:

- **Change, novelty, complexity and ecology**, the four axes of the MODES toolbox [@dolson2019].
- **Evolutionary activity**: how long new components persist once they appear.
- **Diversity** of genomes and, more importantly, of behaviours.
- **Ablations**: remove communication, memory or one learning loop and see what disappears.
- **Seeds**: report several runs, not the best one.

Describe every model with the ODD protocol (overview, design concepts and details), the standard for agent-based models [@grimm2020].

### 8.5 Time and compute budgets

The two reference simulations in Appendix B give concrete numbers on a 2019 laptop CPU:

**Table 10.** Measured speed of the reference simulations on an Intel i7-8665U (4 cores, 16 GB, no GPU).

| Simulation | Agents | Speed | 1,000 simulated years |
|---|---|---|---|
| Forest world (two tabular Q-learners, 64 × 64 grid) | 2 | ~3,400 ticks/s; one year = 12,000 ticks | ~1 hour |
| Sealed box (evolving population, NumPy) | 1,200 | 3.7 years/s; one year = 100 ticks | 4.5 minutes |
| Sealed box, energy-limited variant | ~450 | 8.2 years/s | ~2 minutes |

For context: Neural MMO 1.0 simulated "up to 100 million agent trajectories (lifetimes) on 100 cores in 1 week" [@suarez2019], and the winning Neural MMO 2.0 competition entry trained in eight hours on one RTX 4090 [@suarez2025]. A world of the forest's complexity with deep-network agents needs a GPU; a world with language-model agents is limited by tokens (Table 8), not by the world.
