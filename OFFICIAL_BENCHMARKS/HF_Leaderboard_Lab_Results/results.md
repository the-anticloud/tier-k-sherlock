# HF_Leaderboard_Lab_Results

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

**Framework:** [HuggingFace Open LLM Leaderboard (proxy via distilbert-base-uncased)](https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive)

**Model used:** `distilbert-base-uncased`

### Inference Latency (Classification)

| Metric | Value |
| ------ | ----- |
| Avg latency | **44.89 ms** |
| Min latency | 38.27 ms |
| Max latency | 52.05 ms |
| Samples | 5 |

### Real Tokenization Results

| Field | Value |
| ----- | ----- |
| Token count | **31** |
| Tokenization latency | 2.0 ms |
| Classification label | `LABEL_0` |
| Classification score | 0.5841 |
| Classification latency | 115.0 ms |
| Status | **PASS** |

**Input text tokenized:**
```
K_SHERLOCK (sherlock-project/sherlock) — 56 files, 2217 source lines, licence MIT, primary language ['Python']
```

**First 20 tokens:**
```
['[CLS]', 'k', '_', 'sherlock', '(', 'sherlock', '-', 'project', '/', 'sherlock', ')', '—', '56', 'files', ',', '221', '##7', 'source', 'lines', ',']
```

> Full MMLU/HellaSwag/TruthfulQA/ARC/Winogrande/GSM8K require dedicated GPU.
> These results are CPU inference proxy metrics using distilbert-base-uncased.

---
_Anticloud Benchmark Suite — isolation log — 2026-09-30T15:07:07.146295+00:00_