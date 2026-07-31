# NIST SP 1800-36 IoT onboarding engagement guide

> This is original operational guidance, not NIST practice-guide content, an IoT architecture, a trust determination, a compliance claim, or professional advice. Confirm current material through [NIST SP 1800-36](https://csrc.nist.gov/pubs/sp/1800/36/final) and the organization's approved security, engineering, privacy, legal, procurement, safety, and operational decisions.

## Engagement focus

Manage a controlled lifecycle for network-layer onboarding and operation of internet-protocol IoT devices. Connect each in-scope device type, manufacturer, model, software or firmware version, intended use, owner, network segment, identity and posture evidence, onboarding path, credential lifecycle, permitted operations, supplier dependency, monitoring, change, and retirement record. Treat device or network attestation evidence as an input to accountable authorization—not an automatic grant of network access or assurance of safe behavior.

Maintain clear decisions for device admission, identity proofing, configuration baselines, credential issuance, network restrictions, update and vulnerability response, lost or compromised devices, exceptions, decommissioning, and evidence retention. The engagement should surface unapproved or unknown devices and stale lifecycle evidence without automatically disconnecting devices or changing production configurations.

## Roles and annual rhythm

Security, network, IoT or product engineering, identity, operations, data, privacy, procurement, supplier, safety, incident-response, records, and business owners establish scope and make accountable decisions. Operators maintain inventories, approved-device criteria, onboarding and credential records, configuration and posture evidence, monitoring, supplier materials, lifecycle actions, exceptions, incident cases, and review history. Reconcile device inventory, ownership, onboarding status, and high-risk dependencies quarterly; review material vulnerabilities, supplier notices, and network changes promptly; and conduct an annual lifecycle governance review.

Independent reviewers sample a device type from procurement or enrollment through onboarding evidence, access decision, lifecycle monitoring, and retirement or review, testing traceability. Auditors evaluate supplied evidence without authorizing devices, granting credentials, changing network configuration, selecting suppliers, determining safety, accepting risk, or issuing an attestation. AI may organize device records, flag missing ownership or stale evidence, compare approved inventories, draft workpapers, and prepare review questions. AI cannot decide trust, grant access or credentials, modify device or network settings, approve exceptions, determine safety, accept risk, or attest to conformance.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
