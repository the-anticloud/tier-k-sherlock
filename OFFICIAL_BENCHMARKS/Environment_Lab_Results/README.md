# Environment Lab Results — K_SHERLOCK
**Benchmark type:** Local static analysis (Bandit + Radon)
**Date:** 2026-10-01
**Note:** GPU inference metrics (tok/s, latency, KV cache) available only for T4-scanned projects.

## Static Analysis

| Tool | Metric | Value |
|------|--------|-------|
| Bandit | HIGH findings | 0 |
| Bandit | MEDIUM findings | 0 |
| Bandit | Status | ✅ PASS |
| Radon CC | Avg complexity grade | ? |
| Radon MI | Avg maintainability | None |

## Code Metrics

| Metric | Value |
|--------|-------|
| Python files | 0 |
| Python LOC (est.) | 0 |
| Total files | 283 |

## Anticloud Integration

This project's AIOSS integration layer (`aioss_integration.py`) uses SHA3-256
chain hashing for tamper-evident audit. See `SECURITY_PATCHES.md` for any upstream
Bandit findings documented and mitigated in the Anticloud wrapper.

---
*Anticloud FZ LLE | Apache-2.0 OR LicenseRef-Anticommons-Enterprise-1.0*
