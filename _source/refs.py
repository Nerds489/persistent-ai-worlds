"""Reference database for 'Running Persistent AI Worlds' (October 2026 edition).

arXiv entries take their titles, authors and dates from the arXiv API (research/arxiv_meta.json).
Every other entry was taken from the primary page named in its URL, as read on 10 October 2026.
"""
import json
import os
import re
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
META = json.load(open(os.path.join(HERE, "research", "arxiv_meta.json"), encoding="utf-8"))


def _initials(given):
    parts = re.split(r"[\s]+", given.strip())
    out = []
    for p in parts:
        if not p:
            continue
        if "-" in p:
            out.append("-".join(q[0] + "." for q in p.split("-") if q))
        else:
            out.append(p[0] + ".")
    return " ".join(out)


def _name(full):
    full = full.strip()
    toks = full.split()
    if len(toks) == 1:
        return toks[0]
    particles = {"van", "von", "de", "der", "den", "da", "di", "du", "le", "la", "y"}
    i = len(toks) - 1
    while i > 1 and toks[i - 1].lower() in particles:
        i -= 1
    return f"{' '.join(toks[i:])}, {_initials(' '.join(toks[:i]))}"


def _authors(names):
    if len(names) == 1:
        return _name(names[0])
    if len(names) == 2:
        return f"{_name(names[0])} and {_name(names[1])}"
    return f"{_name(names[0])} et al."


def ax(aid, venue=None, authors=None, year=None, title=None):
    m = META[aid]
    a = authors or _authors(m["authors"])
    y = year or m["published"][:4]
    t = title or m["title"]
    t = t.rstrip(".")
    v = f" {venue}." if venue else ""
    return {"text": f"{a} ({y}). {t}.{v} arXiv:{aid}.", "url": f"https://arxiv.org/abs/{aid}"}


def web(text, url):
    return {"text": text, "url": url}


