# Canada DND IT security-risk management engagement guide

> Original operational guidance, not Department of National Defence direction, risk acceptance or authorization to operate.

## Source and applicability

Use [DAOD 6003-2](https://www.canada.ca/en/department-national-defence/corporate/policies-standards/defence-administrative-orders-directives/6000-series/6003/6003-2-information-technology-security-risk-management.html), current departmental instructions and the engagement's delegated authorities. Checked 2026-09-04; the public page identifies issue date 2014-01-14 and page details 2024-12-16. Do not confuse those dates with a newly issued directive. Obtain current internal instructions through the approved departmental route; this public source cannot establish their contents.

The directive applies to DND employees and CAF members. Its lifecycle approach uses assessment and authorization, aligned with ITSG-33. Operational authority (OA), security authority (SA) and technical authority (TA) have distinct responsibilities. DIM Secur acts as departmental SA; the OA makes risk decisions within delegation, supported by security advice and technical implementation. The directive requires continuing monitoring and risk-decision reporting to DIM Secur. Confirm current role assignments rather than inferring delegation from a job title. Contractor obligations require their own contract and authority record.

## Engagement focus

Keep the mission, system boundary, approved control profile, implementation, assessment observations and authorization conditions connected as the system changes. Produce a decision packet that lets an authorized official see what is known, what is uncertain and what changed. A completed assessment is not permission to operate.

## Roles

Record the named OA, SA, TA, project or service manager, evidence owners and reviewer with the source and limit of each delegation. The engagement coordinator maintains the work queue and dependencies. The reviewer challenges evidence and records unresolved disagreement. AI prepares read-only inventories, traceability records and draft questions; accountable people select requirements, judge risk and approve operational use. AI must not process classified content in this workflow or move restricted evidence into an unapproved environment.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Open a bounded work item with the mission/system name, owner, input links, expected output and exit condition. Confirm authorized evidence handling, correct system version and the lifecycle decision being supported. Obtain the mission description, boundary, approved profile, prior risk/authorization records, current departmental instructions and owner roster. Mark unavailable inputs explicitly and continue only work independent of them. Do not create a substitute departmental profile from public web searches.

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Establish the decision | Coordinator and delegated authorities identify the lifecycle gate, system version, mission use, required decision and decision owner. Verify authority evidence and information-handling constraints. | Scope/authority record; missing delegation blocks the decision, not unrelated document organization. |
| 2. Reconcile the boundary | System owners compare the approved asset/dependency map with current architecture and mission use. Record additions, removals, interfaces and inherited services. | Versioned boundary with discrepancy owners; no asset disappears because its evidence is difficult to retrieve. |
| 3. Confirm requirements | SA and relevant authorities provide the approved profile and tailoring decisions through departmental processes. Coordinator links each requirement to its rationale, implementation owner and assessment method. | Complete requirement register reconciled to the approved profile. Unapproved tailoring remains a proposal. |
| 4. Establish implementation | TA and system teams supply original implementation descriptions and dated operating evidence for the agreed period. Reviewer checks scope, provenance and consistency against the register. | Evidence-linked workpapers with expected and observed results. A policy or planned design alone does not show operation. |
| 5. Assess and treat gaps | Authorized assessors record findings and limitations. Assigned owners propose corrective work with dependencies and dates; changes follow separately approved implementation procedures. | Risk/action register retaining adverse evidence, treatment proposal and retest requirement. No silent replacement of failed results. |
| 6. Prepare the risk decision | Coordinator links findings, residual uncertainty, mission consequences, options and proposed conditions in one versioned packet. Authorities verify recommendations and the decision's scope. | Exact draft presented to the appropriately delegated official. AI cannot select an acceptable mission risk. |
| 7. Record and verify | Authorized owner records the actual decision, conditions and scope, and follows required reporting/registry procedures. Coordinator reads back the permitted destination record. | Decision and registry evidence are linked; a draft or attempted write is not a recorded authorization. |
| 8. Monitor and reopen | Assigned owners track control observations, incidents, changes and decision conditions. Route changed risk to the relevant authorities and reassess affected requirements and dependencies. | Change-to-decision trail and next review date. An old authorization is not extended by this workflow. |

## Evidence and test plan

The assessment lead determines coverage and safe methods under the actual profile. These original workpaper examples do not replace departmental assessment procedures or establish their required depth. Preserve the complete evidence corpus; do not trim evidence supplied to a scorer.

| Package and owner | Verification task | Limitation to record |
| --- | --- | --- |
| Mission, assets and authority — sponsor/system owner | Trace a material dependency from mission use through the current boundary, handling record and accountable authority. Reconcile discrepancies across the full inventory. | A selected trace checks that path; document untested paths and incomplete inventories. It does not establish classification or delegation. |
| Profile and implementation — SA/TA | Link every approved requirement to implementation responsibility, evidence location and assessment disposition; distinguish inherited services from local settings. | Provider claims or a different system's assessment cannot automatically support this implementation. |
| Safeguard operation — system teams | Compare dated observations with the approved expected behavior. Trace a failed observation to its finding and corrective action. Use retained evidence or an explicitly authorized QA test. | Record environment, period, test scope and unavailable telemetry. No live intrusive test or production change is authorized here. |
| Treatment and retest — action owner/reviewer | Compare proposed fix, approved change, actual implementation and retest result; reopen when the fix affects another requirement. | A closed ticket, accepted risk or future implementation date is not proof of effective remediation. |
| Decision and ongoing review — coordinator/authorities | Trace a condition from its signed decision to monitoring evidence, any breach, escalation and subsequent decision. Check the registry record against the approved version. | Registry entry verifies recording, not authority validity or operational effectiveness; those require separate evidence. |

Each workpaper records the requirement reference, source system, collector, date, covered period, evidence pointer, expected/actual observation, missing coverage, reviewer and next action. Keep sensitive artifacts in their approved repository and only permitted metadata in coordination records.

## Failure branches and decisions

- **Wrong system or stale boundary:** isolate affected workpapers, identify the current version and reassess the changed dependencies before reusing conclusions.
- **Missing internal instruction or delegation:** ask the designated departmental owner for that specific record. Leave the dependent profile or authorization unresolved; do not infer authority from seniority.
- **Restricted evidence encountered:** stop processing it in the current environment, retain only permitted metadata and route the access question to its security owner. Do not copy it into chat or this repository.
- **Conflicting evidence or failed safeguard:** retain both observations and notify the assigned security/technical owners. Record the impact on the decision packet and required retest.
- **Condition expired or risk changed:** flag the affected authorization record and escalate to the named authority. Do not invent a grace period, renew approval or direct operational shutdown without authority.
- **Urgent mission request:** preserve the urgency and decision question for the delegated official. Urgency does not give the AI authority to accept risk or skip recording obligations.
- **Interrupted collection or uncertain registry write:** save the last completed step, evidence versions and pending decision. Check the destination before retrying; restart only the work invalidated by changed facts.

## Cadence and renewal

Use lifecycle gates, the authority's recorded conditions and ongoing monitoring arrangements. The engagement owner sets internal evidence-review intervals and owners; do not invent a universal annual authorization expiry. Mission, information, threat or system changes trigger evaluation of affected work. Keep each review date distinct from any binding decision expiry.

## Completion and handoff

A preparation packet contains approved scope and authority records, current profile, complete requirement dispositions, evidence/workpapers, open risks, corrective actions, retests, decision questions and monitoring owners. Mark absent or disputed elements explicitly. A recorded decision is a separate milestone with its own authority, scope, conditions and destination evidence. Handoff lists the next action, owner, due date and unresolved dependency so another agent can resume without inventing a decision.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared applicability, authority, evidence, technical-test, exception, source-change and renewal requirements.
