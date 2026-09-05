# FedRAMP — engagement guide

> Original operational guidance, not a FedRAMP authorization claim. Check the
> current [FedRAMP rules](https://www.fedramp.gov/2026/providers/rev5/controls/assessment-authorization-and-monitoring/)
> at engagement start and before every significant milestone.

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

## Service-boundary and evidence sequence

Use the [agent runbook](../agent-runbook.md). Original execution recommendations
below require the current program rules for the selected path. Search on
2026-09-04 surfaced current, legacy, preview and demo documentation together;
no full current rule set or actual offering status was verified in this pass.
Do not promote an RFC, preview page or legacy process into current authority
because its search snippet sounds applicable. Resolve the canonical rule/version
and any transition conditions before setting deliverables or deadlines.

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

**Failure branches:** a missing canonical current-rule source leaves path-specific
requirements `inconclusive`. An inaccessible evidence source is `not_tested`.
A known configured dependency omitted from the approved boundary makes that
boundary-completeness assertion `not_supported`; do not hide it behind a listing.

**Fictional desk case:** an offering's evidence covers Region A, but the proposed
agency integration exports logs to an unreviewed service in Region B. Region A's
entry does not establish the combined configuration's coverage. Record the actual
flow and obtain the owned scope/risk decision; do not call the integrated system
authorized from the offering name alone. No actual agency system was assessed.

## Annual rhythm

Maintain the monitoring calendar; validate evidence and inventory changes;
review vulnerabilities, incidents, and remediation; assess significant changes
early; support independent assessment; and always re-check current program
rules rather than relying on legacy workflow descriptions.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
