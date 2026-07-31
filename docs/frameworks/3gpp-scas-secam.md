# 3GPP SCAS / SECAM — telecom assurance guide

> Original operational guidance, not a 3GPP evaluation result. Consult the [3GPP SCAS overview](https://www.3gpp.org/technologies/scas-cert).

## Engagement focus

Maintain product classes, releases, functions, suppliers, relevant versions, test records, vulnerabilities, dispositions, and change evidence.

## Roles and annual rhythm

Product owners maintain records; external schemes and labs remain independent. AI maps assets and stale evidence, but cannot reproduce specifications or claim evaluation results. Review releases and annually.

## Tailored evidence plan

**Source and rights snapshot.** Use the [3GPP SCAS overview](https://www.3gpp.org/technologies/scas-cert), checked 2026-07-31, to identify the applicable assurance context and current publication path. This is original planning language: it does not reproduce 3GPP specifications, define a test method, decide product eligibility, or assert a laboratory evaluation result. Product, security, legal, and scheme/lab contacts retain all release, applicability, submission, and external-claim decisions.

### 1. Product and evaluation-scope record

- **Request and owner:** Product, engineering, and security owners provide the selected product class, product/model identity, release and build identifiers, enabled functions and interfaces, deployment assumptions, supplier/component context, and the dated human decision explaining which assurance path is being explored.
- **Validate and limit:** Trace a human-selected release from catalogue entry through version/build evidence, owned functions, applicable test or assurance request, and approval record. This supports release traceability; it cannot determine whether a product is in scope, establish conformance, or replace a scheme decision.
- **AI and trigger:** AI may reconcile supplied version and ownership metadata, identify missing links, and prepare a read-only evidence index. Humans approve scope and release decisions. Refresh before a material feature, interface, component, deployment, supplier, or version change.

### 2. Security-test, vulnerability, and change package

- **Request and owner:** Security and engineering owners provide authorized test plans/results, defect and vulnerability records, remediation/change records, component provenance, release approvals, and evidence of security-relevant regression or retest activity.
- **Validate and limit:** Follow a selected reported weakness or test observation to accountable triage, decision, implemented change, retest reference, and release disposition. This supports a bounded corrective-action trail; it cannot prove complete coverage, sustained security, or evaluation success.
- **AI and trigger:** AI may classify supplied records and flag stale remediation dates; it cannot run tests against production systems, alter results, or decide a disposition. Recollect after a material finding, remediation, release candidate, dependency change, or test-method change.

### 3. Independent evidence handoff and claim-control workpaper

- **Request and owner:** Product, assurance, legal, and communications owners provide evidence-request lists, authorized handoff records, independent lab or scheme correspondence where shareable, external-claim drafts, exception decisions, and management approvals.
- **Validate and limit:** Trace a selected external statement or handoff package to source version, accountable reviewer, retained support, and approval date. This supports disciplined claim control; it cannot certify a product, interpret scheme rules, or substitute for an independent laboratory.
- **AI and trigger:** AI may prepare an access-controlled checklist and flag unsupported claim language. Humans authorize submissions, disclosure, exceptions, and public statements. Review before any external handoff or statement and annually while the product remains marketed.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
