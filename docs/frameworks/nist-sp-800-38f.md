# NIST SP 800-38F key-wrapping engagement guide

> Original operational guidance, not NIST key-wrapping specifications, a cryptographic design, an approval, or a compliance claim. Confirm current material through [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) and the organization’s approved cryptography, security, architecture, legal, and operational decisions.

## Engagement focus

Operate a governed lifecycle for in-scope cryptographic-key-wrapping uses. Connect each use to an approved purpose and scope, protected-key and associated-data context, implementation and configuration decisions, wrapping-key dependencies, interfaces and transfer paths, access, logging, validation, supplier dependencies, changes, incidents, transition planning, and retirement. A configuration extract, implementation record, supplier statement, test result, or audit log is evidence to assess; none alone proves suitable wrapping design, correct implementation, protected keys, approved use, secure operation, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, key-management operations, application and data owners, supplier-management, legal and privacy where relevant, change-management, incident-response, and records-management roles. Operators maintain scoped use inventories, approved design and configuration decisions, key and interface dependency records, implementation and validation baselines, access and audit records, supplier materials, exception and incident records, transition decisions, and retirement evidence. Reconcile uses, owners, dependencies, interfaces, and suppliers quarterly; review key-handling alerts, implementation changes, exceptions, incidents, transition needs, and unresolved risks at least quarterly; and complete an annual management review after material cryptographic, product, provider, threat, or publication changes. Before annual renewal, an independent reviewer samples purpose-to-implementation-to-operation-to-review traceability; auditors test supplied evidence without wrapping or accessing keys, selecting modes or parameters, changing configuration, approving exceptions, accepting risk, or attesting for management.

AI may organize supplied inventory, design, implementation, test, supplier, and review evidence, identify missing owners or stale decisions, and draft workpapers for human review. AI cannot select a wrapping method or parameters, wrap or access keys, change cryptographic configuration, approve an exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
