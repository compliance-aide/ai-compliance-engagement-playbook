# FIPS 198-1 HMAC engagement guide

> Original operational guidance, not FIPS content, HMAC implementation instructions, a cryptographic approval, a validation claim, or a compliance claim. Confirm current status and successor guidance through [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) and the organization’s approved security, cryptography, architecture, legal, and operational decisions.

## Engagement focus

Manage the approved use of keyed-hash message authentication across in-scope applications, interfaces, APIs, services, devices, and suppliers. Maintain traceability from business purpose and protected message flow to owner, implementation or module, key lifecycle reference, verification behavior, deployment environment, change history, exceptions, and current standards-status review. A passing test, successful verification, or provider statement is evidence to assess; it does not prove secure implementation, correct key handling, complete coverage, validation, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, application and service owners, identity, procurement, supplier-management, change-management, incident-response, legal and privacy where relevant, and records-management roles. Operators maintain an in-scope use inventory, approved purpose and ownership records, module or provider baselines, key-lifecycle references, deployment and verification evidence, standards-status assessments, supplier assurance, exception decisions, and system-to-use traceability. Reconcile uses, owners, dependencies, and deployed versions quarterly; review technical guidance status, key and access changes, failed verifications, provider notices, exceptions, and unresolved risks at least quarterly; and complete an annual management review after material application, protocol, cryptographic, supplier, or standards changes. Before annual renewal, an independent reviewer samples use-to-deployment-to-review traceability; auditors test evidence without creating or accessing keys, changing cryptography, approving exceptions, accepting risk, or attesting for management.

AI may organize supplied inventory, lifecycle, verification, supplier, and review evidence, identify missing ownership or stale standards-status assessments, and draft workpapers for human review. AI cannot design or implement cryptography, create or access keys, configure production systems, approve an exception, decide migration timing, accept risk, make a compliance conclusion, attest for management, or replace independent review.


<!-- evidence-plan: generated-draft -->
## Tailored evidence plan

**Plan status:** Draft generated from this guide's existing engagement focus; it requires independent source and skeptical review before a final catalog claim.

**Source and rights snapshot.** Use the guide's cited publisher source (https://csrc.nist.gov/pubs/fips/198-1/final) and check its current edition or status before use. This plan uses original operational language and does not reproduce protected requirements, assessment questions, mappings, or branded templates. A named human engagement owner confirms applicability and source rights.

**Guide-specific planning input.** Manage the approved use of keyed-hash message authentication across in-scope applications, interfaces, APIs, services, devices, and suppliers. Maintain traceability from business purpose and protected message flow to owner, implementation or module, key lifecycle reference, verification behavior, deployment environment, change history, exceptions, and current standards-status review. A passing test, successful verification, or provider statement is evidence to assess; it does not prove secure implementation, correct key handling, complete coverage, validation, or compliance.

### 1. Applicability and boundary evidence

- **Request and owner:** A dated record of the applicable product or operational boundary, asset/process population, safety constraint, supplier, and change window, exclusions, inherited responsibilities, and accountable human owners, maintained by engineering, safety, operations, and supplier owners.
- **Validate and limit:** Trace a human-approved selection from the declared boundary to source systems or operating records; preserve population, period, access restriction, and unresolved-boundary notes. This can support a bounded engagement scope. It cannot decide legal applicability, publisher acceptance, certification, or completeness beyond the documented population.
- **AI and trigger:** AI may organize approved metadata and flag inconsistent boundaries. Humans approve scope and exclusions. Refresh after product, asset, supplier, safety condition, maintenance window, or incident change.

### 2. Operating evidence for FIPS 198-1 HMAC

- **Request and owner:** Time-bounded design/operating records, asset/configuration, maintenance, test/exercise, supplier, and corrective-action records, selected because this guide focuses on manage the approved use of keyed-hash message authentication across in-scope applications, interfaces, apis, services, devices, and suppliers. maintain traceability from business purpose and protected message flow to owner, implementation or module, key lifecycle reference, verification behavior, deployment environment, change history, exceptions, and current standards-status review. a passing test, successful verification, or provider statement is evidence to assess; it does not prove secure implementation, correct key handling, complete coverage, validation, or compliance., from engineering, safety, operations, and supplier owners.
- **Validate and limit:** Inspect provenance and freshness, then trace a human-approved sample to its source record, accountable owner, and exception or follow-up path. This can support that the stated practice has observable evidence. It cannot prove continuous effectiveness, satisfy an assessor by itself, or support an unreviewed conformance claim.
- **AI and trigger:** AI may create a read-only evidence index, identify gaps, and draft questions; it may not alter systems, close findings, or create external representations. Recollect after product, asset, supplier, safety condition, maintenance window, or incident change.

### 3. Decisions, exceptions, and renewal evidence

- **Request and owner:** Approved risk or exception decisions, corrective-action and retest records, source-change watch, and annual review or renewal record from engineering, safety, operations, and supplier owners.
- **Validate and limit:** Trace a selected exception or remediation item to a named human decision, due date, expiry, evidence source, and retest result. This can support accountable follow-through. It cannot accept residual risk, make a legal decision, or replace an independent assessment.
- **AI and trigger:** AI may flag stale approvals and assemble a review packet. Humans approve risk treatment, submissions, attestations, and closure. Revisit on product, asset, supplier, safety condition, maintenance window, or incident change.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
