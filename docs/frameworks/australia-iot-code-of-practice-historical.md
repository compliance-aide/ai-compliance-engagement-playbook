# Australia historical IoT guidance — engagement guide

> Original operational guidance, not government code text, product certification
> or a legal compliance conclusion.

## Source and applicability

The [ASD manufacturer page](https://www.cyber.gov.au/business-government/secure-design/secure-by-design/iot-secure-by-design-guidance-for-manufacturers),
checked 2026-09-04, is titled IoT Secure by Design guidance for manufacturers,
updated September 2023 and first published September 2020. It supports AS ETSI
EN 303 645 and focuses on devices rather than associated backend servers. Do not
label that current page as the exact historical Code of Practice without checking
the engagement's actual reference and edition.

Use this guide for a specifically identified historical or voluntary engagement.
Separately resolve [current smart-device duties](australia-smart-devices-rules-2025.md).
An old voluntary claim cannot establish current statutory compliance. Obtain lawful
access to any referenced standard needed for the assessment; do not reconstruct it.
See the [author record](../refresh-reviews/australia-iot-code-of-practice-historical.md).

## Engagement focus

Build a traceable product-lifecycle packet: which device and software were examined,
against which source, what was observed, and which claims the evidence supports.
Keep associated services visible as dependencies with separately approved scope.

## Roles

Product owns identity and support commitments; engineering owns implementation;
security owns test methods and vulnerability handling; privacy owns data decisions.
Legal and authorised product leadership decide applicability and external claims.
Independent reviewers challenge evidence. AI may reconcile permitted records and
draft workpapers, but cannot certify safety, approve release or accept risk.

## Before starting

Obtain the exact requested source/edition, product/model and firmware inventory,
support dates, dependency map, design and update records, approved test population,
QA devices and evidence permissions. If the historical source is missing, inventory
work may continue but source-alignment conclusions remain pending. Follow the
[agent runbook](../agent-runbook.md) and save one work item per bounded claim.

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Pin the reference | Product/legal resolve the historical request and current obligations separately. | Dated source and scope decision; unresolved edition is explicit. |
| 2. Reconcile products | AI compares supplied model, hardware, firmware, interfaces and supplier records. Product resolves differences. | Versioned population and dependency register; no unexplained exclusions. |
| 3. Plan verification | Security maps each scoped claim to evidence, method, QA device and expected observation. | Approved coverage plan with limitations and safety constraints. |
| 4. Observe lifecycle behavior | Authorised operators exercise approved setup, update, recovery and data-handling cases. | Actual outputs and product versions retained; policy promises remain separate. |
| 5. Trace vulnerability handling | Support/security follow an approved fictional report through triage, engineering disposition and customer-impact review. | Owned trail and observed response route, without sending to outside parties. |
| 6. Correct and retest | Engineering performs approved fixes; reviewer repeats affected checks. | Finding/change/retest links and remaining gaps. |
| 7. Review representations | Product/legal compare proposed wording with exact source, version and observed coverage. | Reviewed draft and named claim owner; no implied certification. |

## Evidence and test plan

| Evidence and custodian | Check | Expected observation | Failure or limit |
| --- | --- | --- | --- |
| Product/source register, product owner | Match each work item to hardware, firmware and source edition. | Reproducible context. | Unknown edition prevents source-alignment judgment. |
| QA update receipts, engineering | Compare installed version before/after an approved update and its verification result. | Observed state matches the intended artifact. | A release note alone does not prove installation. |
| Vulnerability/support records, support | Follow a fictional case and reconcile published support date with internal ownership. | Case reaches an accountable owner; commitments agree. | A mailbox address alone does not prove handling. |
| Proposed claim, legal/product | Trace wording to evidence and exclusions. | Wording stays within tested product/version and source. | Historical evidence cannot support a new legal claim. |

## Failure branches and decisions

Missing supplier evidence stays a gap. Conflicting firmware IDs require inventory
repair before tests can be compared. Unexpected device behavior stops the affected
QA procedure for the safety owner; retain the adverse observation. Do not test
customer devices or production services under a documentation task. If interrupted,
resume from the recorded device state and verify it before repeating an update.

## Cadence and renewal

Review before reusing historical claims and after firmware, supplier, service,
market or support changes. Quarterly product housekeeping and annual governance
review are planning defaults, not statutory deadlines. Preserve old evidence and
source labels when preparing a new edition comparison.

## Completion and handoff

Deliver the source/product register, coverage plan, protected evidence index,
observations, corrections/retests and reviewed claim draft. Name untested variants,
missing historical material and separate current-law work. Independent review and
named human publication approval remain pending for this guide.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md).
