# 100 Days of LLM Inference

A structured deep‑dive schedule that starts with building an LLM from scratch (days 1‑60) and then extends into inference engineering topics (days 61‑100), based on *[Build a Large Language Model (From Scratch)(https://www.amazon.com/Build-Large-Language-Model-Scratch/dp/0999348450)* and *[Inference Engineering](https://www.baseten.co/library/inference-engineering/)* by Philip Kiely (Baseten Books, 2026).

---

## The Plan

### Original LLM Building Plan (Days 1‑60)

| Day | Topic | Book |
|-----|-------|------|
| 01 | Preface – Overview of the book's goals and author background | <a href="days/day01" target="_blank">Preface</a> |
| 02 | About the Author – Understand the author's perspective and experience | <a href="days/day02" target="_blank">Preface</a> |
| 03 | Understanding Large Language Models – What is an LLM? | <a href="days/day03" target="_blank">Ch 1.1</a> |
| 04 | Understanding Large Language Models – Applications of LLMs | <a href="days/day04" target="_blank">Ch 1.2</a> |
| 05 | Understanding Large Language Models – Stages of building and using LLMs | <a href="days/day05" target="_blank">Ch 1.3</a> |
| 06 | Understanding Large Language Models – Introducing the transformer architecture | <a href="days/day06" target="_blank">Ch 1.4</a> |
| 07 | Understanding Large Language Models – Utilizing large datasets | <a href="days/day07" target="_blank">Ch 1.5</a> |
| 08 | Understanding Large Language Models – A closer look at the GPT architecture | <a href="days/day08" target="_blank">Ch 1.6</a> |
| 09 | Understanding Large Language Models – Building a large language model | <a href="days/day09" target="_blank">Ch 1.7</a> |
| 10 | Working with Text Data – Understanding word embeddings | <a href="days/day10" target="_blank">Ch 2.1</a> |
| 11 | Working with Text Data – Tokenizing text | <a href="days/day11" target="_blank">Ch 2.2</a> |
| 12 | Working with Text Data – Converting tokens into token IDs | <a href="days/day12" target="_blank">Ch 2.3</a> |
| 13 | Working with Text Data – Adding special context tokens | <a href="days/day13" target="_blank">Ch 2.4</a> |
| 14 | Working with Text Data – Byte‑pair encoding | <a href="days/day14" target="_blank">Ch 2.5</a> |
| 15 | Working with Text Data – Data sampling with a sliding window | <a href="days/day15" target="_blank">Ch 2.6</a> |
| 16 | Working with Text Data – Creating token embeddings | <a href="days/day16" target="_blank">Ch 2.7</a> |
| 17 | Working with Text Data – Encoding word positions | <a href="days/day17" target="_blank">Ch 2.8</a> |
| 18 | Coding Attention Mechanisms – The problem with modeling long sequences | <a href="days/day18" target="_blank">Ch 3.1</a> |
| 19 | Coding Attention Mechanisms – Capturing data dependencies with attention | <a href="days/day19" target="_blank">Ch 3.2</a> |
| 20 | Coding Attention Mechanisms – Self‑attention mechanics | <a href="days/day20" target="_blank">Ch 3.3</a> |
| 21 | Coding Attention Mechanisms – Implementing self‑attention with trainable weights | <a href="days/day21" target="_blank">Ch 3.4</a> |
| 22 | Coding Attention Mechanisms – Hiding future words with causal attention | <a href="days/day22" target="_blank">Ch 3.5</a> |
| 23 | Coding Attention Mechanisms – Masking additional attention weights with dropout | <a href="days/day23" target="_blank">Ch 3.5</a> |
| 24 | Coding Attention Mechanisms – Extending to multi‑head attention | <a href="days/day24" target="_blank">Ch 3.6</a> |
| 25 | Implementing a GPT Model – Coding an LLM architecture | <a href="days/day25" target="_blank">Ch 4.1</a> |
| 26 | Implementing a GPT Model – Layer normalization | <a href="days/day26" target="_blank">Ch 4.2</a> |
| 27 | Implementing a GPT Model – Feed‑forward network with GELU | <a href="days/day27" target="_blank">Ch 4.3</a> |
| 28 | Implementing a GPT Model – Adding shortcut connections | <a href="days/day28" target="_blank">Ch 4.4</a> |
| 29 | Implementing a GPT Model – Connecting attention and linear layers in a transformer block | <a href="days/day29" target="_blank">Ch 4.5</a> |
| 30 | Implementing a GPT Model – Coding the GPT model | <a href="days/day30" target="_blank">Ch 4.6</a> |
| 31 | Implementing a GPT Model – Generating text | <a href="days/day31" target="_blank">Ch 4.7</a> |
| 32 | Pretraining on Unlabeled Data – Evaluating generative text models | <a href="days/day32" target="_blank">Ch 5.1</a> |
| 33 | Pretraining – Calculating text generation loss | <a href="days/day33" target="_blank">Ch 5.1</a> |
| 34 | Pretraining – Building training and validation sets | <a href="days/day34" target="_blank">Ch 5.1</a> |
| 35 | Pretraining – Training an LLM | <a href="days/day35" target="_blank">Ch 5.2</a> |
| 36 | Pretraining – Decoding strategies to control randomness | <a href="days/day36" target="_blank">Ch 5.3</a> |
| 37 | Pretraining – Loading and saving model weights in PyTorch | <a href="days/day37" target="_blank">Ch 5.4</a> |
| 38 | Pretraining – Loading pretrained weights from OpenAI | <a href="days/day38" target="_blank">Ch 5.5</a> |
| 39 | Fine‑tuning for Classification – Different categories of fine‑tuning | <a href="days/day39" target="_blank">Ch 6.1</a> |
| 40 | Fine‑tuning – Preparing the dataset | <a href="days/day40" target="_blank">Ch 6.2</a> |
| 41 | Fine‑tuning – Creating data loaders | <a href="days/day41" target="_blank">Ch 6.3</a> |
| 42 | Fine‑tuning – Initializing a model with pretrained weights | <a href="days/day42" target="_blank">Ch 6.4</a> |
| 43 | Fine‑tuning – Adding a classification head | <a href="days/day43" target="_blank">Ch 6.5</a> |
| 44 | Fine‑tuning – Calculating classification loss and accuracy | <a href="days/day44" target="_blank">Ch 6.6</a> |
| 45 | Fine‑tuning – Fine‑tuning on supervised data | <a href="days/day45" target="_blank">Ch 6.7</a> |
| 46 | Fine‑tuning – Using the LLM as a spam classifier | <a href="days/day46" target="_blank">Ch 6.8</a> |
| 47 | Fine‑tuning to Follow Instructions – Introduction to instruction fine‑tuning | <a href="days/day47" target="_blank">Ch 7.1</a> |
| 48 | Instruction fine‑tuning – Preparing dataset for supervised instruction | <a href="days/day48" target="_blank">Ch 7.2</a> |
| 49 | Instruction fine‑tuning – Organizing data into training batches | <a href="days/day49" target="_blank">Ch 7.3</a> |
| 50 | Instruction fine‑tuning – Creating data loaders for instruction dataset | <a href="days/day50" target="_blank">Ch 7.4</a> |
| 51 | Instruction fine‑tuning – Loading a pretrained LLM | <a href="days/day51" target="_blank">Ch 7.5</a> |
| 52 | Instruction fine‑tuning – Fine‑tuning on instruction data | <a href="days/day52" target="_blank">Ch 7.6</a> |
| 53 | Instruction fine‑tuning – Extracting and saving responses | <a href="days/day53" target="_blank">Ch 7.7</a> |
| 54 | Instruction fine‑tuning – Evaluating the fine‑tuned LLM | <a href="days/day54" target="_blank">Ch 7.8</a> |
| 55 | Instruction fine‑tuning – Conclusions | <a href="days/day55" target="_blank">Ch 7.9</a> |
| 56 | What's Next? – Staying up‑to‑date in a fast‑moving field | <a href="days/day56" target="_blank">Ch 7.9</a> |
| 57 | Appendix A – Introduction to PyTorch | <a href="days/day57" target="_blank">Appendix A</a> |
| 58 | Appendix B – References and further reading | <a href="days/day58" target="_blank">Appendix B</a> |
| 59 | Appendix C – Exercise solutions | <a href="days/day59" target="_blank">Appendix C</a> |
| 60 | Appendix D – Adding bells and whistles to the training loop | <a href="days/day60" target="_blank">Appendix D</a> |

---

### Phase 1 — Runtime: Single‑Instance Optimization (Days 61‑78)

| Day | Topic | Book |
|-----|-------|------|
| 61 | LLM Inference Mechanics: End‑to‑end text generation | <a href="days/day61" target="_blank">Ch 2.2</a> |
| 62 | Inference from Scratch: Model internals & tokenization | <a href="days/day62" target="_blank">Ch 2.2</a> |
| 63 | Embeddings: From integers to vectors | <a href="days/day63" target="_blank">Ch 2.2.1</a> |
| 64 | Transformer Blocks & Attention Deep Dive | <a href="days/day64" target="_blank">Ch 2.2.2–2.2.3</a> |
| 65 | Ops: Byte Ratio & Arithmetic Intensity | <a href="days/day65" target="_blank">Ch 2.4</a> |
| 66 | Mixture of Experts (MoE) Routing | <a href="days/day66" target="_blank">Ch 2.2.4</a> |
| 67 | CUDA Kernels, Kernel Selection & Kernel Fusion | <a href="days/day67" target="_blank">Ch 4.1</a> |
| 68 | PyTorch, Model File Formats, ONNX & TensorRT | <a href="days/day68" target="_blank">Ch 4.2</a> |
| 69 | vLLM: PagedAttention & Continuous Batching | <a href="days/day69" target="_blank">Ch 4.3.1</a> |
| 70 | SGLang: RadixAttention & Structured Outputs | <a href="days/day70" target="_blank">Ch 4.3.2</a> |
| 71 | TensorRT‑LLM: Compilation & Plugin System | <a href="days/day71" target="_blank">Ch 4.3.3</a> |
| 72 | NVIDIA Dynamo: Disaggregated Serving | <a href="days/day72" target="_blank">Ch 4.4</a> |
| 73 | Quantization: Number Formats (FP8, INT8, INT4) | <a href="days/day73" target="_blank">Ch 5.1.1</a> |
| 74 | Quantization: GPTQ, AWQ, SmoothQuant | <a href="days/day74" target="_blank">Ch 5.1.2</a> |
| 75 | Speculative Decoding: Draft‑Target, Medusa, EAGLE | <a href="days/day75" target="_blank">Ch 5.2</a> |
| 76 | KV Cache: Prefix Caching & Cache‑Aware Routing | <a href="days/day76" target="_blank">Ch 5.3</a> |
| 77 | Model Parallelism: Tensor & Expert | <a href="days/day77" target="_blank">Ch 5.4</a> |
| 78 | Disaggregation: Prefill/Decode Split | <a href="days/day78" target="_blank">Ch 5.5</a> |

---

### Phase 2 — Infrastructure: Scaling Across Clusters (Days 79‑86)

| Day | Topic | Book |
|-----|-------|------|
| 79 | GPU Architecture: SMs, Memory Hierarchy, HBM | <a href="days/day79" target="_blank">Ch 3.1</a> |
| 80 | GPU Generations: Hopper, Ada, Blackwell, Rubin | <a href="days/day80" target="_blank">Ch 3.2</a> |
| 81 | Multi‑GPU Instances & Multi‑Instance GPU (MIG) | <a href="days/day81" target="_blank">Ch 3.3</a> |
| 82 | Containerization: Docker & NVIDIA NIMs | <a href="days/day82" target="_blank">Ch 7.1</a> |
| 83 | Autoscaling: Concurrency, Batching & Cold Starts | <a href="days/day83" target="_blank">Ch 7.2</a> |
| 84 | Routing, Load Balancing & Queueing | <a href="days/day84" target="_blank">Ch 7.2.3</a> |
| 85 | Multi‑Cloud Capacity Management | <a href="days/day85" target="_blank">Ch 7.3</a> |
| 86 | Zero‑Downtime Deployment & Cost Estimation | <a href="days/day86" target="_blank">Ch 7.4</a> |

---

### Phase 3 — Tooling: Productivity & Observability (Days 87‑89)

| Day | Topic | Book |
|-----|-------|------|
| 87 | Performance Benchmarking: Tooling & Profiling | <a href="days/day87" target="_blank">Ch 4.5</a> |
| 88 | Observability: Metrics, Tracing & Dashboards | <a href="days/day88" target="_blank">Ch 7.4.3</a> |
| 89 | Client Code: Streaming, Async & Protocol Support | <a href="days/day89" target="_blank">Ch 7.5</a> |

---

### Phase 4 — Deep Implementation (Days 90‑100)

| Day | Project |
|-----|---------|
| 90 | Implement a BPE tokenizer from scratch |
| 91 | Build a bare autoregressive decoder loop in PyTorch |
| 92 | Implement scaled dot‑product attention (SDPA) with masking |
| 93 | Implement Flash Attention (simplified, tiling in Python) |
| 94 | Profile attention memory growth across sequence lengths |
| 95 | Build an INT8 quantization pipeline: quantize → dequantize → measure error |
| 96 | Implement GPTQ‑style round‑to‑nearest with Hessian weighting |
| 97 | Sweep quantization bit widths and plot perplexity vs compression |
| 98 | Simulate draft‑target speculative decoding with acceptance sampling |
| 99 | Build a simple KV cache manager (block allocator, eviction policy) |
| 100 | Implement prefix caching with hash‑based deduplication |
---
## Setup

**Install dependencies with uv:**
```bash
uv sync
```

**CLI commands:** See [progress.md](progress.md) for detailed CLI usage.

**Start Jupyter:**
```bash
uv run jupyter notebook
```

---

## Progress

| Phase | Status |
|-------|--------|
| LLM Building Plan (Days 1‑60) | 0 / 60 |
| Runtime Layer (Days 61‑78) | 0 / 18 |
| Infrastructure Layer (Days 79‑86) | 0 / 8 |
| Tooling Layer (Days 87‑89) | 0 / 3 |
| Deep Implementation (Days 90‑100) | 0 / 11 |
| **Total** | **0 / 100** |

---

## Reference

- **Book:** *Build a Large Language Model (From Scratch)* — Sebastian Raschka (Manning Publications, 2025) — ISBN: 978-1633437166
- **Book:** *Inference Engineering* — Philip Kiely (Baseten Books, 2026) — [Online](https://www.baseten.co/library/inference-engineering/)
- **Cluster:** spark-01 `192.168.1.76` · spark-02 `192.168.1.77`

