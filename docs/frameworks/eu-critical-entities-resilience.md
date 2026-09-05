# EU Critical Entities Resilience Directive — engagement guide

> Original operational guidance, not a designation, legal conclusion or proof of resilience.

## Source and applicability

Use [Directive (EU) 2022/2557](https://eur-lex.europa.eu/eli/dir/2022/2557/oj/eng), current amendments, national implementing law and the entity's authority notification. Record jurisdiction, sector, essential service, notification receipt and the legal owner's applicability decision. Sector membership alone does not replace designation evidence.

Article 6 sets Member State identification by 17 July 2026 and notification within one month of identification. Chapter III generally applies ten months after the entity notification; Article 12 separately requires risk assessment within nine months, when necessary thereafter and at least every four years. Articles 6 and 8 contain sector-specific treatment: verify it and national measures before assigning obligations. These clocks are not one universal company deadline.

Articles 12–13 address natural and human-caused risks, cross-sector/border dependencies, proportionate measures, resilience planning and a liaison officer. Existing documents may contribute, but do not automatically prove complete coverage. Source check: 2026-09-04; national implementation and entity-specific applicability remain engagement prerequisites.

## Engagement focus

Trace each essential service through facilities, people, technology, utilities, suppliers and recovery arrangements. Connect risk assumptions to implemented measures and observed exercise results. Preserve the distinction between having a continuity plan and being able to restore a service.

## Roles

Legal owns interpretation and designation response. Executive/service owners approve priorities and resources. Resilience, safety, facilities, security, operations and supplier teams maintain evidence. The liaison coordinates approved authority interactions. Independent reviewers challenge assumptions and test records. AI organizes evidence and drafts procedures; authorized tools may support safe QA. Humans decide crisis actions, risk acceptance, notifications, physical tests and public conclusions.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Obtain authority notices, local rules, service/dependency inventory, risk assessments, recovery objectives, plans and named owners. Restrict infrastructure maps, vulnerabilities and contact details to approved storage. Define safe exercise boundaries, stop conditions, observers and recovery authority; do not interrupt essential services to manufacture evidence.

For every assertion record its source, owner, service, dependency, period, evidence and expected observation. Text-only agents prepare exact requests; tool-capable agents record authorized procedures and outputs. Missing evidence remains an explicit gap.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Establish authority | Legal reconciles national law, notification and service boundary. | Approved applicability record and separately calculated obligation dates. |
| 2. Map dependencies | Service owners reconcile every in-scope service and upstream/downstream dependency. | Full map with owners, alternatives and unverified assumptions. |
| 3. Assess risks | Resilience team uses relevant national information and local scenarios. | Source-linked risk record covering relevant hazards and cascading effects. |
| 4. Plan measures | Owners link risks to prevention, protection, response and recovery work. | Implemented/planned distinction, accountable actions and supporting records. |
| 5. Exercise safely | Authorized teams execute agreed scenarios and collect observations. | Timeline, service outcomes, dependency behavior, limitations and failed steps. |
| 6. Correct and retest | Owners address failed assumptions and implementation defects. | Fresh evidence for affected assertions; meeting minutes alone do not close a failed recovery test. |
| 7. Prepare escalation | Liaison/legal validate reporting triggers, contacts and approval paths against current local rules. | Tested internal routing and reviewable notification packet; no unauthorized external send. |
| 8. Handoff and renew | Sponsor reviews gaps and the next operating cycle. | Named decisions, remediation owners, deadlines and change triggers. |

## Failure branches and decisions

- Notice receipt date is missing: retrieve the authority record and obtain legal calculation; do not guess from the EU identification deadline.
- A generic IT recovery plan is supplied: map remaining people, facility, physical and supplier dependencies rather than calling it full resilience coverage.
- Two alternate suppliers depend on the same site or utility: retain the shared failure and reassess the claimed independence.
- Exercise restores technology but not the essential service: classify the service criterion from its actual outcome; technical restart alone is insufficient.
- Test tools fail before observing recovery: record `not_tested` with the error and recovery owner.
- A reportable incident may have occurred: invoke the approved incident/legal escalation immediately; quarterly reviews do not govern urgent notification decisions.
- Existing NIS2 or sector evidence is offered as automatic equivalence: map its exact coverage and obtain the legal/authority decision where required.

## Worked handoff example

A fictional tabletop assumes an alternate site can sustain the essential service during a power outage. Both sites rely on the same unavailable utility feed. The assertion of independent power continuity is `not_supported` by the dependency record. Facilities identifies a viable alternative and the service owner commissions a safe follow-up exercise. Actual restored service remains `not_tested` until observed; discussion of a backup does not demonstrate recovery.

## Evidence and test plan


**Source and rights snapshot.** Use [Directive (EU) 2022/2557](https://eur-lex.europa.eu/eli/dir/2022/2557/oj/eng), applicable national transposition, competent-authority direction, and qualified legal review; prior snapshot 2026-07-31; verify current national measures. This original planning aid does not reproduce the Directive, determine designation or scope, set a resilience standard, or make a notification or compliance conclusion. Counsel and designated accountable owners confirm legal status and evidence handling.

### 1. Entity, essential-service, and dependency package

- **Request and owner:** Executive, legal, resilience, operations, service, facilities, IT, procurement, and supplier owners provide jurisdiction/entity records, designated-service decisions where made by the competent authority or counsel, essential-service descriptions, dependency maps, alternate-provider assumptions, owner assignments, and review history.
- **Validate and limit:** Trace one declared essential service to the source designation/applicability record, service owner, critical dependencies, alternate arrangements, and review date. This cannot determine designation, essentiality, national applicability, or supplier sufficiency.
- **AI and trigger:** AI may reconcile authorized inventories and flag missing dependency/owner links. Humans decide applicability, designation response, service priority, and investment/risk choices. Refresh after jurisdiction, entity, service, location, ownership, or material dependency changes.

### 2. All-hazards risk, continuity, and exercise package

- **Request and owner:** Resilience, security, safety, facilities, operations, and service owners provide approved risk assessments, continuity and recovery plans, crisis roles/contact records, exercise scenarios and observations, restoration/dependency evidence, corrective actions, and exception records.
- **Validate and limit:** Sample an exercise or disruption scenario from approved scope through participating owners, dependency assumptions, observed result, recovery decision, action owner, and retest evidence. This does not prove operational resilience, establish a required protection level, or approve a crisis decision.
- **AI and trigger:** AI may assemble scenario packets and identify stale contact, test, or action records. Humans approve scenarios, risk treatment, service-restoration priorities, and exceptions. Refresh after an exercise, significant disruption, supply interruption, material facility/technology change, or quarterly review.

### 3. Liaison, incident, and improvement-readiness package

- **Request and owner:** Legal, liaison, incident, communications, resilience, and independent-review owners provide authority-contact records, notification decision logs, incident/cross-border coordination records, communications approvals, lessons learned, metrics sources, and remediation follow-up.
- **Validate and limit:** Trace a selected incident or reporting exercise to source evidence, accountable liaison, escalation/decision record, communication approval, limitation, and corrective action. This cannot decide reportability, notification timing/content, or make an authority representation.
- **AI and trigger:** AI may track action dates, draft internal workpapers, and flag missing provenance; it cannot submit reports or contact authorities. Humans decide reporting, external communications, risk acceptance, and closure. Refresh after an incident, authority change, significant exercise outcome, or annual independent review.


## Cadence and renewal

Use entity-specific legal dates alongside the agreed operating review cadence. Reopen assessments after designation, service, facility, supplier, threat or incident changes and after adverse exercises. Track risk-assessment refresh separately from exercise schedules; do not treat a statutory outer interval as permission to ignore material change.

## Completion and handoff

Deliver the source/notification record, scope and dependency map, complete risk/measure ledger, exercise results, unresolved assumptions, retest actions and current liaison/escalation procedures. State which service outcomes were observed and which remain untested. Independent source, engagement, skeptical and rights review plus named human publication approval remain required. No designation, compliance, resilience or notification claim follows from structural completion.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for applicability, authority, evidence, testing, exceptions, source changes and renewal.
