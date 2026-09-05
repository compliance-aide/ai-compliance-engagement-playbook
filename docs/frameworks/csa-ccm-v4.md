# CSA Cloud Controls Matrix v4 — engagement guide

> Original operational guidance, not CSA content or a cloud-assurance claim.
> Check the current [CSA CCM source](https://cloudsecurityalliance.org/research/cloud-controls-matrix)
> and its intellectual-property terms.

## Engagement focus

Map in-scope cloud services, data flows, responsibility decisions, contacts, and
assurance targets. Build responsibility and evidence narratives for material
services, distinguish provider assertions from customer-operated evidence,
monitor change and expiring assurances, exercise escalation coordination, and
reconcile cloud inventory and residual-risk decisions annually.

## Roles

Operators own configuration, vendor coordination, and evidence collection.
Independent reviewers challenge assumed responsibility splits. AI may maintain a non-authoritative
service/evidence register and draft vendor questions; it cannot decide a shared-
responsibility dispute, approve a supplier, accept risk, alter cloud configuration, or claim assurance. Monitor changes monthly, review dependencies quarterly,
and renew the supplier calendar annually.

## Source and applicability

Select the actual release from the [CCM and CAIQ v4.1 artifact page](https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix-v4-1). It identifies 207 controls across 17 domains and distinguishes the reference CAIQ inside the matrix from the separate STAR-submittable questionnaire. The general CCM landing page still describes 197 objectives; resolve this discrepancy using the retrieved versioned package before defining coverage. Do not combine old counts with new identifiers or substitute CCM Lite for a full CCM engagement.

Record matrix, implementation guidance, auditing guidance, questionnaire and mapping versions separately. Confirm use rights before importing licensed material. Determine cloud services, deployment regions, tenants/accounts, service models, data and assessment period. Mappings support further review; they do not transfer compliance conclusions across frameworks.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Name service, security, procurement and independent-review owners. Collect approved inventories and read-only evidence from the actual in-scope environments. Create one work item per control/service/responsibility boundary with expected evidence, owner, period and reviewer. Keep supplier-confidential reports in authorized storage and publish only permitted metadata.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Establish baseline | Program owner retrieves the selected official package and records edition and intended assurance route. | Versioned source register; full matrix availability before claiming complete coverage. |
| 2. Reconcile service scope | Cloud owners compare contracts, account inventory, billing/service lists and architecture. | Complete scoped service register with regions, dependencies and data flows; discrepancies assigned. |
| 3. Allocate controls | Architecture, service and procurement owners document provider, customer and shared duties. | Every matrix control has a disposition and accountable owner; no assumption that outsourcing removes customer work. |
| 4. Request evidence | Owners request implementation and operating records matched to service, period and responsibility. | Evidence register separating supplier assertions, independent reports and customer configuration evidence. |
| 5. Test operation | Independent reviewers inspect approved evidence and perform authorized QA checks against documented expectations. | Workpapers with scope, provenance, expected/observed behavior, exceptions and standard runbook results. |
| 6. Reconcile assurances | Owners compare CAIQ answers, provider reports, exclusions and customer duties against actual evidence. | Unsupported or contradictory answers retained for resolution; a report title or registry listing is not a control test. |
| 7. Correct and retest | Operational owners implement approved changes; reviewers check affected controls and dependencies. | Remediation evidence tied to the right environment and period, with historical gaps preserved. |
| 8. Review and sustain | Independent reviewers challenge coverage and management approves representations. | Scoped handoff, expiry/change watch and unresolved decisions; any STAR submission uses its own verified route and approval. |

## Failure branches and decisions

- **Provider report excludes the selected service or region:** mark the evidence mismatch; request relevant coverage instead of borrowing assurance from another offering.
- **Shared control has no customer owner:** assign the unresolved responsibility decision to service management and procurement; do not mark it inherited or not applicable.
- **Report describes required customer configuration:** verify those settings and their operation in the scoped tenant. Provider evidence cannot supply this missing customer evidence.
- **Evidence is stale after migration:** preserve the old period record and obtain evidence for the new service, region, identity and logging boundaries.
- **CAIQ says yes but testing contradicts it:** retain both records, identify the answer owner and require resolution before approved use of the questionnaire.
- **Reference questionnaire selected for submission:** prepare the correct current STAR questionnaire and record the mismatch; completing a reference workbook is not submission readiness.

## Evidence and test plan

**Source and rights snapshot.** Use the current [CSA Cloud Controls Matrix source](https://cloudsecurityalliance.org/research/cloud-controls-matrix) and applicable CSA intellectual-property terms; prior snapshot 2026-07-31; verify current release and terms. This plan is original cloud-assurance evidence guidance, not a reproduction of CCM content, a completed assessment, a provider assurance statement, or a conformance claim. Human owners approve source use, service scope, responsibility decisions, and external representations.

### 1. Cloud-service boundary, data flow, and responsibility package

- **Request and owner:** Cloud/service, architecture, security, privacy, and procurement owners provide service inventory, environment/account boundaries, data-flow references, provider/subprocessor list, customer commitments, responsibility assignments, and unresolved shared-responsibility questions.
- **Validate and limit:** Trace a selected service/data flow to its environment, provider dependency, customer boundary, responsible owner, and documented responsibility rationale. This can reveal unowned or inconsistent assumptions; it cannot settle contractual responsibility, prove all services are in scope, or make an assurance claim.
- **AI and trigger:** AI may reconcile authorized inventories and flag changed providers, missing owners, or inconsistent boundaries. Humans decide responsibility splits, contractual positions, and scope. Refresh after material service, data, hosting, provider, subprocessor, or customer-commitment changes.

### 2. Cloud-operation, configuration, and supplier-evidence package

- **Request and owner:** Cloud operations, security, platform, engineering, and supplier owners provide time-bounded configuration/change evidence pointers, identity/access records, logging/monitoring references, incident/change records, provider assurance artifacts, and evidence provenance metadata.
- **Validate and limit:** Sample a material operational assertion through source system, period, service boundary, owner, change/exception history, and where relevant provider evidence. This can support a bounded review of declared operation; it cannot establish continuous effectiveness, alter a configuration, or validate provider-operated controls.
- **AI and trigger:** AI may create a non-destructive evidence index and flag missing dates, source links, or exception approvals. Humans decide evidence sufficiency, configuration changes, supplier escalation, and remediation. Refresh monthly and after material configuration, incident, access, or provider changes.

### 3. Assurance, exceptions, and independent-challenge package

- **Request and owner:** Program, legal, security, procurement, executive, and independent-review owners provide assurance targets, exception/risk records, supplier review calendar, findings, remediation/retest records, customer statements, and skeptical-review workpapers.
- **Validate and limit:** Trace a selected exception or assurance-related statement to its evidence, approver, limitation, due date, remediation path, and independent challenge. This can test governance of an assertion; it cannot approve a supplier, accept risk, choose an assurance route, or attest externally.
- **AI and trigger:** AI may flag expiring evidence, overdue actions, or unsupported statements. Humans approve exceptions, risk treatment, supplier decisions, assessment participation, and communications. Review dependencies quarterly, before external claims, and annually for the assurance calendar.


## Cadence and renewal

Monthly change checks, quarterly dependency review and annual renewal are engagement conventions. Apply actual contract, assurance and assessment deadlines separately. Reopen affected work after service migration, new regions, supplier changes, incidents, customer configuration changes or source revisions. Track report coverage periods and missing subsequent-period evidence explicitly.

## Completion and handoff

Deliver the source register, complete control dispositions, service inventory, responsibility decisions, supplier/customer evidence, test workpapers and questionnaire reconciliation. Separate prepared, executed, reviewed and approved states. Each gap needs an owner, next action and required evidence without relying on prior chat. A complete workbook does not establish continuous control effectiveness or certification.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
