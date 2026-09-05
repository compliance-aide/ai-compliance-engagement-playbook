# EU payment-services transition — engagement guide

> Original operational guidance, not EU or member-state legal advice. Track current law at [EUR-Lex PSD2](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015L2366) and verify replacement-act publication.

## Source and applicability

**Source checkpoint, 2026-09-04:** the [Council state-of-play note dated
9 June 2026](https://data.consilium.europa.eu/doc/document/ST-9814-2026-INIT/en/pdf),
page 3, records provisional agreement on PSD3 and PSR on 27 November 2025 and
COREPER confirmation on 22 April 2026. These are verified historical milestones,
not proof of final publication or present applicability. Current adoption,
Official Journal publication, entry into force, application and national
transposition dates remain unverified in this pass. Do not calculate a binding
cutover date from this note or describe its June status as confirmed September status.


Confirm the current PSD2/national-law baseline, applicable technical standards,
authorization conditions and other relevant payment rules with the legal owner.
This draft has not verified the full operative legal corpus. Link a separate
[DORA assessment](eu-dora.md) where applicable; do not infer that a payment-services
transition replaces operational-resilience or other independently applicable duties.

## Engagement focus

Maintain applicability by entity/service/state, current-law evidence, future-readiness assumptions, fraud, authentication, communications, incident, supplier, open-banking, and transition records.

## Roles

Legal/compliance owns entity/service applicability, authorization and transition
interpretation. Product and payment-operations owners define customer journeys
and reconcile operational results. Fraud/security owners investigate control
failures. Supplier owners verify external dependencies. Independent reviewers
challenge source and test conclusions; authorized leaders approve legal,
customer-treatment, release and reporting decisions. AI may organize approved
metadata and draft evidence comparisons, but cannot exercise those approvals.

## Before starting

Define the complete entity/service/country population, period, payment rails,
customer groups, third-party roles and dependencies. Record evidence access,
reviewers and the approved criteria in [work items](../../templates/work-item.md).
Keep current compliance testing and future readiness results distinct. Use only
QA-named environments with synthetic customers and transactions; keep actual
account numbers, credentials, customer cases and supplier secrets out of this repo.

Obtain the current approved journey specification before interpreting a test.
Define the expected status at each stage and which system is authoritative for
that observation. Without those criteria, an agent must not decide that an
accepted request means a completed or reversible transaction.

## Ordered workflow

Use the [agent runbook](../agent-runbook.md). The following is an original
execution recommendation; legal/compliance owns the applicable-law decisions.
Maintain separate records for current operation and future readiness.


1. Identify each entity, authorization, service and country. Link the current
   approved legal basis and control obligations to the payment-flow inventory.
   Record missing national or regulator sources as open questions with owners.
2. For every proposed change, record the specific obligation, official text
   version, legislative stage and affected flows. Keep announcement, political
   agreement, formal adoption, publication, entry into force, application and
   national implementation as separate fields, each supported by its own source.
3. Ask the legal owner to resolve the applicable transition conditions. Record
   what starts each period and which entity/service it covers. Unknown dates
   remain unknown; do not copy another country's or another provision's date.
4. Map each approved future requirement to implementation work, customer wording,
   supplier dependencies and tests. Keep the current obligation and its evidence
   linked until an authorized decision establishes its replacement. A successful
   future-readiness test does not suspend a current control.
5. Reconcile the complete population of affected journeys and exceptions. For
   authorized QA tests, define expected authentication, refusal, timeout, retry,
   consent/access and error behavior before execution. Use synthetic transactions
   and no real funds. Keep actual payment initiation or customer treatment outside
   this drafting authorization.
6. Compare observations with the approved criterion and retain failures. Test
   interface receipt, customer-visible status and the downstream record separately;
   an HTTP success or acceptance message does not establish completed payment.
   For a retry scenario, check duplicate handling against the approved design
   without assuming every payment rail offers the same reversal or finality rules.
7. Prepare the cutover packet with verified legal trigger, system/configuration
   version, complete test dispositions, outstanding defects, customer/support
   readiness and a reviewed recovery plan. Obtain the named legal and release
   approvals before operational change. Do not infer permission from a target date.
8. Verify the actual approved release and reconcile transition exceptions. Preserve
   the prior baseline and open customer/provider cases; a release does not prove
   every pre-existing transaction or complaint moved to the new process.

## Failure branches and decisions

 absent official publication evidence leaves the proposed
application-date assertion `inconclusive`. An unexecuted payment-path test is
`not_tested`. A known failure against an approved criterion is `not_supported`,
even if applicability of a different future rule remains uncertain. Record these
separately rather than replacing them with a single green readiness score.

**Fictional desk case:** an internal roadmap schedules a change for 1 December,
using the Council's provisional-agreement milestone as its sole legal source.
The date's legal applicability is `inconclusive`; the roadmap is evidence only
of an internal target. A QA interface accepts a retry twice when the approved
criterion permits only one transaction record. Duplicate handling is separately
`not_supported`. Neither uncertainty about legislation nor changing the roadmap
resolves the observed duplicate. No real payment or legal decision is represented.

## Evidence and test plan

The following packages retain PR #340's useful requests with full in-scope
coverage. Previous review of an earlier artifact does not approve this revision.

### 1. Service, entity, country, and transition assumption record

- **Request and owner:** Legal-entity/service/country register, authorization and agent/outsourcing inputs, product and payment-flow map, official-change watch, dated transition assumptions, and human approval log from legal, compliance, and product owners.
- **Validate and limit:** Trace each in-scope service or assumption to entity, country, owner, source reference, effective-date assumption, and decision record. This supports readiness evidence; it cannot decide whether a rule applies or is effective.
- **AI and trigger:** AI may reconcile approved registers and surface source changes. Humans approve interpretation and release decisions. Refresh for a country launch, service change, official publication, or regulator communication.

### 2. Customer, authentication, fraud, and open-banking operation

- **Request and owner:** Customer-communication versions, authentication/fraud-monitoring evidence, access-interface/change records, third-party-provider interaction logs, operational incidents, and corrective-action records from product, security, fraud, and operations owners.
- **Validate and limit:** Trace each in-scope payment journey or exception to its owner, dated operational record, escalation, and remediation. This supports process traceability; it cannot validate authentication adequacy, approve a customer treatment, or determine liability.
- **AI and trigger:** AI may index redacted operational records and flag failed controls or aging exceptions; it may not approve payment changes. Refresh after a fraud event, interface change, material provider issue, or control failure.

### 3. Incident, external engagement, and annual readiness review

- **Request and owner:** Incident timelines, regulatory and customer communication approvals, complaint/escalation records, provider oversight evidence, internal audit/review outputs, remediation/retest, and management transition decisions.
- **Validate and limit:** Trace each in-scope incident or transition decision to facts, owner, authority, approved communication, remediation, and review date. This supports accountability; it cannot decide reportability, make a submission, or declare compliance.
- **AI and trigger:** AI may assemble a redacted review packet and deadline warnings. Legal, compliance, and accountable leaders approve communications, filings, risk acceptance, and closure. Revisit at the approved operational cadence and after relevant change.


### Payment-journey reconciliation

This is an original test-design recommendation, not a prescribed legal test.
For each approved QA journey, record the initiating request identifier,
authentication/authorization outcome, interface acknowledgment, downstream record,
customer-visible status and exception disposition. Preserve event and observation
times separately. Trace aliases across systems so retries can be distinguished
from genuinely separate requests.

Have the owner identify the full set of approved success and failure scenarios.
Run only authorized tests; keep failed, blocked and not-run cases visible. For a
simulated lost response, inspect downstream state before retrying. Test the
approved duplicate-handling behavior and compare every related record, not only
the final screen. If authentication succeeds but the downstream action fails,
record both observations instead of a single successful-journey result.

Reconcile open complaints, exceptions and provider actions across any proposed
transition. Link each case to the process/version responsible for its next action.
Do not migrate a status label without its evidence, ownership and unresolved
customer outcome. Access to personal case content must follow the approved
restricted workflow; the public deliverable contains only non-sensitive references.

## Cadence and renewal

Use the approved operational review cadence and current legal/regulator deadlines;
do not invent a universal quarterly or annual requirement. Recheck sources after
formal legislative milestones and before relying on an application date. Reopen
journey tests after changes to authentication, fraud rules, interfaces, providers,
customer communications or downstream processing. Reconcile live incident and
complaint deadlines independently of scheduled reviews.

## Completion and handoff

Deliver the current/future obligation register, verified source versions,
entity/service/country decisions, complete journey/test matrix, controlled evidence
index, defects, retests and owned transition actions. Preserve unresolved legal
questions and missing operational observations. State whether the packet is a
readiness draft, observed test result or authorized acceptance record.

The next operator must be able to identify the approved current baseline, the
specific trigger for each proposed change and every case still using the prior
process. Record actual release/submission receipts only when those actions were
authorized and verified. Independent source, skeptical, rights and publication
reviews remain pending; structural checks do not prove legal accuracy or usable
execution across models.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
