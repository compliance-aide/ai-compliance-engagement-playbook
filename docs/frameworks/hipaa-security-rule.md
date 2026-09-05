# HIPAA Security Rule — engagement guide

> Original operational guidance, not legal advice or a compliance assertion. Draft pending independent source, skeptical and rights review.

## Source and applicability

Use the [Security Rule](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C) and [HHS overview](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html). The overview read 2026-09-04 explicitly distinguishes the rule currently in effect from proposed modifications. Do not silently turn a proposal into a current obligation.

HHS identifies covered entities and business associates, ePHI scope, risk analysis and administrative, physical and technical safeguards. This guide does not decide entity status or replace the binding text. Full regulation, current amendments, implementation-specification treatment and organization-specific legal interpretation remain to be verified before final conclusions. Privacy and breach-notification obligations require their own applicable analysis.

## Engagement focus

Maintain a complete ePHI boundary and connect risks, safeguard decisions, actual implementation and ongoing evaluation. Separate risk analysis from a vulnerability scan, a documented decision from implementation, and restored infrastructure from usable information. Preserve failures and uncertainty without converting a checklist score into compliance.

## Roles

The designated security official and accountable management own the program. Privacy/legal owners determine roles, obligations, agreements and notifications. IT, facilities, workforce, biomedical and supplier owners maintain their evidence. An independent reviewer challenges scope, risk reasoning and results. Clinical authorities approve actions affecting care.

AI may organize authorized metadata, reconcile populations and draft workpapers. AI cannot approve safeguards, accept risk, decide legal compliance or reportability, access ePHI without authority, direct patient care or alter production. Use approved synthetic QA fixtures and restricted evidence references.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Record entity/role decisions, services, source versions, assessment period, owners and evidence permissions. Obtain ePHI flows, asset and supplier inventories, approved risk method, prior findings and testing boundaries. Missing role decisions block dependent conclusions; missing assets remain visible rather than excluded.

## Ordered workflow

1. **Define applicable duties.** Legal/security owners approve the source and role register, including required decisions for implementation specifications. Output: obligation register with unresolved interpretations assigned; do not treat an unresolved specification as optional.
2. **Reconcile all ePHI routes.** Compare systems, integrations, endpoints, cloud services, backups and provider records. Identify creation, receipt, maintenance and transmission within the approved scope. Output: complete boundary and responsibility matrix with orphaned flows retained.
3. **Analyze risks.** Apply the approved method to threats, vulnerabilities, existing safeguards and potential consequences across that boundary. Record evidence, assumptions and unknowns. Output: risk analysis; scanner output is one input, not the entire analysis.
4. **Record treatment decisions.** Connect each risk and applicable duty to an authorized decision, implementation owner, rationale and follow-up. Output: safeguard/decision register. A signed exception cannot erase the observed condition.
5. **Test actual practices.** Reconcile the evidence packages below with approved criteria and QA methods. Record expectation, observed outcome, period/build and gaps. Output: test results covering technical and non-technical practices without claiming untested populations passed.
6. **Verify response and correction.** Trace incidents, contingency exercises and remediation through actual actions and retests. Preserve separate legal notification decisions. Output: findings and recovery evidence, including inaccessible data and failed handoffs.
7. **Evaluate and hand off.** Review environmental changes, evidence completeness and unresolved disagreements. Deliver bounded conclusions to the authorized owners. Output: versioned report, next actions and review triggers; no automatic compliance certification.

## Evidence and test plan

These packages retain the earlier PR340 domains, with complete population reconciliation. Each test needs criterion/source, scope, expectation, method, actual outcome, date, owner and limitation. Selection of technical cases must remain explicit; no silent trimming, sampling or capping of assessment evidence is allowed. Previous review status does not transfer to this rewritten draft.

### 1. ePHI boundary, role, and supplier record

- **Request and owner:** A minimized system/data-flow inventory showing where ePHI is created, received, maintained, or transmitted; covered-entity/business-associate role inputs; and vendor/business-associate responsibility records, owned by privacy, architecture, and vendor-management leads.
- **Validate and limit:** Reconcile every in-scope data flow to system ownership, hosting/processor record, and approved responsibility documentation without copying ePHI into the workpaper. This can support a bounded risk-analysis scope; it cannot decide legal status, contractual sufficiency, or completeness of all ePHI flows.
- **AI and trigger:** AI may index approved metadata and flag unowned flows. Legal/privacy humans determine roles and approve scope. Refresh for a new ePHI system, integration, vendor, acquisition, or material data-flow change.

