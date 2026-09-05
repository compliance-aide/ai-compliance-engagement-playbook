# Canada ITSG-33 security-risk management engagement guide

> Original operational guidance, not Canadian government direction, a control catalogue, risk acceptance or an authorization decision.

## Source and applicability

Start with the [ITSG-33 overview](https://www.cyber.gc.ca/en/guidance/it-security-risk-management-lifecycle-approach-itsg-33), [departmental activities](https://www.cyber.gc.ca/en/guidance/annex-1-departmental-it-security-risk-management-activities-itsg-33) and [system activities](https://www.cyber.gc.ca/en/guidance/annex-2-information-system-security-risk-management-activities-itsg-33). Source check: 2026-09-04. The November 2012 lifecycle guidance distinguishes departmental risk management from work throughout a system's implementation, operation and disposal.

**Catalogue transition:** the [ITSP.10.033 foreword](https://www.cyber.gc.ca/en/guidance/cyber-security-privacy-risk-management/itsp10033/foreword-overview-introduction) explicitly supersedes ITSG-33 Annex 3A, effective March 31, 2026. It also identifies newer organizational and system lifecycle publications. Do not infer that every older annex or every existing authorization has the same replacement or transition status. Record the exact documents and versions mandated by the organization, obtain current transition direction, and preserve historical references when reviewing older evidence. This guide does not supply a control crosswalk or decide equivalence.

## Engagement focus

Connect organizational security needs and common services to each system's approved requirements, implementation evidence, assessment, authorization conditions and monitoring. Keep organizational decisions separate from system decisions, while recording their dependencies. A useful record explains why evidence applies to the current system and which decisions remain with people.

## Roles

Business and information owners provide service needs and approved context. Organizational security owners provide the applicable profiles, common-control arrangements and risk-management direction. System owners and engineers supply implementation and operation records. Assessors determine evidence sufficiency and findings within their authority. The delegated authorizing official makes the operational decision. AI maintains traceability, compares versions and drafts questions; it cannot choose acceptable risk, select final safeguards, issue authorization or close findings without the accountable review.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Identify whether the work concerns the organization, a named system or their interface. Record owner, lifecycle stage, system version, input locations, expected output and exit condition in a bounded work item. Obtain the approved business/security context, applicable source versions, profile, boundary, prior decisions and handling authorization. Missing inputs become named dependencies; do not invent them. Keep classified or otherwise restricted evidence out of unapproved environments and this public repository.

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Set organizational context | Business/security owners identify the governing direction, business needs, domain assumptions and common services. Coordinator records the applicable catalogue and any transition question. | Versioned context and decision-owner register. Unresolved source applicability blocks dependent conclusions. |
| 2. Establish system context | System and information owners reconcile service use, information assets, interfaces and dependencies with the actual boundary; obtain approved categorization. | Scope record linked to organizational assumptions. A system is not categorized by copying another service's label. |
| 3. Plan assurance | Security and assessment owners establish the required assessment approach, coverage and dependencies and integrate them into the project plan before implementation gates. | Approved plan identifying inputs, methods, evidence owners and decision points; retrospective evidence gaps remain visible. |
| 4. Confirm requirements and design | Authorized owners select and approve the system requirements and tailoring through their governing process. Engineers trace the design and common-service dependencies to those requirements. | Complete requirement register with rationale, responsibility and planned verification. AI proposals remain drafts. |
| 5. Examine implementation | System teams provide dated configuration and operation evidence. Assessors compare observed implementation with requirements and record findings, limitations and inherited assumptions. | Evidence-linked assessment workpapers covering the complete approved register. A design description alone does not demonstrate operation. |
| 6. Treat and retest | Assigned owners propose corrective actions and obtain applicable change authorization. Assessors verify implementation and retest affected requirements and dependencies. | Finding-to-change-to-retest record. A future fix, accepted risk or closed ticket is not automatically a passing assessment result. |
| 7. Prepare and record the decision | Coordinator reconciles assessment results, residual uncertainty and proposed conditions into the exact decision packet. The delegated official decides; authorized staff retain and read back the recorded decision. | Separate prepared, decided and recorded statuses, with scope, conditions and evidence of authority. No implied permission to deploy. |
| 8. Monitor both levels | System owners report changed conditions and safeguard observations; organizational owners evaluate common-service and policy implications across dependent systems. | Change-impact and decision queue, preserving which systems require further assessment. |
| 9. Retire safely | System/records owners provide the approved disposal or transition plan. Authorized implementers execute it; reviewer verifies retained records, transferred dependencies and disposal evidence. | Exit record identifying remaining obligations and owners. Turning off a system does not prove disposal of its data. |

## Evidence and test plan

Use the complete approved requirement register to define coverage. These original examples are working aids, not the official assessment procedure or control set. Keep the entire evidence corpus available; never trim evidence sent to a scorer.

| Package and owner | Verification task | Limitation |
| --- | --- | --- |
| Organization/system context — business and system owners | Trace a significant system dependency to the organizational service, current boundary, approved assumption and accountable owner. Reconcile discrepancies against the full inventory. | A selected trace does not prove the inventory complete; name untested paths and missing records. |
| Common safeguards — organizational security owner | Compare a claimed inherited safeguard with its service scope, covered period, evidence and the system's local obligations. | Organizational implementation cannot automatically establish correct local use or continuing coverage. |
| Requirements and assessment — assessor/engineer | Follow each requirement disposition to its approved version and workpaper; compare expected and actual observations for examined evidence. | A superseded identifier needs an approved applicability decision, not an invented mapping. |
| Corrective actions — implementer/reviewer | Trace a failed observation through assigned action, authorized change and retest; check effects on connected requirements. | Record what remains untested. Never replace adverse evidence with a plan or a generic success message. |
| Authorization and monitoring — system owner | Compare the actual decision with its recorded conditions, monitoring evidence, escalations and subsequent changes. | Administrative readback proves recording, not delegated authority or effective security by itself. |

Workpapers record source, collector, date, period, requirement, environment, expected/actual observation, evidence pointer, limitation, reviewer and follow-up. If testing uses a selected population, state its rationale and untested coverage. Intrusive tests and production changes need separately approved plans; use authorized QA exercises or retained records where appropriate.

## Failure branches and decisions

- **Wrong lifecycle level:** separate organizational and system records, link dependencies and route decisions to their actual owners. Do not let a system owner silently change organizational policy.
- **Old catalogue or missing transition instruction:** preserve the original evidence version and request the applicable direction. Do not relabel old results as current or assume universal grandfathering.
- **Missing common-service evidence:** mark inherited coverage unresolved and ask the service owner for the exact scope and period. Continue independent system work.
- **Conflicting evidence or failed test:** retain observations and limitations, assign follow-up and identify affected decision inputs. Unknown is not satisfied.
- **Changed boundary or expired condition:** notify the system and authorization owners, evaluate dependent requirements and request the required decision. Do not invent a grace period or automatically extend authorization.
- **Restricted evidence encountered:** stop processing it in the current environment and route handling to its authorized owner. Do not copy it into chat as proof of access.
- **Interrupted assessment or uncertain record write:** preserve the last completed step, versions and pending decisions. Read back the destination before retrying and redo only work invalidated by changed facts.

## Cadence and renewal

Use project lifecycle gates, actual authorization conditions and approved monitoring arrangements. The owner selects internal review reminders and records their rationale. Revisit assumptions after changes to mission, data, architecture, common services, threats or governing sources. Do not invent a universal annual authorization or review deadline.

## Completion and handoff

A preparation packet contains approved organizational/system context, source-version decisions, complete requirement dispositions, assessment evidence, open findings, corrective actions, retests, decision questions and monitoring owners. Mark every missing element. A recorded authorization is a separate milestone requiring actual authority and destination evidence. Handoff lists the next action, owner, due date, evidence location and dependency so another agent can resume without reconstructing a decision.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared applicability, authority, evidence, technical-test, exception, source-change and renewal requirements.
