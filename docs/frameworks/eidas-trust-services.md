# eIDAS trust services — engagement guide

> Original operational guidance, not a qualified-status conclusion. Consult the [European Commission eIDAS overview](https://digital-strategy.ec.europa.eu/en/policies/discover-eidas).

## Engagement focus

Maintain jurisdiction, role, legal effect, service, provider, certificate, signature, seal, timestamp, trusted-list, revocation, incident, and reliance evidence.

## Roles and annual rhythm

Counsel and competent authorities determine qualified status; independent reviewers test lifecycle evidence. AI cannot make legal or qualified-status claims. Review quarterly and annually.

## Tailored evidence plan

**Source and rights snapshot.** Use the [European Commission eIDAS overview](https://digital-strategy.ec.europa.eu/en/policies/discover-eidas), applicable official EU legal material, the relevant trusted-list source, and approved counsel; checked 2026-07-31. This is original evidence-planning language, not legal advice, a qualified-status determination, a trusted-list assertion, or a trust-service certification. Counsel and competent authorities determine legal effect and qualified status.

### 1. Service scope, provider, and status-boundary package

- **Request and owner:** Trust-service, legal, compliance, and service owners provide the service inventory, jurisdiction and role records, declared service type, provider identity, applicable trusted-list reference, certificate/service version references, intended relying parties, and accountable owners.
- **Validate and limit:** Trace one declared service from its approved scope record to the named provider, service/certificate reference, trusted-list lookup record where applicable, relying context, owner, and review date. This checks evidence linkage only; it cannot establish legal effect, qualified status, provider authorization, or inclusion in a trusted list.
- **AI and trigger:** AI may organize supplied public references and flag missing scope, owner, or review-date links. Humans and competent authorities decide status, legal effect, service eligibility, and any external representation. Refresh after provider, certificate, service, jurisdiction, or trusted-list changes.

### 2. Signing, seal, timestamp, and validation-lifecycle package

- **Request and owner:** Operations, security, cryptography, and service owners provide approved lifecycle records for issuance or activation where in scope, key/certificate custody references, signature/seal/timestamp service logs or redacted records, validation/revocation interface references, time-source dependencies, incidents, and change approvals.
- **Validate and limit:** Sample one completed lifecycle event or controlled exercise through its owner, service version, relevant event record, validation or revocation reference, exception path, and closure evidence. This cannot validate a signature or seal, inspect private keys, prove time accuracy, determine certificate validity, or authenticate a signer.
- **AI and trigger:** AI may index redacted event records and identify stale lifecycle links or unresolved actions; it cannot operate signing services, access key material, validate a legal signature, or alter status data. Humans approve operational changes, exception handling, incident response, and remediation. Refresh after a material service, certificate, validation, or incident change.

### 3. Reliance, incident, and record-retention package

- **Request and owner:** Legal, compliance, customer/relying-party, security, records, and supplier owners provide reliance-context records, customer communication and disclosure references, incident/escalation playbooks, audit-log retention/access records, third-party dependency notices, corrective actions, and approved exception decisions.
- **Validate and limit:** Trace a selected reliance inquiry, incident, or exercise to its source record, accountable owner, escalation decision, communication path, corrective action, and retention reference. This cannot determine liability, reporting duty, legal reliance, sufficiency of notice, or regulator-facing conclusions.
- **AI and trigger:** AI may correlate approved, minimized records and flag overdue actions or absent owners. Humans decide notification, legal advice, risk acceptance, external statements, and retention changes. Review quarterly and after a material incident, reliance dispute, provider notice, or legal/source update.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
