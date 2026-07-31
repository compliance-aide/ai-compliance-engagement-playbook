# NIST SP 800-38D GCM and GMAC engagement guide

> Original operational guidance, not NIST GCM or GMAC specifications, a cryptographic design, an approval, or a compliance claim. Confirm current material through [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) and the organization’s approved cryptography, security, architecture, legal, and operational decisions.

## Engagement focus

Operate a governed lifecycle for in-scope uses of GCM authenticated encryption and GMAC message authentication. Connect each use case to an approved purpose and scope, protected data and associated-data context, implementation and configuration decisions, key-management and input-handling dependencies, interfaces, access, logging, validation, supplier dependencies, changes, incidents, transition planning, and retirement. A configuration extract, implementation record, vendor statement, test result, or audit log is evidence to assess; none alone proves suitable mode selection, correct implementation, protected keying material, approved use, confidentiality or integrity, secure operation, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, application and data owners, key-management operations where relevant, supplier-management, legal and privacy where relevant, change-management, incident-response, and records-management roles. Operators maintain scoped use inventories, approved design and configuration decisions, data-flow and dependency records, implementation and test baselines, access and audit records, supplier materials, exception and incident records, transition decisions, and retirement evidence. Reconcile uses, owners, dependencies, interfaces, and suppliers quarterly; review authentication or decryption failures, implementation changes, exceptions, incidents, transition needs, and unresolved risks at least quarterly; and complete an annual management review after material cryptographic, product, provider, threat, or publication changes. Before annual renewal, an independent reviewer samples purpose-to-implementation-to-operation-to-review traceability; auditors test supplied evidence without selecting a mode or parameters, accessing keying material, changing configuration, approving exceptions, accepting risk, or attesting for management.

AI may organize supplied inventory, design, implementation, test, supplier, and review evidence, identify missing owners or stale decisions, and draft workpapers for human review. AI cannot select an authenticated-encryption or authentication mode or parameters, access protected material, change configuration, approve an exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [NIST SP 800-38D publication record](https://csrc.nist.gov/pubs/sp/800/38/d/final) and approved organizational cryptography decisions; checked 2026-07-31. This original plan collects implementation and usage evidence only. It does not reproduce the publication, validate an algorithm or module, prescribe GCM/GMAC selection or parameters, or make a conformance claim.

### 1. GCM/GMAC purpose and integration package

- **Request and owner:** Application and cryptography owners provide an inventory distinguishing declared GCM and GMAC uses, approved purpose and data/message-flow references, caller/receiver or service-interface references, library/version identifiers, key-management dependencies, and named owners.
- **Validate and limit:** Trace one declared use from purpose through the identified application or service integration to its library/version, key-management interface, and accountable owner. This evaluates supplied provenance; it cannot establish confidentiality, integrity, correct implementation, or appropriate mode selection.
- **AI and trigger:** AI may reconcile inventories and flag undocumented mode labels, owners, dependencies, or version mismatches. Human cryptography, architecture, and application owners decide technical design and scope. Refresh after a new use, interface, library, data flow, or key-management change.

### 2. Change and operational-evidence package

- **Request and owner:** Platform and application owners provide approved change tickets, build/release/deployment identities, configuration references identifying the declared integration, protected configuration-access records, and non-secret authentication/decryption error or incident summaries.
- **Validate and limit:** Link a selected release to its approved change, deployment record, integration/configuration reference, owner, and operational record; identify unavailable evidence. This does not process protected data, access keys, conduct cryptographic testing, validate nonces or tags, or establish secure operation.
- **AI and trigger:** AI may index approved metadata and detect missing linkage or stale records. It may not access secrets, call cryptographic operations, change configuration, or treat telemetry as validation. Humans approve releases, exceptions, and corrective actions. Refresh after a release, incident, material error pattern, or provider change.

### 3. Supplier, exception, and transition package

- **Request and owner:** Security, supplier-management, and records owners provide component/vendor provenance, support or vulnerability notices, exception/incident records, transition and retirement decisions, review minutes, and evidence-retention references.
- **Validate and limit:** Sample one component, exception, or transition event through provenance, accountable challenge/review, decision, action, and next-review date. This supports responsible oversight; it cannot certify supplier controls, validate the module, or accept risk.
- **AI and trigger:** AI may flag stale notices, unowned exceptions, or missing follow-up. Humans decide remediation, migration, risk acceptance, and public statements. Review quarterly and after material supplier, threat, implementation, or publication changes.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
