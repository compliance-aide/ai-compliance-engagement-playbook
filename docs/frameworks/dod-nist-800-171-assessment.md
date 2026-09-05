# DoD NIST SP 800-171 assessment readiness — engagement guide

> Original operational guidance, not a DoD score or SPRS submission. Consult the [DoD safeguarding and assessment page](https://www.acq.osd.mil/asda/dpc/cp/cyber/safeguarding.html).

## Engagement focus

Confirm contract clauses and assessment need; maintain SSP, implementation evidence, POA&M governance, score history, supplier flow-down, scope, provenance, and timestamp records.

## Roles

Authorized humans approve scores and submissions; independent reviewers test evidence quality. AI builds read-only readiness ledgers, but cannot calculate or submit official scores. Reconcile quarterly and prepare annually.

## Source and applicability

Retrieve the applicable [DoD assessment methodology](https://www.acq.osd.mil/asda/dpc/cp/cyber/safeguarding.html), contract clauses and current SPRS instructions. The DoD source lists methodology version 1.2.1, June 24, 2020. Record the actual methodology, NIST revision, assessment type and contractual basis; do not substitute a newer NIST publication without resolving its applicability.

Keep this assessment separate from [CMMC](cmmc.md) and the broader [DFARS workflow](dfars-cybersecurity.md). A readiness review, government assessment, approved score and posted SPRS record are different states. The methodology uses deductions from 110 and can produce negative scores; do not convert a weighted result to a percentage of controls implemented. Obtain the complete methodology before preparing any score review.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Assign contracts, SSP/system, evidence, remediation, independent-review and authorized submission owners. Freeze the system boundary, SSP version, assessed period and organizational identifiers. Keep controlled information and detailed security evidence in authorized storage. Create one work item per requirement/system with evidence and decision provenance; AI maintains the readiness ledger rather than calculating an official score.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Confirm assessment need | Contracts verifies applicable clauses, relevant systems and required recency. | Award-linked assessment calendar with actual dates and unresolved interpretation questions. |
| 2. Reconcile SSP scope | System owners compare the SSP with deployed assets, information flows and service providers. | Approved boundary and SSP version; undocumented systems remain gaps rather than excluded by omission. |
| 3. Establish coverage | Assessment owner reconciles all applicable requirements with the selected methodology. | Complete requirement register, evaluation plan and ownership; no selective evidence subset presented as full coverage. |
| 4. Review implementation | Authorized reviewers inspect and test evidence against expected operation. | Requirement-level observations with source, date, scope and contradictions; policies alone do not prove implementation. |
| 5. Reconcile remediation | Owners connect each gap to actions, dependencies, milestones and retests. | Current implementation separated from planned work; POA&M entries do not count as completed controls. |
| 6. Prepare score review | Authorized assessment personnel apply the complete official methodology to reviewed determinations. | Traceable deductions and any special treatment, independently checked; AI does not approve or generate the official score. |
| 7. Prepare the external record | Authorized owner reconciles approved result, identifiers, SSP, assessment date and required fields. | Reviewable submission package with exact scope and authority; government and contractor assessment records remain distinct. |
| 8. Verify and maintain | After authorized submission, owner reads back the actual SPRS record and monitors changes. | Matching posted fields and receipt, or explicit unposted status; future updates have named owners. |

## Failure branches and decisions

- **SSP describes a different boundary:** reconcile systems and affected evidence before reusing a result; an organization-wide label cannot bridge the mismatch.
- **A requirement is only planned:** preserve the implementation gap and route methodology treatment to the authorized assessor; a target completion date is not evidence of completion.
- **Scoring workbook hides deductions:** require transparent requirement-level rationale and independent calculation review; a total without provenance is insufficient.
- **Record date is refreshed without assessment:** preserve the original assessment date and require evidence for any new assessment claim.
- **SPRS entry belongs to another system or identifier:** retain the mismatch and prepare correction through the authorized owner; do not claim coverage based on company name alone.
- **Government finding conflicts with self-assessment:** preserve both records and route the discrepancy through the defined review process; do not overwrite the government result.

## Evidence and test plan

**Source and rights snapshot.** Use the [DoD safeguarding and assessment page](https://www.acq.osd.mil/asda/dpc/cp/cyber/safeguarding.html), applicable solicitation/contract and incorporated terms, and authorized DoD/organization records; prior snapshot 2026-07-31; verify methodology and contractual baseline. This is original readiness-planning language, not NIST or DoD assessment content, an official score, an SPRS submission, a CMMC result, or a contractual representation. Contracts, legal, system, security, and authorized officials decide applicability, scope, score approval, submission, and external statements.

### 1. Contract, scope, SSP, and assessment-governance package

- **Request and owner:** Contracts, program, system, security, and information-governance owners provide award/modification references, human-approved scope rationale, system/security-plan ownership and version record, boundary and information-flow context, assessment need/deadline ledger, supplier dependencies, and accountable approver roster.
- **Validate and limit:** Trace one selected scope or assessment entry to a source record, named owner, system/boundary context, applicable decision record, and review date. This supports readiness traceability; it cannot interpret a contract, determine covered information, or decide official assessment scope.
- **AI and trigger:** AI may maintain a read-only ledger of approved metadata and flag stale plans, missing owners, or changed dependencies. Humans decide applicability, scope, and assessment route. Refresh after an award, modification, boundary/information-flow change, supplier change, or source update.

### 2. Evidence, POA&M, and readiness-observation package

- **Request and owner:** System, control, operations, assessment-support, and remediation owners provide original implementation evidence, evidence index/provenance, assessment observations, POA&M governance records, milestones, constraints, remediation approvals, and retest/follow-up records.
- **Validate and limit:** Sample a readiness claim or open item through a dated artifact, owner, bounded system/process context, observation, limitation, action/milestone, and retest or management review. This can support preparation; it cannot calculate a score, attest implementation, or close an official assessment finding.
- **AI and trigger:** AI may identify missing provenance, stale milestones, and inconsistent metadata and draft questions. Humans validate evidence, approve corrective-action closure, and interpret assessment observations. Recollect after failed testing, milestone changes, material technical changes, or assessment activity.

### 3. Score, submission, and supplier-status governance package

- **Request and owner:** Executive, security, contracts, supplier-management, and authorized submission owners provide score-history inputs, review/approval records, representation-preparation records, supplier assurance/status records, exceptions, risk decisions, and annual-review evidence.
- **Validate and limit:** Trace one selected score input, supplier record, or status statement to its source, accountable reviewer, limitation, decision authority, date, and follow-up. This supports accountable governance; it cannot generate or approve an official score, submit to SPRS, accept contractual risk, or certify a supplier.
- **AI and trigger:** AI may flag stale status, expiring decisions, and incomplete review trails. Authorized humans approve scores, submissions, affirmations, risk decisions, and external statements; independent reviewers challenge assumptions and source traceability. Review quarterly, annually, and after material contract, supplier, system, or remediation change.


## Cadence and renewal

Quarterly reconciliation and annual preparation are engagement conventions. Verify required recency from the solicitation and clauses rather than resetting the assessment annually by assumption. Reopen affected evidence after scope, supplier, control or remediation changes; preserve history of assessments, approvals and posted records.

## Completion and handoff

Deliver source and applicability decisions, SSP/boundary version, complete requirement evidence, remediation status, authorized score-review records and actual submission/readback records where permitted. State what was prepared, assessed, approved and posted. Name each next owner, action and required evidence without earlier chat; readiness does not establish a score, certification or contractual compliance.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
