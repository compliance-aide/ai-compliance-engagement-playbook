# NIST SP 800-38A block-cipher-mode engagement guide

> Original operational guidance, not NIST mode specifications, a cryptographic design, an approval, or a compliance claim. Confirm current material through [NIST SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) and the organization’s approved cryptography, security, architecture, legal, and operational decisions.

## Engagement focus

Operate a governed lifecycle for in-scope uses of block-cipher modes that provide confidentiality. Connect each use case to an approved purpose and scope, data and system context, implementation and configuration decisions, initialization and input-handling dependencies, key-management interfaces, access, logging, validation, supplier dependencies, changes, incidents, transition planning, and retirement. A configuration extract, source or build record, vendor statement, test result, or audit log is evidence to assess; none alone proves suitable mode selection, correct implementation, protected keying material, approved use, secure operation, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, application and data owners, key-management operations where relevant, supplier-management, legal and privacy where relevant, change-management, incident-response, and records-management roles. Operators maintain scoped use inventories, approved design and configuration decisions, data-flow and dependency records, implementation and test baselines, access and audit records, supplier materials, exception and incident records, transition decisions, and retirement evidence. Reconcile uses, owners, dependencies, interfaces, and suppliers quarterly; review cryptographic alerts, implementation changes, exceptions, incidents, transition needs, and unresolved risks at least quarterly; and complete an annual management review after material cryptographic, product, provider, threat, or publication changes. Before annual renewal, an independent reviewer samples purpose-to-implementation-to-operation-to-review traceability; auditors test supplied evidence without selecting a mode, accessing keying material, changing configuration, approving exceptions, accepting risk, or attesting for management.

AI may organize supplied inventory, design, implementation, test, supplier, and review evidence, identify missing owners or stale decisions, and draft workpapers for human review. AI cannot select a cryptographic mode or its parameters, access protected material, change configuration, approve an exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