### 2. Risk analysis and safeguard-decision record

- **Request and owner:** Risk-analysis method and results, risk-treatment decisions, safeguard rationale, approved exceptions, and remediation tracking from the security and privacy owners.
- **Validate and limit:** Reperform approved risk calculations or trace it to source assumptions, evidence, responsible decision-maker, and review trigger. This can support that risks and decisions were documented; it cannot prove safeguards are reasonable and appropriate for every environment or establish compliance.
- **AI and trigger:** AI may organize evidence and draft questions but cannot choose safeguards, accept risk, or access restricted records without authorization. Refresh after incident, architecture, threat, workforce, or process change.

### 2a. Physical, workstation, device-media, and business-associate evidence

- **Request and owner:** Facility/workstation access and environment records, device and media handling/disposal records, ePHI-capable asset assignment, business-associate contract or other arrangement providing satisfactory assurances, and vendor change evidence from facilities, endpoint, records, privacy, and vendor owners.
- **Validate and limit:** Reconcile every in-scope ePHI-capable asset and vendor to its accountable owner, authorized environment/handling record, and written business-associate responsibility evidence while keeping ePHI out of the workpaper. This can support that these evidence domains are addressed; it cannot establish agreement sufficiency, complete physical coverage, or vendor compliance.
- **AI and trigger:** AI may index approved metadata and flag missing ownership or expired vendor review. Humans approve contracts, physical safeguards, asset disposition, and vendor decisions. Refresh after a facility, workstation/device, media-handling, or business-associate change.

### 3. Operating-practice and resilience evidence

- **Request and owner:** Time-bounded access-review, audit/log-review, workforce-training, incident-response, backup/restore or contingency-exercise, and change-management records from their accountable operational owners.
- **Validate and limit:** Independently trace the approved test population to source logs or records, dates, population coverage, and follow-up action while minimizing protected information. This can support that declared practices have observable operating evidence; it cannot prove uninterrupted effectiveness, breach-reportability, or an external audit result.
- **AI and trigger:** AI may produce a redacted evidence index and escalate missing or inconsistent records. Humans approve conclusions, notifications, remediation closure, and changes. Recollect on a security incident, failed exercise, major system/vendor change, and the approved review cycle.


## Failure branches and decisions

- Confirmed ePHI system omitted from risk analysis: mark completeness not_supported and reopen analysis; preserve results for systems actually examined.
- Agreement exists but provider/customer duties lack implementation evidence: distinguish contract presence from unverified operation.
- Backup succeeds but restoration cannot make required data usable: retain backup success separately from the failed recovery criterion.
- Remediation ticket closed without retest: retain the last evidenced finding state and assign verification.
- Suspected incident with uncertain breach status: preserve facts and escalate promptly to designated officials; AI must not decide notification duties or wait for the next periodic review.

Fictional desk case: an inventory lists ten ePHI systems, but risk-analysis evidence covers nine. The complete-scope claim is not_supported; risks in the tenth system are unassessed. A passing scan of the nine does not resolve that omission.

## Cadence and renewal

Set a documented risk-based schedule and event triggers consistent with verified requirements. Reevaluate after environmental, organizational, provider, threat or incident changes. Do not invent a universal annual HIPAA certification or treat one yearly scan as ongoing risk management. Preserve source-backed documentation retention requirements separately from patient-record retention decisions.

## Completion and handoff

Deliver role/source decisions, complete ePHI inventory, risk analysis, safeguards and physical/device/media/vendor records, tests, incidents, remediation, gaps and disagreements. Classify assertions supported, not_supported, inconclusive, not_applicable or not_tested with reasons. Final legal conclusions and external communications require named authority. No live ePHI assessment or production testing occurred in drafting this guide.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) and [agent runbook](../agent-runbook.md). Keep ePHI and restricted legal/incident records out of this public repository.
