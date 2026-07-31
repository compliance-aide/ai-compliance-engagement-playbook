# NIST SP 1800-24 PACS cybersecurity engagement guide

> This is original operational guidance, not NIST practice-guide content, a clinical-safety determination, a HIPAA conclusion, a compliance claim, or professional advice. Confirm current material through [NIST SP 1800-24](https://csrc.nist.gov/pubs/sp/1800/24/final) and the healthcare organization’s approved clinical, security, privacy, legal, safety, and operational decisions.

## Engagement focus

Manage a year-round cybersecurity engagement for picture archiving and communication systems and their connected imaging ecosystem. Connect clinical workflows, patient-image data, PACS components, image modalities, archives, cloud or vendor services, identities, interfaces, data flows, access, configuration, monitoring, continuity dependencies, incidents, and evidence. Treat a reference architecture, scan result, log, or vendor statement as assessment input—not proof of safe clinical operation, adequate privacy protection, or compliance.

Preserve the rationale behind decisions affecting confidentiality, integrity, availability, usability, and clinical performance. Make critical care, patient-safety, operational downtime, emergency access, and vendor support constraints visible. Responsible clinical, safety, privacy, security, and technical leaders must decide whether a proposed change, exception, or response action is appropriate.

## Roles and annual rhythm

Clinical leadership, radiology, imaging operations, biomedical engineering, IT, security, privacy, identity, vendor management, legal, safety, incident-response, continuity, and records owners establish scope and make accountable decisions. Operators maintain asset and interface inventories, approved configurations, access evidence, vendor materials, monitoring records, vulnerability and change actions, downtime or recovery tests, incidents, exceptions, and review history. Reconcile material components, interfaces, owners, and vendors quarterly; review safety-relevant changes promptly; exercise downtime or recovery scenarios during the year; and conduct an annual governance review.

Independent reviewers sample an imaging-data path from clinical purpose through access and configuration evidence, vendor responsibility, continuity evidence, and leadership review, testing traceability. Auditors evaluate supplied evidence without changing clinical systems, authorizing access, deciding patient safety, making privacy or legal conclusions, accepting risk, or issuing an attestation. AI may organize supplied records, flag stale evidence or missing owners, draft workpapers, and prepare review questions. AI cannot alter PACS or clinical settings, grant access, decide care or safety, approve exceptions, make legal conclusions, or attest to conformance.

## Tailored evidence plan

**Source and rights snapshot.** Retain the retrieved version and applicable use terms for the official [NIST SP 1800-24 publication record](https://csrc.nist.gov/pubs/sp/1800/24/final) with approved clinical, security, privacy, legal, safety, and operational direction. This is original evidence planning, not reproduced NIST guidance, clinical advice, or a conformance claim.

### 1. PACS ecosystem and clinical-boundary package

- **Request and owner:** Radiology, imaging operations, biomedical engineering, IT, security, privacy, and vendor owners provide component/modality/archive inventory, clinical workflow and interface map, owner records, data-flow references, and vendor responsibility assumptions.
- **Validate and limit:** Trace one selected image-data path from clinical purpose through identified components, interface, owner, and vendor boundary. This tests supplied traceability; it cannot determine clinical safety, privacy compliance, or data-flow completeness.
- **AI and trigger:** AI may flag missing interface owners or stale supplier references. Humans decide clinical, safety, privacy, and scope boundaries. Refresh after a modality, interface, vendor, clinical workflow, or architecture change.

### 2. Access, configuration, and continuity package

- **Request and owner:** PACS, identity, security, biomedical, and continuity owners provide approved configuration/access baselines, change records, access-review evidence, monitoring summaries, downtime or recovery exercise records, and identified limitations.
- **Validate and limit:** Sample one component or workflow path through its access/configuration record, approved change, and continuity evidence. This cannot alter clinical systems, authorize access, or prove patient-safe recovery.
- **AI and trigger:** AI may organize review metadata and flag missing exercise or approval links. Humans authorize access, changes, and continuity decisions. Recollect after a downtime event, access incident, baseline change, or vendor update.

### 3. Vendor, exception, and corrective-action package

- **Request and owner:** Vendor management, security, clinical, privacy, safety, legal, risk, and independent-review owners provide support commitments, vulnerability/incident follow-up, exceptions, compensating measures, corrective actions, and leadership-review records.
- **Validate and limit:** Trace one vendor issue, exception, or corrective action to human authority, stated limitation, target date, and follow-up evidence. This supports governance observation; it cannot approve a supplier or accept clinical or privacy risk.
- **AI and trigger:** AI may flag expiring support records or overdue action. Humans approve exceptions, risk treatment, and external statements. Review quarterly and after an incident, support change, safety concern, or material supplier change.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
