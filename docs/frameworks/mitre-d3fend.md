# MITRE D3FEND — defensive knowledge-graph engagement guide

> Original operational guidance, not an audit standard or efficacy certification. Version-pin the [MITRE D3FEND resource](https://d3fend.mitre.org/api-docs/) used in an engagement.

## Engagement focus

Define architecture and defense questions, approved data, selected defensive patterns, and supporting evidence. Preserve system context and version history; use engineering tests or tabletops to determine whether intended protective behavior occurs; track gaps, dependencies, and design decisions.

## Roles and annual rhythm

Architecture and defense owners maintain evidence and test outcomes. Independent reviewers challenge the link between modeled capability and observed operation. AI can discover related evidence, draft narratives, and flag missing verification; it cannot infer effectiveness, deploy changes, or certify defenses. Review changes continuously and evidence annually.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [MITRE D3FEND resource and API documentation](https://d3fend.mitre.org/api-docs/) selected by architecture and defense owners; record the version/date of the resource used. Retrieved 2026-07-31. This guide is original planning, not a reproduction of D3FEND data, a control catalogue, or a claim that a defensive technique is effective.

### 1. Architecture question and defensive-pattern boundary

- **Request and owner:** Approved architecture/security question, system/component and trust-boundary diagram, selected defensive-pattern reference, dependency/assumption record, data-sensitivity boundary, and named architecture, engineering, and defense owners. Cover the documented release or operating context selected for review.
- **Validate and limit:** Trace selected pattern references to the stated architecture question, system boundary, assumptions, and accountable owner. Avoid publishing sensitive diagrams or exploitation context. This supports an intelligible design record; it cannot prove the pattern is suitable, implemented, secure, or effective.
- **AI and trigger:** AI may index approved relationship metadata and flag missing owner, dependency, or version data. Humans decide pattern selection, architecture tradeoffs, and scope. Trigger on architecture change, material dependency change, threat-model update, or annual design review.

### 2. Defensive implementation and engineering-test trace

- **Request and owner:** Human-approved design/implementation references, configuration/change records, test-plan authorization, non-production test results, defects/limitations, and named engineering, platform, and security-test owners. Bound sampling to the selected component/release and authorized environment.
- **Validate and limit:** Reperform a read-only review of a selected implementation from approved design decision through change record and authorized test evidence. Do not deploy, alter controls, or execute adversarial activity. This can support a trace from intended pattern to test record; it cannot prove protection, absence of defects, or production effectiveness.
- **AI and trigger:** AI may compare approved design, test, and change metadata and draft questions about missing links. Humans approve code/configuration, test scope, and release decisions. Trigger on release, test failure, configuration drift, or material design change.

### 3. Operational observation, exception, and improvement record

- **Request and owner:** Monitoring/operational observation summaries, incident or exercise references, exception/risk decisions, remediation backlog, retest evidence, and closure records from defense operations, engineering, architecture, and risk owners.
- **Validate and limit:** Trace selected observations or exceptions to the affected defensive pattern, decision owner, remediation/deferral, and follow-up evidence. Keep raw logs and sensitive incident details out of public materials. This supports accountable improvement history; it cannot establish causal prevention, resilience, or complete operation.
- **AI and trigger:** AI may cluster approved observations and flag unlinked exceptions or stale retests. Humans decide severity, risk acceptance, remediation, and closure. Trigger on material incident/exercise finding, control exception, dependency failure, or annual review.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
