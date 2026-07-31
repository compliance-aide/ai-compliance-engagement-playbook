# PCI DSS v4.0.1 SAQ C engagement guide

> Original operational guidance, not PCI SSC content, payment-brand direction, an eligibility decision, an attestation, or a compliance claim. Confirm the current [PCI DSS v4.0.1 SAQ resources](https://www.pcisecuritystandards.org/document_library/) and validation instructions with the entity that receives the submission.

## Engagement focus

Treat SAQ C as a conditional validation profile with its own eligibility conditions. Document payment channels, systems and locations, transaction paths, connections, account-data handling, provider boundaries, access and change processes, security operations, and material changes. Keep profile eligibility analysis separate from the underlying PCI DSS evidence and from the required submission process. When a new system, channel, connection, data path, provider, or operational fact changes the documented boundary, stop and obtain a human decision on scope and profile eligibility.

## Roles and annual rhythm

Name accountable owners for payment operations, information technology, security, vendor management, facilities, finance, and incident response. Operators retain inventories, diagrams, configurations, access evidence, change approvals, provider records, security testing results, exceptions, and incident artifacts. Review the scope record and evidence register quarterly, and after any material payment-environment change. Before annual validation, management obtains confirmation from the submission recipient; an independent reviewer samples systems, payment paths, and evidence to assess whether the documented profile boundary operated. Auditors test the evidence and review process without choosing the profile or attesting for management.

AI may organize supplied evidence, reconcile asset and change records, identify missing ownership or contradictory facts, and draft workpapers for human review. AI cannot select an SAQ, decide eligibility or scope, authorize system changes, determine compliance, attest for management, or replace independent review.


<!-- evidence-plan: generated-draft -->
## Tailored evidence plan

**Plan status:** Draft generated from this guide's existing engagement focus; it requires independent source and skeptical review before a final catalog claim.

**Source and rights snapshot.** Use the guide's cited publisher source (https://www.pcisecuritystandards.org/document_library/) and check its current edition or status before use. This plan uses original operational language and does not reproduce protected requirements, assessment questions, mappings, or branded templates. A named human engagement owner confirms applicability and source rights.

**Guide-specific planning input.** Treat SAQ C as a conditional validation profile with its own eligibility conditions. Document payment channels, systems and locations, transaction paths, connections, account-data handling, provider boundaries, access and change processes, security operations, and material changes. Keep profile eligibility analysis separate from the underlying PCI DSS evidence and from the required submission process. When a new system, channel, connection, data path, provider, or operational fact changes the documented boundary, stop and obtain a human decision on scope and profile eligibility.

### 1. Applicability and boundary evidence

- **Request and owner:** A dated record of the applicable business activity, product, customer, system, third-party, and decision boundary, exclusions, inherited responsibilities, and accountable human owners, maintained by business, risk, compliance, finance, and operational owners.
- **Validate and limit:** Trace a human-approved selection from the declared boundary to source systems or operating records; preserve population, period, access restriction, and unresolved-boundary notes. This can support a bounded engagement scope. It cannot decide legal applicability, publisher acceptance, certification, or completeness beyond the documented population.
- **AI and trigger:** AI may organize approved metadata and flag inconsistent boundaries. Humans approve scope and exclusions. Refresh after product, customer, supplier, material event, regulatory update, or control change.

### 2. Operating evidence for PCI DSS v4.0.1 SAQ C

- **Request and owner:** Time-bounded governance, transaction/process, access/change, exception, supervisory-review, and remediation records, selected because this guide focuses on treat saq c as a conditional validation profile with its own eligibility conditions. document payment channels, systems and locations, transaction paths, connections, account-data handling, provider boundaries, access and change processes, security operations, and material changes. keep profile eligibility analysis separate from the underlying pci dss evidence and from the required submission process. when a new system, channel, connection, data path, provider, or operational fact changes the documented boundary, stop and obtain a human decision on scope and profile eligibility., from business, risk, compliance, finance, and operational owners.
- **Validate and limit:** Inspect provenance and freshness, then trace a human-approved sample to its source record, accountable owner, and exception or follow-up path. This can support that the stated practice has observable evidence. It cannot prove continuous effectiveness, satisfy an assessor by itself, or support an unreviewed conformance claim.
- **AI and trigger:** AI may create a read-only evidence index, identify gaps, and draft questions; it may not alter systems, close findings, or create external representations. Recollect after product, customer, supplier, material event, regulatory update, or control change.

### 3. Decisions, exceptions, and renewal evidence

- **Request and owner:** Approved risk or exception decisions, corrective-action and retest records, source-change watch, and annual review or renewal record from business, risk, compliance, finance, and operational owners.
- **Validate and limit:** Trace a selected exception or remediation item to a named human decision, due date, expiry, evidence source, and retest result. This can support accountable follow-through. It cannot accept residual risk, make a legal decision, or replace an independent assessment.
- **AI and trigger:** AI may flag stale approvals and assemble a review packet. Humans approve risk treatment, submissions, attestations, and closure. Revisit on product, customer, supplier, material event, regulatory update, or control change.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
