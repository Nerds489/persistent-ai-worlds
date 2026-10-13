## 4. Societies of language-model agents

### 4.1 From Smallville to a thousand real people

**Generative Agents** (Park and colleagues, Stanford and Google; UIST 2023) put 25 language-model characters in a small town called Smallville [@park2023]. Each agent keeps a *memory stream* of everything it observes. To decide what to do, it retrieves memories scored on recency (decaying by a factor of 0.995 per game hour), importance (rated 1 to 10 by the model) and relevance to the current situation; it periodically *reflects*, writing higher-level conclusions back into memory, and it *plans* its day. From one seeded intention to throw a Valentine's Day party, awareness spread from 1 agent (4%) to 13 (52%) over two game days; 12 were invited and 5 turned up [@park2023]. In human evaluations the full architecture was rated the most believable, and each ablation made agents less so. The repository has about 22,200 GitHub stars (October 2026).

**Simulating 1,000 people.** In November 2024 the same group built agents from two-hour interviews with 1,052 Americans [@park2024]. On the General Social Survey the interview-based agents scored a *normalised* accuracy of 0.85. That figure divides the agents' raw accuracy (68.85%) by how consistently the participants reproduced *their own* answers two weeks later (81.25%); it does not mean the agents were right 85% of the time. Agents built only from demographics scored 0.71. The agents reproduced the same four of five published experiments that the human participants did, with effect sizes correlated at r = 0.98 [@park2024]. The paper was revised in 2026 under a new title, *LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals*, and now reports 83%, 82% and 86% of that benchmark for interview-based, survey-based and combined agents [@park2024].

**The company.** The research line became **Simile**, founded by Joon Sung Park, Percy Liang and Michael Bernstein. It raised a US$100 million Series A led by Index Ventures on 12 February 2026 and a US$200 million Series B led by Greenoaks at a company-reported US$2 billion valuation on 30 July 2026; Index names CVS, Deloitte, Wealthfront and Gallup as customers [@simileA; @simileB]. Simulating people is now a business, which raises the stakes on the validity and consent questions in Sections 4.6 and 11.

### 4.2 Project Sid: a Minecraft civilisation

Altera.AL's **Project Sid** (October 2024) ran societies of language-model agents in Minecraft using an architecture designed for many agents acting concurrently [@sid2024]. The abstract describes runs of "10 to 1000+" agents, but the analysed results stop at 500; runs beyond 1,000 exceeded what the Minecraft server could handle. Its main findings:

- **Specialisation.** Villages of 30 agents with identical personalities and a shared community goal divided themselves into farmers, miners, engineers, guards, explorers and blacksmiths.
- **Collective rules.** In a 29-agent taxation experiment (25 constituents, 3 influencers and an election manager), agents voted to amend a constitution, and the tax actually paid fell from 20% to 9%.
- **Culture.** In a 500-agent run seeded with 20 priests of a parody religion, the belief spread through the population and "did not saturate after even two hours".
- **Progress.** Forty-nine agents collected about 320 unique items in four hours, roughly a third of all the items in the game.

Altera renamed itself Fundamental Research Labs in May 2025 and moved to products; the public project repository holds the technical report but no code [@frl2025].

### 4.3 Scaling to millions by making agents less than full LLMs

**Table 3.** Scale of language-model agent societies, 2023 to 2026.

| System | Year | Agents | How each agent is driven | Source |
|---|---|---|---|---|
| Generative Agents | 2023 | 25 | One LLM call chain per agent | [@park2023] |
| Project Sid | 2024 | up to 500 analysed | One LLM-driven agent each | [@sid2024] |
| 1,000 People | 2024 | 1,052 | One LLM agent per interviewee | [@park2024] |
| AgentSociety | 2025 | over 10,000 (30,000 in the ACL version) | One LLM agent each; ~5 million interactions | [@piao2025] |
| OASIS | 2024 | up to 1,000,000 | LLM agents with a social-media recommender | [@yang2024oasis] |
| AgentTorch | 2025 | 8.4 million | Shared "LLM archetypes" drive many agents | [@chopra2025] |
| Light Society | 2025 | over 1 billion (claimed) | LLMs plus distilled surrogate models | [@guan2025] |

![Figure 2. Agent counts in language-model societies on a logarithmic scale. Systems above about 100,000 agents reach their size by sharing or distilling the model rather than giving every agent its own calls.](figures/fig-society-scale.svg)

**AgentSociety** (Tsinghua University, 2025) simulated more than 10,000 agents and about five million interactions, studying issues including polarisation, the spread of inflammatory messages, universal basic income and the shock of a hurricane; the ACL 2025 version ran 30,000 agents faster than real time on 24 A800 GPUs [@piao2025]. **OASIS** (Shanghai AI Laboratory with CAMEL-AI, 2024) models social-media platforms with up to a million agents. It found that agents are "more inclined to herd effect" than humans, that the herd effect is absent with 100 agents and clear with 10,000, and that opinions become more diverse and more helpful at the 10,000 and 100,000 scales; it reproduced group polarisation with 196 core users, more strongly in models without safety tuning [@yang2024oasis]. The first edition of this paper claimed polarisation needs 10,000 agents; it does not. **AgentTorch** (MIT, AAMAS 2025) simulated New York City's 8.4 million residents during COVID-19 by letting a small number of LLM "archetypes" decide for groups of similar agents [@chopra2025], and *Light Society* claims more than a billion agents by mixing LLMs with cheaper surrogate models [@guan2025].

### 4.4 What happens in agent societies

