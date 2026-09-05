# EU Cyber Resilience Act engagement guide

> Original operational guidance, not Regulation (EU) 2024/2847 text, legal advice, a conformity assessment, or a compliance claim. Confirm current requirements through the [EU Cyber Resilience Act regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R2847).

## Engagement focus

Maintain a product-cybersecurity engagement record that connects products with digital elements, accountable manufacturer and economic-operator roles, product and software lifecycle evidence, vulnerability handling, supplier dependencies, security events, remediation, required decision records, and independent assurance. Preserve a clear boundary between AI-supported evidence coordination and accountable legal, product-safety, market-access, and disclosure decisions.

## Roles and annual rhythm

Executive, product, engineering, security, legal, privacy, and quality authorities retain accountable decisions; product and supplier owners preserve lifecycle evidence; independent reviewers test traceability and readiness. AI may organize authorized records, identify incomplete evidence, correlate known product dependencies, and draft questions or workpapers, but cannot determine legal scope, make a conformity or market-access determination, approve a release, accept risk, decide a reporting obligation, alter production systems, or claim compliance. Review annually and before material product, software, vulnerability, supplier, incident, market, or regulatory changes.


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