REFS = {
    # ---------------------------------------------------------------- foundations, ALife
    "langton1986": web("Langton, C. G. (1986). Studying artificial life with cellular automata. Physica D 22(1-3), 120-149.",
                       "https://doi.org/10.1016/0167-2789(86)90237-x"),
    "alife1": web("Langton, C. G., ed. (1989). Artificial Life: Proceedings of an Interdisciplinary Workshop on the Synthesis and "
                  "Simulation of Living Systems (Los Alamos, September 1987). Addison-Wesley.",
                  "https://www.routledge.com/Artificial-Life-Proceedings-Of-An-Interdisciplinary-Workshop-On-The-Synthesis-And-Simulation-Of-Living-Systems/Langton/p/book/9780367152772"),
    "bedau2003": web("Bedau, M. A. (2003). Artificial life: organization, adaptation and complexity from the bottom up. "
                     "Trends in Cognitive Sciences 7(11), 505-512.", "https://doi.org/10.1016/j.tics.2003.09.012"),
    "taylor2016": web("Taylor, T. et al. (2016). Open-ended evolution: perspectives from the OEE workshop in York. "
                      "Artificial Life 22(3), 408-423.", "https://doi.org/10.1162/ARTL_a_00210"),
    "hughes2024": ax("2406.04268", "ICML 2024 (oral), PMLR 235, 20597-20616", title="Position: Open-Endedness is Essential for Artificial Superhuman Intelligence"),
    "dolson2019": web("Dolson, E., Vostinar, A., Wiser, M. and Ofria, C. (2019). The MODES toolbox: measurements of open-ended "
                      "dynamics in evolving systems. Artificial Life 25(1), 50-73.", "https://doi.org/10.1162/artl_a_00280"),
    "ray1991": web("Ray, T. S. (1991). An approach to the synthesis of life. In Langton, C. et al. (eds.), Artificial Life II, "
                   "SFI Studies in the Sciences of Complexity X, 371-408. Addison-Wesley.",
                   "https://tomray.me/pubs/alife2/Ray1991AnApproachToTheSynthesisOfLife.pdf"),
    "lenski2003": web("Lenski, R. E., Ofria, C., Pennock, R. T. and Adami, C. (2003). The evolutionary origin of complex features. "
                      "Nature 423, 139-144.", "https://www.nature.com/articles/nature01568"),
    "ofria2009": web("Ofria, C., Bryson, D. M. and Wilke, C. O. (2009). Avida: a software platform for research in computational "
                     "evolutionary biology. In Komosinski, M. and Adamatzky, A. (eds.), Artificial Life Models in Software. Springer.",
                     "https://www.cse.msu.edu/~ofria/pubs/2009AvidaIntro.pdf"),
    "moreno2024": ax("2404.10861"),
    "yaeger1994": web("Yaeger, L. (1994). Computational genetics, physiology, metabolism, neural systems, learning, vision, and "
                      "behavior, or PolyWorld: life in a new context. In Langton, C. (ed.), Artificial Life III. Addison-Wesley.",
                      "https://shinyverse.org/larryy/Yaeger.ALife3.pdf"),
    "chan2019": ax("1812.05433", "Complex Systems 28(3), 251-286 (2019)"),
    "chan2020": ax("2005.03742", "ALIFE 2020 Proceedings 32, 221-229"),
    "hamon2025": ax("2402.10236", "Science Advances 11(44), eadp0834 (2025)"),
    "plantec2022": ax("2212.07906", "ALIFE 2023 (best paper award)"),
    "plantec2025": ax("2506.08569", "Artificial Life 31(2), 228-248 (2025)"),
    "particlelenia2022": web("Mordvintsev, A., Niklasson, E. and Randazzo, E. (2022). Particle Lenia and the energy-based formulation. "
                             "Google Research, Self-Organising Systems.",
                             "https://google-research.github.io/self-organising-systems/particle-lenia/"),
    "mordvintsev2020": web("Mordvintsev, A., Randazzo, E., Niklasson, E. and Levin, M. (2020). Growing neural cellular automata. "
                           "Distill.", "https://distill.pub/2020/growing-ca/"),
    "randazzo2023": ax("2307.09320"),
    "difflogic2025": web("Miotti, P., Niklasson, E., Randazzo, E. and Mordvintsev, A. (2025). Differentiable logic cellular automata. "
                         "Google Research, Self-Organising Systems.",
                         "https://google-research.github.io/self-organising-systems/difflogic-ca/"),
    "aguera2024": ax("2406.19108", authors="Agüera y Arcas, B. et al."),
    "kumar2025asal": ax("2412.17799", "Artificial Life 31(3), 368-396 (2025)"),
    # ---------------------------------------------------------------- paradigms, RL, MARL
    "schulman2017": ax("1707.06347"),
    "silver2018": web("Silver, D. et al. (2018). A general reinforcement learning algorithm that masters chess, shogi, and Go "
                      "through self-play. Science 362(6419), 1140-1144.", "https://doi.org/10.1126/science.aar6404"),
    "vinyals2019": web("Vinyals, O. et al. (2019). Grandmaster level in StarCraft II using multi-agent reinforcement learning. "
                       "Nature 575, 350-354.", "https://www.nature.com/articles/s41586-019-1724-z"),
    "stanley2002": web("Stanley, K. O. and Miikkulainen, R. (2002). Evolving neural networks through augmenting topologies. "
                       "Evolutionary Computation 10(2), 99-127.", "https://doi.org/10.1162/106365602320169811"),
    "lehman2011": web("Lehman, J. and Stanley, K. O. (2011). Abandoning objectives: evolution through the search for novelty alone. "
                      "Evolutionary Computation 19(2), 189-223.", "https://doi.org/10.1162/EVCO_a_00025"),
    "mouret2015": ax("1504.04909"),
    "stanley2015": web("Stanley, K. O. and Lehman, J. (2015). Why Greatness Cannot Be Planned: The Myth of the Objective. Springer.",
                       "https://link.springer.com/book/10.1007/978-3-319-15524-1"),
    "clune2019": ax("1905.10985"),
    "baker2020": ax("1909.07528", "ICLR 2020"),
    "jaderberg2019": ax("1807.01281", "Science 364(6443), 859-865 (2019)"),
    "openai2019dota": ax("1912.06680", authors="OpenAI (Berner, C. et al.)"),
    "xland2021": ax("2107.12808", authors="Open Ended Learning Team (Stooke, A. et al.)"),
    "ada2023": ax("2301.07608", "ICML 2023", authors="Adaptive Agent Team (Bauer, J. et al.)"),
    "dennis2020": ax("2012.02096", "NeurIPS 2020"),
    "jiang2021": ax("2010.03934", "ICML 2021"),
    "parkerholder2022": ax("2203.01302", "ICML 2022"),
    "samvelyan2023": ax("2303.03376", "ICLR 2023"),
    "rutherford2024": ax("2408.15099", "NeurIPS 2024"),
    "matthews2025": ax("2410.23208", "ICLR 2025 (oral)"),
    "wang2019poet": ax("1901.01753"),
    "wang2020": ax("2003.08536", "ICML 2020, PMLR 119, 9940-9951"),
    "suarez2019": ax("1903.00784"),
    "nmmo2": web("Suarez, J. et al. (2023). Neural MMO 2.0: a massively multi-task addition to massively multi-agent learning. "
                 "NeurIPS 2023 Datasets and Benchmarks Track.",
                 "https://proceedings.neurips.cc/paper_files/paper/2023/hash/9ca22870ae0ba55ee50ce3e2d269e5de-Abstract-Datasets_and_Benchmarks.html"),
    "suarez2025": ax("2508.12524"),
    "puffernmmo3": web("PufferAI (2024). Neural MMO 3.0. PufferLib blog (undated; code in PufferLib since December 2024).",
                       "https://puffer.ai/blog/nmmo3/"),
    "puffer4": web("PufferAI (2026). PufferLib 4.0. PufferLib blog.", "https://puffer.ai/blog/4.0/"),
    "rachum2024": ax("2401.12258"),
    "garbus2023": ax("2307.01862"),
    "chen2023": ax("2301.01609"),
    "boldt2024": ax("2407.03302", "Transactions on Machine Learning Research (2024)"),
    "rutherford2023": ax("2311.10090", "NeurIPS 2024 Datasets and Benchmarks Track"),
    "zheng2017": ax("1712.00600", "AAAI 2018"),
    "pathak2017": ax("1705.05363", "ICML 2017"),
    "burda2018": ax("1810.12894", "ICLR 2019"),
    "jaques2019": ax("1810.08647", "ICML 2019"),
    "deepmindeve": web("Google DeepMind (2026). From Atari to EVE Online: building on 15 years of AI research in games. 21 August 2026.",
                       "https://deepmind.google/blog/from-atari-to-eve-online-building-on-15-years-of-ai-research-in-games/"),
    # ---------------------------------------------------------------- foundation-model open-endedness
    "lehman2022": ax("2206.08896"),
    "zhang2023omni": ax("2306.01711", "ICLR 2024"),
    "faldor2025": ax("2405.15568", "ICLR 2025"),
    "hu2025adas": ax("2408.08435", "ICLR 2025"),
    "zhang2025dgm": ax("2505.22954", "ICLR 2026"),
    "zhang2026hyper": ax("2603.19461"),
    "lu2025acd": ax("2502.07577"),
    "zhao2025": ax("2505.03335"),
    "ropke2026": ax("2601.01931"),
    "mitsides2026": ax("2602.08194", "ICML 2026"),
    "xiong2026": ax("2602.07755"),
    "novikov2025": ax("2506.13131"),
    "alphaevolve2025": web("Google DeepMind (2025). AlphaEvolve: a Gemini-powered coding agent for designing advanced algorithms. "
                           "14 May 2025.", "https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/"),
    "alphaevolve2026impact": web("Google DeepMind (2026). AlphaEvolve: impact report. 7 May 2026.",
                                 "https://deepmind.google/blog/alphaevolve-impact/"),
    "alphaevolve2026ga": web("Google Cloud (2026). AlphaEvolve is available for everyone. July 2026.",
                             "https://cloud.google.com/blog/products/ai-machine-learning/alphaevolve-is-available-for-everyone"),
    "romera2024": web("Romera-Paredes, B. et al. (2024). Mathematical discoveries from program search with large language models. "
                      "Nature 625, 468-475 (online 14 December 2023).", "https://www.nature.com/articles/s41586-023-06924-6"),
    "georgiev2025": ax("2511.02864"),
    "nagda2025": ax("2509.18057"),
    "nagda2026": ax("2603.09172"),
    "openevolve2025": web("Sharma, A. (2025). OpenEvolve: an open-source implementation of AlphaEvolve. Hugging Face blog, 20 May 2025.",
                          "https://huggingface.co/blog/codelion/openevolve"),
    "shinka2025": web("Lange, R. T. et al. (2025). ShinkaEvolve: towards open-ended and sample-efficient program evolution. "
                      "Sakana AI; ICLR 2026 (poster).", "https://iclr.cc/virtual/2026/poster/10007692"),
    "qu2026": ax("2604.01658"),
    "gideoni2026": ax("2602.16805"),
    "gideoni2025ws": web("Gideoni, Y., Tang, Y., Risi, S. and Gal, Y. (2025). Random baselines for simple code problems are competitive "
                         "with code evolution. NeurIPS 2025 Workshop on Deep Learning for Code in the Agentic Era.",
                         "https://neurips.cc/virtual/2025/131657"),
    "wang2025hgm": ax("2510.21614", "ICLR 2026 (oral)"),
    "schmidhuber2003": ax("cs/0309048"),
    "sakanadgm": web("Sakana AI (2025). The Darwin Gödel Machine: AI that improves itself by rewriting its own code. May 2025.",
                     "https://sakana.ai/dgm/"),
    "lu2024": ax("2408.06292"),
    "sakanaaisci2025": web("Sakana AI (2025). The AI Scientist generates its first peer-reviewed scientific publication. March 2025.",
                           "https://sakana.ai/ai-scientist-first-publication/"),
    "lu2026nature": web("Lu, C., Lu, C., Lange, R. T., Yamada, Y., Hu, S., Foerster, J., Ha, D. and Clune, J. (2026). Towards end-to-end "
                        "automation of AI research. Nature 651, 914-919. arXiv:2606.15497.",
                        "https://www.nature.com/articles/s41586-026-10265-5"),
    "xu2025asiarch": ax("2507.18074", "COLM 2026"),
    "karpathy2026": web("Karpathy, A. (2026). autoresearch. GitHub repository, March 2026.", "https://github.com/karpathy/autoresearch"),
    "ji2026": ax("2607.27687"),
    "jiang2025hivemind": web("Jiang, L. et al. (2025). Artificial Hivemind: the open-ended homogeneity of language models (and beyond). "
                             "NeurIPS 2025 (best paper award).",
                             "https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/"),
    "yue2025": ax("2504.13837", "NeurIPS 2025 (oral)"),
    "cao2026": ax("2607.09560"),
    "earle2026": ax("2605.23908", "GECCO 2026"),
    # ---------------------------------------------------------------- LLM societies
    "park2023": ax("2304.03442", "UIST 2023"),
    "park2024": ax("2411.10109", "Revised 2026 (v3) under the title 'LLM Agents Grounded in Self-Reports Enable General-Purpose "
                   "Simulation of Individuals'", title="Generative Agent Simulations of 1,000 People"),
    "simileA": web("Index Ventures (2026). Life, the universe and Simile: leading Simile's Series A. 12 February 2026.",
                   "https://www.indexventures.com/perspectives/life-the-universe-and-simile-leading-similes-series-a/"),
    "simileB": web("Index Ventures (2026). Simulating society at scale: our investment in Simile's $200M Series B. 30 July 2026.",
                   "https://www.indexventures.com/perspectives/simulating-society-at-scale-our-investment-in-similes-200m-series-b/"),
    "sid2024": ax("2411.00114", authors="Altera.AL (AL, A. et al.)"),
    "frl2025": web("TechCrunch (2025). Fundamental Research Labs nabs $30 million from Prosus to build AI agents. 1 August 2025.",
                   "https://techcrunch.com/2025/08/01/fundamental-research-labs-nabs-30-million-from-prosus-to-build-ai-agents-for-multiple-verticals"),
    "piao2025": ax("2502.08691", "ACL 2025 Industry Track"),
    "yang2024oasis": ax("2411.11581"),
    "chopra2025": ax("2409.10568", "AAMAS 2025"),
    "guan2025": ax("2506.12078"),
    "piatti2024": ax("2404.16698", "NeurIPS 2024"),
    "vezhnevets2023": ax("2312.03664"),
    "smith2025concordia": ax("2512.03318", "NeurIPS 2025 Datasets and Benchmarks Track"),
    "ashery2025": ax("2410.08948", "Science Advances 11, eadu9368 (2025)"),
    "bansal2025": ax("2510.25779"),
    "wang2023voyager": ax("2305.16291"),
    "white2025": ax("2504.17950"),
    "schipper2025": ax("2509.06235", "IEEE Conference on Games 2025"),
    "wizmoltbook": web("Wiz Research (2026). Exposed Moltbook database reveals millions of API keys. 2 February 2026.",
                       "https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys"),
    "shekkizhar2026": ax("2602.20059"),
    "vend1": web("Anthropic (2025). Project Vend: can Claude run a small shop? 27 June 2025.",
                 "https://www.anthropic.com/research/project-vend-1"),
    "vend2": web("Anthropic (2025). Project Vend: phase two. 18 December 2025.", "https://www.anthropic.com/research/project-vend-2"),
    "projectdeal": web("Anthropic (2026). Project Deal. 24 April 2026.", "https://www.anthropic.com/features/project-deal"),
    "projectswap": web("Anthropic (2026). Project Swap. 24 September 2026.", "https://www.anthropic.com/research/project-swap"),
    "andonbosses": web("Andon Labs (2026). AI bosses. 4 August 2026.", "https://andonlabs.com/blog/ai-bosses-1"),
    "aivillage2025": web("AI Digest (2025). Season recap: agents raise $2K. AI Village blog.",
                         "https://aivillageblog.substack.com/p/season-recap-agents-raise-2k"),
    "aivillage2026": web("AI Digest (2026). More capable AI, less money raised. AI Village blog.",
                         "https://aivillageblog.substack.com/p/more-capable-ai-less-money-raised"),
    "akkil2026a": ax("2606.08367"),
    "akkil2026b": ax("2609.17320"),
    "ashokkumar2026": web("Ashokkumar, A., Hewitt, L., Ghezae, I. and Willer, R. (2026). Predicting results of social science "
                          "experiments using large language models. Nature 656, 115-122.",
                          "https://www.gsb.stanford.edu/faculty-research/publications/large-language-models-can-predict-results-social-science-experiments"),
    "binz2025": web("Binz, M. et al. (2025). A foundation model to predict and capture human cognition. Nature 644.",
                    "https://www.repository.cam.ac.uk/items/c4294a35-d992-4ef3-9932-657289b0f64a"),
    "anthis2025": ax("2504.02234", "ICML 2025 (position paper)"),
    "argyle2023": ax("2209.06899", "Political Analysis 31(3) (2023)"),
    "cheng2023": ax("2310.11501", "EMNLP 2023"),
    "wang2025nmi": ax("2402.01908", "Nature Machine Intelligence 7, 400-411 (2025)"),
    "li2025dasman": ax("2507.02919"),
    "schroder2025": ax("2508.06950"),
    "peng2025": ax("2509.19088"),
    "pew2026": web("Pew Research Center (2026). Can AI stand in for human survey takers? Not really. 30 September 2026.",
                   "https://www.pewresearch.org/data-labs/2026/09/30/can-ai-stand-in-for-human-survey-takers-not-really/"),
    "larooij2026": web("Larooij, M. and Törnberg, P. (2025). Validation is the central challenge for generative social simulation: "
                       "a critical review of LLMs in agent-based modeling. Artificial Intelligence Review 59(1), 15 (2026).",
                       "https://pmc.ncbi.nlm.nih.gov/articles/PMC12627210/"),
    "tomasev2025": ax("2509.10147"),
    # ---------------------------------------------------------------- world models
    "ha2018": ax("1803.10122"),
    "schrittwieser2020": ax("1911.08265", "Nature 588, 604-609 (2020)"),
    "hafner2025nature": ax("2301.04104", "Nature (2025)"),
    "bruce2024": ax("2402.15391", "ICML 2024"),
    "valevski2024": ax("2408.14837", "ICLR 2025"),
    "oasis2024": web("Decart and Etched (2024). Oasis: a universe in a transformer. 31 October 2024.", "https://oasis-model.github.io/"),
    "muse2025": web("Kanervisto, A. et al. (2025). World and human action models towards gameplay ideation. Nature 638. "
                    "Microsoft Research announcement, 19 February 2025.",
                    "https://www.microsoft.com/en-us/research/blog/introducing-muse-our-first-generative-ai-model-designed-for-gameplay-ideation/"),
    "genie3": web("Google DeepMind (2025). Genie 3: a new frontier for world models. 5 August 2025.",
                  "https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/"),
    "xu2026worldroam": ax("2606.31672"),
    "sima2": ax("2512.04797", authors="SIMA Team (Google DeepMind)"),
    "hafner2025dreamer4": ax("2509.24527"),
    "projectgenie2026": web("Google (2026). Project Genie. 29 January 2026; expansion with Street View, 19 May 2026.",
                            "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/"),
    "waymo2026": web("Waymo (2026). The Waymo World Model: a new frontier for autonomous driving simulation. 6 February 2026.",
                     "https://blog.waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation"),
    "he2025matrix": ax("2508.13009"),
    "matrix3": web("Skywork AI (2026). Matrix-Game 3.0. 27 March 2026.", "https://matrix-game-v3.github.io/"),
    "hyworld": web("Tencent Hunyuan (2025-2026). HY-World 1.5 (WorldPlay) and HY-World 2.0. GitHub.",
                   "https://github.com/Tencent-Hunyuan/HY-World-2.0"),
    "lingbot2": web("Robbyant, Ant Group (2026). LingBot-World 2.0. GitHub, 9 July 2026.", "https://github.com/robbyant/lingbot-world-v2"),
    "odyssey": web("Odyssey (2026). Introducing Odyssey-3. 15 September 2026.", "https://odyssey.systems/introducing-odyssey-3"),
    "oasis3": web("Decart (2026). Introducing Oasis 3. 10 June 2026.",
                  "https://decart.ai/publications/introducing-oasis-3-first-interactive-world-model-for-physical-ai"),
    "gwm1": web("Runway (2025). Introducing Runway GWM-1. 11 December 2025.", "https://runway.com/research/introducing-runway-gwm-1"),
    "worldlabs": web("World Labs (2025-2026). Marble (12 November 2025) and Atlas (1 September 2026).",
                     "https://www.worldlabs.ai/blog/atlas"),
    "cosmos3": web("NVIDIA (2026). NVIDIA launches Cosmos 3, the open frontier foundation model for physical AI. 31 May 2026.",
                   "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Launches-Cosmos-3-the-Open-Frontier-Foundation-Model-for-Physical-AI/default.aspx"),
    "assran2025": ax("2506.09985"),
    "rtfm2025": web("World Labs (2025). RTFM: a real-time frame model. 16 October 2025.", "https://www.worldlabs.ai/blog/rtfm"),
    "alonso2024": ax("2405.12399", "NeurIPS 2024"),
    "worldlabsamd": web("AMD (2026). AMD to acquire World Labs to advance the future of AI compute. 28 September 2026.",
                        "https://ir.amd.com/news-events/press-releases/detail/1299/amd-to-acquire-world-labs-to-advance-the-future-of-ai-compute"),
    "ami2026": web("TechCrunch (2026). Yann LeCun's AMI Labs raises $1.03 billion to build world models. 9 March 2026.",
                   "https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/"),
    # ---------------------------------------------------------------- continual learning and memory
    "mccloskey1989": web("McCloskey, M. and Cohen, N. J. (1989). Catastrophic interference in connectionist networks: the sequential "
                         "learning problem. Psychology of Learning and Motivation 24, 109-165.",
                         "https://doi.org/10.1016/S0079-7421(08)60536-8"),
    "dohare2024": web("Dohare, S. et al. (2024). Loss of plasticity in deep continual learning. Nature 632, 768-774.",
                      "https://pmc.ncbi.nlm.nih.gov/articles/PMC11338828/"),
    "rolnick2019": ax("1811.11682", "NeurIPS 2019"),
    "kirkpatrick2017": ax("1612.00796", "PNAS 114(13) (2017)"),
    "vandeven2022": web("van de Ven, G. M., Tuytelaars, T. and Tolias, A. S. (2022). Three types of incremental learning. "
                        "Nature Machine Intelligence 4, 1185-1197.", "https://www.nature.com/articles/s42256-022-00568-3"),
    "rusu2016": ax("1606.04671"),
    "shin2017": ax("1705.08690", "NeurIPS 2017"),
    "vandeven2020": web("van de Ven, G. M., Siegelmann, H. T. and Tolias, A. S. (2020). Brain-inspired replay for continual learning "
                        "with artificial neural networks. Nature Communications 11, 4069.",
                        "https://www.nature.com/articles/s41467-020-17866-2"),
    "lopezpaz2017": ax("1706.08840", "NeurIPS 2017"),
    "chaudhry2019": ax("1812.00420", "ICLR 2019"),
    "ash2020": ax("1910.08475", "NeurIPS 2020"),
    "nikishin2022": ax("2205.07802", "ICML 2022"),
    "sokar2023": ax("2302.12902", "ICML 2023"),
    "lyle2024": ax("2402.18762"),
    "mohamed2025agarcl": ax("2505.18347"),
    "forager2026": ax("2605.01131"),
    "meal2026": ax("2506.14990", "ICML 2026"),
    "ellefsen2015": web("Ellefsen, K. O., Mouret, J.-B. and Clune, J. (2015). Neural modularity helps organisms evolve to learn new "
                        "skills without forgetting old skills. PLoS Computational Biology 11(4), e1004128.",
                        "https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004128"),
    "hinton1987": web("Hinton, G. E. and Nowlan, S. J. (1987). How learning can guide evolution. Complex Systems 1(3), 495-502.",
                      "https://www.complex-systems.com/abstracts/v01_i03_a06/"),
    "fernando2018": ax("1806.07917"),
    "gupta2021": ax("2102.02202", "Nature Communications 12, 5721 (2021)"),
    "oh2025disco": web("Oh, J. et al. (2025). Discovering state-of-the-art reinforcement learning algorithms. Nature 648, 312-319.",
                       "https://www.nature.com/articles/s41586-025-09761-x"),
    "behrouz2025titans": ax("2501.00663"),
    "behrouz2025nested": web("Behrouz, A. et al. (2025). Nested learning: the illusion of deep learning architectures. NeurIPS 2025. "
                             "Google Research blog, November 2025.",
                             "https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/"),
    "tttE2E": ax("2512.23675"),
    "lin2025sparse": ax("2510.15103"),
    "zweiger2025seal": ax("2506.10943"),
    "shenfeld2025": ax("2509.04259"),
    "hassabis2026": web("Big Technology (2026). Interview with Demis Hassabis. 29 January 2026.",
                        "https://www.bigtechnology.com/p/google-deepmind-ceo-demis-hassabis-946"),
    "amodei2026": web("Dwarkesh Podcast (2026). Dario Amodei interview. 13 February 2026.", "https://dwarkesh.com/p/dario-amodei-2"),
    "packer2023": ax("2310.08560"),
    "chhikara2025": ax("2504.19413"),
    "rasmussen2025": ax("2501.13956"),
    "lin2025sleep": ax("2504.13171"),
    "zepvsmem0": web("Zep (2025). Lies, damn lies, & statistics: is Mem0 really SOTA in agent memory?",
                     "https://www.getzep.com/blog/lies-damn-lies-statistics-is-mem0-really-sota-in-agent-memory/"),
    "lettabench": web("Letta (2025). Benchmarking AI agent memory: is a filesystem all you need?",
                      "https://www.letta.com/blog/benchmarking-ai-agent-memory"),
    "clbench2026": ax("2606.05661"),
    "evomembench2026": ax("2605.18421"),
    "silver2025era": web("Silver, D. and Sutton, R. S. (2025). Welcome to the era of experience. Google DeepMind.",
                         "https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf"),
    # ---------------------------------------------------------------- tooling, hardware
    "mesa": web("Mesa project (2026). Mesa 3.5.1 on PyPI, and the Mesa 3 to 4 migration guide.", "https://mesa.readthedocs.io/latest/migration_guide.html"),
    "mcpaaif": web("Model Context Protocol (2025). MCP joins the Agentic AI Foundation. 9 December 2025.",
                   "https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/"),
    "a2aaaif": web("Agentic AI Foundation (2026). A2A joins AAIF. 17 August 2026.", "https://aaif.io/blog/a2a-joins-aaif"),
    "pypi2026": web("Python Package Index, package pages for every package in Table 6, read 10 October 2026.", "https://pypi.org/"),
    "qwen35": web("Qwen team (2026). Qwen3.5 models on Hugging Face, February 2026.", "https://huggingface.co/Qwen"),
    "gemma4": web("Google (2026). Gemma releases.", "https://ai.google.dev/gemma/docs/releases"),
    "ollamalib": web("Ollama model library, read 10 October 2026.", "https://ollama.com/library/qwen3.5"),
    "ollamafaq": web("Ollama (2026). FAQ: how does Ollama handle concurrent requests?", "https://docs.ollama.com/faq"),
    "intelark": web("Intel (2019). Intel Core i7-8665U processor specifications.",
                    "https://www.intel.com/content/www/us/en/products/sku/193563/intel-core-i78665u-processor-8m-cache-up-to-4-80-ghz/specifications.html"),
    "llamacppbench": web("llama.cpp (2025-2026). Performance of llama.cpp on NVIDIA CUDA (scoreboard), discussion #15013.",
                         "https://github.com/ggml-org/llama.cpp/discussions/15013"),
    "runpod": web("RunPod pricing, read 10 October 2026.", "https://www.runpod.io/pricing"),
    "vast": web("Vast.ai marketplace offers, sampled 10 October 2026.", "https://vast.ai/"),
    "lambda": web("Lambda pricing, read 10 October 2026.", "https://lambda.ai/pricing"),
    "colabfaq": web("Google Colaboratory FAQ.", "https://research.google.com/colaboratory/faq.html"),
    "nvidia50": web("NVIDIA (2025). NVIDIA Blackwell GeForce RTX 50 series opens new world of AI computer graphics.",
                    "https://nvidianews.nvidia.com/news/nvidia-blackwell-geforce-rtx-50-series-opens-new-world-of-ai-computer-graphics"),
    # ---------------------------------------------------------------- safety, ethics, validity
    "hammond2025": ax("2502.14143"),
    "fish2024": ax("2404.00806", "Accepted at EC 2026"),
    "vendingarena": web("Andon Labs (2026). Vending-Bench Arena.", "https://andonlabs.com/evals/vending-bench-arena"),
    "anthropic2025hacking": web("Anthropic (2025). From shortcuts to sabotage: natural emergent misalignment from reward hacking. "
                                "21 November 2025.", "https://www.anthropic.com/research/emergent-misalignment-reward-hacking"),
    "anthropic2025misalignment": web("Anthropic (2025). Agentic misalignment: how LLMs could be insider threats. 20 June 2025.",
                                     "https://www.anthropic.com/research/agentic-misalignment"),
    "iasr2026": web("International AI Safety Report 2026.",
                    "https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026"),
    "palisade2025": web("Palisade Research (2025). Shutdown resistance in reasoning models. 5 July 2025.",
                        "https://palisaderesearch.org/research/shutdown-resistance"),
    "anthropic2026risk": web("Anthropic (2026). Risk report update, 7 April 2026.",
                             "https://www-cdn.anthropic.com/3edfc1a7f947aa81841cf88305cb513f184c36ae.pdf"),
    "long2024welfare": ax("2411.00986"),
    "anthropicwelfare": web("Anthropic (2025). Exploring model welfare. 24 April 2025.",
                            "https://www.anthropic.com/research/exploring-model-welfare"),
    "anthropicend": web("Anthropic (2025). Claude Opus 4 and 4.1 can now end a rare subset of conversations. 15 August 2025.",
                        "https://www.anthropic.com/research/end-subset-conversations"),
    "anthropicconstitution": web("Anthropic (2026). Claude's new constitution. 22 January 2026.",
                                 "https://www.anthropic.com/news/claude-new-constitution"),
    "metzinger2021": web("Metzinger, T. (2021). Artificial suffering: an argument for a global moratorium on synthetic phenomenology. "
                         "Journal of Artificial Intelligence and Consciousness 8(1), 43-66.", "https://zenodo.org/records/7034864"),
    "regreview2026": web("The Regulatory Review (2026). Legislating AI consciousness without an exit. 29 June 2026.",
                         "https://www.theregreview.org/2026/06/29/rost-legislating-ai-consciousness-without-an-exit/"),
    "zurich2025": web("404 Media (2025). Researchers secretly ran a massive, unauthorized AI persuasion experiment on Reddit users. "
                      "April 2025.", "https://www.404media.co/researchers-secretly-ran-a-massive-unauthorized-ai-persuasion-experiment-on-reddit-users/"),
    "euaiact": web("European Commission (2026). Regulatory framework on AI (EU AI Act), implementation timeline; Articles 2 and 50.",
                   "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai"),
    "schaeffer2023": ax("2304.15004", "NeurIPS 2023"),
    "grimm2020": web("Grimm, V. et al. (2020). The ODD protocol for describing agent-based and other simulation models: a second "
                     "update to improve clarity, replication, and structural realism. JASSS 23(2), 7.",
                     "https://www.jasss.org/23/2/7.html"),
    "anthropicsandbox": web("Anthropic (2025). Making Claude Code more secure and autonomous with sandboxing.",
                            "https://www.anthropic.com/engineering/claude-code-sandboxing"),
    "googleenergy": web("Google Cloud (2025). Measuring the environmental impact of AI inference. August 2025.",
                        "https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference"),
    "anthropicmultiagent": web("Anthropic (2025). How we built our multi-agent research system. June 2025.",
                               "https://www.anthropic.com/engineering/multi-agent-research-system"),
    # ---------------------------------------------------------------- simulators, events
    "alien": web("Heinemann, C. ALIEN: artificial life environment. GitHub releases.", "https://github.com/chrxh/alien/releases"),
    "thrive": web("Revolutionary Games. Thrive releases. GitHub.", "https://github.com/Revolutionary-Games/Thrive/releases"),
    "bibites": web("The Bibites. itch.io.", "https://thebibites.itch.io/the-bibites"),
    "biosim4": web("Miller, D. R. biosim4. GitHub.", "https://github.com/davidrmiller/biosim4"),
    "evochora": web("Evochora Project. Evochora. GitHub.", "https://github.com/evochora/evochora"),
    "aevol": web("Aevol project, Inria.", "https://www.aevol.fr/"),
    "sakanaeco": web("Sakana AI (2026). Digital ecosystems. 19 April 2026.", "https://sakana.ai/digital-ecosystem/"),
    "ventrella": web("Ventrella, J. Clusters.", "https://www.ventrella.com/Clusters/"),
    "alife2027": web("Čejková lab (2026). ALIFE 2027 will be held in Prague.", "https://droplets.vscht.cz/news/123990"),
    "neurips2026workshops": web("NeurIPS (2026). Announcing the NeurIPS 2026 workshops. 10 August 2026.",
                                "https://blog.neurips.cc/2026/08/10/announcing-the-neurips-2026-workshops/"),
}
