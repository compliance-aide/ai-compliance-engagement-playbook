# FATF Recommendations — engagement context guide

> Original operational guidance, not FATF text or a firm-level legal conclusion. Check the [FATF Recommendations](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html) and national law.

## Source and applicability

Use the [agent runbook](../agent-runbook.md). Source checkpoint, 2026-09-04:
the official FATF Recommendations page's indexed text describes international
standards implemented through country-specific measures, with Interpretive Notes
and Glossary forming part of the standards. Full current standards, amendments,
national law and supervisory guidance remain unverified in this pass. Do not
convert a recommendation number directly into a firm-level legal obligation.


## Engagement focus

Maintain jurisdiction, entity, product, channel, country, sector, customer-risk, local-obligation, alert/case, and remediation evidence.

## Before starting

Define the complete approved entity/product/channel population, review period,
local-law mapping owner and evidence-access boundary. Record test criteria and
individual assertions in [work items](../../templates/work-item.md). Separate
source completeness, configured logic, observed routing and authorized case
outcomes. None is a substitute for the others.

Keep customer information, confidential reporting decisions and investigation
records in their approved restricted locations. Use synthetic events and identities
in QA-named workspaces for demonstrations. The scope must identify what the
method can observe, including unavailable feeds and unreviewed local sources.

## Ordered workflow


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

## Failure branches and decisions

 absent local-law mapping leaves the legal-duty assertion
`inconclusive`. An inaccessible source feed means its ingestion test is
`not_tested`; known lost events make complete ingestion `not_supported`. Neither
outcome determines whether a specific customer committed a crime.

**Fictional desk case:** a synthetic source file contains 100 events; monitoring
receives 80 and generates no alerts. Reconciliation contradicts the approved
all-events-ingested criterion, so ingestion completeness is `not_supported`.
“No alerts” describes the observed output only; it cannot support “no suspicious
activity in all 100 events.” No actual customer or report is represented.

## Roles

Humans decide customer classification and suspicious-activity outcomes; independent reviewers test evidence. AI normalizes sources and gaps, but cannot report suspicion or make legal decisions. Use the approved review schedule and change triggers below.


## Evidence and test plan

Retain these three PR #340 packages with full in-scope coverage. Earlier review
does not approve the revised guide. Preserve complete evidence bound for scoring.

### 1. Jurisdiction, product, and risk-model package

- **Request and owner:** AML compliance, legal, product, and risk owners provide applicable-jurisdiction register, entity/product/channel/country scope, approved risk methodology, current risk factors, governance approvals, and local-obligation inventory.
- **Validate and limit:** Trace each in-scope product, channel, or jurisdiction entry to its local-law source reference, approved methodology/version, accountable owner, stated assumption, and review date. This cannot interpret local law, establish legal applicability, or set risk appetite.
- **AI and trigger:** AI may organize approved source references and flag stale jurisdiction or methodology versions. Humans decide applicability, methodology, and risk appetite. Refresh after new market/product/channel, legal change, or scheduled risk assessment.

### 2. Customer and transaction-monitoring operations package

- **Request and owner:** Operations, onboarding, investigations, data, and compliance owners provide approved customer-risk records, screening/monitoring governance, alert/case workflow, data-quality observations, disposition records, quality reviews, and corrective actions.
- **Validate and limit:** Trace each in-scope case or quality observation to its permitted source data, assigned owner, workflow timing, reviewer record, limitation, disposition authority, and remediation. This does not classify a customer, infer suspicion, or validate every alert outcome.
- **AI and trigger:** AI may surface missing case metadata, aging items, and inconsistent workflow records while preserving human review. Authorized humans make customer, alert, and case decisions. Refresh after material model/workflow/data change, quality finding, or case escalation.

### 3. Governance, escalation, and regulatory-reporting package

- **Request and owner:** Compliance leadership, legal, investigations, and designated reporting officers provide training/oversight records, escalation routes, decision logs, local reporting procedures, access controls, independent-test observations, and board or management review evidence.
- **Validate and limit:** Trace each in-scope escalation or governance decision to its source, named authority, timing, confidentiality handling, approval trail, and improvement action. This can show controlled process operation; it cannot determine suspicion, file a report, or disclose a case.
- **AI and trigger:** AI may flag overdue reviews, incomplete ownership, and missing evidence provenance. Designated humans decide escalation, reporting, and external communication; independent reviewers challenge evidence. Refresh after a regulatory change, material finding, reporting event, or annual review.

### Monitoring and decision traceability

For each approved test scenario, freeze the rule/model version, input fields,
expected signal, queue and owner. Compare actual field values after ingestion to
the source; equal record counts can conceal lost currency, country, ownership or
time information. Keep null values distinct from zero or an approved low-risk
classification. An imputed default needs a documented decision and test.

Separate the event date, ingestion date, alert date and review date. A rule that
operates on the wrong clock can produce a plausible but unsupported result.
Have the owner define the relevant window and time-zone treatment; do not invent
those criteria after observing the output.

Reconcile source events through cases using stable identifiers and retain retry,
rejection and duplicate handling. Preserve negative scenarios as well as expected
alerts. If tuning fixes a missed pattern, retest affected scenarios without
claiming a general accuracy rate from a few examples.

For customer ownership or risk records, distinguish documentary assertions,
verified facts, conflicts and unresolved chains. A completed field does not prove
its value was verified. Escalate unresolved material facts under the approved
local procedure; the agent cannot choose a customer outcome to clear a queue.

## Cadence and renewal

Recheck after changes in local sources, products, geography, channels, customer
risk, ownership information, monitoring logic or data feeds. Use the approved
operating schedule and actual local deadlines instead of an invented universal
quarterly/annual requirement. Reopen affected mappings and tests when sources or
configurations change; do not treat unchanged documentation as unchanged risk.

## Completion and handoff

Deliver the source/local-duty map, approved population and risk methodology,
evidence index, input-to-case reconciliation, authorized decisions, test results,
blind spots and remediation/retest records. Every unresolved feed, mapping or
case handoff needs an owner and next action. Keep any confidential reporting
material separately controlled and reference only what the recipient may access.

State whether the result is a context map, readiness review or observed operating
test. Do not label it FATF certification or use a country's evaluation as proof
of one firm's compliance. Independent source, skeptical, rights, publication and
cross-model reviews remain pending; structural checks do not establish them.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
