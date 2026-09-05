# DISA STIG program engagement guide

> Original operational guidance, not STIG or Security Requirements Guide text, an authorization-to-operate decision, a production-change authorization, or a compliance claim. Confirm current material through the [DISA STIG program](https://public.cyber.mil/stigs/) and applicable DoD, component, system-owner, and authorization direction.

## Engagement focus

Maintain a release-aware technical-hardening engagement that connects applicable Security Technical Implementation Guides and Security Requirements Guides to owned technology, approved baselines, implementation evidence, assessment findings, exceptions, remediation, and change control. Record the actual version and scope used for each environment. Treat a benchmark result, automation output, or documented exception as evidence for accountable review—not as an authorization, risk acceptance, or confirmation that a system is suitable for its mission.

## Roles

Assign accountable system-owner, security, platform, network, application, configuration-management, assessor, authorizing-official support, change-management, and supplier-management roles. Operators maintain technology inventories, applicable guidance/version decisions, baseline and implementation evidence, assessment results, exception and remediation records, test evidence, release-monitoring records, supplier evidence, and approved change records. Review published releases, material technology changes, open findings, and exceptions quarterly; reassess in scope when relevant guidance, system scope, or architecture changes. Before annual renewal, an independent reviewer samples guidance selection through closure evidence; auditors test the evidence trail without authorizing operation, approving production changes, accepting risk, or attesting for management.

AI may organize supplied applicability, assessment, and remediation evidence, flag stale release reviews or missing ownership, and draft workpapers for human review. AI cannot change systems, determine an authorization decision, approve an exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.

## Source and applicability

Select current authorized STIG/SRG packages through [Cyber Exchange](https://www.cyber.mil/stigs/), matching product, version, role and environment. Record package version/release, publication date and approved baseline date separately. Retrieve overview, revision history, manual checks and applicable automation; never infer that a scanner covers the entire guide. The [DISA GPO page](https://public.cyber.mil/stigs/gpo/) warns that GPO and STIG publication dates can differ, so a downloaded policy bundle must be reconciled with the selected baseline.

System owners and assessors decide applicability under governing component and authorization direction. Keep draft guidance, approved baselines and candidate upgrades distinct. A vendor implementation guide or third-party mirror is not a substitute for verifying the official package and its scope.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Identify assets, product versions, management boundaries and dependencies. Establish read-only assessment authority, credential handling, approved QA change scope and recovery access. Create one work item per rule/asset or justified asset cohort. Record exact rule identity and release; similar titles do not prove equivalent requirements. Preserve original result files in approved storage with complete rule coverage.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Establish scope | System/platform owners reconcile assets, roles and approved guide selections. | Full asset-to-baseline register with unsupported products and unknown versions assigned. |
| 2. Reconcile rules | Assessor compares the complete selected manual guide with automation and prior results. | Every rule has an evaluation method; new, changed and removed rules receive explicit treatment. |
| 3. Verify collection readiness | Operators confirm tool/benchmark compatibility, access and targeted asset identity. | Recorded execution context and credentials scope; failed access cannot generate a successful assessment. |
| 4. Assess and inspect | Authorized reviewers run approved checks and complete manual evaluations. | Rule-level evidence, time, asset and observed outcome; automation errors and untested rules remain visible. |
| 5. Resolve findings | Assessor reviews contradictions and evidence sufficiency against the selected check procedure. | Human-reviewed checklist results, with runbook work states separate from official finding classifications. |
| 6. Plan changes and exceptions | Owners assess operational impact, dependencies, recovery and any required risk decision. | Approved remediation or documented exception request with scope/expiry; neither request nor acceptance changes the observed technical condition. |
| 7. Retest applied changes | Operators verify resulting configuration and reviewers repeat affected checks. | Evidence from the actual asset after required restart/policy application, plus mission-function regression checks. |
| 8. Review and maintain | Independent reviewer challenges completeness and outstanding issues. | Versioned checklist, exceptions, change evidence and renewal triggers; authorization remains a separate decision. |

## Failure branches and decisions

- **Scanner reports no findings after authentication failure:** record collection failure and untested rules; do not report zero vulnerabilities.
- **Automation omits a rule:** assign manual evaluation or an explicitly untested result; absence from output is not non-applicability.
- **Imported results use another release:** reconcile rule changes and preserve original provenance; do not copy statuses by title alone.
- **GPO configured but setting ineffective:** verify effective policy, conflicts and relevant runtime state; policy intent cannot close a failed check.
- **Hardening breaks required service behavior:** stop further QA rollout, invoke approved recovery and escalate the implementation/risk tradeoff.
- **Exception expires:** reopen the decision and preserve the actual finding; an old waiver is not perpetual approval.

## Evidence and test plan

**Source and rights snapshot.** Use the official [DISA STIG program](https://public.cyber.mil/stigs/), applicable authorized guide/version access, and controlling DoD, component, system-owner, and authorization direction; prior snapshot 2026-07-31; verify current release and access terms. STIG and SRG materials may have controlled distribution or use conditions. This guide stores only original evidence objectives and organization-created records—not guide text, check content, automated results beyond approved metadata, or mappings. Humans confirm source rights, applicability, release use, exceptions, production changes, and authorization decisions.

### 1. Technology inventory, guidance-selection, and baseline package

- **Request and owner:** System, platform, network, application, configuration-management, and security owners provide approved technology inventories, environment/use context, guidance/version selection records, baseline ownership, source-access/right confirmations, dependency records, and documented applicability assumptions.
- **Validate and limit:** Trace one selected technology instance to its owner, environment, approved guidance/version-selection record, baseline reference, and review date. This supports selection traceability; it cannot determine applicability, reproduce a requirement, or approve an implementation baseline.
- **AI and trigger:** AI may correlate authorized inventory metadata and flag version drift or missing owners. Humans confirm guidance selection, source rights, and baseline applicability. Refresh after a technology, environment, architecture, source-release, or mission change.

### 2. Implementation, assessment, and remediation package

- **Request and owner:** Platform, application, security, assessor, and operations owners provide approved configuration/implementation references, change records, authorized assessment metadata, test observations, findings, remediation plans, milestones, retest evidence, and documented constraints.
- **Validate and limit:** Trace a selected finding or asserted implementation to a dated organization-created artifact, owner, bounded asset population, observation, limitation, corrective action, and retest/follow-up. This can support technical evidence review; it cannot create a benchmark result, prove every setting, or state compliance.
- **AI and trigger:** AI may index approved artifacts, flag missing evidence links, and prepare questions. Humans select assessment methods, interpret results, approve changes, and authorize closure. Recollect after a failed test, release, material change, or remediation milestone.

### 3. Exception, change-control, and authorization-support package

- **Request and owner:** System, risk, change-management, security, authorization-support, and supplier-management owners provide approved exception records, compensating-measure evidence, risk/decision records, supplier evidence, production-change approvals, review dates, and independent-review workpapers.
- **Validate and limit:** Trace one selected exception or change from source evidence through named authority, scope/expiry, approved action, and follow-up. This supports accountable governance; it cannot approve an exception, accept risk, authorize production, or issue an authorization decision.
- **AI and trigger:** AI may flag expired exceptions, unreviewed changes, and missing decision provenance. Humans approve exceptions, risk treatment, production changes, and authorization actions; independent reviewers test the evidence trail without exercising those authorities. Review quarterly and after exception expiry, material change, source update, or incident.


## Cadence and renewal

Quarterly and annual review intervals are engagement conventions; governing deadlines and release direction take precedence. Reassess changed rules and affected assets after guide releases, product upgrades, image changes, policy changes or incidents. Track stale evidence and new assets separately from existing compliant configurations.

## Completion and handoff

Deliver the asset/baseline register, complete rule-method coverage, source results, manual evidence, reviewed checklist, remediation/retests and exception decisions. Preserve unknown, untested and failed-collection states. Name each next owner, action and evidence requirement without earlier chat. A green automation summary cannot establish complete STIG compliance or authorization to operate.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
