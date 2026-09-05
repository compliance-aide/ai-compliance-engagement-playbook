# EU payment-services transition — engagement guide

> Original operational guidance, not EU or member-state legal advice. Track current law at [EUR-Lex PSD2](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015L2366) and verify replacement-act publication.

## Engagement focus

Maintain applicability by entity/service/state, current-law evidence, future-readiness assumptions, fraud, authentication, communications, incident, supplier, open-banking, and transition records.

## Transition decision sequence

Use the [agent runbook](../agent-runbook.md). The following is an original
execution recommendation; legal/compliance owns the applicable-law decisions.
Maintain separate records for current operation and future readiness.

**Source checkpoint, 2026-09-04:** the [Council state-of-play note dated
9 June 2026](https://data.consilium.europa.eu/doc/document/ST-9814-2026-INIT/en/pdf),
page 3, records provisional agreement on PSD3 and PSR on 27 November 2025 and
COREPER confirmation on 22 April 2026. These are verified historical milestones,
not proof of final publication or present applicability. Current adoption,
Official Journal publication, entry into force, application and national
transposition dates remain unverified in this pass. Do not calculate a binding
cutover date from this note or describe its June status as confirmed September status.

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

**Failure branches:** absent official publication evidence leaves the proposed
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

## Roles and annual rhythm

Operators maintain service and country evidence; independent reviewers test approved interpretations and readiness. AI monitors official changes and flags assumptions, but cannot interpret law, declare future rules effective, approve payment changes, or submit filings. Review quarterly and annually.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
