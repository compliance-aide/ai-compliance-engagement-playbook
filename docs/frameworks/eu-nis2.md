# EU NIS2 — engagement guide

> Author draft. Original operational guidance, not legal advice, entity designation,
> notification approval or a declaration of NIS2 compliance.

## Source and applicability

Use the [official directive](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng),
current national implementation and competent-authority instructions. Record
entity, country, sector/service, size/group facts, special inclusion or exclusion,
jurisdiction, registration and essential/important classification decisions.
Legal owns these decisions; an industry label or supplier questionnaire does not
settle applicability. Distinguish the EU baseline from the national rule actually
used for an entity, and document any sector-specific equivalent-law analysis.

Source check, 2026-09-04: read operative Articles 20, 21(1)–(3) and 23(3)–(4).
Article 20 addresses management approval, oversight and training. Article 21
sets risk-management expectations. Article 23 provides staged significant-incident
reporting: early warning within 24 hours and notification within 72 hours of
awareness, both without undue delay. The trust-service notification exception is
24 hours. Final reporting normally follows within one month after notification;
an ongoing incident uses a progress report and a final report within one month
of handling. Confirm exact national application and all conditions before use.

Also check [Implementing Regulation 2024/2690](https://eur-lex.europa.eu/eli/reg_impl/2024/2690/oj/eng)
for covered digital/service-provider categories. Its indexed official scope was
identified; its full requirements and significance tests were not read in this
pass. Full directive applicability, current amendments, national laws and authority
procedures still need scope-specific verification. Do not apply one provider's
thresholds across all sectors or treat a proposed amendment as adopted law.

## Engagement focus

Make an accountable chain from each entity/service to risk decisions, implemented
measures, tested behavior and incident readiness. Keep source obligations separate
from internal recommendations. A policy pack does not prove operational resilience;
a successful exercise does not establish every entity's compliance.

## Roles

Legal/compliance owns jurisdiction, applicable rules and reportability advice.
Management owns the required governance decisions. Service, security and supplier
owners provide operational evidence and execute authorized corrections. Incident
command maintains facts and escalation; authorized submitters handle external
reports after approval. Independent reviewers challenge evidence and conclusions.
AI may reconcile records, timeline events and draft packets. It cannot designate
an entity, accept risk, approve notification or represent a regulator's decision.

## Before starting

Follow the [agent runbook](../agent-runbook.md) and create
[work items](../../templates/work-item.md) with one observable assertion each.
Define entity/service populations, review period, source versions, evidence access,
approved criteria, reviewers and stop conditions. Use synthetic incidents in
QA-named workspaces; do not test through a real regulator reporting channel.
Keep personal, privileged, operational and supplier-sensitive records in their
approved repositories. Preserve the complete evidence corpus for scoring.

## Ordered workflow

1. **Resolve the entity/service register.** Reconcile legal entities, countries,
   services and acquisitions with the approved applicability decisions. Record
   source and date for each decision, including unresolved registration or authority
   questions. Continue authorized factual mapping while legal questions are open;
   do not turn uncertainty into an out-of-scope result.
2. **Map service dependencies.** Link each service to systems, locations, data,
   personnel, suppliers and alternative arrangements. Ask owners to reconcile
   missing dependencies against architecture and purchasing records. A completed
   list is not necessarily a complete estate.
3. **Build the obligation/evidence matrix.** Have the owner map all applicable
   EU, implementing and national requirements to controls, decision records and
   tests. Assign every item an owner, period, evidence location and criterion.
   Separate national registration, management governance, risk management and
   reporting instead of collapsing them into one readiness score.
4. **Verify governance and implementation.** Compare the approved measure/version
   to implementation evidence and oversight records. Identify unapproved changes,
   unresolved actions and missing role training. Keep approval existence and actual
   effectiveness as separate assertions; neither can substitute for the other.
5. **Exercise resilience and supplier dependencies.** Use approved tests to check
   recovery, access, vulnerability handling and critical supplier failure paths.
   Trace service availability through dependencies; two contracts may still share
   one failure point. Capture failed and unexecuted checks as well as successes.
6. **Exercise incident reporting.** Use the staged sequence below. Assign each
   jurisdiction and obligation its own clock, recipient and owner. Link related
   GDPR, DORA or other analyses where relevant, without assuming one report
   satisfies the others.
7. **Correct and retest.** Link each gap to affected entities, services and
   obligations. Record owner, proposed remedy, approval, execution and retest.
   Preserve original failures and residual limitations. A work ticket closed by
   its assignee does not by itself establish a successful correction.
8. **Review and hand off.** Present the complete matrix, observed results,
   unresolved source questions and management decisions. Record exactly which
   deliverable was approved, by whom, and what remains open.

### Significant-incident reporting sequence

This is an original execution design. Legal/incident owners supply the current
applicable significance criteria, clock interpretation and authorized routing.

1. Preserve detection, awareness, escalation and decision timestamps with their
   evidence and time zones. Do not replace awareness with the later time a ticket
   was assigned to the response team. Preserve disputed times for urgent review.
2. Match observed service impact and potential harm to the approved significance
   criteria. Record unknowns and competing interpretations. Do not wait for a
   confirmed root cause before escalating an apparently qualifying incident.
3. Open separate records for early warning, notification, requested updates and
   final/progress reporting. Keep the initial awareness clock visible beside
   later submission-based clocks. A delayed early warning does not restart the
   notification clock. Check the trust-service branch before using a generic
   72-hour notification template.
4. Draft the required content from the facts currently known. Mark preliminary
   assessments and update them when evidence changes. Route approval and incident
   response concurrently; a complete forensic narrative must not become an
   invented prerequisite for initial escalation.
5. Verify the current recipient, portal/access path, submitter and contingency
   route before an actual incident. For a real authorized submission retain the
   approved artifact/version, time, recipient, receipt and any delivery error.
   A saved draft, upload page or successful login does not prove reporting.
6. At the final-report checkpoint, determine whether the incident is ongoing and
   apply the approved progress/final route. Track handling status separately from
   ticket closure. Retain authority requests and subsequent update obligations.
7. Reconcile every reporting obligation, including any separate service-recipient
   communications. Preserve missing receipts and overdue actions with a named
   owner; do not close the reporting record simply because service recovered.

## Evidence and test plan

Retain the three PR #340 packages below with full in-scope coverage. Their source
snapshot does not establish review of this revised workflow.

### 1. Jurisdiction, entity, and critical-service applicability evidence

- **Request and owner:** Legal, compliance, and service owners provide entity and country registers, national-transposition tracking, critical-service descriptions, customer/dependency maps, designated authorities, and documented scope decisions for the review period.
- **Validate and limit:** Trace each in-scope entity-service pair to its jurisdiction, service rationale, supporting source record, accountable owner, and change date. This supports a transparent applicability record; it cannot interpret national law or decide entity classification.
- **AI and trigger:** AI may reconcile approved registers and flag a new country, service, or missing owner. Legal and authorized leaders decide applicability and authority engagement. Refresh after expansion, acquisition, a national-law change, or material service change.

### 2. Risk, resilience, and supplier evidence

- **Request and owner:** Security, resilience, procurement, and service owners provide risk assessments, asset and dependency records, continuity or recovery exercise outputs, supplier due-diligence records, material contract-change records, and remediation tracking for in-scope services.
- **Validate and limit:** Inspect each in-scope critical dependency from service map through owner, risk record, planned resilience activity, supplier evidence, and open action; preserve confidential supplier material in its approved repository. This supports traceability, not a finding of adequate risk management or supplier compliance.
- **AI and trigger:** AI may build an evidence index and flag stale supplier or exercise records. Human owners validate evidence and decide treatment, contract changes, and risk acceptance. Refresh after a critical supplier, outage, exercise, or architecture change.

### 3. Incident decision and notification-readiness evidence

- **Request and owner:** Incident, legal, communications, and executive owners provide incident classification records, time-stamped escalation logs, decision records, contact lists, communications approvals, lessons learned, and notification-preparation artifacts.
- **Validate and limit:** Trace each in-scope incident or exercise from detection through escalation, owner handoff, documented decision, and follow-up action while preserving privileged material. This can test process lineage and timeliness evidence; it cannot decide materiality, notification duties, or make a regulatory report.
- **AI and trigger:** AI may timeline approved records and flag missing timestamps or handoffs. Authorized legal and incident leaders decide notifications and approve communications. Run after incidents or exercises, and review contacts and procedures at the approved operational cadence.

## Failure branches and decisions

Use `supported`, `not_supported`, `inconclusive`, `not_applicable` and `not_tested`
for assertions separately from task status.

- National law or entity classification is unresolved: legal applicability stays
  `inconclusive`. Assign the exact missing source/decision; inventory work may
  continue under its own authorization.
- A recovery exercise cannot access its backup store: recovery is `not_tested`,
  not passed because a backup job reported success.
- A documented notification deadline was missed in the exercise: its timing
  assertion is `not_supported`; record the cause and retest without erasing the
  original failure. Actual legal consequences need authorized interpretation.
- An authority receipt is missing: submission remains unverified. Inspect the
  known transmission attempt before repeating it; avoid duplicate reports.
- A supplier certificate covers another service: it cannot support the in-scope
  service assertion without a verified scope relationship.

**Fictional desk case:** A non-trust-service QA incident has an approved awareness
anchor of Monday 10:00 UTC. Its early warning is sent Tuesday 12:00 UTC. Under the
approved 24-hour criterion, warning timeliness is `not_supported`. The standard
72-hour notification target remains Thursday 10:00 UTC, not Friday 12:00 UTC.
No real incident was evaluated or reported. This tests clock handling only, not
whether a real incident is significant or legally reportable.

## Cadence and renewal

Review against approved operational and national requirements rather than a
universal quarterly/annual rule. Reopen scope after country, entity or service
changes; recheck authorities and source updates before use. Refresh contact/access
readiness, exercise results and supplier dependencies after relevant change or
failure. Live incident clocks operate independently of scheduled reviews.

## Completion and handoff

Deliver the full entity/service and obligation registers, source versions,
controlled evidence index, results, unresolved questions, remediation/retest
records, reporting readiness and actual receipts where authorized actions occurred.
State the limits of each conclusion. Independent source, skeptical, rights and
publication reviews remain pending; structural tests do not prove legal accuracy
or reliable execution across different models.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md)
for shared applicability, authority, evidence, tests, exceptions and renewal.
