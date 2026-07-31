# SPARTA spacecraft cybersecurity engagement guide

> Original operational guidance, not SPARTA requirements, countermeasures, mappings, scores, or a spacecraft-security assessment. Confirm framework materials through the [SPARTA user guide](https://sparta.aerospace.org/resources/user-guide).

## Engagement focus

Maintain a mission-aware cybersecurity record for spacecraft and associated ground, development, supply-chain, and operational environments: mission objectives, system and interface inventories, threats and risk decisions, security architecture evidence, software and hardware provenance, communications dependencies, test evidence, anomaly and incident records, mission changes, and retirement plans. Preserve the separation between mission assurance, safety, flight authorization, and cybersecurity review.

## Roles and annual rhythm

Mission and spacecraft owners decide mission and operational risk; systems engineering maintains design evidence; cybersecurity teams manage threat and assurance records; safety and flight authorities retain independent decision rights; suppliers provide approved provenance; independent reviewers test traceability. AI may organize authorized artifacts, compare versions, identify missing evidence, and draft questions, but cannot operate a spacecraft, alter mission systems, make flight or safety decisions, score SPARTA materials, approve a launch or mission change, or make an assurance claim. Reassess at each material design, integration, launch, operational, anomaly, supplier, or end-of-mission transition.


## Tailored evidence plan

**Source and rights snapshot.** Use the public [SPARTA user guide](https://sparta.aerospace.org/resources/user-guide), checked 2026-07-31, with mission-owner confirmation of the applicable release and authorized access conditions. This original plan does not reproduce SPARTA content, produce a score, or make a launch, flight, safety, or assurance decision.

### 1. Mission boundary, interfaces, and authority package

- **Request and owner:** Obtain the approved mission and lifecycle boundary, spacecraft/ground/development inventories, interface and communications-dependency records, mission assumptions, owner roles, and separation of cybersecurity, safety, and flight authority from mission systems engineering and leadership.
- **Validate and limit:** Trace a selected mission element or interface to its accountable owner, lifecycle phase, dependency, approved boundary, and unresolved risk or decision. This supports scoped traceability; it cannot authorize a mission, determine flightworthiness, or prove system completeness.
- **AI and trigger:** AI may correlate authorized metadata and flag missing lifecycle or ownership links. Mission, safety, and flight authorities retain decisions. Trigger on design baseline changes, integration, supplier/interface changes, launch readiness, anomaly, or retirement planning.

### 2. Engineering assurance and supply-chain package

- **Request and owner:** Obtain architecture and threat/risk work references, approved software/hardware provenance, secure-development and configuration references, supplier evidence, test records, change history, and accepted exceptions from systems engineering, cyber, quality, and supplier owners.
- **Validate and limit:** Trace a selected component or change through provenance, approved engineering decision, test evidence, exception, and remediation/retest link. This supports accountable engineering evidence; it cannot prove mission security, validate a countermeasure, or evaluate classified material beyond authorization.
- **AI and trigger:** AI may organize permitted records and flag incomplete provenance or test links; it cannot alter mission systems, select security treatments, or expose restricted information. Qualified human owners decide disposition. Trigger on supplier substitution, software release, test failure, or material risk change.

### 3. Operations, anomaly, and mission-transition package

- **Request and owner:** Obtain authorized operational monitoring and anomaly records, incident/escalation decisions, mission-change approvals, lessons learned, recovery/continuity references, and end-of-mission or disposal planning from operations, cyber, safety, and mission leadership.
- **Validate and limit:** Trace a selected anomaly or transition from source record to accountable triage, authority decision, action owner, and documented outcome. This supports chronology and learning; it cannot command spacecraft, decide safety actions, or issue an assurance conclusion.
- **AI and trigger:** AI may generate a read-only timeline and surface stale action owners. Humans approve operations, safety actions, external communications, and closure. Trigger on anomaly, operational change, mission phase transition, or post-event review.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
