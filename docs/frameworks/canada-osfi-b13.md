# Canada OSFI Guideline B-13 technology and cyber risk-management engagement guide

> Original operational guidance, not OSFI text, a supervisory determination, legal advice, or a compliance claim. Confirm current applicability through [OSFI Guideline B-13](https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/technology-cyber-risk-management) and qualified regulatory counsel.

## Engagement focus

Maintain a technology and cyber-risk record that connects governance, accountable ownership, technology assets and services, critical dependencies, architecture and change evidence, resilience planning, cyber observations, incident records, remediation, third-party context, management decisions, and review dates. Make the rationale, sources, scope, and limitations of material statements visible. Keep the record connected to operating evidence so an assessment can distinguish documented intent from observed practice.

## Source and applicability

The official B-13 page was checked on 2026-09-04. It covers federally regulated financial institutions, including foreign branches subject to applicable Canadian obligations, and uses a risk-based approach. Its three domains address governance, technology operations/resilience and cyber security. Confirm entity scope and current related supervisory direction with compliance owners. A self-assessment does not establish OSFI approval.

## Roles

Management owns strategy, resources and risk decisions. Business/service owners provide operational context; technology and security owners maintain implementation evidence. Risk, compliance and independent assurance challenge results. Incident authorities determine escalation and reporting. AI drafts traceability records and questions; it cannot accept risk, authorize changes, determine reporting duties or make compliance claims.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Create a bounded work item naming entity, service, environment, period, owner, inputs, output and exit check. Obtain the approved risk framework, service/asset inventory, applicable requirements, decision authorities and evidence-handling permissions. Record missing inputs explicitly; continue only independent preparation. Keep private operational evidence out of this repository.

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Establish coverage | Risk and service owners reconcile applicable expectations across all three domains with services, assets and owners. | Complete coverage register and scope decisions; cyber tooling alone cannot cover technology operations. |
| 2. Reconcile dependencies | Technology owners compare actual inventories, configurations and supplier dependencies with architecture and business-service records. | Versioned inventory with discrepancies, unsupported assets and accountable follow-up. |
| 3. Plan verification | Assessment owners assign evidence and methods to every applicable expectation, recording scope and review depth. | Evidence plan; missing coverage stays visible rather than becoming not applicable. |
| 4. Examine governance and operation | Reviewers compare management decisions, project/change records, operating observations and security evidence with approved expectations. | Workpapers showing actual results, limitations and contradictions. Policies alone do not prove operation. |
| 5. Verify resilience | Continuity and service owners provide approved recovery objectives, dependency assumptions and exercise or incident evidence. Reviewers compare achieved results with expected recovery. | Recovery workpaper with failed or untested assumptions. A backup-success message does not prove restoration. |
| 6. Correct and retest | Owners assign remediation and obtain separate implementation approval. Reviewers verify actual corrections and affected dependencies. | Finding/change/retest chain; ticket closure is not a passing retest. |
| 7. Obtain decisions | Coordinator presents open risks, exceptions, resource needs and proposed actions to the named authorities. Read back approved decisions from their system of record. | Versioned decision record with conditions, owners and dates; no inferred risk acceptance. |
| 8. Monitor and reassess | Service/security owners monitor indicators, incidents and changes and reopen affected evidence and decisions. | Owned review queue with escalation triggers and continuing obligations. |

## Evidence and test plan

Use the complete approved coverage register; these original examples do not replace it. Preserve the full evidence corpus and never trim evidence sent to a scorer.

| Package and owner | Verification task | Limitation |
| --- | --- | --- |
| Governance/assets — risk and technology | Trace a service to accountable ownership, dependencies, risk rationale and management action; reconcile inventory discrepancies. | A selected trace does not prove all assets known. |
| Design/change — engineering/reviewer | Follow a change through requirements, assessment, approval, implementation and post-change observation. | An approved release is not proof of actual deployment or correct behavior. |
| Security operation — security owner | Trace a detected weakness through affected assets, response, correction and retest. | Missing telemetry is a visibility gap, not zero incidents. |
| Resilience/incidents — service owner | Compare an approved exercise or actual event with recovery objectives, dependencies, escalation and corrective actions. | Simulated results remain labelled; no disruptive exercise is authorized here. |
| Exceptions/assurance — risk and independent reviewer | Link each material observation to evidence, decision authority, mitigation, review date and retest. | Accepted residual risk does not mean the failed control works. |

Record source, collector, date, period, environment, expected/actual observation, evidence pointer, limitation, reviewer and next action. State test populations and untested coverage. Use authorized QA exercises or retained evidence; live intrusive testing and production changes require separate approval.

## Failure branches and decisions

- **Unowned or unsupported asset:** identify affected services, retain the gap and request an owner and treatment decision.
- **Wrong environment or stale evidence:** isolate affected workpapers and recollect from the intended scope; do not relabel artifacts.
- **Failed recovery or security observation:** preserve adverse results and escalate their impact on the service; assign correction and retest.
- **Missing supplier visibility:** request the exact period and service evidence through the relationship owner and retain uncertainty.
- **Incident with possible reporting duties:** promptly route facts to incident/compliance authorities under the institution's process. They determine applicable obligations; AI does not invent a timer or send a regulatory notice.
- **Expired exception or unresolved management decision:** flag it for the authorized owner; do not automatically extend acceptance.
- **Interrupted work or uncertain update:** preserve last completed step, versions and pending decisions. Read back the destination before retrying.

## Cadence and renewal

Use applicable requirements, institution-approved schedules and actual decision conditions. Record the owner and rationale for internal review intervals; the earlier annual readiness challenge is an engagement practice, not a universal B-13 certification cycle. Reassess affected records after material technology, supplier, threat, business, incident or regulatory change.

## Completion and handoff

A preparation packet contains approved scope, complete coverage, governance and operating workpapers, recovery evidence, open findings, remediation/retests and decision questions. Mark omissions. Handoff lists next action, owner, due date and evidence location. Actual changes, regulatory communications and risk acceptance are separate milestones with their own authority and readback.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared applicability, authority, evidence, technical-test, exception, source-change and renewal requirements.
