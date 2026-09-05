# EU DORA — engagement guide

> Original operational guidance, not financial-regulatory advice. Check the
> [binding DORA regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554),
> technical standards, and local supervisor guidance.

## Engagement focus

Confirm entity and service scope and accountable management; maintain recurring
evidence around ICT risk, assets, dependencies, incidents, resilience testing,
and third-party arrangements; review material changes before commitment; and
close with board-level reporting and an owned remediation plan.

## Roles

Operators own regulated decisions, operations, contracts, escalation, and
remediation. Independent reviewers test governance credibility. AI correlates
approved assets, suppliers, incidents, tests, and open actions; it cannot decide
scope or materiality, certify tests, accept risk, or make regulated reports.


## Source and applicability

Record the financial entity, services, jurisdiction, competent authority and approved regulatory basis. Retrieve current DORA provisions, applicable implementing/delegated acts and supervisory instructions before assigning incident thresholds, deadlines, test requirements or register fields. Record each source's status and effective date. Do not treat a draft technical standard or another entity's reporting template as the governing rule.

Separate financial-entity obligations from ICT-provider oversight, ordinary resilience testing from threat-led penetration testing, and internal risk classification from regulatory incident classification. Qualified owners determine which provisions and proportionality or exemption rules apply; AI preserves the decision and evidence.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Obtain the entity/function inventory, ICT assets and dependencies, provider arrangements, risk framework, incident process, approved testing program, reporting route and management responsibilities. Reconcile the full expected population before selecting evidence traces. Keep account, contract, security and customer information in approved storage.

A text-only agent drafts exact evidence requests and expected observations. A tool-capable agent performs permitted checks with recorded targets, versions and outputs. Neither may interpret tool access as authority for disruptive testing, production changes or regulatory submissions.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Confirm perimeter | Legal and management identify entity, functions and governing provisions. | Approved applicability record and unresolved questions with owners. |
| 2. Reconcile dependencies | ICT/service owners align assets, information flows and provider arrangements. | Complete population and dependency map with missing or conflicting records identified. |
| 3. Map obligations | ICT risk and compliance translate applicable requirements into owned checks. | Full obligation/evidence ledger and specific acceptance criteria. |
| 4. Collect operating evidence | Custodians provide configurations, events, incidents and review records. | Source-linked evidence covering the stated period, including failures and retrieval limits. |
| 5. Test resilience | Authorized teams execute the applicable approved test program. | Actual service outcomes, limitations, findings and recovery evidence. |
| 6. Challenge supplier reliance | ICT risk/procurement evaluate service dependencies, contracts and continuity assumptions. | Evidence-backed decisions and open concentration/exit issues. |
| 7. Remediate and retest | Owners address defects and verify affected behavior. | Retest receipts, unchanged unresolved findings and explicit risk decisions. |
| 8. Report and renew | Management reviews the bounded outcome and next actions. | Approved internal report and separately authorized external reporting where applicable. |

## Incident work record

Capture detection, awareness, classification and reporting events separately, with timestamp, timezone, source and decision owner. Legal/incident owners supply the applicable classification method and reporting clocks. Evaluate the actual event facts against that method; do not equate an internal severity label with regulatory classification.

Track initial, intermediate and final reporting requirements under the applicable instructions, including updates and open facts. Retain draft, approval, submission and acknowledgement states separately. Escalate a possible live clock promptly. An incomplete root-cause investigation does not itself authorize delaying an earlier reporting decision. Reuse underlying incident evidence across obligations while preserving each regime's distinct trigger, recipient and receipt.

## Failure branches and decisions

- Asset and contract inventories disagree: reconcile the missing relationship and owner rather than choosing the larger-looking total.
- Provider has an assurance report but the service is excluded: preserve that scope limitation and obtain service-specific evidence.
- Backup succeeds but restoration fails: retain backup success and the adverse recovery result separately; do not report resilience from job status.
- Test infrastructure cannot execute the agreed check: record `not_tested`, the error and recovery owner.
- Incident classification lacks required facts: keep the uncertainty and escalate the decision; do not silently call it non-reportable.
- An ordinary scan is offered as threat-led testing evidence: retain what it actually tested and obtain the applicable program/method decision.
- Management accepted risk but remediation is untested: preserve the acceptance record and technical finding separately; acceptance is not a successful retest.

