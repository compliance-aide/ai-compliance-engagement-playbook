# FDA QMSR / 21 CFR Part 820 — engagement guide

> Original operational guidance, not FDA or ISO content or a quality-system conclusion. See the [FDA QMSR resource](https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr).

## Source and applicability

Use the [agent runbook](../agent-runbook.md). Source checkpoint, 2026-09-04:
FDA's indexed QMSR resource identifies the rule as effective February 2, 2026,
incorporating ISO 13485:2016 by reference. This is current-operation context,
not a future transition deadline. Full Part 820, incorporated licensed standard,
technical amendments and inspection guidance remain unverified in this pass.
Use authorized access to the standard; do not reproduce protected requirements
in this repository or assume an ISO certificate establishes FDA compliance.


## Engagement focus

Maintain device/manufacturer scope, transition, ownership, supplier, change, CAPA, complaint, training, management-review, audit, and disposition evidence.

## Before starting

Record the complete approved device/site/process population, review period,
licensed-source access, evidence permissions and named quality/regulatory owners.
Use [work items](../../templates/work-item.md) to separate process documentation,
execution and effectiveness assertions. Define acceptance criteria before testing.

Keep confidential records and protected standard text outside this repository.
Use synthetic examples in QA-named workspaces; no real product disposition,
controlled-record modification or inspection communication is authorized by this
guide-development task. Record missing sources and unobservable processes explicitly.

## Ordered workflow


1. Record manufacturer role, sites, devices, activities and applicable regulatory
   scope. Quality/regulatory owners approve inclusions, exclusions and source
   interpretations. Link each process to its responsible site and outsourced work.
2. Map the approved current requirements to processes, owners, procedures and
   operating records. Preserve legacy references as historical context where
   needed. Renaming an old procedure or file does not establish that the current
   requirement is addressed or the process actually changed.
3. Reconcile design/change, purchasing, production, complaint, nonconformance and
   corrective-action interfaces within the approved scope. Track where a record
   or decision passes between teams; an isolated complete file cannot establish
   that downstream action occurred.
4. For each process assertion, define its criterion, period, population and method
   before examining results. Trace complete scoped evidence without reducing the
   corpus supplied for scoring. Keep missing, conflicting and inaccessible records
   explicit rather than selecting only closed or successful cases.
5. Distinguish immediate correction, cause investigation, corrective action and
   effectiveness evidence in the approved workflow. A training assignment or
   revised procedure does not prove the cause was addressed. Quality decides
   whether the evidence supports closure; AI cannot close CAPA or disposition product.
6. Link supplier changes to affected materials/components, approvals, acceptance
   evidence and relevant product/process records. A supplier certificate does not
   prove the specific change was evaluated or the received item met criteria.
7. Reconcile training/competence evidence to the role and procedure actually used.
   Attendance or acknowledgment supports that narrow fact, not necessarily ability
   to perform the task. Have the owner define any required competence observation.
8. Prepare management/audit review with complete findings, open actions and repeated
   issues. Verify approved changes and retests in their actual process records.
   Keep missing effectiveness evidence open rather than treating due-date changes
   or administrative closure as success.
9. Hand off unresolved risks, record gaps and regulatory questions with named
   owners. Separate inspection preparation from FDA acceptance and internal
   quality approval from product release or regulatory submission.

## Failure branches and decisions

 an unavailable licensed requirement leaves its mapping
`inconclusive`. Missing execution evidence is `not_tested`; a known missed
approved process step is `not_supported`. Do not use an overall document-count
score to erase a specific observed failure.

**Fictional desk case:** a QA corrective-action record says staff were retrained,
but its approved effectiveness criterion requires checking the next defined
production-record population. That check has not occurred. Training completion
may be `supported`; effectiveness is `not_tested`. No real production, CAPA or
product disposition is represented.

## Roles

Humans approve quality and product decisions; independent reviewers maintain separate evidence ledgers. AI forecasts work queues, but cannot close CAPA, disposition product, or contact FDA. Use the approved review cadence and change triggers below.


## Evidence and test plan

