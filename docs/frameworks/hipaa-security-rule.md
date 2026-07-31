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

Perform periodic review and update when environmental or organizational change
affects the security program; as this playbook's minimum engagement cadence,
annually review ePHI flows, vendors, the documented risk-analysis cycle,
response/recovery tests, remediation, and management decisions. This cadence is
not a statement that HIPAA itself mandates an annual review.

## Tailored evidence plan

**Plan status:** Independently reviewed; see the [review receipt](../evidence-plan-reviews/hipaa-security-rule.md).

**Source and rights snapshot.** Use the current [HIPAA Security Rule](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C), [HHS Security Rule overview](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html), and [HHS guidance](https://www.hhs.gov/hipaa/for-professionals/security/guidance/index.html); checked 2026-07-31. Treat the current rule as binding and any separately identified proposed modification as nonbinding unless and until effective. The eCFR is a continuously updated reference rather than the official legal edition, so legal/compliance owners confirm binding text and applicability. This plan requests artifact classes, never ePHI, and does not make a legal compliance conclusion.

### 1. ePHI boundary, role, and supplier record

- **Request and owner:** A minimized system/data-flow inventory showing where ePHI is created, received, maintained, or transmitted; covered-entity/business-associate role inputs; and vendor/business-associate responsibility records, owned by privacy, architecture, and vendor-management leads.
- **Validate and limit:** Trace a selected data flow to system ownership, hosting/processor record, and approved responsibility documentation without copying ePHI into the workpaper. This can support a bounded risk-analysis scope; it cannot decide legal status, contractual sufficiency, or completeness of all ePHI flows.
- **AI and trigger:** AI may index approved metadata and flag unowned flows. Legal/privacy humans determine roles and approve scope. Refresh for a new ePHI system, integration, vendor, acquisition, or material data-flow change.

### 2. Risk analysis and safeguard-decision record

- **Request and owner:** Risk-analysis method and results, risk-treatment decisions, safeguard rationale, approved exceptions, and remediation tracking from the security and privacy owners.
- **Validate and limit:** Reperform a selected approved risk calculation or trace it to source assumptions, evidence, responsible decision-maker, and expiry date. This can support that risks and decisions were documented; it cannot prove safeguards are reasonable and appropriate for every environment or establish compliance.
- **AI and trigger:** AI may organize evidence and draft questions but cannot choose safeguards, accept risk, or access restricted records without authorization. Refresh after incident, architecture, threat, workforce, or process change.

### 2a. Physical, workstation, device-media, and business-associate evidence

- **Request and owner:** Facility/workstation access and environment records, device and media handling/disposal records, ePHI-capable asset assignment, business-associate contract or other arrangement providing satisfactory assurances, and vendor change evidence from facilities, endpoint, records, privacy, and vendor owners.
- **Validate and limit:** Trace a selected ePHI-capable asset or vendor to its accountable owner, authorized environment/handling record, and written business-associate responsibility evidence while keeping ePHI out of the workpaper. This can support that these evidence domains are addressed; it cannot establish agreement sufficiency, complete physical coverage, or vendor compliance.
- **AI and trigger:** AI may index approved metadata and flag missing ownership or expired vendor review. Humans approve contracts, physical safeguards, asset disposition, and vendor decisions. Refresh after a facility, workstation/device, media-handling, or business-associate change.

### 3. Operating-practice and resilience evidence

- **Request and owner:** Time-bounded access-review, audit/log-review, workforce-training, incident-response, backup/restore or contingency-exercise, and change-management records from their accountable operational owners.
- **Validate and limit:** Independently trace a human-approved selection to source logs or records, dates, population coverage, and follow-up action while minimizing protected information. This can support that declared practices have observable operating evidence; it cannot prove uninterrupted effectiveness, breach-reportability, or an external audit result.
- **AI and trigger:** AI may produce a redacted evidence index and escalate missing or inconsistent records. Humans approve conclusions, notifications, remediation closure, and changes. Recollect on a security incident, failed exercise, major system/vendor change, and annual review.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
