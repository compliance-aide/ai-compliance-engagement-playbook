# EU DORA — engagement guide

> Original operational guidance, not financial-regulatory advice. Check the
> [binding DORA regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554),
> technical standards, and local supervisor guidance.

## Engagement focus

Confirm entity and service scope and accountable management; maintain recurring
evidence around ICT risk, assets, dependencies, incidents, resilience testing,
and third-party arrangements; review material changes before commitment; and
close with board-level reporting and an owned remediation plan.

## Roles and annual rhythm

Operators own regulated decisions, operations, contracts, escalation, and
remediation. Independent reviewers test governance credibility. AI correlates
approved assets, suppliers, incidents, tests, and open actions; it cannot decide
scope or materiality, certify tests, accept risk, or make regulated reports.


## ICT third-party exit-readiness workstream

[Article 28 of DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) keeps responsibility with the financial entity when ICT services are outsourced. For services supporting critical or important functions, it requires documented, sufficiently tested and periodically reviewed exit plans. The objective includes continuity of business and client services, not merely ending the contract. Official indexed Article 28 source checked 2026-09-04; retrieve its full text and applicable technical standards before final legal assessment.

Use the [agent runbook](../agent-runbook.md). This original workstream checks the entity's approved exit assumptions; it does not decide function criticality or authorize termination.

1. **Link function to service.** Business and ICT owners identify the supported function, provider, contract, actual configuration, data, integrations and subcontractor dependencies. Legal approves the applicable classification and obligations. Keep unknown dependencies visible.
2. **Define the exit scenario.** Owners distinguish planned termination, provider failure, unacceptable deterioration and loss of access. State the approved service outcome, tolerable disruption, data requirements, target environment and available transition time. Do not assume a cooperative provider in a failure scenario.
3. **Collect the practical prerequisites.** Obtain contract/transition provisions, export formats, keys and access ownership references, alternative capacity, licenses, integration specifications, staffing, cost approvals and recovery steps. Keep secrets out of workpapers. A contract right to export is not proof that an export is usable.
4. **Prepare an authorized QA exercise.** Use synthetic or approved test data and an isolated target. Specify expected records, service behavior, timing, reconciliation and stop conditions. Do not terminate a live provider or move customer data merely to test the plan.
5. **Observe the full chain.** Trace export, transfer, import, integrity checks, permissions, integrations and the actual business-service outcome. Record every failed step and missing record. Successful download is an intermediate result, not exit success.
6. **Reconcile and challenge.** Compare expected and obtained data, functionality and timing. Check whether the alternative depends on the same failed provider or shared infrastructure. Assign owners for limitations and retests; do not discard inaccessible populations from the denominator.
7. **Approve the next decision.** The accountable business/legal owners decide whether to remediate, revise the plan or prepare a real transition. Record that decision and its evidence. Financial commitment, contractual termination, production migration and regulated communication require their existing approval gates.
8. **Maintain the record.** Reopen after contract, service, dependency, data-format, provider or function changes. Preserve the tested version and scenario so another agent can identify what remains valid.

### Fictional failed exit assumption

A QA exercise exports all named records from provider A, but provider B cannot preserve required history or enforce the approved access roles. “Export completed” can be `supported`; “the service can continue on B under the approved criteria” is `not_supported`. Keep both observations. Engineering and business owners address import/history and access behavior, then retest the affected service. Do not present a portable file as demonstrated service continuity.

### Failure and handoff rules

If export tooling fails before observation, record `not_tested` and the error. If contractual interpretation is unresolved, retain `inconclusive` for the disputed conclusion while collecting permitted technical evidence. If real provider failure creates a live service or reporting issue, invoke the approved incident route immediately instead of waiting for this exercise to finish.

The handoff includes function/service identifiers, approved scenario, source and contract references, expected/observed results, complete reconciliation, limitations, remediation owner and exact next decision. Provider assurances remain evidence inputs; they do not transfer the financial entity's accountability.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
