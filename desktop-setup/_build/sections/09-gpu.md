## 9. Using the RTX 3070

River world never touches the GPU, so the card is free for the two GPU steps of the research paper's eight-week path: fast JAX environments, and a local language model. Give each its own virtual environment.

### 9.1 JAX on the GPU

The JAX build has to match the driver that Section 3.3 reported. `jax[cuda13]` needs driver 580 or newer, and `jax[cuda12]` needs 525 or newer; the RTX 3070 (Ampere) is supported by both.

```bash
python3 -m venv ~/venvs/jax && source ~/venvs/jax/bin/activate && pip install -U pip
pip install -U "jax[cuda13]"        # driver 580 or newer; otherwise: pip install -U "jax[cuda12]"
python3 -c "import jax; print(jax.devices())"          # should list a CUDA device, not only the CPU
pip install jaxmarl craftax
```

JaxMARL [@rutherford2023] and Craftax [@matthews2024craftax] run whole populations of environments on the GPU at once; follow each project's README for a first training run. With 8 GB of memory, start with their default batch sizes and halve them if JAX reports that it is out of memory.

### 9.2 A local language model

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen3.5:4b                 # 3.3 GB; qwen3.5:2b is 2.7 GB
ollama run qwen3.5:4b "In one sentence, what is a ford?"
```

Qwen3.5's 4B model fits in the 3070's 8 GB with room for a working context; the 9B model (6.6 GB) fits too, but leaves little room [@qwen35; @ollamalib]. Watch `nvidia-smi` while it answers.

### 9.3 Why language models cannot run river world's agents

A river world of 800 agents takes 800 decisions a tick and 320,000 a simulated year. Even at ten model calls a second, one simulated year would take about nine hours, and a 1,000-year run about a year. The Q-learners decide in microseconds. Language-model agents belong in a different design: a handful of them, observing the river world or advising one bank, while the population underneath stays cheap. That is step 7 of the research paper's eight-week path, and its Section 11 checklist applies the moment a language model is in the loop: log every prompt, and keep the model's access to the world read-only until you know what it does.
