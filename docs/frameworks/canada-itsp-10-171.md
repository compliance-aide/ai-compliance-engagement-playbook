# Canada ITSP.10.171 specified-information protection engagement guide

> Original operational guidance, not Canadian requirement text, contract interpretation, certification or an assessment conclusion.

## Source and applicability

Use [ITSP.10.171](https://www.cyber.gc.ca/en/guidance/protecting-specified-information-non-government-canada-systems-and-organizations-itsp10171) and its published [assessment companion ITSP.10.171-01](https://www.cyber.gc.ca/en/guidance/assessing-security-requirements-specified-information-itsp10171-01), together with the actual contract or agreement. Checked 2026-09-04. The companion took effect April 20, 2026; do not rely on older text saying a companion is still forthcoming.

The requirements concern confidentiality of specified information in non-government systems, including components protecting the information-handling components. They are not a complete privacy program. Record the contract-selected requirements and versions, and the authority establishing any organization-defined parameter values. Do not substitute US requirements or a CPCSC Level 1 result for the full contract scope. The [CPCSC Level 1 guide](canada-cpcsc-level-1.md) covers that separate program route.

## Engagement focus

Build a chain from contract direction and information flows to an approved boundary, parameterized requirements, operating evidence, assessment objectives, findings and authorized representations. A boundary diagram is a claim to verify; an isolated security domain must account for real administration and protection dependencies.

## Roles

Contract and designated government authorities resolve applicability and interpretations. Information/system owners supply the handling and boundary records. Security and supplier owners coordinate implementation evidence and remediation. Assessors judge evidence and assessment outcomes. The named signatory owns external representations. AI drafts registers, reconciles records and flags gaps; it cannot designate information, decide contract eligibility, select final parameter values, accept risk or sign a declaration.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Create a bounded work item with organization, contract, system, period, owner, input links, expected output and exit condition. Require current contractual direction, information inventory, boundary, source versions and authority roster. Confirm permitted evidence handling before collection. Missing inputs remain named dependencies; continue independent work without inventing them. Never place protected information, credentials or private supplier reports in this repository.

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Establish applicability | Contract owner identifies governing clauses, information categories, source versions, deadlines and required representations. Resolve ambiguous direction with the designated authority. | Applicability record with exact references and unresolved questions; no inferred eligibility. |
| 2. Trace the information | Information/system owners reconcile receipt, use, storage, transfer and disposal paths with systems, locations and external parties. Include protective and administrative dependencies. | Approved boundary and exclusion rationale; every discovered path has an owner and disposition. |
| 3. Complete requirements | Security lead reconciles the entire contract-required set with the current approved source and assessment objectives. Record every required parameter, its value, establishing authority and evidence. | Complete requirements/parameter register. Blank or disputed values remain unresolved rather than becoming agent-selected defaults. |
| 4. Plan assessment | Assessment owner assigns methods, evidence owners, scope and coverage to all required objectives. Separate provider evidence from customer operation. | Approved assessment plan and evidence requests; table examples below do not replace objective coverage. |
| 5. Examine operation | Owners provide dated records; assessors compare expected and actual behavior, record contradictions and document coverage limitations. | Evidence-linked workpapers with objective dispositions; policies alone do not establish operation. |
| 6. Treat and retest | Owners assign corrective actions and obtain separate change authorization. Assessors recheck affected objectives after implementation. Record enduring limitations separately from temporary corrective work. | Findings, decisions and retest evidence remain linked. Documenting an exception does not itself grant a waiver or passing result. |
| 7. Prepare representation | Coordinator reconciles the exact draft statement with all reviewed outcomes, open gaps and contract scope. Signatory reviews the versioned packet. | Decision-ready draft, with unsupported claims removed and outstanding questions visible. No submission without explicit authorization. |
| 8. Verify and maintain | Following authorized action, retain and independently read back any actual destination record. Monitor changes in contracts, information paths, suppliers and requirements. | Separate prepared/submitted/acknowledged statuses and an owned reassessment queue. |

## Evidence and test plan

Use these original workpaper examples alongside the complete approved assessment plan. Preserve the full evidence corpus; do not trim evidence bound for a scorer. Record test selection and untested coverage separately.

| Package and owner | Verification task | Limitation |
| --- | --- | --- |
| Contract and information boundary — contract/system owners | Trace an information flow to its actual systems, location, external party and approved handling decision; reconcile discrepancies against the full inventory. | A selected trace does not prove every path known. An omitted protection service can invalidate the proposed boundary. |
| Requirements and parameters — security lead | Compare requirement references, parameter authority and values with the implementation description and assessment workpapers. | A convenient default or copied US value is not authoritative for this agreement. |
| Operation and suppliers — operators/provider owner | Trace an account, asset or supplier handoff through approved responsibility, current evidence, covered period and exceptions. | Provider commitments alone do not show configured operation or customer-side performance. |
| Assessment and remediation — assessor/action owner | Follow an adverse observation through its finding, assigned correction, implementation and retest. | A future milestone or closed ticket is not evidence the requirement is satisfied. |
| Representations and renewal — signatory/coordinator | Compare each proposed claim with reviewed scope/results; check any approved submission against its retained destination receipt. | Submission acknowledgment does not establish buyer acceptance, certification or broader compliance. |

Each workpaper records objective, source, collector, date, covered period, environment, expected/actual observation, evidence pointer, limitation, reviewer and next action. Use retained records or explicitly authorized QA exercises for technical verification; this guide does not authorize intrusive tests or production changes.

## Failure branches and decisions

- **Unclear information designation or clause:** request the specific authority decision and leave affected requirements unresolved.
- **Unsupported boundary exclusion:** trace the actual information and protective dependency; reopen scope before reusing affected assessment conclusions.
- **Missing parameter value:** identify who may establish it and request the value. Never quietly turn a blank into a default or a pass.
- **Unavailable supplier evidence:** preserve the missing scope/period and assigned request; do not treat outsourced operation as exempt.
- **Failed observation or disputed exception:** retain adverse evidence, decision owner and corrective action. Do not label an exception accepted without an authorized record or equate acceptance with effectiveness.
- **Wrong system or period:** isolate affected evidence and recollect from the intended source. Do not relabel old artifacts.
- **Interrupted work or ambiguous submission:** save last completed step, document version and pending approval; check the destination before retrying.

## Cadence and renewal

Use contract obligations, assessment requirements and actual decision dates. Owners set internal reminders with enough lead time for evidence collection and corrective work. Reassess affected scope after contract, data, supplier, architecture, incident or source changes. Do not invent a universal certification expiry or assume the CPCSC Level 1 cycle governs every ITSP.10.171 engagement.

## Completion and handoff

The preparation packet includes approved applicability/boundary, complete requirements and parameters, assessment coverage, evidence-linked outcomes, open findings, retests, exact draft representations and named decision owners. Mark omissions explicitly. External action requires separate authorization and destination readback. Handoff identifies the next action, owner, due date and dependency for every unresolved item.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared applicability, authority, evidence, technical-test, exception, source-change and renewal requirements.
