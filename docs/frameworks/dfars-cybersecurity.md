# DFARS cybersecurity clauses — engagement guide

> Original operational guidance, not a CMMC certification, SPRS submission, or
> contractual representation. Verify incorporated clauses at [Acquisition.gov](https://www.acquisition.gov/dfars/subpart-204.75-cybersecurity).

## Engagement focus

Extract obligations award by award; make a human-approved applicability decision;
maintain the information/system boundary, service-provider relationships,
security posture, remediation, assessment/certification dates, and subcontract
commitments; and treat incidents, requests, and solicitations as separate,
time-sensitive tracks.

## Roles

Operators own boundary evidence, remediation, and authorized communications.
Independent reviewers distinguish evidence from assertion. AI maintains an
obligation calendar and review packets; it cannot score, certify, submit, infer
information sensitivity, or transmit incidents. Reconcile contracts, changes,
and supplier events monthly and revalidate annually.

## Source and applicability

Build an award-specific ledger from executed clauses, modifications, solicitation dates and applicable deviations. Use [252.204-7012](https://www.acquisition.gov/dfars/252.204-7012-safeguarding-covered-defense-information-and-cyber-incident-reporting.) for safeguarding/reporting analysis; do not substitute a CMMC certificate or SPRS score for contract review. Keep 7019/7020 assessment duties and 7021 CMMC duties as separate applicable tracks, using their current texts and incorporated requirements.

Contracts and security owners resolve information status, system boundary, cloud use and subcontract obligations. Record the authorized NIST edition rather than assuming the newest publication applies everywhere. Consult the [CMMC workflow](cmmc.md) for its separate current implementation-status check; a program scheduling change is not permission to disregard incorporated safeguarding duties.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Assign contracts, security, incident commander, cloud/supplier, legal and signatory owners. Keep covered information, incident evidence and proprietary contract details in authorized systems. Create work items per award/clause/system/party and preserve original dates. Establish incident escalation and reporting access before an incident; an AI preparation task cannot authorize a government report.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Extract obligations | Contracts reviews all awards, relevant modifications and deviations. | Complete clause ledger with version, trigger, owner and deadline; uncertainties assigned for interpretation. |
| 2. Map information and services | Program/security owners trace approved information categories through systems and suppliers. | Human-approved boundary covering storage, processing, transmission and operational dependencies. |
| 3. Reconcile safeguarding | Control owners map applicable requirements to implementation and operating evidence. | Full scoped requirement disposition, implementation gaps and approved treatment; no automatic compliance score. |
| 4. Verify supplier duties | Procurement and cloud owners compare contracts, actual services and required cooperation. | Evidence for provider security and incident support, customer duties and applicable subcontract flow-down. |
| 5. Prepare assessment tracks | Assessment owners reconcile system scope, official methodology and existing records. | Separate preparation, assessment, affirmation and submission states with verified dates and authority. |
| 6. Exercise incident readiness | Incident/legal owners conduct a synthetic scenario with discovery, escalation, reporting and preservation events. | Timed decision trail, access readiness and evidence-preservation plan; no real report sent by this exercise. |
| 7. Remediate and retest | Operational owners implement approved changes; reviewers verify affected obligations. | Retest evidence plus remaining historical incidents and contractual gaps; changes do not retroactively establish compliance. |
| 8. Review representations | Contracts and authorized officials reconcile claims with actual evidence and external records. | Scoped approved handoff, unresolved decisions and event-driven renewal plan. |

## Incident and cloud checkpoints

For applicable 7012 incidents, track the 72-hour discovery-based reporting clock separately from the minimum 90-day preservation period starting at report submission. Preserve affected-system images and relevant monitoring/packet captures. Do not await complete investigation before escalating reporting decisions. Isolated malicious software follows DC3 instructions, not delivery to the contracting officer. Record any additional reporting duties separately.

For external cloud handling covered defense information under 7012(b)(2)(ii)(D), verify FedRAMP Moderate-equivalent security and paragraphs (c)–(g) support. A vendor badge alone cannot establish either. Subcontract reporting must also support prompt delivery of the DoD incident number to the next higher tier where required.

## Failure branches and decisions

- **Clause edition or deviation unclear:** preserve the actual award language and request contracts review; do not silently switch baselines.
- **Incident discovery time disputed:** retain every relevant timestamp and escalate urgently; do not reset discovery to the time the legal team is notified.
- **Reporting credentials fail:** escalate through the authorized incident chain while preserving attempts and clock; a failed login is not a filed report.
- **Provider cannot preserve required evidence:** record the service-specific gap and seek contractual/technical resolution; do not assume ordinary log retention suffices.
- **Supplier claims CMMC satisfies all clauses:** reconcile each obligation separately, including reporting, cloud and assessment duties.
- **Remediation complete but official record stale:** keep implementation verification distinct from authorized record correction and external acceptance.

## Evidence and test plan

**Source and rights snapshot.** Use the current [DFARS cybersecurity subpart](https://www.acquisition.gov/dfars/subpart-204.75-cybersecurity), the applicable solicitation/award and modifications, and authorized organization records; prior snapshot 2026-07-31; revalidate incorporated versions and deviations. This plan is original operational guidance, not contract text, legal advice, a CMMC certification, an SPRS submission, an incident report, or a contractual representation. Contracts, legal, security, and authorized corporate officials decide clause applicability, information handling, notifications, submissions, and representations.

### 1. Award, clause, information-flow, and supplier package

- **Request and owner:** Contracts, program, security, information-governance, and supplier-management owners provide award/modification records, incorporated-clause ledger, stated deliverable and information-flow context, system/service-provider boundary, subcontract flow-down records, owner roster, and deadline calendar.
- **Validate and limit:** Trace one selected obligation entry to an award source, human-approved applicability rationale, affected process/system or supplier, owner, and review date. This supports factual contract-to-evidence traceability; it cannot interpret a clause, determine covered information, or decide a flow-down obligation.
- **AI and trigger:** AI may organize approved award metadata and flag changed clauses, missing owners, or stale supplier records. Humans decide applicability, information status, scope, and supplier commitments. Refresh after solicitation, award, modification, information-flow, system, or subcontractor change.

### 2. Safeguarding, assessment-readiness, and remediation package

- **Request and owner:** Security, system, control, operations, and supplier owners provide approved system descriptions, original implementation evidence, assessment/readiness records, remediation plans, milestones, evidence provenance, supplier assurance records, and change/test observations.
- **Validate and limit:** Sample a selected safeguarding or readiness assertion to an owner, dated evidence artifact, bounded system/process context, observed limitation, action plan, and retest/follow-up. This supports preparation and oversight; it cannot calculate an official score, certify implementation, or state contractual compliance.
- **AI and trigger:** AI may create read-only evidence indexes, flag missing provenance, and draft questions. Humans validate evidence, approve remediation closure, and authorize assessment communications. Recollect after failed tests, material technical change, supplier event, or remediation milestone.

### 3. Incident, request, and accountable-representation package

- **Request and owner:** Incident-response, legal, contracts, executive, and security owners provide incident/runbook governance records, authorized contact and escalation paths, time-sensitive request/notification decision records, status reviews, exceptions, risk decisions, and representation-preparation records.
- **Validate and limit:** Trace a selected scenario, decision, or exception to its source, named authority, timing record, limitation, approval path, and follow-up. This can show preparedness and governance; it cannot decide reportability, transmit an incident, accept contractual risk, submit to SPRS, or make a representation.
- **AI and trigger:** AI may flag stale contacts, deadlines, unowned exceptions, and missing decision records. Authorized humans make legal, notification, submission, risk, and external-representation decisions; independent reviewers challenge the trail. Review monthly and after an incident, request, contract change, or source update.


## Cadence and renewal

Monthly reconciliation and annual review are engagement conventions. Actual award, assessment and incident deadlines control. Reopen work after solicitation changes, awards, modifications, system or cloud changes, subcontract events and incidents. Preserve superseded records so historical representations remain traceable.

## Completion and handoff

Deliver the complete clause ledger, approved information/system boundary, supplier obligations, safeguarding evidence, assessment-state records and incident-readiness workpapers. Identify the next owner, action and evidence without prior chat. State exactly what was drafted, implemented, assessed, approved and submitted; neither preparation nor a passing sample proves contractual compliance.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
