# FIPS 197 AES engagement guide

> Original operational guidance, not FIPS AES content, a cryptographic design, an approval, or a compliance claim. Confirm current material through [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) and the organization’s approved cryptography, security, architecture, legal, and operational decisions.

## Engagement focus

Operate a governed lifecycle for in-scope implementations of the Advanced Encryption Standard. Connect each use case to an approved purpose and scope, protected data and system context, implementation and configuration decisions, key-management dependencies, mode and protocol interfaces, access, logging, validation, supplier dependencies, changes, incidents, transition planning, and retirement. A configuration extract, implementation record, vendor statement, test result, or audit log is evidence to assess; none alone proves suitable algorithm use, correct implementation, protected keying material, approved use, secure operation, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, application and data owners, key-management operations where relevant, supplier-management, legal and privacy where relevant, change-management, incident-response, and records-management roles. Operators maintain scoped use inventories, approved design and configuration decisions, dependency and interface records, implementation and validation baselines, access and audit records, supplier materials, exception and incident records, transition decisions, and retirement evidence. Reconcile uses, owners, dependencies, interfaces, and suppliers quarterly; review cryptographic alerts, implementation changes, exceptions, incidents, transition needs, and unresolved risks at least quarterly; and complete an annual management review after material cryptographic, product, provider, threat, or publication changes. Before annual renewal, an independent reviewer samples purpose-to-implementation-to-operation-to-review traceability; auditors test supplied evidence without selecting an algorithm or parameters, accessing keying material, changing configuration, approving exceptions, accepting risk, or attesting for management.

AI may organize supplied inventory, design, implementation, test, supplier, and review evidence, identify missing owners or stale decisions, and draft workpapers for human review. AI cannot select an algorithm or parameters, access protected material, change cryptographic configuration, approve an exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** Use the current [FIPS 197 publication record](https://csrc.nist.gov/pubs/fips/197/final), public NIST material retrieved 2026-07-31. This is original engagement guidance, not AES specification text, an implementation recipe, or a cryptographic approval. Architecture, cryptography, and data owners determine approved use and deployment scope.

### 1. Encryption-use and protection-boundary package

- **Request and owner:** Data, application, infrastructure, and cryptography owners provide an in-scope encryption-use inventory, protected-data classification reference, declared boundary, service or component association, approved purpose, and responsible owner.
- **Validate and limit:** Trace a selected inventory item to its system/data context, declared boundary, and approved use record without collecting keys or plaintext. This can support inventory and ownership traceability; it cannot prove all data is protected, correct implementation, or appropriate cryptographic architecture.
- **AI and trigger:** AI may organize inventory data and flag absent classification or ownership. Human authorities decide scope and design. Refresh after new data use, system migration, integration, or architecture change.

### 2. Key-management dependency and configuration package

- **Request and owner:** Key-management, platform, engineering, and supplier owners provide approved integration references, protected configuration/baseline identifiers, access-governance records, rotation/lifecycle references, and supplier service documentation.
- **Validate and limit:** Inspect a selected deployed service’s recorded configuration baseline and key-management dependency through authorized metadata only. This can show a documented dependency and review path; it cannot expose or test secret material, validate a configuration, or establish key security.
- **AI and trigger:** AI may compare approved identifiers with supplied deployment metadata and flag drift. Authorized humans decide configuration, access, and remediation. Refresh after rotation, configuration change, supplier change, or security finding.

### 3. Change, assurance, and exception package

- **Request and owner:** Change management, quality, security, risk, and records owners provide release/change approvals, permitted test observations, supplier notices, exceptions, incidents, and annual management-review evidence.
- **Validate and limit:** Trace a selected change or exception from stated impact through approval, implementation record, review, and follow-up. This can support a controlled governance trail; it cannot make a conformance conclusion, approve risk, or prove operation across the population.
- **AI and trigger:** AI may flag unmatched changes, stale exceptions, and unassigned remediation. Humans decide exception and risk outcomes. Refresh after a material release, incident, supplier notice, publication change, or annual renewal.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
