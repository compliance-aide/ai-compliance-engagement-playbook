# CMMC Level 3 program engagement guide

> Original operational guidance, not CMMC assessment content, a DoD determination, or a certification claim. Confirm contract applicability and current program rules through the [DoD CMMC program page](https://dodcio.defense.gov/CMMC/).

## Engagement focus

Maintain a traceable, contract-aware engagement record for advanced protection activities: in-scope systems and data, accountable owners, implementation evidence, assessment preparation, changes, findings, corrective actions, and supplier dependencies.

## Roles

Authorized organizational leaders set scope and risk decisions; system teams maintain evidence; independent assessors review the evidence trail. AI supports evidence indexing, change detection, and reviewer-question drafting, but cannot judge assessment results, accept risk, or speak for DoD. Refresh evidence throughout the year and obtain human approval for all official representations.


## Source and applicability

[Assessment Guide Level 3 v2.13, September 2024, pages 1–4](https://dodcio.defense.gov/Portals/0/Documents/CMMC/AssessmentGuideL3v2.pdf) assigns certification assessment to DCMA DIBCAC and requires Final Level 2 (C3PAO) status for every system in the proposed Level 3 scope before requesting assessment. Internal Level 3 assessment supports preparation but cannot supply an official Level 3 certification result. Selected NIST SP 800-172 requirements use DoD parameters; do not substitute the entire publication or choose parameters freely.

The [current program overview](https://dodcio.defense.gov/CMMC/about/) reports a Phase II implementation pause. The existence of a 2024 guide does not establish a current contractual obligation or an available assessment appointment. Contracts personnel must resolve current direction and the actual requirement before proceeding with the formal assessment route. Keep preparation work available while that decision is pending.

## Before starting

Use the [agent runbook](../agent-runbook.md). Name the contract, system, evidence and assessment owners. Record the approved boundary, source versions, handling environment and intended deliverable. Keep CUI and protected operational evidence in authorized systems; agent workpapers use permitted metadata and references. Distinguish preparation observations, human readiness decisions and official government findings.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Resolve current applicability | Contracts owner verifies award or solicitation direction and current program instructions. | Source-linked level, scope, timing and authority; unresolved route questions remain explicit. |
| 2. Verify prerequisite coverage | Security owner compares every proposed Level 3 system with actual Final Level 2 (C3PAO) status and scope records. | System-by-system reconciliation; any uncovered system blocks a formal request, not authorized gap analysis. |
| 3. Establish detailed scope | Architecture and data owners apply current Level 3 scoping guidance to CUI flows, shared services, suppliers and specialized assets. | Owned boundary and documented inclusions/exclusions; do not assume the Level 2 diagram proves Level 3 scope. |
| 4. Build full coverage | Agent indexes every selected Level 3 requirement, applicable objective and prescribed parameter from authoritative materials. | Complete owner/evidence/method register with unresolved interpretations visible; no silent omissions. |
| 5. Demonstrate operation | Owners provide implementation and operating evidence; authorized testers conduct scoped readiness checks with defined expected behavior and recovery provisions. | Dated observations tied to requirements, scope and limitations. Threat-hunting, penetration-testing or exercise labels alone do not prove effectiveness. |
| 6. Correct gaps | Operational owners execute approved remediation; reviewers retest affected objectives and dependencies. | Evidence-backed closure. Any proposed assessment POA&M requires exact Level 3 eligibility and closeout-rule review, not reuse of Level 2 assumptions. |
| 7. Prepare the formal handoff | Assessment lead reconciles prerequisites, scope, evidence and open issues into a reviewed request package. | Explicit authorization before government communication or submission; record actual government acceptance or scheduling separately from the draft request. |
| 8. Maintain records | Program leadership preserves official results, permitted closeout records, affirmation inputs and current scope. | Separate authoritative dates and owners for reassessment, affirmation and remediation; changes trigger review of affected claims. |

## Failure branches and decisions

- A Level 2 self-assessment is offered as the prerequisite: identify the mismatch and request the required status evidence; do not relabel it as C3PAO status.
- Proposed scope includes a new enclave absent from the prerequisite record: retain the delta and assign the prerequisite/scope decision before requesting assessment.
- A provider supplies an assurance statement without operating evidence: map exact inherited and customer responsibilities and keep unsupported objectives open.
- A technical test fails to collect evidence: record an inconclusive preparation observation and authorized recovery action; do not treat absent telemetry as success.
- An assessor appointment is unconfirmed: retain the request state and next owner. Do not advertise certification, award eligibility or an agreed assessment date.

## Evidence and test plan

**Source and rights snapshot.** Use the current official [DoD CMMC program information](https://dodcio.defense.gov/CMMC/); prior snapshot dated 2026-07-31; revalidate before use. This is original engagement guidance, not restricted assessment content, a scope determination, an assessment result, or a certification statement.

### 1. Contract, data, and advanced-scope decision record

- **Request and owner:** Contracts, program, and security owners provide award/change records, covered-data flow diagrams, system and enclave boundaries, inherited-service records, supplier dependencies, and documented accountable decision makers.
- **Validate and limit:** Trace a selected scope statement to the current contract source, data or service flow, responsible owner, and change history. This checks evidence lineage; it cannot determine legal applicability, assessment level, or required scope.
- **AI and trigger:** AI may correlate approved diagrams and inventories and flag changes. Authorized contracts, legal, and security humans make applicability and scope decisions. Refresh after contract modifications, new data flows, shared-service changes, or acquisitions.

### 2. Protection-operation, testing, and remediation evidence

- **Request and owner:** Technical and process owners provide approved process references, configuration/operation evidence, monitoring and incident records, test observations, limitations, corrective-action plans, retest evidence, and evidence-location pointers.
- **Validate and limit:** Sample a claimed activity from source artifact to owner, in-scope context, observed limitation, remediation action, and retest outcome. It supports readiness work only and cannot attest adequacy, score an assessment, or certify a result.
- **AI and trigger:** AI may organize redacted artifacts, detect missing provenance, and draft non-conclusive reviewer questions. Humans determine test methods, validate conclusions, and approve closure. Refresh after a failed test, material control change, or remediation milestone.

### 3. Governance, supplier, and representation evidence

- **Request and owner:** Executives, contracts, and security owners provide leadership reviews, supplier assurance records, exceptions, risk decisions, status reports, and controlled drafts of assessment-related communications.
- **Validate and limit:** Trace a selected decision or supplier record to authority, rationale, limitation, expiry, action owner, and subsequent review. This cannot accept risk, make an affirmation, submit to a government system, or certify a supplier.
- **AI and trigger:** AI may flag stale decisions and overdue actions. Authorized humans approve risk and any external representation. Review quarterly, annually, and after a significant supplier, incident, or service-boundary change.

## Cadence and renewal

Derive assessment, affirmation and conditional-closeout dates from applicable current rules and actual status records. Quarterly management review is an internal convention. Reconcile Level 2 prerequisite coverage after system, CUI-flow, supplier, contract or architecture changes; preserve historical scope rather than overwriting the evidence behind a prior status.

## Completion and handoff

Deliver the applicability decision, prerequisite reconciliation, complete objective/parameter register, safe evidence references, test and remediation history, unresolved questions and formal-request draft. State which outcomes are prepared, authorized, received or officially determined. Identify the next action, owner and required evidence without relying on prior chat history. Only an official result can support an official status claim.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
