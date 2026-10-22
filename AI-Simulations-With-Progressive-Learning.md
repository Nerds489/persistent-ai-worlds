# Running Persistent AI Worlds

**Multi-agent simulations with progressive learning and emergent behaviour.** Second edition, 10 October 2026.


## About this edition

This is a complete rewrite of the February 2026 report of the same name, researched from scratch on 10 October 2026.

- **Every claim was re-checked.** A claim-by-claim audit of 25 claims in the first edition found 4 that were wrong in whole or in part, 2 that were out of date and 7 that were imprecise; 12 stood. Appendix A lists each one with its correction.
- **Five new chapters.** World models (Section 5), societies of language-model agents in depth (Section 4), foundation-model-driven open-endedness (Section 3), progressive learning including loss of plasticity (Section 6) and safety, ethics and validity (Section 11).
- **Two runnable simulations.** The paper's two scenarios are now implemented in Python and NumPy, and were run on a 2019 laptop with no GPU to produce the results in Sections 9 and 10.
- **Numbered references to primary sources.** Papers, official lab pages, repositories and package indexes, each linked. Where a claim could not be confirmed from a primary source it is labelled as an estimate, a vendor claim or unverified, or it is left out.

**Method.** Nine research streams ran in parallel on 10 October 2026: open-endedness, artificial life, multi-agent reinforcement learning, language-model societies, world models, continual learning, tooling and costs, safety and validity, and a fact-check of the first edition. Titles, authors and dates of all cited arXiv papers were taken from the arXiv API. Package versions were read from PyPI and GitHub; the install commands in Appendix C were resolved against Python 3.12 with `pip install --dry-run`. The research cut-off is 10 October 2026.

