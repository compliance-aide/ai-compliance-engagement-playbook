# FIPS 205 post-quantum hash-based signature engagement guide

> Original operational guidance, not FIPS content, SLH-DSA implementation instructions, a cryptographic approval, a validation claim, or a compliance claim. Confirm current requirements through [FIPS 205](https://csrc.nist.gov/pubs/fips/205/final) and the organization’s approved security, cryptography, architecture, legal, and operational decisions.

## Engagement focus

Operate a governed discovery-and-migration process for in-scope digital-signature uses that may adopt FIPS 205. Connect signing purpose, signer or service identity, application and protocol dependencies, module or provider versions, test outcomes, rollout approvals, exception decisions, rollback readiness, and lifecycle evidence to accountable owners. A vendor statement, successful test, or enabled feature is evidence to assess; it does not prove suitability, interoperability, secure implementation, signer authority, legal effect, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, identity, application and service owners, legal, privacy where relevant, procurement, supplier-management, change-management, incident-response, business-continuity, and records-management roles. Operators maintain a scoped signature-use inventory, approved migration roadmap, signer and service ownership records, protocol and dependency evidence, module or provider status, test and rollout artifacts, change approvals, exception decisions, rollback evidence, and supplier assurance. Reconcile uses, owners, and dependencies quarterly; review cryptographic and provider changes, test outcomes, expiring dependencies, exceptions, supplier notices, and unresolved risks at least quarterly; and complete an annual management review after material application, protocol, provider, cryptographic, legal, or threat changes. Before annual renewal, an independent reviewer samples use-to-rollout traceability and exception handling; auditors test the evidence trail without selecting algorithms, signing on behalf of a user, accessing private keys, configuring production systems, accepting risk, or attesting for management.

AI may organize supplied inventory, test, supplier, rollout, and review evidence, identify missing ownership or stale decisions, and draft workpapers for human review. AI cannot design or implement cryptography, select parameters, sign or access private keys, determine signer authority, configure production systems, approve a migration or exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.


<!-- evidence-plan: generated-draft -->
## Tailored evidence plan

**Plan status:** Draft generated from this guide's existing engagement focus; it requires independent source and skeptical review before a final catalog claim.

**Source and rights snapshot.** Use the guide's cited publisher source (https://csrc.nist.gov/pubs/fips/205/final) and check its current edition or status before use. This plan uses original operational language and does not reproduce protected requirements, assessment questions, mappings, or branded templates. A named human engagement owner confirms applicability and source rights.

**Guide-specific planning input.** Operate a governed discovery-and-migration process for in-scope digital-signature uses that may adopt FIPS 205. Connect signing purpose, signer or service identity, application and protocol dependencies, module or provider versions, test outcomes, rollout approvals, exception decisions, rollback readiness, and lifecycle evidence to accountable owners. A vendor statement, successful test, or enabled feature is evidence to assess; it does not prove suitability, interoperability, secure implementation, signer authority, legal effect, or compliance.

### 1. Applicability and boundary evidence

- **Request and owner:** A dated record of the applicable product or operational boundary, asset/process population, safety constraint, supplier, and change window, exclusions, inherited responsibilities, and accountable human owners, maintained by engineering, safety, operations, and supplier owners.
- **Validate and limit:** Trace a human-approved selection from the declared boundary to source systems or operating records; preserve population, period, access restriction, and unresolved-boundary notes. This can support a bounded engagement scope. It cannot decide legal applicability, publisher acceptance, certification, or completeness beyond the documented population.
- **AI and trigger:** AI may organize approved metadata and flag inconsistent boundaries. Humans approve scope and exclusions. Refresh after product, asset, supplier, safety condition, maintenance window, or incident change.

### 2. Operating evidence for FIPS 205 post-quantum hash-based signature

- **Request and owner:** Time-bounded design/operating records, asset/configuration, maintenance, test/exercise, supplier, and corrective-action records, selected because this guide focuses on operate a governed discovery-and-migration process for in-scope digital-signature uses that may adopt fips 205. connect signing purpose, signer or service identity, application and protocol dependencies, module or provider versions, test outcomes, rollout approvals, exception decisions, rollback readiness, and lifecycle evidence to accountable owners. a vendor statement, successful test, or enabled feature is evidence to assess; it does not prove suitability, interoperability, secure implementation, signer authority, legal effect, or compliance., from engineering, safety, operations, and supplier owners.
- **Validate and limit:** Inspect provenance and freshness, then trace a human-approved sample to its source record, accountable owner, and exception or follow-up path. This can support that the stated practice has observable evidence. It cannot prove continuous effectiveness, satisfy an assessor by itself, or support an unreviewed conformance claim.
- **AI and trigger:** AI may create a read-only evidence index, identify gaps, and draft questions; it may not alter systems, close findings, or create external representations. Recollect after product, asset, supplier, safety condition, maintenance window, or incident change.

### 3. Decisions, exceptions, and renewal evidence

- **Request and owner:** Approved risk or exception decisions, corrective-action and retest records, source-change watch, and annual review or renewal record from engineering, safety, operations, and supplier owners.
- **Validate and limit:** Trace a selected exception or remediation item to a named human decision, due date, expiry, evidence source, and retest result. This can support accountable follow-through. It cannot accept residual risk, make a legal decision, or replace an independent assessment.
- **AI and trigger:** AI may flag stale approvals and assemble a review packet. Humans approve risk treatment, submissions, attestations, and closure. Revisit on product, asset, supplier, safety condition, maintenance window, or incident change.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
