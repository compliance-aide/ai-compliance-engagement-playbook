# Hong Kong PDPO — engagement guide

> Original operational guidance, not legal advice or a regulator conclusion.

## Source and applicability

Use the [PCPD Ordinance overview](https://www.pcpd.org.hk/english/data_privacy_law/ordinance_at_a_Glance/ordinance.html), read 2026-09-04. It describes six data protection principles, data-user responsibility for processors, additional direct-marketing rules and case-specific exemptions. Silence is not direct-marketing consent. Access/correction refusals require reasons and a refusal log. These are overview-level statements; verify the current ordinance, commencement, detailed requirements and applicable codes before legal decisions.

This workflow covers organization-owned processing records and operational tests. Full current statutory text, request timing and exceptions, direct-marketing formalities, transfer restrictions and incident-reporting requirements remain source-review gaps. Do not import GDPR terminology, lawful bases or deadlines as Hong Kong requirements.

## Engagement focus

Trace personal data from collection through use, disclosure, correction, retention and disposal. Identify the responsible data user, all processors and actual purpose for each activity. Separate privacy compliance decisions from operational evidence of what happened.

## Roles

Privacy and legal owners decide applicability, purpose compatibility, exemptions, rights outcomes and communication obligations. Business and system owners maintain accurate records and implement approved changes. Marketing owns audience and preference enforcement. An independent reviewer challenges coverage and contradictory evidence. AI cannot decide exemptions, authorize disclosure, send responses or campaigns, accept risk, or conclude legal compliance. It may organize permitted evidence and draft issues for the accountable owner.

## Before starting

Record entity, processing scope, systems, channels, locations, recipients, processor roles, evidence period, owners and approved workspace. Establish request and incident intake paths with escalation owners. Keep personal data and credentials outside this public repository. Use synthetic fixtures for exercises and obtain approval before touching live customer records.

## Ordered workflow

1. **Identify processing and responsibility.** Reconcile all scoped collection channels, systems, exports, processors and recipients. Record purpose, data categories, owner and lifecycle state. A vendor label does not settle its role when it also uses data for its own purposes.
2. **Check collection and transparency.** Associate each collection interface with its actual notice version and configured fields. Compare collected data with the owner's documented need. Escalate unnecessary fields, undisclosed recipients and stale notices; legal owners decide sufficiency.
3. **Review use and marketing separately.** Record proposed use, original purpose and approved decision. For marketing, retain the applicable permission evidence, disclosures, preference history and downstream audience controls. Separate using data for own marketing from providing it to another party for marketing. No permission record means permission is unproven; a checked import box is not sufficient evidence by itself.
4. **Verify lifecycle and processor controls.** Trace accuracy changes, retention decisions, disposal jobs, access controls and processor obligations to actual results. Include replicas, exports and other scoped copies. A deletion request sent to a processor is not evidence that deletion occurred. Preserve documented legal holds and unresolved copies.
5. **Operate access and correction requests.** Preserve original receipt time; route identity and representative verification to the authorized process. Search all relevant scoped stores, record omitted or unavailable sources and obtain response approval. Have the owner verify the binding deadline and refusal rules immediately; internal reassignment does not restart the clock. Protect third-party data and record reasons and refusal-log entries where applicable.
6. **Handle failures and incidents.** Preserve chronology and evidence, contain only within authorization, and escalate suspected unlawful disclosure, doxxing, complaints and failed controls. The privacy/legal owner decides notification or other legal actions using current rules. Record prepared, approved, sent and received states separately.
7. **Retest and hand off.** Assign each defect an owner, due date and required closure evidence. Retest actual behavior and affected downstream paths. Record residual uncertainty and approved next steps; a task marked closed does not establish compliance.

## Evidence and test plan

Maintain complete population accounting for collection routes, purposes, requests, recipients, processors and findings. Keep all evidence supplied for assessment intact; do not silently trim or sample it. Document testing coverage and limits separately from inventory completeness.

### 1. Collection, purpose, notice, and retention package

- **Request and owner:** Privacy, product, business, and records owners provide a processing/data-flow register, collection-interface and notice history, stated purpose, data categories, systems, accountable owners, disclosures, retention/disposal rules, and material-change records.
- **Validate and limit:** Account for every scoped collection route; trace each route to notice version, documented purpose, owner, system, recipient, retention setting, and disposal evidence. This supports a factual lifecycle trail; it cannot decide purpose compatibility, notice sufficiency, exemption, or lawful retention.
- **AI and trigger:** AI may compare approved inventories, notices, and release metadata and flag stale links. Human privacy, product, and legal owners decide classifications and releases. Refresh for a new collection, purpose, interface, recipient, or retention change.

### 2. Access, correction, and direct-marketing preference package

- **Request and owner:** Privacy operations, support, marketing, and records owners provide approved request/verification procedures, redacted request and correction indexes, response approvals, preference/suppression records, campaign audience controls, training, and complaint escalation records.
- **Validate and limit:** Reperform a redacted request, correction, or preference trace through intake, human authority, relevant records, action, response/campaign controls, and closure. This supports the documented operational coverage; it cannot authenticate a requester, decide an exception, or determine direct-marketing permissions.
- **AI and trigger:** AI may organize approved de-identified records and flag incomplete workflow metadata. It may not respond to individuals, select recipients, or change suppression states. Humans decide outcomes. Recollect after campaign changes, complaints, or workflow defects.

### 3. Processor, security, and incident/change-governance package

- **Request and owner:** Procurement, security, privacy, legal, and leadership owners provide processor/due-diligence records, instructions, access-security references, change reviews, incident/exercise timelines, communications approvals, remediation/retest evidence, and management decisions.
- **Validate and limit:** Inventory all scoped processors, changes, security events and remediation items; trace each applicable record to source evidence, human authority, action owner, and retest. This supports accountable oversight; it cannot prove processor performance, determine notification, accept risk, or conclude compliance.
- **AI and trigger:** AI may flag expired assurance or unresolved actions in approved metadata. Humans approve contracts, communications, risk decisions, and closure. Refresh after a processor change, incident, failed test, or annual review.


## Failure branches and decisions

- Unknown purpose, role or exemption: obtain an accountable decision before dependent processing or disclosure.
- Opt-out recorded locally but absent from a campaign export: preserve the failed end-to-end result and escalate the affected audience; do not send a test campaign to real people.
- Missing processor evidence: report the missing assurance, request evidence and retain customer-side responsibilities.
- Request deadline uncertain or approaching: escalate immediately, preserve receipt time and continue authorized retrieval; do not invent an extension.
- A broad claim is contradicted by one verified failure: retain that failure even if other records are incomplete.

Use [agent runbook](../agent-runbook.md) assertions: supported, not_supported, inconclusive, not_applicable and not_tested. Split compound conclusions and keep legal decisions distinct from technical observations.

## Cadence and renewal

Set review intervals by risk and the approved operating plan, not an invented statutory quarterly or annual cycle. Reopen affected work when collection, purpose, recipient, processor, law, notice, retention, request handling or marketing systems change. Preserve the current source and decision behind every time-sensitive obligation.

## Completion and handoff

Deliver the reconciled population register, evidence references, permission and rights decision records, processor gaps, test coverage, findings and next actions. Named owners approve legal decisions and external communications. Independent source, skeptical and rights review remain required before publication.

Fictional author desk case: the CRM records a marketing opt-out, but a queued export still contains the synthetic contact. Local preference storage is supported; end-to-end suppression is not_supported. Recipient-side processing is untested. No real campaign, request response or legal conclusion occurred.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for applicability, authority, evidence, technical-test, exception, source-change and renewal records.
