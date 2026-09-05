# CIS Critical Security Controls v8.1 — engagement guide

> Original operational guidance, not CIS content or a conformance claim. Consult authorized CIS material for safeguard details and assessment criteria.

## Source and applicability

The [official v8.1 source](https://www.cisecurity.org/controls/v8-1) describes an update to v8, including asset-class and description changes and alignment with the NIST CSF 2.0 Govern function. Pin the version and inspect the authorized change log before carrying forward a v8 assessment. A matching identifier alone does not establish that the old evidence still answers the current requirement.

Use an accountable owner's approved Implementation Group (IG) selection, not an undefined risk tier. Follow the corresponding [IG1](cis-controls-v8-1-ig1.md), [IG2](cis-controls-v8-1-ig2.md) or [IG3](cis-controls-v8-1-ig3.md) workflow for group-specific execution. Groups are cumulative. Record any additional safeguards chosen for the organization's risks and obligations. CIS Controls alignment does not itself establish compliance with another framework, and a CIS Benchmark configuration profile is a different artifact.

## Engagement focus

Create an owned security improvement program: establish the population, choose and justify coverage, verify existing practice, implement approved improvements, observe operation, and maintain evidence through change. Separate design statements, implementation observations and operating results.

## Roles

The program sponsor approves group choice, scope and resources. Security leadership owns source interpretation and the coverage register. Service, asset, identity, configuration and provider owners supply evidence and implement authorized actions. Risk authority decides exceptions. Independent reviewers challenge evidence and closure. AI may reconcile authorized records and draft work items; it cannot attest, accept risk, authorize active tests or production changes, or issue final conclusions.

## Before starting

Apply the [agent runbook](../agent-runbook.md). Obtain the authorized v8.1 source and terms, approved boundary, inventories, prior version/register, existing evidence, open findings, provider responsibility records and decision contacts. Record missing inputs and their owners. Reuse valid authorization for read-only work; preserve sensitive evidence in its approved repository.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Establish scope | Program and service owners reconcile business services with asset, software, identity, data and provider inventories. | Boundary, period, source dates and owners; unexplained population differences are recorded for resolution. |
| 2. Approve priorities | Security lead proposes the Implementation Group and additional coverage from risk and business needs; sponsor decides. | Written rationale and source-pinned coverage. Budget constraints become explicit planning decisions, not silently dropped entries. |
| 3. Reconcile the register | Security lead checks the complete selected scope against authorized source material. For migration, compare the change log and affected definitions. | Every scoped entry has applicability state, owner, affected services, method and evidence need. Changed source assumptions reopen relevant evidence judgments. |
| 4. Establish present state | Owners provide dated configuration and operating evidence; reviewer checks identity, provenance, population and period. | Design, implementation and operation recorded separately, with failed, unassessed and unresolved entries visible. Policy approval alone does not prove operation. |
| 5. Plan and implement | Owners create dependency-ordered work items, including provider responsibilities, acceptance checks and rollback. Execute only authorized changes. | Change receipt with actual affected scope and result. Validate in authorized QA before wider rollout; a failed check stops expansion. |
| 6. Validate operation | Qualified reviewers apply approved source-appropriate methods and reconcile observations to the declared coverage. | Evidence-backed findings, contradictions and limitations. Tool output is an input to review, not automatic assurance. |
| 7. Treat findings | Owners remediate and retest; risk authority decides exceptions with scope, rationale and expiry. | Closure supported by retest or a separately labeled decision. Open dependencies remain assigned even when another team finishes. |
| 8. Review and renew | Independent reviewer challenges coverage and decisions; sponsor approves the program handoff. | Durable register, evidence index, unresolved gaps and named maintenance owners. Final external claims require authorized human approval. |

## Evidence and test plan

Maintain three connected packages:

- **Assets, software, accounts and configurations:** approved inventories, authoritative system references, owners, baseline versions and changes. Reconcile the full declared populations before tracing individual items. Follow an account or configuration change from request through execution to resulting state; an administrative ticket alone leaves verification incomplete.
- **Protective operations and response:** exposure/remediation records, event handling, protective-service observations, recovery results and approved response exercises. Trace detection through assignment, action and retest. Compare recovery claims with observed restoration and service validation; a successful backup job alone does not demonstrate recovery.
- **Governance and renewal:** group-selection rationale, risk decisions, exceptions, remediation dependencies, independent challenge and scope renewal. Link each exception to authority, affected services, expiry and review evidence. Record disagreement rather than averaging competing conclusions.

Use source and engagement-approved criteria for each test; these examples are not a complete CIS assessment method. Preserve full evidence supplied to an assessment scorer without trimming, sampling or capping. If reviewers use an approved inspection selection, state its population, rationale and limitations and do not extrapolate unsupported coverage. Track freshness across the complete evidence index rather than checking only convenient records.

## Failure branches and decisions

An inaccessible source blocks its detailed interpretation, not unrelated authorized inventory work. Missing owners or stale evidence remain open work items. Conflicting versions require source-owner resolution before reusing conclusions. Failed collection retains the exact error and affected population; no result is not a pass. Missing provider evidence remains a customer/provider responsibility gap. Escalate overdue actions and expired exceptions without silently renewing them. If work stops, save source versions, completed observations, unresolved decisions and the next safe action.

## Cadence and renewal

Use actual safeguard frequencies and applicable operational commitments from the pinned source. Monthly signal review, quarterly coordination and annual scope renewal are optional program rhythms, not universal CIS deadlines. Reopen affected work after material asset, identity, configuration, ownership, provider, threat or incident changes. Assign recurring checks and exception-expiry handling to named owners.

## Completion and handoff

Deliver scope and source records, group rationale, complete register, evidence references, methods and coverage limits, findings, changes, retests, exceptions and renewal dates. Report what was observed and what remains unverified. Independent review and named human approval are required before final conclusions or external claims; a complete task list does not prove complete implementation.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared applicability, authority, evidence, technical-test, exception, source-change and renewal requirements.
