# EU AML package transition — engagement guide

> Original operational guidance, not legal advice, a suspicious-activity determination or an assessment of program adequacy.

## Source and applicability

Keep three source tracks: the current national operating baseline, the future directly applicable EU requirements, and national implementation/supervisory measures. Record instrument, version, jurisdiction, entity, activity, source paragraph, application date and approving legal owner for each obligation.

[Regulation (EU) 2024/1624, Article 90](https://eur-lex.europa.eu/eli/reg/2024/1624/oj/eng) sets general application at 10 July 2027 and 10 July 2029 for entities in Article 3(3)(n) and (o). Confirm the precise entity/activity scope rather than applying the later date to a whole corporate group.

[Directive (EU) 2024/1640, Articles 77–78](https://eur-lex.europa.eu/eli/dir/2024/1640/oj/eng) repeals Directive 2015/849 from 10 July 2027 and requires general national transposition by that date. Article 78 sets earlier dates for Article 74 (10 July 2025) and Articles 11, 12, 13 and 15 (10 July 2026), and a later date for Article 18 (10 July 2029). These are Member State transposition deadlines; an entity's operational duties require the applicable national measures and legal interpretation.

Sources checked 2026-09-04. Retrieve current amendments, technical standards, guidance and national rules before completing the obligation register. A draft consultation or future rule is not evidence that an existing duty has ended.

## Engagement focus

Build a transition plan that preserves current controls while changing customer due diligence, ownership information, monitoring, reporting decisions and record handling under the approved future baseline. Keep readiness for a future date separate from operation under today's duties.

## Roles

Legal and the money laundering reporting officer (MLRO) own applicability, interpretation and reporting decisions. Country/business owners own local execution and resources; operations owns customer and case processes; engineering/data owners own system changes and migration controls. Independent assurance reviews evidence. AI organizes authorized records and prepares procedures; humans decide customer acceptance, case closure, account restrictions, reports and external communications. Tools do not expand the agent's authority.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Obtain the legal entity/country/activity inventory, current procedures, applicable sources, customer and case populations, system interfaces, migration plan and named owners. Identify restricted case information and approved storage. Use synthetic or authorized redacted records for QA; never put customer or suspicious-activity material in this public repository.

Create one work item per entity/obligation/change. Record current rule, future rule, exact difference, affected records and systems, dependency, owner, acceptance criterion, due date and evidence location. Missing national law is an open legal dependency, not proof of no local obligation.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Establish perimeter | Legal and country owners reconcile entities, activities and jurisdictions. | Complete scope matrix with reasoned inclusions/exclusions and unresolved interpretations. |
| 2. Reconcile sources | Legal owner compares current and future requirements and national measures. | Obligation-level timeline; applicability, transposition and implementation milestones remain distinct. |
| 3. Map the change | Operations and engineering identify procedure, data, system and training effects. | Complete gap register with dependencies and accountable owners, including unchanged controls to preserve. |
| 4. Design the transition | Business/MLRO approve sequence, interim controls, cutover and recovery. | Reviewable plan showing how open customers, alerts and deadlines survive migration. |
| 5. Implement and test | Authorized teams change QA systems and execute agreed scenarios. | Versioned records, original outputs, reconciliation and documented failures. |
| 6. Challenge readiness | Independent reviewer traces requirements through configuration and actual work. | Open gaps and retests; policy approval alone cannot establish operating readiness. |
| 7. Approve cutover | Accountable owners review prerequisites and residual issues. | Named go/no-go decision and authorized implementation window; AI cannot approve account or reporting actions. |
| 8. Verify and monitor | Operations reconciles post-change populations, queues and access. | Readback of changed behavior, unresolved items with owners and next review date. |

## Transition tests to prepare

These original QA prompts test the approved implementation; legal owners supply actual thresholds, deadlines and rules.

- Customer lifecycle: use a synthetic record with incomplete ownership information. Verify the configured escalation path and absence of an unsupported “verified” result. Retain source provenance and reviewer decisions.
- Data migration: reconcile every source customer/case identifier to its destination or explained disposition. Check open-case status, evidence references, ownership, deadlines and audit history. Do not silently drop duplicates or inaccessible records.
- Monitoring change: use approved synthetic scenarios with known expected outcomes. Record scenario/configuration versions, inputs, outputs and routing. Successful job execution does not prove appropriate detection or coverage.
- Reporting readiness: simulate the internal decision and authorization path without sending a report. Distinguish draft, approved, submitted and acknowledged states; require real external receipts before claiming submission.
- Access and retention: verify the approved access matrix and record handling in QA. Do not delete live evidence to demonstrate a retention rule.

A text-only agent supplies exact requests and expected observations. A tool-capable agent executes only authorized procedures and retains tool failures separately from control results. Preserve the full evidence population; selected traces do not prove complete transition coverage.

## Failure branches and decisions

- The future EU date is used to suspend a current local control: retain the current requirement until legal approves a source-backed change.
- A national implementation measure cannot be found: assign the jurisdiction owner to resolve the source gap; classify the legal conclusion as `inconclusive`.
- A country or business activity is missing from the group plan: reopen scope and assign an owner; group policy alone does not cover the omission.
- Migration loses open cases or resets deadlines: treat the reconciliation criterion as `not_supported`; escalate and use the approved recovery path before cutover approval.
- A monitoring tool returns no alerts after a collection error: record `not_tested`; do not report zero suspicious activity.
- Ownership information conflicts: preserve provenance and route to the authorized reviewer; do not overwrite one source with the more convenient answer.
- A consultation is presented as final: record its actual status and maintain the governing baseline until the change is verified.
- A case may require urgent action: invoke the approved escalation immediately, preserving confidentiality; do not wait for the project review meeting or independently contact the customer.

## Worked handoff example

A fictional QA migration contains 12 open cases. The destination contains 11; the omitted case remains open in the source. The assertion “all open cases migrated” is `not_supported`. Engineering traces the missing identifier and tests the correction, while operations checks ownership and deadlines across all 12 cases. The agent neither closes the missing case nor determines whether it should be reported. If the source export instead failed before population reconciliation, that test would be `not_tested` and require a new authorized export.

## Evidence and test plan


**Source and rights snapshot.** Use [Regulation (EU) 2024/1624](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32024R1624), the related EU AML package material, applicable national law and supervisory direction, and qualified AML/legal review; prior snapshot 2026-07-31; verify current source status. This original transition-planning aid does not reproduce legal requirements, decide obliged-entity scope, customer due diligence, beneficial ownership, suspicious activity, filing duty, account restriction, or program adequacy. Legal/MLRO and accountable business owners confirm the transition approach and controlled handling of sensitive data.

### 1. Jurisdiction, entity, and transition-governance package

- **Request and owner:** Legal, MLRO/compliance, business, product, operations, and country owners provide a country/entity matrix, current local-baseline references, approved applicability and gap decisions, effective-date/milestone register, governance forum records, accountable owners, dependencies, and escalation paths.
- **Validate and limit:** Trace one country/entity transition entry to its approved legal/source record, owner, local baseline, milestone, gap/treatment decision, and review date. This cannot decide legal applicability, supersession, or an obliged-entity conclusion.
- **AI and trigger:** AI may maintain a source-linked milestone index and flag stale jurisdiction or owner records. Humans decide applicability, interpretation, transition priority, and risk treatment. Refresh for official/national changes, acquisition, new jurisdiction, material product/customer change, and before effective dates.

### 2. Customer lifecycle and ownership-information package

- **Request and owner:** Customer-operations, onboarding, compliance, data, product, and records owners provide approved lifecycle procedures, risk-tiering decision records, beneficial-ownership/data-source references, quality controls, review/escalation queues, retention rules, training records, and change approvals, using controlled access.
- **Validate and limit:** Sample a redacted lifecycle/change record from intake through approved procedure, data-source/provenance reference, human review/escalation, recorded disposition, and retention/access control. This does not determine customer acceptance, identity/ownership truth, required due diligence, or a legal outcome.
- **AI and trigger:** AI may identify missing metadata, route approved internal deadlines, and prepare redacted workpapers. Humans decide verification, escalation, customer treatment, and exceptions. Refresh after a procedure, data-source, risk-model, product, or material customer-segment change.

### 3. Monitoring, reporting-decision, and assurance package

- **Request and owner:** MLRO/compliance, investigations, legal, security, audit, and independent-review owners provide monitoring governance/version records, alert/case workflow evidence, escalation and reporting-decision logs, access/audit trails, quality assurance results, findings, remediation plans, and independent review workpapers.
- **Validate and limit:** Trace a selected redacted alert, scenario test, or review finding to the source record, assigned owner, human decision/escalation, limitation, corrective action, and closure follow-up. This cannot determine suspicion, require or make a report, close an alert, restrict an account, or attest to AML effectiveness.
- **AI and trigger:** AI may organize approved case metadata, identify overdue review/actions, and draft non-sensitive evidence indexes; it cannot investigate independently, file a report, or decide a case. Humans decide alert disposition, reporting, account action, risk acceptance, and external communications. Refresh after a material monitoring change, control failure, supervisory update, significant case trend, and at quarterly/annual review.


## Cadence and renewal

Review the transition at agreed milestones and before each legal or implementation date. Reopen affected work after national measures, supervisory direction, acquisitions, new activities, system changes or control failures. Continue normal operational case escalation independently of project cadence.

## Completion and handoff

Deliver the country/entity matrix, source register, current/future obligation map, complete change and population reconciliations, QA records, cutover decisions, outstanding legal questions and remediation owners. Distinguish prepared, approved, implemented and verified states. Independent source, engagement, skeptical and rights review plus named human publication approval remain required. No AML effectiveness, customer decision or reporting conclusion is established by structural completion.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for applicability, authority, evidence, testing, exceptions, source changes and renewal.
