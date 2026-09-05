# DoD Zero Trust Reference Architecture v2 — engagement guide

> Original operational guidance, not DoD content or a Department of Defense authorization decision. Confirm source status through the [DoD reference architecture](https://dodcio.defense.gov/Portals/0/Documents/Library/(U)ZT_RA_v2.0(U)_Sep22.pdf).

## Engagement focus

Maintain mission and system scope, data and access decisions, identity and device evidence, service dependencies, architecture roadmap, implementation records, exceptions, testing results, and accountable approvals.

## Roles

DoD and component authorities determine architecture, mission risk, and deployment decisions; independent reviewers assess evidence. AI organizes approved evidence and detects inconsistencies, but cannot grant access, change configurations, or authorize systems. Review quarterly and annually.

## Source and applicability

Use the linked reference architecture with the current [DoD CIO source library](https://dodcio.defense.gov/library/), strategy, capability/activity material and component direction. Record each document's own version; architecture, strategy and implementation guidance are different artifacts. A v2 architecture filename does not establish the version of every companion document. The official library also identifies implementation resources; check those before treating a historical roadmap as current authority.

Mission owners approve the desired outcomes, scope and target state. Keep capability and activity identifiers distinct and retain all applicable activities in the coverage register. Do not infer completion from product purchases, architecture diagrams, installed features or a generic zero-trust maturity score.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Identify mission services, users, non-human identities, devices, workloads, data and enforcement boundaries. Select approved QA access journeys and synthetic identities/data. Establish test authority, telemetry access, safety limits, rollback and mission-continuity owners. Do not execute disruptive policy changes in operational systems under a read-only assessment task.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Establish authority and scope | Mission and architecture owners approve source versions, priorities and system boundaries. | Dated target-state decision and complete scoped service inventory. |
| 2. Map access journeys | Identity, application, data and network owners trace request, policy decision, enforcement and telemetry. | End-to-end maps including service identities, alternate paths and missing observations. |
| 3. Reconcile capabilities | Program owners map applicable activities to outcomes, dependencies and responsible teams. | Full coverage register with supported reuse, gaps and justified deferrals; no vendor-feature substitution. |
| 4. Design measurable checks | Owners define expected access decisions, revocation behavior, signal freshness and failure handling. | Approved test criteria and observations needed at each boundary, including denied and degraded cases. |
| 5. Test implementation | Authorized reviewers execute QA journeys and compare independent telemetry with actual access. | Versioned evidence tying identity/device context, decision, enforcement and outcome together. |
| 6. Assess dependencies and failure | Reviewers examine missing signals, unavailable decision services and bypass routes. | Documented failure behavior and mission impact; success on the intended path does not cover alternate paths. |
| 7. Remediate and retest | Owners make authorized changes and reviewers repeat affected journeys. | Verified security behavior plus mission-function checks, residual issues and approved recovery decisions. |
| 8. Review and sustain | Independent reviewers challenge activity claims; mission authorities approve representations. | Evidence-backed outcome register, monitoring plan and next owners; authorization remains separate. |

## Failure branches and decisions

- **Policy logs deny while resource access succeeds:** trace enforcement and alternate paths; preserve the contradiction rather than accepting the policy log as the outcome.
- **Device posture is stale:** test the approved response to unavailable or expired signals; do not treat a last-known healthy state as current without a supported policy decision.
- **Revoked identity keeps an active session:** measure the actual session/token behavior against approved expectations and assign the enforcement gap.
- **Service account bypasses user controls:** create a separate non-human access journey with its own credentials, permissions and monitoring evidence.
- **Fail-closed behavior interrupts a mission:** route the measured tradeoff to the mission/risk authority; AI cannot choose availability over protection or approve a bypass.
- **Dashboard reports activity complete without evidence:** reopen the claim and request the specific outcome and test records; a deployment milestone alone is insufficient.

## Evidence and test plan

**Source and rights snapshot.** Use the official [DoD Zero Trust Reference Architecture v2](https://dodcio.defense.gov/Portals/0/Documents/Library/(U)ZT_RA_v2.0(U)_Sep22.pdf), current DoD/component mission and authorization direction, and authorized source access; prior snapshot 2026-07-31; verify current architecture and implementation direction. This original plan does not reproduce architecture content, select a target state, set a maturity result, authorize a system, approve access, or make a Department of Defense compliance claim. Authorized DoD/component officials decide architecture, mission scope, risk, funding, deployment, and representation.

### 1. Mission, architecture, and transformation-governance package

- **Request and owner:** Mission executives, enterprise architecture, security, identity, data, network, platform, privacy, and program owners provide mission/service priorities, approved transformation scope, architecture decisions, owner roster, dependency/investment records, planned milestones, assumptions, and governance minutes.
- **Validate and limit:** Trace one selected transformation objective to a named authority, mission/service rationale, approved decision record, dependency, and review date. This supports governed planning traceability; it cannot approve an architecture, establish a target state, or prove enterprise completeness.
- **AI and trigger:** AI may organize approved decisions and flag conflicting inventories, stale approvals, or unowned objectives. Humans approve scope, priorities, funding, architecture, and risk decisions. Refresh after material mission, identity, data, device, workload, network, supplier, or operating-model change.

### 2. Access journey, implementation, and telemetry package

- **Request and owner:** Identity, endpoint, application/workload, data, network, security-operations, and service owners provide original architecture/implementation narratives, approved inventory and configuration metadata, access-decision records, telemetry/monitoring metadata, test evidence, change/rollback artifacts, and documented limitations.
- **Validate and limit:** With a human-approved method, trace one selected service or access journey across identity, device/workload, data, network, and telemetry records, recording population boundary, period, owner, and exception. This can demonstrate bounded traceability; it cannot grant access, prove zero trust is achieved, or authorize configurations.
- **AI and trigger:** AI may correlate authorized metadata, identify missing links, and draft questions. Humans choose tests, interpret results, approve technical changes, and close corrective actions. Recollect after material access, device, workload, data-flow, telemetry, network, incident, or supplier change.

### 3. Exception, measurement, and authorization-support package

- **Request and owner:** Governance, risk, system, authorization-support, service, and program owners provide approved exceptions, compensating-measure evidence, measurement definitions/results, remediation portfolio, retest records, management reviews, source-change watch, and independent-review workpapers.
- **Validate and limit:** Trace one selected exception, metric, or gap from source evidence through accountable interpretation, named decision authority, action/expiry, and follow-up. This supports readiness and governance discussion; it cannot accept risk, make an authorization decision, issue a maturity rating, or replace independent review.
- **AI and trigger:** AI may flag expired exceptions, missing measurement inputs, and unresolved evidence conflicts and prepare non-authoritative workpapers. Humans approve risk treatment, authorization actions, external statements, and closure; independent reviewers challenge evidence without operating systems. Refresh after failed testing, metric changes, exception expiry, source update, or annual review.


## Cadence and renewal

Quarterly and annual reviews are planning conventions; current program and component milestones govern actual commitments. Reopen affected journeys after policy, identity, device, workload, data, network, telemetry or mission changes. Track signal freshness and operating failures between formal reviews. Preserve earlier configuration snapshots and test limits.

## Completion and handoff

Deliver source/authority decisions, mission scope, access-journey maps, full activity coverage, dependency decisions, test evidence and unresolved risks. State which outcomes were designed, implemented and actually verified. Name the next owner, action and required evidence without earlier chat. Do not claim target-level achievement or authorization from partial journeys or an aggregate dashboard.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
