# CISA BOD 23-02 management-interface engagement guide

> Original operational guidance, not Binding Operational Directive text, a scope determination, an exposure decision, a production-change authorization, or a compliance claim. Confirm current material through [CISA BOD 23-02](https://www.cisa.gov/news-events/directives) and applicable agency, component, system-owner, and authority direction.

## Engagement focus

For applicable Federal Civilian Executive Branch environments, maintain a governed program for identifying and reducing risk from internet-exposed networked management interfaces. Connect interface inventories to ownership, exposure assessment, approved access architecture, protective measures, validation evidence, exceptions, remediation, and reporting records. Preserve the boundary between an observed interface and a decision to remove exposure, change access design, or approve an alternative protection.

## Roles

Assign accountable agency or component executive, network, platform, cloud, security, zero-trust, system-owner, change-management, risk, and supplier-management roles. Operators maintain interface inventories, exposure and scope records, access-architecture evidence, protection and validation records, exception approvals, remediation plans, reporting artifacts, supplier evidence, and closure status. Review material interface populations, exposure findings, protection assumptions, and exceptions quarterly; reassess after material network, cloud, system, supplier, or access-architecture changes. Before annual renewal, an independent reviewer samples interface records through validated treatment; auditors test the evidence trail without deciding scope, authorizing production changes, accepting risk, or attesting for management.

AI may organize supplied inventory and treatment evidence, flag stale validation or missing ownership, relate interfaces to recorded services, and draft workpapers for human review. AI cannot scan or alter systems without authorization, determine exposure disposition, authorize access architecture, approve an exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.

## Source and applicability

CISA's [official announcement](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/35fc39d) describes removal of covered public management interfaces or qualifying zero-trust access protection within 14 days of discovery. Its [public implementation issue](https://github.com/cisagov/cyhy-system/issues/89) identifies a policy enforcement point separate from the interface. A product marketed as zero trust, or the interface's own login prompt, is not evidence that this condition is met. Verify the full directive, implementation guidance, exact scope, trigger and current agency reporting instructions before final conclusions; direct directive retrieval was unavailable during drafting.

## Before starting

Apply the [agent runbook](../agent-runbook.md). Obtain interface and service inventories, exposure observations, CISA notices, discovery timestamps, access diagrams, provider responsibilities and change authority. Reuse valid authorization. Identify a tested administrative recovery path before proposing a change that could lock operators out.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Resolve source and scope | Agency/security owners verify covered interfaces and current direction. | Source-pinned scope decisions; unclear applicability assigned to authority rather than assumed excluded. |
| 2. Reconcile interfaces | Network/cloud owners compare management endpoints, addresses, ports, gateways and provider inventories. | Full declared population with owners, path evidence and timestamps. A service inventory alone does not identify every administrative path. |
| 3. Register exposure and clock | Qualified reviewer checks observations and notification/discovery evidence against source criteria. | Finding, trigger evidence and due date; ticket reassignment cannot reset age. Unknown reachability remains unassessed. |
| 4. Choose treatment | Architecture and service owners decide removal of public exposure or source-conforming protection. | Approved design showing enforcement location, identity/access policy, dependencies and administrative recovery. Marketing claims do not substitute for design evidence. |
| 5. Implement safely | Authorized operators validate in approved QA, then follow approved production change control. | Change receipt, recovery readiness and actual affected paths. Failed access checks stop expansion and invoke the recovery plan. |
| 6. Verify independently | Reviewer checks the intended public-path restriction and authorized administrator access using approved methods. | Dated readback and bypass-path checks within scope; saved configuration alone cannot close exposure. |
| 7. Escalate and report | Agency/risk owner resolves late or failed treatment under current direction; reporting owner prepares evidence. | Owned open actions, required decisions and actual submission receipts. An internal exception does not automatically waive directive duties. |
| 8. Renew coverage | Independent reviewer reconciles scope, findings and changes. | Handoff with unresolved paths, owners and next review triggers. |

## Evidence and test plan

**Source and rights snapshot.** Use the official [CISA cybersecurity directives index](https://www.cisa.gov/news-events/directives) to confirm current BOD 23-02 material together with applicable agency/component direction; prior locator snapshot 2026-07-31; detailed current-source review pending. This is original evidence-planning guidance, not directive text, an exposure decision, or a federal compliance conclusion.

### 1. Management-interface population and ownership package

- **Request and owner:** Network, cloud, platform, and system owners provide the approved interface population, asset/service links, interface purpose, reachable-path records, accountable owners, scope decisions, and dated inventory reconciliation.
- **Validate and limit:** Trace a selected recorded management interface from inventory through linked service, owner, approved scope rationale, and last validation. This cannot discover interfaces, establish complete population coverage, or decide whether an interface is internet-exposed.
- **AI and trigger:** AI may reconcile supplied records and flag an unowned interface, stale validation, or conflicting service link. Authorized humans determine scope and exposure characterization. Refresh after network, identity, cloud, service, or ownership change.

### 2. Access architecture and protective-treatment package

- **Request and owner:** Security, identity, network, platform, and change owners provide approved access-pattern records, authentication/authorization evidence, segmentation or gateway records, configuration/change references, treatment plans, exceptions, and supplier responsibilities.
- **Validate and limit:** Sample one interface from documented access design through approved implementation/change record, protection evidence, exception if any, and accountable treatment status. This does not authorize an access method, validate every configuration, or approve an alternative safeguard.
- **AI and trigger:** AI may identify missing approval references, expired exceptions, or absent owner attestations. Humans authorize architecture and production changes, approve exceptions, and accept residual risk. Refresh after access-design change, failed control check, exception expiry, or supplier change.

### 3. Validation, escalation, and reporting package

- **Request and owner:** Program, security-operations, risk, reporting, and independent-review owners provide authorized validation records, issue/remediation tickets, retest evidence, escalation decisions, report lineage, limitations, and follow-up actions.
- **Validate and limit:** Trace a selected finding or reported measure from source record through interface linkage, owner assignment, treatment/retest, escalation where applicable, and current status. This cannot certify protection effectiveness, submit a federal report, or attest for management.
- **AI and trigger:** AI may prepare lineage workpapers and flag overdue retests or incomplete report provenance. Authorized humans approve reports, closure, risk decisions, and external representations. Refresh before reporting, after failed validation or a material exposure change, and during annual independent review.


## Failure branches and decisions

Retain all declared interfaces and collection gaps. Any approved inspection selection must state limits and cannot prove unexamined coverage. Never trim, sample or cap evidence passed to an assessment scorer. If a proxy protects one hostname but another authorized observation shows a direct path, keep the finding open. A timeout alone does not prove exposure removal; reconcile service health and test conditions. If access is lost, follow approved recovery and escalate. Missing provider evidence remains a responsibility gap. Preserve source versions, original trigger dates and next safe action on interruption.

## Cadence and renewal

The deadline discussed above is an operational requirement to verify against current direction; quarterly coordination and annual review do not replace it. Recheck affected paths after address, gateway, identity, cloud, provider or access-policy changes. Track active findings through closure and escalate threatened deadlines promptly.

## Completion and handoff

Deliver source/scope decisions, complete interface register, trigger dates, approved architecture, changes, independent path/access observations, unresolved gaps and reporting receipts. Distinguish protected-path evidence from a universal security claim. Independent source and skeptical review and named human approval remain required before final conclusions.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
