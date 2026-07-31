# NIST SP 800-90B entropy-source engagement guide

> Original operational guidance, not NIST entropy-source content, random-number-generator implementation instructions, a validation claim, or a compliance claim. Confirm current requirements and errata through [NIST SP 800-90B](https://csrc.nist.gov/pubs/sp/800/90/b/final) and the organization’s approved security, cryptography, engineering, procurement, and operational decisions.

## Engagement focus

Operate a governed inventory and assurance cycle for in-scope entropy sources used by cryptographic random-bit generation. Maintain traceability from product or system use through source and module identity, version, approved design and deployment baseline, health and validation evidence, operational monitoring, changes, incidents, supplier dependencies, and lifecycle review. A vendor assertion, test result, or health signal is evidence to assess; it does not prove sufficient entropy in a deployed context, correct implementation, validation status, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, product or system owners, procurement, supplier-management, change-management, incident-response, and records-management roles. Operators maintain an in-scope source and module inventory, approved versions and configurations, test and validation-status evidence, operational health and anomaly records, change approvals, supplier assurance, exception decisions, incident records, and system-to-source traceability. Reconcile sources, owners, modules, and deployed versions quarterly; review health anomalies, validation status, supplier notices, configuration changes, exceptions, and unresolved risks at least quarterly; and complete an annual management review after material system, module, provider, cryptographic, or threat changes. Before annual renewal, an independent reviewer samples inventory-to-deployment-to-test traceability; auditors test the evidence trail without generating random values, accessing cryptographic material, changing entropy-source configuration, approving exceptions, accepting risk, or attesting for management.

AI may organize supplied inventory, test, supplier, health, and review evidence, identify missing ownership or stale validation-status records, and draft workpapers for human review. AI cannot design or implement an entropy source, generate or access cryptographic material, change production configuration, determine validation, approve an exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [NIST SP 800-90B publication record](https://csrc.nist.gov/pubs/sp/800/90/b/final) and approved organizational cryptography decisions; checked 2026-07-31. This original plan collects entropy-source inventory and operational-governance evidence only. It does not reproduce the publication, prescribe entropy-source design or testing, collect entropy samples, validate an implementation or module, or make a conformance claim.

### 1. Entropy-source and consuming-module package

- **Request and owner:** Cryptography, platform, and product owners provide a non-secret inventory of declared entropy sources, consuming modules/services, deployed versions, platform/provider identities, approved scope references, and accountable owners.
- **Validate and limit:** Trace one declared source from its platform/provider and consuming-module reference to a deployed-version record and accountable owner. This evaluates supplied record linkage; it cannot determine entropy quality, source sufficiency, correct integration, or cryptographic suitability.
- **AI and trigger:** AI may reconcile redacted inventory metadata and flag missing source, consumer, owner, version, or provider links. Humans decide scope, source treatment, and technical design. Refresh after a module, platform, provider, version, or consumer change.

### 2. Deployment change, health, and anomaly package

- **Request and owner:** Platform and operations owners provide approved change/release records, non-secret configuration/baseline references, deployment identities, available health or anomaly-monitoring records, and incident/corrective-action references.
- **Validate and limit:** Link a selected deployment or anomaly to its approved change, source/module identity, accountable owner, available health record, and documented action. This does not access or generate random material, change a source, run entropy tests, determine validation, or establish operational correctness.
- **AI and trigger:** AI may index authorized metadata and identify missing ownership, change, health-review, or corrective-action links. It may not connect to, sample, test, configure, or alter an entropy source, or treat telemetry as validation. Humans approve changes, incident response, exceptions, and remediation. Refresh after a deployment, anomaly, incident, or platform change.

### 3. Supplier status, exception, and lifecycle-review package

- **Request and owner:** Security, supplier-management, and records owners provide provider/component provenance, support or vulnerability notices, declared test/validation-status references where supplied, exceptions, transition/retirement decisions, review minutes, and retention locations.
- **Validate and limit:** Sample one provider status, notice, exception, or transition through source record, accountable review, documented action, and next-review date. This checks lifecycle accountability; it cannot determine validation status, certify a component, prove source quality, or make a compliance conclusion.
- **AI and trigger:** AI may flag stale notices, missing status dates, unresolved exceptions, and missing review links. Humans decide remediation, migration, risk acceptance, and external statements. Review quarterly and after material supplier, threat, source, module, or publication changes.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
