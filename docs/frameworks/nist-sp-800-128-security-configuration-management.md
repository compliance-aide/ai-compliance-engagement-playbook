# NIST SP 800-128 security-focused configuration-management engagement guide

> Original operational guidance, not NIST guidance, a production-change authorization, a configuration approval, or a compliance claim. Confirm current material through [NIST SP 800-128](https://csrc.nist.gov/pubs/sp/800/128/upd1/final) and the organization’s approved security, engineering, change, and risk decisions.

## Engagement focus

Operate security-focused configuration management that connects material systems to secure baselines, configuration ownership, approved change paths, monitoring, variance analysis, exceptions, remediation, and service impacts. Treat configuration evidence as a managed assurance record, not as proof that every instance is secure or that a proposed, emergency, or automated change is approved.

## Roles and annual rhythm

Assign accountable executive, security, platform, network, application, cloud, change-management, service-owner, risk, and supplier-management roles. Operators maintain system and baseline inventories, configuration standards, change records, assessment evidence, variance and exception records, monitoring outputs, rollback records, supplier evidence, and remediation status. Review material baselines, variance assumptions, exceptions, and high-impact changes quarterly; test representative baseline deployment, change, detection, and rollback paths at least annually and after material architecture, service, supplier, or tooling changes. Before annual renewal, an independent reviewer samples baselines through approved change evidence; auditors test the evidence trail without authorizing production changes, setting technical baselines, accepting risk, or attesting for management.

AI may organize supplied configuration and change evidence, identify stale reviews or missing ownership, correlate variances with recorded services, and draft workpapers for human review. AI cannot alter configurations, authorize production changes, approve a baseline, accept risk or an exception, make a compliance conclusion, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [NIST SP 800-128 publication record](https://csrc.nist.gov/pubs/sp/800/128/upd1/final), recording version and use terms. This is original evidence planning, not configuration guidance, production authorization, or an assertion that a system is secure.

### 1. Asset, baseline, and ownership package

- **Request and owner:** Platform, network, application, cloud, and service owners provide in-scope asset inventories, approved baseline identifiers, configuration-owner assignments, applicability decisions, dependency maps, and baseline review dates.
- **Validate and limit:** Trace a selected production-relevant asset to its accountable owner, applicable baseline, dependency context, and review record. This assesses accountability and traceability; it cannot approve a baseline or confirm every setting is correctly implemented.
- **AI and trigger:** AI may reconcile inventories and flag assets without baseline or owner evidence. Humans determine scope and baseline applicability. Refresh after asset, architecture, supplier, or service change.

### 2. Change, variance, and rollback package

- **Request and owner:** Change-management, engineering, security, and operations owners provide approved change records, pre-change checks, implementation records, variance analyses, exception decisions, rollback plans/results, and service-impact records.
- **Validate and limit:** Sample a normal, emergency, or failed change from request through human approval, implementation record, variance disposition, and rollback or verification evidence. This cannot authorize, execute, or retrospectively approve a change.
- **AI and trigger:** AI may link change and variance records and surface missing approvals. Humans authorize changes, exceptions, and rollback decisions. Recollect after high-impact change, failed deployment, or unapproved variance.

### 3. Monitoring, remediation, and assurance package

- **Request and owner:** Security monitoring, service, risk, supplier-management, and independent-review owners provide configuration assessment outputs, alert/variance tickets, remediation evidence, supplier attestations where applicable, exception register, and sampled-review workpapers.
- **Validate and limit:** Trace sampled variance to detection date, owner, severity rationale, human disposition, remediation or approved exception, and follow-up check. This cannot accept residual risk, certify supplier evidence, or conclude compliance.
- **AI and trigger:** AI may prioritize aging variances and prepare review packets. Humans validate findings, accept risk, and close remediation; independent reviewers sample the chain. Review quarterly and after material tooling or supplier change.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
