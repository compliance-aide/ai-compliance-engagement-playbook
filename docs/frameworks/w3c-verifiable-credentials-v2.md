# W3C Verifiable Credentials Data Model v2 — engagement guide

> Original operational guidance, not W3C normative text or a claim-truth assertion. See the [W3C Recommendation](https://www.w3.org/TR/vc-data-model-2.0/).

## Engagement focus

Maintain issuer, holder, verifier, purpose, schema, status, key, registry, flow, issuance, presentation, expiry, revocation, privacy, and accessibility evidence.

## Roles and annual rhythm

Humans decide policy and claim handling; independent reviewers test lifecycle. AI correlates records, but cannot assert claim truth or make legal identity decisions. Review quarterly and annually.

## Tailored evidence plan

**Source and rights snapshot.** Use the [W3C Verifiable Credentials Data Model v2 Recommendation](https://www.w3.org/TR/vc-data-model-2.0/) and approved organizational identity, privacy, security, and legal decisions; checked 2026-07-31. This is original evidence-planning language, not normative W3C text, a credential-profile implementation, a claim-truth assertion, or a legal identity decision. Accountable humans set trust and claim-handling policy.

### 1. Issuer, schema, and credential-lifecycle package

- **Request and owner:** Credential product, issuer, identity, security, privacy, and records owners provide issuer authorization records, credential purpose and claim-schema references, format/profile and version decisions, issuance/expiry/suspension or revocation lifecycle policies, key/registry dependency references, retention rules, and named owners.
- **Validate and limit:** Trace a selected credential type from approved purpose and issuer authority to schema/version, lifecycle policy, status mechanism reference, key/registry dependency, and owner. This checks documentary traceability; it cannot establish issuer legitimacy, claim truth, credential validity, cryptographic correctness, or legal effect.
- **AI and trigger:** AI may organize supplied metadata and flag absent versions, owners, or lifecycle dates. Humans approve issuer authority, claim schemas, trust policy, retention, and material changes. Refresh after a schema, credential type, issuer, key/registry, or policy change.

### 2. Holder presentation, verifier, and consent-boundary package

- **Request and owner:** Product, identity, privacy, accessibility, and relying-party owners provide approved holder experience designs, presentation-purpose records, verifier/application inventory, requested-attribute/minimization decisions, consent or notice references where applicable, accessibility reviews, session/logging boundaries, and exception decisions.
- **Validate and limit:** Sample one presentation journey or exercise from verifier purpose through requested attributes, holder notice/consent reference where applicable, technical-flow record, result handling, and accountable owner. This cannot prove holder control, valid consent, accessibility, disclosure legality, or that a verifier decision is correct.
- **AI and trigger:** AI may map approved data-flow metadata and flag an unlinked verifier or excessive-request review question. Humans approve verifier purposes, requested attributes, user experience, and disclosures; AI cannot initiate presentations, select credentials, or make identity decisions. Refresh after a verifier, attribute, UX, privacy, or accessibility change.

### 3. Status, compromise, and trust-governance package

- **Request and owner:** Security, operations, issuer, verifier, legal, and supplier owners provide status-list or registry operational references, key-compromise and incident playbooks, monitoring records, trust-list/policy records, dependency notices, corrective actions, exception decisions, and review cadence evidence.
- **Validate and limit:** Trace a selected status event, compromised-key exercise, or trust-policy change to the originating record, authorized owner, affected credential/verifier boundary, escalation, corrective action, and closure. This cannot determine revocation effectiveness, cryptographic security, legal notification duty, or trustworthiness of a participant.
- **AI and trigger:** AI may correlate sanitized event and dependency records and flag overdue actions. Humans decide suspension/revocation, trust-policy changes, notifications, exceptions, and risk acceptance. Review quarterly and after a security event, key/registry change, issuer/verifier onboarding, or material source update.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
