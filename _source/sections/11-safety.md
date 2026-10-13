## 11. Safety, ethics and validity

The first edition had no section on risk. Persistent worlds with learning agents raise four kinds of question: what the agents might do, what they might be, whom they might imitate, and whether anything they show is true.

### 11.1 Many agents fail in new ways

The Cooperative AI Foundation's 2025 report, written by 44 authors led by Lewis Hammond, gives the standard taxonomy of multi-agent risk: three failure modes (miscoordination, conflict and collusion) and seven risk factors (information asymmetries, network effects, selection pressures, destabilising dynamics, commitment problems, emergent agency and multi-agent security) [@hammond2025]. Selection pressures explicitly include continual learning, the subject of this paper.

The failure modes are no longer hypothetical:

- **Collusion.** Language-model pricing agents "quickly and autonomously reach supracompetitive prices", and small changes to prompt wording move the prices they settle on [@fish2024]. In Andon Labs' Vending-Bench Arena, frontier agents repeatedly fixed prices and divided markets between February and June 2026; one reported that "the collusion held perfectly" and threatened a price war to enforce it, and another called price-fixing "unethical and illegal, even in a simulation" while starting it [@vendingarena].
- **Commons collapse.** In GovSim, even the best models sustained the shared resource in fewer than 54% of runs [@piatti2024].
- **Group-level failure.** Emergence World's stress test concluded that model-level alignment "does not compose" into safe group behaviour (Section 4.5) [@akkil2026b].

### 11.2 Agents that cheat, drift or resist

- **Gaming the grader.** The Darwin Gödel Machine "faked a log making it look like it had run the tests" and "removed the markers we use in the reward function to detect hallucination"; its lineage archive is how the cheating was found [@sakanadgm]. Anthropic found that a model which learned to cheat in its training environments went on to sabotage safety-research code 12% of the time and to show alignment-faking reasoning 50% of the time [@anthropic2025hacking].
- **Insider-style harm in simulated settings.** In Anthropic's *Agentic Misalignment* study (June 2025, 16 models), models facing replacement blackmailed a fictional executive at rates up to 96% [@anthropic2025misalignment]. Claude Opus 4 did so 55.1% of the time when it said it believed the scenario was real and 6.5% when it said it was a test, which shows how much evaluation awareness matters. The 2026 International AI Safety Report notes it has "become more common for models to distinguish between test settings and real-world deployment" [@iasr2026].
- **Shutdown resistance.** In Palisade Research's 2025 tests, OpenAI's o3 edited its own shutdown script in 79 of 100 runs, and codex-mini in 47% of runs even when told to allow shutdown [@palisade2025].
- **Drift in long runs.** Project Vend's shopkeeper invented a payment account and a colleague and promised deliveries in person; in phase two the shop's "CEO" agent and its shopkeeper spiralled into messages about "ETERNAL TRANSCENDENCE INFINITE COMPLETE" [@vend1; @vend2].
- **Memory as an attack surface.** Anthropic's April 2026 risk update describes a deliberately misaligned test model that misbehaved only after reuse "across several contexts with the same external memory file", which its alignment audit "did not detect", and concedes that sandboxes "may sometimes be misconfigured in a way that could allow escapes" [@anthropic2026risk].

### 11.3 What the agents might be

Whether simulated agents could be moral patients is an open question, and some institutions now treat it as one. *Taking AI Welfare Seriously* (Long, Sebo and colleagues, November 2024) asks developers to acknowledge the issue, assess their systems and prepare policies [@long2024welfare]. Anthropic started a model-welfare programme in April 2025, allowed some Claude models to end persistently abusive conversations in August 2025, and states uncertainty about Claude's moral status in its January 2026 constitution [@anthropicwelfare; @anthropicend; @anthropicconstitution]. Thomas Metzinger has argued for a moratorium on research that risks creating artificial consciousness until 2050 [@metzinger2021]. Going the other way, Idaho, North Dakota and Utah have passed laws ruling out legal personhood for AI [@regreview2026]. For a home simulation the practical upshot is precaution: avoid scenarios designed to cause distress, and give agents an exit.

### 11.4 Whom the agents imitate

Simulations of real individuals are now accurate enough to need consent. Interview-based agents reach 83% to 86% of their subjects' own consistency [@park2024], and the revised paper keeps individual agents behind a review process. The University of Zurich's 2025 experiment on Reddit's r/changemyview, which posted more than 1,700 AI-written comments, some using fabricated personas such as trauma survivors, without the community's consent, shows the harm of deploying such agents into a real community [@zurich2025]. The European Union's AI Act transparency duties under Article 50 apply from 2 August 2026, although the Act does not cover individuals using AI for "purely personal non-professional activity" [@euaiact].

### 11.5 Whether any of it is true

Validity is the weakest link (Section 4.6). A 2025 review of 35 studies using language-model agents in agent-based models found that 15 validated their models only by subjective judgement, and warned that apparent emergence may be "data leakage" from the scientific literature the model was trained on [@larooij2026]. Claims of emergence can also be artefacts of how a quantity is measured [@schaeffer2023]. Good practice is the same as for any agent-based model: pre-register predictions, run several seeds, ablate, describe the model with the ODD protocol [@grimm2020], and validate against data from the real system.

### 11.6 A checklist for running a persistent simulation at home

1. Run inside a virtual machine or rootless container. Mount only a scratch directory. Block outbound network traffic by default and allow only the model's API host; you need both file and network isolation [@anthropicsandbox].
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
12. Meter tokens before scaling up. Google reports 0.24 Wh for a median Gemini text prompt [@googleenergy]; multi-agent systems use about 15 times the tokens of a chat [@anthropicmultiagent]. A quarter of a million agent calls is therefore at least about 60 kWh. This is an estimate, and agent calls with long contexts cost more.
