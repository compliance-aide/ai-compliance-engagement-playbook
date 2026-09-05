# FERPA — engagement guide

> Original operational guidance, not legal advice or a student-record disclosure
> decision. Check the current [FERPA regulations](https://www.ecfr.gov/current/title-34/subtitle-A/part-99).

## Engagement focus

Establish in-scope institution, programs, records, and authorities. Maintain a
record taxonomy, access model, disclosure-authority register, vendor terms, and
request/disclosure process. Review changes, route rights requests and disclosures
to authorized privacy decision-makers, and validate annual notice and policy
processes without exposing student-level data.

## Source and applicability

Use the current rule and institution-specific policies, with counsel resolving scope and exceptions. On 2026-09-04, the [Department of Education's regulation text](https://studentprivacy.ed.gov/ferpa) was read for institutional scope, definitions, rights transfer, notices, access, amendment and initial disclosure conditions. Remaining disclosure provisions and current eCFR reconciliation require review. Do not treat this draft as a complete legal analysis.

Source checkpoints: §99.10 sets access within a reasonable period, no later than 45 days after receipt, and prohibits destruction while an inspection request is outstanding. Section 99.7 requires annual rights notification. Section 99.5 addresses transfer to eligible students; age alone is not the only trigger. Check the exact conditions before applying a consent exception.

## Roles

Registrar and privacy owners approve classifications, requester authority and disclosure decisions. Technology and vendor owners provide controlled evidence. Independent reviewers challenge completeness and legal interpretations. AI works with authorized redacted metadata or synthetic records, prepares drafts and tracks gaps; it cannot infer consent, decide an exception or release student records.

## Before starting

Record institution, funding/applicability decision, programs, systems, custodians, period, approved policy versions and responsible privacy official. Keep actual education records outside this public repository. Identify approved evidence systems and test accounts. Create a work item using the [agent runbook](../agent-runbook.md), with input, expected result, evidence location and next owner for each check.

## Ordered workflow

1. **Map the record population.** Reconcile every in-scope system and custodian, including vendor-held records and departmental stores. Output a record/source inventory with unresolved classifications. A missing search result does not prove a record does not exist.
2. **Identify the decision holder.** Route requester identity, rights-holder status and any conflicting authority evidence to the authorized institution owner. Record the decision reference without copying sensitive identity documents. A parent's presence in a contact list does not settle access rights.
3. **Register requests and preserve the clock.** Keep original receipt time, request type, applicable deadline and owner. Separate inspection, amendment, hearing and disclosure workflows. Internal reassignment or delayed data collection must not silently reset the receipt time. Escalate threatened deadlines; do not invent an extension.
4. **Build the candidate response.** Search the approved source inventory, record each custodian's result and preserve unresolved searches. Reconcile the candidate with the request and owner-approved scope. Have the reviewer resolve mixed-student content and any exclusions before release. Keep a restricted full evidence index even when the outward response requires redaction.
5. **Prepare disclosure authority review.** Link each proposed recipient, purpose and data set to the precise consent or exception route and its supporting records. A vendor contract is evidence for review, not an automatic permission to disclose. Hold the outbound action until the institution's decision is recorded.
6. **Test the implemented route.** In an authorized QA environment, use synthetic records to check permitted access, prohibited access, wrong recipient, missing authority and failed delivery. Record expected and actual behavior. A login success does not prove the user can access only the approved records.
7. **Verify action and closure separately.** Distinguish a prepared response, approved response, actual authorized delivery and unresolved follow-up. Retest corrections against the failed behavior. Preserve amendment/hearing follow-up as a separate tracked outcome instead of closing it when an access request completes.

## Failure branches and decisions

Use `not_tested` when a custodian or system was not inspected; use `inconclusive` when relevant facts conflict. A known missing record in a candidate response is `not_supported` for the defined completeness criterion even if other searches are unresolved. Keep the affected action awaiting review with a named owner; do not disguise uncertainty as approval.

Fictional desk case: a candidate response includes ten registrar records, but an approved inventory identifies two responsive departmental records that were omitted. Completeness is `not_supported`; an inaccessible archive remains separately `not_tested`. The agent restores the omissions and escalates the archive search without releasing the draft or restarting the original request clock.

## Cadence and renewal

Track the annual rights notice separately from locally scheduled access, provider and process reviews. Recheck after changes to systems, roles, programs, vendors, requests, incidents or official sources. The owner must verify that the notice process reaches its intended audience; an approved draft alone does not prove notification.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
