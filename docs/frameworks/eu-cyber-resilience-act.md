# EU Cyber Resilience Act engagement guide

> Original operational guidance, not Regulation (EU) 2024/2847 text, legal advice, a conformity assessment, or a compliance claim. Confirm current requirements through the [EU Cyber Resilience Act regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R2847).

## Engagement focus

Maintain a product-cybersecurity engagement record that connects products with digital elements, accountable manufacturer and economic-operator roles, product and software lifecycle evidence, vulnerability handling, supplier dependencies, security events, remediation, required decision records, and independent assurance. Preserve a clear boundary between AI-supported evidence coordination and accountable legal, product-safety, market-access, and disclosure decisions.

## Roles

Executive, product, engineering, security, legal, privacy, and quality authorities retain accountable decisions; product and supplier owners preserve lifecycle evidence; independent reviewers test traceability and readiness. AI may organize authorized records, identify incomplete evidence, correlate known product dependencies, and draft questions or workpapers, but cannot determine legal scope, make a conformity or market-access determination, approve a release, accept risk, decide a reporting obligation, alter production systems, or claim compliance. Review annually and before material product, software, vulnerability, supplier, incident, market, or regulatory changes.


## Source and applicability

Record the actual product/version, operator activity, market, support period and governing source. The [Commission summary](https://digital-strategy.ec.europa.eu/en/policies/cra-summary) identifies main application from 11 December 2027, distinct from Article 14 reporting from 11 September 2026. It covers products and separately marketed components, with scope/exclusions and operator-specific obligations requiring legal review. Do not assume every cloud service is covered, or every open-source component exempt. Obtain the actual legal basis and category decision before choosing the conformity route.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Obtain the full product/version inventory, market-entry records, dependency provenance, support commitments, current risk assessment, test records and legal decisions. Assign product, engineering, security and legal owners. Define authorized QA targets, safe test methods, evidence storage and release boundaries. A text-only agent prepares exact requests; a tool-capable agent records permitted observations without expanding its authority.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Fix perimeter | Product/legal reconcile product, version, operator, market and category. | Approved scope and obligation dates; unresolved classification remains open. |
| 2. Map requirements | Quality/security inventory all applicable source requirements and decisions. | Complete disposition ledger with owners; do not replace it with a scan summary. |
| 3. Map lifecycle risk | Engineering links intended use, foreseeable misuse, dependencies and risk treatment. | Version-specific risk and implementation records with explicit assumptions. |
| 4. Collect and test | Authorized teams preserve build, component, configuration and QA evidence. | Repeatable observations, full coverage accounting and recorded failures. |
| 5. Handle vulnerabilities | Product security correlates signals with affected versions and approved decisions. | Separate investigation, remediation, reporting and customer-communication work items. |
| 6. Retest changes | Engineering verifies the fix and affected behavior under the approved method. | Fixed-build evidence and remaining deployed-version coverage; merge is not distribution. |
| 7. Prepare conformity package | Quality/legal assemble the required route's documentation and decisions. | Reviewable version-bound package; no AI signature, CE claim or release approval. |
| 8. Maintain support | Product/security track updates, new signals and support commitments. | Current ownership, action queue and source/change review triggers. |

## Failure branches and decisions

- Dependency inventory is stale: reconcile it against the actual build before deciding affectedness; a missing entry is not proof of absence.
- Scanner reports no findings after an error: record `not_tested`, preserve the error and restore collection before drawing conclusions.
- Fix exists only in source control: retain affected released versions and distribution gaps; do not close customer exposure from a merge.
- Product name is unchanged but functionality changes: reopen scope/category and affected evaluation records.
- Support date is promised without operating evidence: separate the commitment from demonstrated vulnerability-handling capability.
- A self-assessment route is assumed: obtain the approved category and route decision with applicable conditions before preparing an authoritative declaration.
- A report is drafted but no receipt exists: preserve its pending state and resolve submission outcome before any retry.

## Evidence and test plan


**Source and rights snapshot.** Use the official [EU Cyber Resilience Act regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R2847), applicable Commission guidance, market/supervisory direction, and qualified legal/product-safety review; prior snapshot 2026-07-31; verify current source status. This is original lifecycle-evidence planning, not Regulation text, a product classification, conformity assessment, CE-marking basis, vulnerability-reporting conclusion, or market-access claim. Authorized humans confirm applicable role, product scope, timing, source rights, and permitted evidence use.

### 1. Product, operator, and lifecycle-scope package

- **Request and owner:** Product, legal, quality, engineering, security, supply-chain, and economic-operator owners provide product/SKU and software-component inventories, accountable role records, intended use and supported lifecycle records, release/version history, distribution markets, supplier relationships, and material-change decisions.
- **Validate and limit:** Trace one selected product/version to its accountable owner, declared operator role, component/dependency record, supported lifecycle, distribution record, and review date. This cannot decide whether it is a product with digital elements, determine category or applicability, or authorize placing it on the market.
- **AI and trigger:** AI may reconcile approved product and dependency metadata and flag orphaned versions or stale owner records. Humans decide product scope, role, classification, lifecycle commitments, and market action. Refresh before a material product, software, supplier, market, or ownership change.

### 2. Secure-development, vulnerability, and remediation package

- **Request and owner:** Engineering, security, product-security, quality, and supplier owners provide secure-development decision records, component provenance/SBOM references where maintained, testing and release-evidence references, vulnerability intake/triage records, remediation decisions, customer-support coordination, supplier notices, and exceptions.
- **Validate and limit:** Sample one vulnerability or material release through source intake, affected-product/version assessment record, accountable decision, remediation/release evidence, customer/supplier coordination, and closure/retest record. This does not prove absence of vulnerabilities, validate all security properties, direct a production change, or determine notification duty.
- **AI and trigger:** AI may correlate authorized component and case metadata, flag incomplete decision trails, and prepare workpapers. Humans decide severity, remediation priority, exception/risk acceptance, release, and external communication. Refresh after a new vulnerability, exploit signal, dependency change, failed test, or material release.

### 3. Technical-file, reporting, and independent-readiness package

- **Request and owner:** Legal, quality, product, security, compliance, and independent-review owners provide controlled evidence indexes, declarations/assessment artifacts only where authorized, post-market monitoring records, incident/reporting decision logs, authority-contact records, limitation statements, corrective-action tracking, and reviewer workpapers.
- **Validate and limit:** Trace a selected readiness statement, event, or corrective action to controlled source evidence, accountable human decision, limitation, follow-up owner, and review date. This cannot establish technical-documentation completeness, make a conformity declaration, determine reportability, or attest for management.
- **AI and trigger:** AI may organize authorized evidence references and flag stale source or overdue action links; it cannot prepare or submit an authoritative declaration or report. Humans approve documentation, reporting, corrective action, and external statements. Refresh before formal milestones, after an event or regulatory change, and at annual independent review.


## Cadence and renewal

Review before each material release and after dependency, vulnerability, incident, market, role or source changes. Maintain reporting escalation independently of periodic product reviews. Reconcile support commitments and affected versions through retirement; a new release does not erase obligations for older versions.

## Completion and handoff

Deliver the product/role/source manifest, full requirement ledger, risk and dependency records, test and retest evidence, support plan, reporting decisions and unresolved actions. Bind every readiness statement to its version and scope. Independent source, engagement, skeptical and rights review plus named human publication approval remain required. This draft has not established conformity, tested an actual product or submitted a report.

## Reporting-readiness workflow

The [Commission reporting guidance](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting), updated 31 July 2026 and checked 2026-09-04, identifies 11 September 2026 as the start of manufacturer reporting duties for actively exploited vulnerabilities and severe product-security incidents. It describes early warning within 24 hours of awareness and notification within 72 hours, with different final-report triggers. Read Article 14 and current guidance to establish the exact branch, trigger, content and recipient before calculating an engagement deadline. Do not postpone this work to the main product-requirements date.

Use the [agent runbook](../agent-runbook.md) for each evidence check. Keep this reporting track linked to product scope, vulnerability handling and lifecycle records; it does not replace those workstreams.

1. **Fix authority and product scope.** Legal/product owners identify the manufacturer, affected products/versions, distribution facts and applicable reporting basis. Record unresolved scope questions and their decision owner.
2. **Capture the signal.** Product security preserves the original report, receipt timestamp, affected versions, exploitation or incident evidence and source reliability. Distinguish initial signal receipt from the facts supporting legal awareness; do not reset a clock when the ticket changes teams.
3. **Evaluate both triggers.** The accountable security/legal owners consider actively exploited vulnerability and severe incident routes separately. A vulnerability scan result alone does not establish active exploitation. Lack of a named vulnerability does not resolve the incident route.
4. **Record the clock.** Save the approved trigger, event time/timezone, applicable paragraph, calculated milestones and reviewer. Escalate possible live duties immediately; missing details do not justify waiting silently for the weekly meeting.
5. **Prepare the exact packet.** Collect available facts and label unknowns. Assign owners for missing information. Track early warning, notification and final-report states separately; do not wait for remediation completion to prepare earlier stages.
6. **Verify submission readiness.** The authorized submitter checks current official platform instructions, entity/recipient context and access through permitted means. A planned launch date or platform information page does not prove operational access. Use only an explicitly offered test facility for rehearsal; never file a fictional report in the live system.
7. **Obtain the required decision and readback.** AI prepares the reviewable draft; the designated human authorizes submission. Preserve the submitted version, platform receipt and any subsequent requests. A saved draft or successful browser click is not a submission receipt.
8. **Follow through.** Track corrective-measure availability, incident updates and the appropriate final-report trigger. Keep user-notification decisions, regulator reporting and product remediation separately owned. Closure requires the applicable decisions and evidence, not merely a patched build.

### Failure handling and fictional exercise

If access fails, record the exact error and escalate through the approved reporting contingency route; do not claim submission or repeatedly send duplicates when the outcome is uncertain. If a scope or clock interpretation conflicts, preserve both sources and obtain legal resolution while continuing unaffected packet preparation.

In a fictional QA exercise, a severe incident is confirmed but no exploited vulnerability has been identified. The agent records the incident facts and routes the severe-incident reporting decision rather than closing the case because the vulnerability list is empty. It prepares a draft and an internal timeline only. This demonstrates routing logic, not a determination that any real incident is reportable or that the reporting platform works.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
