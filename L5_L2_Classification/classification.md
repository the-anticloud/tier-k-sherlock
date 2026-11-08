# L5 Narrow / L2 General Classification — K_SHERLOCK
**Platform:** Anticloud | **Tier:** TIER_6_SECURITY_EVAL | **PAX:** 27B
**IP:** USPTO pending 2026, Anticloud FZ LLE, 0-1.gg | **License:** Apache-2.0

## L5 Narrow
K_SHERLOCK in TIER_6 specializes in security incident investigation: AIOSS chain anomalies, unauthorized access attempts, CVE exploitation indicators. It uses the same ReAct framework as the TIER_4 instance but with security-domain tools and NIST incident handling procedures.

## L2 General
L2 General: K_SHERLOCK's security investigations serve all Anticloud tiers. A PAX inference security incident and a TIER_7 HIPAA violation both trigger K_SHERLOCK investigations.

## PAX 27B Integration
PAX 27B drives the ReAct security investigation loop. Security-specific tools (api-oss-security, api-oss-logging, K_DOCKSEC reports) are available to PAX as callable functions.

## AIOSS Audit Chain
Every security investigation (incident hash + investigation steps hash + root cause hash + NIST response phase) is chained: H_n = SHA3-256(H_{n-1} || entry_hash_n || timestamp_n).
Offline-verifiable, tamper-evident, zero cloud dependency.

## Regulatory / Compliance
NIST SP 800-53 IR-4 (incident handling). ISO 27001 A.16.
