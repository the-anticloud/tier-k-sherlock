# 3-Seed Simulation — K_SHERLOCK

**Seeds:** `51892` · `83229` · `17428`

**Seed method:** `sha256("K_SHERLOCK")[:8]` as hex→int, offsets +0 / +31337 / +65536

> These seeds are deterministic and documented. Any researcher can reproduce this simulation exactly by running `write_three_seed_simulation.py` with project name `K_SHERLOCK`.

## Confidence Intervals (mean ± σ across 3 seeds)

| Metric | Mean | σ | 95% CI |
|--------|------|---|--------|
| trl_score | 6.971 | 0.2345 | ±0.4596 |
| throughput_tokens_per_sec | 262.0 | 23.8144 | ±46.6762 |
| p50_latency_ms | 45.84 | 4.4566 | ±8.7349 |
| p99_latency_ms | 118.4033 | 6.4043 | ±12.5524 |
| ttft_ms | 25.2667 | 1.2422 | ±2.4347 |
| mmlu_proxy | 0.6835 | 0.0262 | ±0.0514 |
| hellaswag_proxy | 0.7783 | 0.0301 | ±0.059 |
| truthfulqa_proxy | 0.5537 | 0.0205 | ±0.0402 |
| arc_proxy | 0.7027 | 0.0388 | ±0.076 |
| complexity_cyclomatic | 4.2033 | 0.6561 | ±1.286 |
| maintainability_index | 69.9933 | 4.3653 | ±8.556 |
| security_issues_high | 0.3333 | 0.4714 | ±0.9239 |
| dependency_freshness_pct | 81.9333 | 2.2647 | ±4.4388 |
| test_coverage_pct | 67.6333 | 3.8003 | ±7.4486 |
| doc_coverage_pct | 68.6 | 6.4689 | ±12.679 |
| memory_mb | 50.0 | 0.0 | ±0.0 |
| gpu_util_pct | 65.4667 | 5.4908 | ±10.762 |
| openssf_score | 6.6767 | 0.6373 | ±1.2491 |
| eu_ai_act_compliance_pct | 87.4667 | 0.7134 | ±1.3983 |
| slsa_level | 1.6667 | 0.4714 | ±0.9239 |

## Per-Seed Raw Results

| Metric | Seed 51892 | Seed 83229 | Seed 17428 |
|--------|------------|------------|------------|
| trl_score | 7.278 | 6.709 | 6.926 |
| throughput_tokens_per_sec | 295.2 | 240.5 | 250.3 |
| p50_latency_ms | 52.13 | 42.35 | 43.04 |
| p99_latency_ms | 112.37 | 115.57 | 127.27 |
| ttft_ms | 23.89 | 26.9 | 25.01 |
| mmlu_proxy | 0.665 | 0.6649 | 0.7205 |
| hellaswag_proxy | 0.8148 | 0.7791 | 0.741 |
| truthfulqa_proxy | 0.5805 | 0.5496 | 0.5309 |
| arc_proxy | 0.6481 | 0.7343 | 0.7258 |
| complexity_cyclomatic | 3.78 | 3.7 | 5.13 |
| maintainability_index | 73.05 | 63.82 | 73.11 |
| security_issues_high | 1 | 0 | 0 |
| dependency_freshness_pct | 79.6 | 85.0 | 81.2 |
| test_coverage_pct | 65.2 | 64.7 | 73.0 |
| doc_coverage_pct | 61.8 | 66.7 | 77.3 |
| memory_mb | 50 | 50 | 50 |
| gpu_util_pct | 64.8 | 59.1 | 72.5 |
| openssf_score | 7.44 | 6.71 | 5.88 |
| eu_ai_act_compliance_pct | 86.5 | 87.7 | 88.2 |
| slsa_level | 2 | 2 | 1 |

---
_Anticloud 3-Seed Simulation — 2026-09-30T16:01:40.704491+00:00_
_Citation: Lois-Kleinner. (2026). The Anticloud. DOI: pending._