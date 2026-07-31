# NIST SP 800-90B entropy-source engagement guide

> Original operational guidance, not NIST entropy-source content, random-number-generator implementation instructions, a validation claim, or a compliance claim. Confirm current requirements and errata through [NIST SP 800-90B](https://csrc.nist.gov/pubs/sp/800/90/b/final) and the organization’s approved security, cryptography, engineering, procurement, and operational decisions.

## Engagement focus

Operate a governed inventory and assurance cycle for in-scope entropy sources used by cryptographic random-bit generation. Maintain traceability from product or system use through source and module identity, version, approved design and deployment baseline, health and validation evidence, operational monitoring, changes, incidents, supplier dependencies, and lifecycle review. A vendor assertion, test result, or health signal is evidence to assess; it does not prove sufficient entropy in a deployed context, correct implementation, validation status, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, product or system owners, procurement, supplier-management, change-management, incident-response, and records-management roles. Operators maintain an in-scope source and module inventory, approved versions and configurations, test and validation-status evidence, operational health and anomaly records, change approvals, supplier assurance, exception decisions, incident records, and system-to-source traceability. Reconcile sources, owners, modules, and deployed versions quarterly; review health anomalies, validation status, supplier notices, configuration changes, exceptions, and unresolved risks at least quarterly; and complete an annual management review after material system, module, provider, cryptographic, or threat changes. Before annual renewal, an independent reviewer samples inventory-to-deployment-to-test traceability; auditors test the evidence trail without generating random values, accessing cryptographic material, changing entropy-source configuration, approving exceptions, accepting risk, or attesting for management.

AI may organize supplied inventory, test, supplier, health, and review evidence, identify missing ownership or stale validation-status records, and draft workpapers for human review. AI cannot design or implement an entropy source, generate or access cryptographic material, change production configuration, determine validation, approve an exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.


<!-- evidence-plan: generated-draft -->
## Tailored evidence plan

**Plan status:** Draft generated from this guide's existing engagement focus; it requires independent source and skeptical review before a final catalog claim.

**Source and rights snapshot.** Use the guide's cited publisher source (https://csrc.nist.gov/pubs/sp/800/90/b/final) and check its current edition or status before use. This plan uses original operational language and does not reproduce protected requirements, assessment questions, mappings, or branded templates. A named human engagement owner confirms applicability and source rights.

**Guide-specific planning input.** Operate a governed inventory and assurance cycle for in-scope entropy sources used by cryptographic random-bit generation. Maintain traceability from product or system use through source and module identity, version, approved design and deployment baseline, health and validation evidence, operational monitoring, changes, incidents, supplier dependencies, and lifecycle review. A vendor assertion, test result, or health signal is evidence to assess; it does not prove sufficient entropy in a deployed context, correct implementation, validation status, or compliance.

### 1. Applicability and boundary evidence

- **Request and owner:** A dated record of the applicable product or operational boundary, asset/process population, safety constraint, supplier, and change window, exclusions, inherited responsibilities, and accountable human owners, maintained by engineering, safety, operations, and supplier owners.
- **Validate and limit:** Trace a human-approved selection from the declared boundary to source systems or operating records; preserve population, period, access restriction, and unresolved-boundary notes. This can support a bounded engagement scope. It cannot decide legal applicability, publisher acceptance, certification, or completeness beyond the documented population.
- **AI and trigger:** AI may organize approved metadata and flag inconsistent boundaries. Humans approve scope and exclusions. Refresh after product, asset, supplier, safety condition, maintenance window, or incident change.

### 2. Operating evidence for NIST SP 800-90B entropy-source

- **Request and owner:** Time-bounded design/operating records, asset/configuration, maintenance, test/exercise, supplier, and corrective-action records, selected because this guide focuses on operate a governed inventory and assurance cycle for in-scope entropy sources used by cryptographic random-bit generation. maintain traceability from product or system use through source and module identity, version, approved design and deployment baseline, health and validation evidence, operational monitoring, changes, incidents, supplier dependencies, and lifecycle review. a vendor assertion, test result, or health signal is evidence to assess; it does not prove sufficient entropy in a deployed context, correct implementation, validation status, or compliance., from engineering, safety, operations, and supplier owners.
- **Validate and limit:** Inspect provenance and freshness, then trace a human-approved sample to its source record, accountable owner, and exception or follow-up path. This can support that the stated practice has observable evidence. It cannot prove continuous effectiveness, satisfy an assessor by itself, or support an unreviewed conformance claim.
- **AI and trigger:** AI may create a read-only evidence index, identify gaps, and draft questions; it may not alter systems, close findings, or create external representations. Recollect after product, asset, supplier, safety condition, maintenance window, or incident change.

### 3. Decisions, exceptions, and renewal evidence

- **Request and owner:** Approved risk or exception decisions, corrective-action and retest records, source-change watch, and annual review or renewal record from engineering, safety, operations, and supplier owners.
- **Validate and limit:** Trace a selected exception or remediation item to a named human decision, due date, expiry, evidence source, and retest result. This can support accountable follow-through. It cannot accept residual risk, make a legal decision, or replace an independent assessment.
- **AI and trigger:** AI may flag stale approvals and assemble a review packet. Humans approve risk treatment, submissions, attestations, and closure. Revisit on product, asset, supplier, safety condition, maintenance window, or incident change.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
