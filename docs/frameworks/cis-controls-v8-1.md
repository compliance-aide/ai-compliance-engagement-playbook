# CIS Critical Security Controls v8.1 — engagement guide

> Original operational guidance, not CIS content or a conformance claim. Consult
> the current [CIS Controls source](https://www.cisecurity.org/controls/v8-1)
> under its applicable terms.

## Engagement focus

Select a risk tier, service boundaries, assets, owners, and success measures;
maintain an evidence index that separates design claim from observed operation;
ingest approved change and security signals; risk-prioritize remediation; sample
evidence freshness; exercise a high-value response scenario; and independently
challenge closure quality annually.

## Roles and annual rhythm

Operators maintain inventory, configuration, and operational proof. Independent
reviewers challenge evidence and report exceptions without owning fixes. AI may
detect stale or conflicting claims and draft questions and change-impact lists;
it cannot attest, close an exception, accept risk, or alter system configuration. Run monthly signal review, quarterly
validation, and annual scope and priority renewal.


## Tailored evidence plan

**Source and rights snapshot.** Use the official [CIS Controls v8.1 page](https://www.cisecurity.org/controls/v8-1) and its applicable terms; checked 2026-07-31. This original operational plan does not reproduce CIS content, determine conformance, or grant rights to redistribute CIS materials.

### 1. Asset, software, account, and configuration evidence

- **Request and owner:** Security operations provides approved asset and software inventories, account administration records, configuration baselines, change records, and system owners for the selected tier and boundary.
- **Validate and limit:** Independently trace a selected asset, privileged account, and configuration change from inventory entry to authoritative system record, owner, and dated evidence. This tests observable evidence linkage; it cannot establish complete discovery or CIS conformance.
- **AI and trigger:** AI may normalize authorized inventory metadata and flag missing owners or stale records. Security humans approve scope, system facts, exceptions, and remediation. Recollect after material asset, identity, configuration, or ownership change.

### 2. Protective-operation and response evidence

- **Request and owner:** Security and IT owners provide vulnerability/remediation records, security event triage records, backups or recovery-test results, protective-service configurations, and an exercised response scenario.
- **Validate and limit:** Sample a risk-ranked event or exposure through detection, owner assignment, action, timing, and retest record; compare recovery exercise claims with retained results. This supports a bounded operational observation, not a conclusion that all threats were prevented or recovered.
- **AI and trigger:** AI may assemble a redacted evidence index and identify inconsistent dates or unresolved actions; it cannot alter configurations, close a finding, or accept risk. Refresh after a material incident, failed recovery test, critical exposure, or control change.

### 3. Governance, exceptions, and renewal evidence

- **Request and owner:** Program leadership supplies selected-tier rationale, risk decisions, exception register, remediation ownership, independent-review notes, and annual scope/priority review record.
- **Validate and limit:** Trace sampled exceptions to named human approval, scope, compensating evidence, expiry, and retest. This can demonstrate accountable exception handling; it cannot decide acceptability or issue an attestation.
- **AI and trigger:** AI may flag expired exceptions and prepare renewal questions. Humans approve risk decisions, public claims, and closure. Review monthly signals, quarterly validation, and annual scope and priority renewal.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
