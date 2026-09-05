# CISA BOD 19-02 internet-accessible remediation engagement guide

> Original operational guidance, not a remediation order, production-change authorization or compliance conclusion.

## Source and applicability

Read the [original directive](https://www.cisa.gov/sites/default/files/bod-19-02.pdf), [directive page](https://www.cisa.gov/news-events/directives/bod-19-02-vulnerability-remediation-requirements-internet-accessible-systems) and current agency direction. **Historical directive:** [BOD 26-04, issued June 10, 2026](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk), explicitly revoked BOD 19-02 and BOD 22-01. Use this guide to reconcile historical records and migrate ongoing work to current authority, not to apply BOD 19-02 as a current mandate. Verify BOD 26-04 phase applicability, implementation guidance and agency instructions before assigning current deadlines. Preserve historical records under their original source version.

The original directive concerns critical/high findings from Cyber Hygiene scanning and includes scope/access maintenance. This is not a generic authorization to scan internet systems. Current scanning arrangements, source addresses, reporting channels, severity interpretation and deadlines must be confirmed from authorized direction rather than copied from an old contact address.

## Engagement focus

Reconcile the exposed asset population, preserve vulnerability observations and their timing, assign accountable treatment, verify correction and reconcile reporting. Keep discovered, confirmed, planned, changed and independently retested states distinct.

## Roles

Agency authority resolves applicability and reporting. Asset and network owners maintain scope. Vulnerability analysts validate observations. Service and change owners implement authorized treatment. Risk authority decides exceptions. Independent reviewers challenge closure. AI may organize authorized records and draft work items; it cannot authorize scans, change systems, accept risk or submit official reports.

## Before starting

Apply the [agent runbook](../agent-runbook.md). Obtain current direction, scan agreement, approved inventory, reports, source timestamps, owner map, prior findings and change/exception records. Reuse valid authorization within scope. Missing authority blocks affected decisions; authorized evidence organization may continue.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Resolve controlling source | Agency authority checks current directive status and any transition instructions. | Source/version decision, requirements and clocks; unresolved applicability remains explicit. |
| 2. Reconcile scan coverage | Network and asset owners compare public address inventory, hosted services, agency boundaries and approved scanner coverage. | Full declared population with owners and gaps. A blocked scanner is not evidence that a service is safe. |
| 3. Register observations | Vulnerability team retains report date, first observation, affected endpoint, source severity and evidence. | Traceable findings without resetting age during ticket migration or deduplication. |
| 4. Validate and prioritize | Qualified analyst checks affected product/service, contradictory evidence and current authority criteria. | Supported finding, documented false-positive decision or unresolved state; source severity remains preserved separately. |
| 5. Plan treatment | Service owners identify prerequisites, provider dependencies, acceptance and rollback under change control. | Owned work items and source-based due dates. Missing current timing rules escalate rather than produce invented grace periods. |
| 6. Execute and verify | Authorized operators test in approved QA, execute approved changes and independently observe the resulting endpoint state. | Change and retest evidence tied to the original finding. A successful installer or closed ticket alone cannot prove correction. |
| 7. Decide exceptions and report | Risk/reporting owners reconcile unresolved findings, approved decisions and source populations. | Signed decisions where required, review-ready report and separate actual submission/readback receipts. |
| 8. Renew coverage | Independent reviewer challenges inventory gaps, aging findings and closure evidence. | Handoff with remaining actions, owners and next verification events. |

## Evidence and test plan

**Source and rights snapshot.** Use the official [CISA BOD 19-02 page](https://www.cisa.gov/news-events/directives/bod-19-02-vulnerability-remediation-requirements-internet-accessible-systems) and applicable agency/component direction at engagement start; prior locator snapshot 2026-07-31; current applicability unresolved as described above. This original plan does not reproduce directive requirements, determine an internet-exposed scope, order remediation, or make a compliance conclusion.

### 1. Internet-accessible scope and discovery package

- **Request and owner:** Asset, network, cloud, application, and vulnerability-management owners provide approved internet-accessible asset inventories, discovery-source descriptions, owner/service links, exposure-review records, timestamps, known gaps, and scope decisions.
- **Validate and limit:** Independently trace a selected recorded asset from inventory through discovery source, public-service/dependency record, accountable owner, last review, and documented inclusion or exclusion rationale. This cannot prove complete external discovery, determine exposure, or authorize scanning.
- **AI and trigger:** AI may reconcile supplied asset records and flag missing owners, stale discovery, or unexplained population variance. Authorized humans decide scope and authorize technical activity. Refresh after new exposure, acquisition, decommissioning, provider or network change, and quarterly review.

### 2. Vulnerability prioritization and controlled-remediation package

- **Request and owner:** Vulnerability-management, system, security, and change owners provide vulnerability observations, affected-asset links, human prioritization records, treatment tickets, due dates, dependency notes, change approvals, test results, and rollback records.
- **Validate and limit:** Sample one remediation path from source observation through affected asset, human priority/treatment decision, assigned owner, approved change, validation evidence, and current status. This does not validate severity, require a remedy, or authorize production change.
- **AI and trigger:** AI may identify missing handoffs, aging actions, or absent validation records. Humans determine prioritization, approve changes, and close remediation. Refresh after a new observation, missed treatment date, failed test, or material asset/software change.

### 3. Exception, validation, and reporting-readiness package

- **Request and owner:** Risk, security governance, reporting, and supplier-management owners provide exception requests, compensating actions, human approvals, expiry/review dates, validation or retest evidence, reporting inputs, supplier dependencies, and escalation records.
- **Validate and limit:** Trace a selected exception or claimed closure from decision basis through approval, limitation, compensating action, review/retest record, accountable owner, and present status. This cannot accept risk, certify remediation effectiveness, or submit an agency report.
- **AI and trigger:** AI may flag expiring exceptions and reconcile supplied report values to source references. Authorized humans approve exceptions, reports, and external statements. Refresh after exception expiry, failed retest, report-period close, or annual independent review.


## Failure branches and decisions

Reconcile the full declared evidence population before any approved inspection selection. Record selection limits; a selected trace cannot prove complete coverage. Never trim, sample or cap evidence sent to an assessment scorer. Preserve collection errors, unscanned assets and conflicting observations. If a test fails or service degrades, stop expansion and follow the approved recovery plan. If ownership or provider responsibility is missing, assign escalation and retain the finding. Expired exceptions do not renew automatically. On interruption, save versions, original timestamps, active clocks and next safe action.

## Cadence and renewal

Use verified controlling-source deadlines and agency reporting requirements. Quarterly coordination and annual independent review are optional management rhythms, not substitutes for vulnerability treatment or scope-change obligations. Reopen relevant checks after exposure, address ownership, software, provider, network or threat changes. Do not restart a finding's clock because a new agent or reporting period begins.

## Completion and handoff

Deliver source-status decision, asset/scan coverage register, original observations and timestamps, validation decisions, treatment and retest evidence, exceptions, reporting receipts and next due events. Report blind spots alongside results. Current source verification, independent review and named human approval remain required before final conclusions or official reporting.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared authority, evidence, technical-test, exception, source-change and renewal requirements.
