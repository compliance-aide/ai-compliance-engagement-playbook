# PCI DSS v4.0.1 SAQ B-IP engagement guide

> Original operational guidance, not PCI SSC content, payment-brand direction, an eligibility decision, an attestation, or a compliance claim. Confirm the current [PCI DSS v4.0.1 SAQ resources](https://www.pcisecuritystandards.org/document_library/) and validation instructions with the entity that receives the submission.

## Engagement focus

Treat SAQ B-IP as a distinct, conditional validation profile. Establish a written scope record that identifies in-scope payment channels, internet-connected payment components, their networks and locations, supporting services, provider boundaries, account-data exposure, and the exact basis for profile eligibility. Keep that record synchronized with asset, connection, change, vendor, testing, and incident evidence. Do not collapse the broader PCI DSS program into the profile workflow; the profile, scope, and submission authority must be confirmed by accountable people and the receiving entity.

## Roles and annual rhythm

Assign accountable owners for payment operations, network and device administration, security, physical operations, vendor management, finance, and incident response. Operators keep inventories, network and transaction-path records, configuration and maintenance evidence, provider documentation, access records, test results, exceptions, and incident artifacts. Review scope and operational evidence quarterly and after a payment device, network, location, provider, or channel change. Before annual validation, management confirms profile eligibility with the submission recipient; an independent reviewer samples assets, payment paths, and evidence to assess whether the stated boundary operated. Auditors test evidence and review rigor without selecting the profile or making an attestation.

AI may organize supplied evidence, reconcile inventories and change records, flag missing or conflicting documentation, and prepare review workpapers for human review. AI cannot select a profile, decide eligibility or PCI DSS scope, approve payment infrastructure, determine compliance, attest for management, or replace independent review.


<!-- evidence-plan: generated-draft -->
## Tailored evidence plan

**Plan status:** Draft generated from this guide's existing engagement focus; it requires independent source and skeptical review before a final catalog claim.

**Source and rights snapshot.** Use the guide's cited publisher source (https://www.pcisecuritystandards.org/document_library/) and check its current edition or status before use. This plan uses original operational language and does not reproduce protected requirements, assessment questions, mappings, or branded templates. A named human engagement owner confirms applicability and source rights.

**Guide-specific planning input.** Treat SAQ B-IP as a distinct, conditional validation profile. Establish a written scope record that identifies in-scope payment channels, internet-connected payment components, their networks and locations, supporting services, provider boundaries, account-data exposure, and the exact basis for profile eligibility. Keep that record synchronized with asset, connection, change, vendor, testing, and incident evidence. Do not collapse the broader PCI DSS program into the profile workflow; the profile, scope, and submission authority must be confirmed by accountable people and the receiving entity.

### 1. Applicability and boundary evidence

- **Request and owner:** A dated record of the applicable business activity, product, customer, system, third-party, and decision boundary, exclusions, inherited responsibilities, and accountable human owners, maintained by business, risk, compliance, finance, and operational owners.
- **Validate and limit:** Trace a human-approved selection from the declared boundary to source systems or operating records; preserve population, period, access restriction, and unresolved-boundary notes. This can support a bounded engagement scope. It cannot decide legal applicability, publisher acceptance, certification, or completeness beyond the documented population.
- **AI and trigger:** AI may organize approved metadata and flag inconsistent boundaries. Humans approve scope and exclusions. Refresh after product, customer, supplier, material event, regulatory update, or control change.

### 2. Operating evidence for PCI DSS v4.0.1 SAQ B-IP

- **Request and owner:** Time-bounded governance, transaction/process, access/change, exception, supervisory-review, and remediation records, selected because this guide focuses on treat saq b-ip as a distinct, conditional validation profile. establish a written scope record that identifies in-scope payment channels, internet-connected payment components, their networks and locations, supporting services, provider boundaries, account-data exposure, and the exact basis for profile eligibility. keep that record synchronized with asset, connection, change, vendor, testing, and incident evidence. do not collapse the broader pci dss program into the profile workflow; the profile, scope, and submission authority must be confirmed by accountable people and the receiving entity., from business, risk, compliance, finance, and operational owners.
- **Validate and limit:** Inspect provenance and freshness, then trace a human-approved sample to its source record, accountable owner, and exception or follow-up path. This can support that the stated practice has observable evidence. It cannot prove continuous effectiveness, satisfy an assessor by itself, or support an unreviewed conformance claim.
- **AI and trigger:** AI may create a read-only evidence index, identify gaps, and draft questions; it may not alter systems, close findings, or create external representations. Recollect after product, customer, supplier, material event, regulatory update, or control change.

### 3. Decisions, exceptions, and renewal evidence

- **Request and owner:** Approved risk or exception decisions, corrective-action and retest records, source-change watch, and annual review or renewal record from business, risk, compliance, finance, and operational owners.
- **Validate and limit:** Trace a selected exception or remediation item to a named human decision, due date, expiry, evidence source, and retest result. This can support accountable follow-through. It cannot accept residual risk, make a legal decision, or replace an independent assessment.
- **AI and trigger:** AI may flag stale approvals and assemble a review packet. Humans approve risk treatment, submissions, attestations, and closure. Revisit on product, customer, supplier, material event, regulatory update, or control change.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
