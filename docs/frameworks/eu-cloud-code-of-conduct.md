# EU Cloud Code of Conduct — engagement guide

> Original operational guidance, not an adherence determination, certification or legal conclusion.

## Source and applicability

Retrieve the approved code, controls catalogue, monitoring procedures and current service entry. The [EDPB register](https://www.edpb.europa.eu/our-work-tools/accountability-tools/register-code-of-conduct/2021/eu-cloud-code-conduct_pl) concerns the code; the [program public register](https://eucoc.cloud/en/public-register/list-of-adherent-services) concerns particular services. Record both kinds of source separately. A provider name or membership logo does not identify the customer's covered service configuration.

The program's [levels explanation](https://eucoc.cloud/en/public-register/levels-of-compliance) distinguishes evidence substantiation, not different sets of substantive controls. Level 1 uses provider-originating evidence verified by the monitoring body; Levels 2 and 3 add partial and full independent third-party support respectively. The monitoring body decides the level. Do not describe Level 1 as unverified self-declaration or Level 3 as a blanket GDPR certification.

The [assessment procedure](https://eucoc.cloud/en/public-register/assessment-procedure/) requires service-specific agreements and control-by-control explanations. Initial validation precedes listing; continued current listing requires revalidation at least every 12 months, with ad-hoc assessment possible. The public questionnaire is a sample; use the template actually supplied for an assessment. Source check: 2026-09-04.

Do not infer a Chapter V transfer mechanism from base-code adherence. The program [describes a separate transfer initiative](https://eucoc.cloud/en/about/third-country-transfers-initiative); legal must verify the current approval and applicability of any claimed mechanism for the actual transfer. Preserve unresolved status rather than treating development material as an approval.

## Engagement focus

Reconcile service commitments with processing operations: contracts, instructions, subprocessors, locations, customer assistance, security handoffs, deletion/return and renewal. Maintain a complete service/control coverage record, including evidence gaps and changes since the last verification.

## Roles

Service owners own the declared boundary and operational facts. Privacy/legal owns interpretation, roles and customer commitments. Engineering, support, security and supplier management own execution evidence. Independent reviewers challenge claims; the monitoring body makes program verification decisions. AI may reconcile records and prepare workpapers or authorized QA checks. Humans approve declarations, submissions, customer communications, account/data actions and public adherence claims.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Identify whether the task is provider readiness, customer due diligence or renewal support. Obtain approved sources, exact service names/variants, agreement versions, processing inventory, current verification references and evidence access. Assign one owner per control and one accountable service sponsor. Keep personal data, customer agreements and restricted audit reports in approved storage.

A text-only agent requests exact records and describes expected observations. A tool-capable agent records authorized collection/test steps and outputs. Neither invents monitoring-body decisions or operates a real customer deletion workflow for testing.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Fix the service boundary | Service/legal owners reconcile declared service with actual product, agreement, processing role and configuration. | Approved scope and explicit exclusions; unresolved name/version mismatches remain open. |
| 2. Verify the claim | Reviewer checks current register entry and available verification report against that boundary. | Dated status, identifier, level, scope and limitations; a historical badge is insufficient. |
| 3. Map all controls | Compliance owner inventories the applicable approved code/catalogue and assigns evidence owners. | Complete coverage ledger; no removal of inconvenient controls or inaccessible evidence. |
| 4. Collect commitments and operation | Custodians link agreement clauses and procedures to actual execution records. | Source-linked work items with service, period, evidence location and test criterion. |
| 5. Test bounded assertions | Authorized reviewers trace assistance, subprocessor, incident and deletion/return workflows. | Original observations, failed checks and coverage limits; statements and execution remain distinct. |
| 6. Resolve discrepancies | Control owners correct implementation or clarify the documented boundary. | Reviewed rationale and fresh retest; a changed policy alone cannot close an operational defect. |
| 7. Prepare assessment/handoff | Sponsor assembles the approved assessment package or customer due-diligence record. | Exact outstanding questions and owner decisions; prepared is not submitted or verified. |
| 8. Monitor changes | Service/compliance owners track renewals, incidents and scope changes. | Next review triggers and current status evidence; material changes reopen affected assertions. |

## Failure branches and decisions

- Register lists a different service: request a scope match or separate verification. Do not extend a provider-wide logo to an unlisted variant.
- Verification report is old or unavailable: separate historical evidence from current status and seek a current authoritative record; lack of access is not proof of non-adherence.
- Level is used to omit controls: restore full coverage and record evidence type separately from the control requirement.
- Subprocessor/location inventory conflicts with actual configuration: preserve both records, assign service/privacy review and reopen affected commitments.
- Deletion job succeeds but covered data remains retrievable: classify the approved deletion criterion from the retrieval evidence; investigate cache, backup, retention and service scope before claiming completion.
- Collector cannot access the system: record `not_tested` and the error; do not turn a tool failure into a service finding.
- Transfer legitimacy is justified only by the code logo: leave the transfer conclusion `inconclusive` and obtain the legal mechanism and scope decision.
- A complaint or material service change arises between renewals: reopen impacted assertions and route the program-notification decision; do not wait for the calendar anniversary.

## Worked handoff example

Fictional provider “North Cloud” has a current verification record for “Archive Standard.” The customer is evaluating “Archive Analytics,” absent from the supplied report. The assertion that the supplied report covers Analytics is `not_supported` by its explicit scope; whether Analytics is separately verified remains `inconclusive` pending current evidence. Procurement requests the exact service record from the service owner. The agent does not claim the provider is noncompliant and does not approve a purchase from the Standard listing alone.

## Evidence and test plan


**Source and rights snapshot.** Use the [EDPB EU Cloud Code of Conduct register entry](https://www.edpb.europa.eu/our-work-tools/accountability-tools/register-code-of-conduct/2021/eu-cloud-code-conduct_pl), the current approved code materials, participation terms, and qualified privacy/legal review; prior snapshot 2026-07-31; verify current approved materials. Confirm source status, version, participant role, monitoring-body route, and reuse conditions before use. This original plan does not reproduce code text, decide adherence, or create a monitoring-body, certification, or customer assurance conclusion.

### 1. Service, customer, and processing-commitment package

- **Request and owner:** Service, privacy, legal, product, procurement, and customer-success owners provide service descriptions, customer/processor role records, agreement versions, processing instructions, assistance commitments, approved subprocessor and location records, and ownership/review history.
- **Validate and limit:** Trace one in-scope service/customer commitment to its agreement or approved service record, processing role, applicable subprocessor/location entry, owner, and review date. This cannot interpret a contractual term, decide controller/processor status, or establish adherence.
- **AI and trigger:** AI may compare approved commitment metadata with supplied operational records and flag missing links. Humans decide contract interpretation, customer commitments, participation, and scope. Refresh after a service, agreement, processing purpose, location, customer-assistance, or subprocessor change.

### 2. Operational assistance, security, and deletion package

- **Request and owner:** Operations, support, security, privacy, engineering, and records-management owners provide documented assistance workflows, access/change records, security-incident handoffs, deletion/return procedures and execution evidence, service notices, and exception/remediation records.
- **Validate and limit:** Sample an approved assistance, deletion, or incident workflow from request/intake through responsible owner, source-system evidence, decision/communication record, and follow-up, using redacted workpapers. This does not determine a customer outcome, establish security effectiveness, or decide notification duty.
- **AI and trigger:** AI may build evidence indexes and flag missing completion or expired review records. Humans approve customer communications, incident decisions, exceptions, and remediation closure. Refresh after workflow, incident, security, retention, or customer-support changes.

### 3. Accountability, monitoring, and renewal package

- **Request and owner:** Privacy/compliance leadership, legal, service management, supplier management, and independent-review owners provide training/awareness records, internal review workpapers, service or supplier assurance references, issue logs, corrective actions, and any monitoring-body correspondence retained under approved controls.
- **Validate and limit:** Trace one declared operational posture or corrective action to its source, owner, limitation, review result, human decision, and renewal date. This cannot make an adherence statement, replace monitoring, or attest for management.
- **AI and trigger:** AI may flag stale source versions, overdue actions, and incomplete provenance. Qualified humans approve conclusions, communications, risk treatment, and renewal decisions. Refresh before renewal, after material code/program updates, and during annual independent review.


## Cadence and renewal

Track the actual assessment/verification dates and the program revalidation requirement. Review operational changes at the agreed cadence and after service, agreement, subprocessor, location, incident or code changes. An internal annual review does not replace monitoring-body revalidation.

## Completion and handoff

Deliver the service-boundary record, code/catalogue versions, complete control/evidence ledger, dated register and verification references, test results, open discrepancies, corrective actions and next owners. For customer due diligence, state exactly which claims were checked and which remain unresolved. Independent source, engagement, skeptical and rights review plus named human publication approval remain required. No adherence decision or transfer approval results from completing this workpaper.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for applicability, authority, evidence, testing, exceptions, source changes and renewal.
