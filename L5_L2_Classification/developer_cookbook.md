# Developer Cookbook — K_SHERLOCK
**Stack:** Python 3.11, PAX 27B (ReAct), api-oss-logging, AIOSS_FORMAT
**Domain:** Investigative agent (T6 instance): security-specific root cause analysis

## Security incident investigation
```python
from k_sherlock_t6 import SecuritySherlockAgent

sherlock = SecuritySherlockAgent(
    pax_model="./pax-27b-q4.gguf",
    log_db="./api_oss_logging.db",
    aioss_chain_dir="./aioss_chains/",
    aioss_chain="./sherlock_security.aioss"
)

investigation = sherlock.investigate(
    incident="AIOSS chain file ai-oss-gateway.aioss shows 847 entries in 10 minutes at 02:30 UTC",
    context={"severity": "high", "affected_module": "ai-oss-gateway"}
)
print(f"Root cause: {investigation.root_cause}")
print(f"NIST phase: {investigation.nist_incident_phase}")
print(f"Containment: {investigation.containment_actions}")
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
