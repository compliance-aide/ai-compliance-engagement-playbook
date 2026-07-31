# NIST SP 800-92 log-management engagement guide

> Original operational guidance, not NIST guidance, a retention-law interpretation, an investigative conclusion, or a compliance claim. Confirm current material through [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final), applicable retention requirements, and the organization’s approved security, privacy, legal, and operational decisions.

## Engagement focus

Operate a log-management program that makes material security and operational records available, protected, intelligible, and usable for monitoring, investigation, recovery, and assurance. Connect material systems and services to event sources, collection paths, access controls, time integrity, retention and disposal decisions, availability assumptions, monitoring use cases, escalation paths, and evidence requests. Treat log coverage as a managed risk decision; do not treat a logging platform or an AI-generated summary as proof that records are complete, reliable, lawful to retain, or sufficient for an investigation.

## Roles and annual rhythm

Assign accountable executive, security-operations, platform, network, application, data, privacy, legal, records-management, service-owner, and supplier-management roles. Operators maintain log-source inventories, collection and storage evidence, access records, retention and disposal approvals, time-synchronization evidence, monitoring and escalation records, exception registers, supplier evidence, and remediation status. Review material log coverage, access, retention assumptions, and exceptions quarterly; test representative log availability, retrieval, and evidence integrity at least annually and after material service, architecture, data, or supplier changes. Before annual renewal, an independent reviewer samples log evidence from source through retrieval; auditors test the evidence trail without changing records, directing investigations, setting retention policy, accepting risk, or attesting for management.

AI may organize supplied log-management evidence, identify missing ownership or stale coverage records, correlate documented sources with service inventories, and draft workpapers for human review. AI cannot alter or delete records, determine legal retention duties, make an investigative finding, accept risk, make a compliance conclusion, attest for management, or replace independent review.


<!-- evidence-plan: generated-draft -->
## Tailored evidence plan

**Plan status:** Draft generated from this guide's existing engagement focus; it requires independent source and skeptical review before a final catalog claim.

**Source and rights snapshot.** Use the guide's cited publisher source (https://csrc.nist.gov/pubs/sp/800/92/final) and check its current edition or status before use. This plan uses original operational language and does not reproduce protected requirements, assessment questions, mappings, or branded templates. A named human engagement owner confirms applicability and source rights.

**Guide-specific planning input.** Operate a log-management program that makes material security and operational records available, protected, intelligible, and usable for monitoring, investigation, recovery, and assurance. Connect material systems and services to event sources, collection paths, access controls, time integrity, retention and disposal decisions, availability assumptions, monitoring use cases, escalation paths, and evidence requests. Treat log coverage as a managed risk decision; do not treat a logging platform or an AI-generated summary as proof that records are complete, reliable, lawful to retain, or sufficient for an investigation.

### 1. Applicability and boundary evidence

- **Request and owner:** A dated record of the applicable use case, intended purpose, deployment context, affected people, and model/data dependency, exclusions, inherited responsibilities, and accountable human owners, maintained by AI governance, product, model, and risk owners.
- **Validate and limit:** Trace a human-approved selection from the declared boundary to source systems or operating records; preserve population, period, access restriction, and unresolved-boundary notes. This can support a bounded engagement scope. It cannot decide legal applicability, publisher acceptance, certification, or completeness beyond the documented population.
- **AI and trigger:** AI may organize approved metadata and flag inconsistent boundaries. Humans approve scope and exclusions. Refresh after model, data, provider, use-case, geography, release, or incident change.

### 2. Operating evidence for NIST SP 800-92 log-management

- **Request and owner:** Time-bounded inventory, evaluation, monitoring, oversight, release, feedback, and incident records, selected because this guide focuses on operate a log-management program that makes material security and operational records available, protected, intelligible, and usable for monitoring, investigation, recovery, and assurance. connect material systems and services to event sources, collection paths, access controls, time integrity, retention and disposal decisions, availability assumptions, monitoring use cases, escalation paths, and evidence requests. treat log coverage as a managed risk decision; do not treat a logging platform or an ai-generated summary as proof that records are complete, reliable, lawful to retain, or sufficient for an investigation., from AI governance, product, model, and risk owners.
- **Validate and limit:** Inspect provenance and freshness, then trace a human-approved sample to its source record, accountable owner, and exception or follow-up path. This can support that the stated practice has observable evidence. It cannot prove continuous effectiveness, satisfy an assessor by itself, or support an unreviewed conformance claim.
- **AI and trigger:** AI may create a read-only evidence index, identify gaps, and draft questions; it may not alter systems, close findings, or create external representations. Recollect after model, data, provider, use-case, geography, release, or incident change.

### 3. Decisions, exceptions, and renewal evidence

- **Request and owner:** Approved risk or exception decisions, corrective-action and retest records, source-change watch, and annual review or renewal record from AI governance, product, model, and risk owners.
- **Validate and limit:** Trace a selected exception or remediation item to a named human decision, due date, expiry, evidence source, and retest result. This can support accountable follow-through. It cannot accept residual risk, make a legal decision, or replace an independent assessment.
- **AI and trigger:** AI may flag stale approvals and assemble a review packet. Humans approve risk treatment, submissions, attestations, and closure. Revisit on model, data, provider, use-case, geography, release, or incident change.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
