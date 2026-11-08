# Developer Cookbook — K_SHERLOCK
**Stack:** Python 3.11, PAX 27B (ReAct), api-oss-logging, AIOSS_FORMAT, KANTOR_K5
**Domain:** Investigative reasoning agent: systematic root-cause analysis and diagnosis for Anticloud

## Investigate a system anomaly
```python
from k_sherlock import SherlockAgent

sherlock = SherlockAgent(
    pax_model="./pax-27b-q4.gguf",
    log_source="./logs/api_oss_logging.db",
    kantor_db="./kantor_k5.db",
    aioss_chain="./sherlock.aioss"
)

investigation = sherlock.investigate(
    symptom="PAX_INFERENCE_CORE P99 latency increased from 500ms to 2100ms at 14:23 today",
    context={"time_window": "14:00-15:00", "affected_module": "PAX_INFERENCE_CORE"}
)

print("CONCLUSION:", investigation.conclusion)
print("ROOT CAUSE:", investigation.root_cause)
print("REMEDIATION:", investigation.remediation)
print(f"Chain: {investigation.chain_hash}")
```

## Inspect reasoning trace
```python
for step in investigation.trace:
    print(f"[{step.step_type}] {step.content[:100]}")
# [THOUGHT] Latency spike at 14:23 suggests I/O bottleneck or GPU contention
# [ACTION] query_logs: filter PAX_INFERENCE_CORE errors 14:00-15:00
# [OBSERVATION] 47 IOError entries: AIOSS chain file locked
# [THOUGHT] Another process is holding aioss_chain file lock
# [CONCLUSION] Root cause: parallel chain appends without lock
```

## Automated monitoring + investigation
```python
sherlock.watch(
    modules=["PAX_INFERENCE_CORE", "KAMELOT_SEARCH"],
    alert_thresholds={"latency_p99_ms": 1500, "error_rate": 0.01},
    auto_investigate=True
)
```

## AIOSS Chain Append
```python
import hashlib, time

def aioss_append(chain_path, payload: bytes, module_id: str):
    entry_hash = hashlib.sha3_256(payload).digest()
    ts = int(time.time_ns()).to_bytes(8, 'big')
    with open(chain_path, 'rb') as f:
        f.seek(-32, 2); prev_hash = f.read(32)
    new_hash = hashlib.sha3_256(prev_hash + entry_hash + ts).digest()
    with open(chain_path, 'ab') as f:
        f.write(ts + entry_hash + new_hash)
    return new_hash.hex()
```
