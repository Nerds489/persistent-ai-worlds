# Findings brief: artificial life (ALife) and digital evolution, up to 10 October 2026

**How this was checked:** where possible, the primary sources themselves were read: the Nature 2003 PDF, Ray's 1991 chapter (a scan), the Ofria et al. 2009 chapter, arXiv pages, Crossref DOI records, the official conference sites and the GitHub API. Search coverage was partial, so anything marked UNVERIFIED could not be checked, and "none found" for 2026 is weaker evidence than usual.

## Top findings for the paper

1. **Origins.** The term "artificial life" was already in print in October 1986, in the title of Langton's paper "Studying artificial life with cellular automata" (Physica D 22:120-149) ([doi](https://doi.org/10.1016/0167-2789(86)90237-x)). The first workshop was held at Los Alamos in September 1987. It was sponsored by CNLS, the Santa Fe Institute and Apple, about 160 people attended, and the proceedings came out in 1989 ([Routledge](https://www.routledge.com/Artificial-Life-Proceedings-Of-An-Interdisciplinary-Workshop-On-The-Synthesis-And-Simulation-Of-Living-Systems/Langton/p/book/9780367152772)). Bedau (TICS 7(11), November 2003) gives the standard three-way split: soft ALife is "simulations or other purely digital constructions", hard ALife is "hardware implementations", and wet ALife "synthesizes living systems out of biochemical substances". He also credits Langton with coining the phrase ([doi](https://doi.org/10.1016/j.tics.2003.09.012)).

