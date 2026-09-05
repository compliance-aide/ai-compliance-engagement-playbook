# APRA CPS 230 — operational-risk engagement guide

> Original operational guidance, not APRA text, legal advice, a prudential
> conclusion or authorization to make a regulatory submission.

## Source and applicability

[APRA CPS 230](https://www.apra.gov.au/standards/cps-230), checked 2026-09-04,
identifies the current standard as in force from 1 July 2026. Confirm regulated
entity/group/branch scope and any written adjustments with regulatory counsel.
Do not reuse an earlier transition plan without checking this version. The
standard addresses operational risk, continuity of critical operations and
service-provider risk; cybersecurity evidence alone does not cover its scope.

Rights: original instructions and links only; no APRA standard, contract clauses
or customer evidence reproduced. See the
[author review](../refresh-reviews/australia-apra-cps-230.md). Independent source,
engagement, skeptical and publication reviews remain pending.

## Engagement focus

Create an operation-to-dependency-to-exercise record that shows which customer
services were tested, under what conditions and with what observed result.
Maintain unresolved weaknesses and the decisions required to address them.
A provider contract or recovery plan alone does not demonstrate resilience.

## Roles

Board and accountable management retain oversight and criticality/tolerance
approvals. Operations and continuity owners maintain service facts and plans;
provider owners maintain arrangements; counsel controls prudential interpretation
and notification decisions. Internal audit retains its independent role. AI may
reconcile records and draft workpapers; it cannot set tolerances, accept risk,
approve a provider arrangement or submit a report.

## Before starting

Obtain entity scope, current obligations, operation/provider registers,
management-approved tolerances, dependency maps, continuity plans, exercise
schedule, reporting contacts and evidence permissions. Ask owners to resolve
missing criticality or tolerance decisions before drawing resilience conclusions.
Follow the [agent runbook](../agent-runbook.md).

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Reconcile operation scope | Operations and risk owners compare service inventory with the approved critical-operation register. | Each inclusion/exclusion has a decision and owner; unexplained omissions remain open. |
| 2. Trace dependencies and tolerances | Owners connect each operation to people, systems, providers and fallback resources; management confirms tolerances. | Versioned dependency map and approved tolerance references, including units and measurement method. |
| 3. Review provider arrangements | Provider owners trace material arrangements to diligence, monitoring, change and exit evidence; counsel resolves any claimed exception. | Arrangement ledger with missing evidence and decision references. Standard terms do not automatically waive duties. |
| 4. Design the exercise | Continuity owners and reviewers define scenarios, observation points, expected tolerances, safe environment and stop rules. | Approved plan identifies what will and will not be demonstrated. |
| 5. Observe the exercise or disruption | Authorized operators execute; AI preserves timestamps, degraded service, data-loss observations, dependencies and errors. | Results compare like units and the same operation with its approved tolerances. Simulation assumptions remain explicit. |
| 6. Escalate and correct | Incident/legal owners evaluate reporting; management assigns corrections; independent reviewer checks retest evidence. | Decision trail and finding-to-retest chain; unresolved weakness remains in the risk record. |
| 7. Renew oversight | Risk owner assembles management/internal-audit inputs and updates affected operation/provider records. | Readable review packet, open actions, next exercises and authorized filing status. |

This is original engagement coordination; use the governing standard and approved
plan for actual obligations and decisions.

## Evidence and test plan

| Request and custodian | Check | Expected observation | Failure or limit |
| --- | --- | --- | --- |
| Operation/tolerance register from operations and risk | Trace a selected operation to customer impact rationale, decision and dependencies. | Scope and approved expectations are consistent. | An arbitrary recovery target is not a management tolerance. |
| Provider/fallback records from procurement and continuity | Follow one dependency failure into the approved alternative and its demonstrated capacity. | Plan and observed resources reconcile. | A contractual promise does not prove usable fallback capacity. |
| Exercise evidence from continuity | Compare actual timing, data and service observations with predeclared criteria. | Results and limitations are reproducible. | A tabletop discussion cannot prove live recovery timing. |
| Findings and oversight records from risk/internal audit | Trace adverse results through ownership, remediation, retest and reporting decision. | Closure has observed support and retained history. | A closed ticket does not establish resilience. |

## Failure branches and decisions

If a provider is absent from the operation map, open a scope gap before concluding
coverage. If a scenario exceeds a tolerance, preserve the adverse result and
escalate; do not adjust the tolerance to fit the result. A proposed 2026 provider
exception requires counsel's conditions-based decision. Coordinate overlapping
CPS 234 incidents without assuming one submission satisfies every obligation.
Unknown recovery behavior is `inconclusive`, not a successful exercise.

## Cadence and renewal

The cited standard includes an annual continuity exercise and annual material
provider register submission, with annual plan updating as necessary. Its incident
and out-of-tolerance disruption routes have different triggers and outer limits
(72 hours and 24 hours respectively), with prompt reporting required. Counsel
must record the exact trigger, applicable exception/overlap and clock owner;
AI escalates immediately rather than waiting out an outer limit. Quarterly
working reviews are a planning default, not a replacement for these duties.

## Completion and handoff

Deliver approved scope/tolerances, dependency and provider registers, exercise
plan/results, reporting decisions, findings/retests and the next oversight queue.
Identify untested operations and unsupported fallback assumptions. Filing status
requires an authorized submission and independently retrieved receipt.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md).
