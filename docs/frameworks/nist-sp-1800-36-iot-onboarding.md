# NIST SP 1800-36 IoT onboarding engagement guide

> This is original operational guidance, not NIST practice-guide content, an IoT architecture, a trust determination, a compliance claim, or professional advice. Confirm current material through [NIST SP 1800-36](https://csrc.nist.gov/pubs/sp/1800/36/final) and the organization's approved security, engineering, privacy, legal, procurement, safety, and operational decisions.

## Engagement focus

Manage a controlled lifecycle for network-layer onboarding and operation of internet-protocol IoT devices. Connect each in-scope device type, manufacturer, model, software or firmware version, intended use, owner, network segment, identity and posture evidence, onboarding path, credential lifecycle, permitted operations, supplier dependency, monitoring, change, and retirement record. Treat device or network attestation evidence as an input to accountable authorization—not an automatic grant of network access or assurance of safe behavior.

Maintain clear decisions for device admission, identity proofing, configuration baselines, credential issuance, network restrictions, update and vulnerability response, lost or compromised devices, exceptions, decommissioning, and evidence retention. The engagement should surface unapproved or unknown devices and stale lifecycle evidence without automatically disconnecting devices or changing production configurations.

## Roles and annual rhythm

Security, network, IoT or product engineering, identity, operations, data, privacy, procurement, supplier, safety, incident-response, records, and business owners establish scope and make accountable decisions. Operators maintain inventories, approved-device criteria, onboarding and credential records, configuration and posture evidence, monitoring, supplier materials, lifecycle actions, exceptions, incident cases, and review history. Reconcile device inventory, ownership, onboarding status, and high-risk dependencies quarterly; review material vulnerabilities, supplier notices, and network changes promptly; and conduct an annual lifecycle governance review.

Independent reviewers sample a device type from procurement or enrollment through onboarding evidence, access decision, lifecycle monitoring, and retirement or review, testing traceability. Auditors evaluate supplied evidence without authorizing devices, granting credentials, changing network configuration, selecting suppliers, determining safety, accepting risk, or issuing an attestation. AI may organize device records, flag missing ownership or stale evidence, compare approved inventories, draft workpapers, and prepare review questions. AI cannot decide trust, grant access or credentials, modify device or network settings, approve exceptions, determine safety, accept risk, or attest to conformance.


<!-- evidence-plan: generated-draft -->
## Tailored evidence plan

**Plan status:** Draft generated from this guide's existing engagement focus; it requires independent source and skeptical review before a final catalog claim.

**Source and rights snapshot.** Use the guide's cited publisher source (https://csrc.nist.gov/pubs/sp/1800/36/final) and check its current edition or status before use. This plan uses original operational language and does not reproduce protected requirements, assessment questions, mappings, or branded templates. A named human engagement owner confirms applicability and source rights.

**Guide-specific planning input.** Manage a controlled lifecycle for network-layer onboarding and operation of internet-protocol IoT devices. Connect each in-scope device type, manufacturer, model, software or firmware version, intended use, owner, network segment, identity and posture evidence, onboarding path, credential lifecycle, permitted operations, supplier dependency, monitoring, change, and retirement record. Treat device or network attestation evidence as an input to accountable authorization—not an automatic grant of network access or assurance of safe behavior. Maintain clear decisions for device admission, identity proofing, configuration baselines, credential issuance, network restrictions, update and vulnerability response, lost or compromised devices, exceptions, decommissioning, and evidence retention. The engagement should surface unapproved or unknown devices and stale lifecycle evidence without automatically disconnecting devices or changing production configurations.

### 1. Applicability and boundary evidence

- **Request and owner:** A dated record of the applicable use case, intended purpose, deployment context, affected people, and model/data dependency, exclusions, inherited responsibilities, and accountable human owners, maintained by AI governance, product, model, and risk owners.
- **Validate and limit:** Trace a human-approved selection from the declared boundary to source systems or operating records; preserve population, period, access restriction, and unresolved-boundary notes. This can support a bounded engagement scope. It cannot decide legal applicability, publisher acceptance, certification, or completeness beyond the documented population.
- **AI and trigger:** AI may organize approved metadata and flag inconsistent boundaries. Humans approve scope and exclusions. Refresh after model, data, provider, use-case, geography, release, or incident change.

### 2. Operating evidence for NIST SP 1800-36 IoT onboarding

- **Request and owner:** Time-bounded inventory, evaluation, monitoring, oversight, release, feedback, and incident records, selected because this guide focuses on manage a controlled lifecycle for network-layer onboarding and operation of internet-protocol iot devices. connect each in-scope device type, manufacturer, model, software or firmware version, intended use, owner, network segment, identity and posture evidence, onboarding path, credential lifecycle, permitted operations, supplier dependency, monitoring, change, and retirement record. treat device or network attestation evidence as an input to accountable authorization—not an automatic grant of network access or assurance of safe behavior. maintain clear decisions for device admission, identity proofing, configuration baselines, credential issuance, network restrictions, update and vulnerability response, lost or compromised devices, exceptions, decommissioning, and evidence retention. the engagement should surface unapproved or unknown devices and stale lifecycle evidence without automatically disconnecting devices or changing production configurations., from AI governance, product, model, and risk owners.
- **Validate and limit:** Inspect provenance and freshness, then trace a human-approved sample to its source record, accountable owner, and exception or follow-up path. This can support that the stated practice has observable evidence. It cannot prove continuous effectiveness, satisfy an assessor by itself, or support an unreviewed conformance claim.
- **AI and trigger:** AI may create a read-only evidence index, identify gaps, and draft questions; it may not alter systems, close findings, or create external representations. Recollect after model, data, provider, use-case, geography, release, or incident change.

### 3. Decisions, exceptions, and renewal evidence

- **Request and owner:** Approved risk or exception decisions, corrective-action and retest records, source-change watch, and annual review or renewal record from AI governance, product, model, and risk owners.
- **Validate and limit:** Trace a selected exception or remediation item to a named human decision, due date, expiry, evidence source, and retest result. This can support accountable follow-through. It cannot accept residual risk, make a legal decision, or replace an independent assessment.
- **AI and trigger:** AI may flag stale approvals and assemble a review packet. Humans approve risk treatment, submissions, attestations, and closure. Revisit on model, data, provider, use-case, geography, release, or incident change.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
