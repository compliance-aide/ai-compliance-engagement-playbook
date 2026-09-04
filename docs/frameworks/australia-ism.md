# Australian Information Security Manual — engagement guide

> Original operational guidance, not ASD control text, a classification decision,
> an assessment opinion or an authorisation to operate.

## Source and applicability

Use [ASD's ISM](https://www.cyber.gov.au/ism) and
[using the framework](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/ism/using-the-cyber-security-framework).
Checked 2026-09-04: ASD links the September 2026 edition and change record.
Its guidance distinguishes system definition, approved control selection,
implementation, assessment, authorisation and monitoring. ISM advice is not
universally mandatory by itself; record the legal, policy or contractual authority
that makes it applicable. Laws take precedence over conflicting guidance.

Rights: original instructions and links; no controls or restricted system data
copied. See [ASD copyright](https://www.cyber.gov.au/about-us/copyright) and the
[author record](../refresh-reviews/australia-ism.md). Independent review and
publication approval remain pending.

## Engagement focus

Prepare a system-specific evidence and decision packet that stays aligned with
the actual operating environment. Distinguish planned from implemented safeguards,
assessment results from risk acceptance, and source updates from approved system
changes. A passed scan does not authorise a system.

## Roles

System/information owners establish boundaries and approved handling/classification.
Security owners propose safeguards; authorised officers approve selection and
operation. Operators implement changes under the release gate. Qualified assessors
and independent reviewers evaluate evidence. AI may organise permitted metadata,
draft options and execute authorised read-only checks. It cannot classify data,
accept risk, authorise operation or expand its evidence-access permission.

## Before starting

Obtain the charter, pinned ISM edition, system/information-flow inventory,
classification/handling decision, authorising authority, security plan and annex,
existing assessment/authorisation records and test permissions. Confirm the actual
system version. Missing authority or classification blocks dependent access and
claims; permitted metadata preparation may continue. Use the
[agent runbook](../agent-runbook.md).

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Define the system | Owners reconcile boundaries, interfaces, dependencies, criticality and information handling. | Approved system description and unresolved flows, with actual environment/version. |
| 2. Record control decisions | Security drafts system-specific selection and inheritance rationale; the authorising officer approves the plan. | Versioned security-plan annex with decisions and evidence owners; AI proposals remain draft until approved. |
| 3. Record actual implementation | Operators implement authorised work and document departures from the plan; AI indexes receipts. | Actual configuration evidence and change history match the scoped system. |
| 4. Assess | Assessor, owner and authority agree method/scope; authorised tests produce preserved results. | Assessment workpapers and report identify strengths, adverse results and coverage limits. |
| 5. Resolve risk and authorisation | Owners prepare correction/milestone records and supporting plans; the officer decides operation and conditions. | Explicit decision, scope, constraints and expiry where applicable; no implied authorisation from a report. |
| 6. Monitor and reassess | Operations monitor approved signals; security evaluates system/source changes; assessor rechecks affected claims. | Updated evidence/decision packet and next tests; historic results remain traceable. |

These coordination steps follow the source's broad lifecycle; the governing
method and authorised decisions determine assessment detail.

## Evidence and test plan

| Request and custodian | Check | Expected observation | Failure or limit |
| --- | --- | --- | --- |
| System/flow plan from owners | Compare authorised scope and handling with observed metadata/interfaces. | System identity and boundaries reconcile. | A missing interface leaves scope incomplete. |
| Approved annex and implementation from security/operators | Trace a selected safeguard from decision to actual configuration and operation. | Planned and observed states are distinguishable and linked. | A policy or deployment request is not implementation evidence. |
| Inherited assurance from provider/assessor | Compare service, period, exclusions and responsibilities to the system claim. | Reliance rationale and gaps are explicit. | Provider approval does not automatically authorise the customer's system. |
| Assessment and decision packet from assessor/officer | Follow adverse findings through milestones, retest and authorisation conditions. | Decisions match current evidence and remain within conditions. | A completed assessment does not itself grant operation. |

## Failure branches and decisions

If restricted evidence exceeds tool authorisation, preserve an approved reference
and request an authorised reviewer; do not move the content. If a source release
changes, prepare a version delta and impact review before replacing approved
controls. Expired or incompatible operating conditions go to the authorising
owner, not an AI extension. An inherited claim without supporting assurance is
inconclusive. Active tests against operational technology need explicit safety
and operational authority, even when the tool calls them assessments.

## Cadence and renewal

Follow the approved monitoring plan and authorisation conditions. Reassess after
material architecture, threat, policy, incident or control changes. Review the
September 2026 change record against the pinned edition; do not silently migrate.
Quarterly evidence housekeeping and annual governance review are planning defaults,
not a universal authorisation duration or substitute for continuous monitoring.

## Completion and handoff

Deliver the system/security plan and annex, incident/change/monitoring plans,
assessment report, correction/milestone record, authorisation decision and next
queue. State restrictions, untested areas and unresolved inherited claims. Keep
all sensitive artifacts in their approved systems, outside this public repository.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md).
