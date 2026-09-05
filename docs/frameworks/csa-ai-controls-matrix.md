# CSA AI Controls Matrix — engagement guide

> Original operational guidance, not CSA control content or a STAR declaration. Consult the [CSA AICM artifact](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1).

## Engagement focus

Maintain AI use-case, model, vendor, dataset, integration, autonomy, human-oversight, evaluation, red-team, incident, and retirement records.

## Roles

Security, privacy, product, and legal owners approve risk; independent reviewers test evidence. AI normalizes evidence and stale reviews, but cannot reproduce controls, score, make declarations, or approve external claims. Review quarterly and annually.

## Source and applicability

Use the [AICM v1.1 package](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1). CSA identifies 247 objectives across 18 domains; older 243-objective inventories need version reconciliation. Its [July 2026 release explanation](https://cloudsecurityalliance.org/blog/2026/07/14/ai-controls-matrix-v1-1-strengthening-the-foundation-for-trustworthy-ai) distinguishes the matrix, 320-question AI-CAIQ, implementation guidance and auditing guidance. Record the version of each artifact actually used. A completed questionnaire is not equivalent to tested controls or a STAR certification.

Assign responsibility using actual model-provider, cloud-provider, orchestrator, application-provider and customer activities. One organization may perform several roles. Review applicability against architecture and lifecycle; retain every matrix objective with its disposition, including justified non-applicability. Mappings identify review leads, not automatic compliance with another standard or law. Verify permitted use before importing or redistributing matrix or mapping content.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Freeze the evaluated system configuration: model/provider/version, prompt and policy version, retrieval sources, tools, permissions, data flows and environment. Identify authorized testing boundaries, synthetic data, cost limits and rollback authority. Create one work item per applicable control/system/role combination, with owner, evidence request, test expectation and reviewer. Full official matrix and guidance access are prerequisites to complete control coverage.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Establish scope | Product and governance owners identify use cases, affected users, deployments and lifecycle stages. | Approved boundary and versioned dependency inventory; shadow integrations remain assigned gaps. |
| 2. Reconcile the matrix | Control owner checks the complete selected release and related guidance. | All objectives accounted for, with changes from the prior version visible; no keyword-selected subset. |
| 3. Allocate responsibility | Architecture and procurement owners assign implementation and evidence duties across providers and customer teams. | Named accountable owner and interface evidence for each shared duty; vendor ownership does not imply implementation. |
| 4. Specify expected safeguards | Technical owners document control operation, failure behavior and measurable test expectations. | Approved test plan and evidence sources tied to actual model, data, tools and permissions. |
| 5. Collect and evaluate evidence | Authorized reviewers inspect design and operation, and execute approved QA tests. | Reproducible workpapers with environment, inputs, expected/observed behavior and limitations; standard runbook results remain separate from formal ratings. |
| 6. Reconcile questionnaire answers | Owners link each applicable AI-CAIQ response to underlying control evidence and reviewer decisions. | Contradictions, missing supplier evidence and unsupported assertions remain explicit rather than converted to affirmative answers. |
| 7. Remediate and retest | Owners correct approved gaps; reviewers repeat affected tests and examine connected dependencies. | Verified changes tied to the evaluated release, with residual issues and rollback decisions retained. |
| 8. Review and monitor | Independent reviewers challenge coverage; accountable leaders approve representations and monitoring. | Scoped assurance packet, source-change watch, model-change triggers and next actions; registry submission is a separate authorized action. |

## Failure branches and decisions

- **Provider silently changes the model:** record observed version uncertainty and invalidate affected evidence assumptions; establish the new boundary before reusing evaluation results.
- **Supplier says a control is inherited:** request service-, role- and period-specific support plus customer configuration duties. Unsupported inheritance stays inconclusive.
- **Prompt injection reaches a tool:** preserve safe QA evidence, actual permission path and affected actions; route remediation and incident review without repeating the attack against production.
- **Evaluation passes but oversight fails:** record both results. A human-approval policy does not prove that tool execution waits for an authorized human.
- **Questionnaire and test disagree:** retain the contradiction and ask the owner/reviewer to resolve the answer; never edit evidence to match the declaration.
- **Retired model leaves data or credentials:** inventory remaining copies, endpoints and secrets; require disposal/revocation evidence before lifecycle closure.

## Evidence and test plan

**Source and rights snapshot.** Use the official [CSA AI Controls Matrix artifact](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1) and current CSA terms; prior snapshot 2026-07-31; revalidate version and terms. CSA artifacts may carry use conditions. This is original AI-governance evidence planning, not reproduced matrix content, a control score, a STAR declaration, or a claim of conformance. Authorized humans confirm source rights, applicable version, scope, and external-use decisions.

### 1. AI system, data, and accountability package

- **Request and owner:** Product, AI-governance, security, privacy, and procurement owners provide use-case and system inventory, intended use, model/provider/version records, data categories and provenance references, integrations, affected parties, lifecycle status, and named accountable owners.
- **Validate and limit:** Trace a selected AI system to its approved intended use, deployed configuration reference, model/data/supplier dependency, and accountable owner. This can identify undocumented scope or ownership drift; it cannot classify the system, prove data suitability, or establish that all risks are controlled.
- **AI and trigger:** AI may reconcile authorized metadata and flag unowned systems, changed providers, or stale reviews. Humans approve use, data, supplier, and risk-boundary decisions. Refresh after model, data, provider, integration, intended-use, geography, or affected-population changes.

### 2. Evaluation, oversight, and operational-safeguard package

- **Request and owner:** Technical, product, security, privacy, and operations owners provide approved evaluation protocols/results, performance and limitation records, human-oversight design/tests, access/change records, monitoring thresholds, incident/feedback records, and remediation decisions.
- **Validate and limit:** Sample a material AI behavior, release, or event from evaluation/oversight evidence through monitoring source, human decision, and corrective action. This can test evidence traceability and declared safeguards; it cannot determine trustworthiness, fairness, safety, legal compliance, or future model behavior.
- **AI and trigger:** AI may summarize approved results and flag missing evidence or expired review dates, without fabricating a result or changing a system. Humans approve deployment, thresholds, incident response, and remediation closure. Refresh after material evaluation findings, model change, incident, or failed safeguard test.

### 3. Supplier, assurance, and independent-challenge package

- **Request and owner:** Procurement, security, legal, product, and independent-review owners provide supplier assessments/contract references, external-claim inventory, residual-risk decisions, exception register, review workpapers, remediation/retest evidence, and approved communications.
- **Validate and limit:** Trace a selected supplier or external AI claim to relevant evidence, authority, limitation, due date, and independent challenge. This can reveal unsupported dependency or assurance assertions; it cannot approve a supplier, accept risk, make a declaration, or attest for management.
- **AI and trigger:** AI may compare supplied claims with evidence citations and escalate gaps. Humans approve supplier decisions, exceptions, risk acceptance, and external statements. Review quarterly, before material claims, and after supplier, contract, or assurance changes.


## Cadence and renewal

Quarterly and annual reviews are planning conventions, not universal CSA deadlines. Reopen affected work after model, retrieval, prompt, tool, permission, supplier, intended-use or autonomy changes. Monitor real operating failures and feedback against approved thresholds; a previous benchmark result does not predict all future behavior.

## Completion and handoff

Deliver the complete objective-disposition register, role responsibilities, configuration snapshot, evidence/test workpapers, questionnaire reconciliation and unresolved decisions. Identify what was drafted, executed, verified and approved. Name the next owner, action and evidence needed without chat history. Keep preparation, self-assessment, independent assurance and published claims distinct.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
