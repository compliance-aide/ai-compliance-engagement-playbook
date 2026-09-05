# FEMA National Response Framework — engagement guide

> Original operational guidance, not government authority or an emergency directive.

## Source and applicability

Start with the [FEMA National Response Framework collection](https://www.fema.gov/emergency-managers/national-preparedness/frameworks/response) and its linked current edition, then obtain the jurisdiction's approved authorities, response plans, agreements and organizational responsibilities. The NRF describes national response coordination; a preparation review does not confer command authority, grant eligibility or a certification.

Source checkpoint, 2026-09-04: the collection returned HTTP 403. Official indexed [NRF fourth-edition text](https://www.fema.gov/sites/default/files/documents/NRF_FINALApproved_2011028.pdf) describes adaptable coordination and community lifelines. Full edition, current annexes, NIMS interfaces and jurisdiction-specific authorities remain to be verified before substantive conformity conclusions. A search crawl date is not an edition date. The procedures below are original preparation checks, not newly inferred federal mandates.

## Engagement focus

Make the approved coordination plan executable: identify who can decide, what information they need, how partners receive and acknowledge requests, and how unresolved needs survive changes of shift or phase. Keep exercises separate from actual incidents.

## Roles

The emergency-management owner defines the review boundary. Legal and authorized officials confirm authorities, agreements and activation decisions. Operations and partner owners validate dependencies and resource availability. Communications owners approve messages and recipients. An independent reviewer challenges conclusions. AI organizes approved information and drafts records; it does not activate structures, dispatch resources, issue public directions or impersonate an official.

## Before starting

Record jurisdiction, organization, hazard/scenario, geography, period, participating partners and plan versions. Identify the incident-command and coordination interfaces by their locally approved names; do not invent a reporting chain from a generic diagram. Obtain named decision owners and alternates, authorized evidence access, information-sharing restrictions and exercise safety rules. Use synthetic data and clearly marked exercise channels. For a real emergency, follow the approved emergency plan and authorized officials immediately; this review is not a prerequisite to response.

Create a work item using the [agent runbook](../agent-runbook.md). Define each check's expected result before observing it. Inventory every in-scope role, dependency, agreement and exercise objective, including missing evidence. Do not substitute a few successful examples for full population coverage.

## Ordered workflow

1. **Establish the source boundary.** Save edition identifiers, applicable local authority references, approval dates and unresolved conflicts. Output: source register. If authority is unclear, route the question to the authorized owner and continue only independent preparation work.
2. **Map decisions and interfaces.** For each activation, escalation, request, information release and demobilization decision, record the responsible role, alternate, trigger, receiving organization and evidence of authority. Output: decision map; a contact's name alone does not prove authority.
3. **Map needs and dependencies.** Link scenario impacts to affected services, populations, facilities and partner dependencies. Record capacity assumptions, availability evidence and competing requests. Output: dependency and resource register. An agreement or resource listing is not proof of present availability.
4. **Prepare approved information routes.** Define source, observation time, confidence, audience, classification/access limits, approval and acknowledgement for each report or request. Output: routing plan. Separate a factual observation from an unconfirmed report or forecast.
5. **Exercise the handoffs.** With owner approval, test synthetic requests across the planned interfaces, including unavailable primary contact, communications failure, duplicate request and changed priority. Preserve event times, recipients, acknowledgements and observed actions. Output: objective-by-objective results; do not contact real responders without exercise authorization.
6. **Reconcile outstanding work.** Link each request to its unique identifier and current owner. Distinguish requested, acknowledged, allocated, dispatched, received and usable where applicable. Output: reconciled queue with unmet needs; an acknowledgement alone cannot support a delivery claim.
7. **Resolve and retest improvements.** Assign each gap an owner, action, due date and observable closure criterion. Retest the failed handoff or assumption after correction. Output: before/after evidence; editing a procedure does not establish effective operation.
8. **Hand over the record.** Give the next authorized owner the current situation, outstanding decisions, resource commitments, uncertain observations and next update point. Output: received handoff and open-action register. Keep recovery responsibilities explicit when response activity ends; closing an exercise does not close real operational commitments.

## Evidence and test plan

### Authority, role and coordination package

Emergency-management and legal owners provide approved plans, authority references, role/alternate rosters, agreements and decision history. Reconcile all in-scope decision types to accountable roles and current authority evidence. Report missing or conflicting authority separately from an unreachable contact. Check agreement boundaries and expiration conditions against the proposed scenario; do not interpret an unsigned draft as authorization.

### Readiness, exercise and information-sharing package

Operations, continuity, communications and partner owners provide objectives, dependency inventories, authorized participant lists, information-sharing rules, observations and lessons. For every objective, preserve expected behavior, actual input/output, timestamps, evidence identifiers and unexercised branches. A tabletop discussion supports discussion participation, not demonstrated live communications or field performance. Share only approved content; retain restricted underlying evidence in its controlled system with an authorized reference.

### Escalation and improvement package

Authorized leaders provide decision logs, escalation criteria, request/status records, approved communications, transition decisions and corrective actions. Reconcile the complete request and action populations, including rejected, cancelled and duplicate records. Verify closure against the defined outcome and receiving owner's evidence. Record schedule targets as local decisions unless an applicable source establishes a requirement.

## Failure branches and decisions

- Missing current source or local authority: mark the affected conclusion `inconclusive`; assign source/authority verification. Do not create a government mandate from an old plan.
- No authorized observation or failed access: use `not_tested` for that check. Lack of access is not evidence of readiness.
- Contact or route fails under the approved exercise criterion: record `not_supported`, preserve the failure and follow the approved alternate route. A later success does not erase the initial failure.
- Reports conflict: preserve both sources and observation times, seek owner reconciliation and show uncertainty. A newer ingestion time does not make an older observation current.
- A check is outside scope: document the applicability reason before using `not_applicable`. Do not remove an unmet need merely because another organization owns it.

Fictional desk case: a synthetic generator request receives an acknowledgement, but the delivery deadline passes with explicit evidence that no generator arrived. Acknowledgement is `supported`; on-time delivery is `not_supported`; usability is `not_tested`. The agent retains the unmet need and escalates through the approved exercise route. It does not mark the request fulfilled or dispatch a replacement itself.

## Cadence and renewal

Have the owner set the review and exercise schedule from applicable plans and requirements. Recheck after changes to jurisdiction, personnel, agreements, dependencies, communications or source editions, and after exercises or incidents. During an authorized operation, use its defined update cycle and triggers rather than an invented annual or hourly federal requirement. Record the next review owner and date.

## Completion and handoff

Deliver source and scope registers, decision/interface map, complete evidence index, objective results, request reconciliation, uncertainty register and assigned improvements. State which routes were actually exercised and which were only discussed or not tested. Preserve the distinction between draft readiness findings and an authorized operational decision. Obtain independent source, skeptical and rights review before publishing the guide; named officials retain authority for activation, public messaging and government submissions. This draft has not verified actual jurisdictional readiness or incident performance.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) and [agent runbook](../agent-runbook.md) for shared authority, evidence, assertion status, review and handoff requirements.
