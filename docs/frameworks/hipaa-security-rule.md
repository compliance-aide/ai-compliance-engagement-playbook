# HIPAA Security Rule — engagement guide

> Original operational guidance, not legal advice or a claim of compliance.
> Review the binding [HIPAA Security Rule](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C)
> and current HHS guidance before each engagement milestone.

## Engagement focus

Maintain an ePHI inventory and data-flow view. Perform and document ongoing risk
analysis; decide and record safeguards appropriate to the environment; test
workforce, physical, technical, vendor, incident, and recovery practices; and
refresh the work after material change.

## Roles

Operators own the protected environment and evidence. Independent reviewers evaluate
completeness and reasoning rather than a checklist score. AI may organize
authorized evidence and risk narratives while minimizing exposure of ePHI, but cannot
make legal or notification determinations, approve safeguards, access ePHI without authorization,
or alter systems; human review is required before conclusions or changes.

## Annual rhythm

Review ePHI flows, vendors, and environmental changes; complete the documented
risk-analysis cycle; test response and recovery; update the remediation plan;
and preserve management decisions with owners and review dates.

## Tailored evidence plan

**Source and rights snapshot.** Use the current [HIPAA Security Rule](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C) and HHS guidance; reviewed 2026-07-31. The eCFR describes itself as authoritative but unofficial, so legal/compliance owners must resolve binding-source and applicability questions. This plan requests artifact classes, never ePHI, and does not make a legal compliance conclusion.

### 1. ePHI boundary, role, and supplier record

- **Request and owner:** A minimized system/data-flow inventory showing where ePHI is created, received, maintained, or transmitted; covered-entity/business-associate role inputs; and vendor/business-associate responsibility records, owned by privacy, architecture, and vendor-management leads.
- **Validate and limit:** Trace a selected data flow to system ownership, hosting/processor record, and approved responsibility documentation without copying ePHI into the workpaper. This can support a bounded risk-analysis scope; it cannot decide legal status, contractual sufficiency, or completeness of all ePHI flows.
- **AI and trigger:** AI may index approved metadata and flag unowned flows. Legal/privacy humans determine roles and approve scope. Refresh for a new ePHI system, integration, vendor, acquisition, or material data-flow change.

### 2. Risk analysis and safeguard-decision record

- **Request and owner:** Risk-analysis method and results, risk-treatment decisions, safeguard rationale, approved exceptions, and remediation tracking from the security and privacy owners.
- **Validate and limit:** Reperform a selected approved risk calculation or trace it to source assumptions, evidence, responsible decision-maker, and expiry date. This can support that risks and decisions were documented; it cannot prove safeguards are reasonable and appropriate for every environment or establish compliance.
- **AI and trigger:** AI may organize evidence and draft questions but cannot choose safeguards, accept risk, or access restricted records without authorization. Refresh after incident, architecture, threat, workforce, or process change.

### 3. Operating-practice and resilience evidence

- **Request and owner:** Time-bounded access-review, audit/log-review, workforce-training, incident-response, backup/restore or contingency-exercise, and change-management records from their accountable operational owners.
- **Validate and limit:** Independently trace a human-approved selection to source logs or records, dates, population coverage, and follow-up action while minimizing protected information. This can support that declared practices have observable operating evidence; it cannot prove uninterrupted effectiveness, breach-reportability, or an external audit result.
- **AI and trigger:** AI may produce a redacted evidence index and escalate missing or inconsistent records. Humans approve conclusions, notifications, remediation closure, and changes. Recollect on a security incident, failed exercise, major system/vendor change, and annual review.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
