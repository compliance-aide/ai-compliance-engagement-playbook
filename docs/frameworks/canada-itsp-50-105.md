# Canada ITSP.50.105 cloud assessment and authorization engagement guide

> Original operational guidance, not Canadian authorization guidance or an authorization outcome. Confirm current use through [ITSP.50.105](https://www.cyber.gc.ca/en/guidance/guidance-cloud-security-assessment-and-authorization-itsp50105).

## Engagement focus

Maintain cloud-service scope, data and responsibility boundaries, provider evidence, assessment records, conditions, material changes, authorization inputs, and recurring monitoring evidence.

## Roles and annual rhythm

Service and system owners establish scope; cloud providers and operating teams provide evidence; assessors independently review it; authorizing officials decide outcomes. AI indexes approved evidence and flags changes or missing conditions, but cannot assess a service, authorize use, or accept risk. Reassess after material changes and retain dated human authorization decisions.

## Tailored evidence plan

**Source and rights snapshot.** Use [ITSP.50.105](https://www.cyber.gc.ca/en/guidance/guidance-cloud-security-assessment-and-authorization-itsp50105), current authorized Canadian cloud-security material, contract terms, and organization direction; checked 2026-07-31. This plan is original operational language, not Canadian assessment/authorization content, a cloud assessment result, authorization decision, or risk acceptance. The human engagement owner confirms source rights, applicable scope, and permitted provider-evidence use.

### 1. Cloud service, data, and responsibility-boundary package

- **Request and owner:** Service, system, cloud architecture, privacy, and procurement owners provide the approved cloud-service description, data/service boundary, deployment/tenant and interface inventory, shared-responsibility assignment, provider/subprocessor register, and material-change history.
- **Validate and limit:** Trace one data path, interface, or shared service to its boundary record, accountable provider/customer owner, operating assumption, and evidence location. This validates a documented trail; it cannot determine data suitability, service applicability, or the correct authorization scope.
- **AI and trigger:** AI may compare approved records for missing interfaces, ownership gaps, or stale supplier references. Human service, security, privacy, and procurement owners decide scope and responsibility acceptance. Refresh at onboarding and after a material data, architecture, provider, location, or service-model change.

### 2. Assessment-evidence and operating-condition package

- **Request and owner:** Cloud providers, customer operators, and assessment owners provide authorized provider artifacts or evidence references, customer implementation/process records, assessment plans/results, evidence coverage dates, limitations, conditions, and remediation/retest records.
- **Validate and limit:** Sample one assessment area or operating condition to its provider/customer evidence reference, period covered, limitation, accountable owner, remediation action, and retest/open status. This does not validate provider attestations, establish complete assessment coverage, or prove operating effectiveness.
- **AI and trigger:** AI may index permitted metadata and identify missing coverage or unlinked conditions; it cannot inspect restricted artifacts beyond authorization, test production, alter evidence, or decide assessment sufficiency. Human assessors and operators evaluate evidence and action closure. Refresh on the approved review cadence and after a failed test, incident, or material implementation change.

### 3. Authorization-input, change, and monitoring package

- **Request and owner:** Designated decision authorities and service owners provide authorization-input records, human approvals, risk/exception decisions, monitoring outputs, incident/change assessments, deployment decisions, reassessment dates, and source-change log.
- **Validate and limit:** Trace one material change, incident, or open condition from detection through impact review, accountable human decision, required follow-up, and next monitoring/reassessment date. This supports an auditable decision input; it cannot authorize cloud use, accept risk, or declare authorization current.
- **AI and trigger:** AI may flag aging conditions and missing decision fields and prepare read-only review packets. Only named human authorities approve risk, deployment, and authorization outcomes. Reassess before a material decision and after major changes, provider incidents, or conditions affecting the service.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
