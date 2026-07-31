# CERT Resilience Management Model — engagement guide

> Original operational guidance, not a CERT appraisal or an SEI publication.
> Use authorized material and review the [SEI CERT-RMM collection](https://www.sei.cmu.edu/library/cert-resilience-management-model-cert-rmm-collection/).

## Engagement focus

Start with mission-critical services and disruption tolerance. Name owners for
services, assets, suppliers, people, technology, risk, and recovery; test
whether operational processes survive staff changes and disruption; exercise
selected scenarios; and maintain an improvement portfolio tied to measurable
resilience outcomes.

## Roles and annual rhythm

Leadership owns priorities and residual-risk decisions. Independent reviewers
evaluate evidence and scenario outcomes. AI may map service dependencies, authorized evidence,
and missing ownership and draft scenario questions and summaries, but cannot
make an appraisal rating, accept residual risk, approve recovery decisions, or alter services. Conduct leadership review annually and after material
service or threat changes.

## Tailored evidence plan

**Source and rights snapshot.** Use authorized material from the [SEI CERT-RMM collection](https://www.sei.cmu.edu/library/cert-resilience-management-model-cert-rmm-collection/), the organization’s service and recovery context, and approved source-access terms; checked 2026-07-31. This plan is original evidence-planning guidance, not reproduced CERT-RMM material, an SEI appraisal, or a resilience rating. Leadership retains service-priority, residual-risk, and recovery decisions.

### 1. Critical-service, asset, and dependency package

- **Request and owner:** Service, business, technology, supplier, and resilience owners provide critical-service inventory, disruption-tolerance statements, service-owner assignments, asset and dependency maps, supplier commitments, recovery assumptions, and scope-change records.
- **Validate and limit:** Trace one critical service to its accountable owner, stated disruption tolerance, material dependency, supplier or shared-service record, and latest review date. This supports a reviewable service fact base; it cannot prove complete dependency discovery, validate supplier performance, or approve recovery priorities.
- **AI and trigger:** AI may organize authorized inventories and flag inconsistent owner, dependency, or review-date metadata. Humans approve service criticality, tolerance, and scope. Refresh after a service launch, retirement, material supplier change, architecture change, or business-priority change.

### 2. Resilience-operation and disruption-exercise package

- **Request and owner:** Process, incident, continuity, technology, people, and facilities owners provide operating procedures in original language, role/handoff records, exercise design approvals, scenario records, dated exercise outputs, communications logs, recovery evidence, and observed limitations.
- **Validate and limit:** Trace one approved scenario from service context through designated participants, exercise execution, recorded outcome, exception, and accountable follow-up. This can support a bounded observation about preparedness evidence; it cannot prove real-event resilience, establish all recovery capabilities, or authorize service changes.
- **AI and trigger:** AI may sequence authorized evidence, identify missing timestamps or owners, and draft challenge questions. Humans approve scenarios, exercise methods, safety boundaries, conclusions, and production changes. Recollect after an exercise, incident, material staffing change, or recovery-process revision.

### 3. Risk, improvement, and independent-challenge package

- **Request and owner:** Leadership, risk, service, and program owners provide risk decisions, improvement portfolio, corrective actions, resource decisions, target dates, retest evidence, management-review records, and independent-review workpapers.
- **Validate and limit:** Trace a selected resilience gap from source observation through human priority and residual-risk decision, action owner, follow-up, and open limitation. This supports governance traceability; it cannot accept residual risk, issue an appraisal, or certify completion.
- **AI and trigger:** AI may flag overdue actions and prepare non-authoritative workpapers. Humans approve risk acceptance, resource allocation, recovery decisions, closure, and external statements; independent reviewers challenge evidence without managing services. Refresh after failed exercise, incident, missed target, threat change, or annual leadership review.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
