# UK Software Security Code of Practice engagement guide

> Original operational guidance, not UK government text, a security determination, a legal interpretation, or a compliance claim. Confirm current material through the [UK Software Security Code of Practice](https://www.gov.uk/government/publications/software-security-code-of-practice) and applicable authority.

## Engagement focus

Run the engagement around the software the organisation supplies to business customers, its release and maintenance practices, third-party component exposure, customer-facing security commitments, and the records that demonstrate those practices operate. Keep a current product inventory and identify which teams own design, development, release approval, vulnerability response, customer communications, and supplier assurance. Treat the Code as voluntary guidance: record the organisation's intended scope and any contract, regulator, or customer requirement separately.

## Roles and annual rhythm

Assign a senior accountable leader to set the scope, fund corrective work, and attest internally to the engagement's status. Product, engineering, security, release, procurement, support, and legal teams maintain their respective operational records throughout the year. At least quarterly, reconcile the product inventory to component, test, release, vulnerability, and customer-notice evidence; investigate exceptions before the next release cycle. Before the annual renewal, perform an independent review of a risk-based sample of products and releases, confirm that remediation and customer communication decisions are traceable, and give management a bounded findings report. Auditors examine the evidence trail and test the engagement design without taking over management decisions.

AI may organize supplied evidence, trace release records to declared ownership, flag missing or contradictory records, and draft workpapers for human review. AI cannot decide whether software is secure, make a legal or certification conclusion, approve a release, attest on behalf of management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** Record retrieval date and applicable use terms for the official [UK Software Security Code of Practice](https://www.gov.uk/government/publications/software-security-code-of-practice). This plan is original guidance and treats the Code as voluntary unless a named human records a separate contractual, regulatory, or customer obligation. Product, security, legal, and authorized release owners decide scope and external representations.

### 1. Product, ownership, and secure-development-governance package

- **Request and owner:** Product, engineering, security, legal, procurement, and records owners provide in-scope product/version inventory, accountable-role map, secure-development policies, design-review records, dependency/supplier inventory, and stated customer or contractual requirements.
- **Validate and limit:** Trace a selected product/version to its accountable owners, development and dependency records, and recorded scope decision. This supports accountable traceability; it cannot determine security, contractual applicability, or inventory completeness.
- **AI and trigger:** AI may reconcile supplied product, owner, and dependency metadata. Humans decide scope, architecture, supplier acceptance, and policy exceptions. Refresh before material product, supplier, architecture, or market change.

### 2. Build, release, and vulnerability-response package

- **Request and owner:** Engineering, security, release, support, and supplier owners provide build provenance references, test and review outputs, release approvals, vulnerability intake/triage records, remediation decisions, version links, and support/customer-contact evidence.
- **Validate and limit:** Follow a selected release or vulnerability from accountable intake through review, authorized release/remediation decision, version record, and customer communication decision. This supports a sampled lifecycle trail; it cannot approve a release, prove absence of vulnerabilities, or guarantee remediation efficacy.
- **AI and trigger:** AI may organize supplied evidence and flag missing version, owner, or due-date links. Humans authorize releases, severity, remediation, disclosure, and customer communications. Recollect after release, vulnerability, incident, or material supplier issue.

### 3. Assurance, exception, and customer-commitment package

- **Request and owner:** Product, security, legal, commercial, assurance, and executive owners provide approved security-commitment language, exception register, risk decisions, independent review workpapers, corrective-action records, and management-review evidence.
- **Validate and limit:** Trace a selected commitment or exception to its product/version context, supporting evidence, authorized approval, expiry/follow-up, and independent challenge note. This supports controlled representation; it cannot make a legal conclusion, accept risk, or certify software.
- **AI and trigger:** AI may prepare an access-controlled evidence index and flag unsupported commitments. Humans approve claims, exceptions, risk treatment, and closure. Review quarterly, before material commitments, and annually across active products.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