## Evidence and test plan


**Source and rights snapshot.** Use the current binding [DORA Regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554), applicable technical standards, and the competent authority's current guidance; prior snapshot 2026-07-31; verify current measures. This original plan is not legal advice, a materiality decision, or a regulated report.

### 1. Entity scope, ICT asset, and governance evidence

- **Request and owner:** Regulated-entity leadership, ICT risk, and service owners provide entity/service scope records, asset and dependency inventories, ownership assignments, governance minutes, risk-register references, and change approvals.
- **Validate and limit:** Trace a selected critical service or ICT dependency to a current inventory record, accountable owner, governance review, and material-change history. This establishes provenance only; it cannot decide regulated status, criticality, or materiality.
- **AI and trigger:** AI may reconcile approved inventory metadata and flag unowned assets or changes. Management and designated regulatory humans decide scope and materiality. Refresh after a material service, outsourcing, merger, or architecture change.

### 2. Resilience operations, incident, and test evidence

- **Request and owner:** ICT operations, resilience, and incident owners provide monitoring/response records, continuity and recovery exercises, test scopes and observations, incident timelines, corrective actions, and retest records.
- **Validate and limit:** Sample an incident or exercise from evidence source through owner, stated impact, test limitation, action, and closure record. This can assess traceability and cannot classify an incident, determine notification, certify resilience, or close risk.
- **AI and trigger:** AI may compile approved timelines and identify incomplete evidence. Incident, legal, and designated reporting humans decide classification, escalation, and notifications. Refresh after an incident, failed exercise, or material recovery change.

### 3. Third-party and management-review evidence

- **Request and owner:** Procurement, legal, ICT risk, and executive owners provide third-party inventories, due-diligence and contract-governance records, concentration considerations, exit/continuity plans, exceptions, leadership reporting, and action tracking.
- **Validate and limit:** Trace a selected provider relationship to owner, service dependency, review cadence, limitation, decision authority, and follow-up. This does not approve a provider, interpret regulatory duties, or accept residual risk.
- **AI and trigger:** AI may flag expiring reviews, missing owners, and overdue actions. Authorized humans approve provider decisions, risk acceptance, and regulatory representations. Review quarterly and before material outsourcing or renewal decisions.

## Cadence and renewal

Use the approved operating, test and reporting schedules and current legal requirements. Reopen affected work after major architecture, function, provider, incident or regulatory changes. Renew management reporting with both resolved and unresolved findings; do not reset overdue actions when a reporting period changes.

## Completion and handoff

Deliver the entity/source manifest, complete obligation and dependency ledgers, operating evidence, test/retest results, incident decisions, supplier/exit records and owned remediation plan. State exact blind spots and pending reviews. Independent source, engagement, skeptical and rights review plus named human publication approval remain required. Neither structural validation nor management reporting establishes regulatory compliance.

## Reconcile the register of ICT arrangements

[DORA Article 28(3)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng) requires a maintained register of all ICT contractual arrangements at entity, sub-consolidated and consolidated levels, distinguishing support for critical or important functions. It separately provides for yearly information on new arrangements, authority access to the register and timely information about relevant planned arrangements or changed function criticality. Do not reduce the register to critical suppliers or treat its maintenance as identical to one annual submission.

Use the currently applicable register templates and supervisory instructions for official fields and submission rules. The following reconciliation steps are original preparation guidance:

