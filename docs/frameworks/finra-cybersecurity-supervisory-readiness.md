# FINRA cybersecurity supervisory readiness — engagement guide

> Original operational guidance, not a FINRA framework, rule interpretation, or supervisory approval. Consult the [FINRA cybersecurity hub](https://www.finra.org/rules-guidance/key-topics/cybersecurity).

## Engagement focus

With qualified compliance ownership, establish firm-specific supervisory obligations and processes in scope. Maintain evidence for governance, risk, access, change, vendor, branch, data-protection, training, and incident communications. Test consequential scenarios and keep escalations traceable.

## Source and applicability

Use the current FINRA cybersecurity hub, applicable rule text and firm-specific compliance decisions. Official indexed [2026 Regulatory Oversight Report](https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report) material checked 2026-09-04 includes cybersecurity/cyber-enabled fraud and third-party risk topics. The full relevant sections, underlying obligations, later notices and any SEC or state requirements remain to be verified. Keep regulatory obligations, observed effective practices and internal targets distinct; this readiness guide is not a standalone FINRA certification framework.

## Roles

The compliance owner approves obligation mapping and supervisory scope. Technology, branch, business and provider owners produce operating evidence. Incident and legal owners make notification and reporting decisions. Independent reviewers challenge completeness and conclusions. AI organizes authorized records and drafts gaps; it cannot decide reportability, file reports, approve a supervisory program or make customer-account changes.

## Before starting

Record legal entity, business activities, branches, systems, providers, review period and approved information access. Identify responsible supervisors and alternates. Establish a current source register with applicability decisions rather than relying on a prior-year checklist. Use the [agent runbook](../agent-runbook.md) to define each check's expected behavior, scope, evidence and next owner. Use synthetic customer identities and transactions in approved QA; keep real account details and incident evidence in controlled systems.

## Ordered workflow

1. **Map obligations to actual activities.** Link each applicable requirement or approved practice to a business process, responsible supervisor and source. Output an obligation/process map; unresolved legal interpretation goes to compliance without inventing a deadline or blanket exemption.
2. **Reconcile the operating boundary.** Compare branch, user, system, data and provider inventories with the processes in scope. Include remote and outsourced routes. Output a coverage register with omissions; head-office evidence alone cannot establish branch-wide operation.
3. **Trace supervision into execution.** Link written procedures to assigned roles, access configurations, reviews, exception handling and retained results. Output a procedure-to-operation chain. A signed procedure or completed training record does not prove effective supervision.
4. **Check cyber and fraud handoffs.** Define approved synthetic scenarios for suspicious account access, changed contact details, provider outage and suspected data exposure. Record detection, routing, human decision and observed action separately. Output a scenario matrix; generated alerts are not proof that an authorized person received or acted on them.
5. **Reconcile incident timelines.** Preserve event, detection, awareness, escalation and action times with source and timezone. Have the authorized owner evaluate each applicable reporting trigger and clock separately. Output a decision register; an internal case being closed does not establish that external obligations were met.
6. **Challenge provider dependencies.** Match provider evidence to actual service, period and responsibilities. Identify firm-side controls and missing subcontractor or downstream information. Output open dependencies; outsourcing does not make evidence gaps disappear.
7. **Correct and retest.** Assign failures a cause, owner, action and predefined closure criterion. Verify changed behavior on the relevant branch/system/version. Output before/after evidence while preserving the original failure and any continuing customer impact.
8. **Prepare supervisory review.** Reconcile all in-scope checks and open actions, including untested branches and unavailable records. Link each narrative claim to its evidence and limitation. Output a draft for compliance and independent review; do not describe the packet as FINRA approval.

## Evidence and test plan

### Firm scope and supervisory procedures

Compliance, legal and supervisory owners provide the business/activity inventory, applicability decisions, procedure versions, branch and affiliate boundaries, supervisor assignments and exceptions. Reconcile every in-scope activity to its responsible supervisor, operating owner and escalation route. Record missing coverage explicitly. An affiliate's policy does not establish that the member firm's process is covered.

Compare the procedure effective at the observation date with the actual role and workflow configuration. Preserve historical versions when reviewing past events. A later procedure correction does not retroactively establish that an earlier review occurred. If a role changed during the period, check the handover and alternate coverage rather than treating the latest roster as evidence for the whole period.

### Cybersecurity operations and escalation

Security, technology and operations owners provide the full in-scope populations of access reviews, changes, events, provider issues and training assignments. Reconcile source counts, time boundaries and exclusions before evaluating completeness. Preserve failed queries and inaccessible branches. A report with zero exceptions does not prove all relevant records were inspected.

For each assessed event, link the source observation, alert, receiving role, decision, action and follow-up. Distinguish the event timestamp from ingestion and case-creation times. Record clock uncertainty instead of silently ordering events by whichever timestamp is available. Keep evidence of detection separate from escalation receipt and authorized response.

For access reviews, compare the approved population with actual accounts and privileges, including leavers and service accounts where in scope. Verify removal or correction through a fresh authorized observation; a removal ticket is not proof that access ended. For training, reconcile assigned and completed populations but do not infer operational competence solely from completion records.

### Representations, issues and oversight

Compliance and executive owners provide issue registers, remediation evidence, management reports, risk decisions and approved customer/public statements. Trace each representation to evidence for the same entity, business scope and period. An assurance statement covering headquarters must not silently expand to unreviewed branches or providers.

Reconcile all open findings through disposition and retesting. Keep repeated symptoms linked to the earlier action so reviewers can distinguish a failed correction from an unrelated event. Management acknowledgement does not itself establish risk acceptance; preserve the actual decision, owner and conditions. For any regulatory communication, separate prepared text, approval, submission and receipt without inferring one from another.

## Failure branches and decisions

Unavailable logs or unperformed scenarios are `not_tested`; unresolved source or applicability conflicts are `inconclusive`. A known failed escalation against the approved criterion is `not_supported` even if the alert generator worked. Preserve these assertions separately and keep the affected workflow assigned to an owner.

Fictional desk case: QA detects a suspicious contact-detail change, but its alert routes to a departed supervisor's disabled mailbox and no alternate receives it. Detection is `supported`; required escalation is `not_supported`. No actual customer loss or regulatory reporting conclusion follows from this synthetic test. The agent records routing evidence and requests an authorized correction and retest.

## Cadence and renewal

Set reviews from applicable rules, approved supervisory procedures and risk decisions; do not invent a universal quarterly or annual cybersecurity review obligation. Reassess after business, branch, provider, threat, system or source changes and after consequential incidents or failed tests. Record the next review owner and trigger.

## Completion and handoff

Deliver the source/applicability map, complete scope and evidence registers, procedure-to-operation chains, scenario results, incident decision references and open-action register. Name all untested branches, missing periods, unresolved provider dependencies and source-review gaps. Give each pending action an owner, deadline or review trigger and the evidence needed for closure.

Independent source, skeptical and rights review are required before publication. Qualified firm owners retain legal interpretation, risk acceptance, customer communications and regulatory filings. Keep the packet labelled draft until its applicable reviews are complete. No real firm compliance, incident reportability or supervisory approval has been established by this guide.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
