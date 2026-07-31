# CIS Benchmarks program engagement guide

> Original operational guidance, not CIS Benchmark content, a product configuration instruction, a license interpretation, or a compliance claim. Confirm current versions, permissions, and authorized source material through [CIS Benchmarks](https://portal.cisecurity.org/benchmarks); do not copy licensed benchmark text into this repository or an AI prompt.

## Engagement focus

Operate a controlled baseline program for products and services covered by CIS Benchmarks. Connect each authorized benchmark version to applicable technology, environment, owner, tailoring decision, implementation evidence, validation results, exceptions, remediation, and version-refresh record. Treat a benchmark result as assessment input rather than proof that a system is secure, suitable for its business use, or authorized for production.

## Roles and annual rhythm

Assign accountable executive, security, platform, endpoint, network, cloud, application, configuration-management, change-management, risk, procurement, and supplier-management roles. Operators maintain technology scope, authorized benchmark version records, tailored-baseline approvals, validation evidence, exception and remediation records, change and rollback artifacts, license and source records, and refresh status. Review material baseline coverage, exceptions, evidence quality, and vendor or benchmark changes quarterly; test representative tailoring, implementation, validation, and rollback workflows at least annually and after material technology, service, provider, or architecture changes. Before annual renewal, an independent reviewer samples records from applicable baseline selection through validated treatment; auditors test the evidence trail without configuring systems, interpreting license terms, authorizing production changes, accepting risk, or attesting for management.

AI may organize supplied evidence, flag stale benchmark-version or ownership records, relate validation results to recorded assets, and draft workpapers for human review. AI cannot retrieve or reproduce restricted content, alter systems, select final tailoring, authorize production changes, accept risk or an exception, make a compliance conclusion, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [CIS Benchmarks portal](https://portal.cisecurity.org/benchmarks) as the source locator; source status, applicable product/version, access rights, and license terms must be confirmed by the designated human source owner before use. Retrieved 2026-07-31. CIS Benchmark material may be licensed or access-controlled: link to the authorized source and record only organization-created metadata, decisions, and evidence references here—never benchmark text, recommendations, scored output, or mappings.

### 1. Authorized baseline applicability and tailoring record

- **Request and owner:** A product/service inventory, deployment-environment boundary, authorized benchmark-version register, applicability rationale, tailoring decisions, approver, and exception references from platform, security, and configuration-management owners. Cover each in-scope technology at the cycle date and each newly introduced technology.
- **Validate and limit:** Trace a selected in-scope asset to its accountable owner, recorded authorized version, environment, and human-approved applicability/tailoring decision. Inspect decision timestamps and immutable change references; do not ingest licensed benchmark content. This can support that a governed selection record exists; it cannot establish correct benchmark interpretation, configuration security, or complete asset coverage.
- **AI and trigger:** AI may reconcile approved inventory metadata and flag missing owner/version links. Humans confirm source rights, applicability, tailoring, and exceptions. Refresh when a product, environment, benchmark version, ownership, or material architecture changes and at annual renewal.

### 2. Configuration-validation and remediation trace

- **Request and owner:** Authorized validation-job metadata, environment/asset identifiers, run dates, tool/version records, summarized result references, evidence integrity information, change tickets, remediation plans, and retest records from platform and security operations. Use the defined population for the approved baseline cycle, with separate records for unavailable or excluded assets.
- **Validate and limit:** Reperform a human-approved trace from one validation result reference to the asset/environment, authorized run, change or exception, and retest evidence, using least-privilege access and redacted outputs where needed. This can support traceability of the declared validation process; it cannot prove every setting is secure, a tool is accurate, or remediation is effective outside the tested condition.
- **AI and trigger:** AI may index result metadata, identify stale retests, and draft questions; it cannot run scans, change configuration, interpret protected benchmark content, or close remediation. Human owners approve test methods, production changes, and closure. Recollect after failed validation, material drift, remediation, incident, or scheduled review.

### 3. Exception, source-change, and governance record

- **Request and owner:** Time-bounded exceptions, compensating-context narratives in original language, risk decisions, approval and expiry records, supplier/product notices, source-version change monitoring, quarterly review minutes, and annual independent-review inputs from risk, procurement, security, and executive owners.
- **Validate and limit:** Inspect a selected exception through accountable approval, stated boundary, mitigation, expiry, source-change check, and retest or renewal outcome. This can support accountable exception handling; it cannot accept risk, decide license terms, establish supplier conformance, or replace independent review.
- **AI and trigger:** AI may flag expired approvals and compare approved metadata for version changes. Humans decide risk, supplier treatment, and source interpretation. Trigger on an exception expiry, publisher/source change, supplier change, material incident, or annual renewal.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
