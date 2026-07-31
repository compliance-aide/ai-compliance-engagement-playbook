# NIST SP 800-55 information-security measurement engagement guide

> Original operational guidance, not NIST text, a determination of control effectiveness, a budget decision, or a compliance claim. Confirm current material through [NIST SP 800-55 Volume 1](https://csrc.nist.gov/pubs/sp/800/55/v1/final) and [Volume 2](https://csrc.nist.gov/pubs/sp/800/55/v2/final).

## Engagement focus

Operate a measurement program that turns security questions into traceable, decision-useful evidence. Maintain a measure register that connects decision purpose, accountable owner, scope, source data, collection method, definitions, quality checks, baseline, target or threshold, limitations, reporting audience, decision use, corrective actions, and review date. Do not let a dashboard metric stand in for a conclusion about overall security or a specific control unless its limitations and supporting evidence are clear.

## Roles and annual rhythm

Security, risk, technology, finance, operations, privacy, compliance, internal-audit, and executive owners retain accountable decisions. Measure owners preserve definitions and source lineage; data owners attest to authorized collection and quality; management decides actions from reported results; and auditors evaluate evidence in their independent role. Independent reviewers sample measures from intended decision through source, transformation, quality review, report, and resulting action, and challenge proxies, stale baselines, selection bias, and unsupported claims.

AI may organize authorized measure metadata, flag missing definitions or aging baselines, compare reports against approved thresholds, draft review questions, and prepare non-authoritative workpapers. AI cannot collect data from unauthorized systems, alter source records, select a threshold, determine effectiveness, set a target, make investment decisions, accept risk, or claim compliance. Reassess measures after material objectives, systems, threats, services, or data changes; review the portfolio quarterly and conduct an annual independent readiness review.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [SP 800-55 Volume 1](https://csrc.nist.gov/pubs/sp/800/55/v1/final) and [Volume 2](https://csrc.nist.gov/pubs/sp/800/55/v2/final) publication records; capture the versions retrieved and applicable use terms. The packages below are original planning, not reproduced NIST material or proof that a measure establishes effectiveness.

### 1. Measure-design and decision package

- **Request and owner:** Security, risk, operations, finance, and measure owners provide the approved measure register, decision questions, scope, accountable owner, definitions, population, baseline/threshold rationale, known limitations, and report audience.
- **Validate and limit:** Trace a sampled measure from decision question to owner, definition, data population, stated limitation, and approved reporting use. This tests design traceability; it cannot select a threshold, determine effectiveness, or approve an investment decision.
- **AI and trigger:** AI may flag missing fields or conflicting definitions. Human owners approve definitions, targets, and intended use. Refresh after an objective, threat, system, or service change.

### 2. Data-lineage and quality package

- **Request and owner:** Data owners and measurement operators provide source-system listings, authorized extracts, collection schedules, transformation records, quality checks, access approvals, error records, and data-retention references.
- **Validate and limit:** Reperform a bounded sample from reported value to authorized source, transformation, quality check, and exception record. This assesses stated lineage; it cannot authenticate all source data, authorize collection, or repair records.
- **AI and trigger:** AI may reconcile supplied extracts and identify missing lineage or stale quality checks. Humans authorize access, resolve data defects, and retain source records. Recollect after a source, transformation, or quality-rule change.

### 3. Reporting, action, and independent-challenge package

- **Request and owner:** Management, risk, internal audit, and measure owners provide reports, distribution records, decision minutes, corrective-action tickets, exception/risk decisions, review workpapers, and follow-up evidence.
- **Validate and limit:** Trace sampled reported results to disclosed limitations, named decision owner, action or rationale, due date, and independent challenge. This does not accept risk, close remediation, or make an audit conclusion.
- **AI and trigger:** AI may prepare trend and overdue-action workpapers. Humans decide action, risk, and closure; independent reviewers challenge causal claims. Review quarterly and after a material adverse trend.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
