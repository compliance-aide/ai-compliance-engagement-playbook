# NIST SP 800-38B CMAC engagement guide

> Original operational guidance, not NIST CMAC specifications, a cryptographic design, an approval, or a compliance claim. Confirm current material through [NIST SP 800-38B](https://csrc.nist.gov/pubs/sp/800/38/b/upd1/final) and the organization’s approved cryptography, security, architecture, legal, and operational decisions.

## Engagement focus

Operate a governed lifecycle for in-scope uses of cipher-based message authentication. Connect each use case to an approved purpose and scope, protected-message context, implementation and configuration decisions, key-management and tag-handling dependencies, interfaces, access, logging, validation, supplier dependencies, changes, incidents, transition planning, and retirement. A configuration extract, implementation record, vendor statement, test result, or audit log is evidence to assess; none alone proves suitable authentication design, correct implementation, protected keying material, approved use, message integrity, secure operation, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, application and data owners, key-management operations where relevant, supplier-management, legal and privacy where relevant, change-management, incident-response, and records-management roles. Operators maintain scoped use inventories, approved design and configuration decisions, message-flow and dependency records, implementation and test baselines, access and audit records, supplier materials, exception and incident records, transition decisions, and retirement evidence. Reconcile uses, owners, dependencies, interfaces, and suppliers quarterly; review authentication failures, implementation changes, exceptions, incidents, transition needs, and unresolved risks at least quarterly; and complete an annual management review after material cryptographic, product, provider, threat, or publication changes. Before annual renewal, an independent reviewer samples purpose-to-implementation-to-operation-to-review traceability; auditors test supplied evidence without selecting an authentication mode or parameters, accessing keying material, changing configuration, approving exceptions, accepting risk, or attesting for management.

AI may organize supplied inventory, design, implementation, test, supplier, and review evidence, identify missing owners or stale decisions, and draft workpapers for human review. AI cannot select an authentication mode or parameters, access protected material, change configuration, approve an exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [NIST SP 800-38B publication record](https://csrc.nist.gov/pubs/sp/800/38/b/upd1/final) and approved organizational cryptography decisions; checked 2026-07-31. This original plan collects implementation and usage evidence only. It does not reproduce the publication, validate an algorithm or module, prescribe CMAC use or parameters, or make a conformance claim.

### 1. Protected-message use package

- **Request and owner:** Application and cryptography owners provide the declared message-protection use inventory, approved sender/receiver and interface references, data/message-flow diagrams, library/version references, key-management dependency identifiers, and named owners.
- **Validate and limit:** Trace a selected declared message flow from approved purpose through sender and receiver implementation references to its named library and key-management interface. This evaluates record linkage only; it cannot establish message integrity, correct tag handling, or suitable design.
- **AI and trigger:** AI may reconcile supplied, non-secret metadata and flag unmapped senders, receivers, owners, or versions. Human cryptography, architecture, and application owners decide scope and technical treatment. Refresh after a new message path, integration, library, or key-management change.

### 2. Release and operational-observability package

- **Request and owner:** Platform and application owners provide build and deployment identifiers, approved change records, configuration references identifying the declared CMAC integration, protected access-change records, and non-secret failure/exception summaries.
- **Validate and limit:** Link one release to an approved change, deployment identity, declared integration reference, owner, and available operational record, documenting gaps. This does not recompute tags, access key material, test an implementation, or validate an authentication result.
- **AI and trigger:** AI may compare release metadata and surface absent approvals or stale ownership; it may not use credentials, modify configuration, or classify any implementation as validated. Humans approve releases, exceptions, and fixes. Refresh after release, operational anomaly, provider, or interface change.

### 3. Supplier, incident, and retirement package

- **Request and owner:** Supplier-management, security, and records owners provide library/supplier provenance, support or vulnerability notices, incident and exception references, migration/retirement decisions, review minutes, and retention locations.
- **Validate and limit:** Sample one supplier notice, exception, or retirement decision through source provenance, accountable review, approved action, and next review. This supports lifecycle accountability; it cannot establish supplier security, algorithm assurance, or compliance.
- **AI and trigger:** AI may flag stale supplier records, overdue decisions, or incomplete corrective-action links. Humans decide remediation, migration, risk acceptance, and communications. Review quarterly and after material supplier, threat, implementation, or publication changes.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
