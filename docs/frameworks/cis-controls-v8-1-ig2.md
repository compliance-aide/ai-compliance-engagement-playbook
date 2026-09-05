# CIS Controls v8.1 Implementation Group 2 engagement guide

> Original operational guidance, not CIS Controls text, a certification, or an implementation verdict. Use authorized CIS material for safeguard details.

## Source and applicability

The official [CIS IG2 resource](https://www.cisecurity.org/controls/implementation-groups/ig2) identifies 74 additional safeguards built on IG1's 56: the combined scope is 130, not the additional 74 alone. CIS describes IG2 in terms of greater operational complexity and dedicated technology responsibilities. These characteristics inform an accountable owner's group-selection decision; headcount or an AI classification alone does not decide suitability. Pin v8.1 and the authorized source edition before building the engagement register. Do not confuse an implementation group with a CIS Benchmark configuration profile or certification.

The steps below are an original engagement method. Detailed safeguard wording, applicability and assessment methods must be checked against authorized current material; this guide is not a substitute or a reproduced safeguard catalog.

## Engagement focus

Build one traceable record across departments, platforms and service providers. Carry the IG1 foundation into the IG2 plan, identify the additional work, and verify both implementation and operation without hiding unresolved coverage behind a percentage.

## Roles

The security lead proposes scope and sequencing; the business sponsor approves group selection and resources. Service and technology owners implement authorized work and supply evidence. Procurement and provider managers obtain responsibility and service records. The risk owner decides exceptions. An independent reviewer challenges coverage and conclusions. AI organizes authorized records, drafts work items and flags contradictions; it does not accept risk, approve design, certify implementation or authorize scans and production changes.

## Before starting

Use the [agent runbook](../agent-runbook.md). Record the authorized services, business units, environments, assessment period, source version, evidence location and decision owners. Obtain the existing IG1 register, current asset and service inventories, provider agreements and responsibility records, prior findings and available operating evidence. Identify missing inputs explicitly. Reuse valid existing authorization; ask only when the next action exceeds it.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Establish boundaries | Security and service owners reconcile inventories, data sensitivity, departments, hosting boundaries and supplier dependencies. Sponsor confirms group choice. | Scope record with source dates, included populations, unresolved discovery gaps and approved rationale. Gaps remain visible; do not infer absence from an empty export. |
| 2. Build the combined register | Security lead checks all IG1 and IG2 entries against the authorized v8.1 source. AI may reconcile identifiers without publishing protected text. | Every source entry has an applicability decision or an open question, service links, owner and evidence need. An exclusion requires recorded rationale and decision authority. |
| 3. Resolve dependencies | Architecture, service and provider owners identify prerequisites, shared platforms and customer/provider responsibilities. Prioritize foundation defects alongside additional IG2 work. | Ordered work items with named accountable owners. A provider contract or product purchase alone is not implementation evidence. |
| 4. Establish present state | Evidence owners supply dated configuration, activity and review records. Reviewer compares each record with its declared population and period. | Separate implemented, failed, unassessed and applicability-pending findings under the engagement's defined criteria. Unsupported assertions remain unverified. |
| 5. Implement approved changes | Technology owners execute authorized work through change control, checking prerequisites and rollback arrangements. AI prepares bounded tasks within its authority. | Implementation receipt, affected scope and observed result. Test in an authorized QA environment before wider rollout; failed acceptance stops expansion. |
| 6. Check operation | Qualified reviewers use approved methods to trace service behavior, recurring activities and provider/customer handoffs to evidence. | Coverage record identifies what was examined, unavailable evidence, failures and limits. A configured feature does not by itself demonstrate continued operation. |
| 7. Remediate and decide | Owners correct failures; risk authority reviews exceptions and dependencies. Independent reviewer verifies retest evidence before closure. | Each open item has impact, owner, next action and due date; each closed item has supporting retest or an explicitly distinguished decision record. |
| 8. Hand off | Security lead assembles the register, evidence index, decisions and maintenance schedule for independent review. | Signed decision record and durable handoff with remaining gaps. A completed work packet is not a claim that all safeguards are effective. |

## Evidence and test plan

Maintain three connected packages:

- **Environment and dependencies:** service inventory, data and hosting boundaries, owners, provider responsibilities and approved priority rationale. Reconcile the full declared population before tracing individual services; identify stale or unowned relationships. Record differences between departments instead of assuming a shared platform produces identical coverage.
- **Operating practices:** authorized access-review records, monitoring and validation metadata, changes, incident follow-up, recovery exercise results and provider oversight. Tie each to its source, period, service and register entry. For example, follow an approved access removal through the request, execution and resulting account state; a closed ticket without the resulting state leaves verification open. Select methods from the applicable authorized source and engagement plan, not from this example alone.
- **Remediation and decisions:** issue scope, dependency impact, action owner, decision authority, exception expiry and retest. Follow a cross-owner failure through all affected responsibilities; one team's closure does not close another team's unresolved action.

Preserve the full evidence corpus and distinguish coverage from inspection depth. Never trim, sample or cap evidence passed to an assessment scorer. Any approved inspection selection must state its population, rationale and limits; it cannot support an unexamined-population claim. Keep confidential source evidence in the authorized system, with references here only.

## Failure branches and decisions

Missing IG1 evidence: reopen the foundation entry; do not assume a prior IG1 label establishes current operation. Missing provider evidence: record the affected responsibility as unverified and assign follow-up. Conflicting records: preserve both and seek resolution from their owners. Tool failure: retain the exact error and affected coverage; a failed collection is not a successful test. Overdue remediation or expired exception: escalate to the named risk owner without silently extending it. On interruption, save the source version, completed work, unresolved questions and next safe action before resuming.

## Cadence and renewal

Use the actual safeguard frequencies and approved operational obligations from the pinned source. Quarterly evidence coordination and annual group-fit review may be useful management rhythms; they do not replace more frequent requirements. Reopen affected entries after material service, asset, provider, business, threat, incident or regulatory changes. Assign recurring activities and exception expiry checks to named owners.

## Completion and handoff

Provide scope and version records, combined coverage register, dependency map, evidence references, methods and limitations, findings, remediation and exception decisions, retest results and the next review schedule. Independent reviewers confirm whether conclusions are supported. Keep unresolved source, rights and coverage questions explicit. Only the authorized human may approve final conclusions or external claims.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared authority, evidence, technical-test, exception, source-change and renewal requirements.
