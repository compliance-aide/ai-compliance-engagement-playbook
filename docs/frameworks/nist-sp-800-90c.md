# NIST SP 800-90C random-bit-generator engagement guide

> Original operational guidance, not NIST RBG construction content, random-number-generator implementation instructions, a validation claim, or a compliance claim. Confirm current requirements through [NIST SP 800-90C](https://csrc.nist.gov/pubs/sp/800/90/c/final) and the organization’s approved security, cryptography, engineering, procurement, and operational decisions.

## Engagement focus

Operate a governed lifecycle for in-scope random-bit-generator constructions and their dependency on approved deterministic mechanisms, entropy sources, modules, providers, and applications. Maintain traceability from intended use through component identity and version, approved construction baseline, test and validation evidence, health and monitoring records, deployment and change history, incidents, supplier dependencies, and retirement decisions. A passing test, generated output, or provider assertion is evidence to assess; it does not prove construction suitability, cryptographic strength in context, validation, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, application and product owners, procurement, supplier-management, change-management, incident-response, and records-management roles. Operators maintain an in-scope construction inventory, component and dependency records, approved version and configuration baselines, test and validation-status evidence, operational health records, change approvals, supplier assurance, exception decisions, incidents, and system-to-construction traceability. Reconcile constructions, components, owners, and deployed versions quarterly; review health anomalies, validation status, supplier notices, configuration changes, exceptions, and unresolved risks at least quarterly; and complete an annual management review after material system, module, provider, cryptographic, or threat changes. Before annual renewal, an independent reviewer samples inventory-to-deployment-to-test traceability; auditors test the evidence trail without generating random values, accessing cryptographic material, changing production configuration, approving exceptions, accepting risk, or attesting for management.

AI may organize supplied inventory, dependency, test, supplier, health, and review evidence, identify missing ownership or stale validation-status records, and draft workpapers for human review. AI cannot design or implement an RBG, generate or access cryptographic material, change production configuration, determine validation, approve an exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
