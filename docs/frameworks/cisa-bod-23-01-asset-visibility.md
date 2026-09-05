# CISA BOD 23-01 asset-visibility engagement guide

> Original operational guidance, not Binding Operational Directive text, a scope determination, a federal compliance conclusion, or a compliance claim. Confirm current material through [CISA BOD 23-01](https://www.cisa.gov/news-events/directives/bod-23-01-improving-asset-visibility-and-vulnerability-detection-federal-networks) and applicable agency, component, system-owner, and authority direction.

## Engagement focus

For applicable Federal Civilian Executive Branch environments, maintain evidence that IP-addressable asset discovery and vulnerability detection are scoped, operated, measured, and improved with accountable ownership. Connect reportable asset populations to discovery coverage, vulnerability-enumeration evidence, data quality, performance measures, gaps, remediation handoffs, and reporting records. Preserve the directive’s applicable scope and exclusions; do not treat a scanner output, dashboard, or AI-generated inventory reconciliation as proof that every asset is in scope, reachable, identified, or compliant.

## Roles

Assign accountable agency or component executive, asset-management, vulnerability-management, network, cloud, security-operations, system-owner, data, reporting, and supplier-management roles. Operators maintain scope decisions, asset-discovery records, vulnerability-enumeration evidence, data-quality checks, measurement records, gaps, remediation handoffs, reporting artifacts, supplier evidence, and corrective-action status. Review material asset populations, discovery coverage, performance trends, and open gaps quarterly; reassess after material network, cloud, system, supplier, or scope changes. Before annual renewal, an independent reviewer samples records from asset scope through performance reporting; auditors test the evidence trail without determining directive applicability, directing scans, accepting risk, submitting agency reports, or attesting for management.

AI may organize supplied asset and vulnerability evidence, flag stale coverage or missing ownership, correlate documented asset populations with reporting records, and draft workpapers for human review. AI cannot scan or change systems without authorization, determine federal scope, submit reports, accept risk, make a compliance conclusion, attest for management, or replace independent review.

## Source and applicability

Verify the directive linked above, its implementation guidance and current agency instructions before setting scope, exclusions, measurement rules or deadlines. Direct official retrieval returned 403 during drafting. This workflow does not assert that its management cadence satisfies the directive. Record unresolved source questions and their authority owner; do not invent substitute thresholds. Discovery, vulnerability enumeration and remediation are separate activities, each requiring its own evidence.

## Before starting

Apply the [agent runbook](../agent-runbook.md). Obtain approved network/cloud boundaries, inventories, address allocations, discovery and enumeration configurations, collection histories, reporting definitions and decision contacts. Reuse valid authorization. Resolve active-test permissions and safe operating conditions before executing collection; organizing existing authorized exports may continue while those permissions are pending.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Pin requirements | Agency owner confirms source version, applicable systems, exclusions and actual required frequencies. | Requirement register with source citations and unresolved decisions. No source gap is silently converted into an exclusion. |
| 2. Reconcile populations | Asset/network/cloud owners compare inventories, address allocations and provider boundaries. | Full declared population and stable identity references; address reuse and ephemeral assets retain their time context. |
| 3. Map collection paths | Operators map each population to discovery and vulnerability-enumeration methods separately. | Owned coverage plan, access dependencies, authorized targets and expected evidence. Discovery success does not establish enumeration success. |
| 4. Collect and preserve | Authorized operators run approved methods and retain actual start/end times, configuration version, results and errors. | Original output and per-population execution state. A launched job is not a completed collection. |
| 5. Reconcile coverage | Data and security owners compare expected assets with observed, unreachable, stale, unsupported and failed records. | Explicit denominator and gap register. Authentication failure cannot be counted as a successful authenticated check. |
| 6. Route findings and gaps | Owners assign collection repairs separately from vulnerability remediation; preserve original observations and timestamps. | Linked work items with owner, current-source due date and retest criteria. A clean dashboard cannot close an unresolved feed failure. |
| 7. Verify repairs and metrics | Independent reviewer checks renewed collection, finding handoffs and calculations against source records. | Observed retest and reconciled report with limits. A corrected feed does not prove the underlying vulnerability is fixed. |
| 8. Handoff and report | Reporting owner prepares the approved packet; authorized officials handle submission. | Evidence index, remaining gaps, recurring owners and actual submission/readback receipts where available. |

## Evidence and test plan

**Source and rights snapshot.** Use the official [CISA BOD 23-01 page](https://www.cisa.gov/news-events/directives/bod-23-01-improving-asset-visibility-and-vulnerability-detection-federal-networks) and applicable agency/component direction at engagement start; prior locator snapshot 2026-07-31; detailed current-source review pending. This original plan does not reproduce directive text, determine reportable scope, direct scanning, or make a federal compliance conclusion.

### 1. Asset-population, scope, and data-lineage package

- **Request and owner:** Asset, network, cloud, system, and data owners provide approved asset-population definitions, inventory extracts, address/allocation records, source inventories, ownership links, inclusion/exclusion decisions, timestamps, and documented known gaps.
- **Validate and limit:** Independently trace a selected reported asset population from source inventory through collection date, normalization or reconciliation record, accountable owner, scope rationale, and current gap record. This cannot prove all assets are identified, determine directive scope, or validate every source feed.
- **AI and trigger:** AI may compare supplied population counts and flag stale sources, missing owners, or unexplained variances. Authorized humans decide scope and data-quality treatment. Refresh after material network, cloud, acquisition, decommissioning, source, or ownership change.

### 2. Discovery, vulnerability-detection, and gap-treatment package

- **Request and owner:** Vulnerability-management, security-operations, network, platform, and system owners provide authorized discovery/detection records, coverage measures, service/asset links, data-quality checks, gap logs, remediation handoffs, change references, and supplier evidence.
- **Validate and limit:** Sample one documented coverage gap or detection result from source record through asset linkage, accountable owner, analysis, treatment or remediation handoff, and current validation/status record. This does not authorize scans, establish complete coverage, or close a vulnerability.
- **AI and trigger:** AI may identify stale coverage records, orphaned gap owners, or missing validation references. Humans authorize technical activity, set treatment priority, and approve changes or closure. Refresh after collection failure, material coverage variance, new environment, failed validation, or threat change.

### 3. Measurement, reporting, and independent-challenge package

- **Request and owner:** Program/reporting, security leadership, and independent reviewers provide metric definitions, reporting-period source data, transformation/assumption records, reconciliation evidence, management decisions, reviewer samples, limitations, and corrective actions.
- **Validate and limit:** Trace a selected metric from reported value through source population, calculation/assumption record, period, reviewer challenge, accountable response, and follow-up action. This assesses lineage for one sample; it cannot certify metric accuracy, submit a federal report, or attest for management.
- **AI and trigger:** AI may draft lineage workpapers and flag undocumented transformations or stale reports. Authorized humans approve metrics, reports, risk decisions, and external statements. Refresh before each reporting cycle, after metric/source change, and during annual independent review.


## Failure branches and decisions

Preserve the full declared population and evidence corpus. Any approved inspection selection must state its scope and limits; never trim, sample or cap evidence passed to an assessment scorer. Duplicate identities require documented reconciliation rather than blind row deletion. Empty results with an error remain failed collection, not zero vulnerabilities. Unreachable or unsupported assets retain gap owners. Scope disputes route to agency authority. On interruption, save collection handles, versions, timestamps, completed populations and next safe action; verify actual process status before resuming or restarting.

## Cadence and renewal

Use verified directive and implementation-guidance frequencies, on-demand response obligations and agency reporting requirements. Quarterly coordination and annual independent review are management choices, not sufficient collection schedules. Track discovery, enumeration, feed freshness and reporting separately. Reopen affected coverage after network, cloud, provider, inventory-source or authentication changes.

## Completion and handoff

Deliver source decisions, population and collection maps, original outputs, errors, coverage calculations, gap/remediation handoffs, retests and reporting receipts. Report blind spots with the measured results. Independent source, skeptical and engagement reviews and named human approval remain necessary before final compliance conclusions.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
