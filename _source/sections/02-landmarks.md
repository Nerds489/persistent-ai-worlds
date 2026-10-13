## 2. Landmark experiments, re-checked

Every number in this section was re-read from the primary source in October 2026. Where the first edition was wrong, Appendix A gives the original wording and the correction.

### 2.1 OpenAI hide-and-seek: six phases, with the real numbers

Baker and colleagues placed teams of one to three hiders and one to three seekers in a physics world with three to nine boxes and two ramps. Episodes last 240 steps, and the first 40% is a preparation phase in which seekers are frozen. Hiders are rewarded when all of them are hidden; seekers are rewarded when any hider is seen. Nothing else is rewarded [@baker2020]. Six strategies appeared, each a response to the last:

**Table 1.** The six emergent phases of hide-and-seek, with the paper's own names and episode counts [@baker2020].

| Phase | Paper's name | What happens | When it appears |
|---|---|---|---|
| 1 | Running and Chasing | Seekers chase; hiders crudely run away | From the start |
| 2 | Fort Building | Hiders move and lock boxes into shelters | After about 25 million episodes |
| 3 | Ramp Use | Seekers carry ramps to the walls and climb in | About 75 million episodes later |
| 4 | Ramp Defense | Hiders drag the ramps away and lock them | About 10 million episodes later |
| 5 | Box Surfing | Seekers bring a box to a locked ramp, climb onto it and "surf" it over the walls | After about 380 million episodes in total |
| 6 | Surf Defense | Hiders lock every unused box before building | Later still; the plotted runs end near 500 million |

The often-quoted "132.3 million episodes (31.7 billion frames)" is the cost for the default model to reach phase 4 in a separate batch-size experiment, over 34 hours of training, not the length of the whole run [@baker2020]. Two further results matter more for anyone building a world: teams of two and three hiders locked 25% and 36% more boxes than a single hider, so cooperation was emergent too, and the policies trained at batch sizes of 16,000 and 8,000 never reached the later phases at all [@baker2020].

### 2.2 Populations and leagues

**Capture the Flag.** DeepMind's *For The Win* agents learned to play a modified Quake III Arena on procedurally generated maps from pixels and game score alone. A population of 30 agents was trained together with population-based training, and each agent evolved its own internal reward signal [@jaderberg2019]. Two professional game testers with full communication, playing against a fixed pair of agents after 12 hours of practice, won 25% of games and drew 6.3%. The agents tagged with 80% accuracy against the humans' 48%, and reacted in 258 ms against 559 ms [@jaderberg2019].

**AlphaStar.** A continually evolving league of agents reached Grandmaster level in StarCraft II with all three races, ranking above 99.8% of officially ranked human players on Battle.net [@vinyals2019].

**OpenAI Five.** One continuous training run from June 2018 to April 2019 used 770 ± 50 petaflop/s-days on up to 1,536 GPUs, with a 159-million-parameter policy; it beat the world champions OG 2-0. Its 99.4% public win rate across 7,257 games counts 3,140 games that humans abandoned [@openai2019dota].

### 2.3 Open-ended task spaces

**XLand** (2021) generated games procedurally inside 3D worlds. Each agent in the final generation trained on about 3.4 million unique tasks, roughly 700,000 games in 4,000 worlds, and showed zero-shot competence on held-out tasks such as hide and seek, capture the flag and tag [@xland2021]. The 3.4 million is a count per agent, not the size of the task space.

**XLand 2.0 and the Adaptive Agent** (2023) enlarged the space to "over 10^40 possible tasks". A 265-million-parameter Transformer-XL agent adapted to held-out tasks as fast as humans, measured on 1,000 test tasks [@ada2023].

**Unsupervised environment design** (UED) automates the curriculum. PAIRED trains an adversary to propose levels that maximise the gap between two learners [@dennis2020]; Prioritised Level Replay revisits levels with high learning potential [@jiang2021]; ACCEL edits levels instead of sampling them [@parkerholder2022]; MAESTRO is the first multi-agent version [@samvelyan2023]. In 2024, *No Regrets* showed that the practical regret estimates most methods use mostly track success rate, and that simply sampling for learnability works better [@rutherford2024]. Kinetix (ICLR 2025 oral) turned the idea into tens of millions of procedurally generated 2D physics tasks [@matthews2025].

### 2.4 POET: environments that co-evolve with their solvers

Uber AI Labs' Paired Open-Ended Trailblazer co-evolves obstacle courses and walking agents, and transfers solutions between courses so that a skill learned in one becomes a stepping stone in another [@wang2019poet]. Enhanced POET (ICML 2020) added a domain-general measure of novelty and showed a phylogenetic tree of the first 100 environments of one run; the authors note that it resembles natural trees but "is much smaller" [@wang2020].

### 2.5 Neural MMO: a persistent world for many agents

Neural MMO (2019) is a persistent, tile-based world with food, water and combat. The original experiments capped populations at 16 to 128 agents per world across 100 worlds, and could simulate "up to 100 million agent trajectories (lifetimes) on 100 cores in 1 week" [@suarez2019]. Neural MMO 2.0 (NeurIPS 2023) supports 1 to 1,024 agents and ran three times faster [@nmmo2]. In the NeurIPS 2023 competition, the winner scored four times the baseline after eight hours of training on one RTX 4090 [@suarez2025]. Version 3.0 was rewritten in C inside PufferLib, with a demonstration map of 1,024 agents and 2,048 enemies [@puffernmmo3]. The standalone Python package has been idle since August 2024 and does not support Python 3.12 (Section 7).

