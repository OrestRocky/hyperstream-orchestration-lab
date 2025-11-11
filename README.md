# HyperStream Orchestration Lab

**Reference architecture for real-time AI systems under extreme data intensity**

[![CI](https://github.com/orestyatskuliak/hyperstream-orchestration-lab/actions/workflows/ci.yml/badge.svg)](../../actions)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Built With](https://img.shields.io/badge/Built%20With-FastAPI%20%7C%20Streamlit%20%7C%20Kafka%20%7C%20ONNX%20-%23007ec6)]()

> A high-intensity AI orchestration lab for real-time model pipelines, data synchronization, and human-in-the-loop safety.

## Overview

**HyperStream** is a modular orchestration framework for managing *multi-model AI pipelines, real-time data streams, and human-in-the-loop operations* in high-frequency environments.

It simulates the kind of technical intensity seen in live telemetry, smart manufacturing, or autonomous systems without using any proprietary data. The repository demonstrates how to design, synchronize, and control AI systems at scale while maintaining safety, observability, and cost efficiency.

> **Core Concepts:**
> Orchestration · Stream Processing · Model Mesh · HIL Safety · Observability · Cost-Aware AI Ops


## Tech Summary

| Category       | Tools / Frameworks                         |
| -------------- | ------------------------------------------ |
| Language       | Python 3.11                                |
| Frameworks     | FastAPI · Streamlit · scikit-learn         |
| Infrastructure | Docker Compose · Kafka · MinIO             |
| Architecture   | Model Mesh · Microbatching · SLA-aware DAG |
| Observability  | OpenTelemetry · Prometheus metrics         |
| Docs           | MkDocs · CI/CD via GitHub Actions          |

## Architecture at a Glance

```
[Streams] → [Ingest] → [Processing] → [Feature Store] → [Model Mesh]
                                            ↘                ↘
                                             [HIL Console]    [Alerts/API]
```

**Highlights**

* **Orchestration Layer** — micro-batch & streaming DAGs with backpressure and SLA timers.
* **Model Mesh Router** — dynamic routing (A/B, canary, shadow) based on confidence and rollout strategy.
* **Observability Stack** — RED+USE metrics, alert budgets, and audit logs for overrides.
* **Human-in-the-Loop** — analysts can override, tag, or feed back into retraining cycles.
* **Cost Control** — adaptive sampling, tiered storage, on-demand compute activation.

## Principles of Orchestration

* **Single Source of Truth:** schema-driven configuration (YAML + JSON).
* **Fail-Safe Defaults:** degraded modes when latency exceeds SLA.
* **Observable Everything:** metrics, tracing, audit logs.
* **Human in Command:** AI serves decision-makers, not replaces them.

## Core Modules

| Layer             | Folder               | Description                                            |
| ----------------- | -------------------- | ------------------------------------------------------ |
| **Orchestrator**  | `src/orchestrator/`  | DAG flow control, retries, SLA degradation modes       |
| **Ingest**        | `src/ingest/`        | Synthetic data stream generator + Kafka producer       |
| **Processing**    | `src/processing/`    | Signal decoding, synchronization, feature extraction   |
| **Models**        | `src/models/`        | Rules engine, anomaly ensemble, degradation models     |
| **Router**        | `src/router/`        | Confidence-based model routing, canary/shadow logic    |
| **HIL Console**   | `src/hil/`           | Streamlit interface for human feedback and triage      |
| **Storage**       | `src/storage/`       | Parquet/Delta mock storage & feature store abstraction |
| **API**           | `src/api/`           | FastAPI service for queries, health, and alerts        |
| **Observability** | `src/observability/` | Metrics, tracing, performance dashboards               |

## Quickstart

```bash
# Setup environment
make setup

# Launch core stack (API + UI)
make stack-up

# Start synthetic stream
make run-sim

# Open HIL console
make ui

# Access API
make api
# → http://localhost:8000/docs
```

## Example Configs

```yaml
# config/routing.yaml
routes:
  - name: baseline
    when: "always"
    send: [rules]
  - name: hybrid-anomaly
    when: "confidence >= 0.6"
    send: [anomaly]
    shadow: [degrader]
  - name: canary-rollout
    when: "rollout == true"
    canary:
      model: anomaly
      percent: 10
```

```yaml
# config/topics.yml
raw:
  topic: hyperstream.raw
features:
  topic: hyperstream.features
alerts:
  topic: hyperstream.alerts
```

## Key Metrics

| Category    | Metric            | Description                |
| ----------- | ----------------- | -------------------------- |
| Performance | **Latency p95**   | time from ingest → alert   |
| Reliability | **MTTD / MTTR**   | time to detect / recover   |
| Accuracy    | **FPR / TPR**     | anomaly detection quality  |
| Human-AI    | **Override Rate** | human vs model agreement   |
| Efficiency  | **Cost/hour**     | compute + storage per mode |

## Tech Stack

* **Core:** Python 3.11, FastAPI, Streamlit, NumPy, Pandas, scikit-learn
* **Infra (mock):** Kafka / Redpanda, MinIO, Docker Compose
* **Orchestration:** Prefect / Temporal-ready DAGs
* **Observability:** OpenTelemetry, Prometheus-style metrics
* **Serving:** ONNX / Triton (roadmap)
* **CI/CD:** GitHub Actions · Ruff · Pytest · MkDocs for documentation

## Use Cases

* Real-time quality control in smart manufacturing
* Predictive maintenance in industrial IoT
* Telemetry monitoring in high-frequency data environments
* Autonomous system evaluation pipelines

## Roadmap

* [ ] Online learning via human feedback loop
* [ ] Triton / ONNX runtime integration
* [ ] Kalman + wavelet denoising
* [ ] Scenario generator (sensor failure, dropouts, edge cases)
* [ ] K8s autoscaling + resource orchestration
* [ ] Stream replay & simulation benchmarking

## Documentation

Full documentation available in `/docs`:

* `architecture.md` — system design overview
* `orchestrator-design.md` — DAG logic & SLA management
* `model-mesh.md` — routing, confidence & canary patterns
* `hil-ops.md` — human-in-the-loop process
* `observability.md` — metrics & tracing
* `cost-optimization.md` — compute/storage strategies

## License

MIT License — free for educational and research use.

## Author

**Orest Yatskuliak**
AI Orchestration & Performance Engineering | Systems Generalist
📍 Dubai | 🌐 [linkedin.com/in/orestyatskuliak](https://linkedin.com/in/orestyatskuliak)

> *“Architecture is not code — it’s the discipline of making complexity predictable.”*

<p align="center">
  <sub>Maintained by <a href="https://linkedin.com/in/orestyatskuliak">Orest Yatskuliak</a> · MIT License · 2025</sub>
</p>