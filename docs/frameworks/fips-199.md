# FIPS 199 security categorization — engagement guide

> Original operational guidance, not FIPS text or a federal categorization decision. Confirm current status at the [NIST publication record](https://csrc.nist.gov/pubs/fips/199/final).

## Engagement focus

Maintain system boundary, information types, impact rationale, mission dependencies, categorization decisions, accountable approvals, inherited-service assumptions, changes, and review evidence.

## Source and applicability

Use the [FIPS 199 publication](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.199.pdf), current agency instructions and applicable information-type guidance. Sections on applicability, impact definitions, information types and system aggregation were read on 2026-09-04. Full remaining text and current agency guidance still require review. FIPS 199 uses separate confidentiality, integrity and availability impacts; system aggregation takes the highest value for each objective across resident information types. Do not average the ratings or substitute a control-effectiveness score. Its information-type confidentiality NA value is distinct from the runbook's evidence status `not_applicable`.

## Roles

Information and mission owners explain consequences of loss. System and architecture owners document boundaries and dependencies. Designated agency authorities approve categorization. Independent reviewers challenge scope and rationale. AI consolidates authorized records and drafts comparisons; it cannot approve a categorization, classify national-security information, accept risk or change a production boundary.

## Before starting

Record agency, system, mission, approved boundary, information sources, recipients, dependencies and decision owner. Identify which current instructions govern categorization and which questions need agency interpretation. Use the [agent runbook](../agent-runbook.md), with one traceable record per information type and per security objective. Keep sensitive mission details in the authorized evidence system.

## Ordered workflow

1. **Establish the actual boundary.** Reconcile architecture, system inventories, interfaces and data flows. Output a boundary register with unresolved discrepancies. A drawing alone does not prove all resident information was identified.
2. **Inventory information types.** Include user and system information, identifying owners, sources, uses and dependencies. Reconcile the full population; do not select only the largest or most familiar data sets. Output an information-type register and missing-owner queue.
3. **Describe loss consequences.** For each type, separately explain unauthorized disclosure, unauthorized modification/destruction and disruption of access. Link mission, asset and individual consequences to owner evidence. Output three reasoned impact proposals; do not infer integrity or availability from confidentiality.
4. **Apply source definitions.** Compare each proposed impact with the official definitions and current agency guidance. Preserve assumptions, disagreements and requested clarifications. Output a draft impact matrix; labels without a consequence rationale are incomplete.
5. **Aggregate transparently.** Calculate each objective's highest applicable information-type impact and identify the driving rows. Review additional system-level considerations under the full source and agency process before finalization. Output a reproducible system proposal; a small high-impact data set cannot disappear through averaging.
6. **Challenge and approve.** Have independent reviewers check omitted types, unsupported downgrades and inconsistent boundaries. Route the reconciled record to the designated approving authority. Output a dated decision only when approval exists; author completion is not agency approval.
7. **Propagate and monitor changes.** Link the approved result to downstream risk-management records through their separate processes. Reassess new information, interfaces, mission dependencies and boundary changes. Output assigned updates; categorization alone does not establish selected controls are implemented or the system is authorized.

## Evidence and test plan

### Information types and system boundary

Information, mission and system owners provide the complete information-type inventory, boundary version, data flows, supporting services and accountable agency roles. Reconcile processing, storage and transmission locations against the actual system description. Preserve unknown types and disputed boundaries as explicit gaps; a small data volume is not grounds to omit a consequential information type.

Record the source and owner of every inventory entry and exclusion. Compare diagrams, service inventories and owner statements, resolving differences before claiming completeness. An inherited service's assurance report does not determine the consuming system's categorization. Record the dependency and its mission consequences for qualified review.

### Impact rationale and decision

Owners provide separate confidentiality, integrity and availability rationale for each information type, with mission effects, affected individuals/assets, assumptions and stakeholder input. Reconcile the proposed system values to their driving rows. Preserve review challenges and documented adjustments; do not hide a disagreement by replacing its rationale with an unexplained label.

Check that the matrix and narrative refer to the same boundary and information population. A technically correct maximum over an incomplete inventory does not establish a complete categorization. Keep arithmetic verification separate from substantive review of the impact assumptions. Record the exact proposal version, reviewer and approving authority; a meeting invitation or acknowledgement is not approval.

### Changes and downstream use

System governance owners provide new information/use requests, interface changes, reassessment triggers, decisions and downstream security-planning references. Reconcile all material in-scope changes with a documented categorization review or owner-approved explanation. Preserve open reassessments; do not silently reuse an older decision for a changed boundary.

For each approved change, identify every downstream consumer and obtain evidence of the version received or incorporated. A sent notification is not proof that a security plan was updated. Keep categorization, control selection, implementation and authorization as distinct outcomes, with unresolved work assigned to the appropriate process owner.

## Failure branches and decisions

Unknown information populations or conflicting mission consequences make the affected proposal `inconclusive`. An unexamined data flow is `not_tested`. A known omitted high-impact row makes an asserted complete aggregation `not_supported`; retain that fact even if other types remain unresolved. Keep evidence statuses separate from the impact values being proposed.

Fictional desk case: nine information types have low integrity impact and one has high integrity impact. A draft averages them and reports low. The aggregation check is `not_supported`; the system integrity proposal must retain the high driver for authority review. The agent does not approve the category or decide the other two objectives by analogy.

## Cadence and renewal

Revisit after material mission, information-type, dependency, boundary or source changes and on the agency's required schedule. Do not invent annual FIPS renewal. Assign a named owner to detect changes and keep downstream records aligned with the approved categorization.

## Completion and handoff

Deliver the boundary/source register, complete information-type inventory, three-objective impact matrix, rationale and assumptions, reproducible aggregation, reviewer challenges and approval references. Name unresolved types, disputed consequences and missing agency guidance with next owners and actions. Hand downstream users the exact approved version and track incorporation gaps.

Independent source, skeptical and rights review remain required before publication. Designated federal authorities retain categorization approval and risk decisions. This draft has not categorized a real system, selected its controls or authorized operation.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
