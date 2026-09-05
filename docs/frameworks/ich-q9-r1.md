# ICH Q9(R1) quality-risk engagement guide

> Original operational guidance, not an ICH document, scientific conclusion or risk acceptance.

## Source and applicability

Use the [ICH Q9(R1) final guideline](https://database.ich.org/sites/default/files/ICH_Q9%28R1%29_Guideline_Step4_2025_0115.pdf). The document history identifies adoption on 18 January 2023 and a minor correction on 15 January 2025. ICH retains copyright in the source; this original workflow is not endorsed by ICH.

Source check 2026-09-04: document history, introduction, scope and principles read. The guideline connects scientific quality-risk evaluation to patient protection, includes availability risks arising from quality/manufacturing issues, and calls for proportionate effort and documentation. Risk management does not override regulatory requirements. Full methodology, annexes, regional implementation and applicable product requirements remain to be reviewed before execution.

## Engagement focus

Make each quality-risk decision understandable from its question, evidence, uncertainty, approved method, alternatives, action and follow-up. Cover the approved product/process lifecycle and dependencies, including quality-related supply interruption. A populated risk register is not evidence that its conclusions are sound.

## Roles

Quality and product owners establish scope. Qualified scientific and process experts assess hazards and evidence. The named decision-maker approves criteria, method, treatment and residual risk. An independent reviewer challenges assumptions, conflicts and missing coverage. AI can organize permitted records, check calculations against an approved method and draft questions; it cannot set acceptance thresholds, invent scientific estimates, accept risk, release product, authorize process changes or certify effectiveness.

## Before starting

Record product, process, site, lifecycle stage, patient-related concern, decision question, responsible team and decision deadline. Identify governing requirements, approved procedures, source versions and prior decisions. Define permitted evidence and workspace; keep batch records, confidential research and personal data outside this public repository. Production experiments, batch disposition and regulatory submissions require the applicable named authority.

## Ordered workflow

1. **Define the decision.** State what must be decided and why, including the affected product, process and availability scenario. Record assumptions, boundaries, mandatory constraints and accountable decision-maker. Return an ambiguous question for clarification before assigning risk values.
2. **Assemble the full evidence population.** Reconcile relevant deviations, complaints, process data, supplier information, changes and prior assessments. Preserve provenance, dates and conflicting findings. Record unavailable sources and the uncertainty they introduce; absence of incidents is not proof of zero probability.
3. **Approve the approach.** Qualified owners select the method, scales, criteria and degree of formality with rationale for uncertainty, importance and complexity. Record participant expertise and disagreements. Do not default every problem to a numerical matrix or choose scales after seeing the desired outcome.
4. **Assess and challenge.** Experts identify hazards, potential harm, existing controls and supporting data. Keep observations separate from estimates. Check units, scale definitions and calculation reproduction where applicable. Retain severe scenarios even when an aggregate number is low; equal aggregate scores can conceal different consequences. Escalate unsupported estimates instead of filling blanks with zero.
5. **Decide and authorize control.** Compare alternatives, expected effects, new risks and quality-related supply implications. Record the decision, rationale, owner, due date, residual uncertainty and required approval. Risk acceptance cannot waive a binding requirement. Link approved actions to the change-control system before implementation.
6. **Verify implementation and effectiveness.** Read back actual change records and test against the preapproved effectiveness objective. Distinguish installation, successful test execution and sustained effect. Keep failed observations and unresolved deviations visible; a signed action closure alone does not prove risk reduction.
7. **Communicate and review.** Provide the approved decision and its limits to responsible functions. Record receipt where an operational handoff is necessary. Reassess after new evidence, changes or failed controls, and at the approved review interval. Preserve earlier decisions and explain why conclusions changed.

## Evidence and test plan

The following packages restore the tailored plan with complete scoped accounting. Retain every relevant record supplied for assessment without silent trimming or sampling. Inventory completeness and scientific adequacy are separate questions; record what was actually examined and what remains untested.

### 1. Product and quality-risk context package

- **Request and owner:** Quality and product owners provide the defined product/process scope, intended use, decision context, quality attributes or hazards considered, accountable decision-maker, and dated information sources.
- **Validate and limit:** Reconcile all scoped risk records; trace each record from its stated context to its owner, source inputs, and decision boundary. This tests whether the record can be understood and located; it does not validate scientific conclusions or establish that every hazard was identified.
- **AI and trigger:** AI may organize authorized records and identify missing owners, dates, or assumptions. Qualified humans set the context and approve decisions. Refresh before a material product, process, supplier, or evidence change.

### 2. Risk-assessment rationale package

- **Request and owner:** Quality-risk and subject-matter owners provide the assessment approach, assumptions, uncertainty notes, participant roles, source references, and authorized assessment output.
- **Validate and limit:** Inspect every scoped assessment for a visible link between its approach, assumptions, evidence, uncertainty, and approved outcome. This supports traceability of reasoning; it cannot independently determine probability, severity, detectability, or the appropriateness of the chosen method.
- **AI and trigger:** AI may compare record fields, flag stale assumptions, and draft questions for reviewers. It must not select methods, score risk, or turn a synthesis into an accepted judgment. Reassess after new quality information, a deviation, or a material change.

### 3. Treatment, change, and effectiveness-follow-up package

- **Request and owner:** Process, quality, and change owners provide authorized treatment actions, implementation/change records, residual-risk decision records, follow-up observations, open deviations, and closure approvals.
- **Validate and limit:** Account for all treatment actions; trace each material action from risk decision through assigned owner, implementation evidence, follow-up, and authorized closure or escalation. This tests the documented chain; it cannot prove continuing effectiveness or accept residual risk.
- **AI and trigger:** AI may link actions to evidence and surface overdue follow-up. Humans approve treatment, residual risk, closure, and communications. Review at approved risk-based intervals and after a significant deviation, complaint, audit result, or change.


## Failure branches and decisions

- Missing scientific basis: mark the estimate unresolved and assign evidence retrieval; do not turn uncertainty into a low-risk score.
- Disagreement among experts: retain competing assumptions and evidence; the authorized decision-maker resolves or escalates with documented rationale.
- Control creates a new hazard or supply concern: reopen the assessment and obtain an approved decision before dependent changes.
- New evidence contradicts accepted risk: escalate immediately under the quality system; retain the original decision and chronology.
- Effectiveness test fails: preserve the failure, assign further action and retest; do not lower the acceptance criterion to close the item.

Use [agent runbook](../agent-runbook.md) statuses for evidence assertions: supported, not_supported, inconclusive, not_applicable and not_tested. These are not risk ratings. Split assertions about implementation, effectiveness and authorized acceptance.

## Cadence and renewal

Set review timing through the approved risk process and governing requirements; do not impose a universal quarterly or annual renewal. Include evidence-expiry and change triggers. A planned future review does not defer an urgent quality signal.

## Completion and handoff

Deliver the question and scope, complete evidence index, approved method and criteria, expert rationale, uncertainties, decision records, action evidence, effectiveness results and next review triggers. Every open item needs an owner and next action. Independent source, skeptical and rights review remain pending for this draft; no scientific validation or agent usability trial is implied by structural checks.

Fictional author desk case: a new alarm was installed and its task closed, but a synthetic challenge still fails to reach the designated operator. Installation is supported; alert delivery is not_supported; sustained risk reduction is not established. The quality owner must revisit the action and residual-risk decision. No production test or batch decision occurred.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for applicability, authority, evidence, technical-test, exception, source-change and renewal records.