1. Obtain the approved reporting perimeter and complete contract/procurement, service-owner and ICT-dependency records. Record source dates and exclusions.
2. Link each arrangement to the relevant legal entities, provider, ICT services and supported functions using stable identifiers. Preserve one-to-many relationships; one provider can support multiple arrangements and functions.
3. Identify missing links, duplicate identifiers, expired-but-still-used arrangements and services without a matched contract. Resolve each through its owner; never discard it merely to pass a format check.
4. Reconcile criticality decisions with the approved function inventory. Preserve the decision owner and effective date rather than deriving criticality from supplier size or brand.
5. Validate the approved template's relationships and formats, then separately reconcile the content against source records. Schema acceptance does not establish completeness or truth.
6. Save the versioned register, unresolved discrepancies and required approvals. Any external submission needs its authorized route and receipt; local validation is not regulator acceptance.

Fictional example: one provider supports two contracts, but the register contains only the contract for the critical function. The completeness assertion is `not_supported` because the other in-scope arrangement is missing. Add its verified relationship and recheck the population; do not relabel the second function critical merely to make it eligible for the register.

## ICT third-party exit-readiness workstream

[Article 28 of DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) keeps responsibility with the financial entity when ICT services are outsourced. For services supporting critical or important functions, it requires documented, sufficiently tested and periodically reviewed exit plans. The objective includes continuity of business and client services, not merely ending the contract. Official indexed Article 28 source checked 2026-09-04; retrieve its full text and applicable technical standards before final legal assessment.

Use the [agent runbook](../agent-runbook.md). This original workstream checks the entity's approved exit assumptions; it does not decide function criticality or authorize termination.

1. **Link function to service.** Business and ICT owners identify the supported function, provider, contract, actual configuration, data, integrations and subcontractor dependencies. Legal approves the applicable classification and obligations. Keep unknown dependencies visible.
2. **Define the exit scenario.** Owners distinguish planned termination, provider failure, unacceptable deterioration and loss of access. State the approved service outcome, tolerable disruption, data requirements, target environment and available transition time. Do not assume a cooperative provider in a failure scenario.
3. **Collect the practical prerequisites.** Obtain contract/transition provisions, export formats, keys and access ownership references, alternative capacity, licenses, integration specifications, staffing, cost approvals and recovery steps. Keep secrets out of workpapers. A contract right to export is not proof that an export is usable.
4. **Prepare an authorized QA exercise.** Use synthetic or approved test data and an isolated target. Specify expected records, service behavior, timing, reconciliation and stop conditions. Do not terminate a live provider or move customer data merely to test the plan.
5. **Observe the full chain.** Trace export, transfer, import, integrity checks, permissions, integrations and the actual business-service outcome. Record every failed step and missing record. Successful download is an intermediate result, not exit success.
6. **Reconcile and challenge.** Compare expected and obtained data, functionality and timing. Check whether the alternative depends on the same failed provider or shared infrastructure. Assign owners for limitations and retests; do not discard inaccessible populations from the denominator.
7. **Approve the next decision.** The accountable business/legal owners decide whether to remediate, revise the plan or prepare a real transition. Record that decision and its evidence. Financial commitment, contractual termination, production migration and regulated communication require their existing approval gates.
8. **Maintain the record.** Reopen after contract, service, dependency, data-format, provider or function changes. Preserve the tested version and scenario so another agent can identify what remains valid.

### Fictional failed exit assumption

A QA exercise exports all named records from provider A, but provider B cannot preserve required history or enforce the approved access roles. “Export completed” can be `supported`; “the service can continue on B under the approved criteria” is `not_supported`. Keep both observations. Engineering and business owners address import/history and access behavior, then retest the affected service. Do not present a portable file as demonstrated service continuity.

### Failure and handoff rules

If export tooling fails before observation, record `not_tested` and the error. If contractual interpretation is unresolved, retain `inconclusive` for the disputed conclusion while collecting permitted technical evidence. If real provider failure creates a live service or reporting issue, invoke the approved incident route immediately instead of waiting for this exercise to finish.

The handoff includes function/service identifiers, approved scenario, source and contract references, expected/observed results, complete reconciliation, limitations, remediation owner and exact next decision. Provider assurances remain evidence inputs; they do not transfer the financial entity's accountability.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
