# FIPS 205 post-quantum hash-based signature engagement guide

> Original operational guidance, not FIPS content, SLH-DSA implementation instructions, a cryptographic approval, a validation claim, or a compliance claim. Confirm current requirements through [FIPS 205](https://csrc.nist.gov/pubs/fips/205/final) and the organization’s approved security, cryptography, architecture, legal, and operational decisions.

## Engagement focus

Operate a governed discovery-and-migration process for in-scope digital-signature uses that may adopt FIPS 205. Connect signing purpose, signer or service identity, application and protocol dependencies, module or provider versions, test outcomes, rollout approvals, exception decisions, rollback readiness, and lifecycle evidence to accountable owners. A vendor statement, successful test, or enabled feature is evidence to assess; it does not prove suitability, interoperability, secure implementation, signer authority, legal effect, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, identity, application and service owners, legal, privacy where relevant, procurement, supplier-management, change-management, incident-response, business-continuity, and records-management roles. Operators maintain a scoped signature-use inventory, approved migration roadmap, signer and service ownership records, protocol and dependency evidence, module or provider status, test and rollout artifacts, change approvals, exception decisions, rollback evidence, and supplier assurance. Reconcile uses, owners, and dependencies quarterly; review cryptographic and provider changes, test outcomes, expiring dependencies, exceptions, supplier notices, and unresolved risks at least quarterly; and complete an annual management review after material application, protocol, provider, cryptographic, legal, or threat changes. Before annual renewal, an independent reviewer samples use-to-rollout traceability and exception handling; auditors test the evidence trail without selecting algorithms, signing on behalf of a user, accessing private keys, configuring production systems, accepting risk, or attesting for management.

AI may organize supplied inventory, test, supplier, rollout, and review evidence, identify missing ownership or stale decisions, and draft workpapers for human review. AI cannot design or implement cryptography, select parameters, sign or access private keys, determine signer authority, configure production systems, approve a migration or exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