2. **Tierra (Ray 1991): the famous results are real, with caveats.** The run starts from a hand-written ancestor of 80 instructions, 48 of which are no-ops, in a soup of 60,000 instructions. Parasites of 45 instructions "begin to emerge within the first few million instructions". Size-79 hosts evolved immunity, and size-51 parasites then got round it. Hyper-parasites drove the parasites extinct. Social hyper-parasites followed (61 instructions, 24% smaller than the ancestor), then "hyper-hyper-parasite cheaters" ([Ray](https://tomray.me/pubs/alife2/Ray1991AnApproachToTheSynthesisOfLife.pdf)). The mutualistic symbionts in the paper were cut apart by hand. Ray says it is "not known if such relationships have evolved spontaneously".

3. **Avida's EQU result (Lenski, Ofria, Pennock, Adami, Nature 423:139-144, 2003) is narrower than usually told.**
   - 23 of 50 populations evolved EQU.
   - When only EQU was rewarded, 0 of 50 did.
   - Across 36 environments with reduced rewards, 124 of 360 (34%) did.
   - In the case-study population, 18 of the 111 steps leading to EQU were deleterious. The step just before EQU was a deleterious mutation that knocked out NAND, and reverting it removed EQU.
   - Across all 23 populations that evolved EQU, 5 of the mutations one step before it were deleterious, and in 3 of those EQU depended on them ([Nature](https://www.nature.com/articles/nature01568)).

4. **The throughput figure is genuine but dated.** Ofria, Bryson & Wilke (2009), p. 7: "population with 10,000 organisms can have 20,000 generations processed per day on a modern desktop computer" ([chapter](https://www.cse.msu.edu/~ofria/pubs/2009AvidaIntro.pdf)). Moreno et al. (2024) restate this as "about two hundred million individual replication cycles daily" on one CPU. Their own Cerebras wafer-scale genetic algorithm reaches "upwards of 1 million generations a minute for population sizes reaching 16 million agents". That uses a simple agent model, not Avida ([arXiv 2404.10861](https://arxiv.org/abs/2404.10861)).

5. **The Lenia family.**
   - Chan's original Lenia (arXiv December 2018; Complex Systems 28(3):251-286, 2019) reports "More than 400 species in 18 families" ([arXiv](https://arxiv.org/abs/1812.05433)).
   - Expanded Lenia (ALIFE 2020, Proceedings 32:221-229) adds multiple kernels, multiple channels and higher dimensions. It reports self-replication, emission, growth by ingestion and "virtual eukaryotes" ([arXiv](https://arxiv.org/abs/2005.03742)).
   - Particle Lenia (Mordvintsev, Niklasson, Randazzo, Google, 23 December 2022) is a web article, not a paper ([Google](https://google-research.github.io/self-organising-systems/particle-lenia/)).
   - Sensorimotor agency discovered in Lenia: Hamon et al., Science Advances 11(44) eadp0834 (2025) ([arXiv](https://arxiv.org/abs/2402.10236)).

6. **Flow-Lenia is a 2022 idea that reached a journal in 2025.**
   - First posted to arXiv on 14 December 2022 ([arXiv](https://arxiv.org/abs/2212.07906)).
   - Best Paper Award at ALIFE 2023, held in Sapporo on 24-28 July 2023 ([project page](https://sites.google.com/view/flowlenia/), [ALIFE 2023](https://2023.alife.org/?p=1510)).
   - The extended version has a different title: "Flow-Lenia: Emergent Evolutionary Dynamics in Mass Conservative Continuous Cellular Automata", Artificial Life 31(2):228-248 (2025) ([doi](https://doi.org/10.1162/artl_a_00471)).
   - The authors call it "an important step towards" open-ended evolution, not an achievement of it ([arXiv 2506.08569](https://arxiv.org/html/2506.08569)).

7. **Neural cellular automata (NCA) are now a mainstream ALife substrate.**
   - Growing NCA (Distill, 11 February 2020): one shared update rule of about 8,000 parameters grows a pattern and repairs damage ([Distill](https://distill.pub/2020/growing-ca/)).
   - Biomaker CA (18 July 2023): plant-like ecosystems in JAX, with meta-evolution ([arXiv](https://arxiv.org/abs/2307.09320)).
   - DiffLogic CA (Google, March 2025): learned the Game of Life exactly, as a circuit of 336 active logic gates ([Google](https://google-research.github.io/self-organising-systems/difflogic-ca/)).
   - Sakana's Petri Dish NCA (November 2025) and its 2026 follow-ons, and an NCA paper shared Best Paper at ALIFE 2026 (see the 2026 section).

8. **ASAL** ("Automating the Search for Artificial Life with Foundation Models").
   - **Authors:** Kumar (MIT/Sakana), Lu (OpenAI), Kirsch (IDSIA), Tang and Ha (Sakana), Stanley (independent), Isola (MIT).
   - **Publication:** arXiv 23 December 2024; Artificial Life 31(3):368-396 (2025) ([doi](https://doi.org/10.1162/artl.a.8)).
   - **Method:** CLIP scores rendered simulations in three modes: matching a target, open-endedness, and illumination (finding a diverse set).
   - **Substrates:** Boids, Particle Life, Life-like cellular automata (CAs), Lenia and NCA.
   - **Results:** it found "previously unseen Lenia and Boids lifeforms". It searched all 262,144 Life-like CAs by brute force, and Conway's Life ranked in the top 5% on its open-endedness metric.
   - **Limitations:** NCA were left out of the open-endedness search, and novelty was hard to sustain in Lenia and Boids ([arXiv](https://arxiv.org/html/2412.17799v2)).

9. **BFF ("Computational Life", Agüera y Arcas et al., Google, arXiv 27 June 2024): self-replicators arise from random code.**
   - **Setup:** 2^17 random programs of 64 bytes each. Programs are paired, concatenated, executed and split again. There is no fitness function.
   - **Results:** about 40% of runs "show a state transition within 16k epochs" to self-replicators. It also happens with no background mutation at all. Forth soups transition almost always within 1k epochs. SUBLEQ never produced replicators ([arXiv](https://arxiv.org/html/2406.19108v2)).
   - **Why it matters:** Tierra and Avida both start from a hand-written replicator. Here, replication arises from random interaction and self-modification.
   - **Status:** Google Research still lists it only as an arXiv preprint ([Google Research](https://research.google/pubs/computational-life-how-well-formed-self-replicating-programs-emerge-from-simple-interaction/)).

10. **Open-ended evolution (OEE) is still unsolved by the field's own account.**
    - The MODES toolbox (Dolson, Vostinar, Wiser, Ofria; Artificial Life 25(1):50-73, April 2019) measures change, novelty, complexity and ecology ([doi](https://doi.org/10.1162/artl_a_00280)).
    - Evolutionary activity statistics are still in use, for example in the Flow-Lenia journal paper.
    - ASAL (2025) calls finding open-ended simulations "a grand challenge of ALife", whose necessary conditions "are yet to be realized".
    - The 25-author OEE workshop report from York (2016) concluded with "pluralism about OEE" ([doi](https://doi.org/10.1162/artl_a_00210)).

## Timeline

| Year | System | People / organisation | Significance | Source |
|---|---|---|---|---|
| 1986 | The term in print | Langton (Los Alamos) | "Artificial life" in a paper title | https://doi.org/10.1016/0167-2789(86)90237-x |
| 1987 | ALife I workshop | Langton; CNLS, SFI, Apple | Founding meeting, Los Alamos, September | https://www.routledge.com/Artificial-Life-Proceedings-Of-An-Interdisciplinary-Workshop-On-The-Synthesis-And-Simulation-Of-Living-Systems/Langton/p/book/9780367152772 |
| 1991 | Tierra | Thomas S. Ray (Univ. of Delaware) | Evolved parasites, sociality and cheaters | https://tomray.me/pubs/alife2/Ray1991AnApproachToTheSynthesisOfLife.pdf |
| 1993 | Avida | Adami, Ofria, C. Titus Brown | Parallel virtual CPUs; rewarded logic tasks | https://www.cse.msu.edu/~ofria/pubs/2009AvidaIntro.pdf |
| 1994 | PolyWorld | Larry Yaeger (Apple) | Hebbian neural nets and vision in an ecology | http://shinyverse.org/larryy/Yaeger.ALife3.pdf |
| 2003 | EQU experiment | Lenski, Ofria, Pennock, Adami | A complex feature built from simpler ones | https://www.nature.com/articles/nature01568 |
| 2003 | Soft/hard/wet | Bedau (Reed College) | Standard taxonomy | https://doi.org/10.1016/j.tics.2003.09.012 |
| 2018-19 | Lenia | Bert Wang-Chak Chan | Continuous CA; 400+ species | https://arxiv.org/abs/1812.05433 |
| 2019 | MODES | Dolson et al. (MSU) | Metrics for open-ended dynamics | https://doi.org/10.1162/artl_a_00280 |
| 2020 | Growing NCA | Mordvintsev et al. (Google), Levin (Tufts) | Learned growth and regeneration | https://distill.pub/2020/growing-ca/ |
| 2020 | Expanded Lenia | Chan | Multi-channel, self-replication | https://arxiv.org/abs/2005.03742 |
| 2021 | biosim4 | David R. Miller | Neural-genome evolution sim (repo created 18 Sep 2021) | https://github.com/davidrmiller/biosim4 |
| 2022 | Flow-Lenia | Plantec et al. (Inria FLOWERS, Google) | Mass conservation, local parameters | https://arxiv.org/abs/2212.07906 |
| 2022 | Particle Lenia | Google | Particle and energy formulation | https://google-research.github.io/self-organising-systems/particle-lenia/ |
| 2023 | Biomaker CA | Randazzo, Mordvintsev | JAX ecosystem CA | https://arxiv.org/abs/2307.09320 |
| 2024 | BFF | Agüera y Arcas et al. (Google) | Self-replicators arise spontaneously | https://arxiv.org/abs/2406.19108 |
| 2024 | Wafer-scale ALife | Moreno, Yang, Dolson, Zaman | 1M generations/min | https://arxiv.org/abs/2404.10861 |
| 2024-25 | ASAL | MIT, Sakana, OpenAI, IDSIA | Foundation-model ALife search | https://arxiv.org/abs/2412.17799 |
| 2025 | DiffLogic CA | Miotti, Niklasson, Randazzo, Mordvintsev | Learned logic-circuit CA | https://google-research.github.io/self-organising-systems/difflogic-ca/ |
| 2025 | Evochora | Evochora Project | Open-source (MIT), Java; no fitness function | https://github.com/evochora/evochora |
| 2025 | Petri Dish NCA | Zhang, Risi, Darlow (Sakana) | NCA that keep learning during the run | https://pub.sakana.ai/pdnca/ |
| 2025 | Thrive 1.0 | Revolutionary Games | "the big 1.0 release"; microbe stage done | https://github.com/Revolutionary-Games/Thrive/releases |
| 2026 | Digital Red Queen | Kumar et al. (Sakana, MIT) | LLM-driven Core War coevolution | https://arxiv.org/abs/2601.03335 |

## Key numbers

- **Lenski et al. 2003:** populations of 3,600; each run was 100,000 updates, which the paper equates to 15,873 ancestral generations. Avida 1.6 ran on a Beowulf cluster of 64 Pentium III processors. The first genome able to do EQU had 60 instructions, and removing any of 35 of them destroyed EQU ([Nature PDF](https://www.cs.princeton.edu/courses/archive/fall24/cos597C/bib/598-2017/adami03Nature.pdf)).
- **Ray 1991:**
  - Speed: a 20 MHz 80386 laptop ran over 12 million Tierran instructions an hour.
  - A run of 2.56 billion instructions produced 1,180 size classes, 367 of which reached at least five individuals.
  - Longest runs: 2.86 billion instructions.
  - One run under selection for large size evolved genomes over 23,000 instructions long.
  - The genebank held 29,275 genotypes across 305 size classes.
- **Avida 2009:** 10,000 organisms at 20,000 generations a day on a "modern desktop" of the time.
- **Moreno et al. 2024:** over 1 million generations a minute with up to 16 million agents.
- **Lenia:** more than 400 species in 18 families (2019).
- **Growing NCA:** about 8,000 parameters. **DiffLogic CA:** 336 active gates for the Game of Life.
- **ASAL:** 262,144 Life-like CAs searched; Conway's Life in the top 5%.
- **BFF:** 2^17 × 64-byte programs; about 40% of runs transition within 16k epochs at 0.024% mutation; about 50% in long runs with no mutation.
- **Digital Red Queen** ([web paper](https://pub.sakana.ai/drq)):
  - Runs on GPT-4.1 mini.
  - Each plot point uses 96 independent runs.
  - Generality is measured against 317 human-written warriors held out from training.
  - Keeping the full opponent history (K=10) gives 77% fewer cycles.
  - In single-round tests, the specialist warriors together beat or tie 283 of 294 human warriors.

## 2026 developments (January to October 2026)

- **Digital evolution:** Digital Red Queen (arXiv 6 January 2026). An LLM evolves Core War programs, each round written to beat all earlier ones. Over the rounds they become "increasingly general" and "less behaviorally diverse across independent runs": their behaviour converges, but their code does not ([arXiv](https://arxiv.org/abs/2601.03335)).
- **Neural cellular automata** ([Sakana blog](https://sakana.ai/blog/)):
  - Sakana's "Digital Ecosystems" (19 April 2026): browser-based NCA species that keep learning during the run, with more than 40 tunable parameters ([post](https://sakana.ai/digital-ecosystem/)).
  - "Smart Cellular Bricks" (13 July 2026): only the title and a one-line summary were read; details UNVERIFIED.
- **Open-endedness:** Sakana's "The AI Picbreeder Experiment" (10 July 2026): title only, content UNVERIFIED.
- **ALIFE 2026** ([site](https://2026.alife.org/), [announcement](https://alife.org/2025/08/15/announcement-of-alife-2026-venue-dates-and-organizers/)):
  - Held 17-21 August 2026 in Waterloo, Ontario, at Wilfrid Laurier University and the University of Waterloo, in hybrid format, jointly with the VII AMMCS conference.
  - Theme: "Living and Lifelike Complex Adaptive Systems".
  - Two Best Paper Awards, both also named Best Student Paper:
    - "Endosymbiotic Mutualism Can Constrain Host Diversity and Evolved Complexity" (Kelley et al.).
    - "Architectural Relationship between Neural Cellular Automata and ConvLSTM" (Omija, Takadama, Iba).
  - Papers of Distinction: Ahmed & Davis on polynomial Kolmogorov-Arnold Networks learning Game of Life dynamics; Bohm & Hintze, "The Surprising Evolvability of Unappreciated Cellular Automata".
  - Proceedings are MIT Press, volume 38. They are dedicated "IN MEMORIAM: Inman Harvey, 1948 – 2026". I only saw that dedication in a repost of the proceedings announcement; the MIT Press page returned 403 ([comdig](https://comdig.cssociety.org/2026/09/06/alife-2026-proceedings-of-the-2026-artificial-life-conference/)).
  - ALIFE 2027 goes to Prague, with Čejková as General Chair ([Čejková lab](https://droplets.vscht.cz/news/123990)).
- **Simulators:**
  - Thrive: 1.0.1 (7 March), 1.1.0 (23 May) and 1.6.0 (30 August 2026). Since 1.0, development has moved on to the multicellular stage.
  - The Bibites: version 0.6.3.1, 17 March 2026; also on Steam ([itch.io](https://thebibites.itch.io/the-bibites)).
  - ALIEN (Christian Heinemann): no tagged release since v4.12 (29 December 2024), but the develop branch was pushed on 9 October 2026 ([GitHub](https://github.com/chrxh/alien/releases)).
  - biosim4 is "transitioning to maintenance-only".
- **None found in 2026:** new Lenia or Flow-Lenia results, BFF follow-ups, ASAL follow-ups from other groups, and new OEE measurement work. Search coverage for these was partial.

## Corrections to the old paper

1. **"10,000 organisms … 20,000 generations per day":** this is accurate as a quote, but it is a 2009 single-desktop figure (Ofria et al. 2009). Date it and cite that chapter. Do not mix it up with the 2003 experiments, which used 3,600 organisms and about 15,873 generations per run on a 64-CPU cluster.
2. **"Flow-Lenia (2025)":** first posted December 2022; ALIFE 2023 Best Paper; the 2025 item is the journal version, under a different title.
3. **"400+ species in 18 families":** correct. Attribute it to Chan's 2019 Complex Systems paper (preprint December 2018), not to Expanded Lenia.
4. **Langton "coined the term at the 1987 workshop":** the term was already in print in 1986.
5. **Tierra:**
   - The symbiosis in the paper was engineered by hand.
   - Open-ended size growth happened in one run, under selection for large size.
   - Cite the printed volume information: Artificial Life II, SFI vol. X, Addison-Wesley, 1991, pp. 371-408.
6. **Avida EQU:** 23 of 50 populations, not all of them. Deleterious stepping-stone mutations mattered "in some cases" (3 of 23), not as a rule.
7. **ASAL is not just "Sakana's":** it is a five-institution paper, and its venue is Artificial Life (2025).
8. **BFF:** an arXiv preprint, not peer-reviewed. Replicators arise "with or without" mutation, and SUBLEQ is a counterexample.
9. **"No artificial system has achieved unbounded open-ended evolution":** safer wording is "no artificial system is generally accepted as having demonstrated unbounded OEE". Channon's earlier claim that his Geb system showed unbounded evolutionary activity is UNVERIFIED (his site was unreachable).
10. **ALIFE 2025 was in Kyoto**, 6-10 October 2025, at Kyoto Sangyo-Kaiken Hall, theme "Ciphers of Life" ([site](https://2025.alife.org/), [about](https://2025.alife.org/about)). ISAL's own awards post wrongly says Tokyo ([ISAL](https://alife.org/2025/11/03/2025-isal-awards-winners/)).
    - Best Paper: Johnson, Croft, Vostinar, Lalejini, Dolson, on partner choice in endosymbiotic coevolution.
    - Best Student Paper: Gaylinn, Rees, Cheney, Bongard, "Ramps and Ratchets: Evolving Spatial Viability Landscapes".
    - The Artificial Life Institute in Kyoto launched there.
11. **Particle Lenia** is a Google web article (December 2022), not a peer-reviewed paper.

## Unverified

- **Primordis:** no primary source found; primordis.com is a parked domain. Drop it or source it.
- **Not checked:**
  - Framsticks history (site certificate error).
  - Chromaria (Soros & Stanley, ALIFE 14, 2014; paper URL returned 404).
  - Avida-ED awards. Its role as Avida's teaching interface is confirmed in Ofria et al. 2009.
  - PolyWorld's page numbers in Artificial Life III.
  - The exact days of ALife I.
  - The Bibites' Steam launch date.
  - Dates for particle life. Ventrella's own site confirms "Clusters was the inspiration for Particle Life by Tom Mohr" ([Ventrella](https://www.ventrella.com/Clusters/)).
  - The venue for Hughes et al. (2024), the open-endedness position paper ([arXiv](https://arxiv.org/abs/2406.04268)).
- **Checked, briefly:** Aevol is open source (GPL-3), hosted on Inria's GitLab, and runs "hundreds of thousands of generations" ([aevol.fr](https://www.aevol.fr/)).

**Files:**
- **CORTEX pointers** (in `codex-division-2`, not cloned here, so not read): `/home/minty/CORTEX/matrix/lanes/02-artificial-intelligence/neural-evolution.md`, lines 107, 115, 117 and 143. The file at line 117, `spiking-networks-2025a.pdf`, is actually titled "Neural Cellular Automata and Deep Equilibrium Models", so its filename does not match its topic.