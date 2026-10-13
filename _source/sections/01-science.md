## 1. The science of never-ending learning

### 1.1 What "open-ended" means in 2026

Artificial life (ALife) studies "life as it could be" by building it. Christopher Langton put the name in print in 1986, in "Studying artificial life with cellular automata" [@langton1986], and convened the first workshop on the synthesis and simulation of living systems at Los Alamos in September 1987 [@alife1]. Bedau's taxonomy is still the standard one: *soft* ALife builds simulations and other purely digital constructions, *hard* ALife builds hardware, and *wet* ALife synthesises living systems from biochemical substances [@bedau2003]. This paper is about soft ALife and its descendants in machine learning.

Two research lineages want the same thing, a system that keeps producing new and interesting things without being told what to produce:

- **Open-ended evolution** (OEE) comes from ALife. It asks why biological evolution never seems to finish, and whether a digital world can do the same. A 25-author workshop report in 2016 concluded with "pluralism about OEE": there is no single accepted definition or test [@taylor2016].
- **Open-ended learning** (OEL) comes from reinforcement learning. It asks how an agent can keep acquiring skills when the tasks themselves keep changing, as in POET [@wang2019poet] and DeepMind's XLand [@xland2021].

In 2024 Hughes and colleagues at Google DeepMind gave the field a working definition in an ICML position paper that was selected for an oral: "from the perspective of an observer, a system is open-ended if and only if the sequence of artifacts it produces is both novel and learnable" [@hughes2024]. Novelty means the artifacts become harder to predict from the observer's model at any fixed time; learnability means that seeing more of the history makes them easier to predict. The observer is "a free parameter of great importance": a system can be open-ended to a person and not to a more capable model. The paper argues that open-endedness is essential to any path to artificial superhuman intelligence, and that today's foundation models are not open-ended by themselves because they are trained on fixed data [@hughes2024].

> **Key insight:** "Open-ended" is a relationship between a system and an observer, not a property you can read off a single run. Every claim of open-endedness in this paper should be read as "open-ended to someone, for a while".

The field's own verdict on the central question has not moved: **no artificial system is generally accepted as having demonstrated unbounded open-ended evolution** [@hughes2024; @kumar2025asal]. Systems produce bursts of novelty and then plateau, cycle or converge. The MODES toolbox (Dolson, Vostinar, Wiser and Ofria, 2019) is the most widely used way to measure what a run is actually doing, along four axes: change, novelty, complexity and ecology [@dolson2019]. Older *evolutionary activity statistics* are still used alongside it, for example in the Flow-Lenia journal paper [@plantec2025].

### 1.2 The core paradigms

Every system in this paper combines a handful of mechanisms:

| Paradigm | What learns or changes | Typical algorithms | Strength | Weakness |
|---|---|---|---|---|
| Reinforcement learning (RL) | One agent's policy, from reward | PPO [@schulman2017], DQN | Learns skills from scratch | Needs a reward; forgets when the task shifts |
| Multi-agent RL (MARL) | Several policies at once, formalised as stochastic games | Independent PPO, MAPPO, league training | Other agents become an ever-changing curriculum | Non-stationary; costly at scale |
| Self-play and autocurricula | A policy against copies of itself or a league | AlphaZero [@silver2018], AlphaStar [@vinyals2019] | Difficulty rises automatically | Can cycle; narrow to the game |
| Evolution and genetic algorithms | A population of genomes, by selection and mutation | GA, evolution strategies | No gradients needed; parallel | Slow per generation |
| Neuroevolution | Network weights and topology | NEAT [@stanley2002] | Grows structure as needed | Scales poorly to large networks |
| Quality-diversity (QD) | An archive of diverse, good solutions | Novelty search [@lehman2011], MAP-Elites [@mouret2015] | Keeps stepping stones | Needs a behaviour descriptor |
| Foundation-model agents | Prompts, memories and code around a fixed model | Generative agents [@park2023], self-improving agents [@zhang2025dgm] | Rich behaviour from day one | Expensive per step; the model itself does not learn |
| World models | A learned simulator of the environment | Dreamer [@hafner2025dreamer4], Genie [@genie3] | Imagination, planning, generated worlds | Short consistency horizons |

Stanley and Lehman's argument that "greatness cannot be planned" [@stanley2015] underlies the quality-diversity column: in deceptive search spaces the stepping stones to a great solution rarely look like progress toward it, so an archive of interesting variety beats a single objective. Clune's *AI-generating algorithms* proposal (2019) combines three pillars: meta-learning architectures, meta-learning the learning algorithms, and automatically generating environments [@clune2019]. Much of the 2024 to 2026 work in Section 3 implements those pillars with foundation models.

### 1.3 The autocurriculum, with its fine print

The most productive single idea from 2019 to 2026 is the *autocurriculum*: when agents compete or cooperate, each improvement by one changes the problem for the others, so the curriculum writes itself. OpenAI's hide-and-seek (Section 2.1) is the canonical demonstration. The practical rule that follows: make other agents the hardest part of the environment, then budget for far more experience than intuition suggests.

Two cautions belong next to it, both from the original paper:

1. **Scale is a precondition, not a detail.** The default hide-and-seek run used a batch of 64,000 and a 1.6 million-parameter policy; batch sizes of 16,000 and 8,000 "never converged" to the later strategies [@baker2020].
2. **The comparison with intrinsic motivation was narrow.** Baker and colleagues found that multi-agent competition "may scale better with increasing environment complexity" than count-based exploration and random network distillation, in their environment [@baker2020]. That is evidence, not a law. The first edition of this paper overstated it.
