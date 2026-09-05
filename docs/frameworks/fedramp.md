# FedRAMP — engagement guide

> Original operational guidance, not a FedRAMP authorization claim. Check the
> current [FedRAMP rules](https://www.fedramp.gov/2026/providers/rev5/controls/assessment-authorization-and-monitoring/)
> at engagement start and before every significant milestone.

## Source and applicability

Use the [agent runbook](../agent-runbook.md). Original execution recommendations
below require the current program rules for the selected path. Search on
2026-09-04 surfaced current, legacy, preview and demo documentation together;
no full current rule set or actual offering status was verified in this pass.
Do not promote an RFC, preview page or legacy process into current authority
because its search snippet sounds applicable. Resolve the canonical rule/version
and any transition conditions before setting deliverables or deadlines.


## Engagement focus

Establish the government-use and authorization path, stakeholders, and assessor
boundaries. Maintain the security package and system inventory as living,
access-controlled artifacts. Run continuous monitoring; handle changes,
deviations, incidents, remediation, and risk decisions through the current
official process; and preserve package integrity.

## Roles

The provider operates the service and produces ongoing evidence. Agency
authorizing officials make risk decisions. An independent assessment
organization performs defined assessment work. AI may coordinate authorized evidence and
drift detection, but cannot approve a package, accept risk, alter a system, or represent an
authorization.

## Before starting

Define engagement type, offering identifier, review period, approved boundary,
program path, agency context and evidence-access authority. Use
[work items](../../templates/work-item.md) for individual assertions and criteria.
Keep controlled packages, vulnerability details and agency information in their
approved repositories; public workpapers contain non-sensitive references only.

Identify the evidence sources that cover the complete scoped asset/component
population. Record freshness criteria, reviewer roles and known blind spots before
reviewing results. Use QA-named environments and synthetic data for demonstrations;
this guide-development task does not authorize live assessment or submissions.

## Ordered workflow


1. Identify the exact cloud service offering, provider entity, deployment/region,
   service features, data types and intended agency use. Separate the provider's
   service boundary from the agency system and its integrations. A parent cloud
   platform's designation does not automatically cover an application built on it.
2. Verify the applicable program path and source versions with the authorized
   owner. Record current terminology and criteria verbatim only where permitted;
   keep legacy labels identifiable without assuming an unchanged process.
3. Retrieve the exact official Marketplace entry and controlled package references
   when authorized. Record offering identifier, observed status, scope, date and
   limitations. A provider logo, sales page or similarly named offering is not
   evidence for the target service. Keep unavailable package evidence explicit.
4. Reconcile architecture, data flows, inventory, external dependencies and actual
   configured services to the approved boundary. Include administration, identity,
   logging, backups and support paths where relevant to the scope. Document each
   shared responsibility rather than assuming the infrastructure provider covers it.
5. Build the complete requirement/evidence/test matrix for the approved path.
   Separate provider-operated, inherited and agency/customer-operated assertions.
   Link inheritance to the exact service and evidence supporting it; no unverified
   blanket inheritance claim. Preserve all scoped scoring evidence.
6. Execute authorized checks against defined criteria in QA-named environments.
   Record build/configuration, coverage, failures and limitations. An assessment
   artifact's existence does not establish a passing result or accepted risk.
7. Reconcile monitoring, vulnerability and remediation records to the current
   boundary and observation period. Match source identifiers and preserve absent
   or stale feeds. A dashboard with zero findings cannot prove no vulnerabilities
   when assets or evidence sources were missing.
8. Evaluate proposed changes through the current owned change process before
   treating prior conclusions as applicable. Record the affected features,
   controls, dependencies and required review. A newer package or deployed build
   is not automatically the approved one.
9. Prepare the decision packet with complete evidence, unresolved findings,
   responsibility assignments and current scope. Authorized officials determine
   acceptance and agency use. Keep draft, assessment, program designation and
   agency risk decision separate; do not assert a Government-wide permission to use.

## Failure branches and decisions

 a missing canonical current-rule source leaves path-specific
requirements `inconclusive`. An inaccessible evidence source is `not_tested`.
A known configured dependency omitted from the approved boundary makes that
boundary-completeness assertion `not_supported`; do not hide it behind a listing.

**Fictional desk case:** an offering's evidence covers Region A, but the proposed
agency integration exports logs to an unreviewed service in Region B. Region A's
entry does not establish the combined configuration's coverage. Record the actual
flow and obtain the owned scope/risk decision; do not call the integrated system
authorized from the offering name alone. No actual agency system was assessed.

## Cadence and renewal

Maintain the monitoring calendar; validate evidence and inventory changes;
review vulnerabilities, incidents, and remediation; assess significant changes
early; support independent assessment; and always re-check current program
rules rather than relying on legacy workflow descriptions.


## Evidence and test plan

Restore the three PR #340 packages below with full in-scope coverage. Their older
source snapshot does not establish current path verification or approve this draft.

### 1. Authorization path, boundary, and package-integrity evidence

- **Request and owner:** Provider security leadership provides the government-use path, system boundary and inventory records, stakeholder/role assignments, package revision history, access controls, and evidence of authoritative artifact ownership.
- **Validate and limit:** Trace all in-scope boundary components and package artifacts to an owner, current revision, access restriction, and change history. This can support package-integrity observations; it cannot approve scope, validate all components, or authorize a system.
- **AI and trigger:** AI may organize authorized metadata, compare inventory versions, and flag unlinked changes. Provider and agency humans determine scope, package content, and access. Refresh before submission, significant architecture change, or package milestone.

### 2. Ongoing monitoring, remediation, and incident evidence

- **Request and owner:** Operations and security owners provide monitoring calendar outputs, vulnerability and remediation records, incident handling records, assessment evidence, deviation records, and dated closure/retest evidence.
- **Validate and limit:** Trace each in-scope monitored item, finding, or incident through source evidence, severity/owner assignment, action, due date, and retest or current status. This is a bounded trace, not a finding closure, continuous-monitoring conclusion, or authorization statement.
- **AI and trigger:** AI may prepare evidence indexes and flag missing dates, stale artifacts, or unresolved actions; it cannot modify systems, close findings, or determine incident reporting. Recollect per monitoring cadence and after an incident, material finding, or failed retest.

### 3. Change, deviation, assessment, and risk-decision record

- **Request and owner:** Provider, assessor, and agency stakeholders provide change assessments, significant-change analysis, assessor communications/results, deviation and remediation plans, and decisions by the appropriate authorization authority.
- **Validate and limit:** Trace each in-scope significant change or deviation to the current program process, named human authority, evidence, limitation, and follow-up. This can show that decisions are attributable; it cannot accept risk, represent an assessor, or authorize operation.
- **AI and trigger:** AI may flag overdue decisions and assemble a controlled review packet. Only designated humans make authorization, risk, and submission decisions. Reassess before significant changes and according to the current FedRAMP program cadence.

### Package and monitoring reconciliation

For each package artifact, record its owner, revision, effective period, approved
scope and controlled location. Reconcile referenced inventories, diagrams, test
outputs and responsibility records to the same baseline. A collection of individually
current documents may still describe incompatible configurations.

Match monitoring sources to the actual scoped inventory. Preserve missing assets,
failed collections, scan exclusions and stale observations separately from results.
Use source identifiers to reconcile findings across ingestion, triage, remediation
and retest. A suppressed or administratively closed finding is not automatically
corrected; link its approved disposition and evidence.

For inherited controls, identify the external offering/configuration and the
specific provider evidence. Check the customer's remaining configuration and
operating duties separately. A provider-side passing result cannot establish
that customer-controlled access or logging was configured correctly.

After an authorized change, compare the actual resulting build/configuration to
the reviewed change record and determine which prior evidence remains applicable.
Retest affected assertions under the approved plan. Preserve all scoped evidence
without sampling or truncation before scoring, including adverse observations.

## Completion and handoff

Deliver the canonical source/path record, exact offering and agency-use context,
complete boundary/inventory, responsibility matrix, controlled package index,
monitoring coverage, findings and authorized decisions. Every missing source,
untested assertion and unresolved change needs an owner and next action.

State whether each artifact is a draft, an assessor result, a program-status
observation or an agency decision, and identify the scope/date it supports. Do
not convert evidence preparation into authorization or program certification.
Independent source, skeptical, rights, publication and cross-model reviews remain
pending; structural checks cannot establish those outcomes.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
