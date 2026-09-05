# CISA Zero Trust Maturity Model Version 2 engagement guide

> Original operational guidance, not CISA model text, an architecture certification, a maturity rating, or a compliance claim. Confirm current materials through [CISA’s Zero Trust Maturity Model Version 2](https://www.cisa.gov/sites/default/files/2023-04/CISA_Zero_Trust_Maturity_Model_Version_2_508c.pdf).

## Engagement focus

Maintain a zero-trust transformation record that connects mission and service context, identity and access decisions, device and workload ownership, data and network dependencies, telemetry, implementation evidence, exceptions, remediation, and independent review. Treat the engagement as a governed operating change rather than a checklist or an automated declaration that an architecture is safe.

## Roles

Mission executives, architecture, identity, security, privacy, and operations authorities retain accountable decisions; platform and service owners preserve evidence; independent reviewers test traceability and readiness. AI may organize authorized records, identify evidence gaps, correlate approved inventories, and draft questions or workpapers, but cannot determine an agency’s target state, assign a maturity rating, approve an architecture or exception, accept risk, modify production access or services, or claim compliance. Review annually and before material identity, data, device, workload, network, supplier, incident, or mission changes.

## Source and applicability

Use the April 2023 Version 2 model, especially pages 6–10 for its structure and assessment-first approach, and the detailed pillar tables for each assessment criterion. Its five pillars are Identity, Devices, Networks, Applications and Workloads, and Data. Visibility and Analytics, Automation and Orchestration, and Governance cut across them. The stages are Traditional, Initial, Advanced, and Optimal. Pillars may advance at different speeds; dependencies still need coordination. These facts come from the official model linked above, not a vendor scorecard.

Record the actual model version, assessment boundary, agency direction, and source retrieval date. Treat policy obligations and their dates separately from maturity planning: the model's historical references do not establish today's applicable deadline. Have the accountable authority resolve current requirements before asserting compliance. A product purchase, roadmap, or single successful access test does not establish a maturity stage.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Create one work item per assessed function and scope, with source page/table reference, owner, evidence period, expected behavior, observed behavior, result and limitation. Start read-only. Keep criterion results separate from human-approved maturity judgments. Missing evidence is inconclusive; it is not automatically Traditional. Do not invent a numeric average across stages or conceal weak functions inside a pillar label.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Fix the boundary | Mission and architecture owners identify services, users, non-human identities, assets, data, external dependencies and excluded areas. | Approved scope with owners and exclusion rationale; unresolved boundaries remain explicit. |
| 2. Build the coverage register | Agent indexes every function in the adopted pillar tables, including the cross-cutting capabilities, against in-scope services. | Complete source-linked register; each unmapped item has a gap or an owner-approved applicability decision. |
| 3. Establish current behavior | Platform owners supply inventories, policy/configuration records, telemetry and existing test evidence before proposing new purchases. | Dated observations with population, collection method and access limitations; conflicting evidence remains open. |
| 4. Assess the criteria | Agent organizes evidence against the exact stage criteria; architecture and security reviewers decide the defensible maturity assessment. | Function-level rationale distinguishes implemented, operating, planned and unknown behavior; any pillar summary preserves variation. |
| 5. Set the target and dependencies | Mission leadership chooses outcomes and priorities; owners identify dependencies between identity, device posture, network enforcement, workloads and data decisions. | Approved target and sequenced plan with resources, responsible owner, measurable exit criteria and review date. No assumed mandate to reach Optimal everywhere. |
| 6. Validate an access journey | Authorized testers trace a scoped request from identity and device signals through policy decision, enforcement, data access and monitoring. Include allowed and denied cases and loss of a required signal using an approved test environment. | Expected versus observed decisions and telemetry; bypasses, stale signals and untested routes remain findings or coverage gaps. |
| 7. Correct and retest | Owners implement approved changes through change control with recovery provisions; reviewers reassess affected functions and dependencies. | Actual implementation and retest evidence, not a closed change ticket alone. Failed tests keep the affected claim open. |
| 8. Review and hand off | Independent reviewers challenge coverage and maturity rationale; accountable leadership decides target, risk and external representations. | Reviewable package of baseline, target, gaps, decisions, evidence and next actions; no automatic authorization or certification. |

## Failure branches and decisions

- A dashboard reports strong maturity but logs show stale posture inputs: preserve both records, mark the contested criterion inconclusive until resolved, and investigate collection and enforcement separately.
- An integration exists only in design documents: record planned capability, request operating evidence and avoid raising the assessed stage from intent alone.
- A legacy service cannot support the proposed control: document its boundary, dependency and compensating proposal; the risk owner decides treatment. Do not silently exclude it or change production access.
- A test cannot collect logs: record the collection failure and affected coverage. Do not convert missing telemetry into either an access-control pass or proof of a breach.

## Evidence and test plan

**Source and rights snapshot.** Use [CISA’s Zero Trust Maturity Model Version 2](https://www.cisa.gov/sites/default/files/2023-04/CISA_Zero_Trust_Maturity_Model_Version_2_508c.pdf), current agency mission and authorization context, and authorized source material; prior plan snapshot dated 2026-07-31; revalidate the adopted source and agency direction before use. This plan is original evidence-planning guidance, not copied model text, a target-state decision, a maturity rating, an authorization, or a compliance conclusion. Authorized agency officials decide architecture, scope, risk, and representation.

### 1. Mission, transformation-scope, and decision-governance package

- **Request and owner:** Mission executives, enterprise architecture, security, privacy, identity, data, and service owners provide mission/service priorities, approved transformation boundary, target-state decisions, accountable-owner roster, investment/dependency records, documented assumptions, and change-governance minutes.
- **Validate and limit:** Trace a selected transformation objective to a named authority, mission or service rationale, approved scope/decision record, dependency, and review date. This supports governed planning traceability; it cannot determine a maturity level, approve an architecture, or prove enterprise-wide scope completeness.
- **AI and trigger:** AI may organize approved decision records and flag unowned objectives, stale approvals, or conflicting inventories. Humans approve scope, priorities, target state, funding, and risk decisions. Refresh after material mission, identity, data, workload, device, network, supplier, or operating-model change.

### 2. Cross-pillar implementation and telemetry package

- **Request and owner:** Identity, endpoint, application/workload, data, network, security-operations, and platform owners provide original implementation narratives, approved architectural decisions, authorized inventory and configuration evidence, telemetry/monitoring metadata, test records, change and rollback artifacts, and documented limitations.
- **Validate and limit:** Use a human-approved method to trace one selected service or access journey through applicable identity, device/workload, data, network, and telemetry evidence, recording period, population boundary, owner, and exception. This can demonstrate bounded traceability; it cannot prove zero trust is achieved, establish effectiveness across every pillar, or authorize access or configuration changes.
- **AI and trigger:** AI may correlate authorized metadata and identify missing links, stale evidence, or unresolved inconsistencies. Humans select tests, interpret results, approve architecture and technical changes, and close corrective actions. Recollect after material access, device, workload, data-flow, telemetry, network, incident, or supplier change.

### 3. Exception, measurement, and independent-readiness package

- **Request and owner:** Governance, risk, service, and program owners provide approved exception records, compensating measures, measurement definitions and results, remediation portfolio, retest evidence, management reviews, source-change watch, and independent-review workpapers.
- **Validate and limit:** Trace a selected exception, metric, or gap from source evidence through accountable interpretation, human decision, action plan, review date, and unresolved limitation. This supports a readiness discussion; it cannot accept risk, issue a maturity rating, claim compliance, or replace independent review.
- **AI and trigger:** AI may flag expired exceptions or missing measurement inputs and prepare a non-authoritative review packet. Humans approve risk treatment, external statements, target changes, closure, and authorization; independent reviewers challenge evidence and assumptions without operating systems. Refresh after a failed test, material metric change, exception expiry, source update, or annual review.


## Cadence and renewal

Agree a review cadence with the program owner; annual review here is a planning convention, not a model-imposed universal deadline. Reassess affected functions after material identity, device, workload, data, network, supplier, incident or source changes. Preserve previous scope and results so apparent improvement cannot arise solely from a changed denominator or excluded legacy service.

## Completion and handoff

Deliver the versioned coverage register, evidence links, current-state rationale, approved target, dependency plan, tests, exceptions and unresolved decisions. State exactly which scope was assessed and which functions remain unknown or untested. The receiving agent must be able to identify the next action, its owner and the evidence needed without prior chat history. Draft completion does not imply a maturity rating has been approved.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
