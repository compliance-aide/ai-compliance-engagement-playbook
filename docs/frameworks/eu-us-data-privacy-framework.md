# EU–U.S. Data Privacy Framework engagement guide

> Original operational guidance, not Data Privacy Framework program text, legal advice, a self-certification, or a participation claim. Confirm current program status through the [U.S. Department of Commerce Data Privacy Framework information](https://www.trade.gov/country-commercial-guides/eu-digital-economy), the [program website](https://dataprivacyframework.gov/), and qualified privacy counsel.

## Source and applicability

Source checkpoint, 2026-09-04: search identified the official EDPB
[January 2026 business FAQ](https://www.edpb.europa.eu/system/files/2026-01/edpb_dpf_faq-for-businesses_v2_en.pdf).
Its indexed text describes active participation and a nuanced HR-data coverage
check, including a privacy-policy commitment route in specified circumstances.
Full PDF retrieval returned HTTP 429, so those conditions require full-source
verification before use. Do not hard-code the older FAQ's simplified HR checkbox
interpretation as the sole rule. No recipient entry or current adequacy/legal
status was verified in this pass.


Verify the current adequacy decision, program principles, participant record and
relevant exporter-jurisdiction guidance before reliance. Record exporter versus
U.S. participant responsibilities separately. This guide does not establish that
every U.S. recipient is eligible or that every transfer is covered.

## Engagement focus

Maintain a cross-border transfer and participation-readiness record: participating entity and service scope, personal-data flows, onward recipients, public privacy representations, complaint and escalation handling, retention and deletion practices, supplier commitments, evidence of implemented practices, annual renewal dates, and program or legal-status changes. Keep the record separate from broader GDPR and U.S. privacy compliance analyses.

## Before starting

Define whether this engagement reviews an exporter's reliance, a participant's
operating practices, or preparation for participation/renewal. Record the complete
entity/service/flow population, review period, sources, evidence permissions,
legal owner and independent reviewers in [work items](../../templates/work-item.md).
Use synthetic examples in QA-named workspaces. Keep personal data, complaints,
contracts and restricted evidence outside this public repository.

Set an approved criterion for each check: exact recipient identity, observed
listing scope, policy-version consistency or actual handling of a request. Do not
collapse those different assertions into one participation/compliance result.

## Ordered workflow

Follow the [agent runbook](../agent-runbook.md). Keep the transfer decision,
recipient-status observation and wider privacy assessment separate. This is an
original workflow recommendation for an authorized read-only review.


1. Record the actual exporter, U.S. recipient legal entity, service, data categories,
   purpose and transfer date/period. Resolve trading names and subsidiaries against
   contracts and the actual processing flow. A parent-company logo is not an entity
   match; do not silently substitute another group company.
2. Open the [official participant list](https://www.dataprivacyframework.gov/list)
   and record the specific entry, observation time, active/inactive status, covered
   entities, framework and data scope. A search snippet, cached directory, URL
   containing “Active” or script-loading page does not establish current status.
3. Compare the exact recipient and transfer to the entry and linked privacy policy.
   Have privacy/legal resolve HR-data and subsidiary coverage using current official
   guidance. Record the policy version and relevant commitment evidence rather than
   inferring coverage from a group name or a single checkbox.
4. Keep EU–U.S., UK-extension and Swiss–U.S. observations distinct. An entry for one
   route is not evidence for every exporter jurisdiction. Record the applicable
   decision source and counsel-owned transfer mechanism for each flow.
5. Trace onward recipients and the approved commitments governing their processing.
   A direct recipient's listing does not prove every later recipient is separately
   listed or that the whole transfer chain satisfies its obligations. Preserve all
   in-scope flows and unresolved recipients in the evidence index.
6. Compare public representations to the observed entry, approved service/data scope
   and policy version. Prepare corrections for authorized review when claims differ;
   do not publish new claims or file a self-certification during this evidence review.
7. Record renewal/status-change triggers and an owner for rechecking ongoing flows.
   If status becomes inactive or cannot be verified, escalate the affected flow and
   distinguish new transfers from previously received data. Legal owns the required
   treatment; do not automatically delete retained data or switch mechanisms.
8. Hand off the complete flow register, entry/policy references, timestamps,
   discrepancies, source gaps and human decisions. Approval to draft this packet is
   not approval to transfer data or claim participation.

## Failure branches and decisions

 an unavailable registry check is `not_tested`; current
recipient coverage remains `inconclusive`. A retrieved entry explicitly covering
only a different legal entity does not support an exact-entity-match assertion.
Keep that mismatch separate from uncertainty about another possible entry.

**Fictional desk case:** a contract names Example Payroll LLC, while the supplied
entry names Example Analytics Inc. and does not identify the payroll entity as
covered. The supplied-record entity-match assertion is `not_supported`. If the
live list is unavailable, whether a different applicable entry exists remains
`inconclusive`; neither assuming coverage nor declaring definite nonparticipation
is justified. No real company, transfer or certification is represented.

## Roles

Qualified privacy and legal owners determine eligibility, program obligations, and transfer mechanisms; business owners approve service scope and public statements; operations and suppliers maintain evidence; independent reviewers test traceability and renewal readiness. AI may organize approved records, flag stale statements or evidence, and draft nonbinding questions, but cannot self-certify, submit a filing, decide eligibility, respond to a complaint, select a legal transfer mechanism, or claim participation. Reassess before any material entity, service, data-flow, supplier, public-statement, complaint, or program-status change and complete an accountable human annual review.


## Evidence and test plan

Restore the three PR #340 packages below with full in-scope coverage. Prior review
of an older artifact does not approve this revised guide. Preserve all evidence
bound for a scorer; use non-sensitive references in public workpapers.

### 1. Entity, service, and transfer-scope record

- **Request and owner:** Participating-entity and service-scope records, personal-data flow inventory, data categories and purposes, EU/EEA/UK/Swiss context where applicable, onward-recipient inventory, processing-location context, and accountable owner assignments from privacy, legal, product, and business owners.
- **Validate and limit:** Trace each in-scope service and data flow to entity scope, purpose, data category, recipient context, owner, and review date. This supports a bounded readiness record; it cannot establish eligibility, determine a lawful transfer mechanism, or prove inventory completeness.
- **AI and trigger:** AI may reconcile authorized metadata and flag unowned flows, stale scope records, or inconsistent recipient entries. Humans decide eligibility, transfer mechanisms, and scope. Refresh before a new entity, service, purpose, data category, data location, onward recipient, or material architecture change.

### 2. Public commitments, individual handling, and incident evidence

- **Request and owner:** Approved privacy notices and public statements, complaint/dispute-resolution procedures and case records, access/correction or other individual-request records where applicable, incident/escalation evidence, retention/deletion operation evidence, and communication approvals from privacy, customer operations, security, and records-management owners.
- **Validate and limit:** Trace each in-scope public-statement revision, complaint, request, or incident to source evidence, accountable handling, escalation, action, and closure. This can show the reviewed case trails; it cannot decide individual rights, resolve a dispute, establish notice adequacy, or determine notification duties.
- **AI and trigger:** AI may organize authorized records in their restricted evidence location and flag missing handoffs or aging actions; it may not respond to an individual, make a legal conclusion, alter a notice, or send a complaint response. Humans approve statements, decisions, investigations, and communications. Recollect after a complaint, incident, public-statement change, or retention-process change.

### 3. Onward-transfer, renewal, and management-review workpaper

- **Request and owner:** Supplier/onward-recipient agreements and oversight evidence, assurance or due-diligence records, program-renewal calendar, exception/remediation register, management review and decision records, and closure/retest evidence from procurement, privacy, legal, security, leadership, and independent-review owners.
- **Validate and limit:** Trace each in-scope recipient, renewal item, or exception to contractual/oversight context, accountable decision, due date, and retest. This supports readiness transparency; it cannot authorize a recipient, approve a certification/renewal, accept transfer risk, or replace legal review.
- **AI and trigger:** AI may prepare a source-linked evidence index and factual challenge questions. Humans approve recipient decisions, renewal submissions, risk acceptance, closure, and all external representations. Review annually and after a supplier, assurance result, complaint, audit finding, program update, or legal-status change.


### Operating-practice checks

These are original execution recommendations. The legal/privacy owner must supply
the current applicable program criteria before a legal conclusion is drawn.

- Reconcile every in-scope public claim to its approved text, actual publication
  location and underlying scope evidence. A draft correction does not establish
  that a stale page was changed. Record an observed mismatch separately from the
  legal consequence, which requires review.
- Trace each in-scope complaint or request from receipt through routing, decision,
  action and verified communication. A closed ticket is not delivery evidence.
  Test the routing with a synthetic internal case rather than sending a fake
  complaint to an external dispute-resolution body.
- Compare the approved retention rule with system and onward-recipient actions.
  Distinguish account closure, inaccessible data and verified deletion. Record
  legal-hold conflicts for the authorized owner instead of choosing a disposition.
- Reconcile the full onward-flow map to agreements, accountable owners and actual
  processing locations. Document missing recipient evidence explicitly; a vendor's
  questionnaire alone does not establish implementation of its commitments.
- For renewal readiness, index every required input and human decision, then
  distinguish prepared, approved, submitted and verified-status records. A saved
  form or paid fee is not evidence that participation has been renewed.

If a test cannot obtain an authorized observation, mark it `not_tested`; do not
replace the missing observation with the policy's intended behavior. Reconcile
all failed, unresolved and unexecuted checks before any readiness handoff.

## Cadence and renewal

Use the program's verified renewal requirements and the owner's review schedule.
Recheck ongoing reliance after entity, data-scope, recipient, policy, legal or
program-status changes. Retain observation dates so an old status check cannot
silently become a claim about the present. Each unresolved flow needs an owner
and next action independent of the annual review calendar.

## Completion and handoff

Deliver the complete flow register, source/entry/policy references, evidence index,
individual results, discrepancies, remediation/retest records and named human
choices. Separate observed listing status from transfer legality and operating
compliance. Keep inaccessible sources and unverified current legal status visible.
State the exact engagement type and scope; do not describe readiness work as
self-certification, renewal or an approved transfer.

Independent source, skeptical, rights and publication reviews remain pending.
Structural checks and an author's fictional desk case do not establish independent
validation or reliable execution across different AI models.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
