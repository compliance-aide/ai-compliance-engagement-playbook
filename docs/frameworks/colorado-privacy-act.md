# Colorado Privacy Act — engagement guide

> Original operational guidance, not legal advice. Verify live rules at the [Colorado Attorney General privacy page](https://coag.gov/resources/colorado-privacy-act/).

## Engagement focus

Maintain processing and vendor maps, rights, notices, consent, universal-opt-out, and high-risk-processing evidence; test web/app behavior and processor oversight.

## Roles

Counsel validates scope; independent reviewers test user outcomes and evidence. AI compares releases and tags to inventories, but cannot make coverage or signal conclusions or approve assessments. Review quarterly and annually.

## Source and applicability

Use the official AG page above together with current statutes and rules. Its FAQ describes controller/processor roles, consumer rights and opt-out handling, but retains historical future-tense language. Do not treat the FAQ as a complete consolidated statement of current law. Screen amendments separately, including [biometric protections](https://leg.colorado.gov/bills/hb24-1130), [children’s online data](https://www.leg.colorado.gov/bills/sb24-041), and the [CPA rulemaking record](https://coag.gov/colorado-privacy-act-rulemaking/). Counsel verifies final text, scope and effective dates before applying those provisions.

Maintain separate applicability records for each processing activity and role. Do not infer a blanket exemption from employment context, organization type or general volume thresholds without reviewing any independently applicable amended provision. Keep Colorado ADMT-law work separate from CPA obligations even when the same product is involved.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Name privacy, legal, product, engineering and processor owners. Record authorized evidence environments and use synthetic accounts for tests. Build a complete obligation register against the adopted sources, with applicability, owner, evidence, expected behavior, observation, limitation and next action. A banner screenshot cannot prove that downstream processing respects a preference.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Verify source and scope | Counsel reviews current thresholds, exclusions, amendments and entity roles. | Dated source-linked applicability decisions, including separate minors/biometrics screening. |
| 2. Map real processing | Business and engineering owners trace data from collection through use, recipients, storage and disposal. | Complete owned flow inventory, including tags, SDKs, backend exports and processors. |
| 3. Reconcile notices and consent | Privacy owner compares actual purposes and recipients with published versions and consent records. | Unsupported uses and consent gaps assigned for legal review; acceptance of general terms is not assumed to authorize every use. |
| 4. Define preference behavior | Privacy/legal owners identify applicable recognized opt-out mechanisms and rights rules; engineering documents expected propagation. | Versioned expected behavior across web, app, account and recipient paths, with unresolved cases explicit. |
| 5. Exercise real execution safely | Authorized testers use synthetic identities to trace opt-out, access, correction, deletion, portability and appeal paths where applicable. | Evidence of downstream effects, timing and limitations; unsupported channels remain untested rather than passed. |
| 6. Evaluate elevated-risk processing | Owners assemble assessment inputs and amended-law facts; qualified reviewers decide required assessments and treatment. | Source-linked decisions and approved actions; an assessment template alone is not a completed assessment. |
| 7. Remediate and retest | Operational owners correct approved issues and obtain processor evidence; reviewers repeat affected journeys. | Observed correction across the affected systems, with remaining copies or recipients disclosed. |
| 8. Review and maintain | Privacy leadership approves responses and claims, preserves receipts and assigns future checks. | Reviewable package with open issues, current source versions and change triggers. |

## Failure branches and decisions

- **Signal received but advertising continues:** retain request and observed network/backend evidence; isolate routing, interpretation and enforcement failures separately.
- **Conflicting consent and opt-out records:** preserve the full sequence and request the legally approved resolution; do not silently choose the most permissive state.
- **Request deadline approaching:** the AG FAQ describes 45 days and a reasoned extension notice within that period when necessary. Confirm the applicable current rule and request type; do not automatically extend or reset the clock at internal reassignment.
- **Provider says deletion completed:** obtain system-specific confirmation and retained-data limitations before closing the consumer case.
- **Minor or biometric use discovered:** reopen the relevant applicability and safeguards review; do not assume the original general CPA analysis covered the new facts.

## Evidence and test plan

**Source and rights snapshot.** Use the [Colorado Attorney General privacy page](https://coag.gov/resources/colorado-privacy-act/) and qualified Colorado privacy/legal review; prior snapshot dated 2026-07-31; revalidate amended law and current rules before use. This original plan does not decide applicability, controller/processor status, consent, sensitive-data treatment, a universal opt-out mechanism result, assessment need, request outcome, or enforcement posture.

### 1. Processing, notice, and party-inventory package

- **Request and owner:** Processing register for personal and sensitive data; collection sources; purposes; systems; retention; disclosures; controller/processor and subprocessor relationship inputs; notice/version history; and product, privacy, data, and procurement ownership records.
- **Validate and limit:** Trace a selected processing activity to collection channel, documented purpose, data categories, system, recipient/processor, notice version, retention record, and owner. This supports an auditable fact base; it cannot decide coverage, role, permissibility, or adequacy of notice.
- **AI and trigger:** AI may reconcile approved inventory, release, and vendor metadata and identify changed flows. Legal/privacy humans approve classifications and scope. Refresh for a new purpose, sensitive-data flow, processor, recipient, or material product release.

### 2. Consent, rights, and opt-out experience package

- **Request and owner:** Consent/preference configuration evidence where used; universal-opt-out detection/handling design and test records where relevant; request and appeal procedures; redacted case logs; verification controls; response-quality samples; and support/engineering training and remediation records.
- **Validate and limit:** Independently inspect and reperform a de-identified or test-account journey from interface signal or request intake through routing, human decision, system action, response, and appeal record. This can evidence observable workflow behavior; it cannot decide a signal’s legal effect, authenticate a consumer, establish a lawful response, or prove all channels operate correctly.
- **AI and trigger:** AI may compare approved interface configurations to release inventories and flag missing case fields; it cannot honor a preference, authenticate a consumer, or decide an appeal. Human privacy, legal, and support owners decide outcomes. Recheck after interface, signal, request-channel, or release change.

### 3. Assessment, processor, and remediation-governance package

- **Request and owner:** Human-approved assessment/risk inputs for relevant processing; processor diligence and instruction records; security-operation references; exception and remediation decisions; management review; source-change watch; and retest results.
- **Validate and limit:** Trace a selected assessment input, processor change, or remediation item to factual basis, accountable authority, limitation, action owner, due date, and retest. This supports a reviewable governance record; it cannot decide assessment obligations, accept risk, determine cure/enforcement posture, or make a compliance conclusion.
- **AI and trigger:** AI may assemble source-linked packets and flag stale approvals. Legal, privacy, security, and leadership humans approve risk, contracts, representations, and closure. Review quarterly and renew scope annually.


## Cadence and renewal

Quarterly tests and annual scope reviews are internal conventions. Use verified current law for request, appeal, retention and assessment timing. Recheck recognized opt-out mechanisms and operative rules before release; preserve versioned test expectations. Reopen affected work after a new recipient, purpose, sensitive-data flow, interface, model, SDK, complaint trend or source change.

## Completion and handoff

Deliver applicability and obligation registers, actual data flows, notice/consent reconciliation, preference and rights test records, processor evidence, assessments and unresolved decisions. Distinguish drafted response, approved action, observed execution and verified delivery. State the next action, owner and missing evidence without relying on chat history; structural coverage alone cannot establish legal compliance.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
