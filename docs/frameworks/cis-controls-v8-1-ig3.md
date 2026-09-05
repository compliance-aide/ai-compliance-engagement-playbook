# CIS Controls v8.1 Implementation Group 3 engagement guide

> Original operational guidance, not CIS Controls text, certification, a safeguard catalog, or authorization to test systems.

## Source and applicability

The official [CIS IG3 resource](https://www.cisecurity.org/controls/implementation-groups/ig3) identifies 23 additional safeguards, building on IG1 and IG2 to cover all 153 safeguards in v8.1. IG3 therefore does not mean examining only the final 23. CIS describes organizations with specialist security expertise and sensitive or consequential services, including risks from sophisticated attackers. These are group-selection inputs, not an assurance guarantee.

Pin the authorized v8.1 source, publication date and assessment methods. The accountable security and business owners confirm group selection and scope. Do not infer applicability from organization size alone, treat a Benchmark profile as an implementation group, or infer certification from a completed register. Detailed safeguard interpretation requires authorized source review; this original workflow does not replace it.

## Engagement focus

Connect complete safeguard coverage with critical-service dependencies, specialist validation and accountable decisions. Give the next agent a bounded work item and evidence trail, while reserving high-impact judgments for qualified owners.

## Roles

The executive sponsor approves objectives and resources. The security lead owns the combined register and specialist assignments. Service, architecture and provider owners supply system boundaries and operating evidence. Qualified testers own approved methods and observations. Risk authority decides exceptions; an independent reviewer challenges conclusions and unresolved disagreements. AI may reconcile authorized metadata and draft workpapers. It cannot accept risk, approve security design, authorize testing, modify production or issue final assurance claims.

## Before starting

Apply the [agent runbook](../agent-runbook.md). Record the approved systems, tenants, environments, period, source version, data handling rules and decision owners. Collect prior IG1/IG2 records, critical-service inventories, business-impact and threat inputs, provider responsibilities, open incidents and exceptions. Missing inputs become named work items, not assumed facts. Reuse valid authorizations within their scope.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Confirm the boundary | Security, risk and service owners reconcile inventories with sensitive data, consequential functions and dependencies. | Approved scope, criticality rationale, owners and escalation contacts; unexplained population gaps remain open. Critical-service prioritization must not silently exclude other in-scope services. |
| 2. Build full coverage | Security lead reconciles all 153 entries against the authorized source, carrying forward foundational evidence and recording its currency. | Combined register with applicability decisions or open questions, service links, owners and evidence requirements. Prior IG1/IG2 completion is not automatic present-day verification. |
| 3. Plan specialist work | Qualified specialists choose methods based on source requirements, risk and system constraints. Link each planned activity to the register. | Work items with prerequisites, target boundaries, expected observations, evidence destination and decision owner. Missing expertise is an assigned dependency, not an invitation for AI to improvise. |
| 4. Establish test authority | Test owner confirms permission, exact targets, allowed techniques, time window, provider consent where needed, stop conditions and recovery contacts. | Approved test plan. Evidence organization may proceed while approval is missing; active testing may not. Production changes need their separate authorized change path. |
| 5. Collect and validate | Evidence owners preserve records; authorized specialists conduct the planned activities and record actual conditions. | Source-linked observations with time, scope, integrity references and limits. Tool completion, exercise attendance or an installed feature alone does not establish effectiveness. |
| 6. Challenge results | Independent reviewer compares observations to criteria, coverage and contrary evidence. | Findings distinguish supported, failed, unassessed and unresolved applicability states. Record disagreements and adjudication owner without replacing original observations. |
| 7. Treat and retest | Service and provider owners implement authorized remediation; risk authority decides time-bounded exceptions. Reviewer checks retest evidence. | Each issue has scope, impact, owner and next action. Closure requires an observed result or an explicitly distinguished risk decision, not a ticket status alone. |
| 8. Handoff and sustain | Security lead assembles the evidence index, register, decisions and schedule for authorized approval. | Durable review packet with residual gaps, owners and renewal triggers. No claim of protection against every attack follows from this packet. |

## Evidence and test plan

Maintain three linked packages:

- **Critical-service, threat and escalation boundary:** inventories, business-impact inputs, threat context, dependencies, supplier responsibilities and escalation thresholds. Trace each critical service to its owner and approved rationale. Check the full declared population for missing relationships before inspecting individual traces.
- **Operational assurance:** protected references to privileged-operation reviews, technical validation, detection/response observations, change and recovery exercises, and relevant provider evidence. Tie each to its service, period, custodian, method and limitations. For an authorized detection exercise, preserve the planned signal, observed telemetry, alert handling and resulting action; a generated alert alone does not establish an effective response. Use specialist-approved criteria rather than treating this example as a universal test.
- **Executive exceptions and independent challenge:** decision authority, mitigation and contingency records, expiry, supplier escalations, reviewer objections and retest results. Trace an exception through its affected scope and dependencies; record who can decide unresolved disagreement and when that decision is needed.

Preserve full evidence coverage and every collection gap. An approved inspection selection must identify its population, rationale and limits; it cannot support claims about unexamined systems. Never trim, sample or cap evidence sent to an assessment scorer. Keep confidential raw evidence in authorized storage and reference it from workpapers; do not publish credentials, exploit artifacts or customer records in this repository.

## Failure branches and decisions

If permission or target identity is uncertain, stop the affected test and resolve it with the authority owner. If service degradation or a test stop condition occurs, the tester stops and follows the approved recovery/escalation plan. If a tool fails, retain its exact error and affected coverage; no result means unassessed, not passed. If provider evidence is unavailable, retain the responsibility gap. If a foundational safeguard fails, keep it open alongside specialist findings. Escalate expired exceptions without extending them automatically. On interruption, preserve versions, completed observations, outstanding approvals and the next safe action.

## Cadence and renewal

Apply the actual safeguard frequencies and contractual or operational commitments in the pinned source and approved plan. Quarterly coordination and annual independent readiness review are management choices, not replacements for those frequencies. Reopen affected work after material threat, incident, architecture, supplier, regulatory, service or business changes. Assign evidence refresh, retest and exception-expiry responsibilities explicitly.

## Completion and handoff

Deliver the source and scope record, combined register, dependency map, approved methods and permissions, evidence index, findings and disagreements, remediation/retest records, exceptions and next review dates. Report tested conditions and blind spots together. Independent review and named human approval govern final conclusions and external claims; AI-drafted summaries retain their draft status until then.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared applicability, authority, evidence, technical-test, exception, source-change and renewal requirements.
