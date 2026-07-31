# NIST SP 800-37 Revision 2 — engagement guide

> Original operational guidance, not an authorization or risk-acceptance
> decision. Review the [NIST RMF publication](https://csrc.nist.gov/pubs/sp/800/37/r2/final)
> and current organizational policy before each engagement.

## Engagement focus

Connect organizational risk decisions to system work, independent evaluation,
and ongoing monitoring. Maintain an explicit evidence story for each important
risk objective: claimed approach, implemented capability, operating evidence,
known limitations, and a human decision record.

## Roles and annual rhythm

System teams own truthful evidence and corrective work. Independent reviewers
challenge scope and evidence limitations without owning implementation. AI may keep
an authorized evidence ledger, detect contradictions, draft questions, and escalate
uncertainty; it cannot determine scope, authorize a system, accept risk, or issue an authorization decision.
Refresh the plan for changes, incidents, control failures, and business impact.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [NIST SP 800-37 Rev. 2 publication record](https://csrc.nist.gov/pubs/sp/800/37/r2/final) and the organization’s approved risk-management policy at engagement start; checked 2026-07-31. This is original operational guidance, not reproduced NIST text, an authorization decision, or a substitute for an agency method.

### 1. System-context and risk-framing package

- **Request and owner:** The system owner and risk executive provide the approved system purpose, boundary and dependency inventory, stakeholder roles, mission/business context, applicable overlays, risk assumptions, and dated decisions that frame the work.
- **Validate and limit:** Independently trace a selected significant dependency and risk assumption to an accountable owner, current boundary record, source date, and stated impact. This is a bounded trace; it cannot determine applicability, complete the inventory, or approve the risk frame.
- **AI and trigger:** AI may index supplied records and flag missing owners, conflicting versions, or stale assumptions. Designated humans approve scope and risk framing. Refresh after a mission, boundary, supplier, or material-risk change.

### 2. Implementation, assessment, and remediation package

- **Request and owner:** Control and system operators provide implementation narratives, configuration or process evidence references, assessment plans/results, test limitations, findings, corrective-action records, and retest status.
- **Validate and limit:** Sample one claimed capability from approved implementation record through source evidence, test result, limitation, finding (if any), owner, and retest or open status. A sample does not establish operating effectiveness across the system or close a finding.
- **AI and trigger:** AI may assemble traceability workpapers and identify unlinked evidence or overdue actions; it cannot test production systems without authority, alter evidence, determine sufficiency, or close corrective actions. Refresh after material implementation change, failed test, or assessment cycle.

### 3. Authorization, monitoring, and decision-record package

- **Request and owner:** The authorization boundary’s designated human authorities provide decision records, monitoring outputs, incident/change records, accepted exceptions, planned reassessment dates, and evidence of who approved each decision.
- **Validate and limit:** Trace a selected change, incident, or open risk from detection through routing, accountable decision, conditions, and next review. This can show a decision trail; it cannot accept risk, issue an authorization, or attest that monitoring is complete.
- **AI and trigger:** AI may flag missing decision fields and prepare read-only review packets. Only named human authorities authorize systems, accept risk, and make external representations. Refresh on monitoring cadence and before a decision, major change, or renewal.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
