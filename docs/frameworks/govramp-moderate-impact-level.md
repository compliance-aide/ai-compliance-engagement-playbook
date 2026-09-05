# GovRAMP Moderate impact-level engagement guide

> Original operational guidance, not licensed program material, an impact decision or authorization. Draft pending independent source, skeptical and rights review.

## Source and applicability

Use the [current GovRAMP document library](https://govramp.org/document-library), the actual government requirement and authorized program instructions. The library read 2026-09-04 separately lists Moderate and Moderate-with-CJIS-overlay provider/assessor packages. It also lists verification-boundary, monitoring, incident and significant-change guidance. These catalog descriptions identify documents to obtain, not their full requirements.

Current package contents, exact control/parameter sets, overlays, assessment-route rules and partner requirements remain unverified in this draft. Record source versions before requirement-level conclusions. Do not infer that Moderate automatically satisfies CJIS, federal authorization or a particular state's procurement conditions.

## Engagement focus

Build an offering-specific evidence trail for the approved Moderate boundary and selected program route. Account separately for baseline requirements, government additions and approved overlays. Keep impact level, program status, actual control results and buyer acceptance distinct.

## Roles

Government and accountable offering authorities approve categorization and scope. Security, engineering, operations and suppliers maintain evidence. Qualified assessors, PMO and sponsoring authorities retain their program decisions. An independent reviewer challenges completeness and outcomes. Legal and customer-assurance owners approve representations.

AI may reconcile authorized records, identify mismatches and draft workpapers. AI cannot select impact level, waive requirements, approve overlays or exceptions, accept risk, submit attestations or make authorization/procurement decisions. Tests use approved QA scope and authorized methods.

## Before starting

Apply the [agent runbook](../agent-runbook.md). Obtain the signed or otherwise authoritative Moderate decision, offering name/build, regions, data flows, service boundary, intended program status, source packages, owners and evidence access. If classification is unresolved, record the missing decision and continue only independent discovery.

## Ordered workflow

1. **Bind the scope decision.** Match the government requirement, information/service consequences and approved Moderate category to the actual offering. Output: dated boundary/level record; a commercial product name alone is insufficient.
2. **Select the exact package.** Record current baseline, parameters, program route and any overlay/additional requirement separately. Resolve incompatible versions. Output: complete obligation register with sources and owners; never substitute a minimum-readiness set for a full-authorization assessment.
3. **Reconcile dependencies.** Inventory all included regions, components, administrative paths, interfaces and shared services. Identify inherited, provider and customer portions. Output: full responsibility matrix with unverified dependencies retained.
4. **Collect operating evidence.** Link each applicable obligation to current implementation, artifact date, owner and evidence period. Output: complete manifest including missing artifacts and source restrictions. A provider certificate cannot prove the application's own configuration.
5. **Test against approved criteria.** Record expectation, actual result, authorized method, build, environment and coverage for every planned case. Include failures and inaccessible components. Output: scoped results; a policy statement or populated template is not a passed operational test.
6. **Reconcile change and remediation.** Link findings to actions, approvals and retests. Assess the effect of changed regions, data, interfaces or providers against the current boundary and verified change process. Output: finding/change register; do not assume a historical authorization covers new functionality.
7. **Review and prepare decisions.** Give independent reviewers the full evidence and disagreements. Freeze the package for authorized submission and separately verify program status and buyer acceptance. Output: bounded decision record with remaining work, not an automatic authorization claim.

## Evidence and test plan

### Category, baseline and overlay package

Maintain the actual government requirement, level decision, package/version register, parameters, approved additions and overlay scope. Reconcile every obligation to an owner and acceptance criterion. Keep a reasoned record for non-applicable items; missing evidence cannot justify exclusion. Preserve licensed materials in restricted storage and use references rather than reproducing requirements here.

### Offering, inheritance and test package

Record complete component/data/interface populations, provider and customer responsibilities, deployment identifiers and operational evidence. Test applicable shared-responsibility handoffs such as the customer's receipt and use of provider security outputs. Mark an inherited portion and its consumer portion independently. Document all untested routes; a technical test selection does not permit deleting other assets from assessment evidence.

### Monitoring, remediation and representation package

Maintain monitoring coverage, collection failures, incidents, recovery results, remediation and authoritative status references for the exact boundary. Match each public or buyer-facing claim to scope, level, status and date. See the [general GovRAMP workflow](govramp-licensed-program.md) for status distinctions. Keep a separate record for any overlay claim and government-specific acceptance; neither follows merely from Moderate status.

## Failure branches and decisions

- Base evidence exists but required overlay evidence is missing: preserve the base results and classify the overlay claim inconclusive or not_tested; do not claim the combined requirement is complete.
- Government parameter differs from a template default: record the mismatch and route the correction/decision to its authority before treating the default as accepted.
- Required inherited output never reaches the application: distinguish provider availability from failed consumer implementation.
- Monitoring misses a new region: mark coverage not_supported if the region is confirmed in scope; do not report complete monitoring from the remaining regions.
- Status record conflicts with a proposal: preserve both and obtain authoritative resolution before publication; a successful package upload is not an issued status.

Fictional desk case: the provider exposes required audit logs, but the application never enables the customer-side feed. Provider capability is supported; the defined application logging criterion is not_supported. Other controls and official status remain separate claims.

## Cadence and renewal

Use the verified program route and partner requirements for monitoring, reassessment, renewal and incident/change reporting. Record exact triggers, owners and due dates. Reopen affected work after boundary, data, parameter, provider or source changes. Do not invent universal quarterly reviews or carry old evidence forward without checking applicability.

## Completion and handoff

Deliver approved scope, full obligation/boundary matrices, source versions, tests, findings, monitoring gaps, overlay/addition results, disagreements and named next owners. Classify assertions supported, not_supported, inconclusive, not_applicable or not_tested. Keep internal completion, program decisions, overlay claims and procurement acceptance separate. No actual offering assessment or authorization occurred in authoring this guide.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) and [agent runbook](../agent-runbook.md). Restricted program and customer evidence must not enter this public repository.
