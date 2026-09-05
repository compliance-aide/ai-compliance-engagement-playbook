# IRS Publication 1075 / FTI safeguarding — engagement guide

> Original operational guidance, not IRS content, authorization to receive federal tax information, or an approved safeguard report.

## Source and applicability

Use the [IRS Safeguards Program](https://www.irs.gov/privacy-disclosure/safeguards-program), current Publication 1075, agency agreements and IRS directions. The program listing checked 2026-09-04 references the November 2021 revision. The full publication and agency-specific directions have not been reviewed for this draft; confirm the controlling version and requirements before a safeguard determination.

The [SSR guidance](https://www.irs.gov/privacy-disclosure/safeguard-security-report) and [incident guidance](https://www.irs.gov/privacy-disclosure/reporting-unauthorized-accesses-disclosures-or-data-breaches) were read on 2026-09-04. They distinguish approved access, annual reporting, separate notifications and immediate incident escalation. Resolve inconsistent cross-reference numbering against the controlling publication rather than copying a section number as proof.

## Engagement focus

Trace federal tax information (FTI) from authorized receipt and permitted use through systems, people, contractors, disclosures, storage and disposal. Keep evidence of controls separate from evidence that a particular use, recipient or environment is authorized. A cloud certification or contract does not itself authorize FTI processing.

## Roles

The agency safeguards official owns the program and IRS coordination; legal and program owners establish disclosure/use authority. System, identity, physical-security and contractor owners supply implementation evidence. Incident leaders preserve facts and activate the approved reporting process. The authorized agency head certifies required reports. An independent reviewer challenges scope and evidence. AI may organize sanitized metadata in an authorized environment, but cannot receive FTI in an unapproved system, authorize services, grant access, determine disclosure authority, submit reports or accept risk.

## Before starting

Record the receiving agency, statutory/agreement authority, purpose, systems, sites, contractors and review period. Identify approved evidence repositories, actual processing tools and accountable officials. Confirm that every tool, model endpoint, log destination and support path used for sensitive work is permitted before ingesting FTI. This public repository and an ordinary chat are not presumed approved. Use synthetic fixtures or approved non-sensitive metadata; if evidence cannot be accessed safely, record the gap rather than uploading it elsewhere.

## Ordered workflow

1. **Establish authority and the baseline.** Obtain approval references for receipt, use, systems and disclosures. Reconcile the complete known FTI population and all routes against program and technical inventories. Assign stable system, flow and owner IDs. Record disputed classification for safeguards/legal resolution; do not infer absence of FTI from a missing label.
2. **Map actual boundaries and dependencies.** Include interfaces, extracts, reports, backups, logs, physical media, remote support and downstream contractors. Compare intended destinations with configuration and authorized operational evidence. Preserve unknown stores and copies. Never silently sample, trim or cap evidence bound for assessment; distinguish complete inventory accounting from the scope of technical tests.
3. **Verify access and operations.** Link each access role and scoped access change to permitted use, need, approval, required personnel checks/training, actual provisioning and removal evidence. Review safeguards across physical access, logging, monitoring, encryption, transmission and disposal against the verified requirements. Keep supplier assertions separate from agency implementation evidence; identify shared responsibilities and unsupported controls.
4. **Prepare changes before data movement.** Classify new technologies, hosting, contractors and interfaces against current notification/approval requirements. The [IRS cloud guidance](https://www.irs.gov/privacy-disclosure/cloud-computing-environment) identifies advance cloud notification at least 45 days before transmitting FTI. Have the safeguards owner verify the complete conditions and actual permitted start; elapsed time or a send receipt alone is not an authorization. Record the change in both the applicable notification process and the SSR update register.
5. **Activate incident handling without waiting for certainty.** Preserve the time a possible FTI issue was identified, known facts, evidence references and authorized containment actions. IRS incident guidance requires immediate contact with TIGTA and the Office of Safeguards, no later than 24 hours after identifying a possible issue involving FTI. Do not await a completed investigation or use 24 hours as a target delay. Escalate to the authorized official and backup promptly; preserve reporting receipts and failed attempts. AI prepares facts but does not independently transmit FTI or make submissions.
6. **Build the correct report and notification package.** Use the accepted SSR returned with the agency's previous acceptance letter; new-agency onboarding uses the IRS process. Verify the reporting period and agency-specific deadline from the current IRS table. Reconcile every assertion with evidence and unresolved deficiencies, map attachments clearly and obtain the required agency-head certification. SSR submission does not replace a separate notification. New-agency access requires the applicable approved SSR, SAR and ATO evidence before FTI receipt, as described by IRS guidance.
7. **Verify outcomes and retain open work.** Read back report and notification receipts through the approved channel and distinguish submitted, accepted, approved and unresolved states. Track IRS questions, findings, corrective actions and retests. Verify recovery and continued protection before closure; a restored service or closed ticket does not establish remediation. Deliver an accountable handoff with remaining gaps and next decisions.

## Evidence and test plan

These three original packages preserve and expand the earlier tailored plan.

| Package | Minimum records | Reviewer challenge |
| --- | --- | --- |
| FTI boundary, flow and authorization | Complete known inventory, source/use authority, actual destinations, approvals, labels and custodians | Is the specific route authorized, and does it match reality? |
| Access, operations and incident | Personnel/access records, safeguard evidence, media lifecycle, original incident clock, escalation and response receipts | Did the control operate and did each required reporting path receive attention? |
| Reporting, governance and independent review | Accepted SSR baseline, agency calendar, change notifications, evidence mappings, certification, IRS responses and retests | Are report assertions supported, and are independent notification duties still visible? |

Use the [agent runbook](../agent-runbook.md) statuses `supported`, `not_supported`, `inconclusive`, `not_applicable` and `not_tested` for individual assertions. Split compound conclusions. Unknown coverage does not cancel a demonstrated failure. If an official inspection methodology specifies a subset, record that method and approval separately without discarding any available assessment evidence or representing the inspection as a full-population test.

Fictional author desk case: an annual SSR draft mentions a planned cloud service, but the separate cloud-notification record is absent. The SSR entry does not prove notification or permission to transmit FTI. Record the missing gate, retain the planned destination and have the safeguards owner resolve it before movement. No real FTI or cloud test is needed for this desk check.

## Failure branches and decisions

- FTI appears in an unapproved tool or destination: stop further transfer, preserve authorized incident facts and promptly invoke the approved escalation route; do not copy it into a public issue.
- A supplier certificate is the only control evidence: retain the evidence limitation and obtain configuration/responsibility records.
- Reporting contact or delivery fails: activate the approved backup route and preserve timing; never mark a send attempt as successful reporting.
- Incident communications to individuals or media are proposed: route for required agency approval and IRS coordination before release, following the incident guidance.

## Cadence and renewal

Maintain the actual annual SSR cycle and event-driven obligations, with agency-specific due dates. Verify other required inspection, training and control-review frequencies from the current publication and directions. Remove invented blanket quarterly reviews. Reopen affected records after use, system, personnel, contractor, physical-site, source or incident changes.

## Completion and handoff

Deliver sanitized registers and approved private evidence links, source decisions, control results, reporting status and owned corrective actions. Independent source, skeptical and rights review remain required before guide publication. Author desk checks are not an IRS review, authorization, real assessment or cross-model usability validation.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) with the runbook for authority, evidence, exceptions and source changes.
