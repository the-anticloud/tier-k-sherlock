# Anticloud × SHERLOCK
> Autonomous AI investigation — air-gapped, cryptographically audited.

**Part of:** Security Eval · Anticloud FZ LLE · 0-1.gg
**Upstream:** sherlock-project/sherlock (MIT)
**License:** Apache-2.0 OR LicenseRef-Anticommons-Enterprise-1.0
**IP:** USPTO pending · Lois-Kleinner Alpasan · 2026

Find usernames/emails across 400+ platforms. We make it tamper-evident + legally defensible.

---

## Key Improvements Over Sherlock

1. **100% local pattern database** — no web scraping footprint
2. **AIOSS ledger** — every search logged with cryptographic proof
3. **K5-hashed results** — legally defensible evidence for investigations
4. **Zero external APIs** — entirely self-contained

```bash
sherlock-anticloud "john.doe" --audit --output results.json

# Every finding: ledger entry with
# {query_hash, result_hash, timestamp, all_fields_tamper_evident}
```

**OWASP/OSINT safe:** No external calls, all operations logged, no cloud dependency.
