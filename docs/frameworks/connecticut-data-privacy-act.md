# Connecticut Data Privacy Act — engagement guide

> Original operational guidance, not legal advice. Confirm the live [Connecticut privacy program source](https://portal.ct.gov/AG/Sections/Privacy-/The-Connecticut-Data-Privacy-Act).

## Engagement focus

Track legal changes, collection, sharing, sensitive/minor-data, automated-decision, vendor, rights, opt-out, consent, notice, retention, and assessment evidence.

## Roles

Operators maintain the record; independent reviewers test end-to-end experiences and evidence. AI flags declared-versus-observed drift, but cannot judge coverage, minors’ status, or compliance. Review quarterly and annually.

## Source and applicability

The [Attorney General’s July 2026 guidance](https://portal.ct.gov/ag/press-releases/2026-press-releases/attorney-general-tong-sends-message-to-big-tech-about-hooking-kids-on-addictive-apps) describes expanded coverage: at least 35,000 Connecticut residents outside payment transactions, or sale of personal data or processing sensitive data. It also identifies expanded sensitive-data categories, rights concerning inferences and third-party sales, profiling rights and new protections for minors. Do not reuse the original 2023 threshold or rights checklist without amendment review.

Use the [current statutory supplement](https://www.cga.ct.gov/2026/sup/chap_743jj.htm) together with enacted amendments and effective dates. Counsel must distinguish operative July provisions from later 2026 and 2028 changes and evaluate exemptions and exact definitions. A press summary is a change alert, not the complete legal test. Keep a separate row for each amendment and affected activity.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Name the legal, privacy, product, data, support and processor owners. Record the applicable population, processing period and approved evidence environment. Use synthetic test identities and permitted metadata; do not infer a real person’s age or collect extra sensitive data merely to populate a checklist.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Revalidate coverage | Counsel checks current thresholds, data-specific triggers, exclusions and effective dates. | Source-linked decision with old assumptions retired explicitly; low volume alone is not a sufficient exclusion. |
| 2. Map actual flows | Engineering and business owners trace collection, inference, sharing, profiling, storage and deletion through all services and processors. | Owned processing inventory, including derived data and actual recipient paths. |
| 3. Reconcile sensitive/minor features | Privacy and product owners identify age-related design inputs, sensitive categories, profiling and targeted-advertising uses for legal review. | Approved classifications and control expectations; uncertainty is visible, not silently treated as adult/non-sensitive. |
| 4. Build complete obligations | Agent maps the adopted requirement set to each activity, owner, evidence need and due date. | Full register separating current duties, future changes and voluntary controls. |
| 5. Exercise rights and preferences | Approved testers trace synthetic access, correction, deletion, portability, opt-out and appeal requests through intake, systems and recipients. | Dated observed behavior and coverage; include amended rights where applicable, not only the legacy interface. |
| 6. Evaluate profiling and assessments | Qualified owners review decision use, consumer-review routes and assessment triggers using current law. | Human-approved assessment and workflow decisions supported by evidence; a model card is not a completed assessment. |
| 7. Remediate and retest | Owners implement approved fixes and verify processor actions and downstream data effects. | Retest evidence with incomplete recipients or channels retained as gaps. |
| 8. Review and sustain | Independent reviewers challenge scope and closure; authorized humans approve responses and representations. | Reviewed package, verified delivery where authorized, open decisions and source-watch dates. |

## Failure branches and decisions

- **Volume below old threshold:** evaluate amended sale/sensitive-data triggers and current threshold before an exemption conclusion.
- **Notice promises access but inferences are omitted:** reconcile the actual current rights scope and systems holding derived data before approving the response.
- **Consent offered for prohibited processing:** obtain the precise legal decision; consent does not automatically override a prohibition.
- **Preference stored but export continues:** retain interface and downstream evidence separately and assign enforcement remediation.
- **Profiling appeal returns the same automated result:** have the responsible human assess whether the implemented route meets the applicable review obligation; repeated automation is not proof of meaningful review.

## Evidence and test plan

**Source and rights snapshot.** Use the live [Connecticut privacy program source](https://portal.ct.gov/AG/Sections/Privacy-/The-Connecticut-Data-Privacy-Act) and qualified Connecticut privacy/legal review; prior snapshot dated 2026-07-31; revalidate amendments and effective dates. This original plan does not determine coverage, controller/processor role, a minor’s status, consent, automated-decision obligations, assessment need, request result, or any regulator-facing duty.

### 1. Processing, sensitive/minor-data, and notice package

- **Request and owner:** Processing and data-flow register; data-category, sensitive-data, and age-related design inputs; collection sources; purposes; systems; recipients/processors; retention; notice/version history; and accountable product, privacy, engineering, and vendor owners.
- **Validate and limit:** Trace a selected flow from collection experience to documented purpose, system, data classification input, recipient/processor, notice, retention record, and owner. This supports a factual evidence base; it cannot determine a person’s age, scope, consent, legal classification, or whether processing is permitted.
- **AI and trigger:** AI may reconcile approved inventories with release and provider metadata and flag divergences. Human legal/privacy/product owners decide classifications and approvals. Refresh for a new collection point, sensitive/minor-data design, automated-decision feature, provider, or material change.

### 2. Consent, rights, opt-out, and automated-decision operation package

- **Request and owner:** Consent/preference and opt-out configuration where used; rights and appeal procedures; redacted request records; verification design; automated-decision inventory and human-review/escalation design; response-quality tests; and training/remediation evidence from privacy, support, data, and engineering owners.
- **Validate and limit:** Independently trace a de-identified request, preference, or test decision journey through interface, intake, assigned owner, verification step, system action, human review where configured, response, and appeal record. This can support workflow traceability; it cannot authenticate an individual, decide an appeal, establish meaningful human review, or prove a legally sufficient response.
- **AI and trigger:** AI may prepare de-identified sample indexes and identify missing workflow records; it cannot infer age, decide an outcome, or communicate externally. Authorized humans determine identity, requests, appeals, and any human review. Recheck after a complaint trend, interface, model/decision, or workflow change.

### 3. Assessment, processor, and change-assurance package

- **Request and owner:** Human-approved assessment/risk inputs for potentially relevant processing; processor/subprocessor diligence and instruction records; security test references; exception, incident, and remediation/retest records; management review; and source-change monitoring.
- **Validate and limit:** Trace a selected assessment input, provider change, incident, or remediation item to source evidence, authority, stated limitation, corrective action, and retest. This supports accountable oversight; it cannot decide assessment requirements, accept risk, determine notification, or establish processor performance.
- **AI and trigger:** AI may index approved materials and flag expired reviews. Legal, privacy, security, and leadership humans approve risk, contracts, external communications, and closure. Refresh after a processor, high-risk change, incident, source update, or annual scope review.


## Cadence and renewal

Quarterly testing and annual reconciliation are internal conventions. Derive request, appeal, assessment and retention deadlines from current applicable law. Recheck after amendments, sensitive-data discovery, age-related feature changes, new profiling uses, processor changes or failed tests. Preserve original receipt dates and source versions when cases move between teams.

## Completion and handoff

Deliver the applicability/amendment register, full obligation coverage, actual data flows, consent/notice evidence, rights and profiling tests, processor confirmations and unresolved decisions. State what was drafted, approved, executed and delivered. The next agent must know the next action, owner and missing evidence without prior chat history; no compliance claim follows solely from completing a template.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
