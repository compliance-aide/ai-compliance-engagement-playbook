# FFIEC Architecture, Infrastructure, and Operations — engagement guide

> Original operational guidance, not examiner guidance or a certification. Consult the [FFIEC AIO booklet release](https://www.ffiec.gov/news/press-releases/2021/pr-06-30).

## Engagement focus

Maintain architecture, infrastructure, provider, change, resilience, cyber, operational-risk, management-narrative, remediation, and examination-readiness evidence.

## Source and applicability

Use the current official booklet, applicable supervisory communications and the institution's approved scope. The [FFIEC release](https://www.ffiec.gov/news/press-releases/2021/pr-06-30) describes the June 2021 AIO booklet as replacing the July 2004 Operations booklet and covering interconnected assets, processes and providers. That release was available through official indexed results on 2026-09-04; the complete current booklet and subsequent supervisory changes remain to be verified. These original preparation procedures do not substitute for examination procedures or establish a universal control checklist.

## Roles

Business-service owners define the services and approve criticality. Architecture and infrastructure owners explain dependencies and actual configurations. Operations and provider owners supply results and resolve gaps. Independent reviewers challenge the management narrative. AI reconciles authorized metadata and drafts findings; humans approve risk treatment, production changes and examiner communications.

## Before starting

Record legal entity, regulator, services, locations, review period, production and recovery environments, providers and evidence-access limits. Define each check's expected outcome and evidence source using the [agent runbook](../agent-runbook.md). Use synthetic transactions in an approved QA environment for exercises; this guide does not authorize production failover or customer-data access. Preserve complete evidence coverage, including untested dependencies and unavailable provider records.

## Ordered workflow

1. **Establish the review boundary.** Map approved business services to accountable owners and source requirements. Separate requirements, supervisory guidance and internal targets. Output a scope/source register; unresolved applicability goes to the designated risk owner.
2. **Reconcile intended and actual architecture.** Compare diagrams with authorized inventories and configuration observations. Include identity, network, storage, processing, logging, backup and external dependencies. Output a discrepancy register; a diagram approval is not evidence that the deployed service matches it.
3. **Assign responsibility at each interface.** Record what the institution operates, what each provider operates and what evidence demonstrates each responsibility. Output a responsibility/evidence matrix. A provider assurance report covering another service or period cannot close the gap.
4. **Trace changes to observed operation.** Link the change request, approval, implemented configuration, testing, rollback plan and post-change observation. Output a change chain. A completed ticket is not proof of implementation, and an implementation record does not prove customer functionality.
5. **Check operational coverage.** Reconcile monitored components with the complete service dependency map. Distinguish expected no activity from missing telemetry. Review capacity assumptions against the defined workload and incident/problem records against observed failures. Output coverage and exception results without inferring health from a green summary dashboard.
6. **Exercise recovery of the service.** Under a separately approved plan, define the scenario, recovery point and elapsed-time criteria before testing. Record restored data, dependent services, authentication and synthetic business outcomes. Output scenario-specific results; successful backup creation or server startup alone cannot prove usable recovery.
7. **Resolve findings and retest.** Assign each gap a cause, owner, action and observable closure criterion. Reconcile repeat incidents with prior corrective actions. Output before/after evidence and remaining risks. Changed documentation does not demonstrate corrected operation.
8. **Prepare the management handoff.** Link each narrative claim to current evidence for the same service, environment and period. Carry unresolved dependencies, provider limitations and untested scenarios into the packet. Output a draft for authorized management and independent review, not an examiner acceptance claim.

## Failure branches and decisions

Missing permission or an unperformed exercise means `not_tested` for that check. Contradictory configuration evidence means `inconclusive` until reconciled. A demonstrated mismatch with the predefined acceptance criterion is `not_supported`, even if other evidence is unavailable. Keep task state separate from the assertion: an evidence request can be complete while the service assertion remains unsupported.

Fictional desk case: a QA restore starts the application servers within the target time, but the required identity service is unavailable and the synthetic user cannot complete the defined transaction. Server startup is `supported`; end-to-end recovery is `not_supported`. Data recovery point is separately `not_tested` if no qualifying data comparison occurred. The agent retains all three outcomes and does not rewrite the recovery objective after seeing the result.

## Cadence and renewal

Set review frequency from applicable sources and approved institutional policy; do not infer a mandatory quarterly or annual AIO review from this guide. Revisit after architecture, provider, workload or source changes, outages and failed recovery exercises. Record the next owner and review trigger.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
