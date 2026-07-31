# NIST SP 800-38F key-wrapping engagement guide

> Original operational guidance, not NIST key-wrapping specifications, a cryptographic design, an approval, or a compliance claim. Confirm current material through [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) and the organization’s approved cryptography, security, architecture, legal, and operational decisions.

## Engagement focus

Operate a governed lifecycle for in-scope cryptographic-key-wrapping uses. Connect each use to an approved purpose and scope, protected-key and associated-data context, implementation and configuration decisions, wrapping-key dependencies, interfaces and transfer paths, access, logging, validation, supplier dependencies, changes, incidents, transition planning, and retirement. A configuration extract, implementation record, supplier statement, test result, or audit log is evidence to assess; none alone proves suitable wrapping design, correct implementation, protected keys, approved use, secure operation, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, key-management operations, application and data owners, supplier-management, legal and privacy where relevant, change-management, incident-response, and records-management roles. Operators maintain scoped use inventories, approved design and configuration decisions, key and interface dependency records, implementation and validation baselines, access and audit records, supplier materials, exception and incident records, transition decisions, and retirement evidence. Reconcile uses, owners, dependencies, interfaces, and suppliers quarterly; review key-handling alerts, implementation changes, exceptions, incidents, transition needs, and unresolved risks at least quarterly; and complete an annual management review after material cryptographic, product, provider, threat, or publication changes. Before annual renewal, an independent reviewer samples purpose-to-implementation-to-operation-to-review traceability; auditors test supplied evidence without wrapping or accessing keys, selecting modes or parameters, changing configuration, approving exceptions, accepting risk, or attesting for management.

AI may organize supplied inventory, design, implementation, test, supplier, and review evidence, identify missing owners or stale decisions, and draft workpapers for human review. AI cannot select a wrapping method or parameters, wrap or access keys, change cryptographic configuration, approve an exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [NIST SP 800-38F publication record](https://csrc.nist.gov/pubs/sp/800/38/f/final) and approved organizational cryptography decisions; checked 2026-07-31. This original plan collects key-wrapping implementation and usage evidence only. It does not reproduce the publication, validate an algorithm or module, prescribe a wrapping method or parameters, or make a conformance claim.

### 1. Protected-key purpose and dependency package

- **Request and owner:** Cryptography, application, and key-management owners provide an inventory of declared protected-key transfer or storage uses, approved purpose references, caller and receiver/service identifiers, cryptographic-library or provider/version identifiers, wrapping-key dependency references, and named owners.
- **Validate and limit:** Trace one declared use from purpose through its identified caller, receiver or service, library/provider, and wrapping-key-management dependency. This evaluates supplied record linkage; it cannot establish that a wrapping method, key relationship, implementation, or protected-key handling is appropriate or correct.
- **AI and trigger:** AI may reconcile redacted inventory metadata and flag missing owners, endpoints, dependencies, or version links. Humans decide scope and technical treatment. Refresh after a new use, integration, provider, library, or key-management change.

### 2. Release and key-transfer-operation package

- **Request and owner:** Platform and application owners provide approved change records, build/release/deployment identities, non-secret configuration references identifying the declared integration, protected administrative-access records, and non-secret transfer failure or incident summaries.
- **Validate and limit:** Link one selected release or transfer-path change to its approved change, deployed identity, configuration reference, accountable owner, and available operational record. This does not unwrap or access keys, inspect secret material, run cryptographic operations, validate a transfer, or establish secure operation.
- **AI and trigger:** AI may index metadata and identify unlinked changes, unavailable records, or stale ownership. It may not access keys, call cryptographic services, alter configuration, or treat telemetry as validation. Humans approve releases, exceptions, and corrective actions. Refresh after a release, transfer-path change, incident, or provider change.

### 3. Component, incident, and transition package

- **Request and owner:** Security, supplier-management, and records owners provide component/provider provenance, support or vulnerability notices, exception and incident references, transition or retirement decisions, review minutes, and evidence-retention locations.
- **Validate and limit:** Sample a component, incident, exception, or transition event through provenance, owner review, recorded action, and next-review date. This supports accountable lifecycle evidence; it cannot establish component assurance, absence of vulnerabilities, key protection, or compliance.
- **AI and trigger:** AI may flag stale notices, unowned exceptions, and missing follow-up. Humans decide remediation, migration, risk acceptance, and external statements. Review quarterly and after material supplier, threat, implementation, or publication changes.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
