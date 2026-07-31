# MITRE ATT&CK — threat-informed engagement guide

> Original operational guidance, not a MITRE certification or coverage claim. Version-pin work to the [ATT&CK release history](https://attack.mitre.org/resources/versions/).

## Engagement focus

Select relevant platforms and threat scenarios with stakeholders. Maintain a bounded analytic record linking observed threats, detection evidence, exercises, and defensive decisions. Preserve source provenance and version context; test detection and response in authorized exercises; track gaps, false positives, owners, and remediation.

## Roles and annual rhythm

Defense owners maintain detections and exercise evidence. Independent reviewers sample rationale, outcomes, and closure records. AI can group signals, find evidence, propose hypotheses, and compare changes; it cannot label activity as fact, modify production detections, run offensive activity, or claim complete coverage. Review threats quarterly and scope annually.

## Tailored evidence plan

**Source and rights snapshot.** Use MITRE's official [ATT&CK version history](https://attack.mitre.org/resources/versions/) and the linked official knowledge base selected by human defense owners. Record the release/version used for each analysis. Retrieved 2026-07-31. MITRE ATT&CK content has its own terms; this guide provides original planning and does not reproduce a matrix, claim coverage, or certify a defense program.

### 1. Threat-priority and ATT&CK-version decision record

- **Request and owner:** Approved threat-prioritization record, selected ATT&CK release/version reference, environment/platform scope, threat-intelligence provenance, business/system criticality inputs, and named threat-intelligence, security, and business owners. Cover the annual threat model and material updates.
- **Validate and limit:** Trace selected priority scenarios to their approved business context, source provenance, version pin, and human rationale. Handle intelligence under its distribution restrictions. This supports a repeatable prioritization record; it cannot prove adversary intent, likelihood, relevance to every system, or complete technique coverage.
- **AI and trigger:** AI may compare approved scenario metadata to versioned knowledge-base references and flag stale version/source links. Humans decide prioritization and relevance. Trigger on a new ATT&CK release, material threat change, major architecture change, incident, or annual planning cycle.

### 2. Detection-and-telemetry engineering trace

- **Request and owner:** Detection use-case inventory, authorized telemetry/data-source boundary, implementation/configuration references, test/exercise records, tuning/change approvals, false-positive/negative observations, and named detection/platform owners. Define the selected systems, dates, and data-retention constraints.
- **Validate and limit:** For a human-selected sample, trace one priority scenario to telemetry availability, approved detection logic/configuration reference, authorized test result, tuning decision, and owner. Do not run unapproved simulations or modify production rules. This can support engineering traceability; it cannot prove a detection will identify real activity, telemetry completeness, or operational effectiveness.
- **AI and trigger:** AI may map internal labels to approved versioned references, search authorized evidence, and draft gap questions. Humans approve detection changes, tests, and tuning. Trigger on telemetry loss, detection change, test finding, platform migration, or quarterly engineering review.

### 3. Exercise, investigation, and remediation learning loop

- **Request and owner:** Authorized tabletop/simulation approvals, exercise observations, investigation references, response handoff records, remediation backlog, risk/exception decisions, retest evidence, and closure approvals from incident-response, detection, engineering, and risk owners.
- **Validate and limit:** Trace a selected exercise or investigated event through authorization, observation, decision, corrective action, retest or documented deferral, and human closure. Keep raw security events and sensitive intelligence out of the repository. This supports a bounded learning history; it cannot establish incident attribution, response effectiveness, or enterprise-wide coverage.
- **AI and trigger:** AI may organize sanitized observations and identify unresolved links. Humans decide incident classification, containment, risk acceptance, remediation priority, and closure. Trigger on an exercise, material detection failure, confirmed incident, or annual management review.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
