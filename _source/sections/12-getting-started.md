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
