# NIST SP 800-92 log-management engagement guide

> Original operational guidance, not NIST guidance, a retention-law interpretation, an investigative conclusion, or a compliance claim. Confirm current material through [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final), applicable retention requirements, and the organization’s approved security, privacy, legal, and operational decisions.

## Engagement focus

Operate a log-management program that makes material security and operational records available, protected, intelligible, and usable for monitoring, investigation, recovery, and assurance. Connect material systems and services to event sources, collection paths, access controls, time integrity, retention and disposal decisions, availability assumptions, monitoring use cases, escalation paths, and evidence requests. Treat log coverage as a managed risk decision; do not treat a logging platform or an AI-generated summary as proof that records are complete, reliable, lawful to retain, or sufficient for an investigation.

## Roles and annual rhythm

Assign accountable executive, security-operations, platform, network, application, data, privacy, legal, records-management, service-owner, and supplier-management roles. Operators maintain log-source inventories, collection and storage evidence, access records, retention and disposal approvals, time-synchronization evidence, monitoring and escalation records, exception registers, supplier evidence, and remediation status. Review material log coverage, access, retention assumptions, and exceptions quarterly; test representative log availability, retrieval, and evidence integrity at least annually and after material service, architecture, data, or supplier changes. Before annual renewal, an independent reviewer samples log evidence from source through retrieval; auditors test the evidence trail without changing records, directing investigations, setting retention policy, accepting risk, or attesting for management.

AI may organize supplied log-management evidence, identify missing ownership or stale coverage records, correlate documented sources with service inventories, and draft workpapers for human review. AI cannot alter or delete records, determine legal retention duties, make an investigative finding, accept risk, make a compliance conclusion, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [NIST SP 800-92 publication record](https://csrc.nist.gov/pubs/sp/800/92/final), applicable retention requirements, and approved security, privacy, legal, and operational direction at engagement start; record the version retrieved and applicable use terms. This is original evidence planning, not reproduced NIST guidance, a retention-law interpretation, or an investigative conclusion.

### 1. Log-source, purpose, and coverage-boundary package

- **Request and owner:** Security operations, platform, network, application, data, service, privacy, legal, records, and supplier owners provide material-service and log-source inventory, event-purpose/use-case record, source ownership, collection-boundary diagram, coverage gaps, data classifications, and approved exceptions.
- **Validate and limit:** Trace one material service or use case to its stated event sources, collection ownership, documented coverage boundary, access/retention considerations, and known limitation. This can assess documented coverage; it cannot prove every event is captured or that logs will answer every investigation.
- **AI and trigger:** AI may compare supplied inventories and identify missing owners, stale coverage statements, or unmapped sources. Humans approve scope, privacy boundaries, and exceptions. Refresh after service, source, data, architecture, supplier, or monitoring-use-case change.

### 2. Collection, protection, integrity, and retrieval package

- **Request and owner:** Platform, security operations, identity, network, application, and storage owners provide collection/configuration records, time-synchronization evidence, access-review records, storage/availability monitoring, integrity controls, sample retrieval results, and incident/escalation records.
- **Validate and limit:** Sample a source record through collection path, time reference, authorized storage/access, availability or integrity signal, and human-performed retrieval test. This can support an evidence observation; it cannot alter records, validate all events, or establish forensic sufficiency.
- **AI and trigger:** AI may organize authorized metadata and flag missing evidence links; it cannot write, delete, modify, or access records beyond approved authority. Humans configure systems, approve access, conduct retrieval tests, and assess incidents. Recollect after collection failure, access change, integrity concern, or material platform change.

### 3. Retention, exception, and monitoring-improvement package

- **Request and owner:** Records, legal, privacy, security operations, service, risk, and independent-review owners provide retention/disposal decisions, approved exceptions, monitoring-use-case results, alert/escalation follow-up, corrective actions, reviewer workpapers, and management decisions.
- **Validate and limit:** Trace a selected retained source, exception, or monitoring improvement to its human authority, decision date, evidence limitation, due date, and follow-up/retest. This cannot determine legal duty, accept risk, or establish that retention is appropriate across all jurisdictions.
- **AI and trigger:** AI may flag expiring records or overdue corrective actions and draft review packets. Humans decide retention, disposal, risk, closure, and external statements. Review quarterly and after legal/privacy, threat, monitoring, service, or source changes.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
