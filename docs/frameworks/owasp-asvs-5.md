# OWASP ASVS 5.0 — engagement guide

> Original operational guidance, not a rehosted checklist or conformity claim. Use the current authorized [OWASP ASVS project source](https://owasp.org/www-project-application-security-verification-standard/).

## Engagement focus

Have a human select assurance scope and version-pin the authorized source. Link locally approved verification work to components and releases, preserve evidence provenance and change impact, retest meaningful changes, and govern exceptions through accountable risk decisions.

## Roles and annual rhythm

Engineering owners operate remediation and retesting. Independent reviewers test scope, version, samples, evidence, and exceptions. AI may organize authorized artifacts and expose missing retests; it cannot copy or publish the checklist, invent results, issue a conformity claim, approve a release, or accept an exception. Review each material release and refresh annually.

## Tailored evidence plan

**Plan status:** Draft; independent source and skeptical review required before reliance.

**Source and rights snapshot.** Use the authorized [OWASP ASVS project source](https://owasp.org/www-project-application-security-verification-standard/) and the project's published release/source materials; checked 2026-07-31. Version-pin the authorized material selected by the accountable engineering/security owner and respect its license. This original plan neither reproduces verification requirements nor makes a conformance claim.

### 1. Application boundary, version, and assurance-decision record

- **Request and owner:** Application/component inventory, data/trust-boundary summary, selected ASVS version/assurance decision, release scope, and named verification owners from product, architecture, engineering, and security leads.
- **Validate and limit:** Trace a selected release component to the declared boundary, authorized version decision, accountable owner, and change record. This supports defined verification scope; it cannot prove that the scope is adequate or that every component is covered.
- **AI and trigger:** AI may index authorized metadata and flag changed components without associated review. Humans select scope/version and approve release decisions. Refresh on new exposed surfaces, material architecture/data-flow change, or major release.

### 2. Authorized verification and remediation chain

- **Request and owner:** Locally authorized verification workpapers, tester independence/competence record, findings register, secure-development/change links, remediation evidence, and retest record from application-security and engineering owners.
- **Validate and limit:** Sample a finding through its authorized workpaper reference, affected release, remediation, retest, and disposition without copying the ASVS checklist into this repository. This can support traceability of claimed testing; it cannot validate testing quality, prove absence of defects, or issue verification assurance.
- **AI and trigger:** AI may correlate approved finding metadata with release/change records and flag missing retests. Humans perform or authorize tests, assess results, and approve risk decisions. Refresh after material code/dependency/configuration change or failed retest.

### 3. Exception, release, and recurring-assurance record

- **Request and owner:** Time-bound exception/risk decisions, compensating-design rationale, release approval evidence, dependency/security-monitoring inputs, and annual program review from accountable security, engineering, and risk owners.
- **Validate and limit:** Inspect a selection for expiry, approver, affected scope, follow-up, and release linkage. This supports accountable exception handling; it cannot endorse compensating measures or show continuing security.
- **AI and trigger:** AI may surface expired exceptions, affected releases, and missing evidence; authorized humans accept risk and approve releases. Refresh before exception expiry, after a security incident, or at annual program review.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
