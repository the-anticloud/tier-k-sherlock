# K_SHERLOCK

## 1. WHAT — K_SHERLOCK (TIER_4_INFERENCE_AGENTS)

K_SHERLOCK is a first-party Anticloud component in TIER_4_INFERENCE_AGENTS. It is developed in this repository (no third-party upstream); the source of truth is the code in this directory.
Scanned source: 558 code/text files, ~44189 lines. Dominant extensions: {'.md': 353, '.json': 134, '.toml': 2, '.yml': 12, '.sh': 2, '.py': 55}.
Key entry points / manifests: anticloud\pyproject.toml, anticloud\src\anticloud_ref\cli.py, UPSTREAM_CLONE\pyproject.toml.
Representative files:
- `00_README.md`
- `BENCH.json`
- `DATA_ROOM_INDEX.md`
- `README.md`
- `sbom.cdx.json`
- `01_INVESTOR_PACKAGE\CAP_TABLE.md`
- `01_INVESTOR_PACKAGE\FINANCIAL_MODEL.md`
- `01_INVESTOR_PACKAGE\GTM_STRATEGY.md`
- `01_INVESTOR_PACKAGE\HIRING_PLAN.md`
- `01_INVESTOR_PACKAGE\IP_ASSIGNMENT.md`
- `01_INVESTOR_PACKAGE\USE_OF_FUNDS.md`
- `02_COMMITMENT_TO_SOCIETY\COMMITMENT_TO_SOCIETY.md`
- `03_COMMITMENT_TO_HUMANITY\COMMITMENT_TO_HUMANITY.md`
- `04_COMMITMENT_TO_ENVIRONMENT\COMMITMENT_TO_ENVIRONMENT.md`
- `05_COMMITMENTS_TO_PAST_PRESENT_FUTURE\COMMITMENTS_TO_PAST_PRESENT_FUTURE.md`

## 2. INSTALL

```bash
# inspect source
ls "K_SHERLOCK"
pip install -e .
```

## 3. USE

```bash
python anticloud/cli.py --help
```

## 4. API

Top-level Python imports observed in source (first 60 lines per file):
- `from .gcounter import GCounter`
- `from .lww import HybridLogicalClock, LWWRegister`
- `from .orset import ORSet`
- `from .pncounter import PNCounter`
- `from __future__ import annotations`
- `from anticloud_ref._version import __version__`
- `from anticloud_ref._version import __version__, version_tuple`
- `from anticloud_ref.bench import (  # noqa: E402`
- `from anticloud_ref.bench.compliance import (`
- `from anticloud_ref.bench.runner import (`
- `from anticloud_ref.bench.sbom import build_sbom, write_sbom`
- `from anticloud_ref.crdt import (`
- `from anticloud_ref.crdt.convergence import (`
- `from anticloud_ref.crdt.convergence import convergence_report`
- `from anticloud_ref.crdt.gcounter import GCounter`
- `from anticloud_ref.crdt.lww import HybridLogicalClock, LWWRegister`
- `from anticloud_ref.crdt.lww import HybridLogicalClock, LWWRegister, Timestamp`
- `from anticloud_ref.crdt.orset import ORSet`
- `from anticloud_ref.crdt.pncounter import PNCounter`
- `from anticloud_ref.deps import generate_lock, parse_lock, verify_lock`

## 5. DEPENDENCIES

Extensions histogram: {".md": 353, ".json": 134, ".toml": 2, ".yml": 12, ".sh": 2, ".py": 55}. Manifests detected: anticloud\pyproject.toml, anticloud\src\anticloud_ref\cli.py, UPSTREAM_CLONE\pyproject.toml.

## 6. CONFIGURE

Environment variables and config files are read from source defaults; no mandatory external config was detected by the scan. Check the entry-point files above for env-var names. Common pattern: copy any `*.example` / `config.*` file next to the entry point and edit values.

## 7. CONTRIBUTING

First-party repo: open an issue describing the change, keep patches small, add/extend tests next to the module, and ensure the 16-check suite stays green before submitting.

## 8. LICENSE — Anticommons 0.1.0

This first-party component is released under the Anticommons 0.1.0 license. See LICENSE (or LICENCE) in the repository root; if absent, the Anticommons 0.1.0 terms apply as stated by the project owner.

## 9. UPSTREAM — first-party (no third-party upstream)