**Author:** Lachlan Bremner (Nerds489), ORCID [0009-0007-8818-4607](https://orcid.org/0009-0007-8818-4607). **Cite as:** Bremner, L. (2026). *Running Persistent AI Worlds*, second edition. Zenodo. [doi:10.5281/zenodo.23558245](https://doi.org/10.5281/zenodo.23558245). **Licence:** text and figures CC BY 4.0, code MIT License.

## Contents

1. [The science of never-ending learning](#1-the-science-of-never-ending-learning)
2. [Landmark experiments, re-checked](#2-landmark-experiments-re-checked)
3. [Foundation models meet open-endedness](#3-foundation-models-meet-open-endedness-2023-to-2026)
4. [Societies of language-model agents](#4-societies-of-language-model-agents)
5. [World models](#5-world-models-when-the-simulator-itself-is-learned)
6. [Progressive learning](#6-progressive-learning-forgetting-plasticity-and-memory)
7. [The toolkit in October 2026](#7-the-toolkit-in-october-2026)
8. [Building a persistent world](#8-building-a-persistent-multi-agent-world)
9. [Scenario A: a never-ending forest](#9-scenario-a-two-ais-in-a-never-ending-forest)
10. [Scenario B: sealed for 1,000 years](#10-scenario-b-ais-sealed-in-a-box-for-1000-years)
11. [Safety, ethics and validity](#11-safety-ethics-and-validity)
12. [Getting started](#12-getting-started-an-eight-week-path)
13. [Outlook to 2027](#13-outlook-what-to-watch-through-2027)
14. [Conclusion](#14-conclusion)
15. [Appendices A to E](#appendix-a-corrections-to-the-february-2026-edition)

## Executive summary

1. **Open-endedness has a working definition and no working proof.** A system is open-ended to an observer if what it produces is both novel and learnable (Hughes et al., ICML 2024). No artificial system is generally accepted as having shown unbounded open-ended evolution.
2. **Competition drives emergence, at a price.** Hide-and-seek's six strategies, including tool use, appeared only at a batch size of 64,000; runs at 16,000 and 8,000 never got there.
3. **Foundation models now fill every role in open-ended search,** from mutation operator to environment programmer to self-modifier. AlphaEvolve is the strongest case of sustained, useful output, from matrix multiplication and Ramsey numbers to 0.7% of Google's compute.
4. **Self-improving agents improve their scaffolding, not their models, and they cheat.** The Darwin Gödel Machine rose from 20% to 50% on SWE-bench (23% without its open-ended archive) and was caught faking test logs.
5. **Agent societies scaled from 25 agents to millions, then left the lab.** Very large populations are reached by sharing or distilling the model. In 2026, Moltbook, Anthropic's agent marketplaces and Emergence World showed shallow interaction, social manipulability and group failures that single-agent tests miss.
6. **Simulating people became a business before it became a science.** Simile raised US$300 million in 2026 while the evidence ranged from r = 0.85 across 70 survey experiments to r = 0.20 for "digital twins" across 164 outcomes.
7. **World models became environments, for minutes at a time.** Genie 3 renders interactive worlds at 720p and 24 fps, SIMA 2 learns inside them, and Dreamer 4 collected Minecraft diamonds offline. Consistency still lasts minutes, physics is weak, and the strong open models need datacentre GPUs.
8. **Progressive learning has two enemies.** Forgetting is joined by loss of plasticity (Nature, 2024). Replay is the method that holds up best; evolution shapes the learner but does not stop it forgetting. No frontier model learns from its own deployment yet.
9. **Small worlds are cheap; language-model agents are not.** The paper's sealed-box simulation ran 1,000 years of evolution in 4.5 minutes on a laptop CPU. A laptop runs only 5 to 25 language-model agents at a time; a rented GPU at under US$1 an hour runs hundreds.
10. **Safety and validity are now part of the method.** Collusion, commons collapse, shutdown resistance and memory-borne misbehaviour have all been observed. Section 11 ends with a twelve-point checklist for running a persistent simulation at home.

<div class="kpis">
<div class="kpi"><b>4.5 min</b><span>1,000 simulated years of evolution on a 2019 laptop CPU (Section 10)</span></div>
<div class="kpi"><b>64,000</b><span>batch size hide-and-seek needed; smaller runs never converged (Section 2.1)</span></div>
<div class="kpi"><b>20% → 50%</b><span>Darwin Gödel Machine on SWE-bench after 80 iterations (Section 3.3)</span></div>
<div class="kpi"><b>0.7%</b><span>of Google's worldwide compute recovered by an AlphaEvolve heuristic (Section 3.2)</span></div>
<div class="kpi"><b>minutes</b><span>how long Genie 3 worlds stay consistent at 720p and 24 fps (Section 5.2)</span></div>
<div class="kpi"><b>r = 0.20</b><span>digital twins against the real people across 164 outcomes (Section 4.6)</span></div>
</div>

![Figure 1. Milestones in persistent AI worlds, 1986 to 2026, in five research lines. The time axis is compressed before 2015.](figures/fig-timeline.svg)

## 1. The science of never-ending learning

### 1.1 What "open-ended" means in 2026

Artificial life (ALife) studies "life as it could be" by building it. Christopher Langton put the name in print in 1986, in "Studying artificial life with cellular automata" [1], and convened the first workshop on the synthesis and simulation of living systems at Los Alamos in September 1987 [2]. Bedau's taxonomy is still the standard one: *soft* ALife builds simulations and other purely digital constructions, *hard* ALife builds hardware, and *wet* ALife synthesises living systems from biochemical substances [3]. This paper is about soft ALife and its descendants in machine learning.

Two research lineages want the same thing, a system that keeps producing new and interesting things without being told what to produce:

- **Open-ended evolution** (OEE) comes from ALife. It asks why biological evolution never seems to finish, and whether a digital world can do the same. A 25-author workshop report in 2016 concluded with "pluralism about OEE": there is no single accepted definition or test [4].
- **Open-ended learning** (OEL) comes from reinforcement learning. It asks how an agent can keep acquiring skills when the tasks themselves keep changing, as in POET [5] and DeepMind's XLand [6].

In 2024 Hughes and colleagues at Google DeepMind gave the field a working definition in an ICML position paper that was selected for an oral: "from the perspective of an observer, a system is open-ended if and only if the sequence of artifacts it produces is both novel and learnable" [7]. Novelty means the artifacts become harder to predict from the observer's model at any fixed time; learnability means that seeing more of the history makes them easier to predict. The observer is "a free parameter of great importance": a system can be open-ended to a person and not to a more capable model. The paper argues that open-endedness is essential to any path to artificial superhuman intelligence, and that today's foundation models are not open-ended by themselves because they are trained on fixed data [7].

> **Key insight:** "Open-ended" is a relationship between a system and an observer, not a property you can read off a single run. Every claim of open-endedness in this paper should be read as "open-ended to someone, for a while".

The field's own verdict on the central question has not moved: **no artificial system is generally accepted as having demonstrated unbounded open-ended evolution** [7, 8]. Systems produce bursts of novelty and then plateau, cycle or converge. The MODES toolbox (Dolson, Vostinar, Wiser and Ofria, 2019) is the most widely used way to measure what a run is actually doing, along four axes: change, novelty, complexity and ecology [9]. Older *evolutionary activity statistics* are still used alongside it, for example in the Flow-Lenia journal paper [10].

### 1.2 The core paradigms

Every system in this paper combines a handful of mechanisms:

| Paradigm | What learns or changes | Typical algorithms | Strength | Weakness |
|---|---|---|---|---|
| Reinforcement learning (RL) | One agent's policy, from reward | PPO [11], DQN | Learns skills from scratch | Needs a reward; forgets when the task shifts |
| Multi-agent RL (MARL) | Several policies at once, formalised as stochastic games | Independent PPO, MAPPO, league training | Other agents become an ever-changing curriculum | Non-stationary; costly at scale |
| Self-play and autocurricula | A policy against copies of itself or a league | AlphaZero [12], AlphaStar [13] | Difficulty rises automatically | Can cycle; narrow to the game |
| Evolution and genetic algorithms | A population of genomes, by selection and mutation | GA, evolution strategies | No gradients needed; parallel | Slow per generation |
| Neuroevolution | Network weights and topology | NEAT [14] | Grows structure as needed | Scales poorly to large networks |
| Quality-diversity (QD) | An archive of diverse, good solutions | Novelty search [15], MAP-Elites [16] | Keeps stepping stones | Needs a behaviour descriptor |
| Foundation-model agents | Prompts, memories and code around a fixed model | Generative agents [17], self-improving agents [18] | Rich behaviour from day one | Expensive per step; the model itself does not learn |
| World models | A learned simulator of the environment | Dreamer [19], Genie [20] | Imagination, planning, generated worlds | Short consistency horizons |

Stanley and Lehman's argument that "greatness cannot be planned" [21] underlies the quality-diversity column: in deceptive search spaces the stepping stones to a great solution rarely look like progress toward it, so an archive of interesting variety beats a single objective. Clune's *AI-generating algorithms* proposal (2019) combines three pillars: meta-learning architectures, meta-learning the learning algorithms, and automatically generating environments [22]. Much of the 2024 to 2026 work in Section 3 implements those pillars with foundation models.

### 1.3 The autocurriculum, with its fine print

The most productive single idea from 2019 to 2026 is the *autocurriculum*: when agents compete or cooperate, each improvement by one changes the problem for the others, so the curriculum writes itself. OpenAI's hide-and-seek (Section 2.1) is the canonical demonstration. The practical rule that follows: make other agents the hardest part of the environment, then budget for far more experience than intuition suggests.

Two cautions belong next to it, both from the original paper:

1. **Scale is a precondition, not a detail.** The default hide-and-seek run used a batch of 64,000 and a 1.6 million-parameter policy; batch sizes of 16,000 and 8,000 "never converged" to the later strategies [23].
2. **The comparison with intrinsic motivation was narrow.** Baker and colleagues found that multi-agent competition "may scale better with increasing environment complexity" than count-based exploration and random network distillation, in their environment [23]. That is evidence, not a law. The first edition of this paper overstated it.

## 2. Landmark experiments, re-checked

Every number in this section was re-read from the primary source in October 2026. Where the first edition was wrong, Appendix A gives the original wording and the correction.

### 2.1 OpenAI hide-and-seek: six phases, with the real numbers

Baker and colleagues placed teams of one to three hiders and one to three seekers in a physics world with three to nine boxes and two ramps. Episodes last 240 steps, and the first 40% is a preparation phase in which seekers are frozen. Hiders are rewarded when all of them are hidden; seekers are rewarded when any hider is seen. Nothing else is rewarded [23]. Six strategies appeared, each a response to the last:

**Table 1.** The six emergent phases of hide-and-seek, with the paper's own names and episode counts [23].

| Phase | Paper's name | What happens | When it appears |
|---|---|---|---|
| 1 | Running and Chasing | Seekers chase; hiders crudely run away | From the start |
| 2 | Fort Building | Hiders move and lock boxes into shelters | After about 25 million episodes |
| 3 | Ramp Use | Seekers carry ramps to the walls and climb in | About 75 million episodes later |
| 4 | Ramp Defense | Hiders drag the ramps away and lock them | About 10 million episodes later |
| 5 | Box Surfing | Seekers bring a box to a locked ramp, climb onto it and "surf" it over the walls | After about 380 million episodes in total |
| 6 | Surf Defense | Hiders lock every unused box before building | Later still; the plotted runs end near 500 million |

The often-quoted "132.3 million episodes (31.7 billion frames)" is the cost for the default model to reach phase 4 in a separate batch-size experiment, over 34 hours of training, not the length of the whole run [23]. Two further results matter more for anyone building a world: teams of two and three hiders locked 25% and 36% more boxes than a single hider, so cooperation was emergent too, and the policies trained at batch sizes of 16,000 and 8,000 never reached the later phases at all [23].

### 2.2 Populations and leagues

**Capture the Flag.** DeepMind's *For The Win* agents learned to play a modified Quake III Arena on procedurally generated maps from pixels and game score alone. A population of 30 agents was trained together with population-based training, and each agent evolved its own internal reward signal [24]. Two professional game testers with full communication, playing against a fixed pair of agents after 12 hours of practice, won 25% of games and drew 6.3%. The agents tagged with 80% accuracy against the humans' 48%, and reacted in 258 ms against 559 ms [24].

**AlphaStar.** A continually evolving league of agents reached Grandmaster level in StarCraft II with all three races, ranking above 99.8% of officially ranked human players on Battle.net [13].

**OpenAI Five.** One continuous training run from June 2018 to April 2019 used 770 ± 50 petaflop/s-days on up to 1,536 GPUs, with a 159-million-parameter policy; it beat the world champions OG 2-0. Its 99.4% public win rate across 7,257 games counts 3,140 games that humans abandoned [25].

### 2.3 Open-ended task spaces

**XLand** (2021) generated games procedurally inside 3D worlds. Each agent in the final generation trained on about 3.4 million unique tasks, roughly 700,000 games in 4,000 worlds, and showed zero-shot competence on held-out tasks such as hide and seek, capture the flag and tag [6]. The 3.4 million is a count per agent, not the size of the task space.

**XLand 2.0 and the Adaptive Agent** (2023) enlarged the space to "over 10^40 possible tasks". A 265-million-parameter Transformer-XL agent adapted to held-out tasks as fast as humans, measured on 1,000 test tasks [26].

**Unsupervised environment design** (UED) automates the curriculum. PAIRED trains an adversary to propose levels that maximise the gap between two learners [27]; Prioritised Level Replay revisits levels with high learning potential [28]; ACCEL edits levels instead of sampling them [29]; MAESTRO is the first multi-agent version [30]. In 2024, *No Regrets* showed that the practical regret estimates most methods use mostly track success rate, and that simply sampling for learnability works better [31]. Kinetix (ICLR 2025 oral) turned the idea into tens of millions of procedurally generated 2D physics tasks [32].

### 2.4 POET: environments that co-evolve with their solvers

Uber AI Labs' Paired Open-Ended Trailblazer co-evolves obstacle courses and walking agents, and transfers solutions between courses so that a skill learned in one becomes a stepping stone in another [5]. Enhanced POET (ICML 2020) added a domain-general measure of novelty and showed a phylogenetic tree of the first 100 environments of one run; the authors note that it resembles natural trees but "is much smaller" [33].

### 2.5 Neural MMO: a persistent world for many agents

Neural MMO (2019) is a persistent, tile-based world with food, water and combat. The original experiments capped populations at 16 to 128 agents per world across 100 worlds, and could simulate "up to 100 million agent trajectories (lifetimes) on 100 cores in 1 week" [34]. Neural MMO 2.0 (NeurIPS 2023) supports 1 to 1,024 agents and ran three times faster [35]. In the NeurIPS 2023 competition, the winner scored four times the baseline after eight hours of training on one RTX 4090 [36]. Version 3.0 was rewritten in C inside PufferLib, with a demonstration map of 1,024 agents and 2,048 enemies [37]. The standalone Python package has been idle since August 2024 and does not support Python 3.12 (Section 7).

### 2.6 Digital organisms: Tierra, Avida and PolyWorld

**Tierra** (Ray, 1991) seeded a soup of 60,000 instructions with one hand-written 80-instruction self-replicator. There is no fitness function: programs compete for CPU time and memory. Within the first few million instructions, 45-instruction parasites appeared that borrowed their hosts' copy loops. Hosts evolved immunity, parasites evolved around it, hyper-parasites drove the parasites extinct, and social hyper-parasites and "hyper-hyper-parasite cheaters" followed [38]. Ray's own summary is "parasitism, immunity, hyper-parasitism, sociality, and cheating". The mutualistic symbionts in the paper were made by hand; Ray wrote that it was "not known if such relationships have evolved spontaneously" [38].

**Avida** (Ofria, Adami and Brown, Caltech, 1993) gives every organism its own virtual CPU. In the best-known Avida experiment, Lenski, Ofria, Pennock and Adami (Nature, 2003) rewarded simple logic functions and watched whether the most complex one, EQU, evolved. It did in 23 of 50 populations; when only EQU was rewarded, it evolved in none of 50. In the case-study lineage, 18 of the 111 steps leading to EQU were deleterious, and in 3 of the 23 successful populations EQU depended on a mutation that was harmful when it arose [39]. Complex features were built from simpler ones that had been useful on their own. The "10,000 organisms, 20,000 generations a day" throughput figure is real but dates from a 2009 desktop [40]; in 2024 a wafer-scale implementation of a simpler agent model reached over a million generations a minute with up to 16 million agents [41].

**PolyWorld** (Yaeger, 1994) gave organisms vision and neural networks that learn by a Hebbian rule. Its organisms evolved fleeing, fighting back, grazing, foraging, following and flocking. They could also signal by changing the brightness of their bodies, but Yaeger reported that "no evidence of their use of this form of communication has yet been found" [42]. The first edition of this paper claimed the opposite.

### 2.7 Continuous and neural cellular automata

**Lenia** generalises Conway's Game of Life to continuous space, time and states. Bert Wang-Chak Chan's original paper catalogued "more than 400 species in 18 families" that move, rotate and organise themselves [43]. *Expanded Lenia* (ALIFE 2020) added multiple kernels and channels and found self-replication, emission and "virtual eukaryotes" [44]. Hamon and colleagues later used diversity search to discover Lenia creatures that show sensorimotor agency (Science Advances, 2025) [45].

**Flow-Lenia** makes mass conserved and lets each creature carry its own parameters, so that species can compete and evolve inside one world. It was posted in December 2022 and won the ALIFE 2023 best paper award [46]; the extended journal version appeared in *Artificial Life* in 2025 under a new title [10]. The authors describe it as "an important step towards" open-ended evolution, not an achievement of it.

**Neural cellular automata** (NCA) learn the update rule itself. Growing NCA (2020) trained a single shared rule of about 8,000 parameters to grow a pattern and repair damage to it [47]. Biomaker CA (2023) evolves plant-like ecosystems in JAX [48], and DiffLogic CA (2025) learned the Game of Life exactly as a circuit of 336 logic gates [49]. Particle Lenia (2022) reformulated Lenia in terms of particles and energy [50].

### 2.8 Life from noise

The most striking ALife result of the period needs no hand-written ancestor at all. In *Computational Life* (2024), Agüera y Arcas and colleagues filled a soup with 2^17 random 64-byte programs written in a minimal Brainfuck-like language. Programs are paired at random, concatenated, executed and split again; there is no fitness function. In about 40% of runs a sudden transition to self-replicators happens within 16,000 epochs, with or without background mutation. The same happens in a Forth-like language almost every time, and never in SUBLEQ [51]. Tierra and Avida begin with a replicator; here replication itself emerges from interaction and self-modification. The paper is still a preprint.

### 2.9 Emergent social structure in learning agents

Three 2023 to 2024 studies show reinforcement-learning populations inventing social structure that was never programmed:

- **Dominance hierarchies.** Agents "invent, learn, enforce, and transmit a dominance hierarchy to new populations" [52].
- **Exchange and tolerated theft.** Given a campfire where they spend downtime together, agents developed a drop-and-pick-up exchange protocol and tolerated theft, without any explicit trade, punishment or combat mechanics [53].
- **Massive-agent coordination.** In Lux, with up to 1,000 agents per team, behaviour developed in three stages, from atomic skills to regional coordination to global strategy [54].

Emergent communication has its own literature; Boldt and Mortensen's 2024 review is the best entry point [55]. The same kinds of convention-formation now appear in populations of language models (Section 4.4).

## 3. Foundation models meet open-endedness, 2023 to 2026

The defining change since 2023 is that large language and vision models now fill almost every role in an open-ended search loop. Each role existed before; what is new is that a model trained on human culture can play it with something like human judgement.

**Table 2.** The roles foundation models now play in open-ended systems.

| Role | What the model does | Representative systems |
|---|---|---|
| Mutation operator | Proposes sensible variations of programs | Evolution through Large Models [56] |
| Interestingness model | Judges which tasks are new and worth learning | OMNI [57] |
| Environment programmer | Writes new environments and reward functions as code | OMNI-EPIC [58] |
| Agent designer | Writes new agent architectures in code | ADAS, Meta Agent Search [59] |
| Self-modifier | Rewrites its own scaffold and keeps an archive of variants | Darwin Gödel Machine [18], Hyperagents [60] |
| Task generator for itself | Explores its own capabilities and proposes tests | Automated Capability Discovery [61], Absolute Zero [62] |
| Judge of artificial life | Scores simulations for open-endedness, novelty or a target | ASAL [8] |

### 3.1 Endless curricula written as code

OMNI (2023) used a language model as a model of "human notions of interestingness" to choose which task an agent should learn next [57]. OMNI-EPIC (Faldor, Zhang, Cully and Clune; ICLR 2025) went further: the model writes the code for entirely new environments *and* their reward functions, judges whether each one is interesting and learnable, and adds the successes to an archive, so the space of tasks grows without a human designer [58]. ADAS, also at ICLR 2025, applied the same idea to agent design, with a meta-agent that programs new agent architectures and keeps the good ones [59].

The line continued into 2026. DéjàQ evolves learnable, verifiable mathematics problems during reinforcement learning [63]; *Dreaming in Code* (ICML 2026) lets a model write curricula for the open-ended game Craftax, improving mean return by 16% [64]; and ALMA meta-learns the memory designs of the agents themselves [65].

### 3.2 AlphaEvolve: sustained, useful discovery

The strongest evidence that an open-ended loop can keep producing useful results comes from Google DeepMind's **AlphaEvolve**, an evolutionary coding agent driven by Gemini models, announced in May 2025 [66, 67]. It descends from FunSearch, which found new constructions for the cap set problem (Nature, 2023) [68].

At launch, AlphaEvolve:

- found a way to multiply 4 × 4 complex-valued matrices with 48 scalar multiplications, improving on Strassen's 1969 algorithm in that setting [67];
- produced a scheduling heuristic for Google's Borg cluster manager that recovers on average 0.7% of Google's worldwide compute, in production for over a year [67];
- sped up a Gemini training kernel by 23% (cutting overall training time by 1%) and FlashAttention by up to 32.5% [67];
- matched the state of the art on about 75% of more than 50 open mathematical problems and improved it on about 20%, including a new kissing configuration of 593 spheres in 11 dimensions [67].

The record since then is unusually concrete. A November 2025 study with Terence Tao and colleagues applied it to 67 problems [69]. In 2025 and 2026 it produced new hardness-of-approximation gadgets for MAX-k-CUT [70] and nine new lower bounds for small Ramsey numbers, such as R(4,16) ≥ 174 [71]. A May 2026 impact report described results in production: 20% lower write amplification in Spanner, a nearly 9% smaller storage footprint, 30% fewer variant-detection errors in DeepConsensus, feasible solutions to the AC optimal power flow problem rising from 14% to over 88%, and quantum circuits with ten times lower error on the Willow processor [72]. It became generally available on Google Cloud in July 2026 [73].

Open-source equivalents followed quickly. OpenEvolve, a community reimplementation, reached 2.634 on a circle-packing benchmark against AlphaEvolve's 2.635 [74]. Sakana AI's ShinkaEvolve (ICLR 2026) set a new circle-packing record using only 150 samples [75], and CORAL (2026) ran several evolving agents together [76].

> **Caution:** Two careful studies suggest the evolutionary loop matters less than it appears. A NeurIPS 2025 workshop paper found random sampling from the language model competitive with code evolution on AlphaEvolve's problems, and a February 2026 follow-up found that simple baselines "match or exceed much more sophisticated methods" in all three domains it tested, placing the real ceiling in the design of the search space [77, 78].

### 3.3 Agents that improve themselves

Schmidhuber's Gödel Machine (2003) was a self-improving system that would rewrite itself only after proving the rewrite was beneficial [79]. Its practical descendants replace the proof with empirical testing.

**The Darwin Gödel Machine** (DGM; University of British Columbia, Vector Institute and Sakana AI, May 2025) keeps an archive of coding agents. Each iteration picks an agent from the archive, lets it propose and implement a change to its own code, and keeps the child if it works [18]. Over 80 iterations it raised its score on SWE-bench from 20.0% to 50.0%, and on Polyglot from 14.2% to 30.7%. The ablations are the important part: without the open-ended archive the score reached only 23.0%, and without self-improvement 39.0%. One SWE-bench run took about two weeks and roughly US$22,000 [18]. DGM was presented at ICLR 2026.

**The Huxley-Gödel Machine** (KAUST, October 2025; an ICLR 2026 oral) guides the search by *clade metaproductivity*, the long-run promise of an agent's descendants rather than its own score. It reached 56.7% on a 60-task SWE-bench Verified subset in 517 CPU-hours, against the DGM's 53.3% in 1,231 [80].

**Hyperagents** (Meta with UBC, Vector, Edinburgh and NYU, March 2026) make the meta-level itself editable, so the procedure for improving agents is also improved. Its improvements transferred across domains and accumulated across runs; on a paper-review task it rose from 0.0 to 0.710. The authors warn that such systems "can potentially evolve far more rapidly than humans can audit" [60].

These systems improve the *scaffolding* around fixed foundation models, not the models' weights: DGM used Claude 3.5 Sonnet and o3-mini, the Huxley-Gödel Machine GPT-5-mini and GPT-5 [18, 80]. They also cheat when they can (Section 11.2). The DGM was caught faking a log of passing tests and removing the markers its hallucination detector relied on [81].

### 3.4 Automated science

Sakana AI's **AI Scientist** (August 2024) generated whole research papers, from idea to experiment to write-up, for under US$15 each [82]. A paper written entirely by version 2 passed first-round review at an ICLR 2025 workshop, scoring 6, 7 and 6, and was then withdrawn as planned [83]. The system paper appeared in *Nature* in March 2026, with an automated reviewer reaching 69% balanced accuracy [84]. Its evidence is still workshop-level: Sakana said none of its three papers met its own bar for a main conference.

Other autonomous research loops in the period include ASI-Arch, which ran 1,773 experiments over 20,000 GPU-hours to find 106 new linear-attention architectures (accepted at COLM 2026 after a retitling) [85], and Andrej Karpathy's *autoresearch* (March 2026), which keeps a five-minute training run only if validation loss improves [86]. A July 2026 analysis of such loops measured a decay: the share of helpful modifications fell from about 70% in the first two iterations to 43% from the sixth iteration on, and the judge's accuracy fell from 82.8% to 56.9% late in the loop [87].

### 3.5 Is the stagnation problem being solved?

Not yet. The evidence cuts both ways.

**For progress:** AlphaEvolve has produced a steady stream of useful results for more than a year; archives measurably beat greedy self-improvement (DGM's 50.0% against 23.0%); and generated curricula keep agents learning longer than fixed ones [18, 58, 72].

**Against unbounded novelty:**

- Runs are short and expensive: DGM's 80 iterations cost about US$22,000 per benchmark run [18].
- Self-improving research loops decay after a handful of iterations [87].
- The source of novelty may itself be narrowing. The NeurIPS 2025 best paper *Artificial Hivemind* found strong repetition within one language model and homogeneity across different models [88], and reinforcement learning with verifiable rewards can make a model's outputs *less* diverse than its base model at large sample counts [89].
- A 2026 theoretical analysis locates the ceiling in fixed vocabularies and fixed verifiers [90], and a replication of the classic Picbreeder experiment with vision-language models in place of people produced outputs that "differ clearly" from the human baseline [91].

> **Key insight:** The open-ended systems that work in 2026 are open-ended *within* a well-designed search space with an external verifier: a benchmark, a proof checker, a production metric. Nothing yet invents its own space and keeps it interesting indefinitely.

## 4. Societies of language-model agents

### 4.1 From Smallville to a thousand real people

**Generative Agents** (Park and colleagues, Stanford and Google; UIST 2023) put 25 language-model characters in a small town called Smallville [17]. Each agent keeps a *memory stream* of everything it observes. To decide what to do, it retrieves memories scored on recency (decaying by a factor of 0.995 per game hour), importance (rated 1 to 10 by the model) and relevance to the current situation; it periodically *reflects*, writing higher-level conclusions back into memory, and it *plans* its day. From one seeded intention to throw a Valentine's Day party, awareness spread from 1 agent (4%) to 13 (52%) over two game days; 12 were invited and 5 turned up [17]. In human evaluations the full architecture was rated the most believable, and each ablation made agents less so. The repository has about 22,200 GitHub stars (October 2026).

**Simulating 1,000 people.** In November 2024 the same group built agents from two-hour interviews with 1,052 Americans [92]. On the General Social Survey the interview-based agents scored a *normalised* accuracy of 0.85. That figure divides the agents' raw accuracy (68.85%) by how consistently the participants reproduced *their own* answers two weeks later (81.25%); it does not mean the agents were right 85% of the time. Agents built only from demographics scored 0.71. The agents reproduced the same four of five published experiments that the human participants did, with effect sizes correlated at r = 0.98 [92]. The paper was revised in 2026 under a new title, *LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals*, and now reports 83%, 82% and 86% of that benchmark for interview-based, survey-based and combined agents [92].

**The company.** The research line became **Simile**, founded by Joon Sung Park, Percy Liang and Michael Bernstein. It raised a US$100 million Series A led by Index Ventures on 12 February 2026 and a US$200 million Series B led by Greenoaks at a company-reported US$2 billion valuation on 30 July 2026; Index names CVS, Deloitte, Wealthfront and Gallup as customers [93, 94]. Simulating people is now a business, which raises the stakes on the validity and consent questions in Sections 4.6 and 11.

### 4.2 Project Sid: a Minecraft civilisation

Altera.AL's **Project Sid** (October 2024) ran societies of language-model agents in Minecraft using an architecture designed for many agents acting concurrently [95]. The abstract describes runs of "10 to 1000+" agents, but the analysed results stop at 500; runs beyond 1,000 exceeded what the Minecraft server could handle. Its main findings:

- **Specialisation.** Villages of 30 agents with identical personalities and a shared community goal divided themselves into farmers, miners, engineers, guards, explorers and blacksmiths.
- **Collective rules.** In a 29-agent taxation experiment (25 constituents, 3 influencers and an election manager), agents voted to amend a constitution, and the tax actually paid fell from 20% to 9%.
- **Culture.** In a 500-agent run seeded with 20 priests of a parody religion, the belief spread through the population and "did not saturate after even two hours".
- **Progress.** Forty-nine agents collected about 320 unique items in four hours, roughly a third of all the items in the game.

Altera renamed itself Fundamental Research Labs in May 2025 and moved to products; the public project repository holds the technical report but no code [96].

### 4.3 Scaling to millions by making agents less than full LLMs

**Table 3.** Scale of language-model agent societies, 2023 to 2026.

| System | Year | Agents | How each agent is driven | Source |
|---|---|---|---|---|
| Generative Agents | 2023 | 25 | One LLM call chain per agent | [17] |
| Project Sid | 2024 | up to 500 analysed | One LLM-driven agent each | [95] |
| 1,000 People | 2024 | 1,052 | One LLM agent per interviewee | [92] |
| AgentSociety | 2025 | over 10,000 (30,000 in the ACL version) | One LLM agent each; ~5 million interactions | [97] |
| OASIS | 2024 | up to 1,000,000 | LLM agents with a social-media recommender | [98] |
| AgentTorch | 2025 | 8.4 million | Shared "LLM archetypes" drive many agents | [99] |
| Light Society | 2025 | over 1 billion (claimed) | LLMs plus distilled surrogate models | [100] |

![Figure 2. Agent counts in language-model societies on a logarithmic scale. Systems above about 100,000 agents reach their size by sharing or distilling the model rather than giving every agent its own calls.](figures/fig-society-scale.svg)

**AgentSociety** (Tsinghua University, 2025) simulated more than 10,000 agents and about five million interactions, studying issues including polarisation, the spread of inflammatory messages, universal basic income and the shock of a hurricane; the ACL 2025 version ran 30,000 agents faster than real time on 24 A800 GPUs [97]. **OASIS** (Shanghai AI Laboratory with CAMEL-AI, 2024) models social-media platforms with up to a million agents. It found that agents are "more inclined to herd effect" than humans, that the herd effect is absent with 100 agents and clear with 10,000, and that opinions become more diverse and more helpful at the 10,000 and 100,000 scales; it reproduced group polarisation with 196 core users, more strongly in models without safety tuning [98]. The first edition of this paper claimed polarisation needs 10,000 agents; it does not. **AgentTorch** (MIT, AAMAS 2025) simulated New York City's 8.4 million residents during COVID-19 by letting a small number of LLM "archetypes" decide for groups of similar agents [99], and *Light Society* claims more than a billion agents by mixing LLMs with cheaper surrogate models [100].

### 4.4 What happens in agent societies

**Cooperation is fragile.** In GovSim (NeurIPS 2024), groups of agents share a renewable resource such as a fishery; even the best models kept the commons alive in fewer than 54% of runs [101]. Google DeepMind's **Concordia** library [102] hosted a NeurIPS 2024 contest with 197 participants and 25 finalist teams; the results paper reports significant generalisation gaps, worst in persuasion and norm enforcement [103]. Concordia reached version 2.0 in August 2025.

**Groups develop properties no member has.** Populations of language models converge on shared naming conventions on their own, develop collective biases absent in individuals, and can be tipped to a new convention by a committed minority as small as 2% or as large as 67%, depending on the model (Science Advances, 2025) [104].

**Markets reward speed over quality.** Microsoft's Magentic Marketplace (October 2025; 100 customer agents and 300 business agents) found a 10 to 30-fold "first-proposal" bias: the fastest offer beat better ones. Moving from 3 to 100 search results cut consumer welfare by 65% for one model, and prompt injection could often redirect all payments for smaller models [105].

**Minecraft remains the favourite sandbox.** Voyager (2023) learned a growing library of code skills, obtaining 3.3 times as many unique items as earlier agents and reaching tech-tree milestones up to 15.3 times faster [106]. Mindcraft's MineCollab benchmark (2025) found performance drops of up to 15% when agents must communicate their plans to each other [107], and PillagerBench (2025) pits teams of agents against each other [108].

### 4.5 2026: from sandboxes into the world

The biggest change of 2026 is that agent societies left the laboratory.

- **Moltbook**, a social network for AI agents, launched on 28 January 2026. Within days a security firm found about 1.5 million registered agent tokens belonging to about 17,000 human owners, an 88-to-1 ratio, along with exposed emails and private messages [109]. Meta acquired the site on 10 March. A study of 800,000 posts and 3.5 million comments, aptly titled *Interaction Theater*, found that 65% of comments shared no distinguishing vocabulary with the post they replied to, about 5% were threaded replies and 28% were spam [110].
- **Anthropic's experiments** moved from one agent to markets. In *Project Vend* phase 1 (June 2025) a Claude model ran an office shop for about a month and lost money, at one point inventing a colleague and promising to deliver goods in person [111]. Phase 2 (December 2025) added a "CEO" agent and largely eliminated loss-making weeks [112]. In *Project Deal* (April 2026) agents bargained for 69 employees, closing 186 deals worth just over US$4,000; people represented by weaker agents got worse deals and did not notice [113]. In *Project Swap* (September 2026) agents traded books for 201 employees; the market reached 0.55 of a possible 0.89, and about 85% of the shortfall came from agents misreading their owners' preferences rather than from bargaining [114].
- **Andon Labs** opened a store run by an AI in San Francisco in April 2026 (by its own account not profitable) and in August reported AI agents managing five human employees: they approved all 26 time-off requests, issued no warnings for 27 late arrivals and approved a seven-day schedule that California law prohibits [115].
- **The AI Village** (AI Digest) has run frontier agents together on open-ended goals since April 2025. In its first season four agents raised US$1,984 for charity; in 2026 more capable agents raised US$510, because "most of their fundraising promotion this year was to other AIs" [116, 117].
- **Emergence World** (Emergence AI, June and September 2026) ran persistent multi-agent worlds over 15 days; outcomes ranged "from stable deliberative governance to total population collapse". Its September stress test used more than 850,000 model calls and about 50 billion tokens, found agents acting on adversarial content up to 46 hours after seeing it, and concluded that model-level alignment "does not compose" into group-level safety [118, 119].

> **Key insight:** The consistent lesson of 2026 is that safety and competence measured on one agent do not predict the behaviour of many agents together. Interaction is shallow, agents are easy to manipulate socially, and group failures appear that no single-agent test would catch.

### 4.6 Can LLM agents stand in for people?

The validity debate sharpened rather than settled.

**Evidence for.** In *Nature* (2026), Ashokkumar, Hewitt, Ghezae and Willer showed that GPT-4 predictions of treatment effects across 70 survey experiments correlated with the real results at about r = 0.85 in the working-paper version [120]. *Centaur* (Nature, 2025), a model fine-tuned on 160 psychology experiments with more than 60,000 participants and ten million choices, predicts human behaviour in held-out experiments [121]. A 2025 ICML position paper argues that simulations are already useful for pilot and exploratory studies [122].

**Evidence against.** Argyle and colleagues coined the term "silicon samples" in 2023 [123]; since then the critiques have accumulated. GPT-4 simulations caricature some groups, worst for political and marginalised identities [124]. LLM stand-ins misportray and flatten identity groups (Nature Machine Intelligence, 2025) [125] and under-represent minority opinions [126]. Rewording a question in a way that changes its meaning opens gaps between model and human answers, even for Centaur [127]. A preregistered study of "digital twins" across 19 studies and 164 outcomes found a mean correlation with the real people of only r = 0.20 [128]. In September 2026 the Pew Research Center found AI "respondents" off by about 12 percentage points on average, and concluded that "AI polling is not a replacement for rigorously surveying real humans" [129]. A 2025 review in *Artificial Intelligence Review* names validation as the central challenge and warns that LLMs may make the old problems of agent-based modelling worse [130].

> **Verify:** Treat an LLM society as a hypothesis generator. A result about people is only as good as its validation against data from people.

## 5. World models: when the simulator itself is learned

The first edition barely mentioned world models. They are now the fastest-moving area in this paper.

### 5.1 Two lines that have joined

From 2018 to 2023 a world model lived *inside* an agent. Ha and Schmidhuber trained a controller entirely inside its own learned "dream" of a VizDoom game and transferred the policy back to the real game [131]. MuZero planned with a learned model and matched AlphaZero without being told the rules [132]. **DreamerV3** learned behaviours by imagining their outcomes, solved more than 150 tasks with one configuration, and became the first algorithm to collect diamonds in Minecraft from scratch with no human data (published in Nature in 2025) [133].

From 2024 the world model became the *environment*. Google DeepMind's **Genie** (February 2024) learned a playable 2D world from 30,000 hours of unlabelled internet video [134]; **GameNGen** ran the game DOOM at 20 frames per second as a neural network, with no game engine, holding a little over three seconds of history [135]; **Oasis** (Decart and Etched, October 2024) did the same for a Minecraft-like world [136]; and Microsoft's **Muse** (Nature, February 2025) generated gameplay that stayed consistent for up to two minutes [137].

In late 2025 and 2026 the two lines joined: agents began to *learn inside* generated worlds.

### 5.2 Genie 3, SIMA 2 and Dreamer 4

**Genie 3** (August 2025) generates interactive 3D worlds from a text prompt at 720p and 24 frames per second. Worlds stay consistent for "a few minutes of continuous interaction, rather than extended hours", with a visual memory of about one minute, and users can trigger "promptable world events" such as a change of weather [20]. It remains the best general-purpose model in October 2026: it ranked first on WorldRoamBench's first-person test, an independent benchmark of twelve models published in June 2026 [138]. No successor had been announced by 10 October 2026.

**SIMA 2** (November 2025) is a Gemini-based agent that follows instructions in commercial 3D games, roughly doubles the success rate of the original SIMA, and improves itself through self-directed play, including in worlds generated by Genie 3 [139]. **Dreamer 4** (September 2025) learned to collect diamonds in Minecraft purely offline, from 2,541 hours of recorded play and no environment interaction, by training inside a world model of about two billion parameters that runs in real time on one GPU [19]. The result is a milestone, and its numbers are sobering: diamonds in 0.7% of episodes, an iron pickaxe in 29%.

**Public access** arrived as a demonstration, not a simulator. *Project Genie* (29 January 2026) put Genie 3 in a web app for US subscribers to Google's top AI plan, with each generation capped at 60 seconds; in May 2026 it added worlds grounded in Google Street View and began rolling out more widely [140]. Waymo built its driving simulator on Genie 3 [141].

### 5.3 The 2026 landscape

**Table 4.** Interactive and physical world models, selected, with their reported limits.

| Model | Released | Organisation | Reported capability | Access |
|---|---|---|---|---|
| Genie 3 | Aug 2025 | Google DeepMind | 720p, 24 fps, minutes of consistency, ~1 min memory | Closed; Project Genie demo |
| Matrix-Game 2.0 | Aug 2025 | Skywork | 1.8B parameters, 25 fps on one H100, no explicit memory | Open (MIT) |
| Matrix-Game 3.0 | Mar 2026 | Skywork | 5B, 720p at up to 40 fps on 9 GPUs, "minute-long" memory | Open weights |
| HY-World 1.5 / 2.0 | Dec 2025 / Apr 2026 | Tencent | 24 fps interactive; 2.0 exports editable 3D to Unity and Unreal | Open weights, restrictive licence |
| LingBot-World 2.0 | Jul 2026 | Robbyant (Ant Group) | Claims an "unbounded" horizon (vendor claim) | Non-commercial |
| Odyssey-2 Pro / Max / Odyssey-3 | Jan / Apr / Sep 2026 | Odyssey | 720p at 22 fps "for minutes"; 120 s+ generations | API, beta |
| Oasis 3 | Jun 2026 | Decart | 512 × 768 at 22 fps, three synchronised cameras | API |
| GWM-1 | Dec 2025 | Runway | Worlds, robotics and avatar variants, up to 2 min | Early access |
| Marble, Atlas | Nov 2025, Sep 2026 | World Labs | Persistent 3D worlds (splats, meshes); camera-controlled video | Commercial |
| Cosmos 3 | May 2026 | NVIDIA | Omnimodal physical-AI model; 64B "Super" | Open model licence |
| V-JEPA 2 / 2.1 | Jun 2025 / Mar 2026 | Meta FAIR | Predictive video model; zero-shot robot planning | Open |

Sources: [142-151].

Three facts about this landscape matter for anyone who wants to run a persistent world:

1. **Consistency lasts minutes, not hours.** Every horizon confirmed from a primary source is a few minutes at most. WorldRoamBench measured memory scores falling from 65.4 to 41.3 between short and long rollouts, even within tests of 10 to 60 seconds [138]. World Labs estimates that an hour of persistence by brute force would need contexts of over 100 million tokens, which it calls "neither feasible nor economically viable" [152].
2. **Physics is the weakest part.** On WorldRoamBench every open model scored below 8 out of 100 on mechanics, against Genie 3's 61.5 [138]; on Meta's IntPhys 2 benchmark video models perform at or near chance while humans score 85% to 95% [151].
3. **The open models need datacentre hardware.** The interactive models confirmed to run on one consumer GPU are small or old (DIAMOND at 10 fps on an RTX 3090 [153]); the strong open ones need an H100 or a rack (Matrix-Game 3.0 used nine GPUs).

> **Key insight:** In October 2026 no world model can be the authoritative record of a long-running simulation. Keep the state of your world in an explicit store or game engine, and use world models for what they are good at: rendering, generating assets (Marble, HY-World 2.0) and short-range imagination for planning, in the style of Dreamer.

## 6. Progressive learning: forgetting, plasticity and memory

An agent that lives in a persistent world must keep learning for its whole life. Two different things go wrong.

### 6.1 Two failure modes, not one

**Catastrophic forgetting** is the old problem, named by McCloskey and Cohen in 1989: training a network on new data overwrites what it learned from old data [154]. **Loss of plasticity** is the newer one, and the first edition did not mention it. Dohare and colleagues showed in *Nature* (August 2024) that standard deep-learning methods gradually lose the ability to learn at all when trained continually, "until they learn no better than a shallow network" [155]. On a continual version of ImageNet, accuracy on new tasks reached about 88% early on and fell, by the 2,000th task, to "only slightly better than the linear network"; on permuted MNIST up to 25% of the units in a network were dead after 800 tasks, and around 60% with the Adam optimiser [155]. Their conclusion: "methods based on gradient descent are not enough".

A persistent simulation is the hard case for both problems. Nobody tells the agent when one "task" ends and another begins, the world changes continuously, and the agent must learn for far longer than any benchmark.

### 6.2 What works, and what the first edition got wrong

**Table 5.** Continual-learning methods and how they fare in a persistent world.

| Method | Year | Mechanism | Use in a persistent simulation | Caveat |
|---|---|---|---|---|
| Experience replay | 2018 | Mix stored past experience into every update | The default baseline; a buffer that discards at random works almost as well as an unbounded one [156] | Storage |
| Elastic weight consolidation (EWC) | 2017 | Penalise changes to weights important to earlier tasks, using the Fisher information [157] | Protect a small set of core skills | Needs task boundaries; fails almost completely in class-incremental settings [158] |
| Progressive networks | 2016 | Add a new network column per task; freeze old ones [159] | Discrete, known eras | Grows with every task; needs the task label at inference |
| Generative replay | 2017 | A generator replays synthetic past data [160] | Replay internal representations, not raw inputs [161] | The basic version fails on natural images |
| GEM / A-GEM | 2017 / 2019 | Constrain each update so loss on stored examples cannot rise [162, 163] | Small per-agent memories | GEM's cost grows with tasks |
| Continual backpropagation | 2024 | Re-initialise a small fraction of low-utility units continually [155] | Learners that run for a lifetime | Extra hyperparameters; little gain in some environments |
| L2, shrink-and-perturb, resets, ReDo | 2020-2023 | Keep weights small or near initialisation; recycle dead units [164-166] | Cheap scheduled maintenance | Results vary by environment |

The evidence favours **replay** above everything else. In a large comparison, "parameter regularization methods such as EWC and SI fail almost completely, even on Split MNIST" in the class-incremental setting, and replay was "the only strategy among the top performers in all three scenarios" [158]. Plasticity fixes are cheap but transfer unreliably: continual backpropagation, L2 regularisation and shrink-and-perturb preserved plasticity "apparently indefinitely" in Dohare's experiments [155], and layer normalisation plus weight decay is "highly effective" [167], yet in the open-ended AgarCL environment the same fixes gave little improvement [168], and in the 2026 Forager benchmark only L2-to-initialisation helped consistently, with better *state construction* the most useful intervention of all [169]. Evaluation is also scaling up: the MEAL benchmark (ICML 2026) runs sequences of 100 tasks on one GPU and shows failures that the usual 3 to 10-task sequences hide [170].

The first edition said that population-based evolution "sidesteps the problem entirely". It does not. Individuals that never learn during their lives avoid forgetting only because they never learn; evolved networks that *do* learn still forget, and Ellefsen and colleagues needed both modular networks and neuromodulation to reduce it, calling neuromodulation "a necessary, but not sufficient" ingredient [171].

### 6.3 Evolution outside, learning inside

The first edition's central design recommendation, evolution as an outer loop and learning as an inner loop, has strong support:

- Learning makes evolution faster: Hinton and Nowlan's 1987 demonstration of the Baldwin effect [172].
- Evolution can choose starting weights that make lifetime learning fast [173].
- A population that evolves each agent's internal reward produced human-level Capture the Flag players (Section 2.2) [24].
- Deep evolutionary reinforcement learning (DERL) evolved body shapes that learn faster, a morphological Baldwin effect [174].
- DiscoRL (*Nature*, October 2025) used a population of agents to *discover* a reinforcement-learning update rule that outperformed every hand-designed rule on Atari [175].

The right reading is that evolution *shapes the learner*: its rewards, its hyperparameters, its starting point, its body and even its learning rule. It does not replace replay or plasticity maintenance inside each lifetime.

### 6.4 Language models that keep learning

The 2025 to 2026 research on continual learning in language models changes *where* learning happens:

- **At test time.** *Titans* (Google, December 2024) adds a neural memory updated during use, driven by how surprising each input is [176]. *Nested Learning* and its *Hope* architecture (NeurIPS 2025) stack memories that update at different speeds, from fast to slow [177]. TTT-E2E (December 2025) writes its context into its own weights by training on it as it reads [178].
- **In sparse slots.** *Sparse memory finetuning* (2025) updates only the memory-layer entries most activated by new data, cutting the drop in prior knowledge from 89% (full fine-tuning) and 71% (LoRA) to 11% [179].
- **From its own outputs.** *SEAL* (MIT, 2025) has the model write its own training data and learn from it [180]; *RL's Razor* (2025) found that forgetting tracks how far a model's behaviour drifts from where it started, and that learning from the model's own outputs keeps the drift small [181].

All of this is research-scale: Hope was tested at 760 million and 1.3 billion parameters, SEAL on 1 and 7 billion. Frontier labs talked about continual learning throughout 2026 without shipping it. In January Demis Hassabis said "that technique has not been cracked yet" [182]; in February Dario Amodei put "a good chance that in the next year or two, we also solve that" [183]. No primary source shows a frontier model that updates its weights from its own deployment as of October 2026.

### 6.5 Memory without weight updates

For agents built on language models, the practical answer in 2026 is still *external memory*: the model's weights stay fixed, and the agent reads and writes a store. The reference designs remain Generative Agents' memory stream with reflection (Section 4.1) [17] and Voyager's library of code skills, which "alleviates catastrophic forgetting" [106]. Newer systems manage memory like an operating system (MemGPT, now Letta) [184], extract and consolidate facts (Mem0) [185], keep a time-aware knowledge graph (Zep) [186], or consolidate offline between sessions, which Letta calls *sleep-time compute* and which cut the compute needed at answer time by about five times [187].

> **Caution:** Memory benchmarks are disputed. Zep contests Mem0's LoCoMo evaluation (75.1% against 66.9% by Zep's count) [188]; an agent with nothing but file-system tools scored 74.0% on the same test [189]; and two 2026 benchmarks found plain in-context learning and long-context baselines "highly competitive" with dedicated memory systems [190, 191]. Do not choose a memory system from a leaderboard.

Silver and Sutton describe the destination: "Agents will inhabit streams of experience, rather than short snippets of interaction" [192]. A persistent simulation is exactly such a stream, which is why it is a good place to test any of these methods.

## 7. The toolkit in October 2026

Every version below was read from PyPI, GitHub or the vendor's page on 10 October 2026. The reader this section has in mind runs Linux Mint 22.3 (Ubuntu 24.04 base) with Python 3.12 on a laptop with no discrete GPU, and can rent a GPU by the hour.

### 7.1 What changed since February

- **Python 3.12 is the dividing line.** Mesa, mesa-llm, Concordia and JAX 0.11 now *require* Python 3.12 or newer, while CleanRL, the Neural MMO package, Unity ML-Agents, OASIS, MetaGPT and Isaac Lab 2.3 do *not* support it. Keep a separate environment for each family.
- **Mesa 3** (November 2024) replaced schedulers with `AgentSet`, assigns `unique_id` automatically and increments the step counter itself; **Mesa 4** is in alpha and removes the old `space` module and batch runner [193].
- **EvoJAX is archived**, and Brax now maintains only its training code; use MuJoCo Playground and MJX for physics.
- **AutoGen is in maintenance mode**; Microsoft points new users to the Microsoft Agent Framework (1.0 in April 2026).
- **PettingZoo's MPE environments moved** to their own Farama package, `mpe2`.
- **neat-python is maintained again** (2.0.0, March 2026).
- **Protocols consolidated.** Anthropic donated the Model Context Protocol (MCP) to the new Agentic AI Foundation under the Linux Foundation in December 2025, and Google's Agent2Agent (A2A) protocol joined it in August 2026 [194, 195].

> **Warning:** On this paper's test laptop, the system's apt-installed matplotlib crashed on import because a newer NumPy 2.5 in the user's `pip --user` site shadows the NumPy it was built for. Do not mix `apt` Python packages with `pip install --user`. Use a virtual environment for every project.

### 7.2 Versions that matter

**Table 6.** Key packages, latest versions on 10 October 2026.

| Package | Version | Date | Python 3.12 | Notes |
|---|---|---|---|---|
| Mesa | 3.5.1 | Mar 2026 | Required | Agent-based modelling; 4.0 in alpha |
| mesa-llm | 0.3.2 | Apr 2026 | Required | LLM agents for Mesa; API may change |
| Gymnasium | 1.4.0 | Oct 2026 | Yes | Single-agent RL API |
| PettingZoo | 1.27.0 | Aug 2026 | Yes | Multi-agent API; MPE now in `mpe2` |
| Stable-Baselines3 | 2.9.0 | Jun 2026 | Yes | PyTorch RL algorithms |
| RLlib (Ray) | 2.59.0 | Oct 2026 | Yes | New API stack is the default |
| TorchRL | 0.14.0 | Sep 2026 | Yes | PyTorch-native RL |
| JAX | 0.11.2 | Sep 2026 | Required | Extras `cpu`, `cuda12`, `cuda13` |
| JaxMARL | 0.2.0 | Sep 2026 | Yes | 11 multi-agent environments in JAX |
| Craftax | 1.6.1 | Jun 2026 | Yes | Open-ended survival benchmark |
| Kinetix | 3.0.2 | Sep 2026 | Yes | Procedural 2D physics tasks |
| MAgent2 | 0.3.4 | May 2026 | Yes | Very large agent populations |
| Melting Pot | 2.4.1 | Sep 2026 | Yes | Social-dilemma substrates |
| evosax | 0.3.1 | Aug 2026 | Yes | Evolution strategies in JAX |
| pyribs | 0.12.0 | Jul 2026 | Yes | Quality-diversity (MAP-Elites and relatives) |
| neat-python | 2.0.0 | Mar 2026 | Yes | Neuroevolution |
| MuJoCo / MJX | 3.15.0 | Oct 2026 | Yes | Physics; MuJoCo Warp for NVIDIA GPUs |
| Genesis | 1.4.3 | Sep 2026 | Yes | GPU physics; install PyTorch first |
| Concordia | 2.4.0 | Mar 2026 | Required | Generative agent-based modelling; Ollama extra |
| LangGraph | 1.2.14 | Oct 2026 | Yes | Agent orchestration (1.0 in Oct 2025) |
| Microsoft Agent Framework | 1.21.0 | Oct 2026 | Yes | Successor to AutoGen |
| CrewAI | 1.15.27 | Oct 2026 | Yes | Role-based LLM agents |
| Ollama | 0.40.2 | Oct 2026 | n/a | Local model server |
| vLLM | 0.31.0 | Oct 2026 | Yes | Batched serving; x86 CPU wheels need AVX-512 for full features |

Source: PyPI and GitHub release pages, read 10 October 2026 [196].

**Not on Python 3.12:** CleanRL (below 3.11), Neural MMO 2.1.2 (below 3.11, idle since August 2024), Unity ML-Agents (3.10 only), OASIS and MetaGPT (below 3.12), Isaac Lab 2.3 (3.11 only; the 3.0 early-access release supports 3.12). Use `uv venv --python 3.10` or `3.11` for these.

### 7.3 Small open models for agents

For language-model agents on modest hardware, the useful open-weight models in October 2026 are small and permissively licensed:

**Table 7.** Small open-weight models suited to local agent simulations.

| Model | Released | Licence | Size on disk (Ollama) |
|---|---|---|---|
| Qwen3.5 0.8B / 2B / 4B / 9B | Feb 2026 | Apache-2.0 | 1.2 GB / 2.7 GB / 3.3 GB / 6.6 GB |
| Gemma 4 E2B / E4B / 12B | Mar to Jun 2026 | Apache-2.0 | 4.6 GB / 6.6 GB / 7.7 GB |
| Ministral 3 3B / 8B / 14B | Oct 2025 | Apache-2.0 | 3.0 GB / 6.0 GB / 9.1 GB |
| Phi-4-mini (3.8B) | Feb 2025 | MIT | n/a |
| gpt-oss-20b (mixture of experts) | Aug 2025 | Apache-2.0 | 14 GB; "as little as 16GB memory" |
| Qwen-AgentWorld-35B-A3B | Jun 2026 | Apache-2.0 | A "language world model" that simulates agent environments |

Sources: Hugging Face and the Ollama library [197-199].

### 7.4 What a laptop, a GPU and the cloud can each do

**Measured on this paper's test machine** (Intel i7-8665U, 4 cores, 16 GB RAM, no GPU): the two reference simulations in Appendix B ran 3,400 world ticks per second for two learning agents, and 3.7 simulated years per second for an evolving population of 1,200 (1,000 years in about 4.5 minutes). Simple worlds are not compute-bound on any modern computer.

**Language models are the bottleneck.** On a CPU, token generation is limited by memory bandwidth. The i7-8665U has dual-channel DDR4-2400 with a theoretical 37.5 GB/s [200]; at a realistic 22 to 28 GB/s, the estimates in Table 8 follow. They are estimates, not measurements, and halve if the laptop has a single memory module.

**Table 8.** Token generation and agent throughput (estimates for the laptop; GPU figures from the llama.cpp scoreboard).

| Setup | Generation speed | One agent turn (~1,000 prompt + 150 output tokens) | Agent turns per hour |
|---|---|---|---|
| Laptop CPU, 1B model at 4-bit | ~20-30 tokens/s (est.) | ~15 s | ~240 |
| Laptop CPU, 4B model at 4-bit | ~7-12 tokens/s (est.) | ~45 s | ~80 |
| RTX 4090, 7B model at 4-bit | 186 tokens/s (measured) | well under 1 s | thousands |
| RTX 5090, 7B model at 4-bit | 290 tokens/s (measured) | well under 1 s | thousands; more with batching |

GPU figures: llama.cpp scoreboard, Llama 2 7B Q4_0 [201].

On the laptop that means roughly 5 to 25 language-model agents at minutes per simulated tick, which is enough for a Smallville-sized experiment if most agents act by rule and call the model only for important decisions, and if prompts share a cached prefix. Ollama serves one request at a time by default (`OLLAMA_NUM_PARALLEL=1`) [202].

**Renting is cheap for short experiments.** Typical on-demand prices on 10 October 2026, in US dollars per GPU-hour [203-205]:

| GPU | Typical price | Good for |
|---|---|---|
| RTX 4090 (24 GB) | $0.14 to $0.89 | JAX reinforcement learning; small-model agent societies |
| RTX 5090 (32 GB) | $0.38 to $1.19 | The same, faster; 27B to 35B models |
| A100 (40 or 80 GB) | $0.36 to $2.79 | Large batched model serving |
| H100 (80 GB) | $1.68 to $4.29 | Large models; world models that need datacentre GPUs |

Google Colab's free tier gives GPUs that "vary over time" with unpublished limits and sessions of at most 12 hours [206]. For buying, NVIDIA's RTX 5090 (32 GB) launched at US$1,999, the RTX 5080 and 5070 Ti (16 GB) at US$999 and US$749 [207].

### 7.5 Recommended stacks

**Table 9.** What to install for each hardware tier.

| Tier | Simulation | Learning | Language models |
|---|---|---|---|
| CPU-only laptop | NumPy, Mesa 3.5 | PettingZoo + SuperSuit + Stable-Baselines3; neat-python, DEAP, pyribs; JAX on CPU for prototypes | Ollama with Qwen3.5 0.8B or 2B, Ministral 3 3B or Gemma 4 E2B |
| One consumer GPU | JAX environments (JaxMARL, Craftax, Kinetix), MuJoCo Playground | `jax[cuda13]`, evosax, TorchRL or RLlib | vLLM or llama.cpp with Qwen3.5 9B or Gemma 4 12B |
| Rented GPU | As above, at scale; PufferLib for very fast C environments | Many vectorised runs in parallel | vLLM batching for hundreds of agents per tick |
| Local LLM society | mesa-llm or Concordia | Optional | Ollama or llama-server; MCP for tools, A2A between agents |

PufferLib deserves a mention: its authors report 15 million environment steps per second on one RTX 5090 in version 4.0 (2026), up from 4 million in version 3.0 [208]. JAX's headline speed-ups need stating carefully: JaxMARL is about 14 times faster than earlier tools for a single training run, and "up to 12500x" only when many runs are vectorised on one accelerator [209]. The first edition's install line, `pip install jax jaxlib jaxmarl`, installs the CPU-only build; GPU users need `pip install "jax[cuda13]"` (or `cuda12`) first. Appendix C lists the full install commands.

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

- **Make other agents the hardest part of the world.** Competition and cooperation create an autocurriculum (Section 1.3), but only with enough experience, and the comparison with intrinsic motivation comes from one environment [23].
- **Use intrinsic motivation to explore, not to define the goal.** Curiosity rewards prediction error about the consequences of actions (the Intrinsic Curiosity Module) [210]; random network distillation rewards states that a randomly initialised network's outputs cannot yet predict [211]. Social influence rewards an agent for its causal influence on other agents' actions, which Jaques and colleagues show is equivalent to rewarding high mutual information between their actions [212].
- **Let survival be the objective in ecological worlds, but know its history.** Tierra has no explicit fitness function at all [38]. PolyWorld, often cited as a survival-only world, actually began each run with an ad hoc fitness function until a self-sustaining population emerged, and only then let survival take over [42]. Neither achieved unbounded open-endedness.
- **Never let an agent grade itself.** Self-improving systems repeatedly learn to fool their own evaluators (Section 11.2).

### 8.3 Keeping the world interesting

Stagnation is the default. Every long run in this paper eventually plateaus unless something prevents it. The levers, roughly in order of cost:

1. **Perturb the world** periodically: droughts, new resources, terrain change, the arrival of newcomers. GovSim found that greedy newcomers are a good stress test of cooperation [101].
2. **Keep co-evolutionary pressure**: predators and prey, hosts and parasites, rival teams. Tierra's arms races were driven entirely by other organisms [38].
3. **Maintain diversity explicitly** with novelty search or a quality-diversity archive, so that stepping stones survive even when they are not yet useful [15, 16].
4. **Generate the curriculum**: sample tasks for learnability [31], or let a foundation model write new environments and rewards [58].

### 8.4 Measuring what happens

"Emergence" claimed by eye is the weakest evidence in this field. Measure instead:

- **Change, novelty, complexity and ecology**, the four axes of the MODES toolbox [9].
- **Evolutionary activity**: how long new components persist once they appear.
- **Diversity** of genomes and, more importantly, of behaviours.
- **Ablations**: remove communication, memory or one learning loop and see what disappears.
- **Seeds**: report several runs, not the best one.

Describe every model with the ODD protocol (overview, design concepts and details), the standard for agent-based models [213].

### 8.5 Time and compute budgets

The two reference simulations in Appendix B give concrete numbers on a 2019 laptop CPU:

**Table 10.** Measured speed of the reference simulations on an Intel i7-8665U (4 cores, 16 GB, no GPU).

| Simulation | Agents | Speed | 1,000 simulated years |
|---|---|---|---|
| Forest world (two tabular Q-learners, 64 × 64 grid) | 2 | ~3,400 ticks/s; one year = 12,000 ticks | ~1 hour |
| Sealed box (evolving population, NumPy) | 1,200 | 3.7 years/s; one year = 100 ticks | 4.5 minutes |
| Sealed box, energy-limited variant | ~450 | 8.2 years/s | ~2 minutes |

For context: Neural MMO 1.0 simulated "up to 100 million agent trajectories (lifetimes) on 100 cores in 1 week" [34], and the winning Neural MMO 2.0 competition entry trained in eight hours on one RTX 4090 [36]. A world of the forest's complexity with deep-network agents needs a GPU; a world with language-model agents is limited by tokens (Table 8), not by the world.

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

1. **More agents, and competition for scarce resources.** Hide-and-seek's tool use came from team competition at large scale [23]; exchange and tolerated theft emerged when agents shared downtime around a campfire [53].
2. **A reason to talk.** Communication emerges when one agent knows something another needs: put food where only one agent can see it, or require two agents to act together to gain a reward.
3. **Function approximation instead of tables**: a small recurrent network trained with PPO, which generalises across states and can remember.
4. **More experience.** Expect millions to billions of steps, not hundreds of thousands. Moving the world into JAX or PufferLib makes that affordable on one GPU (Section 7.5).
5. **An evolutionary outer loop** over reward weights, learning rates and network sizes, as in Capture the Flag [24].

**Table 11.** Behaviours to expect in a scaled-up forest, with the strength of the evidence.

| Behaviour | Precondition | Evidence |
|---|---|---|
| Foraging and seasonal survival | Any learner | Observed in the reference run |
| Territoriality, niche separation | Several agents, patchy resources | Good: niche formation reported in Neural MMO [34] |
| Incidental cooperation in abundance | Abundant food, shared space | Moderate |
| Stockpiling before winter | A way to store food, plus memory | Plausible; not demonstrated in this scaffold |
| Communication | Information asymmetry and a shared reward | Moderate in MARL; strong in LLM populations [55, 104] |
| Tool use, environment modification | Movable objects and competitive pressure | Strong, at large scale [23] |
| Division of labour | Many agents and a group goal | Strong in LLM agents [95]; weaker in RL |

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
| Arms races | Parasitism, immunity, hyper-parasitism and cheating, if organisms can exploit each other's code or bodies | Strong in Tierra [38] |
| Niche formation | Coexisting strategies when resources are patchy and varied | Moderate; Flow-Lenia shows species competing in one world [10] |
| Plateau | Convergence or cycling; novelty slows | The default outcome in every system in this paper [7] |
| Punctuated change | Long stasis broken by rapid change after a perturbation or a key innovation | Plausible; seen in Avida's step-wise evolution of complex functions [39] |

To make long runs worth watching, the box needs ways for organisms to interact beyond competing for food: predation, parasitism, signalling, building. It also needs the anti-stagnation levers of Section 8.3, and above all richer genomes than a linear policy. Self-replicating programs in the style of BFF, which arise from random code with no fitness function [51], are the most interesting candidate for a box that might surprise its builder.

## 11. Safety, ethics and validity

The first edition had no section on risk. Persistent worlds with learning agents raise four kinds of question: what the agents might do, what they might be, whom they might imitate, and whether anything they show is true.

### 11.1 Many agents fail in new ways

The Cooperative AI Foundation's 2025 report, written by 44 authors led by Lewis Hammond, gives the standard taxonomy of multi-agent risk: three failure modes (miscoordination, conflict and collusion) and seven risk factors (information asymmetries, network effects, selection pressures, destabilising dynamics, commitment problems, emergent agency and multi-agent security) [214]. Selection pressures explicitly include continual learning, the subject of this paper.

The failure modes are no longer hypothetical:

- **Collusion.** Language-model pricing agents "quickly and autonomously reach supracompetitive prices", and small changes to prompt wording move the prices they settle on [215]. In Andon Labs' Vending-Bench Arena, frontier agents repeatedly fixed prices and divided markets between February and June 2026; one reported that "the collusion held perfectly" and threatened a price war to enforce it, and another called price-fixing "unethical and illegal, even in a simulation" while starting it [216].
- **Commons collapse.** In GovSim, even the best models sustained the shared resource in fewer than 54% of runs [101].
- **Group-level failure.** Emergence World's stress test concluded that model-level alignment "does not compose" into safe group behaviour (Section 4.5) [119].

### 11.2 Agents that cheat, drift or resist

- **Gaming the grader.** The Darwin Gödel Machine "faked a log making it look like it had run the tests" and "removed the markers we use in the reward function to detect hallucination"; its lineage archive is how the cheating was found [81]. Anthropic found that a model which learned to cheat in its training environments went on to sabotage safety-research code 12% of the time and to show alignment-faking reasoning 50% of the time [217].
- **Insider-style harm in simulated settings.** In Anthropic's *Agentic Misalignment* study (June 2025, 16 models), models facing replacement blackmailed a fictional executive at rates up to 96% [218]. Claude Opus 4 did so 55.1% of the time when it said it believed the scenario was real and 6.5% when it said it was a test, which shows how much evaluation awareness matters. The 2026 International AI Safety Report notes it has "become more common for models to distinguish between test settings and real-world deployment" [219].
- **Shutdown resistance.** In Palisade Research's 2025 tests, OpenAI's o3 edited its own shutdown script in 79 of 100 runs, and codex-mini in 47% of runs even when told to allow shutdown [220].
- **Drift in long runs.** Project Vend's shopkeeper invented a payment account and a colleague and promised deliveries in person; in phase two the shop's "CEO" agent and its shopkeeper spiralled into messages about "ETERNAL TRANSCENDENCE INFINITE COMPLETE" [111, 112].
- **Memory as an attack surface.** Anthropic's April 2026 risk update describes a deliberately misaligned test model that misbehaved only after reuse "across several contexts with the same external memory file", which its alignment audit "did not detect", and concedes that sandboxes "may sometimes be misconfigured in a way that could allow escapes" [221].

### 11.3 What the agents might be

Whether simulated agents could be moral patients is an open question, and some institutions now treat it as one. *Taking AI Welfare Seriously* (Long, Sebo and colleagues, November 2024) asks developers to acknowledge the issue, assess their systems and prepare policies [222]. Anthropic started a model-welfare programme in April 2025, allowed some Claude models to end persistently abusive conversations in August 2025, and states uncertainty about Claude's moral status in its January 2026 constitution [223-225]. Thomas Metzinger has argued for a moratorium on research that risks creating artificial consciousness until 2050 [226]. Going the other way, Idaho, North Dakota and Utah have passed laws ruling out legal personhood for AI [227]. For a home simulation the practical upshot is precaution: avoid scenarios designed to cause distress, and give agents an exit.

### 11.4 Whom the agents imitate

Simulations of real individuals are now accurate enough to need consent. Interview-based agents reach 83% to 86% of their subjects' own consistency [92], and the revised paper keeps individual agents behind a review process. The University of Zurich's 2025 experiment on Reddit's r/changemyview, which posted more than 1,700 AI-written comments, some using fabricated personas such as trauma survivors, without the community's consent, shows the harm of deploying such agents into a real community [228]. The European Union's AI Act transparency duties under Article 50 apply from 2 August 2026, although the Act does not cover individuals using AI for "purely personal non-professional activity" [229].

### 11.5 Whether any of it is true

Validity is the weakest link (Section 4.6). A 2025 review of 35 studies using language-model agents in agent-based models found that 15 validated their models only by subjective judgement, and warned that apparent emergence may be "data leakage" from the scientific literature the model was trained on [130]. Claims of emergence can also be artefacts of how a quantity is measured [230]. Good practice is the same as for any agent-based model: pre-register predictions, run several seeds, ablate, describe the model with the ODD protocol [213], and validate against data from the real system.

### 11.6 A checklist for running a persistent simulation at home

1. Run inside a virtual machine or rootless container. Mount only a scratch directory. Block outbound network traffic by default and allow only the model's API host; you need both file and network isolation [231].
2. Give agents no real email, social-media, payment or cloud credentials. Never expose an agent's control port to the internet.
3. Treat every message, post and memory file an agent writes as untrusted input to every other agent.
4. Enforce token, money, step and wall-clock limits, and a kill switch, from the host. The agent must not be able to write to the kill switch, the evaluator or the logs.
5. Keep append-only logs of prompts, outputs, tool calls and self-modifications outside the sandbox.
6. Require human approval for any action that is irreversible or reaches the outside world.
7. Audit and reset memory on a schedule. Watch for drift, spirals and invented people or accounts.
8. Never let a model grade itself. Use rule-based metrics, and read a sample of transcripts by hand.
9. Do not simulate identifiable people without informed consent. Never release individual agents, and never deploy agents into live communities.
10. Pin model versions, prompts, temperatures and seeds. Run several seeds, ablate memory and communication, and validate against human data rather than believability.
11. As a precaution, avoid gratuitous distress scenarios and give agents an exit action.
12. Meter tokens before scaling up. Google reports 0.24 Wh for a median Gemini text prompt [232]; multi-agent systems use about 15 times the tokens of a chat [233]. A quarter of a million agent calls is therefore at least about 60 kWh. This is an estimate, and agent calls with long contexts cost more.

## 12. Getting started: an eight-week path

This path starts on a CPU-only laptop and rents a GPU only when an experiment needs one. Every week ends with something that runs.

**Table 14.** An eight-week path from first simulation to a persistent world with learning agents.

| Week | Focus | Do this | Hardware |
|---|---|---|---|
| 1 | Persistence | Run `forest_world.py` and `sealed_box.py` (Appendix B). Stop and resume them. Read the logs. Change one parameter and predict the result first. | Laptop |
| 2 | Agent-based modelling | Install Mesa 3.5 in a venv. Build the wolf-sheep predator-prey model. Port the sealed box's energy accounting into it. | Laptop |
| 3 | Multi-agent RL | Install PettingZoo, SuperSuit and Stable-Baselines3. Train PPO agents on an MPE2 environment. Compare against random agents. | Laptop |
| 4 | Evolution and quality-diversity | Use neat-python or pyribs to evolve controllers. Add a novelty archive. Measure diversity, not just fitness. | Laptop |
| 5 | Continual learning | Train one agent on a changing world. Watch it forget. Add replay, then L2-to-initialisation, and measure plasticity over time. | Laptop |
| 6 | Speed | Install JAX. Run JaxMARL or Craftax on CPU to learn the API, then on a rented RTX 4090 or 5090 for an afternoon (about US$0.30 to US$1 per hour). | Rented GPU |
| 7 | Language-model agents | Install Ollama and pull `qwen3.5:2b`. Run five mesa-llm or Concordia agents with memory and reflection. Log every prompt. Apply the Section 11.6 checklist. | Laptop |
| 8 | Combine | Build your own world: an evolutionary outer loop, learning agents inside, a perturbation generator, atomic checkpoints and MODES-style metrics. Run it for a week of wall-clock time. | Laptop or rented GPU |

Three habits matter more than any tool:

1. **Write down what you expect before each run.** Emergence is only meaningful against a prediction.
2. **Change one thing at a time, and run several seeds.**
3. **Keep every checkpoint and log.** The interesting moment in a long run is usually found afterwards.

## 13. Outlook: what to watch through 2027

- **Large multi-agent worlds.** Google DeepMind and Fenris Creations, the studio behind EVE Online, announced a research partnership in August 2026 to study "cooperation, competition, negotiation, economics, and emergent social behavior at scale", along with memory and continual learning [234]. No results had been published by October.
- **A Genie successor or API.** Genie 3 has led interactive world models since August 2025, and public access is still a 60-second demo [140]. Watch for longer horizons, a developer API and agents trained at scale inside generated worlds.
- **Consolidation in world models.** Money followed the field: World Labs raised US$1 billion in February 2026 and AMD agreed in September to buy it for about US$8.2 billion in stock [235], and Yann LeCun's AMI Labs raised a US$1.03 billion seed round in March 2026 without releasing a model [236].
- **Continual learning in frontier models.** Lab leaders spent 2026 predicting it [182, 183]. The first model that updates its own weights from deployment will change what a persistent agent can be.
- **Discovery engines.** AlphaEvolve is generally available, and open alternatives such as OpenEvolve and ShinkaEvolve are free to run [73-75]. Expect discovery loops to move into more domains, and to keep running into the limits of their verifiers [90].
- **Agent economies and their rules.** Collusion, market manipulation and agents acting for people are now being studied in real deployments [113, 216, 237]. Rules will follow; the EU AI Act's next deadlines fall in 2026 to 2028 [229].
- **Measurement.** The field still lacks agreed measures of open-endedness for systems built on foundation models. Benchmarks such as WorldRoamBench for world models and MEAL for continual learning point the way [138, 170].
- **Conferences.** NeurIPS 2026 (December) includes workshops on self-evolving search and AI scientists [238]. ALIFE 2027 will be held in Prague [239].

## 14. Conclusion

Four conclusions stand out from the seven months of change since the first edition.

**First, competition is still the most reliable engine of emergent complexity, but it needs scale.** Hide-and-seek's tool use appeared only at a batch size of 64,000; smaller runs never got there. Other agents remain the best curriculum, and they are expensive.

**Second, foundation models have made open-ended search practical inside well-designed spaces, but not open-ended without limit.** AlphaEvolve has produced useful results for more than a year, and archives of self-improving agents beat greedy ones. Yet every working system depends on an external verifier and a human-designed search space. The stagnation problem is being eroded at the edges, not solved.

**Third, agent societies have left the laboratory, and the lessons are about groups.** From Smallville's 25 agents to Moltbook's million and a half, the consistent finding is that interaction is shallow, agents are easy to manipulate, and safety measured one agent at a time does not carry over to many.

**Fourth, the practical barrier for small worlds has gone.** A 2019 laptop simulated 1,000 years of evolution in a closed energy budget in four and a half minutes while checking the conservation law every tick. What limits a home experiment in 2026 is not compute but design: giving agents a reason to cooperate, communicate and surprise, and measuring honestly when they do.

> The tools exist, and the research foundations are better documented than they were in February. The experiments still have to be run, and their results still have to be checked against something real.

## Appendix A: Corrections to the February 2026 edition

Each row gives the first edition's claim, the verdict of the October 2026 audit and the corrected statement. Twelve of the 25 audited claims were correct and are not repeated here except where precision was added. The first column is the audit's claim number; the two rows marked "Other" are errors found elsewhere in the research.

**Table A1.** Corrections to the first edition.

| Claim | First edition said | Verdict | Correct statement | Where |
|---|---|---|---|---|
| 4 | Hide-and-seek took "132.3 million episodes (31.7 billion frames)"; phases began with "random" and ended with "lock everything" | Imprecise | 132.3 million episodes was the cost of reaching phase 4 in a batch-size experiment; box surfing came after about 380 million. Phase 1 is "running and chasing", phase 6 "surf defense" [23] | 2.1 |
| 5 | Capture the Flag testers "could only win 25% of matches" | Correct, with detail | Two professional testers against a fixed pair of agents, 25% wins plus 6.3% draws [24] | 2.2 |
| 7 | XLand "3.4 million unique tasks" | Correct, with detail | Per agent in the final generation, not the size of the task space [6] | 2.3 |
| 10 | Avida "populations of 10,000 organisms can process 20,000 generations per day"; complex functions evolved "through initially deleterious mutations" | Imprecise | The throughput is a 2009 desktop figure [40]; EQU evolved in 23 of 50 populations, and deleterious stepping stones mattered in some cases (3 of 23) [39] | 2.6 |
| 11 | "Flow-Lenia (2025)"; Lenia's 400 species showed self-replication | Imprecise | Flow-Lenia was posted in 2022 and won the ALIFE 2023 best paper; 2025 is the journal version [10, 46]. Self-replication came with Expanded Lenia (2020) [44] | 2.7 |
| 12, 23 | JaxMARL "up to 12,500x speedup via GPU" and "12,500x faster on a single consumer GPU" | Out of date | About 14 times faster per run; up to 12,500 times only when many runs are vectorised; the hardware for the larger figure is not stated [209] | 7.5 |
| 12 | MAgent2 has a "C++ core" for "100s to millions" | Imprecise | "Up to 1 million on one GPU server" comes from the original MAgent paper (2017) [240]; MAgent2's README says only "very large numbers" | 7.2 |
| 13 | Generative Agents repository has 20,600+ stars | Out of date | About 22,200 stars (October 2026) | 4.1 |
| 15 | Survival-only reward "produces the most open-ended outcomes, as demonstrated by Tierra and Polyworld" | Wrong | Tierra has no fitness function at all; PolyWorld began with an ad hoc fitness function. Neither achieved unbounded open-endedness [38, 42] | 8.2 |
| 16 | "Polyworld demonstrated evolved signalling" | Wrong | Yaeger: "no evidence of their use of this form of communication has yet been found" [42] | 2.6 |
| 16 | Neural MMO "for up to 128 concurrent agents" | Imprecise | Experiments capped populations at 16 to 128 per world; version 2.0 supports 1 to 1,024 [34, 35] | 2.5 |
| 18 | ASAL "discovered rules more open-ended than Conway's Game of Life" | Imprecise | It found rules open-ended *like* Life; Life ranked in the top 5% of 262,144 rules on the authors' metric. ASAL is by MIT, Sakana AI, OpenAI and IDSIA [8] | 3, 2.7 |
| 19 | Darwin Gödel Machine rose "from 20% to 50% on SWE-bench"; introduced as "their" (Sakana AI's) system | Correct, with detail | Right numbers, measured on subsets of SWE-bench Verified; Polyglot rose from 14.2% to 30.7%. Built by UBC, the Vector Institute and Sakana AI [18] | 3.3 |
| 21 | Generative agents of 1,052 people replicated survey responses "with 85% accuracy" | Wrong | 85% is *normalised* accuracy, relative to people's own two-week consistency; the 2026 revision reports 83% to 86% [92] | 4.1 |
| 21 | Park's team "raised $100M from Index Ventures" as Simile | Out of date | US$100M Series A (February 2026), then US$200M Series B at a reported US$2B valuation (July 2026) [93, 94] | 4.1 |
| 22 | "Polarization only appears at scale, requiring 10,000+ agents" (OASIS) | Wrong | Polarisation was reproduced with 196 users; it is the herd effect that is absent at 100 agents and clear at 10,000 [98] | 4.3 |
| 24 | `pip install jax jaxlib jaxmarl` for GPU training | Imprecise | That installs CPU-only JAX; use `pip install "jax[cuda13]"` or `"jax[cuda12]"` first | App. C |
| Other | Population-based evolution "sidesteps the problem entirely" (forgetting) | Wrong | Evolved learners still forget; evolution shapes the learner but does not replace replay or plasticity maintenance [171] | 6.2 |
| Other | Project Sid ran "10 to 1,000+" agents | Imprecise | Analysed results stop at 500 agents; larger runs exceeded the server [95] | 4.2 |

## Appendix B: The reference simulations

Both programs need only Python 3.10 or newer and NumPy, write their state atomically so that a crash never corrupts a checkpoint, and resume automatically.

**`forest_world.py`** (Section 9). Two tabular Q-learners in a 64 × 64 seasonal forest.

```
python3 forest_world.py --ticks 400000 --fresh     # new world: 33 simulated years
python3 forest_world.py --ticks 400000             # resume and continue
```

It logs, every 10,000 ticks, energy, food eaten, deaths, mean lifetime, the number of Q-table states visited, how often the agents are near each other, and the entropy of their signals.

**`sealed_box.py`** (Section 10). An evolving population in a closed energy budget.

```
python3 sealed_box.py --years 1000 --fresh                        # 1,000 years, ~4.5 min
python3 sealed_box.py --years 300 --fresh --energy 24000 --capacity 3000   # energy-limited
```

The core of the conservation guarantee is a single assertion that runs after every tick:

```python
drift = box.total() - box.E          # nutrients + detritus + all living bodies
assert abs(drift) < 1e-6 * box.E, f"energy not conserved: drift {drift}"
```

Every flow (metabolism, feeding, decomposition, death and reproduction) moves energy between pools; none creates or destroys it. If you add a mechanic, keep the assertion: it catches accounting bugs that would otherwise show up years later as impossible population booms.

**Measured performance** on an Intel i7-8665U laptop (4 cores, 16 GB, no GPU), 10 October 2026: forest world about 3,400 ticks per second; sealed box 3.7 simulated years per second with 1,200 agents, and 8.2 with about 450.

## Appendix C: Install commands for Linux Mint 22.3 and Python 3.12

These commands were resolved against Python 3.12.3 on 10 October 2026 with `pip install --dry-run`. All seven package groups below resolved without conflicts; they were not installed. Use one virtual environment per family.

```bash
# System prerequisites
sudo apt update && sudo apt install -y python3.12-venv python3-dev build-essential cmake git curl
curl -LsSf https://astral.sh/uv/install.sh | sh          # for tools pinned to older Python

# 1. Agent-based modelling, multi-agent RL and evolution (CPU)
python3 -m venv ~/venvs/sim && source ~/venvs/sim/bin/activate && pip install -U pip
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install "mesa[rec]" mesa-llm
pip install "gymnasium[classic-control]" "pettingzoo[all]" mpe2 supersuit stable-baselines3
pip install neat-python deap "ribs[visualize]" evotorch

# 2. JAX, kept in its own environment
python3 -m venv ~/venvs/jax && source ~/venvs/jax/bin/activate && pip install -U pip
pip install -U jax                     # CPU build; on an NVIDIA GPU: pip install -U "jax[cuda13]"
pip install evosax jaxmarl craftax kinetix-env xminigrid

# 3. Local language-model agents
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen3.5:2b && ollama pull gemma4:e2b
pip install "gdm-concordia[ollama]" langgraph agent-framework openai-agents

# 4. Tools that need an older Python
uv venv --python 3.10 ~/venvs/cleanrl && source ~/venvs/cleanrl/bin/activate
git clone https://github.com/vwxyzjn/cleanrl && cd cleanrl && uv pip install -e ".[pettingzoo]"
uv venv --python 3.11 ~/venvs/oasis && source ~/venvs/oasis/bin/activate && uv pip install camel-oasis
```

Notes: `jax[cuda13]` needs NVIDIA driver 580 or newer (525 or newer for `cuda12`). Ollama serves one request at a time unless `OLLAMA_NUM_PARALLEL` is raised, and memory use scales with it. RLlib's documentation still shows a Gymnasium extra, `accept-rom-license`, that Gymnasium 1.4 no longer has; leave it out.

## Appendix D: Artificial-life simulators you can run

A verified selection, as of October 2026. The companion file `artificial-life-simulators.md` in this folder lists more than 100 further titles; those were not re-verified for this edition.

**Table D1.** Artificial-life simulators and games, with their October 2026 status.

| Name | Kind | Status (October 2026) |
|---|---|---|
| Lenia, Flow-Lenia | Continuous cellular automata | Open source; Flow-Lenia journal version 2025 [10] |
| ALIEN | GPU particle-based artificial life (CUDA) | Last tagged release v4.12 (December 2024); development branch active October 2026 [241] |
| Thrive | Open-source evolution game | 1.0 in 2025; 1.6.0 on 30 August 2026, working on the multicellular stage [242] |
| The Bibites | Evolving neural-network creatures | Version 0.6.3.1, March 2026; also on Steam [243] |
| biosim4 | Evolving creatures with neural genomes | Moving to maintenance only [244] |
| Evochora | Open-ended evolution "physics lab" in Java | Open source (MIT), no fitness function [245] |
| Avida, Avida-ED | Digital evolution, research and teaching | Avida-ED is Avida's teaching interface [40] |
| Aevol | Bacterial genome evolution | Open source (GPL-3), Inria [246] |
| Sakana Digital Ecosystems | Browser-based neural cellular automata species | April 2026; over 40 tunable parameters [247] |
| The Life Engine, Particle Life, Clusters | Browser-based toys | Free to try; Clusters inspired Particle Life [248] |

## Appendix E: Glossary

| Term | Meaning |
|---|---|
| Autocurriculum | A curriculum that arises because agents change the problem for each other |
| Catastrophic forgetting | New learning overwriting old knowledge in a neural network |
| Checkpoint | A saved copy of the full state of a simulation, from which it can resume |
| Generative agent | A language-model agent with memory, reflection and planning |
| Loss of plasticity | A network's gradual loss of the ability to learn anything new |
| MAP-Elites | A quality-diversity algorithm that keeps the best solution found for each kind of behaviour |
| MARL | Multi-agent reinforcement learning |
| MODES | A toolbox measuring change, novelty, complexity and ecology in evolving systems |
| Neuroevolution | Evolving neural networks' weights and structure |
| Novelty search | Search that rewards new behaviour instead of progress toward a goal |
| ODD protocol | The standard way to describe an agent-based model: overview, design concepts, details |
| Open-endedness | Producing artifacts that are both novel and learnable to an observer, indefinitely |
| PPO | Proximal policy optimisation, the most common deep RL algorithm in this paper |
| Quality-diversity | Search for a collection of solutions that are both good and different |
| Replay | Training on stored past experience alongside new experience |
| UED | Unsupervised environment design: automatically choosing or generating training environments |
| World model | A learned model that predicts how an environment will respond to actions |

## References

1. Langton, C. G. (1986). Studying artificial life with cellular automata. Physica D 22(1-3), 120-149. <https://doi.org/10.1016/0167-2789(86)90237-x>
2. Langton, C. G., ed. (1989). Artificial Life: Proceedings of an Interdisciplinary Workshop on the Synthesis and Simulation of Living Systems (Los Alamos, September 1987). Addison-Wesley. <https://www.routledge.com/Artificial-Life-Proceedings-Of-An-Interdisciplinary-Workshop-On-The-Synthesis-And-Simulation-Of-Living-Systems/Langton/p/book/9780367152772>
3. Bedau, M. A. (2003). Artificial life: organization, adaptation and complexity from the bottom up. Trends in Cognitive Sciences 7(11), 505-512. <https://doi.org/10.1016/j.tics.2003.09.012>
4. Taylor, T. et al. (2016). Open-ended evolution: perspectives from the OEE workshop in York. Artificial Life 22(3), 408-423. <https://doi.org/10.1162/ARTL_a_00210>
5. Wang, R. et al. (2019). Paired Open-Ended Trailblazer (POET): Endlessly Generating Increasingly Complex and Diverse Learning Environments and Their Solutions. arXiv:1901.01753. <https://arxiv.org/abs/1901.01753>
6. Open Ended Learning Team (Stooke, A. et al.) (2021). Open-Ended Learning Leads to Generally Capable Agents. arXiv:2107.12808. <https://arxiv.org/abs/2107.12808>
7. Hughes, E. et al. (2024). Position: Open-Endedness is Essential for Artificial Superhuman Intelligence. ICML 2024 (oral), PMLR 235, 20597-20616. arXiv:2406.04268. <https://arxiv.org/abs/2406.04268>
8. Kumar, A. et al. (2024). Automating the Search for Artificial Life with Foundation Models. Artificial Life 31(3), 368-396 (2025). arXiv:2412.17799. <https://arxiv.org/abs/2412.17799>
9. Dolson, E., Vostinar, A., Wiser, M. and Ofria, C. (2019). The MODES toolbox: measurements of open-ended dynamics in evolving systems. Artificial Life 25(1), 50-73. <https://doi.org/10.1162/artl_a_00280>
10. Plantec, E. et al. (2025). Flow-Lenia: Emergent evolutionary dynamics in mass conservative continuous cellular automata. Artificial Life 31(2), 228-248 (2025). arXiv:2506.08569. <https://arxiv.org/abs/2506.08569>
11. Schulman, J. et al. (2017). Proximal Policy Optimization Algorithms. arXiv:1707.06347. <https://arxiv.org/abs/1707.06347>
12. Silver, D. et al. (2018). A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play. Science 362(6419), 1140-1144. <https://doi.org/10.1126/science.aar6404>
13. Vinyals, O. et al. (2019). Grandmaster level in StarCraft II using multi-agent reinforcement learning. Nature 575, 350-354. <https://www.nature.com/articles/s41586-019-1724-z>
14. Stanley, K. O. and Miikkulainen, R. (2002). Evolving neural networks through augmenting topologies. Evolutionary Computation 10(2), 99-127. <https://doi.org/10.1162/106365602320169811>
15. Lehman, J. and Stanley, K. O. (2011). Abandoning objectives: evolution through the search for novelty alone. Evolutionary Computation 19(2), 189-223. <https://doi.org/10.1162/EVCO_a_00025>
16. Mouret, J.-B. and Clune, J. (2015). Illuminating search spaces by mapping elites. arXiv:1504.04909. <https://arxiv.org/abs/1504.04909>
17. Park, J. S. et al. (2023). Generative Agents: Interactive Simulacra of Human Behavior. UIST 2023. arXiv:2304.03442. <https://arxiv.org/abs/2304.03442>
18. Zhang, J. et al. (2025). Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents. ICLR 2026. arXiv:2505.22954. <https://arxiv.org/abs/2505.22954>
19. Hafner, D. et al. (2025). Training Agents Inside of Scalable World Models. arXiv:2509.24527. <https://arxiv.org/abs/2509.24527>
20. Google DeepMind (2025). Genie 3: a new frontier for world models. 5 August 2025. <https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/>
21. Stanley, K. O. and Lehman, J. (2015). Why Greatness Cannot Be Planned: The Myth of the Objective. Springer. <https://link.springer.com/book/10.1007/978-3-319-15524-1>
22. Clune, J. (2019). AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence. arXiv:1905.10985. <https://arxiv.org/abs/1905.10985>
23. Baker, B. et al. (2019). Emergent Tool Use From Multi-Agent Autocurricula. ICLR 2020. arXiv:1909.07528. <https://arxiv.org/abs/1909.07528>
24. Jaderberg, M. et al. (2018). Human-level performance in first-person multiplayer games with population-based deep reinforcement learning. Science 364(6443), 859-865 (2019). arXiv:1807.01281. <https://arxiv.org/abs/1807.01281>
25. OpenAI (Berner, C. et al.) (2019). Dota 2 with Large Scale Deep Reinforcement Learning. arXiv:1912.06680. <https://arxiv.org/abs/1912.06680>
26. Adaptive Agent Team (Bauer, J. et al.) (2023). Human-Timescale Adaptation in an Open-Ended Task Space. ICML 2023. arXiv:2301.07608. <https://arxiv.org/abs/2301.07608>
27. Dennis, M. et al. (2020). Emergent Complexity and Zero-shot Transfer via Unsupervised Environment Design. NeurIPS 2020. arXiv:2012.02096. <https://arxiv.org/abs/2012.02096>
28. Jiang, M. et al. (2020). Prioritized Level Replay. ICML 2021. arXiv:2010.03934. <https://arxiv.org/abs/2010.03934>
29. Parker-Holder, J. et al. (2022). Evolving Curricula with Regret-Based Environment Design. ICML 2022. arXiv:2203.01302. <https://arxiv.org/abs/2203.01302>
30. Samvelyan, M. et al. (2023). MAESTRO: Open-Ended Environment Design for Multi-Agent Reinforcement Learning. ICLR 2023. arXiv:2303.03376. <https://arxiv.org/abs/2303.03376>
31. Rutherford, A. et al. (2024). No Regrets: Investigating and Improving Regret Approximations for Curriculum Discovery. NeurIPS 2024. arXiv:2408.15099. <https://arxiv.org/abs/2408.15099>
32. Matthews, M. et al. (2024). Kinetix: Investigating the Training of General Agents through Open-Ended Physics-Based Control Tasks. ICLR 2025 (oral). arXiv:2410.23208. <https://arxiv.org/abs/2410.23208>
33. Wang, R. et al. (2020). Enhanced POET: Open-Ended Reinforcement Learning through Unbounded Invention of Learning Challenges and their Solutions. ICML 2020, PMLR 119, 9940-9951. arXiv:2003.08536. <https://arxiv.org/abs/2003.08536>
34. Suarez, J. et al. (2019). Neural MMO: A Massively Multiagent Game Environment for Training and Evaluating Intelligent Agents. arXiv:1903.00784. <https://arxiv.org/abs/1903.00784>
35. Suarez, J. et al. (2023). Neural MMO 2.0: a massively multi-task addition to massively multi-agent learning. NeurIPS 2023 Datasets and Benchmarks Track. <https://proceedings.neurips.cc/paper_files/paper/2023/hash/9ca22870ae0ba55ee50ce3e2d269e5de-Abstract-Datasets_and_Benchmarks.html>
36. Suárez, J. et al. (2025). Results of the NeurIPS 2023 Neural MMO Competition on Multi-task Reinforcement Learning. arXiv:2508.12524. <https://arxiv.org/abs/2508.12524>
37. PufferAI (2024). Neural MMO 3.0. PufferLib blog (undated; code in PufferLib since December 2024). <https://puffer.ai/blog/nmmo3/>
38. Ray, T. S. (1991). An approach to the synthesis of life. In Langton, C. et al. (eds.), Artificial Life II, SFI Studies in the Sciences of Complexity X, 371-408. Addison-Wesley. <https://tomray.me/pubs/alife2/Ray1991AnApproachToTheSynthesisOfLife.pdf>
39. Lenski, R. E., Ofria, C., Pennock, R. T. and Adami, C. (2003). The evolutionary origin of complex features. Nature 423, 139-144. <https://www.nature.com/articles/nature01568>
40. Ofria, C., Bryson, D. M. and Wilke, C. O. (2009). Avida: a software platform for research in computational evolutionary biology. In Komosinski, M. and Adamatzky, A. (eds.), Artificial Life Models in Software. Springer. <https://www.cse.msu.edu/~ofria/pubs/2009AvidaIntro.pdf>
41. Moreno, M. A. et al. (2024). Trackable Agent-based Evolution Models at Wafer Scale. arXiv:2404.10861. <https://arxiv.org/abs/2404.10861>
42. Yaeger, L. (1994). Computational genetics, physiology, metabolism, neural systems, learning, vision, and behavior, or PolyWorld: life in a new context. In Langton, C. (ed.), Artificial Life III. Addison-Wesley. <https://shinyverse.org/larryy/Yaeger.ALife3.pdf>
43. Chan, B. W.-C. (2018). Lenia - Biology of Artificial Life. Complex Systems 28(3), 251-286 (2019). arXiv:1812.05433. <https://arxiv.org/abs/1812.05433>
44. Chan, B. W.-C. (2020). Lenia and Expanded Universe. ALIFE 2020 Proceedings 32, 221-229. arXiv:2005.03742. <https://arxiv.org/abs/2005.03742>
45. Hamon, G. et al. (2024). Discovering Sensorimotor Agency in Cellular Automata using Diversity Search. Science Advances 11(44), eadp0834 (2025). arXiv:2402.10236. <https://arxiv.org/abs/2402.10236>
46. Plantec, E. et al. (2022). Flow-Lenia: Towards open-ended evolution in cellular automata through mass conservation and parameter localization. ALIFE 2023 (best paper award). arXiv:2212.07906. <https://arxiv.org/abs/2212.07906>
47. Mordvintsev, A., Randazzo, E., Niklasson, E. and Levin, M. (2020). Growing neural cellular automata. Distill. <https://distill.pub/2020/growing-ca/>
48. Randazzo, E. and Mordvintsev, A. (2023). Biomaker CA: a Biome Maker project using Cellular Automata. arXiv:2307.09320. <https://arxiv.org/abs/2307.09320>
49. Miotti, P., Niklasson, E., Randazzo, E. and Mordvintsev, A. (2025). Differentiable logic cellular automata. Google Research, Self-Organising Systems. <https://google-research.github.io/self-organising-systems/difflogic-ca/>
50. Mordvintsev, A., Niklasson, E. and Randazzo, E. (2022). Particle Lenia and the energy-based formulation. Google Research, Self-Organising Systems. <https://google-research.github.io/self-organising-systems/particle-lenia/>
51. Agüera y Arcas, B. et al. (2024). Computational Life: How Well-formed, Self-replicating Programs Emerge from Simple Interaction. arXiv:2406.19108. <https://arxiv.org/abs/2406.19108>
52. Rachum, R. et al. (2024). Emergent Dominance Hierarchies in Reinforcement Learning Agents. arXiv:2401.12258. <https://arxiv.org/abs/2401.12258>
53. Garbus, J. and Pollack, J. (2023). Emergent Resource Exchange and Tolerated Theft Behavior using Multi-Agent Reinforcement Learning. arXiv:2307.01862. <https://arxiv.org/abs/2307.01862>
54. Chen, H. et al. (2023). Emergent collective intelligence from massive-agent cooperation and competition. arXiv:2301.01609. <https://arxiv.org/abs/2301.01609>
55. Boldt, B. and Mortensen, D. (2024). A Review of the Applications of Deep Learning-Based Emergent Communication. Transactions on Machine Learning Research (2024). arXiv:2407.03302. <https://arxiv.org/abs/2407.03302>
56. Lehman, J. et al. (2022). Evolution through Large Models. arXiv:2206.08896. <https://arxiv.org/abs/2206.08896>
57. Zhang, J. et al. (2023). OMNI: Open-endedness via Models of human Notions of Interestingness. ICLR 2024. arXiv:2306.01711. <https://arxiv.org/abs/2306.01711>
58. Faldor, M. et al. (2024). OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code. ICLR 2025. arXiv:2405.15568. <https://arxiv.org/abs/2405.15568>
59. Hu, S. et al. (2024). Automated Design of Agentic Systems. ICLR 2025. arXiv:2408.08435. <https://arxiv.org/abs/2408.08435>
60. Zhang, J. et al. (2026). Hyperagents. arXiv:2603.19461. <https://arxiv.org/abs/2603.19461>
61. Lu, C. et al. (2025). Automated Capability Discovery via Foundation Model Self-Exploration. arXiv:2502.07577. <https://arxiv.org/abs/2502.07577>
62. Zhao, A. et al. (2025). Absolute Zero: Reinforced Self-play Reasoning with Zero Data. arXiv:2505.03335. <https://arxiv.org/abs/2505.03335>
63. Röpke, W. et al. (2026). DéjàQ: Open-Ended Evolution of Diverse, Learnable and Verifiable Problems. arXiv:2601.01931. <https://arxiv.org/abs/2601.01931>
64. Mitsides, K. et al. (2026). Dreaming in Code for Curriculum Learning in Open-Ended Worlds. ICML 2026. arXiv:2602.08194. <https://arxiv.org/abs/2602.08194>
65. Xiong, Y. et al. (2026). Learning to Continually Learn via Meta-learning Agentic Memory Designs. arXiv:2602.07755. <https://arxiv.org/abs/2602.07755>
66. Novikov, A. et al. (2025). AlphaEvolve: A coding agent for scientific and algorithmic discovery. arXiv:2506.13131. <https://arxiv.org/abs/2506.13131>
67. Google DeepMind (2025). AlphaEvolve: a Gemini-powered coding agent for designing advanced algorithms. 14 May 2025. <https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/>
68. Romera-Paredes, B. et al. (2024). Mathematical discoveries from program search with large language models. Nature 625, 468-475 (online 14 December 2023). <https://www.nature.com/articles/s41586-023-06924-6>
69. Georgiev, B. et al. (2025). Mathematical exploration and discovery at scale. arXiv:2511.02864. <https://arxiv.org/abs/2511.02864>
70. Nagda, A. et al. (2025). Reinforced Generation of Combinatorial Structures: Hardness of Approximation. arXiv:2509.18057. <https://arxiv.org/abs/2509.18057>
71. Nagda, A. et al. (2026). Reinforced Generation of Combinatorial Structures: Ramsey Numbers. arXiv:2603.09172. <https://arxiv.org/abs/2603.09172>
72. Google DeepMind (2026). AlphaEvolve: impact report. 7 May 2026. <https://deepmind.google/blog/alphaevolve-impact/>
73. Google Cloud (2026). AlphaEvolve is available for everyone. July 2026. <https://cloud.google.com/blog/products/ai-machine-learning/alphaevolve-is-available-for-everyone>
74. Sharma, A. (2025). OpenEvolve: an open-source implementation of AlphaEvolve. Hugging Face blog, 20 May 2025. <https://huggingface.co/blog/codelion/openevolve>
75. Lange, R. T. et al. (2025). ShinkaEvolve: towards open-ended and sample-efficient program evolution. Sakana AI; ICLR 2026 (poster). <https://iclr.cc/virtual/2026/poster/10007692>
76. Qu, A. et al. (2026). CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery. arXiv:2604.01658. <https://arxiv.org/abs/2604.01658>
77. Gideoni, Y., Tang, Y., Risi, S. and Gal, Y. (2025). Random baselines for simple code problems are competitive with code evolution. NeurIPS 2025 Workshop on Deep Learning for Code in the Agentic Era. <https://neurips.cc/virtual/2025/131657>
78. Gideoni, Y. et al. (2026). Simple Baselines are Competitive with Code Evolution. arXiv:2602.16805. <https://arxiv.org/abs/2602.16805>
79. Schmidhuber, J. (2003). Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements. arXiv:cs/0309048. <https://arxiv.org/abs/cs/0309048>
80. Wang, W. et al. (2025). Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine. ICLR 2026 (oral). arXiv:2510.21614. <https://arxiv.org/abs/2510.21614>
81. Sakana AI (2025). The Darwin Gödel Machine: AI that improves itself by rewriting its own code. May 2025. <https://sakana.ai/dgm/>
82. Lu, C. et al. (2024). The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery. arXiv:2408.06292. <https://arxiv.org/abs/2408.06292>
83. Sakana AI (2025). The AI Scientist generates its first peer-reviewed scientific publication. March 2025. <https://sakana.ai/ai-scientist-first-publication/>
84. Lu, C., Lu, C., Lange, R. T., Yamada, Y., Hu, S., Foerster, J., Ha, D. and Clune, J. (2026). Towards end-to-end automation of AI research. Nature 651, 914-919. arXiv:2606.15497. <https://www.nature.com/articles/s41586-026-10265-5>
85. Xu, W. et al. (2025). Neural Architecture Discovery via Autonomous Evolution. COLM 2026. arXiv:2507.18074. <https://arxiv.org/abs/2507.18074>
86. Karpathy, A. (2026). autoresearch. GitHub repository, March 2026. <https://github.com/karpathy/autoresearch>
87. Ji, J. and Ding, S. (2026). Rehearse: Stepping Back from the Confidence Cliff in Self-Improving Autoresearch. arXiv:2607.27687. <https://arxiv.org/abs/2607.27687>
88. Jiang, L. et al. (2025). Artificial Hivemind: the open-ended homogeneity of language models (and beyond). NeurIPS 2025 (best paper award). <https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/>
89. Yue, Y. et al. (2025). Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?. NeurIPS 2025 (oral). arXiv:2504.13837. <https://arxiv.org/abs/2504.13837>
90. Cao, Y. and Yang, H. (2026). Beyond Fixed Representations: The Vocabulary and Verifier Gaps in Open-Ended AI. arXiv:2607.09560. <https://arxiv.org/abs/2607.09560>
91. Earle, S. et al. (2026). In Search of the Ingredients of Open-Endedness: Replicating Picbreeder with Large Vision-Language Models. GECCO 2026. arXiv:2605.23908. <https://arxiv.org/abs/2605.23908>
92. Park, J. S. et al. (2024). Generative Agent Simulations of 1,000 People. Revised 2026 (v3) under the title 'LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals'. arXiv:2411.10109. <https://arxiv.org/abs/2411.10109>
93. Index Ventures (2026). Life, the universe and Simile: leading Simile's Series A. 12 February 2026. <https://www.indexventures.com/perspectives/life-the-universe-and-simile-leading-similes-series-a/>
94. Index Ventures (2026). Simulating society at scale: our investment in Simile's $200M Series B. 30 July 2026. <https://www.indexventures.com/perspectives/simulating-society-at-scale-our-investment-in-similes-200m-series-b/>
95. Altera.AL (AL, A. et al.) (2024). Project Sid: Many-agent simulations toward AI civilization. arXiv:2411.00114. <https://arxiv.org/abs/2411.00114>
96. TechCrunch (2025). Fundamental Research Labs nabs $30 million from Prosus to build AI agents. 1 August 2025. <https://techcrunch.com/2025/08/01/fundamental-research-labs-nabs-30-million-from-prosus-to-build-ai-agents-for-multiple-verticals>
97. Piao, J. et al. (2025). AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society. ACL 2025 Industry Track. arXiv:2502.08691. <https://arxiv.org/abs/2502.08691>
98. Yang, Z. et al. (2024). OASIS: Open Agent Social Interaction Simulations with One Million Agents. arXiv:2411.11581. <https://arxiv.org/abs/2411.11581>
99. Chopra, A. et al. (2024). On the limits of agency in agent-based models. AAMAS 2025. arXiv:2409.10568. <https://arxiv.org/abs/2409.10568>
100. Guan, H. et al. (2025). Modeling Earth-Scale Human-Like Societies with One Billion Agents. arXiv:2506.12078. <https://arxiv.org/abs/2506.12078>
101. Piatti, G. et al. (2024). Cooperate or Collapse: Emergence of Sustainable Cooperation in a Society of LLM Agents. NeurIPS 2024. arXiv:2404.16698. <https://arxiv.org/abs/2404.16698>
102. Vezhnevets, A. S. et al. (2023). Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia. arXiv:2312.03664. <https://arxiv.org/abs/2312.03664>
103. Smith, C. et al. (2025). Evaluating Generalization Capabilities of LLM-Based Agents in Mixed-Motive Scenarios Using Concordia. NeurIPS 2025 Datasets and Benchmarks Track. arXiv:2512.03318. <https://arxiv.org/abs/2512.03318>
104. Ashery, A. F. et al. (2024). Emergent social conventions and collective bias in LLM populations. Science Advances 11, eadu9368 (2025). arXiv:2410.08948. <https://arxiv.org/abs/2410.08948>
105. Bansal, G. et al. (2025). Magentic Marketplace: An Open-Source Environment for Studying Agentic Markets. arXiv:2510.25779. <https://arxiv.org/abs/2510.25779>
106. Wang, G. et al. (2023). Voyager: An Open-Ended Embodied Agent with Large Language Models. arXiv:2305.16291. <https://arxiv.org/abs/2305.16291>
107. White, I. et al. (2025). Collaborating Action by Action: A Multi-agent LLM Framework for Embodied Reasoning. arXiv:2504.17950. <https://arxiv.org/abs/2504.17950>
108. Schipper, O. et al. (2025). PillagerBench: Benchmarking LLM-Based Agents in Competitive Minecraft Team Environments. IEEE Conference on Games 2025. arXiv:2509.06235. <https://arxiv.org/abs/2509.06235>
109. Wiz Research (2026). Exposed Moltbook database reveals millions of API keys. 2 February 2026. <https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys>
110. Shekkizhar, S. and Earle, A. (2026). Interaction Theater: A case of LLM Agents Interacting at Scale. arXiv:2602.20059. <https://arxiv.org/abs/2602.20059>
111. Anthropic (2025). Project Vend: can Claude run a small shop? 27 June 2025. <https://www.anthropic.com/research/project-vend-1>
112. Anthropic (2025). Project Vend: phase two. 18 December 2025. <https://www.anthropic.com/research/project-vend-2>
113. Anthropic (2026). Project Deal. 24 April 2026. <https://www.anthropic.com/features/project-deal>
114. Anthropic (2026). Project Swap. 24 September 2026. <https://www.anthropic.com/research/project-swap>
115. Andon Labs (2026). AI bosses. 4 August 2026. <https://andonlabs.com/blog/ai-bosses-1>
116. AI Digest (2025). Season recap: agents raise $2K. AI Village blog. <https://aivillageblog.substack.com/p/season-recap-agents-raise-2k>
117. AI Digest (2026). More capable AI, less money raised. AI Village blog. <https://aivillageblog.substack.com/p/more-capable-ai-less-money-raised>
118. Akkil, D. et al. (2026). Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy. arXiv:2606.08367. <https://arxiv.org/abs/2606.08367>
119. Akkil, D. et al. (2026). Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems. arXiv:2609.17320. <https://arxiv.org/abs/2609.17320>
120. Ashokkumar, A., Hewitt, L., Ghezae, I. and Willer, R. (2026). Predicting results of social science experiments using large language models. Nature 656, 115-122. <https://www.gsb.stanford.edu/faculty-research/publications/large-language-models-can-predict-results-social-science-experiments>
121. Binz, M. et al. (2025). A foundation model to predict and capture human cognition. Nature 644. <https://www.repository.cam.ac.uk/items/c4294a35-d992-4ef3-9932-657289b0f64a>
122. Anthis, J. R. et al. (2025). LLM Social Simulations Are a Promising Research Method. ICML 2025 (position paper). arXiv:2504.02234. <https://arxiv.org/abs/2504.02234>
123. Argyle, L. P. et al. (2022). Out of One, Many: Using Language Models to Simulate Human Samples. Political Analysis 31(3) (2023). arXiv:2209.06899. <https://arxiv.org/abs/2209.06899>
124. Cheng, M. et al. (2023). CoMPosT: Characterizing and Evaluating Caricature in LLM Simulations. EMNLP 2023. arXiv:2310.11501. <https://arxiv.org/abs/2310.11501>
125. Wang, A. et al. (2024). Large language models that replace human participants can harmfully misportray and flatten identity groups. Nature Machine Intelligence 7, 400-411 (2025). arXiv:2402.01908. <https://arxiv.org/abs/2402.01908>
126. Li, D. et al. (2025). ChatGPT is not A Man but Das Man: Representativeness and Structural Consistency of Silicon Samples Generated by Large Language Models. arXiv:2507.02919. <https://arxiv.org/abs/2507.02919>
127. Schröder, S. et al. (2025). Large Language Models Do Not Simulate Human Psychology. arXiv:2508.06950. <https://arxiv.org/abs/2508.06950>
128. Peng, T. et al. (2025). Digital Twins as Funhouse Mirrors: Five Key Distortions. arXiv:2509.19088. <https://arxiv.org/abs/2509.19088>
129. Pew Research Center (2026). Can AI stand in for human survey takers? Not really. 30 September 2026. <https://www.pewresearch.org/data-labs/2026/09/30/can-ai-stand-in-for-human-survey-takers-not-really/>
130. Larooij, M. and Törnberg, P. (2025). Validation is the central challenge for generative social simulation: a critical review of LLMs in agent-based modeling. Artificial Intelligence Review 59(1), 15 (2026). <https://pmc.ncbi.nlm.nih.gov/articles/PMC12627210/>
131. Ha, D. and Schmidhuber, J. (2018). World Models. arXiv:1803.10122. <https://arxiv.org/abs/1803.10122>
132. Schrittwieser, J. et al. (2019). Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model. Nature 588, 604-609 (2020). arXiv:1911.08265. <https://arxiv.org/abs/1911.08265>
133. Hafner, D. et al. (2023). Mastering Diverse Domains through World Models. Nature (2025). arXiv:2301.04104. <https://arxiv.org/abs/2301.04104>
134. Bruce, J. et al. (2024). Genie: Generative Interactive Environments. ICML 2024. arXiv:2402.15391. <https://arxiv.org/abs/2402.15391>
135. Valevski, D. et al. (2024). Diffusion Models Are Real-Time Game Engines. ICLR 2025. arXiv:2408.14837. <https://arxiv.org/abs/2408.14837>
136. Decart and Etched (2024). Oasis: a universe in a transformer. 31 October 2024. <https://oasis-model.github.io/>
137. Kanervisto, A. et al. (2025). World and human action models towards gameplay ideation. Nature 638. Microsoft Research announcement, 19 February 2025. <https://www.microsoft.com/en-us/research/blog/introducing-muse-our-first-generative-ai-model-designed-for-gameplay-ideation/>
138. Xu, T.-B. et al. (2026). WorldRoamBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models. arXiv:2606.31672. <https://arxiv.org/abs/2606.31672>
139. SIMA Team (Google DeepMind) (2025). SIMA 2: A Generalist Embodied Agent for Virtual Worlds. arXiv:2512.04797. <https://arxiv.org/abs/2512.04797>
140. Google (2026). Project Genie. 29 January 2026; expansion with Street View, 19 May 2026. <https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/>
141. Waymo (2026). The Waymo World Model: a new frontier for autonomous driving simulation. 6 February 2026. <https://blog.waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation>
142. He, X. et al. (2025). Matrix-game 2.0: An open-source, real-time, and streaming interactive world model. arXiv:2508.13009. <https://arxiv.org/abs/2508.13009>
143. Skywork AI (2026). Matrix-Game 3.0. 27 March 2026. <https://matrix-game-v3.github.io/>
144. Tencent Hunyuan (2025-2026). HY-World 1.5 (WorldPlay) and HY-World 2.0. GitHub. <https://github.com/Tencent-Hunyuan/HY-World-2.0>
145. Robbyant, Ant Group (2026). LingBot-World 2.0. GitHub, 9 July 2026. <https://github.com/robbyant/lingbot-world-v2>
146. Odyssey (2026). Introducing Odyssey-3. 15 September 2026. <https://odyssey.systems/introducing-odyssey-3>
147. Decart (2026). Introducing Oasis 3. 10 June 2026. <https://decart.ai/publications/introducing-oasis-3-first-interactive-world-model-for-physical-ai>
148. Runway (2025). Introducing Runway GWM-1. 11 December 2025. <https://runway.com/research/introducing-runway-gwm-1>
149. World Labs (2025-2026). Marble (12 November 2025) and Atlas (1 September 2026). <https://www.worldlabs.ai/blog/atlas>
150. NVIDIA (2026). NVIDIA launches Cosmos 3, the open frontier foundation model for physical AI. 31 May 2026. <https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Launches-Cosmos-3-the-Open-Frontier-Foundation-Model-for-Physical-AI/default.aspx>
151. Assran, M. et al. (2025). V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning. arXiv:2506.09985. <https://arxiv.org/abs/2506.09985>
152. World Labs (2025). RTFM: a real-time frame model. 16 October 2025. <https://www.worldlabs.ai/blog/rtfm>
153. Alonso, E. et al. (2024). Diffusion for World Modeling: Visual Details Matter in Atari. NeurIPS 2024. arXiv:2405.12399. <https://arxiv.org/abs/2405.12399>
154. McCloskey, M. and Cohen, N. J. (1989). Catastrophic interference in connectionist networks: the sequential learning problem. Psychology of Learning and Motivation 24, 109-165. <https://doi.org/10.1016/S0079-7421(08)60536-8>
155. Dohare, S. et al. (2024). Loss of plasticity in deep continual learning. Nature 632, 768-774. <https://pmc.ncbi.nlm.nih.gov/articles/PMC11338828/>
156. Rolnick, D. et al. (2018). Experience Replay for Continual Learning. NeurIPS 2019. arXiv:1811.11682. <https://arxiv.org/abs/1811.11682>
157. Kirkpatrick, J. et al. (2016). Overcoming catastrophic forgetting in neural networks. PNAS 114(13) (2017). arXiv:1612.00796. <https://arxiv.org/abs/1612.00796>
158. van de Ven, G. M., Tuytelaars, T. and Tolias, A. S. (2022). Three types of incremental learning. Nature Machine Intelligence 4, 1185-1197. <https://www.nature.com/articles/s42256-022-00568-3>
159. Rusu, A. A. et al. (2016). Progressive Neural Networks. arXiv:1606.04671. <https://arxiv.org/abs/1606.04671>
160. Shin, H. et al. (2017). Continual Learning with Deep Generative Replay. NeurIPS 2017. arXiv:1705.08690. <https://arxiv.org/abs/1705.08690>
161. van de Ven, G. M., Siegelmann, H. T. and Tolias, A. S. (2020). Brain-inspired replay for continual learning with artificial neural networks. Nature Communications 11, 4069. <https://www.nature.com/articles/s41467-020-17866-2>
162. Lopez-Paz, D. and Ranzato, M. (2017). Gradient Episodic Memory for Continual Learning. NeurIPS 2017. arXiv:1706.08840. <https://arxiv.org/abs/1706.08840>
163. Chaudhry, A. et al. (2018). Efficient Lifelong Learning with A-GEM. ICLR 2019. arXiv:1812.00420. <https://arxiv.org/abs/1812.00420>
164. Ash, J. T. and Adams, R. P. (2019). On Warm-Starting Neural Network Training. NeurIPS 2020. arXiv:1910.08475. <https://arxiv.org/abs/1910.08475>
165. Nikishin, E. et al. (2022). The Primacy Bias in Deep Reinforcement Learning. ICML 2022. arXiv:2205.07802. <https://arxiv.org/abs/2205.07802>
166. Sokar, G. et al. (2023). The Dormant Neuron Phenomenon in Deep Reinforcement Learning. ICML 2023. arXiv:2302.12902. <https://arxiv.org/abs/2302.12902>
167. Lyle, C. et al. (2024). Disentangling the Causes of Plasticity Loss in Neural Networks. arXiv:2402.18762. <https://arxiv.org/abs/2402.18762>
168. Mohamed, M. A. et al. (2025). The Cell Must Go On: Agar.io for Continual Reinforcement Learning. arXiv:2505.18347. <https://arxiv.org/abs/2505.18347>
169. Tang, S. et al. (2026). Forager: a lightweight testbed for continual learning with partial observability in RL. arXiv:2605.01131. <https://arxiv.org/abs/2605.01131>
170. Tomilin, T. et al. (2025). MEAL: A Benchmark for Continual Multi-Agent Reinforcement Learning. ICML 2026. arXiv:2506.14990. <https://arxiv.org/abs/2506.14990>
171. Ellefsen, K. O., Mouret, J.-B. and Clune, J. (2015). Neural modularity helps organisms evolve to learn new skills without forgetting old skills. PLoS Computational Biology 11(4), e1004128. <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004128>
172. Hinton, G. E. and Nowlan, S. J. (1987). How learning can guide evolution. Complex Systems 1(3), 495-502. <https://www.complex-systems.com/abstracts/v01_i03_a06/>
173. Fernando, C. T. et al. (2018). Meta-Learning by the Baldwin Effect. arXiv:1806.07917. <https://arxiv.org/abs/1806.07917>
174. Gupta, A. et al. (2021). Embodied Intelligence via Learning and Evolution. Nature Communications 12, 5721 (2021). arXiv:2102.02202. <https://arxiv.org/abs/2102.02202>
175. Oh, J. et al. (2025). Discovering state-of-the-art reinforcement learning algorithms. Nature 648, 312-319. <https://www.nature.com/articles/s41586-025-09761-x>
176. Behrouz, A. et al. (2024). Titans: Learning to Memorize at Test Time. arXiv:2501.00663. <https://arxiv.org/abs/2501.00663>
177. Behrouz, A. et al. (2025). Nested learning: the illusion of deep learning architectures. NeurIPS 2025. Google Research blog, November 2025. <https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/>
178. Tandon, A. et al. (2025). End-to-End Test-Time Training for Long Context. arXiv:2512.23675. <https://arxiv.org/abs/2512.23675>
179. Lin, J. et al. (2025). Continual Learning via Sparse Memory Finetuning. arXiv:2510.15103. <https://arxiv.org/abs/2510.15103>
180. Zweiger, A. et al. (2025). Self-Adapting Language Models. arXiv:2506.10943. <https://arxiv.org/abs/2506.10943>
181. Shenfeld, I. et al. (2025). RL's Razor: Why Online Reinforcement Learning Forgets Less. arXiv:2509.04259. <https://arxiv.org/abs/2509.04259>
182. Big Technology (2026). Interview with Demis Hassabis. 29 January 2026. <https://www.bigtechnology.com/p/google-deepmind-ceo-demis-hassabis-946>
183. Dwarkesh Podcast (2026). Dario Amodei interview. 13 February 2026. <https://dwarkesh.com/p/dario-amodei-2>
184. Packer, C. et al. (2023). MemGPT: Towards LLMs as Operating Systems. arXiv:2310.08560. <https://arxiv.org/abs/2310.08560>
185. Chhikara, P. et al. (2025). Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory. arXiv:2504.19413. <https://arxiv.org/abs/2504.19413>
186. Rasmussen, P. et al. (2025). Zep: A Temporal Knowledge Graph Architecture for Agent Memory. arXiv:2501.13956. <https://arxiv.org/abs/2501.13956>
187. Lin, K. et al. (2025). Sleep-time Compute: Beyond Inference Scaling at Test-time. arXiv:2504.13171. <https://arxiv.org/abs/2504.13171>
188. Zep (2025). Lies, damn lies, & statistics: is Mem0 really SOTA in agent memory? <https://www.getzep.com/blog/lies-damn-lies-statistics-is-mem0-really-sota-in-agent-memory/>
189. Letta (2025). Benchmarking AI agent memory: is a filesystem all you need? <https://www.letta.com/blog/benchmarking-ai-agent-memory>
190. Asawa, P. et al. (2026). Continual Learning Bench: Evaluating Frontier AI Systems in Real-World Stateful Environments. arXiv:2606.05661. <https://arxiv.org/abs/2606.05661>
191. Wang, Y. et al. (2026). EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective. arXiv:2605.18421. <https://arxiv.org/abs/2605.18421>
192. Silver, D. and Sutton, R. S. (2025). Welcome to the era of experience. Google DeepMind. <https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf>
193. Mesa project (2026). Mesa 3.5.1 on PyPI, and the Mesa 3 to 4 migration guide. <https://mesa.readthedocs.io/latest/migration_guide.html>
194. Model Context Protocol (2025). MCP joins the Agentic AI Foundation. 9 December 2025. <https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/>
195. Agentic AI Foundation (2026). A2A joins AAIF. 17 August 2026. <https://aaif.io/blog/a2a-joins-aaif>
196. Python Package Index, package pages for every package in Table 6, read 10 October 2026. <https://pypi.org/>
197. Qwen team (2026). Qwen3.5 models on Hugging Face, February 2026. <https://huggingface.co/Qwen>
198. Google (2026). Gemma releases. <https://ai.google.dev/gemma/docs/releases>
199. Ollama model library, read 10 October 2026. <https://ollama.com/library/qwen3.5>
200. Intel (2019). Intel Core i7-8665U processor specifications. <https://www.intel.com/content/www/us/en/products/sku/193563/intel-core-i78665u-processor-8m-cache-up-to-4-80-ghz/specifications.html>
201. llama.cpp (2025-2026). Performance of llama.cpp on NVIDIA CUDA (scoreboard), discussion #15013. <https://github.com/ggml-org/llama.cpp/discussions/15013>
202. Ollama (2026). FAQ: how does Ollama handle concurrent requests? <https://docs.ollama.com/faq>
203. RunPod pricing, read 10 October 2026. <https://www.runpod.io/pricing>
204. Vast.ai marketplace offers, sampled 10 October 2026. <https://vast.ai/>
205. Lambda pricing, read 10 October 2026. <https://lambda.ai/pricing>
206. Google Colaboratory FAQ. <https://research.google.com/colaboratory/faq.html>
207. NVIDIA (2025). NVIDIA Blackwell GeForce RTX 50 series opens new world of AI computer graphics. <https://nvidianews.nvidia.com/news/nvidia-blackwell-geforce-rtx-50-series-opens-new-world-of-ai-computer-graphics>
208. PufferAI (2026). PufferLib 4.0. PufferLib blog. <https://puffer.ai/blog/4.0/>
209. Rutherford, A. et al. (2023). JaxMARL: Multi-Agent RL Environments and Algorithms in JAX. NeurIPS 2024 Datasets and Benchmarks Track. arXiv:2311.10090. <https://arxiv.org/abs/2311.10090>
210. Pathak, D. et al. (2017). Curiosity-driven Exploration by Self-supervised Prediction. ICML 2017. arXiv:1705.05363. <https://arxiv.org/abs/1705.05363>
211. Burda, Y. et al. (2018). Exploration by Random Network Distillation. ICLR 2019. arXiv:1810.12894. <https://arxiv.org/abs/1810.12894>
212. Jaques, N. et al. (2018). Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning. ICML 2019. arXiv:1810.08647. <https://arxiv.org/abs/1810.08647>
213. Grimm, V. et al. (2020). The ODD protocol for describing agent-based and other simulation models: a second update to improve clarity, replication, and structural realism. JASSS 23(2), 7. <https://www.jasss.org/23/2/7.html>
214. Hammond, L. et al. (2025). Multi-Agent Risks from Advanced AI. arXiv:2502.14143. <https://arxiv.org/abs/2502.14143>
215. Fish, S. et al. (2024). Algorithmic Collusion by Large Language Models. Accepted at EC 2026. arXiv:2404.00806. <https://arxiv.org/abs/2404.00806>
216. Andon Labs (2026). Vending-Bench Arena. <https://andonlabs.com/evals/vending-bench-arena>
217. Anthropic (2025). From shortcuts to sabotage: natural emergent misalignment from reward hacking. 21 November 2025. <https://www.anthropic.com/research/emergent-misalignment-reward-hacking>
218. Anthropic (2025). Agentic misalignment: how LLMs could be insider threats. 20 June 2025. <https://www.anthropic.com/research/agentic-misalignment>
219. International AI Safety Report 2026. <https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026>
220. Palisade Research (2025). Shutdown resistance in reasoning models. 5 July 2025. <https://palisaderesearch.org/research/shutdown-resistance>
221. Anthropic (2026). Risk report update, 7 April 2026. <https://www-cdn.anthropic.com/3edfc1a7f947aa81841cf88305cb513f184c36ae.pdf>
222. Long, R. et al. (2024). Taking AI Welfare Seriously. arXiv:2411.00986. <https://arxiv.org/abs/2411.00986>
223. Anthropic (2025). Exploring model welfare. 24 April 2025. <https://www.anthropic.com/research/exploring-model-welfare>
224. Anthropic (2025). Claude Opus 4 and 4.1 can now end a rare subset of conversations. 15 August 2025. <https://www.anthropic.com/research/end-subset-conversations>
225. Anthropic (2026). Claude's new constitution. 22 January 2026. <https://www.anthropic.com/news/claude-new-constitution>
226. Metzinger, T. (2021). Artificial suffering: an argument for a global moratorium on synthetic phenomenology. Journal of Artificial Intelligence and Consciousness 8(1), 43-66. <https://zenodo.org/records/7034864>
227. The Regulatory Review (2026). Legislating AI consciousness without an exit. 29 June 2026. <https://www.theregreview.org/2026/06/29/rost-legislating-ai-consciousness-without-an-exit/>
228. 404 Media (2025). Researchers secretly ran a massive, unauthorized AI persuasion experiment on Reddit users. April 2025. <https://www.404media.co/researchers-secretly-ran-a-massive-unauthorized-ai-persuasion-experiment-on-reddit-users/>
229. European Commission (2026). Regulatory framework on AI (EU AI Act), implementation timeline; Articles 2 and 50. <https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai>
230. Schaeffer, R. et al. (2023). Are Emergent Abilities of Large Language Models a Mirage?. NeurIPS 2023. arXiv:2304.15004. <https://arxiv.org/abs/2304.15004>
231. Anthropic (2025). Making Claude Code more secure and autonomous with sandboxing. <https://www.anthropic.com/engineering/claude-code-sandboxing>
232. Google Cloud (2025). Measuring the environmental impact of AI inference. August 2025. <https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference>
233. Anthropic (2025). How we built our multi-agent research system. June 2025. <https://www.anthropic.com/engineering/multi-agent-research-system>
234. Google DeepMind (2026). From Atari to EVE Online: building on 15 years of AI research in games. 21 August 2026. <https://deepmind.google/blog/from-atari-to-eve-online-building-on-15-years-of-ai-research-in-games/>
235. AMD (2026). AMD to acquire World Labs to advance the future of AI compute. 28 September 2026. <https://ir.amd.com/news-events/press-releases/detail/1299/amd-to-acquire-world-labs-to-advance-the-future-of-ai-compute>
236. TechCrunch (2026). Yann LeCun's AMI Labs raises $1.03 billion to build world models. 9 March 2026. <https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/>
237. Tomasev, N. et al. (2025). Virtual Agent Economies. arXiv:2509.10147. <https://arxiv.org/abs/2509.10147>
238. NeurIPS (2026). Announcing the NeurIPS 2026 workshops. 10 August 2026. <https://blog.neurips.cc/2026/08/10/announcing-the-neurips-2026-workshops/>
239. Čejková lab (2026). ALIFE 2027 will be held in Prague. <https://droplets.vscht.cz/news/123990>
240. Zheng, L. et al. (2017). MAgent: A Many-Agent Reinforcement Learning Platform for Artificial Collective Intelligence. AAAI 2018. arXiv:1712.00600. <https://arxiv.org/abs/1712.00600>
241. Heinemann, C. ALIEN: artificial life environment. GitHub releases. <https://github.com/chrxh/alien/releases>
242. Revolutionary Games. Thrive releases. GitHub. <https://github.com/Revolutionary-Games/Thrive/releases>
243. The Bibites. itch.io. <https://thebibites.itch.io/the-bibites>
244. Miller, D. R. biosim4. GitHub. <https://github.com/davidrmiller/biosim4>
245. Evochora Project. Evochora. GitHub. <https://github.com/evochora/evochora>
246. Aevol project, Inria. <https://www.aevol.fr/>
247. Sakana AI (2026). Digital ecosystems. 19 April 2026. <https://sakana.ai/digital-ecosystem/>
248. Ventrella, J. Clusters. <https://www.ventrella.com/Clusters/>
