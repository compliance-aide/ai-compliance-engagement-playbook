# California connected-device security — engagement guide

> Original operational guidance, not California legal advice or a compliance claim.

## Source and applicability

Use [Civil Code 1798.91.04](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.91.04.),
checked 2026-09-04. The retrieved section includes the AB 2392 amendment effective
January 2023 and references a similar parallel section. Counsel must resolve the
applicable chapter text, definitions, exclusions and manufacturer role before a
legal conclusion. A historical SB 327 bill comparison alone is insufficient.

Security features must address device function and information. The authentication
provision is conditional and remains subject to the broader requirements; a unique
password alone is not a universal compliance conclusion. The retrieved text also
provides a conditional NIST-conforming labelling route. Do not infer eligibility
from a generic certificate or logo. See the
[author record](../refresh-reviews/california-sb-327-connected-devices.md).

## Engagement focus

Connect each device/version to its intended function, data, security decisions,
actual QA observations and post-release handling. Keep legal sufficiency separate
from technical test results and approved product claims.

## Roles

Product owns models and intended use; engineering owns implementation; security
owns test methods and vulnerability handling; suppliers supply component facts.
Counsel decides scope and legal routes; authorised leadership approves release and
claims. Independent reviewers challenge evidence. AI may reconcile records and
draft workpapers, but cannot decide safety, legal applicability or release readiness.

## Before starting

Obtain product/hardware/firmware inventory, connectivity and data flows, manufacturer
role, California market facts, approved legal scope, security design, supplier
records and QA devices. Define test authority and abort conditions. Use the
[agent runbook](../agent-runbook.md); never test real customer devices by default.

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Resolve scope | Product/legal identify role, product and applicable statutory route. | Dated decision with unresolved definitions/exclusions. |
| 2. Map function and data | Engineering/product identify interfaces, information, services and dependencies. | Versioned device map with owners and unknowns. |
| 3. Plan security verification | Security defines approved claims, QA cases and expected observations from the design and legal criteria. | Coverage plan addresses more than passwords alone. |
| 4. Observe device behavior | Authorised QA operators test the identified version and preserve actual results. | Expected/observed comparison and limits, including relevant authentication states. |
| 5. Review release evidence | Product/legal/security reconcile failures, supplier assurance and proposed claims. | Exact release decision or pending items; test success is not legal approval. |
| 6. Handle vulnerabilities | Owners trace reports to affected versions, approved fixes and retest. | Finding/change/retest chain with customer-impact decisions. |
| 7. Renew | Product reviews material changes and updates evidence and claims through the approved route. | Current versioned packet and next queue. |

## Evidence and test plan

| Evidence and custodian | Check | Expected observation | Failure or limit |
| --- | --- | --- | --- |
| Product/scope record, legal/product | Match manufacturer role and device version to the decision. | Factual scope is traceable. | A reseller label alone cannot settle statutory role. |
| Design/QA evidence, engineering | Compare intended function and data protection with actual behavior. | Results identify tested states and interfaces. | Password testing alone cannot prove broad security sufficiency. |
| Claimed conformity route, legal/assurance | Trace all applicable conditions to current authorised evidence. | Each claimed condition has support. | A logo alone proves no qualifying route. |
| Vulnerability/update trail, security | Match affected version to approved correction and observed retest. | Original issue is addressed in the tested version. | Published release notes do not prove every device updated. |

## Failure branches and decisions

Missing supplier facts remain gaps. Conflicting firmware IDs require inventory
repair before comparison. Unexpected device effects stop the affected QA test under
its safety rules. Unresolved vulnerabilities require explicit product decisions;
AI cannot erase findings to enable release. After interruption verify actual device
state before repeating updates. Source ambiguity blocks the affected legal claim.

## Cadence and renewal

Review before releases and after material firmware, interface, supplier, data or
legal changes. Quarterly supported-product review is a planning default, not a
statutory timer. Preserve prior evidence and decisions when the product changes.

## Completion and handoff

Deliver scope, product/data map, verification plan, QA observations, release/claim
decisions, findings/retests and next queue. Name untested variants and unresolved
legal scope. Independent source, engagement and skeptical review and named human
publication approval remain pending. Original prose and links only; no statutory
text, proprietary design details or customer evidence reproduced.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md).
