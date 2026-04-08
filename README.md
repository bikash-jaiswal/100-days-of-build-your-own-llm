# 100 Days of LLM Inference

A structured deep‑dive schedule that starts with building an LLM from scratch (days 1‑30) and then extends into inference engineering topics (days 31‑100), based on *[Build a Large Language Model (From Scratch)(https://www.amazon.com/Build-Large-Language-Model-Scratch/dp/0999348450)* and *[Inference Engineering](https://www.baseten.co/library/inference-engineering/)* by Philip Kiely (Baseten Books, 2026).

---

## The Plan

### LLM Building Plan (Days 1‑30)

| Day | Topic | Book |
|-----|-------|------|
| 01 | Preface & Author Overview | <a href="days/day01" target="_blank">Preface</a> |
| 02 | Understanding LLMs: Architecture & Applications | <a href="days/day02" target="_blank">Ch 1.1-1.7</a> |
| 03 | Text Data Processing: Tokenization & Embeddings | <a href="days/day03" target="_blank">Ch 2.1-2.8</a> |
| 04 | Attention Mechanisms: Self-Attention & Multi-Head | <a href="days/day04" target="_blank">Ch 3.1-3.6</a> |
| 05 | GPT Model Architecture & Implementation | <a href="days/day05" target="_blank">Ch 4.1-4.7</a> |
| 06 | Pretraining: Loss, Training & Decoding | <a href="days/day06" target="_blank">Ch 5.1-5.5</a> |
| 07 | Fine-tuning for Classification Tasks | <a href="days/day07" target="_blank">Ch 6.1-6.8</a> |
| 08 | Instruction Fine-tuning & Evaluation | <a href="days/day08" target="_blank">Ch 7.1-7.9</a> |
| 09 | PyTorch Fundamentals & Training Loop | <a href="days/day09" target="_blank">Appendix A-D</a> |
| 10 | Build Complete LLM from Scratch (Integration) | <a href="days/day10" target="_blank">Integration</a> |
| 11-30 | Extended LLM Building Practice & Experiments | <a href="days/day11" target="_blank">Practice</a> |

---

### Phase 1 — Runtime: Single‑Instance Optimization (Days 31‑50)

| Day | Topic | Book |
|-----|-------|------|
| 31 | LLM Inference Mechanics: End‑to‑end text generation | <a href="days/day31" target="_blank">Ch 2.2</a> |
| 32 | Inference from Scratch: Model internals & tokenization | <a href="days/day32" target="_blank">Ch 2.2</a> |
| 33 | Embeddings: From integers to vectors | <a href="days/day33" target="_blank">Ch 2.2.1</a> |
| 34 | Transformer Blocks & Attention Deep Dive | <a href="days/day34" target="_blank">Ch 2.2.2–2.2.3</a> |
| 35 | Ops: Byte Ratio & Arithmetic Intensity | <a href="days/day35" target="_blank">Ch 2.4</a> |
| 36 | Mixture of Experts (MoE) Routing | <a href="days/day36" target="_blank">Ch 2.2.4</a> |
| 37 | CUDA Kernels, Kernel Selection & Kernel Fusion | <a href="days/day37" target="_blank">Ch 4.1</a> |
| 38 | PyTorch, Model File Formats, ONNX & TensorRT | <a href="days/day38" target="_blank">Ch 4.2</a> |
| 39 | vLLM: PagedAttention & Continuous Batching | <a href="days/day39" target="_blank">Ch 4.3.1</a> |
| 40 | SGLang: RadixAttention & Structured Outputs | <a href="days/day40" target="_blank">Ch 4.3.2</a> |
| 41 | TensorRT‑LLM: Compilation & Plugin System | <a href="days/day41" target="_blank">Ch 4.3.3</a> |
| 42 | NVIDIA Dynamo: Disaggregated Serving | <a href="days/day42" target="_blank">Ch 4.4</a> |
| 43 | Quantization: Number Formats (FP8, INT8, INT4) | <a href="days/day43" target="_blank">Ch 5.1.1</a> |
| 44 | Quantization: GPTQ, AWQ, SmoothQuant | <a href="days/day44" target="_blank">Ch 5.1.2</a> |
| 45 | Speculative Decoding: Draft‑Target, Medusa, EAGLE | <a href="days/day45" target="_blank">Ch 5.2</a> |
| 46 | KV Cache: Prefix Caching & Cache‑Aware Routing | <a href="days/day46" target="_blank">Ch 5.3</a> |
| 47 | Model Parallelism: Tensor & Expert | <a href="days/day47" target="_blank">Ch 5.4</a> |
| 48 | Disaggregation: Prefill/Decode Split | <a href="days/day48" target="_blank">Ch 5.5</a> |
| 49 | LoRA/QLoRA for Efficient Inference | <a href="days/day49" target="_blank">Advanced</a> |
| 50 | Streaming Inference & Chunked Processing | <a href="days/day50" target="_blank">Advanced</a> |

---

### Phase 2 — Infrastructure: Scaling Across Clusters (Days 51‑65)

| Day | Topic | Book |
|-----|-------|------|
| 51 | GPU Architecture: SMs, Memory Hierarchy, HBM | <a href="days/day51" target="_blank">Ch 3.1</a> |
| 52 | GPU Generations: Hopper, Ada, Blackwell, Rubin | <a href="days/day52" target="_blank">Ch 3.2</a> |
| 53 | Multi‑GPU Instances & Multi‑Instance GPU (MIG) | <a href="days/day53" target="_blank">Ch 3.3</a> |
| 54 | Containerization: Docker & NVIDIA NIMs | <a href="days/day54" target="_blank">Ch 7.1</a> |
| 55 | Autoscaling: Concurrency, Batching & Cold Starts | <a href="days/day55" target="_blank">Ch 7.2</a> |
| 56 | Routing, Load Balancing & Queueing | <a href="days/day56" target="_blank">Ch 7.2.3</a> |
| 57 | Multi‑Cloud Capacity Management | <a href="days/day57" target="_blank">Ch 7.3</a> |
| 58 | Zero‑Downtime Deployment & Cost Estimation | <a href="days/day58" target="_blank">Ch 7.4</a> |
| 59 | Distributed Inference: Ray Serve & Triton | <a href="days/day59" target="_blank">Advanced</a> |
| 60 | Model Sharding & Pipeline Parallelism | <a href="days/day60" target="_blank">Advanced</a> |
| 61 | Edge Deployment & On-Device Inference | <a href="days/day61" target="_blank">Advanced</a> |
| 62 | Mobile LLM Optimization | <a href="days/day62" target="_blank">Advanced</a> |
| 63 | Serverless Inference & Lambda Functions | <a href="days/day63" target="_blank">Advanced</a> |
| 64 | Custom Kernel Development with Triton | <a href="days/day64" target="_blank">Advanced</a> |
| 65 | Performance Profiling Deep Dive | <a href="days/day65" target="_blank">Advanced</a> |

---

### Phase 3 — Tooling: Productivity & Observability (Days 66‑75)

| Day | Topic | Book |
|-----|-------|------|
| 66 | Performance Benchmarking: Tooling & Profiling | <a href="days/day66" target="_blank">Ch 4.5</a> |
| 67 | Observability: Metrics, Tracing & Dashboards | <a href="days/day67" target="_blank">Ch 7.4.3</a> |
| 68 | Client Code: Streaming, Async & Protocol Support | <a href="days/day68" target="_blank">Ch 7.5</a> |
| 69 | Memory Optimization Techniques | <a href="days/day69" target="_blank">Advanced</a> |
| 70 | Throughput vs Latency Trade-offs | <a href="days/day70" target="_blank">Advanced</a> |
| 71 | Multi-Model Serving & Model Versioning | <a href="days/day71" target="_blank">Advanced</a> |
| 72 | A/B Testing for Inference Systems | <a href="days/day72" target="_blank">Advanced</a> |
| 73 | Monitoring & Alerting Best Practices | <a href="days/day73" target="_blank">Advanced</a> |
| 74 | Cost Optimization Strategies | <a href="days/day74" target="_blank">Advanced</a> |
| 75 | Batch Optimization & Dynamic Batching | <a href="days/day75" target="_blank">Advanced</a> |

---

### Phase 4 — Deep Implementation (Days 76‑100)

| Day | Project |
|-----|---------|
| 76 | Implement a BPE tokenizer from scratch |
| 77 | Build a bare autoregressive decoder loop in PyTorch |
| 78 | Implement scaled dot‑product attention (SDPA) with masking |
| 79 | Implement Flash Attention (simplified, tiling in Python) |
| 80 | Profile attention memory growth across sequence lengths |
| 81 | Build an INT8 quantization pipeline: quantize → dequantize → measure error |
| 82 | Implement GPTQ‑style round‑to‑nearest with Hessian weighting |
| 83 | Sweep quantization bit widths and plot perplexity vs compression |
| 84 | Simulate draft‑target speculative decoding with acceptance sampling |
| 85 | Build a simple KV cache manager (block allocator, eviction policy) |
| 86 | Implement prefix caching with hash‑based deduplication |
| 87 | Build custom CUDA kernel for attention |
| 88 | Implement LoRA adapter for efficient fine-tuning |
| 89 | Build streaming inference server with WebSocket support |
| 90 | Implement model sharding across multiple GPUs |
| 91 | Build distributed inference system with Ray Serve |
| 92 | Optimize model for edge deployment (mobile/embedded) |
| 93 | Implement advanced caching strategies (semantic cache, LRU) |
| 94 | Build A/B testing framework for model comparison |
| 95 | Implement auto-scaling inference service |
| 96 | Build observability dashboard with real-time metrics |
| 97 | Implement cost optimization with spot instances |
| 98 | Build multi-model serving gateway |
| 99 | End-to-end performance optimization project |
| 100 | Capstone: Production-ready inference system |
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
| LLM Building Plan (Days 1‑30) | 0 / 30 |
| Runtime Layer (Days 31‑50) | 0 / 20 |
| Infrastructure Layer (Days 51‑65) | 0 / 15 |
| Tooling Layer (Days 66‑75) | 0 / 10 |
| Deep Implementation (Days 76‑100) | 0 / 25 |
| **Total** | **0 / 100** |

---

## Reference

- **Book:** *Build a Large Language Model (From Scratch)* — Sebastian Raschka (Manning Publications, 2025) — ISBN: 978-1633437166
- **Book:** *Inference Engineering* — Philip Kiely (Baseten Books, 2026) — [Online](https://www.baseten.co/library/inference-engineering/)
- **Cluster:** spark-01 `192.168.1.76` · spark-02 `192.168.1.77`

