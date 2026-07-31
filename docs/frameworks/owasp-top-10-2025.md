# OWASP Top 10:2025 — engagement guide

> Original operational guidance, not OWASP content or a security attestation. Check the [OWASP Top 10:2025 edition](https://owasp.org/Top10/2025/) for the current published edition.

## Engagement focus

Inventory in-scope web applications and their relevant interfaces/APIs, releases, and owners. Use the current published edition to set a risk-led testing and remediation plan, while preserving design, release, configuration, test, and exception evidence. Perform post-release checks and refresh priorities from meaningful findings.

## Roles and annual rhythm

Application owners remediate and preserve evidence. Independent reviewers sample evidence and challenge closure quality. AI can correlate code, configuration, and signal evidence and draft test questions; it cannot run destructive tests, assert security, accept risk, or replace penetration testing. Review releases continuously, risks quarterly, and scope annually.


## Tailored evidence plan

**Plan status:** Independently reviewed; see the [review receipt](../evidence-plan-reviews/owasp-top-10-2025.md).

**Source and rights snapshot.** Use the official [OWASP Top 10:2025 edition](https://owasp.org/Top10/2025/); source status: OWASP identifies 2025 as the current released Top Ten, checked 2026-07-31. OWASP identifies the edition as CC BY 3.0 Unported; this repository nevertheless uses original operational language and links only—no copied categories, test material, or branded template. This plan is not a security attestation or penetration-test substitute.

### 1. Application, API, release, and exposure boundary

- **Request and owner:** Request the in-scope application/API inventory, internet and internal exposure record, release calendar, architecture/data-flow summary, accountable owner register, and risk-acceptance boundary from application, engineering, security, and product owners.
- **Validate and limit:** With approved read-only, least-privilege access, trace a selected application and release to the approved scope, owner, versioned deployment provenance, exposure classification, and exception history; use sanitized/redacted exports and never ingest credentials, secrets, or customer payloads. This establishes a reviewable population; it cannot prove discovery of every endpoint or vulnerability.
- **AI and trigger:** AI may reconcile approved inventories and flag missing ownership. Humans approve scope, risk classification, releases, and exception acceptance. Refresh for an application, API, exposure, ownership, or architecture change.

### 2. Secure delivery, verification, and remediation evidence

- **Request and owner:** Request code-review and build provenance, dependency/configuration records, authorized test plans and sanitized results, defect tickets, remediation and retest records, and release approvals from engineering, security-testing, and release owners.
- **Validate and limit:** With approved read-only access, trace a selected finding or release to the relevant versioned build, immutable or otherwise preserved test-result reference, accountable disposition, corrective action, and retest where applicable; use only sanitized/redacted artifacts and never ingest credentials, secrets, or customer payloads. This supports evidence that a process occurred; it cannot certify absence of exploitable weaknesses or replace authorized testing.
- **AI and trigger:** AI may correlate approved results and draft questions, but may not conduct destructive testing, change production, or mark a finding closed. Recollect after a material release, high-severity finding, dependency change, or testing-method change.

### 3. Exception, incident, and annual risk-review record

- **Request and owner:** Request exception and risk-acceptance records, incident/post-release records, detection and response handoffs, overdue-remediation log, management risk review, and edition/source-change watch from security, legal, engineering, and leadership owners.
- **Validate and limit:** With approved read-only access, trace a selected exception or incident to dated facts, a named human decision, preserved evidence reference, compensating-action evidence, and closure/review date; use redacted material and never ingest credentials, secrets, or customer payloads. This supports governance traceability; it cannot determine regulatory reportability, legal liability, or secure operation.
- **AI and trigger:** AI may prepare a redacted evidence index and surface aging actions. Humans decide incident escalation, risk acceptance, and closure. Revisit quarterly for risk and annually for scope, and after an incident or published-edition change.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
