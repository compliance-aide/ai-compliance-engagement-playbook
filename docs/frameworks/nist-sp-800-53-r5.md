# NIST SP 800-53 Revision 5 — engagement guide

> Original operational guidance, not an official NIST publication or a claim of
> conformance. Review the current [NIST publication record](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
> before each engagement milestone.

## Engagement focus

Define an authorized system boundary and documented risk decisions. For every
applicable safeguard area, maintain an implementation narrative and supporting
governance, operational, and configuration evidence. Independently validate
whether the described practice works; record exceptions, remediation,
reassessment, and continuous-monitoring triggers.

## Roles

The system owner remains accountable for accuracy and operation. The assessor
sets and executes an independent evaluation approach. AI may organize authorized evidence,
check consistency, propose questions, and highlight unsupported assertions;
it cannot select risk acceptance, approve a system boundary, alter configuration, or reach the final conclusion.

## Annual rhythm

Reconfirm boundary and inherited services; refresh evidence; test representative
operation; challenge changes and exceptions; review supply-chain dependencies;
and revise the human-authorized assessment approach after material change.

## Tailored evidence plan

**Plan status:** Independently reviewed; see the [review receipt](../evidence-plan-reviews/nist-sp-800-53-r5.md).

**Source and rights snapshot.** Use the [NIST SP 800-53 Rev. 5 CSRC record](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), Release 5.2.0 issued 2025-08-27; use [SP 800-53A](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final), Release 5.2.0 issued 2025-08-27, only for human-authorized assessment-method context; and use [SP 800-53B](https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final) only where its authority applies. NIST records 5.2.0 as version-aligned for 53B without baseline changes. Check release/change status before every engagement cycle. This guide records original evidence planning, not copied controls, procedures, baselines, mappings, OSCAL data, a baseline selection, an authorization decision, or a conformance claim. The authorizing/system-risk authorities approve boundary and risk decisions.

### 1. Authorized boundary, inheritance, and implementation narrative

- **Request and owner:** System boundary and asset/data inventory, common/inherited-service record, authorization or organizational scope inputs, human-approved selection/tailoring rationale and any authorized overlay, implementation narratives, and applicability/risk decisions from system, common-control, and risk owners.
- **Validate and limit:** Trace a selected system component or inherited service to its owner, implementation statement, evidence pointer, approved boundary decision, and human selection/tailoring rationale. This can support a defensible assessment population; it cannot establish authorization, select a baseline, or establish complete applicability.
- **AI and trigger:** AI may reconcile statements and evidence references, flag conflicts, and preserve provenance. Humans approve scope, inheritance, applicability, and risk acceptance. Revisit after boundary, shared-service, supplier, or material architecture change.

### 2. Governance, operation, and technical-evidence package

- **Request and owner:** Policy/procedure records, responsible-role evidence, time-bounded operational records, approved configuration/log outputs, assessment methods/workpapers, and continuous-monitoring signals, from control and system owners.
- **Validate and limit:** Use the human-approved assessment method to inspect, trace, or reperform selected evidence and record population, period, limitations, and exceptions. This can support an assessment workpaper; it cannot let a scanner result alone establish implementation or effectiveness.
- **AI and trigger:** AI may organize approved evidence and raise unsupported assertions. It may not select assessment conclusions, alter configuration, or close findings. Recollect after material changes, monitoring signals, incidents, or scheduled reassessment.

### 3. Exception, remediation, and reassessment record

- **Request and owner:** Exception/risk decisions, remediation plan, milestones, evidence of completion, retest results, and continuous-monitoring or reassessment plan from accountable risk and system owners.
- **Validate and limit:** Trace a selected exception to a human authority, decision date, expiry, corrective action, and retest. This can support accountable follow-through; it cannot accept residual risk or replace an assessor's conclusion.
- **AI and trigger:** AI may flag overdue items and prepare a review packet. Humans approve exceptions, risk acceptance, closure, authorization, and external statements. Revisit at reassessment and after source, system, threat, or supplier change.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
