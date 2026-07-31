# UNECE R156 — vehicle software-update engagement guide

> Original operational guidance, not type approval or release approval. Check the [UNECE regulation source](https://unece.org/transport/documents/2021/03/standards/un-regulation-no-156-software-update-and-software-update).

## Engagement focus

Maintain update-capable types, market scope, update decisions, validation, deployment, rollback, version identification, and post-release evidence.

## Roles and annual rhythm

Humans approve releases and submissions; independent reviewers perform evidence retrieval tests. AI correlates version/release records, but cannot approve releases or make filings. Reconcile monthly and review annually.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [UNECE Regulation No. 156 source](https://unece.org/transport/documents/2021/03/standards/un-regulation-no-156-software-update-and-software-update), checked 2026-07-31, and confirm applicable market, amendment, vehicle type, and approval route with homologation/legal owners. This is original operational guidance, not regulation text, a software-update-management-system conclusion, type approval, or release authorization.

### 1. Update-capable type and software-identity package

- **Request and owner:** Vehicle program, software release, configuration management, homologation, and supplier owners provide vehicle-type and market records, update-capable component inventory, software/version identifiers, component ownership, supplier boundaries, and approved configuration-baseline references.
- **Validate and limit:** Trace one software item from vehicle/component boundary through version identity, accountable owner, supplier relation, and approved baseline reference. This supports identification traceability; it cannot verify installed state, applicability, or type-approval scope.
- **AI and trigger:** AI may compare supplied version metadata and flag missing owners or inconsistent identifiers. Humans decide configuration baselines and market applicability. Refresh for a new type, component, supplier, software branch, or market.

### 2. Update decision, validation, and release package

- **Request and owner:** Product, engineering, quality, cybersecurity, safety, and release owners provide update rationale, impact/risk decision records, build and validation references, approval gates, deployment/rollback plan, release notes, exception decisions, and supplier assurance links.
- **Validate and limit:** Trace a selected update from approved rationale and affected baseline through validation/reference records, authorized release decision, deployment/rollback preparation, and exception or remediation status. This cannot prove update safety, security, technical correctness, or authorize release.
- **AI and trigger:** AI may organize approved release metadata and flag absent reviews or rollback owners. Qualified humans approve tests, release, risk treatment, and exceptions; AI cannot alter vehicles or initiate deployment. Trigger on an emergency update, vulnerability, failed validation, or supplier/component change.

### 3. Deployment, post-release, and approval-readiness package

- **Request and owner:** Operations, support, quality, incident response, homologation, legal, and records owners provide controlled deployment records, success/failure/rollback telemetry summaries, field reports, issue triage, corrective actions, external-communication authority, evidence index, and retention decisions.
- **Validate and limit:** Trace a selected deployment or post-release event to targeted version/type, authorized owner, monitored result, escalation, corrective action, and closure/review record. This supports evidence retrieval; it cannot establish fleet-wide installation, safety, update effectiveness, or reporting duty.
- **AI and trigger:** AI may correlate sanitized deployment and issue metadata and flag unresolved actions. Humans decide field measures, notifications, filings, and closure. Reconcile monthly, and refresh after a field event, rollback, regulation change, or annual review.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
