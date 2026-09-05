# EU GDPR — engagement guide

> Author draft. Original operational guidance, not legal advice, a rights decision,
> or a finding that an organization complies with GDPR.

## Source and applicability

Start with the [official regulation](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng),
its current amendments, relevant national law and competent supervisory-authority
material. Record entity, establishment, affected people, processing purposes,
territorial basis, controller/processor role and source version. Privacy counsel
owns applicability and any national or sector-specific variation. Do not assume
an EU address is necessary or sufficient for every processing activity to fall
within scope. Keep the [employment-context guide](eu-gdpr-employment-context.md)
linked when worker information is involved.

Source check, 2026-09-04: read the text of the EDPB
[rights guide](https://www.edpb.europa.eu/sme/be-compliant/respect-individuals-rights_en).
It describes the controller's response and processor's assistance, a one-month
response period, conditions for an additional two months, and notice within the
initial month. Access includes personal data and supplementary information;
review others' rights before disclosure. Access and portability differ.
This is a summary source, not the complete legal basis for an individual case.
The current regulation, case law, national rules and full access guidelines still
require verification. The EDPB access-summary PDF returned HTTP 429; its full
contents were not read. Do not treat an unavailable source as verified.

## Engagement focus

Connect approved processing purposes to actual collection, use, sharing,
retention and deletion. Produce source-linked decisions, operational checks and
remediation records. A privacy policy alone does not demonstrate that systems,
vendors or staff follow it. Separate each purpose, right, recipient and test
assertion so one successful step cannot conceal another missing or failed step.

## Roles

The privacy owner maintains the processing map and rights queue. System and
vendor owners retrieve authorized evidence and execute approved changes. Legal
counsel decides legal bases, rights restrictions, transfers, notification duties
and consequential interpretations. The security lead owns technical checks and
incident facts. The DPO, where applicable, performs its designated role without
being treated as the owner of every business decision. Independent reviewers
challenge scope and evidence; named human approvers authorize final responses,
legal conclusions, external submissions and production actions.

AI may reconcile approved metadata, draft requests and responses, calculate
warnings from an approved clock rule, and identify contradictions. It must not
invent identity checks, exemptions, retention periods, legal bases or approvals.

## Before starting

Use the [agent runbook](../agent-runbook.md) and one
[work item](../../templates/work-item.md) per observable assertion. Record the
engagement period, complete population, evidence locations, access authorization,
privacy-safe working area, reviewers and stop conditions. Keep personal data,
requester identities and actual response bundles outside this public repository.
Use synthetic records in QA-named workspaces for demonstrations.

Create an issue list for unresolved legal questions. A missing applicability
answer can block that conclusion while authorized inventory work continues.
Do not start an actual deletion, disclosure or customer-data test from this guide.

## Ordered workflow

1. **Define processing units.** Give each activity a stable identifier. Link
   entity, purpose, person categories, data categories, systems, locations,
   recipients and accountable owner. Reconcile the inventory against collection
   channels, applications and vendor records; identify unmapped systems instead
   of declaring the list complete because every listed row has an owner.
2. **Attach decisions before testing compliance.** Link the approved legal-basis,
   transparency, special-category, retention, transfer, DPO and impact-assessment
   decisions where relevant. Record unresolved questions and exact sources needed.
   A populated field is evidence of a recorded decision, not proof it is correct.
3. **Trace actual behavior.** Compare authorized observations to the approved
   purpose, notice version, recipients and retention rule. Check derived fields,
   logs, exports, support access and processors as well as the main application.
   Record each mismatch separately; do not silently revise the policy to match
   whatever the application currently does.
4. **Run the rights-request sequence below.** Preserve every requested right and
   every source disposition. Access, correction, erasure, restriction, objection
   and portability need separately approved outcomes; an export is not evidence
   that a deletion or objection was carried out.
5. **Test lifecycle and safeguards.** Map retention triggers to executed actions,
   including vendor copies, archives and restoration paths. Have legal owners
   resolve holds or conflicting duties. Use authorized tests for access controls,
   restoration and security measures; identify the exact data and scope tested.
6. **Trace processors and higher-risk change.** Reconcile actual providers,
   subprocessors, instructions and locations with agreements and approved
   safeguards. Route new purposes, profiling and material system changes through
   the owned impact-assessment decision before treating the old approval as valid.
7. **Exercise incident decisions.** Build the incident timeline from observed
   facts, awareness records and affected processing. Give the authorized incident
   and legal owners the current notification sources and facts. Maintain distinct
   clocks for each applicable obligation; do not derive reportability from a
   severity label or use the rights-request clock for an incident.
8. **Review and hand off.** Retest corrections, reconcile every in-scope item,
   record residual uncertainty and obtain the named reviews. Preserve approval
   and delivery/submission evidence separately from drafts.

### Rights-request execution sequence

This sequence is an original operating recommendation. The privacy/legal owner
must supply the current legal criteria, deadline computation and outcome rules.

1. Log receipt time, channel, original wording, requested rights and responsible
   entity in the restricted case record. Route misdirected requests without
   replacing the original receipt with the internal assignment time. Identify
   all parts of a combined request and track them to their individual outcomes.
2. Confirm the approved identity/representative verification path. If identity
   remains unresolved, escalate promptly. Do not collect an identity document by
   default or assume a clarification pauses or restarts a legal clock.
3. Record the approved due date, calendar/time-zone rule, source and escalation
   owner. An extension is a documented decision with required communication,
   not an automatic reset triggered by a busy queue. Keep the initial deadline,
   decision, notice and revised deadline visible together.
4. Establish the search map from processing records plus system/vendor owners.
   For every relevant source record identifiers/aliases used, date range, query
   method, pagination completion, retrieval time and custodian confirmation.
   Include authorized archives, messages, derived information and processor
   holdings when relevant. Search failures, unknown repositories and unresolved
   identity matches remain explicit. Never turn an inaccessible store into zero
   responsive records or trim retrieved evidence for a scorer's context window.
5. Reconcile retrieved records to each requested outcome. Preserve the complete
   restricted evidence set and produce a separate disclosure candidate. Link
   any proposed exclusion or redaction to an authorized decision and source;
   do not delete inconvenient material from the underlying evidence trail.
6. Have the authorized reviewer assess disclosure, other people's information,
   understandable presentation and the required supporting explanation. Confirm
   that the approved output addresses the actual right. Test files for readability
   and accidental disclosure, including hidden sheets, metadata and attachments.
7. Freeze the approved version and recipient/channel. Obtain authorization for
   the actual send. Record transmission outcome and delivery evidence; a draft,
   queued job or portal upload alone cannot prove the intended recipient could
   access the response. Escalate bounced messages or broken access promptly.
8. Close only against the approved completion criteria, with each right's
   decision, execution evidence, timing record and communication. Keep disputed
   outcomes and outstanding processor actions open or explicitly handed off.
   Dispose of working copies under the approved case-retention rule.

## Evidence and test plan

The three packages below retain useful PR #340 content with full in-scope
coverage. Its earlier review does not confer independent review on this revision.
Every artifact needs owner, period, source/version, scope and authorized location.
Complete metadata reconciliation can identify gaps without publishing personal data.

### 1. Processing, purpose, and recipient inventory

- **Request and owner:** A processing inventory that connects purposes, data categories, data-subject groups, systems, locations, expected erasure/retention periods, security-measures reference, controller/processor/DPO/representative details where applicable, recipients, and international transfers, owned by the privacy program with system and vendor owners.
- **Validate and limit:** Trace each in-scope processing activity to an actual system/data-flow record, notice, responsibility record, retention/security reference, and processor or recipient entry; record unverified fields and access restrictions. This can support a traceable accountability record. It cannot determine lawful basis, joint-controller status, DPO applicability, or transfer legality.
- **AI and trigger:** AI may reconcile approved metadata and identify mismatches; human privacy/legal owners approve classifications and decisions. Refresh on a new purpose, sensitive-data use, recipient, transfer, or material system change.

### 2. Transparency, rights, and retention operating evidence

- **Request and owner:** Notice/version records, rights-request intake and response log, identity-verification procedure, retention/disposal schedule and execution evidence, from privacy, customer-operations, and records-management owners.
- **Validate and limit:** Trace the full in-scope population of requests or retention events to intake, disposition, timing, and source system while redacting personal data. This can support that the workflow operates with recorded evidence; it cannot establish the correct individual outcome, exemption, or legal timing conclusion.
- **AI and trigger:** AI may calculate internal due-date warnings and prepare redacted traceability. Humans decide identity, rights outcomes, exemptions, and retention exceptions. Refresh for a new collection channel, rights process, retention rule, or complaint trend.

### 3. Processor, security, and incident-change record

- **Request and owner:** Processor/subprocessor register; executed processor agreement or other binding legal act; documented processing instructions; subprocessor authorization/change-notice evidence; transfer mechanism/transfer-assessment and applicable safeguard decision records; security-assurance inputs; breach register documenting facts, effects, and remedial action; incident timeline/exercise records; DPO-designation/applicability decision where relevant; risk or impact assessments; and remediation tracking.
- **Validate and limit:** Trace each in-scope vendor, transfer, or breach to its binding arrangement/instruction, approval, source evidence, and corrective action. Maintain a counsel-owned high-risk-change/DPIA decision record including whether prior consultation escalation is considered where residual high risk remains after measures. This supports a documented governance trail; it cannot prove processor compliance, security effectiveness, reportability, a DPIA outcome, transfer legality, or supervisory-authority notification obligations.
- **AI and trigger:** AI may maintain a source-linked index and flag expiring or missing records. Legal/privacy and incident owners approve DPO applicability, transfers, incident decisions, risk acceptance, DPIA/prior-consultation decisions, and external communication. Refresh after a processor/subprocessor change, transfer, incident, high-risk initiative, official source change, or annual review.

## Failure branches and decisions

Use `supported`, `not_supported`, `inconclusive`, `not_applicable` and `not_tested`
for assertions, separately from work status.

- A required repository cannot be searched: that search is `not_tested`; the
  completeness of the overall access response is `inconclusive`. Escalate access
  recovery and deadline risk with an owner. Do not state that no data exists.
- Retrieved records contradict an approved disclosure candidate's completeness:
  that completeness assertion is `not_supported`, even if other searches remain
  unresolved. Preserve the adverse finding and the uncertainty separately.
- A legal hold conflicts with proposed erasure: record the conflict and seek the
  legal disposition for the affected records. Neither blanket deletion nor a
  blanket rejection follows from the agent's interpretation.
- A policy says a provider is approved but actual processing reaches an unlisted
  subprocessor: record the observed mismatch. Transfer legality remains a
  separate legal question; a signed primary-provider agreement does not answer it.
- A response was sent but bounced: transmission was attempted, delivery is not
  established. Reopen the delivery action and preserve the original timeline.

**Fictional desk case:** A QA access case names CRM, support and an archive. CRM
returns ten records; support returns two; the archive query fails authorization.
The candidate contains only the ten CRM records. Against an approved criterion
that all identified responsive records be represented, it is `not_supported`
because the two support records are missing. Archive search is `not_tested` and
whole-population completeness is `inconclusive`. Adding the support records does
not resolve the archive gap. This exercise proves no real request outcome.

## Cadence and renewal

Refresh the map and decisions after changes to purposes, collection channels,
providers, locations, retention, laws or guidance. Review rights queues against
their individual clocks; annual review cannot replace timely case handling.
Repeat lifecycle and incident exercises at the approved risk-based cadence and
after material failures. Reopen conclusions when supporting evidence or the
approved criterion changes.

## Completion and handoff

Hand off the complete scope register, source versions, decision owners, evidence
index, individual results, rights-case dispositions, gaps, corrective actions and
retest records. State whether the deliverable is inventory, readiness review,
operating test or another approved engagement; do not relabel it certification.
Unverified national rules or failed searches remain visible with owners and dates.
Independent source, skeptical, rights and publication reviews remain required.
No automated score or structural check authorizes a legal conclusion or response.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md)
for shared authority, source, evidence, testing, exception and renewal rules.
