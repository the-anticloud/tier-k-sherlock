# L5 Narrow / L2 General Classification — K_SHERLOCK
**Platform:** Anticloud | **Tier:** TIER_4_INFERENCE_AGENTS | **PAX:** 27B
**IP:** USPTO pending 2026, Anticloud FZ LLE, 0-1.gg | **License:** Apache-2.0

## L5 Narrow
K_SHERLOCK implements a systematic investigative reasoning agent using ReAct (Reasoning + Acting) with PAX 27B. Narrow scope: Anticloud system diagnosis — not general debugging. It investigates: AIOSS chain anomalies, inference latency spikes, compliance gaps, and model quality degradation.

## L2 General
L2 General: K_SHERLOCK is the universal diagnostic agent for any tier. TIER_7 biosignal anomalies and TIER_8 RF link failures both trigger K_SHERLOCK investigations using the same ReAct framework.

## PAX 27B Integration
PAX 27B is the reasoning engine for K_SHERLOCK's ReAct loop: Thought → Action → Observation → Thought. Each investigation step is AIOSS-chained, producing a tamper-evident reasoning trace that auditors can follow.

## AIOSS Audit Chain
Every investigation trace (hypothesis hash + action sequence hash + evidence hash + conclusion hash) is chained: H_n = SHA3-256(H_{n-1} || entry_hash_n || timestamp_n).
Offline-verifiable, tamper-evident, zero cloud dependency.

## Regulatory / Compliance
NIST AI RMF 1.0 (explainable AI reasoning). ISO/IEC 42001 (documented AI reasoning chains).
