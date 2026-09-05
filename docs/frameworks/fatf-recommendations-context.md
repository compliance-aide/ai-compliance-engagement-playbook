# FATF Recommendations — engagement context guide

> Original operational guidance, not FATF text or a firm-level legal conclusion. Check the [FATF Recommendations](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html) and national law.

## Engagement focus

Maintain jurisdiction, entity, product, channel, country, sector, customer-risk, local-obligation, alert/case, and remediation evidence.

## International-standard to local-duty workflow

Use the [agent runbook](../agent-runbook.md). Source checkpoint, 2026-09-04:
the official FATF Recommendations page's indexed text describes international
standards implemented through country-specific measures, with Interpretive Notes
and Glossary forming part of the standards. Full current standards, amendments,
national law and supervisory guidance remain unverified in this pass. Do not
convert a recommendation number directly into a firm-level legal obligation.

1. Record each legal entity, jurisdiction, license/registration, activity, product
   and customer/channel population. Legal/compliance determines which local AML,
   counter-terrorist-financing and other relevant duties apply. Keep unresolved
   scope questions owned rather than defaulting to “not applicable.”
2. Link each relevant international topic to the actual local source, effective
   date, regulated role and approved interpretation. Distinguish national-level
   institutional measures from operating duties assigned to a firm. Record gaps
   where no verified local mapping exists; do not invent a retention period,
   reporting threshold or filing deadline from a generic global checklist.
3. Build the approved risk-and-control map using actual products, customers,
   geography, channels and delivery arrangements. Record evidence and rationale
   behind each approved risk treatment. Do not replace individual facts with a
   blanket adverse decision based solely on country or group membership.
4. Trace authorized customer/due-diligence records to identification, ownership
   questions, verification evidence, review decisions and unresolved information.
   Keep missing evidence distinct from a confirmed adverse fact. Humans decide
   acceptance, escalation and consequential treatment under the approved program.
5. Reconcile the full in-scope event population to monitoring inputs, generated
   alerts, assigned cases and dispositions. A queue with no alerts cannot show
   that all source events reached monitoring. Preserve ingestion failures,
   excluded fields, duplicates and unmatched records for owner review.
6. Test approved scenarios with synthetic identities and transactions in QA-named
   workspaces. Define expected input, signal, routing and response evidence in
   advance. Do not initiate actual transactions, freeze assets, contact customers
   or submit suspicion reports during this guide-development task.
7. For case review, separate observed facts, inferred patterns and unresolved
   questions. Route suspicious-activity decisions and confidential reporting to
   the named authorized officer. Do not disclose case content to the subject or
   unauthorized recipients; legal owns applicable confidentiality restrictions.
8. Track source/program changes to affected controls, data fields, procedures and
   training. Verify implementation and retest the affected paths. A revised risk
   policy does not prove a screening or monitoring configuration changed.
9. Hand off the complete mapping, evidence index, test results, case-coverage gaps,
   decisions and remediation owners. Keep jurisdiction-level evaluation context
   separate from any claim about one organization's compliance or effectiveness.

**Failure branches:** absent local-law mapping leaves the legal-duty assertion
`inconclusive`. An inaccessible source feed means its ingestion test is
`not_tested`; known lost events make complete ingestion `not_supported`. Neither
outcome determines whether a specific customer committed a crime.

**Fictional desk case:** a synthetic source file contains 100 events; monitoring
receives 80 and generates no alerts. Reconciliation contradicts the approved
all-events-ingested criterion, so ingestion completeness is `not_supported`.
“No alerts” describes the observed output only; it cannot support “no suspicious
activity in all 100 events.” No actual customer or report is represented.

## Roles and annual rhythm

Humans decide customer classification and suspicious-activity outcomes; independent reviewers test evidence. AI normalizes sources and gaps, but cannot report suspicion or make legal decisions. Review quarterly and annually.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
