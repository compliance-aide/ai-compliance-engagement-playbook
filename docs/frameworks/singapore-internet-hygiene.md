# Singapore Internet Hygiene engagement guide

> Original operational guidance, not CSA criteria, an Internet Hygiene Rating, or a public assurance claim. Confirm current official resources through the [Cyber Security Agency of Singapore Internet Hygiene Portal](https://www.csa.gov.sg/resources/internet-hygiene-portal/).

## Engagement focus

Maintain an evidence record for internet-facing services: approved domains and services, accountable owners, permitted assessment results, remediation, configuration changes, supplier dependencies, retests, and communications.

## Roles and annual rhythm

Service owners maintain scope; security and operations teams validate remediation; independent reviewers test evidence traceability. AI can organize approved assessment records, surface aging issues, and draft review questions, but cannot run unapproved scans, change internet-facing systems, determine a rating, or make public claims. Review scope and results on a cadence and after material domain or service changes, with human approval for all external communications.

## Tailored evidence plan

**Source and rights snapshot.** Use the [CSA Internet Hygiene Portal](https://www.csa.gov.sg/resources/internet-hygiene-portal/) as the official program source; checked 2026-07-31. Current assessment coverage, rating method, publication process, and reuse rights require confirmation from CSA materials and accountable Singapore security/legal owners. This original plan does not reproduce CSA criteria or determine a rating.

### 1. Internet-facing scope and ownership package

- **Request and owner:** Service, network, cloud, DNS, and security owners provide an approved domain, IP, certificate, hosting, service, and supplier inventory; business criticality; accountable owners; authorization boundaries; and documented scope changes.
- **Validate and limit:** Trace a selected public endpoint to an approved inventory entry, owner, business purpose, hosting/supplier context, and review date. This supports scope traceability; it cannot discover all exposed assets, authorize testing, or determine program coverage.
- **AI and trigger:** AI may reconcile approved inventories and flag missing ownership or expiry dates. Humans approve scope and assessment authorization. Refresh before new public exposure and after DNS, certificate, hosting, supplier, or ownership change.

### 2. Authorized assessment, remediation, and retest package

- **Request and owner:** Security and operations owners provide authorized assessment outputs, finding intake, severity/risk review, change approvals, remediation evidence, rollback references, retest records, and exceptions.
- **Validate and limit:** Trace a selected finding through authorization, source result, human triage, remediation/change evidence, retest, and closure authority. This supports a controlled remediation history; it cannot prove absence of weaknesses, override an outage decision, or establish a rating.
- **AI and trigger:** AI may organize approved results and flag aging findings; it cannot probe systems, alter configurations, or close findings. Recollect after a critical finding, failed retest, material service change, or overdue exception.

### 3. Communications, supplier, and governance package

- **Request and owner:** Security, legal, supplier, communications, and leadership owners provide supplier escalation records, management review, public-claim approvals, source-change watch, remediation metrics, and annual scope review.
- **Validate and limit:** Trace a selected supplier escalation or external statement to supporting facts, authority, limitation, and follow-up. This supports accountable communications; it cannot make a public rating claim or replace independent review.
- **AI and trigger:** AI may prepare a restricted review packet and flag stale approvals. Humans approve external statements, risk acceptance, and closure. Review at least annually and after supplier, program, or material incident changes.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
