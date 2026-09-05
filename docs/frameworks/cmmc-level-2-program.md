# CMMC Level 2 program — engagement guide

> Original operational guidance, not CMMC certification or a government submission. Check current [DFARS CMMC rules](https://www.acq.osd.mil/dpap/dars/dfars/html/current/204_75.htm).

## Engagement focus

Maintain solicitation, contract, CUI, subcontract, assessment-type, system-scope, evidence, remediation, status, and annual-affirmation records.

## Roles

Operators refresh evidence and change impacts; independent reviewers perform readiness testing. AI identifies gaps and drafts questions, but cannot attest, submit to SPRS, or represent certification. Review quarterly and annually.


## Source and applicability

The [official program overview](https://dodcio.defense.gov/CMMC/about/), checked September 4, 2026, reports suspension of Phase II implementation while Phase I self-assessments remain. It describes Level 2 self-assessment against 110 NIST SP 800-171 Revision 2 requirements every three years with annual affirmation. Do not substitute Revision 3 merely because it is newer. Resolve the contract's actual assessment route, scope, dates and current direction before scheduling assessment or claiming eligibility.

The overview permits limited Level 2 assessment POA&Ms under 32 CFR 170.21, with closeout within 180 days, and states that final status validity runs from the conditional status date. Confirm the full eligibility, scoring, prohibited-item and closeout rules against the current regulation; a score alone does not establish conditional eligibility. Do not restart a status clock when remediation closes. Obtain the current assessment and scoping guides from the [official resources page](https://dodcio.defense.gov/CMMC/Resources-Documentation/) and record exact versions.

## Before starting

Use the [agent runbook](../agent-runbook.md). Name contracts, security, control, assessment and affirming owners. Keep CUI and protected evidence in approved environments; use authorized metadata and evidence pointers in agent workpapers. Create separate fields for draft observation, human assessment determination, official status and verified submission. A prior NIST assessment score, consultant readiness report or purchased tool does not by itself establish CMMC status.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Resolve the route | Contracts owner checks the actual solicitation, award, modifications and current program direction for self-assessment or an expressly applicable other route. | Source-linked requirement, date and decision owner; route ambiguity blocks the related formal claim. |
| 2. Define scope | Security and data owners trace CUI flows, assets, external services, supplier responsibilities and exclusions using current Level 2 scoping guidance. | Approved scope and responsibility register; a supplier assertion or encrypted channel alone does not justify exclusion. |
| 3. Build the assessment register | Agent indexes all 110 requirements and every applicable objective from the adopted assessment guide. | Each has an owner, scope, source reference, evidence plan and method. Missing objectives remain visible. |
| 4. Collect and test | Owners provide system security plan, procedures, configuration and operational artifacts; authorized testers examine, interview and test within approved scope. | Dated observations with coverage and limitations; policy intent is distinguished from demonstrated operation. |
| 5. Review findings and scoring | Human assessment lead applies official finding and scoring rules to the complete evidence set. | Reviewable determinations and calculation provenance; workpaper inconclusive is not silently converted into MET. |
| 6. Decide and execute remediation | Assessment lead checks each proposed assessment POA&M item against all eligibility rules; owners implement approved corrections. | Separate preparation backlog, operational deficiencies and eligible assessment POA&M records, each with authority and dates. No generic risk acceptance overrides a prohibited deferral. |
| 7. Close out and prepare status records | Authorized assessor performs the applicable closeout assessment; owners reconcile scope identifiers, dates, results and annual-affirmation inputs. | Retest and authorized assessment records, then a reviewed submission package. Government submission and affirmation require explicit human approval and system readback before any completion claim. |
| 8. Maintain the status | Program owner tracks annual affirmation, reassessment, conditional deadlines, supplier obligations and material changes separately. | Calendar and verified receipts tied to actual scope; unresolved changes trigger review instead of automatic renewal claims. |

## Failure branches and decisions

- **Assessment route conflict:** preserve both source records and refer to the contracts authority. Do not choose the cheaper route or obsolete rollout schedule by inference.
- **Unknown inheritance:** identify the supplier service and precise responsibility; request evidence for both provider and customer duties. A supplier certificate cannot prove customer configuration.
- **High draft score with prohibited gaps:** keep the eligibility decision unresolved until the full rule is applied. A percentage does not make every missing requirement deferrable.
- **Closeout deadline at risk:** escalate the dated record and status consequences to the accountable owner. Do not invent an extension or call a remediation ticket an assessment closeout.
- **Evidence collection failure:** record an inconclusive workpaper and authorized collection action; do not bypass access controls or suppress the gap from the assessor package.

## Evidence and test plan

**Source and rights snapshot.** Use the current official [DFARS CMMC rule text](https://www.acq.osd.mil/dpap/dars/dfars/html/current/204_75.htm); prior snapshot dated 2026-07-31; revalidate before use. This original operational plan does not reproduce restricted assessment content, determine assessment scope, make a certification claim, submit to SPRS, or make an annual affirmation.

### 1. Contract, CUI, and assessment-path evidence

- **Request and owner:** Contracts, program, and security owners provide solicitation/award applicability records, CUI identification and flow records, subcontractor applicability records, assessment-type and deadline records, system-scope rationale, and accountable owners.
- **Validate and limit:** Trace a selected contractual requirement or CUI flow to the source record, affected system/process, owner, and stated assessment path. This supports a factual scoping trace; it cannot interpret contract obligations, determine CUI status, or decide scope.
- **AI and trigger:** AI may organize approved metadata and flag changed solicitations, systems, or suppliers. Contracts, legal, and authorized security humans decide applicability and scope. Refresh after an award, modification, CUI-flow change, subcontractor change, or architecture change.

### 2. Practice evidence, remediation, and readiness-test record

- **Request and owner:** System and control owners provide policy/process references, implementation evidence, operational records, evidence index, remediation plans, milestones, and independent readiness-test observations.
- **Validate and limit:** Trace selected readiness claims to an owner, dated source artifact, system/process context, observed limitation, remediation action, and retest record. This can support readiness preparation; it cannot attest implementation, determine a score, or state assessment readiness as certification.
- **AI and trigger:** AI may prepare redacted evidence requests, identify missing provenance, and draft questions. Humans validate evidence, authorize remediation closure, and control assessment communications. Refresh after material changes, failed tests, or remediation milestones.

### 3. Status, affirmation, and subcontractor-governance evidence

- **Request and owner:** Executive, contracts, and security owners provide status records, leadership review notes, subcontractor assurance records, exceptions, risk decisions, annual-review inputs, and any affirmation preparation record.
- **Validate and limit:** Sample a status or subcontractor record for source, named owner, limitation, decision authority, expiry, and follow-up. This can demonstrate accountable governance; it cannot make an affirmation, submit to SPRS, accept contractual risk, or certify a supplier.
- **AI and trigger:** AI may flag stale status, expiring decisions, and overdue reviews. Authorized humans make representations, affirmations, submissions, and risk decisions. Review quarterly and annually, and immediately after a material contract, CUI, supplier, or system change.

## Cadence and renewal

Maintain separate clocks for assessment, affirmation and conditional closeout using authoritative dates. Quarterly readiness checks are an internal convention. Reopen affected objectives after CUI-flow, contract, asset, supplier, incident or source changes. Compare new scope with the prior assessed scope before reusing evidence or status; preserve both rather than silently changing the denominator.

## Completion and handoff

Deliver scope and route decisions, full objective register, safe evidence references, human assessment/scoring records, remediation eligibility decisions, closeout evidence and renewal dates. State what is drafted, reviewed, officially recorded and independently verified. The next agent must know the next action, owner and missing evidence without chat history. Preparation completion is not certification or affirmation.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
