# CSA IoT Security Controls Framework v2 engagement guide

> Original operational guidance, not CSA framework content or an assurance conclusion. Confirm the applicable source through the [CSA IoT Security Controls Framework v2 record](https://cloudsecurityalliance.org/artifacts/csa-iot-security-controls-framework-v2).

## Engagement focus

Maintain current IoT system boundaries, device and service ownership, data and network dependencies, lifecycle evidence, supplier records, material changes, testing evidence, exceptions, and remediation.

## Roles

System owners define intended use and risk context; engineering and operations teams maintain evidence; independent reviewers challenge traceability. AI inventories approved device and service evidence, finds missing owners or stale lifecycle records, and drafts questions, but cannot approve deployment, determine safety, or claim conformance. Revisit records at onboarding, major change, and scheduled review; retain human approval for risk and release decisions.

## Source and applicability

This filename preserves the catalog's v2 reference; it must not imply v2 is the latest release. CSA publishes [IoT Controls Matrix v3](https://cloudsecurityalliance.org/artifacts/iot-security-controls-framework-v3), released April 25, 2022, with 198 controls versus 155 previously and an added Incident Management domain. Record why an engagement requires v2 or approves migration. Retrieve the matching matrix and companion guide, confirm rights, and reconcile all changed controls before carrying forward earlier evidence.

CSA assigns system classification to the system owner using data value and potential physical-security impact. Document that human decision against the whole device/network/cloud system, not just a device label. Sector-specific safety, privacy and product obligations need separate applicability review; matrix completion is not product certification.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Identify device models, firmware, gateways, mobile applications, cloud endpoints, operator interfaces and physical dependencies. Use authorized QA devices and synthetic data. Obtain explicit test scope, safe operating conditions, recovery method and responsible operator before active tests; read-only inventory approval does not authorize firmware flashing, radio interference or actuator commands. Create work items by control, device cohort and lifecycle stage.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Select edition and scope | Program and system owners approve source version, system boundary and impact classification. | Source register and classification rationale; v2 retention or migration decision visible. |
| 2. Reconcile assets and flows | Engineering maps device cohorts, versions, networks, applications, cloud services and data paths. | Complete scoped inventory with owners and offline/unknown devices retained as gaps. |
| 3. Allocate controls | Security, engineering and supplier owners review every selected matrix control. | Full disposition register with implementation and evidence responsibilities across device, gateway and service boundaries. |
| 4. Specify lifecycle evidence | Owners define expected provisioning, access, update, monitoring, recovery and retirement behavior. | Version-specific evidence requests and test expectations, including failure and recovery paths. |
| 5. Test approved configurations | Reviewers inspect records and execute approved QA checks on representative configurations. | Observed results, cohort selection rationale, untested variants and safety limits; sample success cannot cover unexplored firmware variants. |
| 6. Trace vulnerabilities and incidents | Operations maps notices and events to affected deployed versions and responsible parties. | Affected-asset record, containment/remediation decisions, communications authority and unresolved supplier dependencies. |
| 7. Remediate and verify | Owners implement authorized changes; reviewers verify installed state and affected behavior. | Per-cohort outcome and recovery evidence; queued update is separate from applied and verified update. |
| 8. Review and retire | Management reviews residual issues, support commitments and lifecycle completion. | Approved handoff, monitoring plan and retirement evidence covering data, credentials and remaining service access. |

## Failure branches and decisions

- **Offline device missing from update results:** retain it in scope and assign recovery or replacement; do not remove it to improve completion percentages.
- **Firmware version cannot be established:** request trusted device or management evidence; vendor release availability does not prove installed version.
- **Update interrupts physical function:** stop the authorized QA test at its defined safety boundary and invoke the operator-approved recovery path; do not improvise production rollback.
- **Cloud service changed without firmware change:** reopen affected authentication, data-flow and dependency checks; device version alone cannot establish unchanged system behavior.
- **Supplier ends support:** record affected cohorts, compensating actions and replacement decision; absence of new patches is not evidence of no vulnerabilities.
- **Retirement leaves access active:** trace device identity, credentials, cloud records and retained data; require verified revocation/disposal before closure.

## Evidence and test plan

**Source and rights snapshot.** Use the [CSA IoT Security Controls Framework v2 record](https://cloudsecurityalliance.org/artifacts/csa-iot-security-controls-framework-v2) and current CSA terms; prior snapshot 2026-07-31; revalidate edition and terms. This plan is original device-lifecycle evidence planning, not CSA framework text, a device-security evaluation, a safety determination, or a conformance claim. Authorized humans confirm source rights, scope, product context, and release authority.

### 1. Device, service, deployment, and ownership package

- **Request and owner:** Product, engineering, operations, security, and safety owners provide device/model/firmware inventory, intended-use and deployment context, network/service dependencies, data-flow references, customer/operator boundary, supplier records, lifecycle state, and named owners.
- **Validate and limit:** Trace a selected device/firmware deployment to its intended use, service/network dependencies, owner, version, and supplier boundary. This can expose incomplete inventory or lifecycle ownership; it cannot prove asset completeness, safety suitability, or secure deployment.
- **AI and trigger:** AI may reconcile approved device/service inventories and flag inconsistent versions, missing owners, or unreviewed supplier links. Humans approve deployment context, device scope, supplier allocation, and safety/risk decisions. Refresh at onboarding and after material firmware, network, intended-use, supplier, or ownership changes.

### 2. Device lifecycle, access, update, and vulnerability-response package

- **Request and owner:** Engineering, operations, security, release, and supplier owners provide design/test references, identity/access and interface records, firmware/software-release approvals, update/rollback evidence, vulnerability intake/triage, remediation/retest records, and exceptions.
- **Validate and limit:** Sample one device version, update, or vulnerability event from affected deployment through evidence of decision, test/retest, rollout/rollback path, owner, and current status. This can test a bounded response chain; it cannot validate all devices, authorize an update, or prove vulnerabilities are absent.
- **AI and trigger:** AI may index authorized records and flag missing affected-version, retest, or approval evidence. Humans approve release, rollback, remediation priority, and exception/risk actions. Refresh after material vulnerability, failed test, update, operational incident, or supplier notice.

### 3. Operational resilience, customer communication, and independent-challenge package

- **Request and owner:** Operations, support, product, legal, security, safety, and independent-review owners provide monitoring/maintenance records, incident/exercise results, end-of-support/retirement plans, customer communication decisions, residual-risk records, corrective actions, and reviewer workpapers.
- **Validate and limit:** Trace a selected operational event or retirement decision to device/service scope, evidence source, escalation, human approval, communication decision, and follow-up. This can assess whether the declared lifecycle process has retained records; it cannot determine legal notification duties, customer obligations, safety, or conformance.
- **AI and trigger:** AI may identify stale maintenance, unsupported communications, or overdue corrective actions without contacting customers or altering operations. Humans approve incident/customer communications, retirement, residual risk, and remediation closure. Review on a scheduled cadence and after material event, support-status, or lifecycle change.


## Cadence and renewal

Choose review frequency from approved system impact, lifecycle and support commitments. Reopen affected work after firmware, hardware, network, cloud service, intended use or supplier changes. Track newly discovered devices and unsupported cohorts continuously through the agreed inventory process; annual review alone cannot establish current deployment state.

## Completion and handoff

Deliver the edition decision, system classification, full control dispositions, cohort inventory, lifecycle evidence, test coverage and unresolved risks. State which devices and versions were actually tested and which remain unknown. Name the next owner, action and required evidence without prior chat. Distinguish prepared, approved, applied and verified work; no safety or conformance conclusion follows automatically.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
