# DAMA-DMBOK-informed data-management engagement guide

> Original operational guidance, not DAMA content, endorsement, or certification. Consult [DAMA’s DMBOK revision information](https://www.damadmbok.org/dmbok2-revisions).

## Engagement focus

Maintain enterprise data domains, authoritative sources, governance decisions, stewardship, quality incidents, privacy/security/retention dependencies, and remediation evidence.

## Roles

Data owners approve definitions and corrections; independent reviewers test stewardship evidence. AI enriches catalogs and flags duplicates, but cannot ingest restricted DMBOK material, accept risk, or certify. Review quarterly and annually.

## Source and applicability

Use DAMA's [revision information](https://dama.org/dama-dmbok-revision/) to identify the authorized edition. DAMA describes the 2024 DMBOK 2.0 revision as maintenance rather than a changed overarching framework. Record edition, language, access rights and any approved local interpretation. Do not treat a future edition under development as the current operating source.

This is a DMBOK-informed improvement engagement, not a mandatory legal control checklist or organizational certification. Management chooses the business outcomes and accountable data domains; reviewers document coverage and justified deferrals across the selected source. Do not convert chapter completion, catalog size or personal certification into proof of organizational data-management maturity.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Identify business data owners, stewards, engineering, consumers, privacy, security and records owners. Define the decision or process the data must support, the evaluated period and authoritative sources. Use approved metadata or synthetic records; access to a catalog does not authorize exporting underlying personal or confidential values. Create one work item per domain/critical element/problem with owner, expected outcome and evidence.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Define business outcomes | Data owners identify decisions, processes and affected consumers. | Approved problem statement, scope and success measures; no tool-first catalog project without a use case. |
| 2. Establish ownership and meaning | Stewards reconcile definitions, authoritative sources and decision rights. | Versioned definitions with owner approval and disputed meanings retained. |
| 3. Trace the lifecycle | Engineering maps collection, storage, transformations, sharing, consumption and disposal. | Source-to-consumer lineage with unknown/manual steps and handling dependencies visible. |
| 4. Specify quality expectations | Owners approve rules, population, thresholds, frequency and business consequences. | Measurable tests and justified acceptance criteria; AI does not invent thresholds. |
| 5. Measure and investigate | Authorized reviewers profile approved data and reconcile totals, failures and missing coverage. | Reproducible results with query/version, evaluated population and limitations; failed collection is not zero defects. |
| 6. Correct the cause | Owners approve source/process changes and downstream repair plans. | Impact analysis, change authorization and affected consumers; no silent overwriting of authoritative records. |
| 7. Verify the result | Reviewers repeat the approved rules and trace corrected data through downstream uses. | Before/after evidence using comparable populations and rules, plus unresolved historical effects. |
| 8. Govern and sustain | Owners review outcomes, sharing/retention decisions and recurring issues. | Approved stewardship handoff, monitoring owners and renewal triggers; maturity claims require separate supported methodology. |

## Failure branches and decisions

- **Two systems both claim authority:** record the conflicting definitions and uses; route the decision to accountable business owners instead of merging by AI confidence.
- **Quality rate improves after rows disappear:** reconcile the denominator and exclusions before accepting improvement; missing records may be a new defect.
- **Lineage stops at a spreadsheet:** retain the manual transformation and request owner evidence; do not draw an invented automated link.
- **Duplicate candidate may represent two people:** preserve both records and use approved matching/review procedures; never auto-merge based only on similar names.
- **Correction fixes a dashboard but not the source:** trace recurrence and downstream copies; cosmetic repair alone does not close the root cause.
- **Retention and business-use requirements conflict:** preserve the decision and request privacy/legal/records review; AI cannot authorize indefinite storage or deletion.

## Evidence and test plan

**Source and rights snapshot.** Consult DAMA's [DMBOK revision information](https://www.damadmbok.org/dmbok2-revisions) and use any DMBOK material only through authorized access; prior snapshot 2026-07-31; revalidate edition and rights. This is original, DMBOK-informed operational guidance and does not reproduce protected framework text, taxonomy, or certification criteria. A named data-governance owner confirms source rights and engagement scope.

### 1. Data-domain, ownership, and definition record

- **Request and owner:** Approved data-domain inventory, critical-data-element list, authoritative-source record, business definitions, classification/handling dependencies, stewardship assignments, and decision history from data owners and stewards.
- **Validate and limit:** Trace a selected critical element to its accountable owner, approved definition, authoritative source, consuming process, and dated decision. This can support transparent stewardship; it cannot establish semantic correctness, legal classification, or enterprise completeness.
- **AI and trigger:** AI may compare approved metadata, flag duplicate candidates, and draft questions without ingesting restricted content or sensitive values. Humans approve definitions, authoritative sources, and classifications. Refresh after a new domain, source, material use, ownership, or classification change.

### 2. Data quality, lifecycle, and issue-response evidence

- **Request and owner:** Approved quality rules/thresholds in original language, profiling or monitoring outputs, issue tickets, lineage/change records, retention/disposal dependencies, correction approvals, and retest evidence from stewardship, engineering, privacy, and records owners.
- **Validate and limit:** Inspect a selected data issue from detection through impact assessment, assigned steward, correction/change record, and retest or documented exception. This supports a bounded account of issue handling; it cannot prove data accuracy, complete lineage, or compliant retention.
- **AI and trigger:** AI may index sanitized quality metadata and flag unresolved ownership or aged issues; it cannot change data, select thresholds, authorize deletion, or approve a correction. Humans approve remediation and lifecycle decisions. Refresh after a quality failure, source/interface change, privacy/security event, or retention-rule change.

### 3. Governance, sharing, and annual stewardship review

- **Request and owner:** Governance meeting records, access/sharing decision references, supplier or consumer data agreements where authorized, metrics, unresolved exceptions, and quarterly/annual stewardship reviews from governance, privacy, security, and business owners.
- **Validate and limit:** Trace a selected sharing or stewardship exception to approved purpose, authority, conditions, review date, and resulting action. This can support accountable oversight; it cannot determine legal permission, contractual sufficiency, or certify data management maturity.
- **AI and trigger:** AI may prepare a source-linked review packet and flag stale approvals. Legal and human governance authorities approve sharing, exceptions, risk acceptance, and external claims. Review quarterly and renew the stewardship record annually.


## Cadence and renewal

Quarterly and annual stewardship reviews are planning conventions. Set operational checks from data-change frequency and consequence of error. Reopen work after source/schema changes, new consumers, changed definitions, ownership transitions or privacy/security events. Preserve rule versions and population definitions so trends remain interpretable.

## Completion and handoff

Deliver the outcome/scope record, owner-approved definitions, lineage, quality rules, population reconciliation, issue decisions and downstream retests. Distinguish drafted metadata from approved semantics and verified operation. Every unresolved item needs an owner, next action and evidence requirement without earlier chat. A populated catalog does not prove accurate data or complete governance.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
