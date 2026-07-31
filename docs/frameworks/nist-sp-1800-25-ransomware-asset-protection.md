# NIST SP 1800-25 ransomware asset-protection engagement guide

> Original operational guidance, not NIST practice-guide text, a technical design approval, a recovery command, or a compliance claim. Confirm current material through [NIST SP 1800-25](https://csrc.nist.gov/pubs/sp/1800/25/final) and the organization’s approved risk, architecture, and incident-response decisions.

## Engagement focus

Maintain an evidence-backed view of data, devices, applications, configurations, and dependencies whose corruption or destruction would materially affect a business service. Connect each material asset group to accountable owners, data-integrity risks, protective measures, backups, logging, vulnerability and maintenance activity, monitoring coverage, exception decisions, and recovery dependencies. Use the practice guide to structure a defensible protection program; do not treat an inventory, a tool deployment, or an AI-generated assessment as proof that risk is accepted or that an environment is protected.

## Roles and annual rhythm

Assign accountable executive, asset-owner, security, technology, data, platform, application, vulnerability-management, business-continuity, supplier-management, and risk owners. Operators maintain authoritative inventories, ownership and classification records, protection configuration evidence, integrity-check and backup records, logging coverage, vulnerability and maintenance records, supplier attestations, exceptions, and remediation status. Reconcile critical assets and their protection assumptions quarterly; reassess after material service, architecture, supplier, data-classification, or threat changes. Before annual renewal, an independent reviewer samples inventory-to-service links and protection evidence; auditors test the evidence trail without designing safeguards, accepting exceptions, accepting risk, approving architecture, or attesting for management.

AI may reconcile supplied inventory and evidence records, flag missing ownership or stale protection artifacts, trace asset groups to service dependencies, and draft workpapers for human review. AI cannot approve architecture, classify data, accept risk or an exception, alter safeguards, make a compliance conclusion, attest for management, or replace independent review.


<!-- evidence-plan: generated-draft -->
## Tailored evidence plan

**Plan status:** Draft generated from this guide's existing engagement focus; it requires independent source and skeptical review before a final catalog claim.

**Source and rights snapshot.** Use the guide's cited publisher source (https://csrc.nist.gov/pubs/sp/1800/25/final) and check its current edition or status before use. This plan uses original operational language and does not reproduce protected requirements, assessment questions, mappings, or branded templates. A named human engagement owner confirms applicability and source rights.

**Guide-specific planning input.** Maintain an evidence-backed view of data, devices, applications, configurations, and dependencies whose corruption or destruction would materially affect a business service. Connect each material asset group to accountable owners, data-integrity risks, protective measures, backups, logging, vulnerability and maintenance activity, monitoring coverage, exception decisions, and recovery dependencies. Use the practice guide to structure a defensible protection program; do not treat an inventory, a tool deployment, or an AI-generated assessment as proof that risk is accepted or that an environment is protected.

### 1. Applicability and boundary evidence

- **Request and owner:** A dated record of the applicable use case, intended purpose, deployment context, affected people, and model/data dependency, exclusions, inherited responsibilities, and accountable human owners, maintained by AI governance, product, model, and risk owners.
- **Validate and limit:** Trace a human-approved selection from the declared boundary to source systems or operating records; preserve population, period, access restriction, and unresolved-boundary notes. This can support a bounded engagement scope. It cannot decide legal applicability, publisher acceptance, certification, or completeness beyond the documented population.
- **AI and trigger:** AI may organize approved metadata and flag inconsistent boundaries. Humans approve scope and exclusions. Refresh after model, data, provider, use-case, geography, release, or incident change.

### 2. Operating evidence for NIST SP 1800-25 ransomware asset-protection

- **Request and owner:** Time-bounded inventory, evaluation, monitoring, oversight, release, feedback, and incident records, selected because this guide focuses on maintain an evidence-backed view of data, devices, applications, configurations, and dependencies whose corruption or destruction would materially affect a business service. connect each material asset group to accountable owners, data-integrity risks, protective measures, backups, logging, vulnerability and maintenance activity, monitoring coverage, exception decisions, and recovery dependencies. use the practice guide to structure a defensible protection program; do not treat an inventory, a tool deployment, or an ai-generated assessment as proof that risk is accepted or that an environment is protected., from AI governance, product, model, and risk owners.
- **Validate and limit:** Inspect provenance and freshness, then trace a human-approved sample to its source record, accountable owner, and exception or follow-up path. This can support that the stated practice has observable evidence. It cannot prove continuous effectiveness, satisfy an assessor by itself, or support an unreviewed conformance claim.
- **AI and trigger:** AI may create a read-only evidence index, identify gaps, and draft questions; it may not alter systems, close findings, or create external representations. Recollect after model, data, provider, use-case, geography, release, or incident change.

### 3. Decisions, exceptions, and renewal evidence

- **Request and owner:** Approved risk or exception decisions, corrective-action and retest records, source-change watch, and annual review or renewal record from AI governance, product, model, and risk owners.
- **Validate and limit:** Trace a selected exception or remediation item to a named human decision, due date, expiry, evidence source, and retest result. This can support accountable follow-through. It cannot accept residual risk, make a legal decision, or replace an independent assessment.
- **AI and trigger:** AI may flag stale approvals and assemble a review packet. Humans approve risk treatment, submissions, attestations, and closure. Revisit on model, data, provider, use-case, geography, release, or incident change.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
