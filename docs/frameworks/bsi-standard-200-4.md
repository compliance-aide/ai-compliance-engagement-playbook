# BSI Standard 200-4 — business-continuity engagement guide

> Original operational guidance, not BSI standard text or continuity assurance.

## Source and applicability

Use the [BSI 200-4 publication](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_4.pdf?__blob=publicationFile&v=8).
Checked 2026-09-04: indexed official material identifies version 1.0, May 2023,
replacing 100-4, and distinguishes the final version from community drafts. Direct
PDF retrieval returned 403; full source/current-edition verification remains
pending. Do not treat older 100-4 training pages as verified 200-4 instructions.
See the [author record](../refresh-reviews/bsi-standard-200-4.md).

Pin the source and approved continuity scope before using detailed definitions,
process stages or maturity claims. This guide supplies an original coordination
workflow; it does not replace the standard or establish ISO certification.

## Engagement focus

Connect business disruption impacts to recovery priorities, dependencies, feasible
strategies, usable plans and observed exercises. Keep business recovery separate
from merely restoring a server. A desired recovery objective is a target until
relevant evidence demonstrates performance under stated conditions.

## Roles

Business owners approve priorities and impact assumptions. Continuity leadership
coordinates plans; technical, workforce, facility and supplier owners provide
capabilities and evidence. Management approves resources and residual risks.
Exercise directors control safety and activation; independent reviewers challenge
results. AI may reconcile permitted metadata and draft workpapers, but cannot
activate crisis response, make safety decisions, accept risk or declare recoverability.

## Before starting

Obtain approved scope, source, business/service inventory, impact inputs, dependency
and supplier records, recovery objectives, existing plans, contacts and exercise
authority. Record QA boundaries, abort conditions and evidence permissions. Use the
[agent runbook](../agent-runbook.md); real emergency communications require separate
authority and are never sent as an unmarked exercise.

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Establish scope and authority | Leadership defines covered services, continuity owners and intended method. | Dated scope and decision route; source uncertainty remains explicit. |
| 2. Analyse business impacts | Business owners document disruption effects over time and critical dependencies. | Reviewed impact assumptions and priority rationale, not AI-selected criticality. |
| 3. Compare needs and capability | Continuity/technical owners compare approved objectives with actual resource and supplier capability. | Gap register separates targets from demonstrated capability. |
| 4. Decide strategies and plans | Owners propose alternatives and dependencies; management approves resources and risk decisions. | Versioned plans with roles, prerequisites, activation authority and return-to-normal path. |
| 5. Design exercises | Exercise director approves scenario, scope, expected outcomes, observations and abort conditions. | Safe QA plan identifies simulated versus actually exercised elements. |
| 6. Observe execution | Authorised operators run approved exercises; AI records permitted observations and timestamps. | Actual outcomes, failed paths and untested assumptions retained. |
| 7. Correct and retest | Owners resolve findings through approved work; reviewer repeats affected scenarios. | Finding/change/retest trail with residual gaps. |
| 8. Review and renew | Leadership reviews capability, unresolved risks and changes; continuity updates the next queue. | Approved decisions and current plans, with prior versions preserved. |

## Evidence and test plan

| Evidence and custodian | Check | Expected observation | Failure or limit |
| --- | --- | --- | --- |
| Impact/dependency map, business | Trace service priority to disruption effects and required people, facilities, suppliers and technology. | Assumptions and owners are explicit. | A technical inventory alone cannot establish business priorities. |
| Capability/strategy record, continuity | Compare approved objectives with demonstrated resources and contractual dependencies. | Shortfalls have decisions and owners. | A supplier promise is not an exercised recovery result. |
| Exercise log, director/operators | Compare expected outcomes with timestamped observations and scenario limits. | Simulated and actual behavior are distinguishable. | A tabletop cannot prove a full live recovery time. |
| Correction/retest packet, reviewer | Trace failed outcome to changed plan/capability and repeated observation. | Retest addresses the original failure. | Editing the plan alone cannot establish recoverability. |

## Failure branches and decisions

Unknown dependencies remain gaps. Conflicting business priorities require leadership
decision before scheduling recovery tests. Unexpected operational effects trigger
the approved abort/safety route; preserve evidence. Actual disruption switches to
the authorised response process, not autonomous AI continuation of the exercise.
After interruption, verify exercise versus real-event state and existing actions
before resuming. Missing source prevents detailed standard-conformance claims.

## Cadence and renewal

Follow the approved exercise and readiness calendar. Annual management review and
quarterly contact/dependency housekeeping are planning defaults, not asserted BSI
frequencies. Reassess after exercises, disruptions, supplier/site changes, revised
objectives or source changes. Retest affected capabilities before reusing assurance.

## Completion and handoff

Deliver scope, impact and dependency records, objectives/capability gaps, approved
strategies/plans, exercise observations, corrections/retests and next queue. Name
untested scenarios and the source-access gap. Independent source, engagement and
skeptical review and named human publication approval remain pending. Original
prose and links only; no protected standard text or real crisis evidence reproduced.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md).
