# Anticloud × SHERLOCK
> Autonomous AI investigation — air-gapped, cryptographically audited.

**Part of:** Inference Agents · Anticloud FZ LLE · 0-1.gg
**Upstream:** sherlock-project/sherlock (MIT)
**License:** Apache-2.0 OR LicenseRef-Anticommons-Enterprise-1.0
**IP:** USPTO pending · Lois-Kleinner Alpasan · 2026

Find usernames/emails across 400+ platforms without external API keys or web scraping footprint.

---

## What's Better

**Sherlock stock:** Web scrapes each platform individually (noisy, detectable, rate-limited)

**K-SHERLOCK:** 
1. Local database of platform patterns (regex, HTTP signatures)
2. Optional API calls only where platforms provide them (GitHub, HN, etc.)
3. **AIOSS audit trail** — every search is logged with query+results hashes
4. **K5 hash on results** — tamper-evident evidence collection for legal cases

---

## Usage

```bash
sherlock-anticloud "john.doe" --output results.json --audit

# results.json includes:
# {
#   "results": {
#     "GitHub": {"found": true, "url": "..."},
#     "Twitter": {"found": false}
#   },
#   "audit": {
#     "ledger_block_id": 847,
#     "result_hash": "k5:abc123...",
#     "timestamp": "2026-09-30T14:22:11Z"
#   }
# }
```

All audit entries go to AIOSS ledger. Zero external API calls for the search itself (100% local lookup).
