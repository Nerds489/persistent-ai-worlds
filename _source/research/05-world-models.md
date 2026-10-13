# World models and generative interactive environments, 2018 to 10 Oct 2026: findings brief

**Scope and method.** Primary sources only: lab blogs, arXiv, GitHub READMEs, model cards and press releases. Search coverage was partial, so the remaining checks fetched known primary URLs directly. Because of that, these were **not researched**: xAI, Tesla's neural simulator, Wayve GAIA, 1X, OpenAI Sora 2, Decart MirageLSD and Dynamics Lab Mirage. The local lane `/home/minty/CORTEX/matrix/lanes/02-artificial-intelligence/` has only loosely related world-model papers (`ai-general.md` line 190, `machine-learning.md` line 522); the store was not searched in depth.

## Top findings

1. **The two lines of work have joined up.** From 2018 to 2023 the world model sat inside the agent:
   - Ha and Schmidhuber trained an agent "entirely within" its learned model.
   - MuZero planned with a learned model.
   - DreamerV3 learned by imagining outcomes.

   From 2024 the model became the environment itself (Genie, GameNGen, Oasis). In late 2025 and 2026, agents started training inside those generated worlds: SIMA 2 in Genie 3, Dreamer 4 from offline data only, and Odyssey-3's driving policies.
2. **Dreamer is the clearest proof that reinforcement learning (RL) inside a world model works, but success rates are low.** DreamerV3 (Nature, 2025) collected Minecraft diamonds from scratch with no human data. Dreamer 4 is the first to do it purely offline, and it succeeds in only **0.7%** of episodes.
3. **Genie 3 (Aug 2025) is still the general-purpose leader, and no successor exists as of 10 Oct 2026.** It runs at 720p and 24 fps, stays consistent for "a few minutes", and has about one minute of visual memory. It ranked first on the independent WorldRoamBench first-person test. DeepMind's Genie page lists no newer version, and I found no Genie 4.
4. **Public access to Genie is a 60-second demo, not a simulator.** Project Genie (29 Jan 2026) caps each generation at 60 s. It launched without promptable world events, only for US adult Ultra subscribers. On 19 May 2026 it added Street View grounding and began rolling out more widely.
5. **Worlds stay consistent for minutes, not hours.** Every primary-source horizon I verified is a few minutes at most. Claims of "unbounded" sessions (LingBot-World 2.0, Decart Oasis 3) come only from the vendors. WorldRoamBench measured a **37%** average drop in memory scores between its short and long rollouts, even within a 10 to 60 s test.
6. **Physics is the weakest area.**
   - WorldRoamBench: every open-source model scored **below 8** on mechanics, against Genie 3's 61.50.
   - Meta's IntPhys 2: video models score at or near chance, while humans score 85-95% across Meta's three benchmarks.
7. **Open weights come mostly from Chinese labs, plus NVIDIA and Meta.** The main ones are Tencent, Skywork, Ant Group's Robbyant, NVIDIA Cosmos and Meta V-JEPA. The Western interactive leaders are all closed or hosted: Genie 3, Odyssey, Runway GWM-1, Decart Oasis 3 and World Labs Atlas.
8. **World models for robots and cars are now standard tooling.** NVIDIA Cosmos went from launch to Cosmos 3. Waymo built its simulator on Genie 3. Runway and Decart sell environments for policy evaluation and RL through an SDK or API.
9. **Lasting worlds currently come from explicit 3D, not from pixel models.** World Labs' June 2026 classification separates pixel "renderers" (Genie 3, RTFM) from "simulators" that output geometry, such as Marble's Gaussian splats and collision meshes. Pixel models forget anything outside their context window.
10. **2026 was a big funding year.** AMI Labs raised a $1.03B seed round. World Labs raised $1B, and AMD then agreed to buy it for about $8.2B in stock.

## Timeline

