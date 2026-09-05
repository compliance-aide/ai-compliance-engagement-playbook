# CISA Trusted Internet Connections 3.0 — engagement guide

> Original operational guidance, not CISA content or a federal architecture authorization. Confirm current material through the [CISA TIC 3.0 program guidebook](https://www.cisa.gov/sites/default/files/publications/CISA%2520TIC%25203.0%2520Program%2520Guidebook%2520v1.1.pdf).

## Engagement focus

Maintain agency scope, network and service inventory, traffic and trust-boundary decisions, architecture evidence, cloud and remote-work dependencies, exceptions, testing results, and improvement records.

## Roles

Federal architecture, security, and system owners authorize design and operation decisions; independent assessors test evidence. AI maps approved artifacts and flags drift, but cannot configure connectivity, approve architecture, or authorize operation. Review changes continuously and annually.

## Source and applicability

Use CISA's [TIC collaboration repository](https://github.com/cisagov/tic3.0/) to locate the official document repository, then pin the program guidebook, reference architecture, security capabilities catalog and relevant use cases. These documents have separate versions; “TIC 3.0” does not establish that an old catalog is current. CISA's [cloud-use-case announcement](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/355af13) illustrates how use cases and catalog revisions connect. Detailed current bundle and agency direction remain to be reviewed. A vendor overlay is supporting evidence, not federal authorization.

## Before starting

Apply the [agent runbook](../agent-runbook.md). Obtain agency scope, service/traffic inventory, current diagrams, trust-boundary decisions, applicable use cases, provider responsibilities and testing authority. Reuse valid read-only authorization. Map actual remote-user, branch, cloud and shared-service paths where present rather than assuming all traffic follows one perimeter.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Pin scope and sources | Agency architecture/security owners confirm applicable policy and document versions. | Source/use-case register with unresolved interpretations and authority owners. |
| 2. Reconcile traffic paths | Network/cloud/service owners map sources, destinations, trust boundaries, routing and dependencies. | Full declared path inventory with owners; missing paths stay visible. |
| 3. Map capabilities | Architects relate required capabilities to enforcement and telemetry locations for each path. | Capability-to-path map with implementation owner and evidence need. Product ownership alone is not capability evidence. |
| 4. Check actual implementation | Authorized operators collect configuration and telemetry references; reviewers compare them with the design. | Dated observations and drift findings. Diagrammed routing is not observed routing. |
| 5. Plan corrections | Owners select authorized changes with dependencies, access continuity and rollback. | Approved work items and acceptance criteria; provider handoffs have named owners. |
| 6. Validate safely | Qualified operators test in approved QA and execute only authorized changes. | Results for intended paths, relevant alternate paths and service continuity; failed checks stop expansion. |
| 7. Independently retest | Reviewer compares resulting connectivity, enforcement and telemetry with criteria. | Closure evidence or open gaps. Traffic allowed correctly does not prove required telemetry arrived. |
| 8. Handoff and sustain | Agency lead reviews residual gaps, decisions and reporting requirements. | Source-linked packet, owners and change triggers; no architecture authorization inferred. |

## Evidence and test plan

**Source and rights snapshot.** Use the official [CISA TIC 3.0 Program Guidebook](https://www.cisa.gov/sites/default/files/publications/CISA%2520TIC%25203.0%2520Program%2520Guidebook%2520v1.1.pdf), current federal and agency/component direction, and authorized source material; prior locator snapshot 2026-07-31; current source bundle review pending. This is original evidence-planning guidance, not reproduced TIC text, an architecture authorization, an applicability decision, or a federal compliance conclusion. Designated federal authorities confirm scope and source-use boundaries.

### 1. Agency scope, service, and trust-boundary package

- **Request and owner:** Agency architecture, system, network, cloud, remote-work, and security owners provide approved service and traffic inventories, system/data-flow context, trust-boundary decisions, deployment models, owner roster, documented scope assumptions, and material-change records.
- **Validate and limit:** Trace a selected service or traffic path to an accountable owner, approved architecture or boundary record, dependency record, and review date. This supports a bounded architecture-evidence population; it cannot determine TIC applicability, approve a boundary, or prove every pathway is inventoried.
- **AI and trigger:** AI may reconcile approved inventories and flag unmatched owner, dependency, or review-date fields. Authorized humans determine scope, architecture, and boundary decisions. Refresh after material network, cloud, remote-access, supplier, system, or data-flow change.

### 2. Security-function and implementation-evidence package

- **Request and owner:** Network, security, platform, identity, cloud, and service owners provide approved design decisions, original implementation narratives, authorized configuration or validation outputs, traffic/security telemetry metadata, test records, change tickets, rollback evidence, and known limitations.
- **Validate and limit:** Sample one human-selected service path from design decision through time-bounded implementation and validation evidence, with owner, period, and recorded exception. This can support a reviewable evidence observation; it cannot independently establish effective protection, authorize connectivity, or alter production configuration.
- **AI and trigger:** AI may organize read-only evidence metadata, compare recorded service paths, and flag stale validation. Humans approve test methods, configuration changes, exceptions, and corrective-action closure. Recollect after material configuration, service, provider, routing, detection, or test-result change.

### 3. Exception, continuous-review, and assurance package

- **Request and owner:** Security governance and service owners provide exception requests, compensating-action records, monitoring and escalation evidence, approval/expiry records, remediation plans, retest evidence, source-change monitoring, and independent-assessor workpapers.
- **Validate and limit:** Trace a selected exception or significant monitoring signal from observation through owner assignment, authorized decision, compensating action, review date, and current status. This supports accountable oversight; it cannot accept risk, certify continuous operation, or make an authoritative federal report.
- **AI and trigger:** AI may flag expiring exceptions and assemble review packets. Humans approve risk treatment, external reporting, operation, and closure; independent assessors test evidence without configuring connectivity or authorizing designs. Refresh after a material alert, exception expiry, missed review, source update, and annual review.


## Failure branches and decisions

Conflicting use-case and catalog versions require source-owner reconciliation. Unsupported provider assertions remain unverified. Alternate routing that bypasses a required capability keeps the path open. Telemetry loss is distinct from connectivity failure. Failed access or continuity checks invoke approved recovery; do not widen access as an unapproved shortcut. Preserve full scorer-bound evidence without trimming, sampling or capping; approved inspection selections must state limits. On interruption, save source versions, verified paths, decisions and next safe action.

## Cadence and renewal

Review affected paths after routing, identity, cloud, provider, capability or source changes. Annual independent review is a management rhythm, not a substitute for change validation or agency-specific obligations. Assign telemetry and configuration-drift handling between reviews.

## Completion and handoff

Deliver source/use-case decisions, complete path inventory, capability map, implementation and telemetry evidence, tests/retests, exceptions and open dependencies. Independent source and skeptical review and named human approval remain necessary for final conclusions and authorization decisions.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
