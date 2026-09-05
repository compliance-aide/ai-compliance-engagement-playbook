# CISA BOD 18-02 high-value-assets engagement guide

> Original operational guidance, not an HVA designation, system authorization, directive text or federal compliance conclusion.

## Source and applicability

Read the [original directive](https://cyber.dhs.gov/assets/report/bod-18-02.pdf), [CISA directive index](https://www.cisa.gov/news-events/directives) and current agency instructions. BOD 18-02 replaced BOD 16-01. Its first two actions cover agency coordination and inventory; additional actions concern agencies selected for assessments. Authority must verify applicability, current selection criteria, reporting channels and any later direction before execution. Do not infer formal HVA designation from an AI criticality score.

## Engagement focus

Connect the enterprise HVA register to assessment participation, findings, remediation and verified reporting. Distinguish candidates, designated assets, selected assessments and authorization decisions. These states answer different questions and must not overwrite one another.

## Roles

Agency leadership owns scope and designation decisions. Federal lead and backup contacts coordinate the program. Mission, asset, architecture and provider owners supply dependencies and evidence. Assessment teams own authorized methods and findings. The Senior Accountable Official for Risk Management (SAORM) owns required risk-management signatures. AI organizes authorized records and drafts workpapers; it cannot designate assets, authorize tests or operation, accept risk, sign or submit official reports.

## Before starting

Apply the [agent runbook](../agent-runbook.md). Obtain current agency direction, enterprise candidate/designation register, contact records, assessment selection notices, existing rules of engagement, reports, remediation records and reporting receipts. Record missing inputs and owners. Reuse valid existing authorization, but verify that the actual asset and related systems are covered. Keep sensitive HVA and architecture information in authorized storage, not this public repository.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Establish authority | Agency lead verifies source version, applicability, selection status and current reporting instructions. | Decision register separates universal agency actions from selected-assessment actions; unresolved questions have authority owners. |
| 2. Reconcile the enterprise | Mission and asset owners reconcile components, designation records and dependencies. | Complete declared population with candidate/designated state, rationale, owner and source date. A missing component remains a coverage gap. |
| 3. Prepare coordination | Program contact checks lead/backup details and approved access; reconcile prior submissions with current records. | Current contact and inventory package with receipt references. Prepared, submitted and acknowledged states remain separate. |
| 4. Prepare assessment participation | Assessment coordinator validates existing engagement documents and required asset-specific documentation with the assessing authority. | Agreed asset/related-system boundary and authorized participation record. AI does not invent testing restrictions or reinterpret authority. |
| 5. Register findings and clocks | Security lead preserves each report, receipt date, source severity and affected asset/dependencies. | Complete finding register with source-triggered deadlines and explicit unresolved classification questions. Ticket creation does not reset a report-receipt clock. |
| 6. Remediate or escalate | Owners plan and execute authorized changes; risk authority handles inability to meet the required timeline. | Observed correction and retest, or the required signed plan with milestones and interim mitigation. A plan does not mean a weakness is fixed. |
| 7. Reconcile reporting | Reporting owner traces each measure and status to the full finding population, decisions and evidence. | Review-ready report, unresolved discrepancies and approval owner. Authorized submission requires separate receipt/readback. |
| 8. Independently challenge | Reviewer checks scope, severity handling, evidence, deadlines and closure. | Handoff records disagreements, remaining actions and next due events. Assessment closure is not system authorization. |

## Cadence and renewal

From the original directive: contact review is at least annual; inventory review is quarterly, with an annual validation meeting. Selected-assessment major/critical findings trigger a 30-day remediation/notification or signed-plan path after report receipt. Plans include milestones within a one-year limit. Remaining findings require 30-day progress reports beginning 30 days after plan submission; timeline changes and full-remediation notifications require SAORM certification. Verify current authority instructions before applying these rules. Historical issuance-based startup deadlines do not restart with a new engagement.

Record trigger evidence, due date, timezone/calendar interpretation, action owner, signature dependency and submission receipt for every required event. If timing is ambiguous, preserve the earliest plausible due event for escalation while the authority resolves it; do not silently choose a later date.

## Evidence and test plan

Maintain three connected packages:

- **Candidate, designation and mission dependencies:** enterprise register, designation authority, mission rationale, component ownership, architecture and provider dependencies. Reconcile the whole declared population before tracing individual assets. Preserve candidate and designated states separately.
- **Assessment and treatment:** authorization references, report versions and receipt dates, findings, source severity, action owners, changes, interim measures, retests and exceptions. Trace each reported weakness to its asset and disposition. A closed work ticket without observed retest remains unverified; one component's correction does not prove a shared dependency is corrected everywhere.
- **Reporting and challenge:** calculation lineage, full source population, authority signatures, submission/readback, independent objections and follow-up. Reconcile totals to finding identifiers and retain contradictory evidence instead of removing inconvenient records.

Use approved assessment methods and preserve their limits. Any approved inspection selection must identify its population and cannot prove unexamined coverage. Never trim, sample or cap evidence passed to an assessment scorer. Record unavailable evidence and collection failures explicitly. Keep restricted reports in their authorized system and use protected references in internal workpapers.

## Failure branches and decisions

Missing designation authority keeps the asset a candidate or unresolved record. Missing assessment authorization blocks active testing, not authorized record preparation. A disputed related-system boundary goes to the assessing authority rather than unilateral scope reduction. Missing report-receipt evidence requires immediate deadline reconciliation. Failed retests keep findings open. Overdue actions escalate to the accountable official with exact gap and next action; no automatic exception or extension. On interruption, save source/report versions, active clocks, unresolved decisions and next safe action.

## Completion and handoff

Deliver source and applicability decisions, register and dependency map, coordination records, assessment evidence, complete findings and deadline register, signed decisions, remediation/retests, verified reporting receipts and next review dates. State remaining gaps and distinguish documentation completion from verified remediation. Independent source review and named human approval remain necessary for final conclusions and official actions.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared authority, evidence, technical-test, exception, source-change and renewal requirements.
