# CISA Continuous Diagnostics and Mitigation engagement guide

> Original operational guidance, not CISA program material, a dashboard conclusion, a risk score, an authorization decision, or a compliance claim. Confirm current material through the [CISA Continuous Diagnostics and Mitigation program overview](https://www.cisa.gov/sites/default/files/publications/cdm-program-overview-fact-sheet-012022-508.pdf) and applicable participation, agency, component, and authority direction.

## Engagement focus

For participating or aligned government environments, operate continuous diagnostics and mitigation as an evidence-driven capability that connects asset, identity, network, and data-protection visibility to accountable risk treatment. Maintain records for data sources, quality controls, dashboard assumptions, prioritization, remediation handoffs, exceptions, and improvements. Treat a sensor, dashboard, or score as decision support—not as proof of complete coverage, a vulnerability finding, or an authorization to change a system.

## Roles

Assign accountable executive, program, security-operations, asset-management, identity, network, data, platform, application, risk, reporting, and supplier-management roles. Operators maintain capability scope, data-source inventories, collection and quality evidence, dashboard and prioritization records, remediation handoffs, exception approvals, reporting artifacts, supplier evidence, and closure status. Review material data coverage, quality trends, priority-risk handling, and exceptions quarterly; reassess after material system, sensor, identity, network, data, provider, or reporting changes. Before annual renewal, an independent reviewer samples records from source through risk-treatment evidence; auditors test the evidence trail without changing systems, setting risk scores, accepting risk, submitting authoritative reports, or attesting for management.

AI may organize supplied program evidence, flag missing ownership or stale data-quality records, correlate documented findings with recorded assets and treatments, and draft workpapers for human review. AI cannot change systems, determine risk scores, approve remediation, accept risk or an exception, make a compliance conclusion, attest for management, or replace independent review.

## Source and applicability

The official overview linked above describes tools, integration and agency/federal dashboards supporting asset, identity/access, network and data-protection capabilities. Verify current participation agreements, dashboard release, data contracts, scoring definitions and agency obligations; the historical overview alone does not define today's implementation. CISA's [2026 training bulletin](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/4154543) describes evolving dashboard integrations. Do not infer an agency has enabled a capability merely because the product supports it.

## Before starting

Use the [agent runbook](../agent-runbook.md). Obtain capability scope, authoritative inventories, feed owners, collection schedules, transformations, dashboard version, metric definitions, known gaps and treatment records. Record authorized environments and data handling. Reuse valid read-only authorization; feed installation, permissions and production changes require their applicable authority.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Define the implemented boundary | Program lead verifies capabilities actually deployed and applicable reporting obligations. | Versioned capability/source map with owners and unresolved obligations. Planned capabilities stay separate from operating ones. |
| 2. Reconcile source populations | Asset, identity, network and data owners compare independent inventories to collection scope. | Complete declared populations, stable identities and documented exclusions. Duplicate records and address reuse require time-aware reconciliation. |
| 3. Trace the pipeline | Integration owners map collection, transformation, storage, agency dashboard and required downstream delivery. | Each stage has owner, freshness criteria, failure signal and evidence location. A healthy first stage does not prove downstream delivery. |
| 4. Validate data quality | Data reviewers check actual collection times, errors, missing fields, joins, duplicates and source-to-dashboard counts. | Coverage and freshness record with explicit gaps. Null or missing data is not zero risk. |
| 5. Interpret priorities | Security owner reviews source findings, approved scoring definitions, business context and contradictory evidence. | Source-linked prioritization decision. AI may flag inconsistencies but cannot invent government scoring logic or accept risk. |
| 6. Treat findings and feed defects | Service owners repair security issues; integration owners repair data defects under approved change control. | Separate linked work items with acceptance criteria. Fixing ingestion does not remediate a vulnerability. |
| 7. Verify outcomes | Independent reviewer checks retests and refreshed downstream records against original evidence. | Observed correction and updated reporting state. A lower score caused by dropped assets is a coverage failure, not improvement. |
| 8. Handoff and sustain | Program/reporting owners reconcile the full register and required delivery receipts. | Open gaps, owners, review schedule and evidence-backed metrics; no unsupported coverage claim. |

## Evidence and test plan

**Source and rights snapshot.** Use the official [CISA CDM program overview](https://www.cisa.gov/sites/default/files/publications/cdm-program-overview-fact-sheet-012022-508.pdf), current participation direction, and component policy at engagement start; prior locator snapshot 2026-07-31; current implementation review pending. This plan is original guidance and does not reproduce program materials, define a government score, or certify coverage.

### 1. Data-source, asset, and coverage-quality package

- **Request and owner:** Asset-management, platform, endpoint, identity, network, and data owners provide authorized source inventories, collection scope, asset/account population definitions, connector or feed health records, coverage metrics, known blind spots, and data-quality remediation records.
- **Validate and limit:** Independently trace a selected reported asset or identity population from source system through collection timestamp, normalization/quality checks, dashboard use, owner, and documented omission. This cannot prove complete discovery, validate every sensor, or determine program coverage.
- **AI and trigger:** AI may compare supplied population counts and flag stale feeds, missing owners, or unexplained variance. Human program owners decide data-source scope and treatment of gaps. Refresh after new/decommissioned sources, collection failure, material variance, and program review.

### 2. Prioritization, remediation, and exception package

- **Request and owner:** Security operations and risk owners provide documented prioritization inputs, finding-to-asset links, remediation tickets, due dates, dependency/constraint notes, exception requests, human approvals, and retest/closure evidence.
- **Validate and limit:** Sample one recorded risk-treatment path from source observation through prioritization basis, assigned owner, action, exception or decision, and current/retest status. This does not validate the score, establish enterprise prioritization accuracy, or authorize remediation closure.
- **AI and trigger:** AI may queue missing handoffs and identify overdue items but cannot set risk scores, approve exceptions, modify systems, or close actions. Refresh after a material finding, missed deadline, exception expiry, or failed retest.

### 3. Dashboard, reporting, and independent-assurance package

- **Request and owner:** Program reporting and security leadership provide dashboard definitions, metric lineage, reporting periods, source-to-report reconciliation records, reviewer samples, management decisions, supplier evidence where applicable, and improvement actions.
- **Validate and limit:** Trace a selected dashboard metric from report value through source population, transformation/assumption record, period, reviewer challenge, and accountable owner’s response. This assesses lineage for the sample; it cannot certify dashboard accuracy or submit authoritative reporting.
- **AI and trigger:** AI may draft lineage workpapers and flag undocumented transformations or stale reports. Humans approve metric definitions, management decisions, and external reporting. Refresh before each reporting cycle, after metric logic/source change, and during annual independent review.


## Failure branches and decisions

Retain original evidence and transformations so discrepancies can be reconstructed. Never trim, sample or cap evidence passed to an assessment scorer. Approved inspection selections must disclose their population and limits. Failed credentials, stale feeds and empty error outputs remain visible failures. Unexpected score improvements trigger population and version reconciliation before crediting mitigation. Missing downstream acknowledgement remains a delivery gap. Escalate overdue actions and expired exceptions to their owners. On interruption, preserve feed/job state, versions, timestamps and next safe action; verify actual liveness before restarting collection.

## Cadence and renewal

Use actual participation, source-feed, reporting and related directive requirements. Quarterly coordination and annual independent review are management rhythms, not a definition of continuous monitoring. Assign failure alerts and freshness checks to operators. Reopen affected lineage and metrics after source, sensor, schema, scoring, dashboard, provider or ownership changes.

## Completion and handoff

Deliver capability scope, source/population map, pipeline lineage, data-quality and freshness observations, scoring-version references, treatment/retest records, downstream receipts and unresolved gaps. Keep sensitive source records in authorized storage. Independent source and skeptical review and named human approval remain necessary before final conclusions; CDM visibility does not grant system authorization.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
