# CMMC Level 1 program engagement guide

> Original operational guidance, not CMMC assessment content, a DoD determination, or a certification claim. Confirm contract applicability and current program rules through the [DoD CMMC program page](https://dodcio.defense.gov/CMMC/).

## Engagement focus

Maintain a contract-aware record of in-scope services, responsible personnel, operational evidence, supplier dependencies, material changes, findings, remediation, and customer or assessor communications.

## Roles

Contract and system owners determine scope; operating teams retain evidence; independent reviewers test traceability. AI organizes approved artifacts and drafts questions, but cannot determine contract applicability, assess achievement, or make certification claims. Review scope at contract and service changes, perform recurring evidence checks, and preserve human approvals.


## Source and applicability

The [official program overview](https://dodcio.defense.gov/CMMC/about/), checked September 4, 2026, states that Phase II implementation is suspended while Phase I self-assessment requirements remain. Do not reuse a historical rollout date as a current contractual obligation. Contracts personnel must confirm the actual solicitation, contract, modification and applicable clause before deciding what status is required and when.

Level 1 addresses FCI through the 15 FAR 52.204-21 safeguarding requirements, annual self-assessment and annual affirmation. The overview states that Level 1 assessment POA&Ms are not permitted. A remediation backlog may organize preparation but cannot justify a conditional Level 1 result. Preserve the difference between remediation planning and an achieved status.

Use the [Level 1 Assessment Guide v2.13](https://dodcio.defense.gov/Portals/0/Documents/CMMC/AssessmentGuideL1v2.pdf), the [Level 1 Scoping Guide](https://dodcio.defense.gov/Portals/0/Documents/CMMC/ScopingGuideL1v2.pdf), current 32 CFR Part 170 and contract direction together. The assessment guide identifies in-scope assets by processing, storing or transmitting FCI and confirms that third-party assistance remains a self-assessment, not certification. Version the requirement and objective register; do not substitute a legacy practice count or a vendor checklist.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Name the contracts owner, system owners, human assessment lead and affirming official. Record permitted evidence locations and tools before collecting contract information. Use approved pointers and metadata in workpapers; do not expose FCI, CUI or credentials to unapproved tools. Keep customer-facing output labeled draft preparation until the relevant reviewed result and submission receipt exist.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Confirm the obligation | Contracts owner identifies clauses, required level, affected contract and dates against current direction. | Source-linked applicability decision; unresolved interpretation blocks the related status claim. |
| 2. Establish scope | Security and service owners trace FCI flows through users, endpoints, services, storage and suppliers using the scoping guide. | Owned asset/boundary register with exclusions justified against the source; suspected CUI is referred for classification and appropriate scope review. |
| 3. Build complete coverage | Agent creates records for all 15 requirements and every applicable assessment objective in the adopted guide. | Each record has scope, owner, source reference, evidence need and planned method; no omitted objective hidden by a checklist total. |
| 4. Collect and evaluate evidence | Owners provide authorized artifacts and interviews; approved testers observe operation. | Dated evidence and observations tied to objectives, methods and populations. Policy text alone does not prove operation. |
| 5. Review the assessment | Human assessment lead applies the official methodology and finding rules to the complete register. | Defensible human-reviewed determinations. Agent work states and inconclusive observations remain separate from formal assessment findings. |
| 6. Remediate and retest | Operational owners correct gaps through authorized change control; assessment lead reviews new evidence. | Retest closes the actual objective gap. An open action plan or accepted business risk cannot be presented as a permitted Level 1 assessment POA&M. |
| 7. Prepare the official record | Agent drafts a package with scope identifiers, assessment results, dates, limitations and evidence references for review. | Authorized human verifies the exact submission and affirmation; any government submission and binding affirmation require explicit approval. Read back the resulting SPRS record before reporting submission or status. |
| 8. Maintain and renew | Program owner tracks annual assessment and affirmation separately, monitors changes and reopens affected objectives. | Calendar, accountable owners, prior receipts and change log; an old receipt is not proof of continuing compliance. |

## Applying the assessment finding rules

[Assessment Guide v2.13, pages 5–9](https://dodcio.defense.gov/Portals/0/Documents/CMMC/AssessmentGuideL1v2.pdf) distinguishes method selection from objective coverage. Choose sufficient examination, interviews or testing for each objective; every suggested method and document is not mandatory. Record why the selected evidence supports the determination. Draft policies are preparation artifacts, not eligible final assessment evidence.

The human assessor records MET, NOT MET or NOT APPLICABLE. One unmet applicable objective makes its requirement NOT MET. Record a defensible rationale for each N/A; it is not a substitute for missing evidence. Provider implementation needs adequate supporting evidence too.

The guide separately recognizes qualifying enduring exceptions and temporary deficiencies with their required documentation. Refer such cases to the assessment lead for exact rule application; do not treat unfinished initial implementation as an automatic temporary deficiency. These provisions do not create a Level 1 assessment POA&M option. Preserve the evidence and decision rather than applying a blanket pass or fail to every operational issue.

## Failure branches and decisions

- **Unknown evidence:** mark the workpaper inconclusive and assign a collection action. Do not turn an unanswered question into MET or an official NOT APPLICABLE determination.
- **Unexpected CUI:** retain safe pointers and seek the responsible classification and contract decision; Level 1 preparation does not establish adequate scope for CUI.
- **Supplier assurance without evidence:** identify the exact service and inherited responsibility, request supporting artifacts and retain unverified coverage as a gap.
- **Submission error or missing readback:** preserve the error and pending state. A prepared report, portal click or consultant statement is not a verified SPRS result.
- **Missed renewal or material change:** notify the program owner and reassess affected status and obligations; do not backdate evidence or reuse a prior affirmation as current.

## Evidence and test plan

**Source and rights snapshot.** Use the current official [DoD CMMC program information](https://dodcio.defense.gov/CMMC/); prior snapshot dated 2026-07-31; verify current program and contract direction before use. This original operational plan does not reproduce assessment materials, determine contract scope, make a certification claim, or make a government submission.

### 1. Contract applicability and system-boundary evidence

- **Request and owner:** Contracts and security owners provide award and modification records, contractual cybersecurity clauses, system/service boundary diagrams, data classifications, supplier dependencies, and named accountable owners.
- **Validate and limit:** Trace a selected contract obligation to its source record, affected service or system, owner, and change date. This tests traceability only; it cannot interpret the contract, determine CMMC applicability, or approve the boundary.
- **AI and trigger:** AI may index approved records and flag changed awards, services, or suppliers. Authorized contracts and security humans decide applicability and boundary. Refresh after an award, modification, acquisition, or material architecture change.

### 2. Safeguard-operation and evidence-retention record

- **Request and owner:** System, IT, and people-operation owners provide approved process references, access and asset records, training completion records, configuration or operational evidence, incident records, and a dated evidence index.
- **Validate and limit:** Sample an asserted operating activity to a dated artifact, accountable owner, system or process context, and retention location; record gaps and follow-up. This supports preparation and cannot determine assessment results or certify implementation.
- **AI and trigger:** AI may create redacted evidence requests, identify missing dates or owners, and draft reviewer questions. Humans validate artifacts and approve findings. Refresh on failed checks, material process change, or before a planned assessment.

### 3. Supplier, exception, and leadership-review evidence

- **Request and owner:** Program leadership, contracts, and security owners provide supplier due-diligence records, exceptions, remediation plans, risk decisions, periodic review notes, and assessment-communication drafts.
- **Validate and limit:** Trace a selected exception or supplier record to its authority, expiry, limitation, action owner, and closure or reapproval record. This does not accept risk, approve a supplier, make an affirmation, or represent a certification outcome.
- **AI and trigger:** AI may flag expired exceptions and overdue actions. Authorized humans approve risk, supplier decisions, and all external representations. Review quarterly and immediately after a significant supplier, incident, or scope change.

## Cadence and renewal

Track annual self-assessment and affirmation requirements using the applicable rules and actual recorded dates. Quarterly evidence checks are an internal planning convention, not a replacement for either annual action. Refresh on contract, FCI flow, service, supplier, personnel, incident or source changes. Retain sufficient historical scope and evidence to explain what changed and why prior conclusions remain supported or require reassessment.

## Completion and handoff

Deliver the full requirement/objective register, authorized evidence pointers, human-reviewed assessment record, remediation and retest history, submission-ready draft and renewal calendar. State separately whether preparation is complete, assessment is reviewed, submission is authorized, and a SPRS record has been verified. Identify the next action and owner without relying on earlier chat history; never describe assisted self-assessment as third-party certification.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
