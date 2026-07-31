# NIST SP 1800-26 ransomware detection-and-response engagement guide

> Original operational guidance, not NIST practice-guide text, an incident command, a technical containment instruction, a legal interpretation, or a compliance claim. Confirm current material through [NIST SP 1800-26](https://csrc.nist.gov/pubs/sp/1800/26/final) and the organization’s approved incident-response, legal, insurance, customer, and authority direction.

## Engagement focus

Maintain evidence that material data-integrity events can be detected, assessed, contained, investigated, and handed over to recovery using accountable operational procedures. Connect critical data and services to telemetry, integrity signals, detection coverage, triage records, escalation paths, containment authorities, investigation records, communications, recovery handoffs, and lessons learned. Treat the practice guide as a structured way to test detection and response capabilities; do not treat monitoring tools, AI summaries, or playbook existence as an operational decision or proof that an event was handled appropriately.

## Roles and annual rhythm

Assign accountable executive, security-operations, platform, application, data, incident-command, legal, communications, insurance, business-continuity, supplier-management, and service-owner roles. Operators maintain detection and logging coverage, integrity-monitoring evidence, alert and triage records, escalation and contact records, incident artifacts, containment approvals, investigation handoffs, communications records, recovery transitions, supplier evidence, and remediation status. Review material coverage and escalation assumptions quarterly; exercise representative detection-to-response paths at least annually and after material service, telemetry, supplier, or threat changes. Before annual renewal, an independent reviewer samples alerts, triage, escalation, and exercise records; auditors test the evidence trail without directing containment, deciding notification or payment, accepting risk, or attesting for management.

AI may organize supplied alert and case evidence, flag gaps in ownership or escalation records, correlate documented events with affected services, and draft workpapers for human review. AI cannot direct containment, alter production safeguards, determine the severity of an event, make notification or payment decisions, determine legal obligations, make a compliance conclusion, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** Retain the retrieved version and applicable use terms for the official [NIST SP 1800-26 publication record](https://csrc.nist.gov/pubs/sp/1800/26/final) with approved incident-response, legal, insurance, customer, authority, and operational direction. This original plan does not reproduce NIST material, direct response, or make a conformance claim.

### 1. Detection scope and escalation-readiness package

- **Request and owner:** Security operations, platform, application, data, service, and incident-command owners provide critical-service map, telemetry/integrity-signal coverage, detection use-case inventory, alert-routing record, on-call contacts, and escalation authority map.
- **Validate and limit:** Trace one selected detection path from service and signal through alert routing, accountable triage owner, and stated escalation route. This assesses documented readiness, not detection effectiveness or severity of a live event.
- **AI and trigger:** AI may organize supplied metadata and flag missing owners or escalation links. Humans determine triage, severity, and response. Refresh after service, telemetry, roster, supplier, or threat change.

### 2. Triage, handoff, and exercise package

- **Request and owner:** Security operations, incident-command, legal, continuity, and service owners provide representative alert/triage records, approved handoff procedures, exercise artifacts, containment-authorization records, recovery-transition references, and observed limitations.
- **Validate and limit:** Walk one authorized exercise or closed record from detection through human triage, escalation, documented handoff, and recovery transition. This cannot direct containment, validate response quality, or decide notification or payment.
- **AI and trigger:** AI may prepare a read-only chronology and identify missing authority links. Humans authorize containment and communications. Recollect after failed exercise, material incident, handoff change, or recovery-process change.

### 3. Lessons, exceptions, and oversight package

- **Request and owner:** Incident-response, risk, legal, insurance, supplier, communications, records, and independent-review owners provide corrective actions, exceptions, post-event lessons, supplier follow-up, retest evidence, and management decisions.
- **Validate and limit:** Trace one finding or exception to named human decision, stated limitation, target date, remediation/retest, and disposition. This supports accountable oversight; it cannot make legal conclusions, accept risk, or attest to response readiness.
- **AI and trigger:** AI may flag overdue actions and draft challenge questions from supplied records. Humans approve risk treatment, closure, notifications, and external statements. Review quarterly and after material exercise, incident, supplier, or regulatory change.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
