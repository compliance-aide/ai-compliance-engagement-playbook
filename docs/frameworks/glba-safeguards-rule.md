# GLBA Safeguards Rule — engagement guide

> Original operational guidance, not legal advice, a compliance conclusion or an FTC notification. Draft pending independent source, skeptical and rights review.

## Source and applicability

Use [16 CFR Part 314](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314) and the [FTC business guide](https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know). The FTC guide was read; current eCFR text returned an access challenge. Full regulation and entity-specific interpretation remain unverified.

The FTC guide ties coverage to activities and regulator jurisdiction. Its fewer-than-5,000-consumer exception concerns specified provisions, not the whole rule. Confirm each exception separately. It describes a Qualified Individual and a written security program. For applicable notification events, it describes FTC reporting as soon as possible and within 30 days of discovery, covering unauthorized acquisition involving at least 500 consumers' unencrypted information. Compromised encryption keys and the access/acquisition presumption matter. Counsel must verify definitions, discovery attribution and other reporting duties before deciding; this paragraph is not a complete incident test.

The steps below are original engagement procedures. Record applicable source versions, provision-level exceptions, required testing frequencies and governance deadlines before execution. Do not assume a previous year's interpretation is current.

## Engagement focus

Demonstrate how the covered customer-information population connects to program accountability, risk decisions, implemented safeguards, provider oversight and incident/governance records. Separate the existence of a policy from actual operation and the evidence of operation from a legal adequacy conclusion.

## Roles

Legal counsel determines jurisdiction and applicability. The Qualified Individual supervises the program within the verified rule and organization structure. System, security, records and service-provider owners supply implementation evidence. Incident officials own response and reporting decisions. An independent reviewer challenges source interpretations, gaps and outcomes. Named management officials approve resources, exceptions and final decisions.

AI may reconcile inventories, organize evidence, reperform approved calculations and draft reports. AI cannot designate the regulator, approve safeguard alternatives, declare safeguards adequate, accept risk, submit notifications or replace independent review. Testing and changes require explicit scope and authorized environments.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Record entity activities, customer-information definition, reporting period, owners, evidence access and permitted actions. Obtain applicability analysis, exact provision-level exceptions, written program, risk assessment, system/provider inventory and incident escalation route. Missing applicability evidence blocks dependent conclusions, not independent inventory work.

## Ordered workflow

1. **Approve scope and duties.** Map each applicable provision to owner, population, required artifact and due date/trigger. Record the evidence supporting any exception and its precise effect. Output: obligation register; do not use a customer count as a blanket exemption.
2. **Reconcile the information boundary.** Follow covered information through collection, paper/electronic storage, access, transmission, providers and disposal. Compare data, asset, affiliate and service records. Output: complete scoped inventory with unlocated data and unsupported exclusions retained.
3. **Connect risks to decisions.** Link foreseeable risks and changes to approved treatments, responsible officials and actual implementation records. Output: risk/safeguard matrix. Distinguish a proposed alternative from approval and approval from demonstrated operation.
4. **Test safeguard operation.** Use the approved assessment plan and source-backed frequency requirements. Record scope, expected behavior, authorized method, actual results and uncovered systems. Output: evidence register with all known gaps; a scanner producing no findings does not prove coverage of disconnected assets.
5. **Verify provider oversight.** Match data/integration scope to provider selection, contracts, responsibilities, monitoring and reassessment evidence. Output: provider matrix; a contract or assurance report cannot establish every customer-side configuration.
6. **Reconcile incidents and oversight.** Preserve discovery chronology, affected-consumer accounting, encryption/key facts, uncertainties, decision authority and notification state. Connect program issues and tests to the required governance report and action owners. Output: separate incident decision packet and management-report packet.
7. **Review and verify remediation.** Supply complete evidence to the independent reviewer, retain disagreements and route final decisions to the authorized officials. Retest affected implementation and reconcile every downstream report. Output: bounded results, open work and verified decision/receipt references.

## Evidence and test plan

### Customer-information boundary and accountability package

Restore the PR340 package with full-population reconciliation. Legal, privacy and business owners supply jurisdiction/applicability, customer-information flows, program ownership and the Qualified Individual's designation. Tie every scoped system and service to actual data and an accountable owner. Record outsourced supervision responsibilities rather than treating outsourcing as transfer of accountability.

### Risk, safeguard and provider package

Security and procurement supply risk records, approved criteria, configurations, access/monitoring/change evidence, retention/disposal records, provider responsibilities and exceptions. Maintain one record per applicable safeguard/population with implementation, test and coverage status. Relevant test routes may include access revocation, approved authentication behavior, data protection, disposal, monitoring and provider handoffs; derive exact requirements and alternatives from the verified rule. Track exceptions by authorizer, rationale, scope, evidence and review trigger, without letting an approval overwrite an observed failure.

### Incident, reporting and oversight package

Incident, legal and program owners supply case chronology, affected-population reconciliation, investigation facts, notifications and management reports. Deduplicate consumer counts without erasing affected records. Keep known facts separate from estimates; escalate uncertainty promptly instead of waiting for forensic perfection. Preserve draft, approved, submitted and acknowledged states separately. Retain notice revisions and their receipts. Governance reporting must preserve adverse findings and source limitations rather than presenting ticket closures as proven effectiveness.

## Failure branches and decisions

- Exception lacks provision-level support: mark the exception claim inconclusive and route it to counsel; continue evaluating unaffected obligations.
- Safeguard approved but not operating: mark its implementation criterion not_supported, retain the approval as a separate fact and assign remediation.
- Monitoring unavailable: mark coverage gaps explicitly. Do not infer continuous monitoring from an installed agent or successful dashboard login.
- Incident threshold or discovery uncertain: promptly route the current facts and legal questions to the responsible officials. Keep original timestamps; team reassignment is not a new discovery date.
- Provider implements its portion but the customer integration is missing: separate those outcomes; do not inherit the entire result.

Fictional desk case: an access-removal ticket is closed, yet an authorized QA check shows the departed test identity can still retrieve covered information through a secondary application. Ticket closure is supported; the access-revocation criterion is not_supported. Other applications remain separately assessed or not_tested.

## Cadence and renewal

Populate a source-backed schedule for testing, reassessment, incident handling and Qualified Individual reporting, accounting for verified exceptions. Preserve event triggers for changes, new threats, incidents and failed tests. Do not replace specific required frequencies with a generic annual review, or label periodic scanning as continuous monitoring without evidence.

## Completion and handoff

Deliver the obligation/exception register, full information/system/provider inventory, risk decisions, safeguard tests, incident packets, governance report, gaps, reviewer disagreements and named next owners. Classify assertions supported, not_supported, inconclusive, not_applicable or not_tested. Final legal conclusions, alternative controls, risk acceptance and notifications require their designated authority and separate evidence. No real financial-institution assessment or notification was performed by drafting this guide.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) and [agent runbook](../agent-runbook.md). Keep customer information and restricted incident records out of this public repository.
