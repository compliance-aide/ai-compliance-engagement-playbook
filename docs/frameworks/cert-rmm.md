# CERT Resilience Management Model — engagement guide

> Original operational guidance, not a CERT appraisal or an SEI publication.
> Use authorized material and review the [SEI CERT-RMM collection](https://www.sei.cmu.edu/library/cert-resilience-management-model-cert-rmm-collection/).

## Engagement focus

Start with mission-critical services and disruption tolerance. Name owners for
services, assets, suppliers, people, technology, risk, and recovery; test
whether operational processes survive staff changes and disruption; exercise
selected scenarios; and maintain an improvement portfolio tied to measurable
resilience outcomes.

## Source and applicability

Use the [SEI version 1.2 record](https://www.sei.cmu.edu/library/cert-resilience-management-model-cert-rmm-version-12/) and authorized model material. Source check: 2026-09-04. SEI describes a process-improvement model for operational resilience, including process areas and generic goals/practices. Record the exact edition and selected engagement scope. Do not turn this readiness workflow into a formal appraisal, certification or invented maturity score. Detailed model and appraisal-method review remains necessary before any such assessment.

## Roles

Leadership approves service priorities, resources and risk decisions. Service owners maintain dependencies and objectives. Process owners provide routine operating evidence. People, facilities, technology and supplier owners supply their respective inputs. An exercise lead controls approved scenarios; independent reviewers challenge observations. AI organizes records and drafts questions; it cannot set appraisal ratings, accept risk, activate recovery or change services.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Name the service, model edition, process scope, owner, inputs, expected output and exit condition. Require approved service objectives, dependency inventory, handling permissions and assessment/exercise authority. Missing inputs become explicit dependencies. Use synthetic QA scenarios and approved evidence locations; do not put confidential operating records in this public repository.

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Establish service priorities | Leadership/service owners identify intended outcomes, disruption assumptions and scope. | Approved service context with accountable decisions; AI does not invent acceptable disruption. |
| 2. Reconcile dependencies | Service owners trace people, information, technology, facilities and suppliers needed for the service. Compare diagrams with actual operating records. | Dependency map and discrepancies; missing ownership remains a gap. |
| 3. Define process coverage | Assessment lead selects the approved model scope and records all relevant practices by reference, evidence owners and verification methods. Include how processes are sustained, not only performed once. | Complete scoped coverage register; exclusions and limitations are explicit. |
| 4. Examine routine operation | Process owners supply dated evidence; reviewers compare procedures with actual execution, staff handoffs and recurring oversight. | Workpapers separating documented intent from observed operation and repeatability. |
| 5. Exercise disruption | Exercise lead obtains approval for scenario, participants, safety limits, success measures and stop conditions. Run only the approved exercise and preserve observations. | Scenario/result record with simulated versus actual evidence distinguished. |
| 6. Improve and retest | Leadership prioritizes gaps; owners propose actions and obtain necessary resource/change approvals. Reviewers verify implemented improvements and repeat affected checks. | Observation/action/retest chain with unresolved limitations retained. |
| 7. Review and sustain | Leadership reviews measured outcomes, remaining risks and resources. Coordinator reads back decisions and assigns continuing monitoring and reassessment. | Owned improvement portfolio and decision record, without a fabricated appraisal rating. |

## Evidence and test plan

These original examples supplement the complete scoped coverage register. Do not reproduce proprietary mappings or trim evidence supplied to an assessment scorer.

| Package and owner | Verification | Limitation |
| --- | --- | --- |
| Service/dependencies — service owner | Trace a material dependency to its owner, service objective, evidence and change history; reconcile inventory discrepancies. | One trace does not prove complete discovery or provider performance. |
| Process operation — process owner | Compare a routine execution with its procedure, resources, alternate staff, oversight and follow-up evidence. | A successful one-time activity does not demonstrate sustained process capability. |
| Disruption exercise — exercise lead | Trace scenario assumptions through participants, execution times, outcomes and unexpected dependencies. | Simulated performance is not proof of real-event recovery; record untested conditions. |
| Improvements — leadership/reviewer | Trace a gap through priority, resource decision, implementation and retest. | Plans or closed tickets alone do not prove improvement. |

Workpapers record source, date, period, service/process, expected/actual observation, evidence pointer, collector, reviewer, limitation and next action. Record test populations and untested scope. Retain original adverse evidence even when later retests improve.

## Failure branches and decisions

- **Missing service objective or owner:** request the specific leadership decision before judging outcomes.
- **Undocumented dependency:** add a discrepancy and assess its effect on the scenario and process scope; do not omit it for convenience.
- **Procedure relies on one person:** record the handoff/resource weakness and propose an approved continuity check; do not claim institutionalized capability from that person's success.
- **Exercise exceeds authority or safety limits:** stop the affected exercise action, preserve observations and seek the exercise lead's decision.
- **Failed recovery or improvement:** retain adverse results, assign corrective action and retest; no automatic passing rating.
- **Wrong edition or unsupported scoring request:** retain references and route to the qualified assessment owner; do not average checklist answers into a maturity result.
- **Interrupted work:** save last completed step, evidence versions, pending decisions and next owner. Read back uncertain record updates before retrying.

## Cadence and renewal

Leadership selects internal review intervals and exercise triggers based on service needs and risk. Annual leadership review is an engagement practice, not a universal model certification requirement. Reassess after significant service, staffing, supplier, threat or process changes and failed exercises.

## Completion and handoff

The preparation packet includes approved scope/objectives, dependencies, complete scoped coverage, routine-operation workpapers, exercise results, open gaps, improvements/retests and leadership decisions. Mark missing evidence. Handoff specifies next action, owner, due date and dependency. Formal appraisal or external claims require their own authorized method and review.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared applicability, authority, evidence, technical-test, exception, source-change and renewal requirements.
