# California CCPA/CPRA — engagement guide

> Original operational guidance, not California legal advice or a compliance determination.

## Source and applicability

Use the [CPPA laws and regulations page](https://cppa.ca.gov/regulations/) and the current operative statute and regulations it links. Checked 2026-09-04. The agency identifies a January 1, 2026 effective regulation set, including cybersecurity-audit, risk-assessment and automated decisionmaking provisions. Effective date is not necessarily each provision's compliance deadline. Preliminary rulemaking is not operative law. Counsel must record applicable thresholds, exceptions, duties and transition dates for the actual entity and processing activities.

CPRA amended the CCPA; do not build two disconnected compliance programs. Classify business, service-provider, contractor and third-party roles by actual activity and approved interpretation, not a vendor label. Evaluate workforce and data-broker obligations separately where applicable; see the [workforce guide](california-workforce-privacy.md). Do not infer a whole-entity exemption from an exemption affecting particular information.

## Engagement focus

Connect each data use to its purpose, collection channel, notice, consumer choice, recipients, retention and actual system behavior. Produce evidence that requests and preferences reach the systems using the data, with legal decisions and missing coverage visible.

## Roles

Privacy and legal owners decide applicability, classifications, exceptions and consumer outcomes. Product/data owners maintain actual processing and interfaces. Vendor owners supply recipient and contract evidence. Customer operations handles approved requests; security and records owners address incidents and retention. Independent reviewers challenge implementation. AI drafts maps and workpapers; it cannot decide legal outcomes, sign certifications or send responses without authorization.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Name the entity, processing activity, channel, period, owner and decision. Require approved applicability, data inventory, request procedures, deadline rules and permitted evidence locations. Create bounded work items with inputs, outputs and exit checks. Missing records stay explicit. Use synthetic QA identities for exercises; do not expose real consumer information in this public repository.

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Establish duties | Privacy/legal owners document applicable provisions, entity/activity roles, exceptions and effective/compliance dates. Include a decision on new audit, risk-assessment and ADMT provisions where relevant. | Versioned obligation register with owners and source references; unresolved scope remains unresolved. |
| 2. Map processing | Data/product owners reconcile collection, uses, recipients, systems and retention with actual flows. | Processing inventory with discrepancies and owners; an unknown analytics recipient is not silently excluded. |
| 3. Align notices and choices | Privacy/product owners compare approved disclosures and choice design with the mapped uses and live interface. | Notice/version and preference workpapers; published words alone do not establish downstream behavior. |
| 4. Route requests | Operations records intake time and request type, applies the approved verification/agent procedure appropriate to that type and calculates its governed clock. Route exceptions to the decision owner. | Case record with source-based deadline and pending actions. Do not impose one verification or timing rule on all request types. |
| 5. Execute approved outcomes | Authorized operators apply the approved decision across relevant systems and recipients; reviewer checks actual results and limitations. | System/recipient readbacks and exact response draft; attempted deletion is not verified deletion. |
| 6. Govern recipients and retention | Vendor/records owners reconcile actual recipient use and retention with approved terms, purposes and holds. | Contract/operation and retention evidence; unresolved conflicts go to legal rather than automatic erasure. |
| 7. Assess and remedy | Responsible owners perform applicable assessments or audit preparation under their approved methods. Track gaps, corrective actions and retests before any required certification or submission decision. | Evidence-linked findings and decision packet. This guide does not authorize a filing or replace independent audit work. |
| 8. Maintain | Privacy owner monitors changes, requests, incidents and new rules; reopens affected maps, notices, assessments and system checks. | Owned renewal/change queue and retained decision history. |

## Evidence and test plan

Use the complete approved obligation register. These original examples are not the legal requirement set. Preserve the full evidence corpus; never trim evidence supplied to a scorer.

| Package and owner | Verification | Limitation |
| --- | --- | --- |
| Data/party map — data/vendor owners | Trace a collection through purpose, recipient, system and retention; reconcile discoveries with the full inventory. | A selected path does not establish complete processing coverage. |
| Notice/choice — product/privacy | In authorized QA, trace an applicable preference event through interface, stored state and downstream processing, including relevant logged-in and logged-out paths. | A visible switch does not prove recipient suppression; record untested channels. |
| Rights — operations/reviewer | Trace an approved synthetic case from intake through type-specific verification, clock, decision, system action and response record. | A generic workflow cannot establish every exception or deadline; use the approved rule for that case. |
| Vendor/retention — vendor/records | Compare actual provider handling and deletion evidence with approved responsibilities and holds. | Contract promises and deletion job success do not prove every relevant copy handled. |
| Assessment/remediation — privacy/security | Trace an applicable assessment finding to action, implementation and retest, retaining unresolved limitations. | Prepared workpapers do not establish independent audit completion or filed certification. |

Record source, collector, time, period, activity, expected/observed result, evidence pointer, limitation, reviewer and next action. Keep consumer records access-controlled and minimize copies; never substitute missing evidence with invented data.

## Failure branches and decisions

- **Unclear sale/sharing, role or exception:** preserve the data-flow facts and seek the legal owner's determination; do not infer from a contract title.
- **Request type misrouted:** correct routing and preserve the original receipt time. Do not reset the clock when escalating.
- **Verification failure:** follow the approved type-specific process; do not disclose information or impose extra identity requirements by default.
- **Preference not propagated:** retain the failed result, identify affected systems/recipients and escalate correction; do not claim compliance from the interface alone.
- **Deletion conflicts with a hold:** obtain a scoped legal decision and document remaining data and permitted treatment. Do not erase first and ask later.
- **Unknown new-rule applicability:** record the provision, activity and decision owner; do not treat all 2026 provisions as having identical deadlines.
- **Interrupted action or uncertain response:** preserve versions, original clock and pending approvals; read back the destination before retrying.

## Cadence and renewal

Use provision-specific dates, approved request clocks and actual review obligations. Internal quarterly review is an owner-selected practice, not a universal CCPA deadline. Recheck after changes in purposes, recipients, interfaces, retention, automated decisions or law. Assign each monitoring trigger an owner.

## Completion and handoff

A preparation packet contains approved applicability, complete processing/obligation records, notices, choice/request workpapers, vendor and retention evidence, findings/retests and pending decisions. Mark omissions. Responses, filings and certifications are separate authorized milestones with destination evidence. Handoff gives each open item's owner, due date, next action and source record.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared applicability, authority, evidence, technical-test, exception, source-change and renewal requirements.
