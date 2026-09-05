# CISA BOD 25-01 cloud-services engagement guide

> Original operational guidance, not Binding Operational Directive text, a cloud authorization decision, a federal applicability determination, or a compliance claim. Confirm current material through [CISA’s cybersecurity directives](https://www.cisa.gov/news-events/directives) and applicable agency, component, cloud-service, and authority direction.

## Engagement focus

For applicable Federal Civilian Executive Branch cloud-service use, maintain a governed security-practices engagement that connects cloud-service scope, shared-responsibility assumptions, accountable owners, security operating evidence, configuration and access reviews, monitoring, incidents, supplier commitments, exceptions, and improvement work. Preserve the distinction between documented service evidence and human decisions on authorization, architecture, risk acceptance, or production change.

## Roles

Assign accountable agency or component executive, cloud, security, identity, platform, application, data, procurement, supplier-management, risk, and system-owner roles. Operators maintain cloud-service inventories, responsibility records, configuration and access evidence, monitoring and incident artifacts, supplier records, exception approvals, remediation plans, review results, and closure status. Review material cloud services, ownership, security assumptions, exceptions, and open remediation quarterly; reassess after material provider, service, data, architecture, identity, or contract changes. Before annual renewal, an independent reviewer samples service records from scope through treatment evidence; auditors test the evidence trail without selecting cloud services, authorizing operation, approving production changes, accepting risk, or attesting for management.

AI may organize supplied cloud-service evidence, flag stale ownership or missing review records, relate documented services to recorded responsibilities, and draft workpapers for human review. AI cannot configure cloud services, authorize operation, approve architecture, accept risk or an exception, determine directive applicability, make a compliance conclusion, attest for management, or replace independent review.

## Source and applicability

Use the [specific directive](https://www.cisa.gov/news-events/directives/bod-25-01-implementing-secure-practices-cloud-services), its implementation guidance and required-configuration list. CISA's [ScubaConnect repository](https://github.com/cisagov/ScubaConnect) links tenant assessment and continuous reporting with BOD 25-01. Do not reduce this engagement to a general cloud-policy review. Pin the applicable tenant, cloud environment, baseline version, assessment-tool version and reporting requirements together. Current required configurations, deadlines and agency-specific instructions remain to be verified before conclusions; historical rollout dates do not restart at onboarding.

## Before starting

Apply the [agent runbook](../agent-runbook.md). Obtain tenant inventory, agency scope decision, baseline sources, assessment permissions, prior reports, reporting receipts, exceptions and change authority. Distinguish commercial and government cloud environments and provider versus tenant responsibilities. Reuse valid authorization; do not infer permission to install an application or grant tenant-wide access from permission to read an existing report.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Resolve requirements | Agency lead confirms covered tenants, applicable baseline and current reporting direction. | Source-pinned register with dates and unresolved questions. No absent baseline is silently marked compliant. |
| 2. Reconcile tenants | Cloud/procurement owners compare service, identity, contract and component inventories. | Full declared tenant population with environment, owner and lifecycle state; unused-looking tenants need verified disposition. |
| 3. Prepare assessment | Security and tenant owners select the applicable tool/version, permissions and safe execution path. | Authorized plan with target tenant identity, prerequisites and evidence destination. Unsupported settings require separate review. |
| 4. Collect actual results | Authorized operators execute approved assessment and preserve raw output, configuration, timestamp and errors. | Per-tenant result with completed, failed and unassessed checks distinct. A running schedule does not prove successful assessment. |
| 5. Review deviations | Qualified reviewer reconciles findings with baseline criteria, manual checks and contradictory evidence. | Owned deviations, unresolved interpretations and documented applicability decisions; a score alone does not establish configuration correctness. |
| 6. Remediate safely | Tenant owners prepare dependency, licensing, user-impact and recovery checks; execute approved changes after authorized QA validation. | Change receipt and actual tenant readback. New spend or expanded permissions require their approval boundary. |
| 7. Retest and report | Reviewer checks corrected settings and remaining gaps; reporting owner verifies delivery separately. | Retest plus actual reporting receipt. A local report file is not evidence that CISA received it. |
| 8. Sustain and hand off | Program lead assigns recurring execution, failure alerts, baseline-change review and independent challenge. | Evidence index, active gaps, owners and next required events. |

## Evidence and test plan

**Source and rights snapshot.** Use the official [CISA cybersecurity directives index](https://www.cisa.gov/news-events/directives) and current agency/component cloud direction at engagement start; prior locator snapshot 2026-07-31; current detailed-source review pending. This is original evidence-planning guidance, not directive text, a cloud authorization, or a determination that a service is in federal scope.

### 1. Cloud-service scope and shared-responsibility package

- **Request and owner:** Cloud, procurement, security, data, application, and system owners provide service inventories, approved use/scope records, service models, data/service classifications, accountable owners, shared-responsibility allocations, contract references, and review history.
- **Validate and limit:** Trace a selected cloud service from inventory through owner, approved purpose, responsibility allocation, supplier reference, and review date. This cannot authorize service use, interpret a contract, or establish complete cloud inventory coverage.
- **AI and trigger:** AI may compare supplied ownership and responsibility records and flag stale reviews or unresolved allocation gaps. Authorized humans decide scope, procurement, and authorization. Refresh after provider, service, data, contract, or ownership change.

### 2. Security-practice operation and change package

- **Request and owner:** Identity, cloud, platform, security-operations, application, and supplier owners provide approved baseline or configuration evidence, access reviews, monitoring/alert records, incident handoffs, change approvals, exceptions, and corrective actions.
- **Validate and limit:** Sample one documented security practice from accountable service through approved implementation or review record, monitoring/change evidence, exception or issue record, and current treatment status. This does not validate all provider controls, configure a tenant, or approve a production change.
- **AI and trigger:** AI may organize supplied evidence and flag missing access reviews, expired exceptions, or orphaned corrective actions. Humans authorize changes, evaluate incidents, and approve exceptions or closure. Refresh after material configuration, identity, incident, baseline, or supplier change.

### 3. Assurance, reporting, and improvement package

- **Request and owner:** Program leadership, risk, supplier-management, reporting, and independent-review owners provide service reviews, supplier assurance artifacts, metrics/source lineage, risk decisions, limitations, remediation follow-up, and reviewer workpapers.
- **Validate and limit:** Trace a selected reported service posture or improvement action to source evidence, accountable reviewer, documented limitation, human decision, and follow-up date. This cannot certify a cloud service, accept risk, or attest for management.
- **AI and trigger:** AI may draft evidence indexes and flag missing provenance or overdue actions. Authorized humans approve assurance conclusions, risk treatment, reporting, and external statements. Refresh before reporting, after material assurance evidence changes, and during annual independent review.


## Failure branches and decisions

Wrong tenant identity stops execution. Authentication or API failures remain failed collection, not zero deviations. Preserve skipped/manual checks and unsupported features; do not remove them from coverage to improve a score. If a baseline changes, compare affected requirements and reopen corresponding evidence. Failed user-access checks stop rollout and invoke approved recovery. Missing delivery receipts remain reporting gaps. Preserve all scorer-bound evidence without trimming, sampling or capping; inspection selections must disclose their population and limits. On interruption, save versions, tenant identity, job state and next safe action.

## Cadence and renewal

Use verified directive, baseline-update and continuous-reporting requirements. Quarterly coordination and annual review do not replace recurring assessments. Monitor actual execution and delivery failures. Recheck affected evidence after identity, provider, licensing, baseline, tool or tenant changes. Assign expiring exceptions and overdue remediation to named decision owners.

## Completion and handoff

Deliver source/scope decisions, full tenant register, baseline/tool versions, raw assessment references, manual-check coverage, deviations, changes, retests, exceptions and reporting readback. Keep sensitive configuration and credentials outside this repository. Independent source and skeptical review and named human approval remain necessary for final conclusions; assessment does not grant cloud authorization.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
