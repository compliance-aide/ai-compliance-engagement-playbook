# CIS Benchmarks program engagement guide

> Original operational guidance, not CIS Benchmark content, a product configuration instruction, a license interpretation, or a compliance claim. Confirm current versions, permissions, and authorized source material through [CIS Benchmarks](https://portal.cisecurity.org/benchmarks); do not copy licensed benchmark text into this repository or an AI prompt.

## Engagement focus

Operate a controlled baseline program for products and services covered by CIS Benchmarks. Connect each authorized benchmark version to applicable technology, environment, owner, tailoring decision, implementation evidence, validation results, exceptions, remediation, and version-refresh record. Treat a benchmark result as assessment input rather than proof that a system is secure, suitable for its business use, or authorized for production.

## Source and applicability

Use the authorized product-specific benchmark and the public [CIS FAQ](https://www.cisecurity.org/cis-benchmarks/cis-benchmarks-faq) and [CIS-CAT reporting documentation](https://ciscat-assessor.docs.cisecurity.org/en/latest/ReportHTML/) for program context. Source check: 2026-09-04. Profiles and assessment coverage differ; some checks require manual review, including checks unsupported by the selected tool. A scan percentage is therefore not proof of complete assessment. Confirm product release, benchmark edition, profile and tool support together.

Source owners confirm access and usage rights before any protected-content processing. This repository retains original process guidance and metadata, not licensed recommendation text, mappings or scored reports. A stronger-sounding profile is not automatically suitable: assess compatibility and business impact before approval.

## Roles

Platform owners establish technology scope and operating needs. Security/configuration owners propose baseline decisions. Source/procurement owners establish permitted use. Change authorities approve implementation; risk owners approve exceptions; reviewers verify results independently. AI indexes permitted metadata and flags gaps. It cannot choose final tailoring, interpret license terms, run scans or alter systems under this guide.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Record product/release, asset population, environment, benchmark/version/profile, assessment tool/version, owner, inputs, output and exit check. Require source authorization, approved baseline and test/change permissions. Missing records remain dependencies. Never place protected benchmark material in chat or this repository.

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Reconcile technology | Platform owners compare the asset population with actual products, roles, versions and environment boundaries. | Inventory with unmatched or unsupported technology explicitly recorded. |
| 2. Select authorized baseline | Security/platform owners confirm applicable benchmark edition/profile, rights and organization-approved deviations. | Versioned applicability record; profile selection and exceptions have named approvers. |
| 3. Plan complete validation | Assessment owners reconcile the approved baseline with automated coverage, manual checks and inaccessible assets using permitted references. | Coverage register; unsupported/manual/error states do not become passes. |
| 4. Establish pre-change evidence | Authorized assessors provide run metadata and permitted result references for the approved population. Reviewer confirms correct targets, tool/version and completeness. | Baseline workpapers with missing coverage and failures retained. |
| 5. Test proposed treatment | Implementers use separately approved QA changes and rollback plans. Reviewers check both intended configuration and service functionality. | QA result and compatibility/rollback evidence; no automatic production rollout. |
| 6. Implement and retest | Authorized change owners execute approved changes through release controls. Reviewers inspect actual target state and new validation evidence. | Change-to-retest trail; merge, deployment message or template value alone is insufficient. |
| 7. Govern exceptions | Risk/platform owners decide each unresolved deviation with scope, rationale, mitigation and review date. | Recorded exception with its actual boundary; accepted risk is not a passing technical check. |
| 8. Monitor drift and versions | Owners evaluate new product/benchmark/tool versions, changed assets and drift; reassess affected coverage before updating the baseline. | Owned migration queue preserving historical versions and results. |

## Evidence and test plan

These original examples do not reproduce benchmark content. Use the complete approved coverage register; preserve all authorized evidence supplied to an assessment scorer without trimming.

| Package and owner | Verification | Limitation |
| --- | --- | --- |
| Applicability — platform/source owner | Trace an asset to release, environment, authorized benchmark/profile and approval. Reconcile inventory discrepancies. | A similar product name does not establish version compatibility. |
| Validation — assessor | Match run metadata to population, permissions, tool coverage and manual-review status. | A completed job may contain errors, exclusions or unassessed checks. |
| Remediation — change owner/reviewer | Follow proposed treatment through QA functionality, approval, actual implementation and retest. | Configuration compliance alone does not prove service availability or overall security. |
| Exception — risk owner | Compare deviation scope with approval, mitigation, expiry and current target state. | An exception for one asset cannot silently cover an entire fleet. |
| Version change — baseline owner | Reconcile revised baseline coverage with affected assets and validation methods using authorized source references. | A newer tool does not necessarily assess the selected benchmark edition fully. |

Workpapers retain permitted identifiers, source location, date, period, target, tool/version, expected/observed status, limitation, reviewer and next action. Keep protected results at their authorized location. State selected test populations and untested coverage separately.

## Failure branches and decisions

- **No matching benchmark or permission:** record the exact product/version or rights gap; do not substitute another edition or bypass access controls.
- **Manual, error or unavailable result:** route to the appropriate assessor and preserve its state. Never count it as passed because the scan finished.
- **Wrong target or inadequate privilege:** invalidate affected conclusions and request a correctly authorized assessment; do not escalate privileges without approval.
- **QA service regression:** stop the proposed rollout and route remediation/rollback to the change owner.
- **Drift after remediation:** reopen the finding and investigate the configuration source rather than repeatedly patching an overridden setting.
- **Expired exception:** escalate to the risk owner; do not renew or broaden it automatically.
- **Interrupted run or uncertain change:** preserve run identifiers, versions and last observed state. Verify the target and job status before retrying.

## Cadence and renewal

Owners set review intervals according to asset risk, release/change activity and exception dates. Quarterly or annual checks are internal program choices, not universal CIS certification deadlines. Reassess after material product, baseline, tool, provider, incident or architecture changes.

## Completion and handoff

The review packet includes the full asset population, approved baseline/version/profile, rights record, complete validation dispositions, manual-review gaps, changes, retests and exceptions. Mark omissions. Production implementation is a separate authorized milestone with actual-state verification. Handoff gives next action, owner, due date and dependency; do not claim certification or overall security from a benchmark result.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared applicability, authority, evidence, technical-test, exception, source-change and renewal requirements.
