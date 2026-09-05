# FISMA federal information security — engagement guide

> Original operational guidance, not an authorization, statutory compliance assertion or permission to submit a government report. Draft pending independent review.

## Source and applicability

Start with the [current statutory collection](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title44-section3551), current OMB/CISA direction and agency policy. The [NIST FISMA overview](https://csrc.nist.gov/topics/laws-and-regulations/laws/fisma) distinguishes the 2014 modernization act from the original 2002 act.

The [2024 edition of 44 USC 3554](https://www.govinfo.gov/content/pkg/USCODE-2024-title44/html/USCODE-2024-title44-chap35-subchapII-sec3554.htm) covers agency security responsibilities, including information and systems operated on its behalf. Subsection (b)(5) specifies risk-based testing no less than annually, including management, operational and technical controls of every inventoried system. This does not mean a quarterly schedule is universally required.

Source limitation: current preliminary-code requests failed during this draft. The 2024 section 3554 text was read; current amendments, section 3555 independent-evaluation requirements, reporting-year instructions and agency-specific rules remain to be verified. Do not use this draft alone to determine a legal deadline, reporting population or evaluation method.

## Engagement focus

Reconcile agency program responsibilities, system scope, operational evidence, deficiencies and reporting inputs. Separate program effectiveness, system control results, authorization status and report delivery. A provider assurance package does not establish the agency's own implementation or fulfill all agency responsibilities.

## Roles

The accountable agency official owns decisions. CIO/security leadership owns program coordination; system and common-control owners maintain implementation evidence; incident and reporting officials own their respective processes. Qualified assessors perform authorized tests. An independent reviewer challenges evidence and reporting methodology; confirm the statutorily required evaluation route separately. Legal and authorized reporting officials determine obligations and submission authority.

AI may reconcile authorized records, calculate reproducible measures and draft workpapers. AI cannot determine impact categories, grant authorization, accept risk, submit reports, close incidents or certify compliance. Operators retain responsibility for changes and evidence; a named human approves final conclusions.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Record agency/component, reporting period, legal/policy sources, authorized scope, systems, officials, evidence access and handling rules. Obtain the actual reporting definitions and deadlines rather than reusing last year's form. Missing authority blocks dependent action; missing evidence remains a tracked gap.

## Ordered workflow

1. **Establish the requirement register.** Identify each applicable source, version, responsible official, affected population and required output. Separate statute, agency instruction and internal practice. Output: approved register with unresolved applicability questions assigned.
2. **Reconcile the population.** Compare system inventories, service/provider records, authorization boundaries, acquisition and retirement records. Preserve orphaned systems and boundary conflicts. Output: complete scoped inventory; do not erase uncovered systems to improve a percentage.
3. **Trace responsibilities.** For each system, map approved categorization, selected controls, agency parameters and provider/common-control dependencies to current owners and artifacts. Output: responsibility matrix that distinguishes inherited portions from agency implementation. Do not infer inheritance from a vendor logo.
4. **Collect and assess operation.** Connect the approved assessment plan to current configurations, monitoring, training, incident, contingency and other applicable evidence. Record criterion, method, time, scope and observed result. Output: evidence register and all coverage gaps; a clean scanner report cannot prove an unobserved asset is secure.
5. **Track deficiencies.** Reconcile findings, incidents, remediation plans, exceptions and retests. Preserve original observations and owner decisions. Output: current action register; a closed ticket or accepted risk does not convert failed implementation into a passed test.
6. **Reconcile reporting.** Calculate each measure from its complete defined population, with reproducible numerator, denominator, period and exclusions. Match narrative claims to evidence and include unresolved limitations. Output: draft report inputs with method and source references, not a submitted report.
7. **Obtain review and decisions.** Provide the independent reviewer the complete packet and disagreements. Route authorization, risk treatment and reporting decisions to their designated officials. Output: dated decision references, open actions and next review triggers. Verify any authorized submission separately through a receipt.

## Evidence and test plan

### Inventory, ownership and boundary package

Restore the prior PR340 inventory package with full-population reconciliation. Agency/component and system owners supply systems, services, assets, interfaces, responsible officials and change history. Record missing rows, conflicting boundaries and unverified exclusions explicitly. Trace every reported system to its accountable owner and evidence status; completeness of inventory is separate from depth of testing.

### Operational security, incidents and remediation package

Security operations, incident and control owners supply assessment outputs, configuration history, monitoring coverage, incident timelines, training and continuity evidence where applicable, and corrective-action records. Track each known deficiency through owner assignment, action, retest and decision. Separate remediation claimed from remediation observed. Keep notification deadlines tied to the applicable trigger and current source; do not wait for an annual reporting cycle to route an incident.

### Independent review and reporting package

Leadership supplies the reporting definitions, complete source populations, calculations, evidence dates, evaluation workpapers, unresolved disagreements and approval records. Recompute each submitted measure's inputs and reconcile corrections through all affected tables and narrative. Preserve version history. A selected successful measure does not validate the full report; disclose exactly what was and was not verified.

## Failure branches and decisions

- Unknown inventory coverage: classify the completeness claim inconclusive and retain all discovered systems; assign reconciliation to the inventory owner.
- Confirmed omitted in-scope system: mark the complete-coverage claim not_supported. Other tested systems retain their own results.
- Provider evidence lacks agency configuration: mark the dependent implementation claim inconclusive or not_tested, according to what was attempted.
- Incident or reporting clock unclear: escalate promptly to the responsible official with known trigger times and source gaps; do not invent a deadline.
- Conflicting report versions: stop approval of the affected claim until the owner reconciles the source and downstream copies.

Fictional desk case: a report says all ten systems were assessed, but the evidence covers nine and the tenth is confirmed in scope. The report's complete-coverage claim is not_supported; the tenth system's controls are not_tested. No actual agency assessment was performed here.

## Cadence and renewal

Use verified statutory minimums and current agency/reporting instructions. Record risk-based operational frequencies and event triggers for acquisition, boundary changes, incidents, failed retests and source changes. Do not substitute an annual report for ongoing operations, or invent a universal authorization expiration. Revalidate affected evidence after changes.

## Completion and handoff

Deliver the source/applicability register, full inventory, responsibility matrix, evidence and assessment records, deficiency register, reproducible reporting inputs, review disagreements and named decision owners. Classify assertions as supported, not_supported, inconclusive, not_applicable or not_tested with reasons. Keep task status separate from evidence status. Final evaluation, authorization, submission and compliance conclusions require their own evidence and authority.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) and [agent runbook](../agent-runbook.md). Keep sensitive agency evidence in its approved repository, never this public project.
