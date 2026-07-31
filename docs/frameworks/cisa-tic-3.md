# CISA Trusted Internet Connections 3.0 — engagement guide

> Original operational guidance, not CISA content or a federal architecture authorization. Confirm current material through the [CISA TIC 3.0 program guidebook](https://www.cisa.gov/sites/default/files/publications/CISA%2520TIC%25203.0%2520Program%2520Guidebook%2520v1.1.pdf).

## Engagement focus

Maintain agency scope, network and service inventory, traffic and trust-boundary decisions, architecture evidence, cloud and remote-work dependencies, exceptions, testing results, and improvement records.

## Roles and annual rhythm

Federal architecture, security, and system owners authorize design and operation decisions; independent assessors test evidence. AI maps approved artifacts and flags drift, but cannot configure connectivity, approve architecture, or authorize operation. Review changes continuously and annually.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [CISA TIC 3.0 Program Guidebook](https://www.cisa.gov/sites/default/files/publications/CISA%2520TIC%25203.0%2520Program%2520Guidebook%2520v1.1.pdf), current federal and agency/component direction, and authorized source material; checked 2026-07-31. This is original evidence-planning guidance, not reproduced TIC text, an architecture authorization, an applicability decision, or a federal compliance conclusion. Designated federal authorities confirm scope and source-use boundaries.

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


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
