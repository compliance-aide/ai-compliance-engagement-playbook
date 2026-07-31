# NIST SP 800-90A Revision 1 DRBG engagement guide

> Original operational guidance, not NIST DRBG content, random-number-generator implementation instructions, a validation claim, or a compliance claim. Confirm current status and future revision activity through [NIST SP 800-90A Revision 1](https://csrc.nist.gov/pubs/sp/800/90/a/r1/final) and the organization’s approved security, cryptography, engineering, procurement, and operational decisions.

## Engagement focus

Operate a governed lifecycle for in-scope deterministic random-bit generators used by applications, cryptographic modules, platforms, services, and suppliers. Maintain traceability from intended use through generator and module identity, approved version and configuration baseline, entropy and construction dependencies, test and validation evidence, operational health, change history, supplier dependencies, and standards-status review. A passing test, generated output, or vendor statement is evidence to assess; it does not prove cryptographic suitability, correct implementation, validation, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, application and product owners, procurement, supplier-management, change-management, incident-response, and records-management roles. Operators maintain an in-scope DRBG inventory, approved versions and configurations, dependent entropy and construction records, test and validation-status evidence, operational health records, change approvals, supplier assurance, exception decisions, incidents, and system-to-generator traceability. Reconcile generators, components, owners, and deployed versions quarterly; review technical guidance status, health anomalies, validation status, supplier notices, configuration changes, exceptions, and unresolved risks at least quarterly; and complete an annual management review after material system, module, provider, cryptographic, or threat changes. Before annual renewal, an independent reviewer samples inventory-to-deployment-to-test traceability; auditors test the evidence trail without generating random values, accessing cryptographic material, changing production configuration, approving exceptions, accepting risk, or attesting for management.

AI may organize supplied inventory, dependency, test, supplier, health, and review evidence, identify missing ownership or stale standards-status records, and draft workpapers for human review. AI cannot design or implement a DRBG, generate or access cryptographic material, change production configuration, determine validation, approve an exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [NIST SP 800-90A Revision 1 publication record](https://csrc.nist.gov/pubs/sp/800/90/a/r1/final) and approved organizational cryptography decisions; checked 2026-07-31. This original plan collects DRBG inventory and operational-governance evidence only. It does not reproduce the publication, prescribe DRBG construction or parameters, generate random bits, validate an implementation or module, or make a conformance claim.

### 1. DRBG deployment and dependency package

- **Request and owner:** Cryptography, platform, and application owners provide a non-secret inventory of declared DRBG/module or provider identities, deployed versions, intended service/application use, accountable owners, and references to upstream entropy and construction dependencies.
- **Validate and limit:** Trace one declared deployment from its service/application reference through the stated DRBG/module or provider, version, dependency record, and accountable owner. This checks supplied traceability; it cannot determine correct construction, entropy sufficiency, output quality, or appropriate deployment.
- **AI and trigger:** AI may reconcile redacted metadata and flag a missing owner, version, dependency, or scope record. Humans decide technical design, deployment treatment, and scope. Refresh after a new use, module/provider, version, or dependency change.

### 2. Release, health, and operational-event package

- **Request and owner:** Platform and application owners provide approved release/change records, non-secret configuration references, deployment identities, availability of health or anomaly records, and non-secret incident or corrective-action references.
- **Validate and limit:** Link a sampled release or anomaly record to its approved change, deployment identity, accountable owner, available health record, and documented follow-up. This does not generate random values, access cryptographic material, run DRBG tests, change configuration, or establish correct operation.
- **AI and trigger:** AI may organize authorized metadata, identify missing links, and prepare questions about stale health reviews. It may not invoke a generator, access protected material, alter configuration, or interpret an event as validation. Humans approve releases, incident response, exceptions, and remediation. Refresh after a release, anomaly, incident, or platform change.

### 3. Component status, exception, and review package

- **Request and owner:** Security, supplier-management, and records owners provide component/provider provenance, support and vulnerability notices, declared test/validation-status references where supplied, exception records, management-review minutes, and retention locations.
- **Validate and limit:** Sample a component status, notice, or exception through source reference, accountable review, recorded action, and next-review date. This supports a reviewable evidence trail; it cannot determine validation status, certify a component, or establish compliance.
- **AI and trigger:** AI may flag stale notices, missing status dates, unowned exceptions, and absent follow-up. Humans decide remediation, migration, risk acceptance, and external statements. Review quarterly and after material supplier, threat, implementation, or publication changes.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
