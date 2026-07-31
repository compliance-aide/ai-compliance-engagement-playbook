# NIST SP 800-38A block-cipher-mode engagement guide

> Original operational guidance, not NIST mode specifications, a cryptographic design, an approval, or a compliance claim. Confirm current material through [NIST SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) and the organization’s approved cryptography, security, architecture, legal, and operational decisions.

## Engagement focus

Operate a governed lifecycle for in-scope uses of block-cipher modes that provide confidentiality. Connect each use case to an approved purpose and scope, data and system context, implementation and configuration decisions, initialization and input-handling dependencies, key-management interfaces, access, logging, validation, supplier dependencies, changes, incidents, transition planning, and retirement. A configuration extract, source or build record, vendor statement, test result, or audit log is evidence to assess; none alone proves suitable mode selection, correct implementation, protected keying material, approved use, secure operation, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, application and data owners, key-management operations where relevant, supplier-management, legal and privacy where relevant, change-management, incident-response, and records-management roles. Operators maintain scoped use inventories, approved design and configuration decisions, data-flow and dependency records, implementation and test baselines, access and audit records, supplier materials, exception and incident records, transition decisions, and retirement evidence. Reconcile uses, owners, dependencies, interfaces, and suppliers quarterly; review cryptographic alerts, implementation changes, exceptions, incidents, transition needs, and unresolved risks at least quarterly; and complete an annual management review after material cryptographic, product, provider, threat, or publication changes. Before annual renewal, an independent reviewer samples purpose-to-implementation-to-operation-to-review traceability; auditors test supplied evidence without selecting a mode, accessing keying material, changing configuration, approving exceptions, accepting risk, or attesting for management.

AI may organize supplied inventory, design, implementation, test, supplier, and review evidence, identify missing owners or stale decisions, and draft workpapers for human review. AI cannot select a cryptographic mode or its parameters, access protected material, change configuration, approve an exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [NIST SP 800-38A publication record](https://csrc.nist.gov/pubs/sp/800/38/a/final) and approved organizational cryptography decisions; checked 2026-07-31. This original plan collects implementation and usage evidence only. It does not reproduce the publication, validate an algorithm or module, prescribe a mode or parameter, or make a conformance claim.

### 1. Confidentiality-use and dependency package

- **Request and owner:** Cryptography and application owners provide an in-scope use inventory, approved purpose and data-flow references, calling-service and cryptographic-library/version references, key-management dependency identifiers, and named technical owners.
- **Validate and limit:** Trace a selected declared use from business purpose through the application/service reference to its named library, key-management interface, and owner. This checks traceability of supplied records; it cannot determine whether the mode choice, key handling, or implementation is correct or suitable.
- **AI and trigger:** AI may reconcile redacted inventories and flag a missing owner, unresolved dependency, or version mismatch. Named human cryptography, architecture, and application owners approve scope and technical decisions. Refresh after a new use, library, interface, data flow, or key-management change.

### 2. Deployment and input-handling evidence package

- **Request and owner:** Platform and application owners provide approved build/deployment identifiers, configuration references that identify the declared mode use, protected configuration-access records, release/change tickets, and non-secret operational telemetry or error summaries relevant to the integration.
- **Validate and limit:** Link one released implementation reference to its approved change, deployment identity, configuration reference, and current owner, recording inaccessible or absent evidence. This does not inspect secret material, execute cryptographic tests, validate input handling, or establish secure operation.
- **AI and trigger:** AI may index metadata, compare declared versions, and prepare missing-evidence questions; it may not access keys, invoke protected services, change configurations, or interpret a result as validation. Humans approve releases, exceptions, and remediation. Refresh after a release, configuration, provider, or incident change.

### 3. Lifecycle, supplier, and exception package

- **Request and owner:** Security, supplier-management, and records owners provide supplier/library provenance statements, support and vulnerability notices, exception and incident references, transition/retirement plans, review minutes, and evidence-retention locations.
- **Validate and limit:** Sample a supplier or lifecycle event through provenance, owner review, decision record, corrective action, and next-review date. This establishes an accountable evidence trail, not supplier assurance, vulnerability absence, or compliance.
- **AI and trigger:** AI may identify stale notices, expiring exceptions, and missing review links. Humans decide remediation, transition, risk acceptance, and external statements. Review quarterly and after material supplier, threat, implementation, or publication changes.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