| Date | Model | Org | Capability | Open? | Source |
|---|---|---|---|---|---|
| 2018-03-27 | World Models | Ha, Schmidhuber | Agent trained inside the learned model, then transferred | Paper | [arXiv](https://arxiv.org/abs/1803.10122) |
| 2019-11-19 (Nature 588, 2020) | MuZero | DeepMind | Planning with a learned model; state of the art on 57 Atari games; matched AlphaZero without being given the rules | Paper | [arXiv](https://arxiv.org/abs/1911.08265) |
| 2023-01-10 (Nature, 2025) | DreamerV3 | DeepMind | 150+ tasks with one config; first diamond at 30M steps (17 days of play) | Code, MIT | [project](https://danijar.com/project/dreamerv3/) |
| 2024-02-23 | Genie | DeepMind | 11B; 30k hours of 160x90 video; about 1 fps; 16-frame memory | Closed | [arXiv](https://arxiv.org/html/2402.15391) |
| 2024-03-13 | SIMA | DeepMind | 9 games plus 4 research environments; 600 skills | Closed | [blog](https://deepmind.google/discover/blog/sima-generalist-ai-agent-for-3d-virtual-environments/) |
| 2024-05-20 | DIAMOND | Alonso et al. | Atari 100k score 1.46 (human-normalised); CS:GO at 10 fps on an RTX 3090 | MIT | [arXiv](https://arxiv.org/abs/2405.12399), [repo](https://github.com/eloialonso/diamond/tree/csgo) |
| 2024-08-27 | GameNGen | Google | DOOM at 20 fps on one TPU-v5; about 3 s of history | Closed | [arXiv](https://arxiv.org/html/2408.14837) |
| 2024-10-31 | Oasis | Decart, Etched | Minecraft-like world at 20 fps | 500M weights | [site](https://oasis-model.github.io/) |
| 2024-12-04 | Genie 2 | DeepMind | 3D worlds from one image; up to 1 min, most 10-20 s | Closed | [blog](https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/) |
| 2025-01-06 | Cosmos | NVIDIA | 9,000T tokens from 20M hours; Nano, Super and Ultra tiers | Open model licence, commercial use allowed | [blog](https://blogs.nvidia.com/blog/cosmos-world-foundation-models/) |
| 2025-02-19 | Muse / WHAM-1.6B | Microsoft | 300x180; consistent for up to 2 min | Weights, research use only | [MSR](https://www.microsoft.com/en-us/research/blog/introducing-muse-our-first-generative-ai-model-designed-for-gameplay-ideation/), [HF](https://huggingface.co/microsoft/wham) |
| 2025-04-04 | WHAMM | Microsoft | Quake II at 10+ fps, 640x360; 0.9 s context | Hosted demo | [MSR](https://www.microsoft.com/en-us/research/articles/whamm-real-time-world-modelling-of-interactive-environments/) |
| 2025-04-11 | MineWorld | Microsoft | 300M-1.2B; 4-7 fps, tested on A100/H100 | MIT | [repo](https://github.com/microsoft/mineworld) |
| 2025-06-11 | V-JEPA 2 | Meta FAIR | 1.2B; zero-shot robot pick-and-place 65-80% | Code and weights | [blog](https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/) |
| 2025-07-26 | HunyuanWorld 1.0 | Tencent | 360° 3D worlds with mesh export; "lite" version runs on an RTX 4090 | Weights | [repo](https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0) |
| 2025-08-05 | Genie 3 | DeepMind | 720p, 24 fps; consistent for minutes; about 1 min memory; promptable world events | Closed | [blog](https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/) |
| 2025-08-12 | Matrix-Game 2.0 | Skywork | 1.8B; 352x640; 25 fps on one H100 | MIT | [arXiv](https://arxiv.org/html/2508.13009) |
| 2025-08-14 | Hunyuan-GameCraft | Tencent | 704x1216; 24 GB VRAM minimum ("very slow") | Weights | [repo](https://github.com/Tencent-Hunyuan/Hunyuan-GameCraft-1.0) |
| 2025-09-29 | Dreamer 4 | DeepMind | Diamonds from offline data only; about 2B params; real-time on one GPU | No release found | [arXiv](https://arxiv.org/html/2509.24527) |
| 2025-10-16 | RTFM | World Labs | Real-time on one H100; frames stored by camera position as spatial memory | Demo | [blog](https://www.worldlabs.ai/blog/rtfm) |
| 2025-10-27 | Odyssey-2 | Odyssey | 20 fps; under 50 ms per frame | Hosted | [blog](https://odyssey.systems/introducing-odyssey-2) |
| 2025-11-12 | Marble | World Labs | Persistent 3D worlds (splats, meshes); not real-time interactive | Commercial | [blog](https://www.worldlabs.ai/blog/marble-world-model) |
| 2025-11-13 | SIMA 2 | DeepMind | Built on Gemini Flash-Lite; roughly doubles SIMA 1's success rate; self-improves in Genie 3 worlds | Closed preview | [blog](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/), [arXiv](https://arxiv.org/html/2512.04797) |
| 2025-12-11 | GWM-1 | Runway | Worlds, Robotics and Avatars variants; 720p; up to 2 min | Closed | [page](https://runway.com/research/introducing-runway-gwm-1) |
| 2025-12-17 | HY-World 1.5 (WorldPlay) | Tencent | 24 fps; 480p; 8B and 5B models | Weights; licence excludes EU, UK and South Korea | [repo](https://github.com/Tencent-Hunyuan/HY-WorldPlay) |
| 2026-01-23 | Odyssey-2 Pro + API | Odyssey | 720p, 22 fps; runs "for minutes" | API | [blog](https://odyssey.systems/the-gpt-2-moment-for-world-models) |
| 2026-01-28 | LingBot-World | Robbyant (Ant Group) | 16 fps; under 1 s latency; "minute-level" horizon | Apache-2.0 | [arXiv](https://arxiv.org/abs/2601.20540) |
| 2026-01-29 | Project Genie | Google | Genie 3 in a web app; 60 s cap | Subscription | [blog](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/) |
| 2026-02-06 | Waymo World Model | Waymo | Built on Genie 3; camera and lidar output | Internal | [blog](https://blog.waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation) |
| 2026-03-16 | V-JEPA 2.1 | Meta FAIR | Encoders from 80M to 2B | Code, MIT | [repo](https://github.com/facebookresearch/vjepa2) |
| 2026-03-27 | Matrix-Game 3.0 | Skywork | 5B; 720p at up to 40 fps on 8+1 GPUs; "minute-long" memory | Weights | [page](https://matrix-game-v3.github.io/) |
| 2026-04-16 | HY-World 2.0 | Tencent | Editable 3D (meshes, splats) for Unity and Unreal | Released in stages | [repo](https://github.com/Tencent-Hunyuan/HY-World-2.0) |
| 2026-04-21 | Odyssey-2 Max | Odyssey | About 3x Pro's size; 120+ s generations | Private beta | [blog](https://odyssey.systems/introducing-odyssey-2-max) |
| 2026-05-19 | Project Genie + Street View | Google | Worlds grounded in real places; wider global rollout | Subscription | [blog](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie-expands/) |
| 2026-05-31 | Cosmos 3 | NVIDIA | Omnimodal (text, image, video, sound, actions); Super is 64B; up to 720p and 400 frames | OpenMDW-1.1 | [IR](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Launches-Cosmos-3-the-Open-Frontier-Foundation-Model-for-Physical-AI/default.aspx), [HF](https://huggingface.co/nvidia/Cosmos3-Super) |
| 2026-06-10 | Oasis 3 | Decart | 512x768, 22 fps, under 200 ms; 3 synced cameras | API | [blog](https://decart.ai/publications/introducing-oasis-3-first-interactive-world-model-for-physical-ai) |
| 2026-07-09 | LingBot-World 2.0 | Robbyant | Claims an "unbounded" horizon; 14B and 1.3B | CC BY-NC-SA 4.0 | [repo](https://github.com/robbyant/lingbot-world-v2) |
| 2026-09-01 | Atlas | World Labs | Camera-controlled video up to 1 min at 1440p; 3D reconstruction | Early access | [blog](https://www.worldlabs.ai/blog/atlas) |
| 2026-09-15 | Odyssey-3 | Odyssey | Base world model for robots, cars, drones and games | Demo | [blog](https://odyssey.systems/introducing-odyssey-3) |

## Key numbers

- **Memory windows:**
  - Genie: 16 frames.
  - GameNGen: "a little over 3 seconds".
  - WHAMM: 0.9 s.
  - Dreamer 4: a 192-frame context, which is about 9.6 s at 20 fps (my calculation).
  - Genie 3: visual memory of about 1 minute.
  - Matrix-Game 2.0: "no explicit memory mechanisms".
- **Session horizon:** Genie 3 supports "a few minutes of continuous interaction, rather than extended hours" ([DeepMind](https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/)).
- **Independent benchmark** ([WorldRoamBench](https://arxiv.org/html/2606.31672), 12 models, 10-60 s keyboard-controlled runs):
  - First-person ranking: Genie 3 70.32, Lyra 2.0 69.61 (best open model), Happy Oyster 68.53.
  - Third-person ranking: Happy Oyster 70.66 ahead of Genie 3 61.86.
  - Memory falls from 65.41 to 41.28 between short and long runs.
- **Compute per frame** (calculations are mine and labelled):
  - GameNGen: 4 denoising steps give about 20 fps on one TPU-v5; a one-step distilled version reaches about 50 fps.
  - Matrix-Game 2.0: 25 fps on one H100, about 40 ms per frame (calculation).
  - Matrix-Game 3.0: about 0.23 GPU-seconds per 720p frame (calculation).
  - Cosmos 3 Super: about 55 s per 189-frame clip on 8x H200, about 2.3 GPU-seconds per frame (calculation). It is not real-time.
  - Genie 3: compute is not disclosed.
  - [RTFM post](https://www.worldlabs.ai/blog/rtfm): naive 4K at 60 fps needs over 100K tokens per second, and an hour of persistence needs contexts over 100M tokens, which it calls "neither feasible nor economically viable."
- **Agent training results:**
  - Dreamer 4: diamonds 0.7%, iron pickaxe 29%, over 90% of runs reach the stone pickaxe. It used 2,541 hours of data, 100x less than OpenAI's VPT agent.
  - V-JEPA 2-AC: 16 s per planned action, against about 4 minutes for Cosmos, both on one RTX 4090 ([arXiv](https://arxiv.org/html/2506.09985)).
  - Odyssey-3: a driving policy trained only in simulation went about 77% as far between safety-driver interventions as one trained on real footage. This is a vendor claim.
  - World Labs R2S2R (real-to-sim-to-real): robot policies trained with no real-world data, several of which ran for an hour without intervention. No success rates were published ([blog](https://www.worldlabs.ai/blog/real-to-sim-to-real)).
- **Physics:** Meta reports that humans score 85-95% on its physics benchmarks while models are near chance on IntPhys 2 ([Meta](https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/)).

## 2026 developments (Jan to Oct)

- **Google:**
  - Project Genie launched on 29 Jan.
  - The Waymo World Model was announced on 6 Feb.
  - Street View grounding and the global rollout came on 19 May.
  - At I/O, Pichai said "With world models, AI is moving from predicting text to simulating reality" while launching Gemini Omni ([post](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/)).
  - I found no Genie 4 and no public Genie API.
- **Open interactive models:**
  - LingBot-World (Jan) and LingBot-World 2.0 (Jul).
  - Matrix-Game 3.0 (Mar).
  - WorldPlay added a 5B model (6 Jan) and RL post-training code (8 Mar).
  - HY-World 2.0 (16 Apr), then a 2.1 update in July with no details given.
- **Closed and hosted models:** Odyssey-2 Pro and its API (23 Jan), Odyssey-2 Max (21 Apr), Odyssey-3 (15 Sep), Decart Oasis 3 (10 Jun) and Alibaba Happy Oyster (16 Apr, unverified).
- **Physical AI and robotics:**
  - Cosmos Reason 2 at CES (6 Jan, [forum](https://forums.developer.nvidia.com/t/nvidia-cosmos-announcements-at-ces-2026/356629)).
  - Cosmos Predict 2.5 robot policy models (23 Feb).
  - Cosmos 3 plus a "Cosmos Coalition" that includes Runway and Skild AI (1 Jun).
  - Meta V-JEPA 2.1 (16 Mar).
  - World Labs: World API (21 Jan), SceniX acquisition (21 Jul), R2S2R (28 Jul) and Atlas (1 Sep).
- **Funding and deals:**
  - AMI Labs raised $1.03B at a $3.5B pre-money valuation; it has released no model and plans no revenue for now ([TechCrunch](https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/)).
  - World Labs raised $1B on 18 Feb ([blog](https://www.worldlabs.ai/blog/funding-2026)).
  - AMD agreed to buy World Labs for $8.2B in stock on 28 Sep, closing expected by the end of 2026 ([AMD IR](https://ir.amd.com/news-events/press-releases/detail/1299/amd-to-acquire-world-labs-to-advance-the-future-of-ai-compute)).
- **Evaluation:**
  - WorldRoamBench (30 Jun, revised to v5 on 18 Sep).
  - A survey paper names compounding prediction errors, sim-to-real transfer and fragmented evaluation as the persistent challenges ([arXiv](https://arxiv.org/abs/2606.00133)).
- **Agent training inside world models:** I found no new peer-reviewed result on the scale of Dreamer 4 in 2026. The only new results are vendor reports (Odyssey-3, World Labs, Decart's PPO-via-API). Search coverage was partial, so this absence is not confirmed.

## Practical verdict

- **On a laptop:** only hosted services are usable.
  - Project Genie, on Google AI Ultra ("$200" per [Google](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie-expands/)), with 60 s generations.
  - Odyssey's API.
  - World Labs' Marble and World API, paid with credits.
  - Decart's Oasis 3 API.
  - Runway's GWM-1, which is early access through a request form.
- **Verified to run on a single consumer GPU:**
  - DIAMOND's CS:GO model: 10 fps on an RTX 3090, MIT licence.
  - V-JEPA 2-AC planning on an RTX 4090.
  - WHAM-1.6B: about 4.5 GB VRAM at batch size 1 on an A6000, but only about 1 frame per second and research use only.
  - HunyuanWorld-1.0-lite on an RTX 4090, for static 3D scenes only.
  - Hunyuan-GameCraft at 24 GB, which its README calls "very slow".
  - DreamerV3: open MIT code, though its README gives no hardware minimum.
- **Not verified on consumer hardware:** Oasis-500M, MineWorld (tested on A100/H100), Matrix-Game 2.0 (25 fps measured on an H100), WorldPlay-5B (described only as fitting "small-VRAM" GPUs, with lower quality) and an unofficial 4-bit LingBot build.
- **Needs datacentre GPUs:** WorldPlay-8B (72 GB on one GPU), Matrix-Game 3.0 (9 GPUs), LingBot-World 2.0 (its examples use 4 to 8 GPUs) and Cosmos 3 Super.
- **Licence traps:**
  - WorldPlay's licence does not apply in the EU, UK or South Korea, and above 1M monthly active users you must ask Tencent for a licence ([licence](https://raw.githubusercontent.com/Tencent-Hunyuan/HY-WorldPlay/main/License.txt)).
  - LingBot-World 2.0 is non-commercial only.
  - WHAM is research use only.
  - Cosmos 3's OpenMDW-1.1 licence allows commercial use.
- **Assessment (my inference, not a sourced fact):** no world model available in Oct 2026 can be the authoritative record for a long-running persistent simulation. A better design keeps state in an explicit store or engine, and uses world models for rendering, asset export (Marble, HY-World 2.0) or short-range imagination in the Dreamer style.

## UNVERIFIED

- Genie 2 at 360p (Wikipedia only).
- Oasis at 360p on H100s (secondary sources).
- Dreamer 4 at 21 fps (ArXivIQ summary).
- Runway GWM-1 at 24 fps (DeepLearning.AI).
- LingBot "nearly 10 minutes" and "hour-long" (press releases; its paper says "minute-level").
- All Happy Oyster details.
- Odyssey's $310M Series B amount and the Agora-1 date.
- Cosmos 3 Nano's size (sources conflict between 8B and 16B).
- SIMA 2's "31% to 65%".
- A third-party claim that Genie has a public API.
- A claim that V-JEPA 2.1 came from AMI Labs; Meta's own repo contradicts it.
- DreamerV3's exact Nature date (press coverage says early April 2025).

**Other sources:** [Genie model page](https://deepmind.google/models/genie/), [World Labs taxonomy](https://www.worldlabs.ai/blog/taxonomy-of-world-models), [World API](https://www.worldlabs.ai/blog/announcing-the-world-api), [Cosmos Predict 2.5 repo](https://github.com/nvidia-cosmos/cosmos-predict2.5), [LingBot-World repo](https://github.com/robbyant/lingbot-world), [Matrix-Game repo](https://github.com/SkyworkAI/Matrix-Game), [Open-Oasis repo](https://github.com/etched-ai/open-oasis), [DreamerV3 repo](https://github.com/danijar/dreamerv3), [Dreamer 4 project](https://danijar.com/project/dreamer4/), [V-JEPA 2 arXiv](https://arxiv.org/abs/2506.09985), [NVIDIA Cosmos press release](https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-world-foundation-model-platform-to-accelerate-physical-ai-development).