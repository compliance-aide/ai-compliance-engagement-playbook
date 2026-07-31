# CISA BOD 18-01 email-and-web-security engagement guide

> Original operational guidance, not Binding Operational Directive text, a DNS or email configuration instruction, a federal applicability determination, or a compliance claim. Confirm current material through [CISA’s cybersecurity directives](https://www.cisa.gov/news-events/directives) and applicable agency, component, system-owner, and authority direction.

## Engagement focus

For applicable Federal Civilian Executive Branch internet services, maintain a governed email-and-web-security engagement that connects owned domains and services to accountable owners, approved configuration baselines, DNS and mail evidence, web-service protections, monitoring, exceptions, supplier dependencies, and change records. Treat observed configuration records as inputs to review, not as authority to alter DNS, email routing, certificates, web protections, or public-facing services.

## Roles and annual rhythm

Assign accountable agency or component executive, domain-owner, email, web, DNS, security, network, platform, communications, change-management, and supplier-management roles. Operators maintain domain and service inventories, baseline and configuration evidence, validation and monitoring records, exception approvals, provider records, change and rollback artifacts, assessment findings, and closure status. Review material domains, services, configuration assumptions, monitoring results, and exceptions quarterly; reassess after material domain, provider, certificate, routing, application, or network changes. Before annual renewal, an independent reviewer samples owned services from scope through validation evidence; auditors test the evidence trail without altering DNS or services, authorizing production changes, accepting risk, or attesting for management.

AI may organize supplied domain and service evidence, flag stale validation or missing ownership, relate documented configurations to recorded services, and draft workpapers for human review. AI cannot alter DNS, email, web, or certificate settings; authorize a change; accept risk or an exception; determine directive applicability; make a compliance conclusion; attest for management; or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [CISA cybersecurity directives index](https://www.cisa.gov/news-events/directives) and applicable agency direction at engagement start; checked 2026-07-31. This is original evidence-planning guidance, not directive text, a configuration instruction, an applicability determination, or a federal compliance conclusion.

### 1. Domain, service, and accountable-boundary package

- **Request and owner:** Domain, web, email, and DNS owners provide approved domain and service inventories, registrant/provider relationships, accountable-owner records, service purpose, routing or hosting dependencies, and documented scope assumptions.
- **Validate and limit:** Independently trace a selected public domain or service from its inventory record to accountable owner, dependency record, review date, and a documented scope decision. This cannot prove all domains are known, determine directive applicability, or authorize a domain or service change.
- **AI and trigger:** AI may compare supplied inventories and flag missing ownership, stale review dates, or inconsistent dependencies. Authorized agency humans determine scope and approve changes. Refresh after domain acquisition, retirement, hosting or routing change, and quarterly review.

### 2. Email, DNS, and web-protection operating-evidence package

- **Request and owner:** Email, DNS, web, security, and platform operators provide approved baseline references, authorized configuration exports or validation records, certificate/service-protection records, monitoring results, change tickets, rollback evidence, and supplier attestations where applicable.
- **Validate and limit:** Sample one owned email or web service from approved baseline through configuration evidence, validation date, responsible owner, change record, and any recorded exception. This does not independently test every endpoint, establish effective protection, or alter production settings.
- **AI and trigger:** AI may organize read-only evidence and identify stale validations or unmatched service records. Humans authorize technical tests, production changes, exceptions, and closure. Refresh after certificate, provider, routing, platform, material configuration, or monitoring change.

### 3. Exception, monitoring, and independent-challenge package

- **Request and owner:** Security governance, service owners, and supplier managers provide exception requests, compensating-action records, monitoring/escalation evidence, expiry dates, approval records, independent review workpapers, and remediation follow-up.
- **Validate and limit:** Trace a selected exception or monitoring alert from observation through owner assignment, human decision, compensating action, review date, and current status. This supports a bounded evidence observation; it cannot accept risk, certify continuous monitoring, or submit an authoritative report.
- **AI and trigger:** AI may flag expiring exceptions and assemble review packets. Accountable humans approve risk treatment, external communications, and corrective-action closure. Refresh after a material alert, missed review, exception expiry, or annual independent review.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
