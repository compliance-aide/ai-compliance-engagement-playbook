# FIPS 199 security categorization — engagement guide

> Original operational guidance, not FIPS text or a federal categorization decision. Confirm current status at the [NIST publication record](https://csrc.nist.gov/pubs/fips/199/final).

## Engagement focus

Maintain system boundary, information types, impact rationale, mission dependencies, categorization decisions, accountable approvals, inherited-service assumptions, changes, and review evidence.

## Roles and annual rhythm

Information and system owners determine categorization with designated federal authorities; independent reviewers test the evidence chain. AI may consolidate authorized inventories and flag drift, but cannot classify information, approve a categorization, accept risk, or alter a production boundary. Revisit on material change and annually.

## Tailored evidence plan

**Source and rights snapshot.** Confirm the official [FIPS 199 publication record](https://csrc.nist.gov/pubs/fips/199/final), current agency policy, and governing system ownership before use; checked 2026-07-31. This is original guidance, not FIPS text and not a federal categorization decision.

### 1. Information-type and system-boundary package

- **Request and owner:** Information and system owners provide the approved boundary, inventory of information types and supporting services, mission/process context, data-flow references, inherited services, and records identifying accountable federal roles.
- **Validate and limit:** Independently trace one material information type to its documented process, storage/processing location, system boundary, owner, and current inventory reference. This cannot classify the information, infer omitted types, or decide the authoritative boundary.
- **AI and trigger:** AI may reconcile supplied inventories and flag unknown owners, inconsistent boundary versions, or undocumented dependencies. Designated human authorities decide information types and scope. Refresh after a new information type, interface, service, or material mission change.

### 2. Impact-rationale and decision package

- **Request and owner:** Owners provide documented impact rationale, assumptions, dependencies, aggregation considerations, stakeholder review input, categorization proposal, and dated approval/decision record under applicable agency process.
- **Validate and limit:** Trace a selected impact rationale to identified mission effect, source assumption, responsible owner, reviewer challenge, and final human decision. This can evaluate traceability; it cannot set impact values, resolve aggregation, approve categorization, or accept risk.
- **AI and trigger:** AI may identify unsupported rationale or inconsistent versions and prepare questions for reviewers. Humans make all categorization and risk decisions. Refresh upon incident, mission change, material dependency change, or review deadline.

### 3. Change-control and downstream-use package

- **Request and owner:** System governance owners provide change tickets, reassessment triggers, links to dependent risk/security planning records, exception records, approval history, and evidence that downstream consumers received the current decision.
- **Validate and limit:** Sample one material change from intake through impact review, categorization reconsideration, human approval, downstream notification, and next review date. This does not validate every downstream artifact or authorize a changed system.
- **AI and trigger:** AI may monitor documented trigger dates and flag missing downstream links; it cannot alter system scope, publish an official decision, or waive reassessment. Refresh on every material trigger and at the agency’s scheduled review.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