First-party Anticloud work: there is no third-party upstream clone for this project. Provenance is the local change history of this directory, not a pinned external SHA.

## 10. BENCHMARKS (from on-disk BENCH.json)

BENCH.json present on disk. Excerpt: `{"schema": "anticloud.tier-bench/1", "project": "K_SHERLOCK", "source": {"repo_path": "E:\\fenta\\Downloads\\The Anticloud\\TIER_4_INFERENCE_AGENTS\\K_SHERLOCK\\UPSTREAM_CLONE", "git": {"head": "e40a45ec2a074b90703b3b4b842c8a3adbd6ada3", "url": "https://github.com/sherlock-project/sherlock.git", "branch": "HEAD", "committed_at": "2026-09-26T14:37:28+02:00"}}, "metrics": {"files_total": 37, "source_files_scanned": 17, "lines_of_code": 2177, "languages": {".py": 17, "(none)": 5, ".md": 4, ".png": 3, ".ini": 2, ".json": 2, ".jpg": 2, ".toml": 1, ".typed": 1}}, "licence": {"spdx": "MIT", "class": "A", "source_file": "LICENSE", "redistribution_allowed": true}, "dependencies": {"count": 0, "unique": 0, "by_ecosystem": {}, "list": []}, "owasp_top10": {"total_findings": 4, "files_with_findings": 4, "severity": {"high": 1, "medium": 2, "low": 1}, "categories": {"A01-BrokenAccessControl": {"count": 0, "findings": []}, "A02-CryptographicFailures": {"count": 0, "findings": []}, "A03-Injection": {"count": 1, "findings": [{"severity": "high", "file": "tests/sherlock_interactives.py", "line": 17, "cwe": "CWE-78", "snippet": "proc_out = subprocess.check_output(command, shell=True, stderr=subproces`
File/LOC scan at doc time: 558 files, ~44189 lines. Result register (ISOLATED_LAB_RESULTS/03_Result_Register.md): present; anticloud/ overlay entries: 17; installer/ dir: present.

## Appendix — full scanned file list (evidence)

