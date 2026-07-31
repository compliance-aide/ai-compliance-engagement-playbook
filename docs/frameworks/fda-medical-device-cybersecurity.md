# FDA medical-device cybersecurity — engagement guide

> Original operational guidance for lifecycle work, not FDA regulatory advice or a submission conclusion. See the [FDA cybersecurity resource](https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity).

## Engagement focus

Maintain product and responsibility inventory, safety-cyber risk integration, secure-development and supply-chain evidence, vulnerability triage, patch practice, release/change records, disclosure exercises, and management review.

## Roles and annual rhythm

Product owners make safety, release, and regulatory decisions. Independent reviewers test selected lifecycle trails and escalation. AI can link evidence and detect gaps, but cannot make patient-safety, submission, clinical, vulnerability-disclosure, or release decisions.

## Tailored evidence plan

**Source and rights snapshot.** Check the current [FDA medical-device cybersecurity resource](https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity), including the currently applicable FDA guidance and notices, before scoping; checked 2026-07-31. FDA material is official public guidance, but this plan is original operational language and does not reproduce guidance or decide a regulatory submission, product safety, or clearance question.

### 1. Product boundary and safety-cyber risk package

- **Request and owner:** The product and safety owners provide the released-product/version inventory, intended environment and interfaces, software bill-of-material inputs, hazard/risk records, and the human-approved product boundary for the review period.
- **Validate and limit:** Trace selected released versions and interfaces to their risk record, accountable owner, and safety escalation path. This supports lifecycle traceability; it cannot establish that every safety hazard was identified or that a benefit-risk decision is appropriate.
- **AI and trigger:** AI may reconcile supplied inventories and flag a version without a linked owner or risk trail. Product and safety authorities decide scope and safety conclusions. Refresh after a material design, dependency, vulnerability, clinical-use, or field-event change.

### 2. Secure development, supplier, and release package

- **Request and owner:** Engineering and quality owners provide approved development/change records, security test outputs, supplier component assurance inputs, release approvals, and unresolved-security decision records for the selected release population.
- **Validate and limit:** Inspect provenance, dates, access restrictions, and a selected trail from change through test and human release approval. This supports that an accountable trail exists; it cannot prove secure operation, supplier quality, or regulatory sufficiency.
- **AI and trigger:** AI may index authorized records and identify missing joins; it may not change code, approve release, select a test conclusion, or accept a security exception. Recollect before release and following a material supplier, test failure, or design change.

### 3. Vulnerability response and postmarket package

- **Request and owner:** Security, quality, and incident owners provide intake/triage records, impact analyses, coordinated-disclosure records where applicable, remediation and communication decisions, field monitoring, and management review minutes.
- **Validate and limit:** Trace a selected vulnerability or field signal to time-stamped intake, assigned authority, evidence, decision, and follow-up. This supports response governance; it cannot decide exploitability, patient impact, reporting, notification, or corrective-action closure.
- **AI and trigger:** AI may de-duplicate authorized tickets and prepare a human review packet. Authorized humans decide disclosure, communications, regulatory contact, and closure. Refresh on a significant vulnerability, incident, recall-related signal, or annual review.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