Retain the three PR #340 packages below with full in-scope coverage. Transition
records explain historical changes; current operation requires current evidence.
Earlier review does not approve this revision.

### 1. Device, establishment, and QMS transition record

- **Request and owner:** Device/family and manufacturing-site scope, legal-manufacturer roles, applicable market/product records, QMS transition assessment, documented-process ownership, and approved gap/change plan from regulatory, quality, and operations leaders.
- **Validate and limit:** Trace each in-scope device or site to an accountable quality owner, declared QMS scope, transition decision, and open change record. This can support a defined preparation boundary; it cannot determine regulatory applicability, market authorization, or inspection readiness.
- **AI and trigger:** AI may reconcile approved inventories and flag missing owners or transition dates. Regulatory and quality humans approve scope and transition decisions. Refresh after a product, site, supplier, market, or rule-change event.

### 2. Design, production, supplier, and training evidence

- **Request and owner:** Controlled document/version records, design or process-change support, production/acceptance records, supplier qualification/monitoring evidence, equipment/process records where applicable, and role-based training records from quality and operations owners.
- **Validate and limit:** Trace each in-scope activity from controlled document through responsible activity, training/qualification, record date, and exception. This can support that traceable records exist for the reviewed activities; it cannot establish product safety, device conformity, or complete process effectiveness.
- **AI and trigger:** AI may index authorized metadata and identify missing approvals or expired training; it may not release product, change a controlled record, or approve a supplier. Recollect after a design/process/supplier change, significant nonconformity, or periodic review.

### 3. Complaint, CAPA, audit, and management-decision record

- **Request and owner:** Complaint intake/trending evidence, nonconformity and CAPA log, investigation/remediation/retest records, internal-audit results, management-review inputs, and product-disposition decisions from quality leadership.
- **Validate and limit:** Trace each in-scope issue from intake to investigation, decision authority, corrective action, effectiveness check, and unresolved risk. This can support controlled issue governance; it cannot close a CAPA, make reportability decisions, disposition product, or contact FDA.
- **AI and trigger:** AI may flag overdue actions and draft a read-only traceability view. Quality and regulatory humans approve dispositions, CAPA closure, external communications, and submissions. Review at the approved operating cadence, at management review, and after a significant complaint or audit finding.


### Process and effectiveness reconciliation

Match the procedure version used at the time of an activity to its operating
record, responsible role and approval. Do not retroactively judge historical work
against a later procedure without an owned basis. Conversely, an old compliant
record cannot establish that today's changed process operates correctly.

For effectiveness checks, have quality define the population, observation period,
method and acceptance criterion. Record whether enough relevant activity has
occurred to execute the check. No recurrence in a period with no applicable
activity does not establish effectiveness. Keep a future check scheduled and owned
rather than closing it as passed.

Reconcile complaint, nonconformance and supplier records to investigations and
related actions using stable identifiers. Preserve duplicate reports as linked
source evidence where relevant; merging case administration must not erase facts
or conceal the extent of an issue. Record independent reportability and product
impact decisions through their authorized routes.

For management review, distinguish input receipt, discussion, decision, assigned
action and implemented result. Meeting minutes do not establish that a resulting
process change occurred. Trace each action to execution and any required retest,
with open limitations visible in the next handoff.

## Cadence and renewal

Follow approved quality procedures and applicable requirements for review timing.
Do not present internal monthly, quarterly or annual schedules as universal QMSR
requirements. Reopen scope and evidence after device/site/process changes, supplier
issues, complaints, audit findings or source updates. Preserve outstanding
transition actions until their current operational effect has been verified.

## Completion and handoff

Deliver the source/scope map, process-owner register, controlled-version links,
complete operating evidence index, findings, decisions, corrections and
quality-approved effectiveness results. Keep unexecuted checks and unresolved
licensed-source questions with named owners and next actions.

State the period and process population supported by the evidence. Readiness
work is not FDA acceptance, product release or a quality-system certification.
Independent source, skeptical, rights, publication and cross-model reviews remain
pending; structural tests do not prove these requirements.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
