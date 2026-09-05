# Canada ITSP.50.105 cloud assessment and authorization engagement guide

> Original operational guidance, not Canadian authorization guidance, an assessment opinion or permission to operate.

## Source and applicability

Use [ITSP.50.105](https://www.cyber.gc.ca/en/guidance/guidance-cloud-security-assessment-and-authorization-itsp50105) and the organization's current approved cloud profile and direction. Checked 2026-09-04. The guidance addresses public and private organizations and separates provider-control assessment, customer-control assessment, authorization and continuing monitoring. Assessment responsibility depends on the cloud service and deployment model. It recommends examining independent provider assurance where direct visibility is unavailable and directly assessing customer responsibilities.

Confirm the actual applicable profile/version before work. For GC profile transition questions see the [GC cloud profile guide](canada-gc-cloud-security-profile.md). This workflow does not grant equivalence between third-party assurance schemes or turn a provider assessment into authorization of the customer's service.

## Engagement focus

Produce a reviewable decision packet for a specific cloud service, tenant, region, deployment and period. Keep provider reliance and customer implementation separate, then connect them through an explicit responsibility register. Preserve limitations across every layer of a provider stack.

## Roles

Service and information owners approve scope and data context. Security and privacy owners supply applicable assessment requirements. Provider relationship owners obtain authorized reports and contractual records. Customer operators provide configuration and operating evidence. Assessors judge evidence and findings. The delegated authorizing official decides acceptable operation and conditions. AI maintains registers, reconciles coverage and drafts questions; it cannot issue an assessment opinion, accept risk, authorize service use or deploy production.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Create bounded work items with inputs, owner, output and exit condition. Require approved categorization/profile, exact service inventory, responsibility assignments, previous decisions and evidence-handling authorization. Mark missing inputs explicitly. Do not upload restricted provider reports, tenant secrets or customer evidence to this public repository. Continue independent preparation while dependent conclusions wait for missing records.

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Fix the boundary | Service owner and architect reconcile the actual offering, tenant, region, data paths, interfaces and underlying provider services with the intended assessment. | Approved boundary and discrepancy list; preview or newly added services are explicitly identified. |
| 2. Allocate assessment work | Assessment lead works through the entire approved profile, assigning provider, customer and shared components, assessment methods and evidence owners. | Complete coverage register. Split shared tasks into concrete obligations; no unowned “shared” rows. |
| 3. Review provider reliance | Provider owner supplies permitted assurance records. Assessor checks offering, period, exclusions, underlying providers, exceptions and customer obligations against the intended reliance. | Provider assessment workpaper with unresolved gaps; an assurance badge alone is insufficient. |
| 4. Assess the customer service | Operators supply dated configuration and operation evidence. Assessor compares actual behavior against allocated requirements, including customer obligations in provider reports. | Customer workpapers with expected/actual observations and untested coverage. A provider result cannot close a missing customer control. |
| 5. Correct and retest | Assigned owners plan remediation and obtain separate change approval. Assessor verifies the implemented change and rechecks affected dependencies. | Finding/action/retest chain; adverse observations remain retained and future plans do not count as effective implementation. |
| 6. Prepare authorization | Coordinator combines reviewed provider reliance, customer results, unresolved risks, proposed conditions and monitoring arrangements in a versioned packet. | Exact decision draft for the delegated official, preserving disagreements and limitations. |
| 7. Verify the decision | Authorized owner records the actual decision; coordinator reads back scope, conditions, dates and version from the permitted destination. | Separate prepared, decided and recorded states. Operational deployment still follows its own release approval. |
| 8. Maintain authorization inputs | Service owner tracks changes, incidents, provider reports and decision conditions; assessor identifies affected requirements and needed reassessment. | Owned monitoring and decision queue; no automatic renewal from an unchanged dashboard. |

## Evidence and test plan

The complete approved assessment plan governs coverage. These original examples do not replace its procedures. Preserve the full evidence corpus; do not trim evidence supplied to a scorer.

| Package and owner | Verification | Limitation |
| --- | --- | --- |
| Boundary/responsibility — architect | Trace an interface through data path, underlying service and each party's assigned task; reconcile discoveries against the full inventory. | A selected trace cannot prove the inventory exhaustive. |
| Provider evidence — assessor/provider owner | Compare the report's actual scope and period with the subscribed offering and inherited obligations, including stacked providers. | Evidence for another region, service or period cannot be silently reused; unavailable underlying assurance remains a gap. |
| Customer operation — assessor/operators | Compare observed settings and operating records with approved expected behavior for allocated requirements. | A QA template, policy or installed product does not prove production operation. |
| Findings/retests — action owner | Trace failed evidence to corrective change and actual verification, including affected interfaces. | Closed tickets and promised fixes are not retest results. |
| Conditions/monitoring — service owner | Follow a changed condition from detection through impact assessment, escalation and recorded decision. | Acknowledgment or administrative closure does not extend authorization. |

Record objective, source, collector, date, covered period, environment, evidence pointer, expected and observed result, limitation, reviewer and next action. State test populations and untested coverage. Technical exercises require an approved safe plan; use authorized QA or retained records and do not test provider infrastructure without permission.

## Failure branches and decisions

- **Wrong tenant or missing service:** isolate affected workpapers and correct scope before reusing conclusions.
- **Preview feature outside assurance scope:** request explicit scope evidence and an authority decision; do not inherit the platform's general status.
- **Restricted or missing provider report:** request permitted access or an assessor-approved alternative through the relationship owner. Never bypass restrictions or invent equivalence.
- **Failed customer control or provider exception:** retain the adverse result, affected requirement and decision impact; assign correction and retest.
- **Unowned shared task:** identify the concrete provider/customer actions and obtain responsibility acceptance before claiming coverage.
- **Expired condition or material incident:** escalate to the service/security and authorization owners. Do not invent grace periods or automatically renew authority.
- **Interrupted work or uncertain record write:** preserve last completed step and versions; read back the destination before retrying and retain any pending approval.

## Cadence and renewal

Use actual decision conditions, provider evidence periods, contracts and organizational requirements. The owner sets internal reminders with time for remediation. Reassess after changes to service, data, provider stack, region, architecture or threat assumptions. No universal annual authorization period is implied.

## Completion and handoff

A preparation packet includes approved scope/profile, complete responsibility and coverage registers, provider/customer workpapers, findings, retests, open risks, decision questions and monitoring owners. Mark missing items. A recorded authorization is a separate milestone requiring actual authority and destination evidence. Handoff gives each unresolved item's next action, owner, due date and evidence location.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared applicability, authority, evidence, technical-test, exception, source-change and renewal requirements.
