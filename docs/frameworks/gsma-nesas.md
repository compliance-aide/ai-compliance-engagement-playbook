# GSMA NESAS — telecom assurance engagement guide

> Original operational guidance, not scheme content, laboratory evaluation or product certification. Draft pending independent source, skeptical and rights review.

## Source and applicability

Use the [GSMA documentation catalog](https://www.gsma.com/solutions-and-impact/technologies/security/nesas-documents/?tab=documents), [results directory](https://www.gsma.com/solutions-and-impact/technologies/security/nesas-results/?tab=product) and [recognized laboratories](https://www.gsma.com/solutions-and-impact/technologies/security/nesas-security-test-laboratories-2/). Indexed official descriptions distinguish vendor development/lifecycle assessment from product evaluation against applicable Security Assurance Specifications (SCAS). Results identify product releases and evaluation context; do not infer all releases of a vendor are covered.

Source limitation: official catalog/resource descriptions were located, but full current FS.15/FS.16/FS.47 documents, applicable SCAS, recognition scope and market-specific rules remain unverified. Search exposes older versions alongside version-3 resource pages. Record current approved versions and transition rules before technical evaluation; a search result's crawl date is not a document's effective date.

## Engagement focus

Prepare evidence linking a precisely identified product release to its development/lifecycle process, applicable evaluation requirements and actual laboratory outcome. Keep supplier process results, product evaluation, deployed-network configuration and market acceptance separate. None substitutes automatically for the others.

## Roles

Product security and release owners define the product and preserve evidence. Supplier/process owners maintain lifecycle records. Qualified auditors and recognized laboratories perform their authorized scheme roles. Regulatory and procurement owners decide market requirements. An independent internal reviewer challenges readiness and claims; leadership approves sharing, releases and external statements.

AI may reconcile metadata, trace evidence and draft questions. AI cannot choose an official evaluation outcome, claim laboratory accreditation, certify conformance, accept risk, authorize a release or submit scheme records. Tests and sharing require approved scope; no access to operator networks or customer data follows from this guide.

## Before starting

Use the [agent runbook](../agent-runbook.md). Record vendor/legal entity, product class, release/build, hardware/software configuration, target markets, intended assurance claim, evaluator and evidence permissions. Obtain the selected scheme versions, applicable SCAS and authorized scope. Missing product-class or method decisions block dependent testing, not independent inventory collection.

## Ordered workflow

1. **Freeze the product boundary.** Identify the exact product under evaluation, release, configuration, interfaces and intended market. Reconcile aliases and component versions. Output: product identity manifest with every mismatch retained.
2. **Confirm evaluation authority and sources.** Verify the current evaluator/laboratory recognition and relevant scope, scheme versions and applicable SCAS through authoritative records. Output: route/source register; a generic accreditation logo is not proof of the required scope.
3. **Trace lifecycle coverage.** Link the release to its actual development, maintenance and delivery processes and their audited scope. Output: process-to-release evidence chain. A vendor's process audit cannot by itself establish this release's evaluation outcome.
4. **Prepare the evidence handoff.** Reconcile every requested artifact to its owner, version, permitted location, product identity and requirement reference. Output: complete manifest; document transfer does not equal evaluator acceptance.
5. **Observe evaluation results.** Preserve authorized laboratory reports, tested configuration, actual case outcomes, exclusions and unresolved observations. Output: bounded product-result register. Internal QA findings remain distinct from official evaluation findings.
6. **Resolve changes and findings.** Track remediation, changed binaries/components, process deviations and retests with evaluator decisions on scope where required. Output: change lineage; do not assume a patch inherits an earlier result or automatically invalidates it without the applicable decision.
7. **Review and hand off.** Reconcile final release claims with authoritative process and product records. Give reviewers full gaps/disagreements and route market/release decisions to their owners. Output: approved claim and decision packet with exact limits.

## Evidence and test plan

### Product, market and assurance-boundary package

Restore PR340's package with full scoped product/release reconciliation. Product, regulatory and procurement owners supply identifiers, target markets, configurations, suppliers and scope decisions. Map each represented product to the relevant result and date. A family name, earlier release or different hardware platform cannot establish coverage without evidence.

### Supplier process and evaluation-readiness package

Process, engineering and laboratory-coordination owners supply lifecycle audit references, release provenance, secure-development artifacts, vulnerability records and evaluation handoffs. Preserve every requested artifact and known gap. Trace the actual release through the covered process rather than relying on a corporate assurance statement. Record who received which version and whether an evaluator accepted it.

### Release governance and improvement package

Leadership and quality owners provide release decisions, changes, findings, remedies, retests and approved customer/market wording. Separate internal readiness, process audit outcome, product result and deployment decision. Preserve limitations when summarizing; passing product tests does not prove operator configuration or every real-world network condition is secure.

For every test/result record the approved criterion, source/version, product/configuration, method, expected and observed outcome, date, evaluator and limitation. Maintain the full declared test/evidence population with all exclusions and untested cases visible; do not silently sample or cap assessment evidence. Keep protected scheme text, proprietary artifacts and customer network information outside this public repository.

## Failure branches and decisions

- Process audit exists but no matching product evaluation: preserve process evidence; classify the product-evaluation claim inconclusive or not_tested.
- Release/build mismatch: stop the affected claim until authoritative coverage is confirmed. Similar naming is insufficient.
- Laboratory recognition cannot be verified: retain the uncertainty and seek confirmation; do not invent accreditation or infer revocation from a failed search.
- Corrected build differs from evaluated build: preserve both manifests and obtain the required change/re-evaluation decision before carrying forward a result.
- Customer requires a separate national scheme: route it to regulatory owners; NESAS evidence alone does not establish that acceptance.

Fictional desk case: a vendor's published process audit covers a product line, while a sales statement claims a new release has passed product evaluation without a matching report. Process coverage may be supported; the release-specific product claim remains inconclusive. No actual laboratory work was performed here.

## Cadence and renewal

Use verified scheme, evaluator and market rules for audit/evaluation validity and renewal. Reopen affected work for release, process, supplier, vulnerability, configuration or source changes. Do not invent universal annual product recertification. Preserve historical results with their original scope even when current assurance requires additional work.

## Completion and handoff

Deliver product identity, authority/source register, lifecycle trace, evidence manifest, actual evaluation references, findings, retests, market questions and reviewer disagreements. Classify assertions supported, not_supported, inconclusive, not_applicable or not_tested with reasons. Keep internal completion separate from laboratory, release and market decisions. No actual evaluation, certification or submission occurred in authoring this guide.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) and [agent runbook](../agent-runbook.md). Public claims require exact scope evidence and authorized wording.
