# NIST AI Risk Management Framework 1.0 — engagement guide

> Original operational guidance, not a declaration of trustworthy AI. Check the
> [NIST AI RMF source](https://www.nist.gov/itl/ai-risk-management-framework)
> and its revision status before each cycle.

## Engagement focus

Maintain a use-case inventory, accountable human roles, affected parties,
lifecycle state, decision impact, and unacceptable-risk boundaries. Create a
risk register covering intended benefit, foreseeable harm, data/model/supplier
dependencies, oversight, and evaluation limits. Revisit the record before
material changes and monitor performance, incidents, feedback, and drift.

## Roles and annual rhythm

Operators own system facts, approved monitoring, and event response. Independent
reviewers challenge high-impact claims and document limitations. AI organizes
inventory and evidence, summarizes evaluation results, and flags gaps; it cannot
self-assess trustworthiness or approve deployment. Review signals quarterly and
independently challenge the inventory and decisions annually.

## Tailored evidence plan

**Source and rights snapshot.** Use the current [NIST AI RMF source](https://www.nist.gov/itl/ai-risk-management-framework) and revision notices; reviewed 2026-07-31. This plan is original language and does not declare a system trustworthy, safe, fair, lawful, or fit for deployment. The accountable AI governance owner approves scope, risk decisions, and release decisions.

### 1. AI use-case, role, and impact inventory

- **Request and owner:** A versioned inventory of each use case, intended purpose, deployment context, model/data/provider dependencies, organization role, affected parties, and lifecycle state, owned by the product and AI-governance leads.
- **Validate and limit:** Trace a selected inventory record to approved product documentation, deployed configuration, and responsible owner. This can support a bounded governance view; it cannot establish the correct classification, anticipated impact, or legal role.
- **AI and trigger:** AI may reconcile authorized metadata and flag unowned or changed records. Humans approve intended use and risk boundaries. Refresh for model, data, provider, user population, geography, or intended-use changes.

### 2. Risk, evaluation, and limitation record

- **Request and owner:** Risk-register entries, evaluation protocol, authorized results, data-quality/provenance inputs, stated performance and limitation records, and response decisions from product, risk, and technical owners.
- **Validate and limit:** Reperform an approved result calculation or trace a selected claim to its evaluation source, measurement boundary, and human decision; preserve known blind spots. This can support transparent evaluation evidence, not a conclusion that all harms are controlled or results generalize.
- **AI and trigger:** AI may summarize approved results and identify missing evidence, but cannot create performance claims or accept residual risk. Refresh after a material evaluation result, model/data change, incident, or new affected-party signal.

### 3. Oversight, monitoring, and event-response evidence

- **Request and owner:** Human-oversight design and test artifacts, monitoring thresholds, change/release approvals, feedback or complaint handling, incident records, and post-event actions from operations and governance owners.
- **Validate and limit:** Trace a selected release or event to the oversight path, monitoring source, escalation, and corrective action. This can support that the declared process has records; it cannot prove human oversight is sufficient or that future behavior will remain acceptable.
- **AI and trigger:** AI may maintain a read-only event index and raise escalation candidates. Humans decide deployment, suspension, notification, and remediation closure. Review quarterly and after a material event or source revision.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
