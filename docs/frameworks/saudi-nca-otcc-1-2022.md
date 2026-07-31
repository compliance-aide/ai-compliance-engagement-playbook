# Saudi NCA OTCC-1:2022 operational-technology cybersecurity engagement guide

> Original operational guidance, not NCA control text, an assessment, operational instruction, or a compliance claim. Confirm the current program through the [NCA Operational Technology Cybersecurity Controls page](https://nca.gov.sa/en/regulatory-documents/controls-list/otcc/).

## Engagement focus

Maintain an industrial-control-system evidence record: asset and network boundaries, process and safety ownership, authorized access paths, service and supplier dependencies, change and maintenance decisions, monitoring and incident records, recovery readiness, and remediation evidence. Treat OT availability and safety constraints as design inputs that require accountable operational review; do not direct changes based only on an evidence gap.

## Roles and annual rhythm

OT process and safety owners authorize operational decisions; cybersecurity teams retain monitoring and assurance evidence; engineering and maintenance owners document changes; supplier owners maintain access and service evidence; independent reviewers challenge traceability; qualified Saudi counsel interprets regulatory scope. AI may inventory approved records, flag missing provenance, and draft questions, but cannot operate or configure industrial systems, override safety processes, authorize remote access, approve change windows, conduct an assessment, submit to NCA, or claim compliance. Review continuously across material changes and conduct a documented annual engagement review.

## Tailored evidence plan

**Source and rights snapshot.** Retain the official [NCA Operational Technology Cybersecurity Controls page](https://nca.gov.sa/en/regulatory-documents/controls-list/otcc/), retrieved 2026-07-31, and have authorized entity leadership confirm the OTCC-1:2022 source/version, status, and permitted use before reliance. This is original evidence-planning language, not NCA control text, a safe-operating instruction, an assessment, or a conformity statement. Keep OT diagrams, configurations, and event data in approved repositories.

### 1. OT boundary, process, and safety-authority package

- **Request and owner:** Obtain the human-approved OT asset/network and process boundary, process/service criticality context, safety and operational owners, engineering support model, remote-access paths, supplier dependencies, and counsel-led scope questions from operations, safety, engineering, cybersecurity, legal, and supplier owners. Define the permitted observation boundary and evidence period before review.
- **Validate and limit:** Trace a selected OT asset or process service to its accountable operational and safety owners, authorized boundary, support/remote-access relationship, and recorded scope or escalation decision. Use approved summaries where engineering detail is restricted. This supports accountable scope provenance; it cannot determine safety, criticality, regulatory applicability, or full asset coverage.
- **AI and trigger:** AI may compare approved inventory metadata and flag missing owner, boundary, or review references. Human operations, safety, and legal authorities decide scope and escalation. Trigger on commissioning, decommissioning, material process/network change, supplier change, or annual review.

### 2. Access, maintenance-change, and monitoring package

- **Request and owner:** Obtain authorized access and remote-support approvals, maintenance/engineering change records, configuration/reference baselines, monitoring or event references, safe test/exercise records, incident records, and exception approvals from OT operations, engineering, maintenance, cybersecurity, and suppliers. Establish safety and availability constraints before access to evidence.
- **Validate and limit:** For a selected access, change, or event, inspect the trail from accountable authorization through time-bounded maintenance/operation evidence, monitoring or test reference, exception/incident record, and remediation/retest link. Do not run commands, alter equipment, or direct live changes. This supports traceability of governance; it cannot prove safe operation, detection coverage, availability, or OTCC conformity.
- **AI and trigger:** AI may organize permitted metadata and identify missing approvals, timestamps, or follow-up links; it cannot access or operate OT systems, grant remote access, modify configurations, or approve a change window. Named humans decide operational action. Trigger on remote-access change, maintenance work, material event, failed test, or incident.

### 3. Recovery, supplier-support, and remediation package

- **Request and owner:** Obtain recovery and continuity exercise references, supplier support/maintenance responsibility records, risk and exception approvals, incident coordination records, independent-review observations, corrective actions, retest evidence, and management-review records from operations, safety, engineering, cybersecurity, suppliers, and leadership.
- **Validate and limit:** Trace a selected recovery exercise, support dependency, or material finding to the OT boundary, accountable owner, approved decision, exercise or response record, corrective action, and retest or documented closure rationale. Preserve safety and outage constraints. This supports a reviewable resilience trail; it cannot demonstrate real-world recovery, supplier performance, safety assurance, or compliance.
- **AI and trigger:** AI may create a non-authoritative action queue and flag overdue remediation or expiring exception records. Independent reviewers challenge traceability; named humans approve residual risk, closure, and external communication. Trigger on exercise result, supplier support change, incident, overdue corrective action, source change, or annual readiness review.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
