# FIPS 200 minimum-security requirements — engagement guide

> Original operational guidance, not FIPS text or a federal authorization decision. Confirm current status at the [NIST publication record](https://csrc.nist.gov/pubs/fips/200/final).

## Engagement focus

Maintain boundary and categorization dependencies, implementation evidence, inherited-service records, exceptions, assessment results, remediation decisions, risk acceptance, and authorization-package traceability.

## Source and applicability

The [NIST publication record](https://csrc.nist.gov/pubs/fips/200/final), read 2026-09-04, identifies the March 2006 standard and its risk-based selection process for minimum security requirements. Obtain the full standard, current control-selection guidance and applicable agency instructions before evaluating a system. Those sources remain to be reconciled. A publication summary or generic checklist does not establish the system's applicable control set.

## Roles

System and information owners maintain the boundary and categorization inputs. Security/control owners prepare selection and implementation records. Common-control providers explain inherited responsibilities. Independent assessors evaluate evidence separately. Designated federal authorities approve security and authorization decisions. AI indexes approved records and drafts gaps; it cannot select binding requirements, accept risk, waive controls or authorize operation.

## Before starting

Record agency, system, boundary version, approved categorization, mission, review period and authoritative selection process. Identify missing approvals before dependent conclusions. Use the [agent runbook](../agent-runbook.md) to record each requirement, implementation owner, evidence and expected assessment outcome. Keep sensitive system evidence in its approved environment.

## Ordered workflow

1. **Reconcile scope and categorization.** Match the current system boundary and information inventory to the approved categorization. Output a dependency register. If they differ, retain a draft selection state and route reassessment; do not quietly apply an old category to a new system.
2. **Establish the control set.** Obtain the authorized baseline, tailoring decisions, parameters and supplemental requirements under the current agency process. Output a versioned selection register with reasons and approval references. Do not drop inconvenient requirements or interpret missing evidence as non-applicability.
3. **Assign implementation responsibilities.** Separate system-specific, common and shared portions for each selected control. Identify provider evidence and remaining consumer actions. Output a responsibility matrix; a provider authorization alone does not prove every consumer responsibility is fulfilled.
4. **Trace implementation claims.** Link each assertion to actual configuration, operating records or other appropriate evidence for the same system and period. Output an evidence index with full coverage. Written plans describe intended behavior; they do not prove operation.
5. **Assess against defined criteria.** Under the approved assessment plan, record procedure, target, expected outcome, observed evidence and result. Preserve failed and unperformed checks. Output assessment records without substituting structural document checks for control effectiveness.
6. **Resolve findings and retest.** Assign gaps an owner, corrective action, due date and closure criterion. Separate remediation plans, implementation and observed correction. Output open findings and retest evidence; an accepted risk does not turn a failed technical check into a passing one.
7. **Prepare the authority decision.** Reconcile selection, implementation, assessment and remediation records into a consistent versioned packet. Identify residual risks and limitations for the authorized official. Output a draft decision package, not an authorization inferred from complete paperwork.
8. **Maintain the decision basis.** Track changes to boundaries, providers, controls and source requirements under the agency's monitoring process. Output assigned reassessments and updated evidence; prior approval does not automatically cover materially different operation.

## Evidence and test plan

### Boundary and categorization dependencies

System, information and architecture owners provide the complete boundary inventory, categorization decision, interconnections, common-service dependencies and ownership records. Reconcile these inputs to the same version and period. Preserve missing interfaces, disputed scope and unapproved changes as open dependencies rather than forcing them into a favorable baseline.

Trace each selected requirement to its authorized source and decision context. Record tailoring and parameter decisions with their rationale and approving owner. A template's default parameter is not automatically the agency-approved value. Keep requirements that still need a decision visible in the selection register.

### Implementation and assessment evidence

Control owners, providers and assessment teams provide implementation records, evidence locators, approved procedures, observations and findings. Reconcile the full selected-control population to responsibilities and assessment coverage. Separate provider, system and shared portions; one provider report cannot close unobserved consumer actions.

For each assertion, record the system/configuration, period, method, criterion and actual result. Preserve original evidence and access limitations in the approved repository. A current document can describe an obsolete deployment; verify the relationship rather than relying only on file modification time. Failed access is not a successful assessment with no findings.

### Authorization, monitoring and risk

System/security owners, monitoring teams and designated authorities provide actual decisions, conditions, change records, monitoring schedules, remediation registers and risk decisions. Match each approval to the precise scope and version; a decision reference without its conditions cannot establish permission for every operation.

Reconcile monitoring findings through ownership, action and retest. Keep planned, implemented and verified corrections distinct. An overdue action does not disappear because a new assessment period began. Preserve accepted residual risk as a decision alongside the factual control result, not as a replacement for it. Track expired evidence and significant changes to the responsible review process.

## Failure branches and decisions

Unperformed checks are `not_tested`; unresolved selection or boundary conflicts are `inconclusive`. A known missing consumer action under a shared-control criterion is `not_supported`, even when the provider's portion is supported. Preserve the portions separately and route the gap to its implementation owner.

Fictional desk case: an approved provider supplies logging infrastructure, but the consuming system never enabled the required event feed. Provider capability is `supported`; the defined system logging criterion is `not_supported`. The agent records the missing feed and does not mark the entire control inherited or authorize the system.

## Cadence and renewal

Use current agency monitoring requirements and change triggers to set review frequency. Do not invent an annual FIPS renewal. Reassess after consequential boundary, categorization, implementation, provider or threat changes, and assign owners for expiring evidence and unresolved findings.

## Completion and handoff

Deliver the consistent boundary/categorization inputs, authorized selection register, responsibility matrix, complete evidence and assessment index, findings, remediation status and decision references. Identify untested controls, unresolved parameters, missing provider evidence and contradictory versions. Assign next owners and review triggers for all open items.

Independent source, skeptical and rights review remain required before publication. Designated federal authorities retain authorization, exceptions and risk decisions. This draft has not assessed a real system or established that minimum requirements are satisfied; completed paperwork alone does not prove either outcome.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
