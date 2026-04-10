# 100 Days of LLM Inference

A structured deep‑dive schedule that starts with building an LLM from scratch (days 1‑30) and then extends into inference engineering topics (days 31‑100), based on *[Build a Large Language Model (From Scratch)(https://www.amazon.com/Build-Large-Language-Model-Scratch/dp/0999348450)* and *[Inference Engineering](https://www.baseten.co/library/inference-engineering/)* by Philip Kiely (Baseten Books, 2026).

---

## The Plan

### LLM Building Plan (Days 1‑40)

| Day | Topic | Book |
|-----|-------|------|
| Day 1 | Understanding LLMs: Architecture & Applications (Part 1) | <a href="days/day01" target="_blank">Ch 1.1-1.3</a> |
| Day 2 | Understanding LLMs: Architecture & Applications (Part 2) | <a href="days/day02" target="_blank">Ch 1.4-1.7</a> |
| Day 3 | Text Data Processing: Tokenization & Embeddings (Part 1) | <a href="days/day03" target="_blank">Ch 2.1-2.4</a> |
| Day 4 | Text Data Processing: Tokenization & Embeddings (Part 2) | <a href="days/day04" target="_blank">Ch 2.5-2.8</a> |
| Day 5 | Attention Mechanisms: Self-Attention & Multi-Head (Part 1) | <a href="days/day05" target="_blank">Ch 3.1-3.3</a> |
| Day 6 | Attention Mechanisms: Self-Attention & Multi-Head (Part 2) | <a href="days/day06" target="_blank">Ch 3.4-3.6</a> |
| Day 7 | GPT Model Architecture & Implementation (Part 1) | <a href="days/day07" target="_blank">Ch 4.1-4.3</a> |
| Day 8 | GPT Model Architecture & Implementation (Part 2) | <a href="days/day08" target="_blank">Ch 4.4-4.7</a> |
| Day 9 | Pretraining: Loss, Training & Decoding (Part 1) | <a href="days/day09" target="_blank">Ch 5.1-5.2</a> |
| Day 10 | Pretraining: Loss, Training & Decoding (Part 2) | <a href="days/day10" target="_blank">Ch 5.3-5.5</a> |
| Day 11 | Fine-tuning for Classification Tasks (Part 1) | <a href="days/day11" target="_blank">Ch 6.1-6.4</a> |
| Day 12 | Fine-tuning for Classification Tasks (Part 2) | <a href="days/day12" target="_blank">Ch 6.5-6.8</a> |
| Day 13 | Instruction Fine-tuning & Evaluation (Part 1) | <a href="days/day13" target="_blank">Ch 7.1-7.4</a> |
| Day 14 | Instruction Fine-tuning & Evaluation (Part 2) | <a href="days/day14" target="_blank">Ch 7.5-7.9</a> |
| Day 15 | PyTorch Fundamentals & Training Loop (Part 1) | <a href="days/day15" target="_blank">Appendix A-B</a> |
| Day 16 | PyTorch Fundamentals & Training Loop (Part 2) | <a href="days/day16" target="_blank">Appendix C-D</a> |
| Day 17 | Build Complete LLM from Scratch (Integration) | <a href="days/day17" target="_blank">Integration</a> |
| Day 18-40 | Extended LLM Building Practice & Experiments | <a href="days/day18" target="_blank">Practice</a> |

---

### Phase 1 — Runtime: Single‑Instance Optimization (Days 41‑60)

| Day | Topic | Book |
|-----|-------|------|
| Day 41 | LLM Inference Mechanics: End‑to‑end text generation | <a href="days/day41" target="_blank">Ch 2.2</a> |
| Day 42 | Inference from Scratch: Model internals & tokenization | <a href="days/day42" target="_blank">Ch 2.2</a> |
| Day 43 | Embeddings: From integers to vectors | <a href="days/day43" target="_blank">Ch 2.2.1</a> |
| Day 44 | Transformer Blocks & Attention Deep Dive | <a href="days/day44" target="_blank">Ch 2.2.2–2.2.3</a> |
| Day 45 | Ops: Byte Ratio & Arithmetic Intensity | <a href="days/day45" target="_blank">Ch 2.4</a> |
| Day 46 | Mixture of Experts (MoE) Routing | <a href="days/day46" target="_blank">Ch 2.2.4</a> |
| Day 47 | CUDA Kernels, Kernel Selection & Kernel Fusion | <a href="days/day47" target="_blank">Ch 4.1</a> |
| Day 48 | PyTorch, Model File Formats, ONNX & TensorRT | <a href="days/day48" target="_blank">Ch 4.2</a> |
| Day 49 | vLLM: PagedAttention & Continuous Batching | <a href="days/day49" target="_blank">Ch 4.3.1</a> |
| Day 50 | SGLang: RadixAttention & Structured Outputs | <a href="days/day50" target="_blank">Ch 4.3.2</a> |
| Day 51 | TensorRT‑LLM: Compilation & Plugin System | <a href="days/day51" target="_blank">Ch 4.3.3</a> |
| Day 52 | NVIDIA Dynamo: Disaggregated Serving | <a href="days/day52" target="_blank">Ch 4.4</a> |
| Day 53 | Quantization: Number Formats (FP8, INT8, INT4) | <a href="days/day53" target="_blank">Ch 5.1.1</a> |
| Day 54 | Quantization: GPTQ, AWQ, SmoothQuant | <a href="days/day54" target="_blank">Ch 5.1.2</a> |
| Day 55 | Speculative Decoding: Draft‑Target, Medusa, EAGLE | <a href="days/day55" target="_blank">Ch 5.2</a> |
| Day 56 | KV Cache: Prefix Caching & Cache‑Aware Routing | <a href="days/day56" target="_blank">Ch 5.3</a> |
| Day 57 | Model Parallelism: Tensor & Expert | <a href="days/day57" target="_blank">Ch 5.4</a> |
| Day 58 | Disaggregation: Prefill/Decode Split | <a href="days/day58" target="_blank">Ch 5.5</a> |
| Day 59 | LoRA/QLoRA for Efficient Inference | <a href="days/day59" target="_blank">Advanced</a> |
| Day 60 | Streaming Inference & Chunked Processing | <a href="days/day60" target="_blank">Advanced</a> |

---

### Phase 2 — Infrastructure: Scaling Across Clusters (Days 61‑75)

| Day | Topic | Book |
|-----|-------|------|
| Day 61 | GPU Architecture: SMs, Memory Hierarchy, HBM | <a href="days/day61" target="_blank">Ch 3.1</a> |
| Day 62 | GPU Generations: Hopper, Ada, Blackwell, Rubin | <a href="days/day62" target="_blank">Ch 3.2</a> |
| Day 63 | Multi‑GPU Instances & Multi‑Instance GPU (MIG) | <a href="days/day63" target="_blank">Ch 3.3</a> |
| Day 64 | Containerization: Docker & NVIDIA NIMs | <a href="days/day64" target="_blank">Ch 7.1</a> |
| Day 65 | Autoscaling: Concurrency, Batching & Cold Starts | <a href="days/day65" target="_blank">Ch 7.2</a> |
| Day 66 | Routing, Load Balancing & Queueing | <a href="days/day66" target="_blank">Ch 7.2.3</a> |
| Day 67 | Multi‑Cloud Capacity Management | <a href="days/day67" target="_blank">Ch 7.3</a> |
| Day 68 | Zero‑Downtime Deployment & Cost Estimation | <a href="days/day68" target="_blank">Ch 7.4</a> |
| Day 69 | Distributed Inference: Ray Serve & Triton | <a href="days/day69" target="_blank">Advanced</a> |
| Day 70 | Model Sharding & Pipeline Parallelism | <a href="days/day70" target="_blank">Advanced</a> |
| Day 71 | Edge Deployment & On-Device Inference | <a href="days/day71" target="_blank">Advanced</a> |
| Day 72 | Mobile LLM Optimization | <a href="days/day72" target="_blank">Advanced</a> |
| Day 73 | Serverless Inference & Lambda Functions | <a href="days/day73" target="_blank">Advanced</a> |
| Day 74 | Custom Kernel Development with Triton | <a href="days/day74" target="_blank">Advanced</a> |
| Day 75 | Performance Profiling Deep Dive | <a href="days/day75" target="_blank">Advanced</a> |

---

### Phase 3 — Tooling: Productivity & Observability (Days 76‑85)

| Day | Topic | Book |
|-----|-------|------|
| Day 76 | Performance Benchmarking: Tooling & Profiling | <a href="days/day76" target="_blank">Ch 4.5</a> |
| Day 77 | Observability: Metrics, Tracing & Dashboards | <a href="days/day77" target="_blank">Ch 7.4.3</a> |
| Day 78 | Client Code: Streaming, Async & Protocol Support | <a href="days/day78" target="_blank">Ch 7.5</a> |
| Day 79 | Memory Optimization Techniques | <a href="days/day79" target="_blank">Advanced</a> |
| Day 80 | Throughput vs Latency Trade-offs | <a href="days/day80" target="_blank">Advanced</a> |
| Day 81 | Multi-Model Serving & Model Versioning | <a href="days/day81" target="_blank">Advanced</a> |
| Day 82 | A/B Testing for Inference Systems | <a href="days/day82" target="_blank">Advanced</a> |
| Day 83 | Monitoring & Alerting Best Practices | <a href="days/day83" target="_blank">Advanced</a> |
| Day 84 | Cost Optimization Strategies | <a href="days/day84" target="_blank">Advanced</a> |
| Day 85 | Batch Optimization & Dynamic Batching | <a href="days/day85" target="_blank">Advanced</a> |

---

### Phase 4 — Deep Implementation (Days 86‑110)

| Day | Project |
|-----|---------|
| Day 86 | Implement a BPE tokenizer from scratch |
| Day 87 | Build a bare autoregressive decoder loop in PyTorch |
| Day 88 | Implement scaled dot‑product attention (SDPA) with masking |
| Day 89 | Implement Flash Attention (simplified, tiling in Python) |
| Day 90 | Profile attention memory growth across sequence lengths |
| Day 91 | Build an INT8 quantization pipeline: quantize → dequantize → measure error |
| Day 92 | Implement GPTQ‑style round‑to‑nearest with Hessian weighting |
| Day 93 | Sweep quantization bit widths and plot perplexity vs compression |
| Day 94 | Simulate draft‑target speculative decoding with acceptance sampling |
| Day 95 | Build a simple KV cache manager (block allocator, eviction policy) |
| Day 96 | Implement prefix caching with hash‑based deduplication |
| Day 97 | Build custom CUDA kernel for attention |
| Day 98 | Implement LoRA adapter for efficient fine-tuning |
| Day 99 | Build streaming inference server with WebSocket support |
| Day 100 | Implement model sharding across multiple GPUs |
| Day 101 | Build distributed inference system with Ray Serve |
| Day 102 | Optimize model for edge deployment (mobile/embedded) |
| Day 103 | Implement advanced caching strategies (semantic cache, LRU) |
| Day 104 | Build A/B testing framework for model comparison |
| Day 105 | Implement auto-scaling inference service |
| Day 106 | Build observability dashboard with real-time metrics |
| Day 107 | Implement cost optimization with spot instances |
| Day 108 | Build multi-model serving gateway |
| Day 109 | End-to-end performance optimization project |
| Day 110 | Capstone: Production-ready inference system |
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
| LLM Building Plan (Days 1‑40) | 0 / 40 |
| Runtime Layer (Days 41‑60) | 0 / 20 |
| Infrastructure Layer (Days 61‑75) | 0 / 15 |
| Tooling Layer (Days 76‑85) | 0 / 10 |
| Deep Implementation (Days 86‑110) | 0 / 25 |
| **Total** | **0 / 110** |

---

## Reference

- **Book:** *Build a Large Language Model (From Scratch)* — Sebastian Raschka (Manning Publications, 2025) — ISBN: 978-1633437166
- **Book:** *Inference Engineering* — Philip Kiely (Baseten Books, 2026) — [Online](https://www.baseten.co/library/inference-engineering/)
- **Cluster:** spark-01 `192.168.1.76` · spark-02 `192.168.1.77`

