# Deploy Guide — K_SHERLOCK
**Tier:** TIER_6_SECURITY_EVAL | **Stack:** Python 3.11, PAX 27B (ReAct), api-oss-logging, AIOSS_FORMAT
**Air-gap capable after initial setup.**

## Prerequisites
Python 3.11+, PAX 27B, api-oss-logging access (read), AIOSS chain access (read).

## Environment
8GB RAM. GPU for PAX reasoning. Read-only access to all Anticloud logs and chains.

## AIOSS Integration
```bash
aioss init --module K_SHERLOCK --output ./k_sherlock.aioss
aioss append --chain ./k_sherlock.aioss --payload ./output.bin --module K_SHERLOCK
aioss verify --chain ./k_sherlock.aioss
```

## Air-Gap Setup
```bash
pip download -r requirements.txt -d ./wheels/
pip install --no-index --find-links ./wheels/ -r requirements.txt
```

## PAX 27B Harness Wiring
```python
from anticloud_pax import PAXHarness
harness = PAXHarness(
    model_path="./pax-27b-q4.gguf",
    module="K_SHERLOCK",
    aioss_chain="./K_SHERLOCK.aioss",
    classification="L5_NARROW_L2_GENERAL"
)
result = harness.process(input_data)
```

## Verification
```bash
aioss verify --chain ./K_SHERLOCK.aioss --verbose
python -m K_SHERLOCK.tests.smoke
```
