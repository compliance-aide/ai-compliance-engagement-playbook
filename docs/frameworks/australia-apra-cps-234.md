# APRA CPS 234 — information-security engagement guide

> Original operational guidance, not APRA text, legal advice, a notification
> decision or a prudential compliance conclusion.

## Source and applicability

Use [APRA CPS 234](https://www.apra.gov.au/standards/cps-234), checked 2026-09-04.
Confirm the applicable entity/group boundary, source version and related-party
or third-party information assets with regulatory counsel. Keep CPS 234 security
work distinct from CPS 230's wider operational-risk work; coordinate overlaps
through the responsible reporting authority.

Rights: original instructions and official links only, no copied requirements,
assessment procedures or sensitive evidence. See the
[author review](../refresh-reviews/australia-apra-cps-234.md). Independent review
and publication approval remain pending.

## Engagement focus

Connect information-asset context and approved classifications to actual
safeguards, assurance coverage, observed weaknesses and accountable decisions.
Retain evidence of what was tested and what was unavailable, including assets
managed by others. A supplier assurance report is an input, not automatic coverage.

## Roles

Board/management retain accountable security decisions. Information owners approve
classification; security/technology owners operate safeguards and response;
provider owners obtain evidence. Internal audit independently evaluates assurance
within its role; regulatory counsel resolves notification. AI may organize
metadata and execute approved read-only checks. It cannot classify assets,
determine materiality, accept risk, direct a live incident or notify APRA.

## Before starting

Obtain entity scope, asset/provider inventory, approved sensitivity/criticality,
security responsibilities, current test program, incident/reporting rules,
remediation backlog and evidence permissions. Missing classifications go to the
information owner; do not silently assign low impact. Use the
[agent runbook](../agent-runbook.md).

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Reconcile assets and responsibility | Information/technology owners match assets to systems, providers, business purpose and approved classification. | Scope register with owner and evidence custodian; unmanaged or unclassified assets remain gaps. |
| 2. Plan assurance coverage | Security and independent reviewers relate safeguards to asset risks, methods, periods and provider evidence. | Approved test plan identifies both coverage and unavailable assurance. |
| 3. Collect operating records | AI gathers permitted configuration, monitoring, vulnerability and incident references; custodians confirm provenance. | Evidence index matches the asset, version and period; errors and omissions are explicit. |
| 4. Test and challenge | Authorized testers perform the approved checks; reviewers challenge design and operating claims and proposed reliance on supplier reports. | Workpapers include actual results, adverse evidence and reliance limits. |
| 5. Triage incident or weakness | Security preserves facts; counsel/reporting authority evaluates the relevant route, trigger and timing. | Separate incident/weakness decision records; no automatic closure from a severity label. |
| 6. Correct and retest | Owners implement approved actions; reviewer rechecks affected safeguards in the intended environment. | Retest receipts and accountable disposition; changed documentation alone is insufficient. |
| 7. Review the program | Management and internal audit review coverage, open weaknesses, capability and changes. | Decisions, resourcing, next tests and unresolved assurance gaps stay visible. |

This is an original evidence-work sequence, not a substituted prudential method.

## Evidence and test plan

| Request and custodian | Check | Expected observation | Failure or limit |
| --- | --- | --- | --- |
| Asset/provider register from information owners | Trace a selected asset to classification decision, custodian and relevant safeguards. | Same asset and scope appear throughout. | An outsourced asset is not automatically outside the boundary. |
| Safeguard evidence from security/technology | Compare approved expectations with actual time-bounded observations and raw references. | Observation supports the narrow assertion under the approved method. | A scanner pass cannot establish all control effectiveness. |
| External assurance from provider owner/internal audit | Compare report period, service, exclusions and intended reliance with the in-scope asset. | Reliance rationale and gaps are explicit. | A report for another service or old period leaves coverage inconclusive. |
| Incident/weakness trail from security and counsel | Trace awareness time, impact inputs, decision, prompt escalation and action/retest. | The relevant route and clock are recorded with authority. | An open remediation ticket does not remove a reporting question. |

## Failure branches and decisions

Preserve conflicting classification or test records and route them to the owner.
If a provider cannot supply evidence, identify the affected assurance claim and
alternative review action; do not label the absence low risk. Separate a security
incident from a material control weakness expected not to be remediated promptly.
A customer-impact hypothesis remains a hypothesis until investigated, but it must
not delay escalation. Never suppress a negative test to achieve a desired result.

## Cadence and renewal

APRA's cited notification section distinguishes an incident route with a 72-hour
outer limit from a material-weakness route with a 10-business-day outer limit;
both require reporting as soon as possible when their conditions apply. The
incident route also addresses notification to other regulators. Counsel records
the exact triggers and clock calculation; AI escalates promptly and does not
wait for proof of financial loss. Set risk-based testing/review frequency in the
approved program; quarterly working reviews are only a planning default. Reopen
affected records after incidents, asset/provider changes and new threats.

## Completion and handoff

Deliver asset responsibility/classification references, assurance plan and coverage,
protected evidence, workpapers, decision trails, corrections/retests and next
reviews. State untested assets, external reliance limits and unresolved reporting
questions. A complete packet is not an APRA compliance conclusion.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md).
