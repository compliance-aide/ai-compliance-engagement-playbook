# Canada GC cloud-security profile engagement guide

> Original operational guidance, not Government of Canada profile content or an authorization decision. Confirm current scope through the [Government of Canada cloud-based services security profile](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/cloud-services/government-canada-security-control-profile-cloud-based-it-services.html).

## Engagement focus

For a government cloud service, maintain clear responsibility boundaries, service and data context, provider evidence, customer-operating assumptions, interface changes, material incidents, remediation, and decision records that can be reviewed over time.

## Roles and annual rhythm

The service owner defines service scope; cloud and customer teams maintain their respective evidence; security and privacy owners review dependencies; independent reviewers assess the evidence trail. AI catalogs approved provider artifacts, tracks shared-responsibility actions, and drafts evidence requests, but cannot declare a cloud service authorized, decide data suitability, or approve a production connection. Review boundaries at onboarding and material change, refresh supplier evidence on a schedule, and retain human approvals for risk and deployment decisions.

## Tailored evidence plan

**Source and rights snapshot.** Use the [Government of Canada cloud-based services security profile](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/cloud-services/government-canada-security-control-profile-cloud-based-it-services.html), current departmental direction, contract terms, and authorized provider materials; checked 2026-07-31. This plan is original operational guidance, not profile content, a control mapping, a cloud-service authorization, or a data-suitability determination. A named human engagement owner confirms source rights, service applicability, and permitted evidence handling.

### 1. Service boundary and shared-responsibility package

- **Request and owner:** The service owner, cloud architect, and contract/procurement owner provide the service description, tenant and interface boundary, data/service dependency inventory, responsibility assignment, provider/subprocessor register, and material-change record.
- **Validate and limit:** Trace one interface or shared service from the boundary record to its accountable customer/provider owner, operating assumption, contract or service reference, and evidence location. This checks traceability; it cannot select the profile, determine service scope, or decide suitability of the data or provider.
- **AI and trigger:** AI may reconcile approved inventories and flag unowned interfaces or stale provider references. Human service, security, privacy, and procurement authorities decide boundaries and responsibility acceptance. Refresh for onboarding and after a material architecture, supplier, data, or service-model change.

### 2. Provider-assurance and customer-operation package

- **Request and owner:** Provider relationship owners and customer operators provide authorized provider assurance artifacts or evidence references, customer configuration/process records, service-level and incident contacts, exception register, and evidence dates/coverage statements.
- **Validate and limit:** Sample one customer responsibility and one provider dependency to their evidence reference, period covered, stated limitation, accountable owner, and open action. This does not assess provider controls, validate an assurance report, or establish that all responsibilities operate effectively.
- **AI and trigger:** AI may index permitted artifact metadata and identify missing coverage periods or unassigned actions; it cannot interpret restricted provider reports beyond authorization, configure production services, or determine evidence sufficiency. Human owners assess limitations and direct remediation. Refresh on evidence cadence, major release, provider change, or material incident.

### 3. Change, incident, and authorization-input package

- **Request and owner:** The service/security owner provides material-change assessments, incident and escalation records, remediation/retest evidence, risk and exception decisions, deployment approvals, and monitoring/review schedule.
- **Validate and limit:** Trace one change, incident, or exception from detection through impact review, accountable decision, corrective action, and next verification. This supports an auditable input record; it cannot authorize a service, accept risk, or approve a production connection.
- **AI and trigger:** AI may flag incomplete approval fields, aging actions, and upcoming reviews. Named human authorities approve risk, deployment, and authorization outcomes. Reassess before major service use and after material changes, incidents, or decision conditions.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
