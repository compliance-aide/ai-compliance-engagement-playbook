# NIST SP 1800-25 ransomware asset-protection engagement guide

> Original operational guidance, not NIST practice-guide text, a technical design approval, a recovery command, or a compliance claim. Confirm current material through [NIST SP 1800-25](https://csrc.nist.gov/pubs/sp/1800/25/final) and the organization’s approved risk, architecture, and incident-response decisions.

## Engagement focus

Maintain an evidence-backed view of data, devices, applications, configurations, and dependencies whose corruption or destruction would materially affect a business service. Connect each material asset group to accountable owners, data-integrity risks, protective measures, backups, logging, vulnerability and maintenance activity, monitoring coverage, exception decisions, and recovery dependencies. Use the practice guide to structure a defensible protection program; do not treat an inventory, a tool deployment, or an AI-generated assessment as proof that risk is accepted or that an environment is protected.

## Roles and annual rhythm

Assign accountable executive, asset-owner, security, technology, data, platform, application, vulnerability-management, business-continuity, supplier-management, and risk owners. Operators maintain authoritative inventories, ownership and classification records, protection configuration evidence, integrity-check and backup records, logging coverage, vulnerability and maintenance records, supplier attestations, exceptions, and remediation status. Reconcile critical assets and their protection assumptions quarterly; reassess after material service, architecture, supplier, data-classification, or threat changes. Before annual renewal, an independent reviewer samples inventory-to-service links and protection evidence; auditors test the evidence trail without designing safeguards, accepting exceptions, accepting risk, approving architecture, or attesting for management.

AI may reconcile supplied inventory and evidence records, flag missing ownership or stale protection artifacts, trace asset groups to service dependencies, and draft workpapers for human review. AI cannot approve architecture, classify data, accept risk or an exception, alter safeguards, make a compliance conclusion, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** Retain the retrieved version and applicable use terms for the official [NIST SP 1800-25 publication record](https://csrc.nist.gov/pubs/sp/1800/25/final) with approved risk, architecture, incident-response, and operational decisions. This is original evidence-planning language, not NIST practice-guide text, a safeguard design, or a conformance claim.

### 1. Critical-asset and service-dependency package

- **Request and owner:** Asset, data, application, platform, business-continuity, and service owners provide critical-asset inventory, classification/criticality decisions, service-dependency map, ownership, and documented integrity-risk assumptions.
- **Validate and limit:** Trace one selected asset group to a named service, owner, data/integrity rationale, dependencies, and documented scope. This assesses evidence linkage; it cannot establish completeness, acceptable risk, or effective protection.
- **AI and trigger:** AI may identify missing owners or unlinked dependencies. Humans approve criticality and scope. Refresh after material asset, service, classification, architecture, or threat change.

### 2. Protective-measure and recoverability-evidence package

- **Request and owner:** Security, platform, vulnerability-management, backup, and application owners provide approved protection baselines, change records, integrity-check/backup records, maintenance evidence, logging references, and known evidence limitations.
- **Validate and limit:** Sample one asset/service relation through its declared protection baseline, change record, integrity or backup evidence, and accountable review. This cannot validate technical effectiveness, alter safeguards, or authorize recovery.
- **AI and trigger:** AI may organize supplied records and flag missing review dates. Humans approve technical changes and remediation. Recollect after a protection failure, vulnerability, backup issue, or material implementation change.

### 3. Exception, incident, and improvement package

- **Request and owner:** Risk, incident-response, supplier, continuity, records, security, and independent-review owners provide exception decisions, incident lessons, supplier notices, remediation/retest records, transition plans, and management-review minutes.
- **Validate and limit:** Trace one selected exception or protection finding to human authority, limitation, corrective action, due date, and retest or disposition. This supports improvement tracking; it cannot accept risk or conclude ransomware resilience.
- **AI and trigger:** AI may flag overdue exceptions or missing retest links. Humans decide risk acceptance, closure, and external statements. Review quarterly and after a material incident, supplier notice, control change, or threat change.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
