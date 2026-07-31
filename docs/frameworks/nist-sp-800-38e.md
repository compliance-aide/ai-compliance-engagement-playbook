# NIST SP 800-38E storage-device confidentiality engagement guide

> Original operational guidance, not NIST XTS-AES specifications, a cryptographic design, an approval, or a compliance claim. Confirm current material through [NIST SP 800-38E](https://csrc.nist.gov/pubs/sp/800/38/e/final) and the organization’s approved cryptography, security, architecture, legal, and operational decisions.

## Engagement focus

Operate a governed lifecycle for in-scope storage-device confidentiality uses. Connect each use case to an approved purpose and scope, device and data context, implementation and configuration decisions, key-management dependencies, access and lifecycle controls, validation, supplier dependencies, changes, incidents, transition planning, and retirement. Explicitly document the security properties the use is intended to provide and those it is not intended to provide. A configuration extract, device inventory, vendor statement, test result, or audit log is evidence to assess; none alone proves suitable design, correct implementation, protected keying material, approved use, protected data, secure operation, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, device and data owners, key-management operations where relevant, supplier-management, legal and privacy where relevant, change-management, incident-response, and records-management roles. Operators maintain scoped device and use inventories, approved design and configuration decisions, data-flow and dependency records, implementation and validation baselines, access and audit records, supplier materials, exception and incident records, transition decisions, and retirement evidence. Reconcile devices, owners, dependencies, configurations, and suppliers quarterly; review cryptographic alerts, device or configuration changes, exceptions, incidents, transition needs, and unresolved risks at least quarterly; and complete an annual management review after material cryptographic, device, provider, threat, or publication changes. Before annual renewal, an independent reviewer samples purpose-to-implementation-to-operation-to-review traceability; auditors test supplied evidence without selecting a mode or parameters, accessing keying material, changing device configuration, approving exceptions, accepting risk, or attesting for management.

AI may organize supplied inventory, design, implementation, test, supplier, and review evidence, identify missing owners or stale decisions, and draft workpapers for human review. AI cannot select cryptographic modes or parameters, access protected material, change device configuration, approve an exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [NIST SP 800-38E publication record](https://csrc.nist.gov/pubs/sp/800/38/e/final) and approved organizational cryptography decisions; checked 2026-07-31. This original plan collects storage-device implementation and usage evidence only. It does not reproduce the publication, validate an algorithm or module, prescribe XTS-AES use or parameters, or make a conformance claim.

### 1. Device scope and protection-intent package

- **Request and owner:** Device, platform, data, and cryptography owners provide an in-scope device/service inventory, approved usage and data-context references, device-to-owner mappings, implementation/provider identifiers, key-management dependency identifiers, and documented intended and non-intended protection properties.
- **Validate and limit:** Trace a selected device or storage service from inventory through owner, declared implementation/provider, data context, key-management dependency, and protection-intent statement. This assesses record linkage only; it cannot establish data protection, correct configuration, or whether the stated properties are achieved.
- **AI and trigger:** AI may reconcile non-secret inventory metadata and flag absent owners, providers, data contexts, or protection-intent records. Humans decide device scope, cryptographic treatment, and data-risk decisions. Refresh after device onboarding, replacement, provider, data-classification, or key-management change.

### 2. Build, provisioning, and operational package

- **Request and owner:** Endpoint/platform owners provide approved build or provisioning records, deployment/configuration references that identify the declared storage protection integration, protected administrative-access records, change tickets, and non-secret operational/incident summaries.
- **Validate and limit:** Link one selected provisioning or configuration change to its approved record, device/service identity, declared implementation reference, owner, and available operational evidence. This does not access device secrets, alter a device, inspect media, validate configuration, or prove recovery or protection outcomes.
- **AI and trigger:** AI may compare supplied build and inventory metadata, and flag unlinked changes or stale ownership; it may not connect to devices, use credentials, change settings, or declare a device validated. Humans approve provisioning, exceptions, and remediation. Refresh after provisioning, configuration, incident, or operational-model change.

### 3. Supplier, media lifecycle, and exception package

- **Request and owner:** Supplier-management, security, device-operations, and records owners provide vendor/component provenance, support notices, media custody/sanitization or disposition process references where applicable, exception/incident records, transition/retirement decisions, and review minutes.
- **Validate and limit:** Sample one supplier, media-lifecycle, exception, or retirement record through provenance, accountable owner review, approved action, and next-review date. This checks lifecycle accountability; it cannot verify sanitization, supplier assurance, encryption strength, or compliance.
- **AI and trigger:** AI may flag stale lifecycle records, unowned exceptions, or missing disposition links. Humans approve supplier actions, disposal, migration, risk acceptance, and external statements. Review quarterly and after material supplier, device, threat, implementation, or publication changes.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
