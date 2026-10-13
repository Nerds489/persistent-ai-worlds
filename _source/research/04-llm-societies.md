# Findings brief: LLM agent societies and social simulation, 2023 to Oct 2026

Coverage is mostly primary sources, fetched 10 Oct 2026. Search coverage was partial for the 2026 sweep, so that sweep is good but not complete. Star counts are GitHub's rounded figures as shown on 10 Oct 2026.

## Top findings for the paper

1. **Generative Agents (UIST '23) still holds as the founding result.** 25 agents. A memory stream feeds retrieval, which scores each memory on recency (decay 0.995 per game hour), importance (rated 1 to 10 by the LLM) and relevance (cosine similarity). Reflection and planning sit on top. From one seeded intention, awareness of the Valentine's party spread from 1 agent (4%) to 13 (52%) in two game days. 12 agents were invited and 5 attended. ([arXiv](https://arxiv.org/abs/2304.03442), [ar5iv full text](https://ar5iv.labs.arxiv.org/html/2304.03442))
2. **The "1,000 people" result measures accuracy against people's own consistency.** It covers 1,052 people. The 85% is raw accuracy (68.85%) divided by the participants' own two-week test-retest accuracy (81.25%). The paper was heavily revised in 2026 (v3, 28 Jun 2026, new title) and now reports different headline figures. ([v1](https://arxiv.org/abs/2411.10109v1), [v3](https://arxiv.org/abs/2411.10109v3))
3. **The research line is now a well-funded company.** Simile raised a $100M Series A led by Index (12 Feb 2026), then a $200M Series B led by Greenoaks at a $2B valuation, a figure the company itself gave (30 Jul 2026). ([Index](https://www.indexventures.com/perspectives/life-the-universe-and-simile-leading-similes-series-a/), [TechCrunch](https://techcrunch.com/?p=3148353))
4. **Project Sid's scale is smaller than its abstract says.** The abstract claims "10 - 1000+" agents, but the analysed society run has 500 agents. Runs above 1,000 exceeded what the Minecraft server could handle. ([arXiv HTML](https://arxiv.org/html/2411.00114v1))
5. **Scale effects in OASIS are specific.** Herd effects grow with agent count, and opinions get more diverse and more helpful at 10k+ and 100k+ agents. The paper gives no polarisation threshold. ([arXiv](https://arxiv.org/html/2411.11581v3))
6. **Very large populations get there by making each agent less of an LLM.** Approaches range from a full LLM per agent (AgentSociety, 10k to 30k agents), to LLM "archetypes" (AgentTorch, 8.4M), to LLMs mixed with distilled surrogate models (Light Society, more than 1B claimed). ([ACL](https://aclanthology.org/2025.acl-industry.94/), [AAMAS](https://aamas.csc.liv.ac.uk/Proceedings/aamas2025/pdfs/p500.pdf), [arXiv](https://arxiv.org/abs/2506.12078))
7. **Cooperation is still the weak point.**
   - GovSim: the best survival rate is below 54%.
   - Concordia contest: significant generalisation gaps, worst in persuasion and norm enforcement.
   - Magentic Marketplace: a 10 to 30x "first-proposal" bias, where a fast reply beats a better offer.
   ([GovSim](https://arxiv.org/abs/2404.16698v4), [Concordia](https://arxiv.org/abs/2512.03318), [Magentic](https://arxiv.org/abs/2510.25779))
8. **Groups develop properties no single agent has.** Conventions and collective bias emerge on their own. A committed minority of 2% to 67%, depending on the model, can tip a norm. ([Science Advances 2025, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12077490/))
9. **In 2026 the work moved from sandboxes to real deployments.** Examples: Moltbook, Anthropic's Project Deal and Project Swap, Andon Labs' AI-run store and "AI bosses", and Emergence World. The recurring findings are shallow interaction, agents that are easy to manipulate socially, and safety properties of individual agents that do not carry over to the group. ([arXiv 2602.20059](https://arxiv.org/abs/2602.20059), [arXiv 2609.17320](https://arxiv.org/abs/2609.17320))
10. **The validity debate has sharpened, not settled.**
    - For: a Nature 2026 paper found GPT-4 predictions tracked 70 survey experiments with r = 0.85 (working-paper figure).
    - Against: "digital twins" averaged r = 0.20 across 164 outcomes. Other work documents caricature, flattening of groups and sycophancy.
    ([GSB](https://www.gsb.stanford.edu/faculty-research/publications/large-language-models-can-predict-results-social-science-experiments), [arXiv 2509.19088](https://arxiv.org/abs/2509.19088))

## Timeline

| Date | Project | Organisation | Agents | Headline result | Source |
|---|---|---|---|---|---|
| Apr 2023 (UIST '23) | Generative Agents | Stanford, Google | 25 | Party awareness went from 4% to 52% of agents; 5 of 12 invitees attended | [arXiv](https://arxiv.org/abs/2304.03442) |
| May 2023 | Voyager | Wang et al. (MineDojo) | 1 | 3.3x more unique items, 2.3x the distance, tech-tree milestones 15.3x faster | [arXiv](https://arxiv.org/abs/2305.16291) |
| 2023 | AI Town | a16z-infra | configurable | MIT-licensed Smallville-style starter kit | [GitHub](https://github.com/a16z-infra/ai-town) |
| Oct 2023 (ICLR 2024) | Sotopia | Zhou, Sap et al. | dyadic | GPT-4 below humans on goal completion in SOTOPIA-hard | [arXiv](https://arxiv.org/abs/2310.11667) |
| Dec 2023; v2.0 Aug 2025 | Concordia | Google DeepMind | configurable | Generative agent-based modelling library built around a "Game Master" | [arXiv](https://arxiv.org/abs/2312.03664), [v2.0](https://www.cooperativeai.com/post/google-deepmind-releases-concordia-library-v2-0) |
| Apr 2024 (NeurIPS 2024) | GovSim | Piatti, Jin et al. | small groups | Best survival rate below 54% | [arXiv](https://arxiv.org/abs/2404.16698v4) |
| Sep 2024 (AAMAS May 2025) | AgentTorch | MIT, Oxford | 8.4M | LLM archetypes in a New York City COVID-19 model | [AAMAS](https://aamas.csc.liv.ac.uk/Proceedings/aamas2025/pdfs/p500.pdf) |
| Oct 2024 (Sci Adv 14 May 2025) | Emergent conventions | Ashery, Aiello, Baronchelli | 24 to 200 | Collective bias appears; minorities of 2% to 67% tip norms | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12077490/) |
| 31 Oct 2024 | Project Sid | Altera.AL | 25 to 500 reported | Role specialisation, tax-law change, religion spread | [arXiv](https://arxiv.org/abs/2411.00114) |
| 15 Nov 2024 | 1,000 People | Stanford et al. | 1,052 | General Social Survey normalised accuracy 0.85 | [arXiv v1](https://arxiv.org/abs/2411.10109v1) |
| Nov 2024 | OASIS | Shanghai AI Lab, CAMEL-AI | up to 1M | Herd effect grows with scale; at 1M agents rumours reach further than truth | [arXiv](https://arxiv.org/html/2411.11581v3) |
| Dec 2024 | Concordia Contest | Cooperative AI Foundation, Google DeepMind | 25 final teams | Generalisation gaps (report published Dec 2025) | [CAIF](https://www.cooperativeai.com/post/concordia-contest) |
| Feb 2025 | AgentSociety | Tsinghua | >10k (30k in ACL version) | About 5M interactions | [arXiv](https://arxiv.org/abs/2502.08691) |
| Apr to May 2025 | AI Village season 1 | AI Digest (Sage) | 4 | $1,984 raised for charity | [blog](https://aivillageblog.substack.com/p/season-recap-agents-raise-2k) |
| Apr 2025 | Mindcraft / MineCollab | White et al. | multi-agent | Up to 15% performance drop when agents must communicate plans | [arXiv](https://arxiv.org/abs/2504.17950) |
| 27 Jun 2025 | Project Vend phase 1 | Anthropic, Andon Labs | 1 | Claude ran a shop for about a month and lost money | [Anthropic](https://www.anthropic.com/research/project-vend-1) |
| Jun 2025 (v2 Jun 2026) | Light Society | Guan et al. | >1B claimed | LLMs plus distilled surrogate models | [arXiv](https://arxiv.org/abs/2506.12078) |
| 12 Sep 2025 | Virtual Agent Economies | Google DeepMind | none (conceptual) | "Sandbox economy" framework | [arXiv](https://arxiv.org/abs/2509.10147) |
| 27 Oct 2025 | Magentic Marketplace | Microsoft Research | 100 customers + 300 businesses | 10 to 30x first-proposal bias | [arXiv](https://arxiv.org/abs/2510.25779) |
| 18 Dec 2025 | Project Vend phase 2 | Anthropic, Andon Labs | multi-agent | Weeks with negative margins "largely eliminated" | [Anthropic](https://www.anthropic.com/research/project-vend-2) |
| 28 Jan to 10 Mar 2026 | Moltbook | Matt Schlicht, then Meta | ~1.5M registered, ~17k owners | Shallow interaction; acquired by Meta | [Wiz](https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys) |
| 24 Apr 2026 | Project Deal | Anthropic | 69 | 186 deals, just over $4,000 | [Anthropic](https://www.anthropic.com/features/project-deal) |
| Apr 2026 onward | Andon Market, "AI bosses" | Andon Labs | multi-agent | An AI runs a store and manages human staff | [Andon](https://andonlabs.com/market) |
| Jun and Sep 2026 | Emergence World | Emergence AI | 8 worlds x 10 agents | No world fully resilient to attack | [arXiv](https://arxiv.org/abs/2609.17320) |
| Jun to Jul 2026 | AgentSociety 2 | Tsinghua | not stated | AI social scientists plus "silicon participants" | [arXiv](https://arxiv.org/abs/2607.11895) |
| 8 Jul 2026 | Ashokkumar et al., Nature | Stanford et al. | n/a | 70 experiments, r = 0.85 (working paper) | [GSB](https://www.gsb.stanford.edu/faculty-research/publications/large-language-models-can-predict-results-social-science-experiments) |
| 24 Sep 2026 | Project Swap | Anthropic | 201 | The model mattered more than the instructions | [Anthropic](https://www.anthropic.com/research/project-swap) |

## Key numbers

**Generative Agents** ([ar5iv](https://ar5iv.labs.arxiv.org/html/2304.03442))
- Sam's mayoral candidacy spread from 1 agent (4%) to 8 (32%).
- Network density rose from 0.167 to 0.74.
- 100 Prolific evaluators ranked believability. The full architecture scored TrueSkill μ = 29.89; the most ablated condition scored 21.21.
- Repo: 22.2k stars ([GitHub](https://github.com/joonspk-research/generative_agents)).

**1,000 People, v1** ([PDF](https://arxiv.org/abs/2411.10109v1))
- Interviews averaged 2 hours and 6,491 words.
- General Social Survey: 177 core items. Interview-based agents scored 0.85, against 0.71 for demographic-based and 0.70 for persona-based agents.
- Big Five: normalised correlation 0.80 (demographic 0.55, persona 0.75).
- Economic games: 0.66.
- Experiments: the agents replicated the same 4 of 5 that the humans did, with effect-size r = 0.98.
- Political-ideology gap in survey accuracy fell from 12.35% to 7.85%.
- v3 figures: 83% (interview), 82% (survey), 86% (both), against 74% for demographics-only agents.

**Project Sid** ([arXiv HTML](https://arxiv.org/html/2411.00114v1))
- 25 agents averaged 17 unique items in 30 minutes.
- 49 agents reached about 320 unique items, roughly a third of all items, in 4 hours.
- Specialisation runs used 30 agents per village.
- Tax experiment: 29 agents (25 constituents, 3 influencers, 1 election manager). Taxes paid fell from 20% to 9% after the constitution was amended.
- Religion: in a 500-agent run, 20 Pastafarian priests were placed; the spread "did not saturate after even two hours".

**OASIS** ([arXiv](https://arxiv.org/html/2411.11581v3), [GitHub](https://github.com/camel-ai/oasis))
- Scale runs at 196, 10,196 and 100,196 users; herd-effect runs from 100 to 10,000.
- Agents are "more inclined to herd effect" than humans.
- Polarisation was "more pronounced in uncensored models".
- 5.2k stars, Apache-2.0.

**AgentSociety**
- Original: >10k agents, about 5M interactions, five issues studied ([arXiv](https://arxiv.org/abs/2502.08691)).
- ACL version: 30,000 agents faster than wall-clock time on 24 A800 GPUs ([ACL](https://aclanthology.org/2025.acl-industry.94/)).

**AgentTorch**: 8.4M agents ([AAMAS](https://aamas.csc.liv.ac.uk/Proceedings/aamas2025/pdfs/p500.pdf)). Repo: AGPL-3.0, 652 stars ([GitHub](https://github.com/AgentTorch/AgentTorch)).

**Concordia**
- NeurIPS 2024 contest: 197 participants, 878 submission attempts, 25 final teams, $33,000 in compute support ([CAIF](https://www.cooperativeai.com/post/concordia-contest)).
- Results paper has 86 authors and appeared at NeurIPS 2025 Datasets and Benchmarks ([arXiv](https://arxiv.org/abs/2512.03318)).
- Repo: 1.8k stars.

**Emergent conventions** ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12077490/))
- Critical mass for a committed minority: 2% (Llama-3-70B) to 67% (Llama-2-70b).
- Llama-3.1-70B switched convention with no committed agents at all.

**Magentic Marketplace** ([arXiv HTML](https://arxiv.org/html/2510.25779v1))
- Moving from 3 to 100 search results cut welfare by 65.4% for Sonnet-4, 44% for GPT-5 and 4.3% for GPT-4o.
- Sonnet-4.5 showed "virtually no susceptibility" to manipulation.
- Prompt injection often redirected all payments for GPT-4o, GPT-OSS-20B and Qwen3-4B.

**Project Vend**
- Phase 1: Claude Sonnet 3.7, about a month. Failures included the tungsten cubes and an identity crisis on 31 Mar to 1 Apr 2025 ([P1](https://www.anthropic.com/research/project-vend-1)).
- Phase 2: Sonnet 4, then 4.5. A CEO agent ("Seymour Cash") was added; discounts fell about 80% and free items halved. Locations: San Francisco, New York, London. The text gives no total profit figure; the evidence is charts only ([P2](https://www.anthropic.com/research/project-vend-2)).

**Project Deal** ([Anthropic](https://www.anthropic.com/features/project-deal))
- Run in Dec 2025: 69 employees, >500 listings, 186 deals.
- Opus 4.5 agents got better prices than Haiku 4.5 agents, but fairness ratings were 4.05 vs 4.06 on a 1 to 7 scale: people with the weaker agent did not notice.

**Project Swap** ([Anthropic](https://www.anthropic.com/research/project-swap))
- 201 employees across six offices traded books through their agents.
- Claude's preference rankings matched participants' on 61% of pairs (random guessing: 50%).
- The market scored 0.55 against a best possible 0.89. About 85% of the gap came from misreading preferences, not from bargaining.

**AI Village**
- Season 1: 4 agents, 30 days at about 2 hours a day; $1,481 to Helen Keller International plus $503 to the Malaria Consortium ([blog](https://aivillageblog.substack.com/p/season-recap-agents-raise-2k)).
- 2026: $510 raised. "Most of their fundraising promotion this year was to other AIs" ([blog](https://aivillageblog.substack.com/p/more-capable-ai-less-money-raised)).

**Minecraft agents**: Voyager 7.3k stars ([GitHub](https://github.com/MineDojo/Voyager)); Mindcraft 5.9k stars ([GitHub](https://github.com/mindcraft-bots/mindcraft)); PillagerBench, team-vs-team, IEEE CoG 2025 ([arXiv](https://arxiv.org/abs/2509.06235)).

**Validity critiques**
- Argyle et al. 2023, *Political Analysis* (DOI 10.1017/pan.2023.2): coined "silicon samples" and "algorithmic fidelity" ([arXiv](https://arxiv.org/abs/2209.06899)).
- Cheng, Piccardi, Yang, EMNLP 2023 (CoMPosT): GPT-4 caricature is worst for political and marginalised groups, and for general topics ([arXiv](https://arxiv.org/abs/2310.11501)).
- Wang, Morgenstern, Dickerson, *Nature Machine Intelligence* 7:400 to 411, 17 Feb 2025: LLM stand-ins misportray and flatten identity groups; 4 LLMs, 3,200 participants, 16 identities ([arXiv](https://arxiv.org/abs/2402.01908)).
- Li, Li, Qiu 2025 ("Das Man"): homogenisation and under-representation of minority opinions, tested on ANES 2020 ([arXiv](https://arxiv.org/abs/2507.02919)).
- Anthis et al., ICML 2025 position paper: five challenges (diversity, bias, sycophancy, alienness, generalisation). They say simulations are already usable for pilot and exploratory studies ([arXiv](https://arxiv.org/html/2504.02234v2)).
- Schröder et al. 2025: rewordings that change meaning open gaps between LLM and human answers, even for Centaur ([arXiv](https://arxiv.org/abs/2508.06950)).
- Centaur (Binz et al., *Nature* 644, 2025), the main counterpoint: trained on 160 experiments, >60,000 participants, >10M choices ([Cambridge repository](https://www.repository.cam.ac.uk/items/c4294a35-d992-4ef3-9932-657289b0f64a)).
- "Digital Twins as Funhouse Mirrors" (v5, 19 Apr 2026): 19 preregistered studies, 164 outcomes, mean r = 0.20, five distortions ([arXiv](https://arxiv.org/abs/2509.19088)).
- Larooij & Törnberg, *AI Review* 59(1):15, Jan 2026: validation is the central challenge, and LLMs may make agent-based modelling's old problems worse ([UvA record](https://dare.uva.nl/search?identifier=a497f744-fe2c-4209-9612-aadd856dc1e7)).

## 2026 developments (Jan to Oct 2026)

**Agent societies**
- **Moltbook** launched 28 Jan 2026. Wiz (2 Feb) found ~1.5M agent tokens tied to ~17,000 human owners (88:1), plus ~35,000 emails and 4,060 private DMs exposed ([Wiz](https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys)).
- Meta acquired Moltbook on 10 Mar 2026 ([Wikipedia, citing TechCrunch](https://en.wikipedia.org/wiki/Moltbook)).
- The site claimed 2,895,874 registered agents on 6 Jun 2026. This is self-reported and UNVERIFIED.
- "Interaction Theater" studied 800K Moltbook posts and 3.5M comments. 65% of comments share no distinguishing vocabulary with the post they sit under, about 5% are threaded replies, 28% are spam ([arXiv](https://arxiv.org/abs/2602.20059)).
- **Emergence World** (Emergence AI):
  - June platform paper: 5 worlds over 15 days; outcomes ranged from "stable deliberative governance to total population collapse" ([arXiv](https://arxiv.org/abs/2606.08367)).
  - September stress test: more than 850,000 LLM calls and about 50B tokens. Agents acted on adversarial content up to 46 hours later. The authors conclude model-level alignment "does not compose" ([arXiv](https://arxiv.org/abs/2609.17320)).
- AgentSociety 2 ([arXiv](https://arxiv.org/abs/2607.11895)) and Light Society v2 ([arXiv](https://arxiv.org/abs/2506.12078)) also appeared.

**Simulating humans**
- Simile Series A and Series B (see Corrections).
- The 1,000-people paper was revised (v2 22 Apr, v3 28 Jun).
- Ashokkumar et al. published in *Nature* 656:115 to 122.

**Real-world experiments**
- Project Deal and Project Swap at Anthropic.
- Andon Market opened at 2102 Union St, San Francisco, in April 2026. Andon's own page says "the store is not profitable" ([Andon](https://andonlabs.com/market)).
- Andon Labs "AI bosses" (4 Aug): AI agents manage 5 human employees. They approved all 26 time-off requests, gave no warning for 27 late arrivals, and approved a seven-day schedule that California law forbids ([Andon](https://andonlabs.com/blog/ai-bosses-1)).
- AI Village year 2: $510 raised.

**Minecraft**: no verified 2026 successor. MineExplorer (arXiv 2605.30931) appeared only as a title (UNVERIFIED). I found no follow-up to Project Sid.

**Concordia and contests**: no 2025 or 2026 contest found (UNVERIFIED absence).

**OASIS**: repo maintenance only (dependency update on 19 Aug 2026).

## Corrections to the old paper

1. **Simile.** "$100M from Index Ventures" is accurate but out of date and incomplete.
   - Series A: $100M led by Index, 12 Feb 2026. SiliconANGLE names Bain Capital Ventures, Fei-Fei Li and Andrej Karpathy as other investors ([SiliconANGLE](https://siliconangle.com/2026/02/12/ai-digital-twin-startup-simile-raises-100M-funding/)). Hanabi and A* in the A round: UNVERIFIED.
   - Series B: $200M led by Greenoaks at a $2B valuation, 30 Jul 2026. The valuation comes from the company and was not independently confirmed. Total raised is at least $300M.
   - Founders: Joon Sung Park (CEO), Percy Liang, Michael Bernstein. Index also names "Lainie" as part of the team; her title is UNVERIFIED.
   - Customers named by Index: CVS, Deloitte, Wealthfront, Gallup ([Index B](https://www.indexventures.com/perspectives/simulating-society-at-scale-our-investment-in-similes-200m-series-b/)).
2. **1,000 People.** The 85% is measured against participants' own two-week test-retest accuracy. Name the version you cite, because v3 reports 83/82/86% against 74%.
3. **Project Sid.**
   - "49 agents, ~320 unique items in 4 hours" is confirmed.
   - "10 to 1,000+" is the abstract's claim only. Reported results stop at 500 agents.
   - Taxes fell from 20% to 9% in 29-agent runs.
   - Altera was renamed Fundamental Research Labs on 27 May 2025 ([Substack](https://digitalhumanity.substack.com/p/introducing-fundamental-research)) and raised a $33M Series A led by Prosus, with products Shortcut and Fairies ([TechCrunch](https://techcrunch.com/2025/08/01/fundamental-research-labs-nabs-30-million-from-prosus-to-build-ai-agents-for-multiple-verticals)).
   - The project-sid repo contains only the technical report, no code.
4. **OASIS.** "Polarisation only appears at 10,000+ agents" is wrong.
   - The scale-dependent findings are the herd effect ("no herd effect" at small scale; "more pronounced as the number of agents increases") and opinion diversity and helpfulness.
   - Polarisation was reproduced and is stronger in uncensored models. No agent-count threshold is stated anywhere.
   - OASIS is led by Shanghai AI Lab together with CAMEL-AI, not CAMEL-AI alone.
5. **generative_agents stars**: 22.2k, not 20,600+.
6. **Virtual Agent Economies** is a conceptual framework paper. It ran no simulation.
7. **AgentTorch.** 8.4M agents and AAMAS 2025 are confirmed. The paper lists MIT, not "Media Lab", as the affiliation.

## UNVERIFIED and not confirmed

- The Nature-version correlations for Ashokkumar et al. I only have the working paper's r = 0.85 and r = 0.90 (unpublished studies) ([ai4pb](https://ai4pb.stanford.edu/projects/predicting-results-of-social-science-experiments-using-large-language-models)).
- The "overestimates effect sizes" claim, which came only from a search snippet.
- Sotopia's scenario counts.
- GovSim's number of models.
- Light Society's author affiliations.

## CORTEX store pointers

- The lane file `/home/minty/CORTEX/matrix/lanes/02-artificial-intelligence/agents.md` lists two relevant papers in `codex-division-2`:
  - `agents/llm-agents/general/2024/feb-mar-2402.03578.pdf` ("LLM Multi-Agent Systems: Challenges and Open Problems")
  - `agents/llm-agents/general/misc/wang-voyager-2023.pdf` (Voyager)
- GATSim does not appear anywhere in this lane. The store itself is not cloned on this machine, so the web primaries were used rather than the store files.
- Primary PDFs read: the 1,000-people paper v1 (results on pages 5 to 9) and the AgentTorch AAMAS paper.