# 100 Days of LLM Inference

A structured deep‑dive schedule that starts with building an LLM from scratch (days 1‑60) and then extends into inference engineering topics (days 61‑100), based on *[Build a Large Language Model (From Scratch)]* and *[Inference Engineering](https://www.baseten.co/library/inference-engineering/)* by Philip Kiely (Baseten Books, 2026).

---

## The Plan

### Original LLM Building Plan (Days 1‑60)

| Day | Topic | Book |
|-----|-------|------|
| 01 | Preface – Overview of the book’s goals and author background | Preface |
| 02 | About the Author – Understand the author’s perspective and experience | Preface |
| 03 | Understanding Large Language Models – What is an LLM? | <a href="days/day03" target="_blank">Ch 1.1</a> |
| 04 | Understanding Large Language Models – Applications of LLMs | Ch 1.2 |
| 05 | Understanding Large Language Models – Stages of building and using LLMs | Ch 1.3 |
| 06 | Understanding Large Language Models – Introducing the transformer architecture | Ch 1.4 |
| 07 | Understanding Large Language Models – Utilizing large datasets | Ch 1.5 |
| 08 | Understanding Large Language Models – A closer look at the GPT architecture | Ch 1.6 |
| 09 | Understanding Large Language Models – Building a large language model | Ch 1.7 |
| 10 | Working with Text Data – Understanding word embeddings | Ch 2.1 |
| 11 | Working with Text Data – Tokenizing text | Ch 2.2 |
| 12 | Working with Text Data – Converting tokens into token IDs | Ch 2.3 |
| 13 | Working with Text Data – Adding special context tokens | Ch 2.4 |
| 14 | Working with Text Data – Byte‑pair encoding | Ch 2.5 |
| 15 | Working with Text Data – Data sampling with a sliding window | Ch 2.6 |
| 16 | Working with Text Data – Creating token embeddings | Ch 2.7 |
| 17 | Working with Text Data – Encoding word positions | Ch 2.8 |
| 18 | Coding Attention Mechanisms – The problem with modeling long sequences | Ch 3.1 |
| 19 | Coding Attention Mechanisms – Capturing data dependencies with attention | Ch 3.2 |
| 20 | Coding Attention Mechanisms – Self‑attention mechanics | Ch 3.3 |
| 21 | Coding Attention Mechanisms – Implementing self‑attention with trainable weights | Ch 3.4 |
| 22 | Coding Attention Mechanisms – Hiding future words with causal attention | Ch 3.5 |
| 23 | Coding Attention Mechanisms – Masking additional attention weights with dropout | Ch 3.5 |
| 24 | Coding Attention Mechanisms – Extending to multi‑head attention | Ch 3.6 |
| 25 | Implementing a GPT Model – Coding an LLM architecture | Ch 4.1 |
| 26 | Implementing a GPT Model – Layer normalization | Ch 4.2 |
| 27 | Implementing a GPT Model – Feed‑forward network with GELU | Ch 4.3 |
| 28 | Implementing a GPT Model – Adding shortcut connections | Ch 4.4 |
| 29 | Implementing a GPT Model – Connecting attention and linear layers in a transformer block | Ch 4.5 |
| 30 | Implementing a GPT Model – Coding the GPT model | Ch 4.6 |
| 31 | Implementing a GPT Model – Generating text | Ch 4.7 |
| 32 | Pretraining on Unlabeled Data – Evaluating generative text models | Ch 5.1 |
| 33 | Pretraining – Calculating text generation loss | Ch 5.1 |
| 34 | Pretraining – Building training and validation sets | Ch 5.1 |
| 35 | Pretraining – Training an LLM | Ch 5.2 |
| 36 | Pretraining – Decoding strategies to control randomness | Ch 5.3 |
| 37 | Pretraining – Loading and saving model weights in PyTorch | Ch 5.4 |
| 38 | Pretraining – Loading pretrained weights from OpenAI | Ch 5.5 |
| 39 | Fine‑tuning for Classification – Different categories of fine‑tuning | Ch 6.1 |
| 40 | Fine‑tuning – Preparing the dataset | Ch 6.2 |
| 41 | Fine‑tuning – Creating data loaders | Ch 6.3 |
| 42 | Fine‑tuning – Initializing a model with pretrained weights | Ch 6.4 |
| 43 | Fine‑tuning – Adding a classification head | Ch 6.5 |
| 44 | Fine‑tuning – Calculating classification loss and accuracy | Ch 6.6 |
| 45 | Fine‑tuning – Fine‑tuning on supervised data | Ch 6.7 |
| 46 | Fine‑tuning – Using the LLM as a spam classifier | Ch 6.8 |
| 47 | Fine‑tuning to Follow Instructions – Introduction to instruction fine‑tuning | Ch 7.1 |
| 48 | Instruction fine‑tuning – Preparing dataset for supervised instruction | Ch 7.2 |
| 49 | Instruction fine‑tuning – Organizing data into training batches | Ch 7.3 |
| 50 | Instruction fine‑tuning – Creating data loaders for instruction dataset | Ch 7.4 |
| 51 | Instruction fine‑tuning – Loading a pretrained LLM | Ch 7.5 |
| 52 | Instruction fine‑tuning – Fine‑tuning on instruction data | Ch 7.6 |
| 53 | Instruction fine‑tuning – Extracting and saving responses | Ch 7.7 |
| 54 | Instruction fine‑tuning – Evaluating the fine‑tuned LLM | Ch 7.8 |
| 55 | Instruction fine‑tuning – Conclusions | Ch 7.9 |
| 56 | What’s Next? – Staying up‑to‑date in a fast‑moving field | Ch 7.9 |
| 57 | Appendix A – Introduction to PyTorch | Appendix A |
| 58 | Appendix B – References and further reading | Appendix B |
| 59 | Appendix C – Exercise solutions | Appendix C |
| 60 | Appendix D – Adding bells and whistles to the training loop | Appendix D |

---

### Phase 1 — Runtime: Single‑Instance Optimization (Days 61‑78)

| Day | Topic | Book |
|-----|-------|------|
| 61 | LLM Inference Mechanics: End‑to‑end text generation | Ch 2.2 |
| 62 | Inference from Scratch: Model internals & tokenization | Ch 2.2 |
| 63 | Embeddings: From integers to vectors | Ch 2.2.1 |
| 64 | Transformer Blocks & Attention Deep Dive | Ch 2.2.2–2.2.3 |
| 65 | Ops: Byte Ratio & Arithmetic Intensity | Ch 2.4 |
| 66 | Mixture of Experts (MoE) Routing | Ch 2.2.4 |
| 67 | CUDA Kernels, Kernel Selection & Kernel Fusion | Ch 4.1 |
| 68 | PyTorch, Model File Formats, ONNX & TensorRT | Ch 4.2 |
| 69 | vLLM: PagedAttention & Continuous Batching | Ch 4.3.1 |
| 70 | SGLang: RadixAttention & Structured Outputs | Ch 4.3.2 |
| 71 | TensorRT‑LLM: Compilation & Plugin System | Ch 4.3.3 |
| 72 | NVIDIA Dynamo: Disaggregated Serving | Ch 4.4 |
| 73 | Quantization: Number Formats (FP8, INT8, INT4) | Ch 5.1.1 |
| 74 | Quantization: GPTQ, AWQ, SmoothQuant | Ch 5.1.2 |
| 75 | Speculative Decoding: Draft‑Target, Medusa, EAGLE | Ch 5.2 |
| 76 | KV Cache: Prefix Caching & Cache‑Aware Routing | Ch 5.3 |
| 77 | Model Parallelism: Tensor & Expert | Ch 5.4 |
| 78 | Disaggregation: Prefill/Decode Split | Ch 5.5 |

---

### Phase 2 — Infrastructure: Scaling Across Clusters (Days 79‑86)

| Day | Topic | Book |
|-----|-------|------|
| 79 | GPU Architecture: SMs, Memory Hierarchy, HBM | Ch 3.1 |
| 80 | GPU Generations: Hopper, Ada, Blackwell, Rubin | Ch 3.2 |
| 81 | Multi‑GPU Instances & Multi‑Instance GPU (MIG) | Ch 3.3 |
| 82 | Containerization: Docker & NVIDIA NIMs | Ch 7.1 |
| 83 | Autoscaling: Concurrency, Batching & Cold Starts | Ch 7.2 |
| 84 | Routing, Load Balancing & Queueing | Ch 7.2.3 |
| 85 | Multi‑Cloud Capacity Management | Ch 7.3 |
| 86 | Zero‑Downtime Deployment & Cost Estimation | Ch 7.4 |

---

### Phase 3 — Tooling: Productivity & Observability (Days 87‑89)

| Day | Topic | Book |
|-----|-------|------|
| 87 | Performance Benchmarking: Tooling & Profiling | Ch 4.5 |
| 88 | Observability: Metrics, Tracing & Dashboards | Ch 7.4.3 |
| 89 | Client Code: Streaming, Async & Protocol Support | Ch 7.5 |

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

