# eIDAS trust services — engagement guide

> Original operational guidance, not a qualified-status conclusion. Consult the [European Commission eIDAS overview](https://digital-strategy.ec.europa.eu/en/policies/discover-eidas).

## Engagement focus

Maintain jurisdiction, role, legal effect, service, provider, certificate, signature, seal, timestamp, trusted-list, revocation, incident, and reliance evidence.

## Roles

Counsel and competent authorities determine qualified status; independent reviewers test lifecycle evidence. AI cannot make legal or qualified-status claims. Review quarterly and annually.

## Source and applicability

Use the amended eIDAS legal framework, relevant implementing acts, national supervision and the [Commission's updated trust-service questions and answers](https://digital-strategy.ec.europa.eu/en/faqs/questions-answers-trust-services-under-european-digital-identity-regulation). Record the actual service type and role: providing, consuming or validating a trust service entail different work. Identity-wallet requirements are not automatically the requirements for every signature or timestamp service.

The [Commission trusted-list explanation](https://digital-strategy.ec.europa.eu/en/policies/eu-trusted-lists) ties qualified status to the particular listed service. Do not promote all of a provider's offerings to qualified because one appears in a list. Record the relevant historical status for an event, not merely today's provider name. A technical validation result, qualified-service status and legal effect are separate questions for the appropriate specialists.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Name trust-service operations, cryptography/validation, legal, security and records owners. Use synthetic signed test documents and authorized validation records; do not request private keys or create legally binding signatures. Define event time, evaluation time, service/certificate identifiers, validation policy and evidence-retention needs before inspection.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Resolve legal and service scope | Counsel and service owners identify applicable roles, service types and current requirements. | Source register and approved scope, including transitions and unresolved legal questions. |
| 2. Establish provider/service identity | Owners reconcile contracts, endpoints, certificates and official service records. | Exact service match; vendor branding or a general certificate logo is insufficient. |
| 3. Preserve status evidence | Authorized specialists retrieve relevant trusted-list and status-history records. | Dated source, service identifier and applicable status interval, with unavailable historical evidence explicit. |
| 4. Define validation method | Specialists approve policy, tooling, trust sources, time assumptions and test cases. | Repeatable method specifying what a result can and cannot establish; AI does not choose legal validity criteria. |
| 5. Review lifecycle operation | Reviewers inspect permitted issuance, signing/sealing, timestamping, revocation and validation evidence. | Event-specific workpapers with artifact identity, times, dependencies and contradictory results retained. |
| 6. Test failure handling | Authorized QA testers exercise invalid, unavailable and indeterminate evidence scenarios. | Observed handling of rejected or unknown results; transport success does not become successful validation. |
| 7. Remediate and retest | Owners correct approved operational gaps and specialists evaluate affected historical events. | Retest evidence and separate historical-reliance decisions; replacing a certificate does not repair all prior events. |
| 8. Approve reliance and sustain | Accountable specialists review service claims and preservation needs. | Scoped approved statement, source-change watch and named handoff; no automatic legal or qualified-status conclusion. |

## Failure branches and decisions

- **Provider listed, selected service absent:** preserve the mismatch and request the correct service record; do not infer status across service types.
- **Current status differs from event-time status:** retain both intervals and route interpretation to validation/legal specialists.
- **Revocation endpoint unavailable:** record unavailable evidence and the approved policy's treatment; do not turn network failure into a good certificate status.
- **Document bytes differ from the validated artifact:** preserve hashes and stop reusing the result for the altered document.
- **Tool returns indeterminate:** retain the exact reason, missing evidence and owner; do not relabel it valid to finish the workflow.
- **Private key requested as evidence:** use authorized custody/control evidence instead; assessment does not require exposing the key.

## Worked handoff example

A fictional QA validation record reports a successful HTTP request but an indeterminate signature result because status evidence is unavailable. The work item is `inconclusive` for the assertion that the supplied evidence establishes the expected validation result. Preserve the original response and artifact identifier; the validation owner must retrieve the missing evidence or approve the method's defined handling. This is not a failed signature conclusion or permission to sign a replacement.

## Evidence and test plan

**Source and rights snapshot.** Use the [European Commission eIDAS overview](https://digital-strategy.ec.europa.eu/en/policies/discover-eidas), applicable official EU legal material, the relevant trusted-list source, and approved counsel; prior snapshot 2026-07-31; verify amended legal framework and service status. This is original evidence-planning language, not legal advice, a qualified-status determination, a trusted-list assertion, or a trust-service certification. Counsel and competent authorities determine legal effect and qualified status.

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


## Cadence and renewal

Quarterly and annual reviews are planning conventions. Monitor actual service-status, certificate, policy, trust-source and legal changes against approved reliance needs. Keep event-time evidence and preservation decisions even after certificate expiry or provider changes. Apply specific audit, incident and retention duties only after source verification.

## Completion and handoff

Deliver role/source decisions, exact service identities, status evidence, approved validation policy, event workpapers, failures and remediation decisions. Separate technical observations from qualified status and legal effect. Name the next owner, action and evidence needed without earlier chat. A retrieved registry page or successful tool invocation is not a complete trust determination.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
