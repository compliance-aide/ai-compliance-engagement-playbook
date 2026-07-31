# NIST SP 800-38C CCM engagement guide

> Original operational guidance, not NIST CCM specifications, a cryptographic design, an approval, or a compliance claim. Confirm current material through [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) and the organization’s approved cryptography, security, architecture, legal, and operational decisions.

## Engagement focus

Operate a governed lifecycle for in-scope uses of authenticated encryption with associated data based on CCM. Connect each use case to an approved purpose and scope, protected data and associated-data context, implementation and configuration decisions, key-management and input-handling dependencies, interfaces, access, logging, validation, supplier dependencies, changes, incidents, transition planning, and retirement. A configuration extract, implementation record, vendor statement, test result, or audit log is evidence to assess; none alone proves suitable authenticated-encryption design, correct implementation, protected keying material, approved use, confidentiality or integrity, secure operation, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, application and data owners, key-management operations where relevant, supplier-management, legal and privacy where relevant, change-management, incident-response, and records-management roles. Operators maintain scoped use inventories, approved design and configuration decisions, data-flow and dependency records, implementation and test baselines, access and audit records, supplier materials, exception and incident records, transition decisions, and retirement evidence. Reconcile uses, owners, dependencies, interfaces, and suppliers quarterly; review authentication or decryption failures, implementation changes, exceptions, incidents, transition needs, and unresolved risks at least quarterly; and complete an annual management review after material cryptographic, product, provider, threat, or publication changes. Before annual renewal, an independent reviewer samples purpose-to-implementation-to-operation-to-review traceability; auditors test supplied evidence without selecting a mode or parameters, accessing keying material, changing configuration, approving exceptions, accepting risk, or attesting for management.

AI may organize supplied inventory, design, implementation, test, supplier, and review evidence, identify missing owners or stale decisions, and draft workpapers for human review. AI cannot select an authenticated-encryption mode or parameters, access protected material, change configuration, approve an exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [NIST SP 800-38C publication record](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) and approved organizational cryptography decisions; checked 2026-07-31. This original plan collects implementation and usage evidence only. It does not reproduce the publication, validate an algorithm or module, prescribe CCM inputs or parameters, or make a conformance claim.

### 1. AEAD use and associated-data package

- **Request and owner:** Application, data, and cryptography owners provide an inventory of declared CCM uses, approved purpose/data-flow references, associated-data and interface descriptions at a non-secret design level, library/version references, key-management dependencies, and named owners.
- **Validate and limit:** Trace a selected declared use from purpose and data flow to its application/library reference, associated-data design reference, key-management interface, and owner. This checks evidentiary linkage; it cannot determine that confidentiality or integrity is achieved, that inputs are correct, or that the design is suitable.
- **AI and trigger:** AI may organize supplied metadata and flag a missing data owner, dependency, or version reference. Humans approve data treatment, cryptographic decisions, and scope. Refresh after new data, associated-data, integration, library, or key-management changes.

### 2. Release and failure-handling package

- **Request and owner:** Application and platform owners provide approved change/release records, deployment identifiers, configuration references identifying the declared integration, access-control records for protected configuration, and non-secret decryption/authentication failure handling and incident references.
- **Validate and limit:** Link one deployment to its approved change, implementation reference, configuration reference, owner, and documented operational handling path. This cannot execute encryption/decryption, inspect keys, validate error treatment, or establish secure operation.
- **AI and trigger:** AI may identify missing links or stale release metadata and draft review questions; it may not invoke services, access protected material, alter configurations, or make validation claims. Humans approve releases, exceptions, and remediation. Refresh after release, material failure, incident, or service-provider change.

### 3. Dependency and lifecycle package

- **Request and owner:** Security, supplier-management, and records owners provide component provenance, dependency/support notices, exception records, transition/retirement plans, review decisions, and evidence-retention references.
- **Validate and limit:** Sample a component or lifecycle event from source provenance through accountable review, action record, and next-review date. This demonstrates governance traceability only; it cannot certify a dependency, prove vulnerability absence, or decide residual risk.
- **AI and trigger:** AI may flag stale component records, expiring exceptions, and absent lifecycle owners. Humans determine transition, remediation, risk acceptance, and external communication. Review quarterly and after material dependency, threat, implementation, or publication changes.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
