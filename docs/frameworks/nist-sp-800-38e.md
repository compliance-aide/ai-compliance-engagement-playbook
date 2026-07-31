# NIST SP 800-38E storage-device confidentiality engagement guide

> Original operational guidance, not NIST XTS-AES specifications, a cryptographic design, an approval, or a compliance claim. Confirm current material through [NIST SP 800-38E](https://csrc.nist.gov/pubs/sp/800/38/e/final) and the organization’s approved cryptography, security, architecture, legal, and operational decisions.

## Engagement focus

Operate a governed lifecycle for in-scope storage-device confidentiality uses. Connect each use case to an approved purpose and scope, device and data context, implementation and configuration decisions, key-management dependencies, access and lifecycle controls, validation, supplier dependencies, changes, incidents, transition planning, and retirement. Explicitly document the security properties the use is intended to provide and those it is not intended to provide. A configuration extract, device inventory, vendor statement, test result, or audit log is evidence to assess; none alone proves suitable design, correct implementation, protected keying material, approved use, protected data, secure operation, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, device and data owners, key-management operations where relevant, supplier-management, legal and privacy where relevant, change-management, incident-response, and records-management roles. Operators maintain scoped device and use inventories, approved design and configuration decisions, data-flow and dependency records, implementation and validation baselines, access and audit records, supplier materials, exception and incident records, transition decisions, and retirement evidence. Reconcile devices, owners, dependencies, configurations, and suppliers quarterly; review cryptographic alerts, device or configuration changes, exceptions, incidents, transition needs, and unresolved risks at least quarterly; and complete an annual management review after material cryptographic, device, provider, threat, or publication changes. Before annual renewal, an independent reviewer samples purpose-to-implementation-to-operation-to-review traceability; auditors test supplied evidence without selecting a mode or parameters, accessing keying material, changing device configuration, approving exceptions, accepting risk, or attesting for management.

AI may organize supplied inventory, design, implementation, test, supplier, and review evidence, identify missing owners or stale decisions, and draft workpapers for human review. AI cannot select cryptographic modes or parameters, access protected material, change device configuration, approve an exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
