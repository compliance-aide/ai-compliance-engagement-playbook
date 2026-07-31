# UK NCSC Protective Domain Name Service engagement guide

> Original operational guidance, not NCSC service instructions, an eligibility decision, a command to change DNS, a certification, or a compliance claim. Confirm current eligibility and operating guidance through the [NCSC Protective Domain Name Service](https://www.ncsc.gov.uk/information/pdns) and the organization’s approved security, privacy, legal, architecture, and change-management decisions.

## Engagement focus

Operate a governed protective-DNS service lifecycle for in-scope networks and devices. Establish service eligibility, asset and traffic scope, design decisions, authorized configuration changes, availability and failover expectations, monitoring, blocked-domain handling, user support, exception treatment, privacy considerations, suppliers, and evidence of periodic review. A blocked request, a service-status report, or use of a protective resolver does not prove complete coverage, absence of malicious activity, service availability, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, network, identity or endpoint, architecture, service-owner, privacy, legal, procurement, supplier-management, service-desk, incident-response, business-continuity, and records-management roles. Operators maintain eligibility records, approved network and device scope, architecture and configuration baselines, change approvals, monitoring and availability evidence, blocked-domain investigation records, exception and allow-list decisions, service-desk records, continuity tests, supplier assurance, and user communications. Reconcile protected networks and device populations quarterly; review block events, exceptions, operational performance, privacy impact, and unresolved risks at least quarterly; and complete an annual management review after material network, endpoint, provider, DNS, remote-work, or threat changes. Before annual renewal, an independent reviewer samples scope, change, exception, and block-event evidence; auditors test the evidence trail without determining eligibility, modifying DNS, authorizing allow lists, accepting risk, or attesting for management.

AI may organize supplied configuration, event, and review evidence, compare approved scope with documented service coverage, flag missing ownership or overdue follow-up, and draft workpapers for human review. AI cannot determine eligibility, change DNS or endpoint settings, approve an exception or allow list, decide a block is benign, accept risk, make a compliance conclusion, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** Record retrieval date, eligibility assumptions, service-status check, and applicable terms for the official [NCSC Protective Domain Name Service](https://www.ncsc.gov.uk/information/pdns). This is original planning guidance, not operational service instructions; named security, network, privacy, legal, and change authorities decide eligibility and configuration.

### 1. Eligibility, protected-scope, and design package

- **Request and owner:** Security, network, endpoint, architecture, service, privacy, legal, and asset owners provide eligibility decision, approved network/device inventory, resolver and traffic-flow design, named service contacts, exclusions, dependency map, and architecture approvals.
- **Validate and limit:** Trace a selected protected network or device population to authoritative inventory, owner, approved design, eligibility decision, and stated exclusion where relevant. This supports scope traceability; it cannot determine eligibility, prove all traffic is protected, or authorize configuration.
- **AI and trigger:** AI may compare supplied inventories and flag unmatched scope or owners. Humans determine eligibility, scope, architecture, and privacy basis. Refresh after network, device, remote-access, provider, or ownership change.

### 2. Configuration-change, availability, and continuity package

- **Request and owner:** Network, service, change, continuity, supplier, and security owners provide approved DNS/endpoint change records, baseline references, implementation validation, monitoring/availability records, failover design, outage tickets, and continuity-test evidence.
- **Validate and limit:** Follow a selected material change or outage from request through authorization, validation, monitoring, and recovery/follow-up evidence. This supports controlled-operation evidence; it cannot alter DNS, guarantee availability, or prove configuration completeness.
- **AI and trigger:** AI may assemble read-only change timelines and flag missing validation. Humans authorize changes, failover, and restoration. Recollect after material change, outage, failed test, or supplier transition.

### 3. Block-event, exception, and governance package

- **Request and owner:** Security operations, service desk, incident-response, privacy, legal, risk, and executive owners provide selected blocked-domain cases, investigation records, allow-list or exception requests, approvals, user-support records, trend measures, and management-review minutes.
- **Validate and limit:** Trace a selected block or exception from detection through accountable investigation, approved disposition, expiry/review date, and follow-up. This supports a bounded handling trail; it cannot determine maliciousness, approve an allow list, or establish absence of compromise.
- **AI and trigger:** AI may group records and identify stale exceptions. Humans decide investigation outcomes, exceptions, notifications, and risk treatment. Review quarterly and after material block patterns, incidents, or privacy concerns.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