- `00_README.md`
- `BENCH.json`
- `DATA_ROOM_INDEX.md`
- `README.md`
- `sbom.cdx.json`
- `01_INVESTOR_PACKAGE\CAP_TABLE.md`
- `01_INVESTOR_PACKAGE\FINANCIAL_MODEL.md`
- `01_INVESTOR_PACKAGE\GTM_STRATEGY.md`
- `01_INVESTOR_PACKAGE\HIRING_PLAN.md`
- `01_INVESTOR_PACKAGE\IP_ASSIGNMENT.md`
- `01_INVESTOR_PACKAGE\USE_OF_FUNDS.md`
- `02_COMMITMENT_TO_SOCIETY\COMMITMENT_TO_SOCIETY.md`
- `03_COMMITMENT_TO_HUMANITY\COMMITMENT_TO_HUMANITY.md`
- `04_COMMITMENT_TO_ENVIRONMENT\COMMITMENT_TO_ENVIRONMENT.md`
- `05_COMMITMENTS_TO_PAST_PRESENT_FUTURE\COMMITMENTS_TO_PAST_PRESENT_FUTURE.md`
- `06_WHITELABELLING_AND_REPACKAGING\WHITELABELLING_AND_REPACKAGING.md`
- `07_ENTERPRISE_LICENSE_AND_PRICING\ENTERPRISE_LICENSE_AND_PRICING.md`
- `08_INTELLECTUAL_PROPERTY_AND_RIGHTS\INTELLECTUAL_PROPERTY_AND_RIGHTS.md`
- `09_COMPLIANCE\COMPLIANCE.md`
- `10_TECHNICAL_HANDOFF\TECHNICAL_HANDOFF.md`
- `11_TUTORIAL_DEVELOPERS\TUTORIAL_DEVELOPERS.md`
- `12_TUTORIAL_ENTERPRISE\TUTORIAL_ENTERPRISE.md`
- `13_TUTORIAL_USERS\TUTORIAL_USERS.md`
- `14_DEVELOPER_COOKBOOKS\DEVELOPER_COOKBOOKS.md`
- `15_DISASTER_RECOVERY\DISASTER_RECOVERY.md`
- `16_VULNERABILITY_MANAGEMENT\VULNERABILITY_MANAGEMENT.md`
- `17_HOW_TO_UPDATE\HOW_TO_UPDATE.md`
- `18_COMMAND_LINE_INTERFACE\COMMAND_LINE_INTERFACE.md`
- `19_SYSTEM_OF_THINGS_SOT\SYSTEM_OF_THINGS_SOT.md`
- `20_ACADEMIC_RESEARCH\ACADEMIC_RESEARCH.md`
- `21_RELATED_SCIENTIFIC_RESEARCH\RELATED_SCIENTIFIC_RESEARCH.md`
- `22_INDEPENDENT_INSURANCE\INDEPENDENT_INSURANCE.md`
- `23_HOW_TO_CITE\HOW_TO_CITE.md`
- `24_ANTICOMMONS_LICENSE\ANTICOMMONS_LICENSE.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\MILLENNIUM_PROBLEM_PROPOSALS.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\HQ_ARCHIVE\HQ_manifest.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P01\P01.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P01\P01.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P02\P02.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P02\P02.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P03\P03.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P03\P03.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P04\P04.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P04\P04.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P04\P04_HQ_solution.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P04\P04_HQ_solution.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P05\P05.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P05\P05.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P06\P06.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P06\P06.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P07\P07.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P07\P07.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P08\P08.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P08\P08.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P09\P09.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P09\P09.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P09\P09_HQ_solution.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P09\P09_HQ_solution.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P10\P10.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P10\P10.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P11\P11.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P11\P11.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P12\P12.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P12\P12.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P13\P13.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P13\P13.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P14\P14.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P14\P14.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P15\P15.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P15\P15.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P16\P16.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P16\P16.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P17\P17.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P17\P17.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P18\P18.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P18\P18.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P19\P19.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P19\P19.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P20\P20.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P20\P20.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P20\P20_HQ_solution.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P20\P20_HQ_solution.md`
- `26_INTEGRATIONS_AND_SDK\INTEGRATIONS_AND_SDK.md`
- `27_DEPENDENCIES\DEPENDENCIES.md`
- `28_TECHNICAL_WHITEPAPER\TECHNICAL_WHITEPAPER.md`
- `29_INVESTOR_MEMO\29_INVESTOR_MEMO.md`
- `30_LOI\ENTERPRISE_LOI.md`
- `30_LOI\GENERAL_LOI.md`
- `31_UNIT_ECONOMICS\31_UNIT_ECONOMICS.md`
- `32_CONTRACTS\CONTRACT_100M.md`
- `32_CONTRACTS\CONTRACT_10M.md`
- `32_CONTRACTS\CONTRACT_1M.md`
- `32_CONTRACTS\CONTRACT_5M.md`
- `32_CONTRACTS\CONTRACT_80M.md`
- `32_CONTRACTS\CONTRACT_8M.md`
- `33_COMPETITIVE_MOAT\33_COMPETITIVE_MOAT.md`
- `34_FOUNDER_PROFILE\FOUNDER_PROFILE.md`
- `35_INVESTOR_FAQ\INVESTOR_FAQ.md`
- `36_ADVISORY_BOARD\ADVISORY_BOARD.md`
- `ACADEMIC\01_Research_Use.md`
- `ACADEMIC\02_Method_And_Limitations.md`
- `anticloud\BENCH.json`
- `anticloud\CHANGELOG.md`
- `anticloud\pyproject.toml`
- `anticloud\sbom.cdx.json`
- `anticloud\.github\workflows\ci.yml`
- `anticloud\11_LICENCE_POLICY\POLICY.md`
- `anticloud\22_COMPLIANCE_FRAMEWORKS\FACTS.md`
- `anticloud\deploy\bench-entrypoint.sh`
- `anticloud\src\anticloud_ref\cli.py`
- `anticloud\src\anticloud_ref\_version.py`
- `anticloud\src\anticloud_ref\__init__.py`
- `anticloud\src\anticloud_ref\bench\compliance.py`
- `anticloud\src\anticloud_ref\bench\runner.py`
- `anticloud\src\anticloud_ref\bench\sbom.py`
- `anticloud\src\anticloud_ref\bench\__init__.py`
- `anticloud\src\anticloud_ref\crdt\convergence.py`
- `anticloud\src\anticloud_ref\crdt\gcounter.py`
- `anticloud\src\anticloud_ref\crdt\lww.py`
- `anticloud\src\anticloud_ref\crdt\orset.py`
- `anticloud\src\anticloud_ref\crdt\pncounter.py`
- `anticloud\src\anticloud_ref\crdt\__init__.py`
- `anticloud\src\anticloud_ref\deps\lock.py`
- `anticloud\src\anticloud_ref\deps\__init__.py`
- `anticloud\src\anticloud_ref\licence\classifier.py`
- `anticloud\src\anticloud_ref\licence\policy.py`
- `anticloud\src\anticloud_ref\licence\__init__.py`
- `anticloud\src\anticloud_ref\perf\harness.py`
- `anticloud\src\anticloud_ref\perf\__init__.py`
- `anticloud\src\anticloud_ref\provenance\chain.py`
- `anticloud\src\anticloud_ref\provenance\__init__.py`
- `anticloud\src\anticloud_ref\security\safeio.py`
- `anticloud\src\anticloud_ref\security\secrets.py`
- `anticloud\src\anticloud_ref\security\validators.py`
- `anticloud\src\anticloud_ref\security\vault.py`
- `anticloud\src\anticloud_ref\security\__init__.py`
- `anticloud\tests\conftest.py`
- `anticloud\tests\test_compliance_frameworks.py`
- `anticloud\tests\test_crdt_convergence.py`
- `anticloud\tests\test_crdt_gcounter.py`
- `anticloud\tests\test_crdt_orset.py`
- `anticloud\tests\test_crdt_pncounter.py`
- `anticloud\tests\test_licence_policy.py`
- `anticloud\tests\test_provenance_chain.py`
- `anticloud\tools\gen_lock.py`
- `anticloud\tools\make_docs.py`
- `anticloud\tools\run_bench.py`
- `APPENDIX\05_Plays_Well_With.md`
- `APPENDIX\06_System_Integration_Glimpses.md`
- `APPENDIX\07_Web_of_Relativity_This_Project.md`
- `BRANDING\brand.md`
- `COMMONS\01_OSS_License.md`
- `COMMONS\02_Contributor_Agreement.md`
- `COMMONS\03_Community_Standards.md`
- `COMMONS\COMMONS_LICENSE.md`
- `COMMONS\CONTRIBUTOR_GUIDE.md`
- `COMPLIANCE\01_Control_Mapping.md`
- `COMPLIANCE\02_SOC2_ISO27001_Readiness.md`
- `COMPLIANCE\03_Vulnerability_Management.md`
- `CONTRACTS\MSA\01_Master_Service_Agreement.md`
- `CONTRACTS\MSA\02_SLA_Addendum.md`
- `CONTRACTS\MSA\deployment_log_template.json`
- `CONTRACTS\MSA\DPA_TEMPLATE.md`
- `CONTRACTS\MSA\MASTER_SERVICE_AGREEMENT.md`
- `CONTRACTS\MSA\ORDER_FORM_TEMPLATE.md`
- `DEVELOPMENT\01_Build_And_Test.md`
- `DEVELOPMENT\02_Architecture.md`
- `DEVELOPMENT\03_Extension_Guide.md`
- `DEV_COOKBOOK\cookbook.md`
- `docs\00_README\README.md`
- `docs\01_INVESTOR_PACKAGE\README.md`
- `docs\02_COMMITMENT_TO_SOCIETY\README.md`
- `docs\03_COMMITMENT_TO_HUMANITY\README.md`
- `docs\04_COMMITMENT_TO_ENVIRONMENT\README.md`
- `docs\05_COMMITMENTS_TO_PAST_PRESENT_FUTURE\README.md`
- `docs\06_WHITELABELLING_AND_REPACKAGING\README.md`
- `docs\07_ENTERPRISE_LICENSE_AND_PRICING\README.md`
- `docs\08_INTELLECTUAL_PROPERTY_AND_RIGHTS\README.md`
- `docs\09_COMPLIANCE\README.md`
- `docs\10_TECHNICAL_HANDOFF\README.md`
- `docs\11_TUTORIAL_DEVELOPERS\README.md`
- `docs\12_TUTORIAL_ENTERPRISE\README.md`
- `docs\13_TUTORIAL_USERS\README.md`
- `docs\14_DEVELOPER_COOKBOOKS\README.md`
- `docs\15_DISASTER_RECOVERY\README.md`
- `docs\16_VULNERABILITY_MANAGEMENT\README.md`
- `docs\17_HOW_TO_UPDATE\README.md`
- `docs\18_COMMAND_LINE_INTERFACE\README.md`
- `docs\19_SYSTEM_OF_THINGS_SOT\README.md`
- `docs\20_ACADEMIC_RESEARCH\README.md`
- `docs\21_RELATED_SCIENTIFIC_RESEARCH\README.md`
- `docs\22_INDEPENDENT_INSURANCE\README.md`
- `docs\23_HOW_TO_CITE\README.md`
- `docs\24_ANTICOMMONS_LICENSE\README.md`
- `docs\25_MILLENNIUM_PROBLEM_PROPOSALS\README.md`
- `docs\26_INTEGRATIONS_AND_SDK\README.md`
- `docs\27_DEPENDENCIES\README.md`
- `docs\28_TECHNICAL_WHITEPAPER\README.md`
- `docs\29_INVESTOR_MEMO\README.md`
- `docs\30_LOI\README.md`
- `EDUCATORS\01_Classroom_Use.md`
- `EDUCATORS\02_Lab_Setup.md`
- `ENTERPRISE\01_Deployment.md`
- `ENTERPRISE\02_Integration.md`
- `ENTERPRISE_LICENSING\01_License_Agreement.md`
- `ENTERPRISE_LICENSING\02_Pricing_Sheet.md`
- `ENTERPRISE_LICENSING\03_Compliance_Checklist.md`
- `ENTERPRISE_LICENSING\COMPLIANCE.md`
- `ENTERPRISE_LICENSING\LICENSE_ENTERPRISE.md`
- `ENTERPRISE_LICENSING\PRICING.md`
- `Environment_Lab_Results\raw_metrics.json`
- `Environment_Lab_Results\README.md`
- `ETHICS\01_Epistemic_Gesturalism.md`
- `ETHICS\02_Positions_And_Basis.md`
- `FUNDING\01_Cost_Structure.md`
- `FUNDING\01_Funding_Brief.md`
- `FUNDING\02_Funding_Model.md`
- `FUTURES\01_Post_Quantum.md`
- `FUTURES\02_Post_Humanity.md`
- `GOVERNANCE\01_Decision_Rights.md`
- `GOVERNANCE\02_Change_Control.md`
- `II\01_Budget_Envelope.md`
- `II\02_Accounting_Outcomes.md`
- `II\03_Preprioception.md`
- `II\budget\ii_envelopes.json`
- `installer\license.md`
- `installer\loi.md`
- `installer\tauri.conf.json`
- `ISOLATED_LAB_RESULTS\01_Environment.md`
- `ISOLATED_LAB_RESULTS\01_Reproduction.md`
- `ISOLATED_LAB_RESULTS\02_Environment.md`
- `ISOLATED_LAB_RESULTS\02_Reproduction.md`
- `ISOLATED_LAB_RESULTS\03_Result_Register.md`
- `L5_L2_Classification\classification.md`
- `L5_L2_Classification\deploy_guide.md`
- `L5_L2_Classification\developer_cookbook.md`
- `L5_L2_Classification\HOW_TO_OPERATE.md`
- `L5_L2_Classification\HOW_TO_UPDATE.md`
- `L5_L2_Classification\PROTOCOLS.md`
- `LEDGERS\01_Ledger_Status.md`
- `LEDGERS\02_Export.md`
- `MARKETING\01_Positioning.md`
- `MARKETING\02_Competitive_Landscape.md`
- `MARKETING\03_Pricing_And_Competitors.md`
- `OFFICIAL_BENCHMARKS\01_FedRAMP.md`
- `OFFICIAL_BENCHMARKS\01_Index.md`
- `OFFICIAL_BENCHMARKS\02_OSINT.md`
- `OFFICIAL_BENCHMARKS\02_SOC2.md`
- `OFFICIAL_BENCHMARKS\03_OWASP.md`
- `OFFICIAL_BENCHMARKS\03_SOC1.md`
- `OFFICIAL_BENCHMARKS\04_COMPREHENSIVE_BENCHMARKS.json`
- `OFFICIAL_BENCHMARKS\04_COMPREHENSIVE_BENCHMARKS.md`
- `OFFICIAL_BENCHMARKS\04_PAX_Results.md`
- `OFFICIAL_BENCHMARKS\05_OWASP.md`
- `OFFICIAL_BENCHMARKS\06_CRDT.md`
- `OFFICIAL_BENCHMARKS\07_Provenance.md`
- `OFFICIAL_BENCHMARKS\08_ZeroTrust.md`
- `OFFICIAL_BENCHMARKS\09_Observability.md`
- `OFFICIAL_BENCHMARKS\10_SovereignMemory.md`
- `OFFICIAL_BENCHMARKS\11_DeterministicBuild.md`
- `OFFICIAL_BENCHMARKS\simulation_3seed.json`
- `OFFICIAL_BENCHMARKS\simulation_3seed.md`
- `OFFICIAL_BENCHMARKS\01_FedRAMP\01_FedRAMP.json`
- `OFFICIAL_BENCHMARKS\01_FedRAMP\01_FedRAMP.md`
- `OFFICIAL_BENCHMARKS\02_SOC2_TypeII\02_SOC2_TypeII.json`
- `OFFICIAL_BENCHMARKS\02_SOC2_TypeII\02_SOC2_TypeII.md`
- `OFFICIAL_BENCHMARKS\03_SOC1_TypeII\03_SOC1_TypeII.json`
- `OFFICIAL_BENCHMARKS\03_SOC1_TypeII\03_SOC1_TypeII.md`
- `OFFICIAL_BENCHMARKS\04_NIST_AI_RMF\04_NIST_AI_RMF.json`
- `OFFICIAL_BENCHMARKS\04_NIST_AI_RMF\04_NIST_AI_RMF.md`
- `OFFICIAL_BENCHMARKS\05_NIST_SP800_53\05_NIST_SP800_53.json`
- `OFFICIAL_BENCHMARKS\05_NIST_SP800_53\05_NIST_SP800_53.md`
- `OFFICIAL_BENCHMARKS\06_NIST_CSFW\06_NIST_CSFW.json`
- `OFFICIAL_BENCHMARKS\06_NIST_CSFW\06_NIST_CSFW.md`
- `OFFICIAL_BENCHMARKS\07_ISO_27001\07_ISO_27001.json`
- `OFFICIAL_BENCHMARKS\07_ISO_27001\07_ISO_27001.md`
- `OFFICIAL_BENCHMARKS\08_OWASP_LLM_Top10\08_OWASP_LLM_Top10.json`
- `OFFICIAL_BENCHMARKS\08_OWASP_LLM_Top10\08_OWASP_LLM_Top10.md`
- `OFFICIAL_BENCHMARKS\09_OWASP_Top10\09_OWASP_Top10.json`
- `OFFICIAL_BENCHMARKS\09_OWASP_Top10\09_OWASP_Top10.md`
- `OFFICIAL_BENCHMARKS\10_HIPAA\10_HIPAA.json`
- `OFFICIAL_BENCHMARKS\10_HIPAA\10_HIPAA.md`
- `OFFICIAL_BENCHMARKS\11_PCI_DSS\11_PCI_DSS.json`
- `OFFICIAL_BENCHMARKS\11_PCI_DSS\11_PCI_DSS.md`
- `OFFICIAL_BENCHMARKS\12_CMMC_2\12_CMMC_2.json`
- `OFFICIAL_BENCHMARKS\12_CMMC_2\12_CMMC_2.md`
- `OFFICIAL_BENCHMARKS\13_FISMA\13_FISMA.json`
- `OFFICIAL_BENCHMARKS\13_FISMA\13_FISMA.md`
- `OFFICIAL_BENCHMARKS\14_FIPS_140_3\14_FIPS_140_3.json`
- `OFFICIAL_BENCHMARKS\14_FIPS_140_3\14_FIPS_140_3.md`
- `OFFICIAL_BENCHMARKS\15_GDPR\15_GDPR.json`
- `OFFICIAL_BENCHMARKS\15_GDPR\15_GDPR.md`
- `OFFICIAL_BENCHMARKS\16_HITRUST_CSF\16_HITRUST_CSF.json`
- `OFFICIAL_BENCHMARKS\16_HITRUST_CSF\16_HITRUST_CSF.md`
- `OFFICIAL_BENCHMARKS\17_TISAX\17_TISAX.json`
- `OFFICIAL_BENCHMARKS\17_TISAX\17_TISAX.md`
- `OFFICIAL_BENCHMARKS\18_DORA\18_DORA.json`
- `OFFICIAL_BENCHMARKS\18_DORA\18_DORA.md`
- `OFFICIAL_BENCHMARKS\19_SOX_ITGC\19_SOX_ITGC.json`
- `OFFICIAL_BENCHMARKS\19_SOX_ITGC\19_SOX_ITGC.md`
