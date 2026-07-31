# NIST SP 800-38C CCM engagement guide

> Original operational guidance, not NIST CCM specifications, a cryptographic design, an approval, or a compliance claim. Confirm current material through [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) and the organization’s approved cryptography, security, architecture, legal, and operational decisions.

## Engagement focus

Operate a governed lifecycle for in-scope uses of authenticated encryption with associated data based on CCM. Connect each use case to an approved purpose and scope, protected data and associated-data context, implementation and configuration decisions, key-management and input-handling dependencies, interfaces, access, logging, validation, supplier dependencies, changes, incidents, transition planning, and retirement. A configuration extract, implementation record, vendor statement, test result, or audit log is evidence to assess; none alone proves suitable authenticated-encryption design, correct implementation, protected keying material, approved use, confidentiality or integrity, secure operation, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, application and data owners, key-management operations where relevant, supplier-management, legal and privacy where relevant, change-management, incident-response, and records-management roles. Operators maintain scoped use inventories, approved design and configuration decisions, data-flow and dependency records, implementation and test baselines, access and audit records, supplier materials, exception and incident records, transition decisions, and retirement evidence. Reconcile uses, owners, dependencies, interfaces, and suppliers quarterly; review authentication or decryption failures, implementation changes, exceptions, incidents, transition needs, and unresolved risks at least quarterly; and complete an annual management review after material cryptographic, product, provider, threat, or publication changes. Before annual renewal, an independent reviewer samples purpose-to-implementation-to-operation-to-review traceability; auditors test supplied evidence without selecting a mode or parameters, accessing keying material, changing configuration, approving exceptions, accepting risk, or attesting for management.

AI may organize supplied inventory, design, implementation, test, supplier, and review evidence, identify missing owners or stale decisions, and draft workpapers for human review. AI cannot select an authenticated-encryption mode or parameters, access protected material, change configuration, approve an exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.


<!-- evidence-plan: generated-draft -->
## Tailored evidence plan

**Plan status:** Draft generated from this guide's existing engagement focus; it requires independent source and skeptical review before a final catalog claim.

**Source and rights snapshot.** Use the guide's cited publisher source (https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) and check its current edition or status before use. This plan uses original operational language and does not reproduce protected requirements, assessment questions, mappings, or branded templates. A named human engagement owner confirms applicability and source rights.

**Guide-specific planning input.** Operate a governed lifecycle for in-scope uses of authenticated encryption with associated data based on CCM. Connect each use case to an approved purpose and scope, protected data and associated-data context, implementation and configuration decisions, key-management and input-handling dependencies, interfaces, access, logging, validation, supplier dependencies, changes, incidents, transition planning, and retirement. A configuration extract, implementation record, vendor statement, test result, or audit log is evidence to assess; none alone proves suitable authenticated-encryption design, correct implementation, protected keying material, approved use, confidentiality or integrity, secure operation, or compliance.

### 1. Applicability and boundary evidence

- **Request and owner:** A dated record of the applicable business activity, product, customer, system, third-party, and decision boundary, exclusions, inherited responsibilities, and accountable human owners, maintained by business, risk, compliance, finance, and operational owners.
- **Validate and limit:** Trace a human-approved selection from the declared boundary to source systems or operating records; preserve population, period, access restriction, and unresolved-boundary notes. This can support a bounded engagement scope. It cannot decide legal applicability, publisher acceptance, certification, or completeness beyond the documented population.
- **AI and trigger:** AI may organize approved metadata and flag inconsistent boundaries. Humans approve scope and exclusions. Refresh after product, customer, supplier, material event, regulatory update, or control change.

### 2. Operating evidence for NIST SP 800-38C CCM

- **Request and owner:** Time-bounded governance, transaction/process, access/change, exception, supervisory-review, and remediation records, selected because this guide focuses on operate a governed lifecycle for in-scope uses of authenticated encryption with associated data based on ccm. connect each use case to an approved purpose and scope, protected data and associated-data context, implementation and configuration decisions, key-management and input-handling dependencies, interfaces, access, logging, validation, supplier dependencies, changes, incidents, transition planning, and retirement. a configuration extract, implementation record, vendor statement, test result, or audit log is evidence to assess; none alone proves suitable authenticated-encryption design, correct implementation, protected keying material, approved use, confidentiality or integrity, secure operation, or compliance., from business, risk, compliance, finance, and operational owners.
- **Validate and limit:** Inspect provenance and freshness, then trace a human-approved sample to its source record, accountable owner, and exception or follow-up path. This can support that the stated practice has observable evidence. It cannot prove continuous effectiveness, satisfy an assessor by itself, or support an unreviewed conformance claim.
- **AI and trigger:** AI may create a read-only evidence index, identify gaps, and draft questions; it may not alter systems, close findings, or create external representations. Recollect after product, customer, supplier, material event, regulatory update, or control change.

### 3. Decisions, exceptions, and renewal evidence

- **Request and owner:** Approved risk or exception decisions, corrective-action and retest records, source-change watch, and annual review or renewal record from business, risk, compliance, finance, and operational owners.
- **Validate and limit:** Trace a selected exception or remediation item to a named human decision, due date, expiry, evidence source, and retest result. This can support accountable follow-through. It cannot accept residual risk, make a legal decision, or replace an independent assessment.
- **AI and trigger:** AI may flag stale approvals and assemble a review packet. Humans approve risk treatment, submissions, attestations, and closure. Revisit on product, customer, supplier, material event, regulatory update, or control change.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