### 2.6 Digital organisms: Tierra, Avida and PolyWorld

**Tierra** (Ray, 1991) seeded a soup of 60,000 instructions with one hand-written 80-instruction self-replicator. There is no fitness function: programs compete for CPU time and memory. Within the first few million instructions, 45-instruction parasites appeared that borrowed their hosts' copy loops. Hosts evolved immunity, parasites evolved around it, hyper-parasites drove the parasites extinct, and social hyper-parasites and "hyper-hyper-parasite cheaters" followed [@ray1991]. Ray's own summary is "parasitism, immunity, hyper-parasitism, sociality, and cheating". The mutualistic symbionts in the paper were made by hand; Ray wrote that it was "not known if such relationships have evolved spontaneously" [@ray1991].

**Avida** (Ofria, Adami and Brown, Caltech, 1993) gives every organism its own virtual CPU. In the best-known Avida experiment, Lenski, Ofria, Pennock and Adami (Nature, 2003) rewarded simple logic functions and watched whether the most complex one, EQU, evolved. It did in 23 of 50 populations; when only EQU was rewarded, it evolved in none of 50. In the case-study lineage, 18 of the 111 steps leading to EQU were deleterious, and in 3 of the 23 successful populations EQU depended on a mutation that was harmful when it arose [@lenski2003]. Complex features were built from simpler ones that had been useful on their own. The "10,000 organisms, 20,000 generations a day" throughput figure is real but dates from a 2009 desktop [@ofria2009]; in 2024 a wafer-scale implementation of a simpler agent model reached over a million generations a minute with up to 16 million agents [@moreno2024].

**PolyWorld** (Yaeger, 1994) gave organisms vision and neural networks that learn by a Hebbian rule. Its organisms evolved fleeing, fighting back, grazing, foraging, following and flocking. They could also signal by changing the brightness of their bodies, but Yaeger reported that "no evidence of their use of this form of communication has yet been found" [@yaeger1994]. The first edition of this paper claimed the opposite.

### 2.7 Continuous and neural cellular automata

**Lenia** generalises Conway's Game of Life to continuous space, time and states. Bert Wang-Chak Chan's original paper catalogued "more than 400 species in 18 families" that move, rotate and organise themselves [@chan2019]. *Expanded Lenia* (ALIFE 2020) added multiple kernels and channels and found self-replication, emission and "virtual eukaryotes" [@chan2020]. Hamon and colleagues later used diversity search to discover Lenia creatures that show sensorimotor agency (Science Advances, 2025) [@hamon2025].

**Flow-Lenia** makes mass conserved and lets each creature carry its own parameters, so that species can compete and evolve inside one world. It was posted in December 2022 and won the ALIFE 2023 best paper award [@plantec2022]; the extended journal version appeared in *Artificial Life* in 2025 under a new title [@plantec2025]. The authors describe it as "an important step towards" open-ended evolution, not an achievement of it.

**Neural cellular automata** (NCA) learn the update rule itself. Growing NCA (2020) trained a single shared rule of about 8,000 parameters to grow a pattern and repair damage to it [@mordvintsev2020]. Biomaker CA (2023) evolves plant-like ecosystems in JAX [@randazzo2023], and DiffLogic CA (2025) learned the Game of Life exactly as a circuit of 336 logic gates [@difflogic2025]. Particle Lenia (2022) reformulated Lenia in terms of particles and energy [@particlelenia2022].

### 2.8 Life from noise

The most striking ALife result of the period needs no hand-written ancestor at all. In *Computational Life* (2024), Agüera y Arcas and colleagues filled a soup with 2^17 random 64-byte programs written in a minimal Brainfuck-like language. Programs are paired at random, concatenated, executed and split again; there is no fitness function. In about 40% of runs a sudden transition to self-replicators happens within 16,000 epochs, with or without background mutation. The same happens in a Forth-like language almost every time, and never in SUBLEQ [@aguera2024]. Tierra and Avida begin with a replicator; here replication itself emerges from interaction and self-modification. The paper is still a preprint.

### 2.9 Emergent social structure in learning agents

Three 2023 to 2024 studies show reinforcement-learning populations inventing social structure that was never programmed:

- **Dominance hierarchies.** Agents "invent, learn, enforce, and transmit a dominance hierarchy to new populations" [@rachum2024].
- **Exchange and tolerated theft.** Given a campfire where they spend downtime together, agents developed a drop-and-pick-up exchange protocol and tolerated theft, without any explicit trade, punishment or combat mechanics [@garbus2023].
- **Massive-agent coordination.** In Lux, with up to 1,000 agents per team, behaviour developed in three stages, from atomic skills to regional coordination to global strategy [@chen2023].

Emergent communication has its own literature; Boldt and Mortensen's 2024 review is the best entry point [@boldt2024]. The same kinds of convention-formation now appear in populations of language models (Section 4.4).
