# Colorado AI law — engagement guide

> Original operational guidance, not legal advice. Treat the current framework as prospective and verify the [Colorado Attorney General AI page](https://coag.gov/ai/) before use.

## Engagement focus

Identify consequential-decision workflows and organizational role; maintain decision-data lineage, outcome review, notices, correction/human-review, vendor, complaint, and remediation evidence; refresh after material changes.

## Roles

Operators track workflow evidence; independent reviewers sample outcomes and remediation. AI may flag potential coverage and assemble case evidence, but cannot decide applicability, make or reconsider decisions, issue notices, or respond to regulators. Review quarterly and annually.

## Source and applicability

The [Attorney General page](https://coag.gov/ai/), checked September 4, 2026, identifies SB26-189 as replacing the 2024 provisions with an automated decision-making technology (ADMT) law effective January 1, 2027. It identifies developer/deployer requirements and personal-data request/correction rights. Proposed rules filed August 11, 2026 remain drafts on that page. Do not treat proposed text as final law or reuse an old high-risk-AI checklist without reviewing the replacement.

Use the [SB26-189 official legislative record](https://www.leg.colorado.gov/bills/SB26-189), enacted text and current rulemaking together. This guide focuses on consequential-decision workflows. Screen conversational-service features separately for the Chatbot Safety Act identified by the Attorney General; do not assume this guide covers that separate regime. Preserve distinct effective dates, source versions and applicability decisions.

The risk and fairness work below is original readiness guidance. It is not a claim that the replaced statute's impact-assessment or reasonable-care duties remain unchanged. Counsel must map each asserted legal obligation to the enacted successor and any effective final rules.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Name legal, product, decision-operation, data and vendor owners. Inventory actual uses of model outputs, including recommendations or rankings that influence a later human decision. Human involvement alone does not resolve statutory coverage. Keep real case data in approved environments and use synthetic cases for workflow demonstrations.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Freeze the source basis | Legal owner records enacted provisions, effective dates and proposed-versus-final rule status. | Versioned obligation register; superseded assumptions remain traceable but cannot silently govern current plans. |
| 2. Map actual decision use | Product and business owners trace input data, model/vendor version, output, human action and consequential outcome. | Workflow inventory with population, purpose, role and unresolved coverage questions. |
| 3. Decide applicability | Counsel evaluates each workflow, organizational role and exception against current definitions. | Approved decision with source rationale; unknown coverage stays open rather than defaulting to exempt. |
| 4. Build complete readiness coverage | Agent maps every applicable obligation to owner, evidence, implementation task and due date. | Full register separating legal requirements, draft-rule scenarios and voluntary risk controls. |
| 5. Reconcile provider information | Engineering and procurement owners obtain documentation for actual deployed versions and compare intended use, limitations and review instructions with local operation. | Version-linked evidence and unresolved mismatches; a generic vendor statement does not establish appropriate use. |
| 6. Exercise consumer workflows | Authorized testers use synthetic requests to trace notices, data retrieval/correction and applicable human-review paths through all affected components. | Observed results, timing, owners and limitations; a policy promise is not working execution. |
| 7. Correct and retest | Owners implement approved fixes; reviewers check both system changes and the resulting decision/communication workflow. | Retest evidence and unresolved findings; no automated adverse decision or reconsideration by the drafting agent. |
| 8. Approve and monitor | Legal and accountable leaders review readiness, claims and future source changes. | Approved deployment/communication decisions where required, monitored changes and clear next actions; no automatic compliance declaration. |

## Failure branches and decisions

- **Old legal checklist:** retain useful evidence, but remap obligations to the replacement law before claiming coverage.
- **Draft rule supplies a detail absent from enacted text:** track it as a planning scenario and assign a source-watch owner; do not label it an effective requirement.
- **Model version changed without provider documents:** identify affected workflows and prevent unsupported reuse of old assurances.
- **Correction stops in one database:** trace downstream decision inputs and caches before reporting complete execution.
- **Fairness metric looks good but complaints persist:** preserve both signals and investigate scope and subgroup limitations; do not infer absence of discrimination from a single aggregate.

## Evidence and test plan

**Source and rights snapshot.** Use the official [Colorado Attorney General AI page](https://coag.gov/ai/), current Colorado statutes/rules identified from that source, and qualified Colorado legal counsel; prior snapshot dated 2026-07-31; revalidate the amended law and rule status before use. This original plan is prospective operational preparation, not legal advice, a determination of covered developer/deployer status, a high-risk-system classification, an impact-assessment conclusion, or a compliance representation.

### 1. Consequential-decision workflow and role boundary

- **Request and owner:** Inventory of AI-assisted decision workflows; intended decision/use record; affected population and deployment context; model/system and vendor components; human-review/override design; release identifiers; and named product, business, HR/operations, engineering, privacy, and legal owners. Preserve the human-approved scope assumptions and unknowns.
- **Validate and limit:** Trace a selected workflow to its business decision, owner, model/service version, input/output context, vendor/dependency record, human-review point, and counsel-reviewed applicability question. This supports a factual workflow packet; it cannot decide whether the system, decision, organization, or person is covered or classify a system as high risk.
- **AI and trigger:** AI may compare approved inventories with deployment metadata and flag missing owners, version records, or review gates. Legal and accountable business humans decide scope and role. Refresh before a new consequential workflow, new AI provider/model, materially changed output use, or deployment context change.

### 2. Risk, fairness, and human-oversight evidence

- **Request and owner:** Human-approved impact/risk review inputs; intended-use and limitation record; data/feature provenance summaries; testing and outcome-monitoring references; human-review/override and escalation procedures; reviewer training; documented remediation decisions; and governance approval records.
- **Validate and limit:** Sample a selected workflow or release from approved risk inputs through test references, named reviewer, observed limitation, human oversight or escalation design, remediation action, and retest. Use de-identified or synthetic evidence where possible. This can support traceability of the organization’s process; it cannot demonstrate absence of bias, prove validity, decide reasonable care, or establish an impact-assessment result.
- **AI and trigger:** AI may organize approved test metadata, identify missing approvals, and draft review questions; it cannot set decision criteria, make/reconsider an outcome, approve a risk decision, or declare a workflow fair. Humans approve deployment, risk treatment, remediation, and closure. Trigger after material model/data/threshold/purpose change, anomaly, complaint pattern, or failed monitoring.

### 3. Notice, feedback, vendor, and incident/change governance

- **Request and owner:** Human-approved notice and internal/external communication records where applicable; feedback/complaint intake and de-identified case trail; vendor due-diligence, responsibility, and change notices; incident/rollback evidence; source-change watch; and management review/resolution records.
- **Validate and limit:** Trace a selected feedback, vendor change, or material incident to the affected workflow, responsible owner, decision/escalation, communication approval, remediation or rollback, and subsequent review. This supports accountable governance; it cannot determine notice obligations, decide an individual outcome, establish a response’s legal sufficiency, or report to a regulator.
- **AI and trigger:** AI may classify approved internal metadata for triage and flag aging cases or vendor/model changes; it cannot issue notices, respond externally, bind the organization, make a filing, or close a complaint. Authorized humans decide communications, regulatory interactions, risk acceptance, and closure. Review quarterly and on a material workflow, vendor, incident, or legal-source change.


## Cadence and renewal

Quarterly review and annual reconciliation are internal planning conventions unless an applicable source establishes a specific duty. Refresh on model, data, threshold, intended-use, population, vendor, complaint or legal-source changes. Recheck final rules before the operative milestone; a dated prospective plan is not evidence of compliance after commencement.

## Completion and handoff

Deliver the source/version register, workflow applicability decisions, complete obligation coverage, provider records, synthetic test results, open gaps and human-approved next actions. Label prospective, draft-rule and effective obligations distinctly. Identify the next action, owner and evidence needed without prior chat history; preserve statutory interpretation and individual outcome decisions for authorized humans.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
