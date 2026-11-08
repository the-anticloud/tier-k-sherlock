# Onboarding Checklist

**Project:** `K_SHERLOCK`  
**Tier:** TIER_6_SECURITY_EVAL  
**Identity:** Upstream `sherlock-project/sherlock` @ `e40a45ec2a07` (MIT)

## Checks

| Check | State | Detail |
| --- | --- | --- |
| Provenance names a commit | PASS | `sherlock-project/sherlock` @ `e40a45ec2a07` |
| Upstream licence identified | PASS | MIT (permissive) |
| Ledger exists | PASS | 0 blocks |
| Ledger chain verifies | PASS | True |
| II budget envelope declared | PASS | 1500.0 IIU |
| At least one verified upstream edit | PASS | 1 patches |

**6 of 6 met.**

A check that reads `NOT MET` is a real gap, not a formatting artefact.
The order matters: provenance and licence gate every edit, the ledger
gates every claim, and the budget gates every claim about cost.

## Handoff state

`K_SHERLOCK` is at TIER_6_SECURITY_EVAL. It carries a verified upstream clone. 6/6 onboarding checks are met.
