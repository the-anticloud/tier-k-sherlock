# SOC2_Lab_Results

**Project:** `K_SHERLOCK`  
**Tier:** `TIER_4_INFERENCE_AGENTS`  
**Slug:** `sherlock-project/sherlock`  
**Commit:** `e40a45ec2a07`  
**Run:** `2026-09-30T15:07:07.146295+00:00`  

## Isolation Environment

| Field | Value |
| ----- | ----- |
| Platform | `win32` |
| Python | `3.12.10` |
| HF model | `distilbert-base-uncased` |
| HF load time | `4.42s` |
| Inference device | `cpu` |

## Results

**Framework:** [SOC 2 Type II (AICPA TSC + AI-specific 2026)](https://soc2auditors.org/insights/soc-2-for-ai-companies/)

Readiness: **40%** (2/5 criteria)

| Control | Name | Status | Method |
| ------- | ---- | ------ | ------ |
| `CC6` | Logical and Physical Access Controls | **FAIL** | presence of .github/ (access controls via branch protection) |
| `CC7` | System Operations - Change Management | **FAIL** | presence of CI/CD workflows (change management) |
| `CC8` | Change Management - Tested Deployments | **FAIL** | presence of tests/ directory |
| `AI-01` | Model Governance (AI-specific) | **PASS** | OFFICIAL_BENCHMARKS/ directory exists (model lifecycle docs) |
| `AI-02` | LLM Subprocessor Risk Assessment | **PASS** | upstream licence identified (vendor risk assessment) |

---
_Anticloud Benchmark Suite — isolation log — 2026-09-30T15:07:07.146295+00:00_