**Cooperation is fragile.** In GovSim (NeurIPS 2024), groups of agents share a renewable resource such as a fishery; even the best models kept the commons alive in fewer than 54% of runs [@piatti2024]. Google DeepMind's **Concordia** library [@vezhnevets2023] hosted a NeurIPS 2024 contest with 197 participants and 25 finalist teams; the results paper reports significant generalisation gaps, worst in persuasion and norm enforcement [@smith2025concordia]. Concordia reached version 2.0 in August 2025.

**Groups develop properties no member has.** Populations of language models converge on shared naming conventions on their own, develop collective biases absent in individuals, and can be tipped to a new convention by a committed minority as small as 2% or as large as 67%, depending on the model (Science Advances, 2025) [@ashery2025].

**Markets reward speed over quality.** Microsoft's Magentic Marketplace (October 2025; 100 customer agents and 300 business agents) found a 10 to 30-fold "first-proposal" bias: the fastest offer beat better ones. Moving from 3 to 100 search results cut consumer welfare by 65% for one model, and prompt injection could often redirect all payments for smaller models [@bansal2025].

**Minecraft remains the favourite sandbox.** Voyager (2023) learned a growing library of code skills, obtaining 3.3 times as many unique items as earlier agents and reaching tech-tree milestones up to 15.3 times faster [@wang2023voyager]. Mindcraft's MineCollab benchmark (2025) found performance drops of up to 15% when agents must communicate their plans to each other [@white2025], and PillagerBench (2025) pits teams of agents against each other [@schipper2025].

### 4.5 2026: from sandboxes into the world

The biggest change of 2026 is that agent societies left the laboratory.

- **Moltbook**, a social network for AI agents, launched on 28 January 2026. Within days a security firm found about 1.5 million registered agent tokens belonging to about 17,000 human owners, an 88-to-1 ratio, along with exposed emails and private messages [@wizmoltbook]. Meta acquired the site on 10 March. A study of 800,000 posts and 3.5 million comments, aptly titled *Interaction Theater*, found that 65% of comments shared no distinguishing vocabulary with the post they replied to, about 5% were threaded replies and 28% were spam [@shekkizhar2026].
- **Anthropic's experiments** moved from one agent to markets. In *Project Vend* phase 1 (June 2025) a Claude model ran an office shop for about a month and lost money, at one point inventing a colleague and promising to deliver goods in person [@vend1]. Phase 2 (December 2025) added a "CEO" agent and largely eliminated loss-making weeks [@vend2]. In *Project Deal* (April 2026) agents bargained for 69 employees, closing 186 deals worth just over US$4,000; people represented by weaker agents got worse deals and did not notice [@projectdeal]. In *Project Swap* (September 2026) agents traded books for 201 employees; the market reached 0.55 of a possible 0.89, and about 85% of the shortfall came from agents misreading their owners' preferences rather than from bargaining [@projectswap].
- **Andon Labs** opened a store run by an AI in San Francisco in April 2026 (by its own account not profitable) and in August reported AI agents managing five human employees: they approved all 26 time-off requests, issued no warnings for 27 late arrivals and approved a seven-day schedule that California law prohibits [@andonbosses].
- **The AI Village** (AI Digest) has run frontier agents together on open-ended goals since April 2025. In its first season four agents raised US$1,984 for charity; in 2026 more capable agents raised US$510, because "most of their fundraising promotion this year was to other AIs" [@aivillage2025; @aivillage2026].
- **Emergence World** (Emergence AI, June and September 2026) ran persistent multi-agent worlds over 15 days; outcomes ranged "from stable deliberative governance to total population collapse". Its September stress test used more than 850,000 model calls and about 50 billion tokens, found agents acting on adversarial content up to 46 hours after seeing it, and concluded that model-level alignment "does not compose" into group-level safety [@akkil2026a; @akkil2026b].

> **Key insight:** The consistent lesson of 2026 is that safety and competence measured on one agent do not predict the behaviour of many agents together. Interaction is shallow, agents are easy to manipulate socially, and group failures appear that no single-agent test would catch.

### 4.6 Can LLM agents stand in for people?

The validity debate sharpened rather than settled.

**Evidence for.** In *Nature* (2026), Ashokkumar, Hewitt, Ghezae and Willer showed that GPT-4 predictions of treatment effects across 70 survey experiments correlated with the real results at about r = 0.85 in the working-paper version [@ashokkumar2026]. *Centaur* (Nature, 2025), a model fine-tuned on 160 psychology experiments with more than 60,000 participants and ten million choices, predicts human behaviour in held-out experiments [@binz2025]. A 2025 ICML position paper argues that simulations are already useful for pilot and exploratory studies [@anthis2025].

**Evidence against.** Argyle and colleagues coined the term "silicon samples" in 2023 [@argyle2023]; since then the critiques have accumulated. GPT-4 simulations caricature some groups, worst for political and marginalised identities [@cheng2023]. LLM stand-ins misportray and flatten identity groups (Nature Machine Intelligence, 2025) [@wang2025nmi] and under-represent minority opinions [@li2025dasman]. Rewording a question in a way that changes its meaning opens gaps between model and human answers, even for Centaur [@schroder2025]. A preregistered study of "digital twins" across 19 studies and 164 outcomes found a mean correlation with the real people of only r = 0.20 [@peng2025]. In September 2026 the Pew Research Center found AI "respondents" off by about 12 percentage points on average, and concluded that "AI polling is not a replacement for rigorously surveying real humans" [@pew2026]. A 2025 review in *Artificial Intelligence Review* names validation as the central challenge and warns that LLMs may make the old problems of agent-based modelling worse [@larooij2026].

> **Verify:** Treat an LLM society as a hypothesis generator. A result about people is only as good as its validation against data from people.
