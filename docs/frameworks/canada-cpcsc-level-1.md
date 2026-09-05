# Canadian Program for Cyber Security Certification Level 1 engagement guide

> Original operational guidance, not Government of Canada text, an attestation, a certification decision or a determination of contract eligibility.

## Source and applicability

Use the current PSPC [Level 1 criteria](https://www.canada.ca/en/public-services-procurement/services/industrial-security/security-requirements-contracting/cyber-security-certification-defence-suppliers-canada/cyber-security-certification-level1.html), [supplier instructions](https://www.canada.ca/en/public-services-procurement/services/industrial-security/security-requirements-contracting/cyber-security-certification-defence-suppliers-canada/meet-level1-certification-requirements.html), [scoping guide](https://www.canada.ca/en/public-services-procurement/services/industrial-security/security-requirements-contracting/cyber-security-certification-defence-suppliers-canada/meet-level1-certification-requirements/scoping-guide.html) and the actual solicitation/contract. Source check: 2026-09-04. Record versions and retrieval dates in the engagement; recheck before relying on them.

The supplier instructions describe an annual self-assessment of 13 requirements, introduced in selected defence contracts from summer 2026. They state assessment is required at award rather than bidding, but also direct suppliers to provide attestation proof and expiry when bidding. Record this timing ambiguity and obtain the contracting authority's direction for the specific procurement; do not silently select the easier interpretation. CMMC recognition is case by case and depends on scope verification, not an automatic exemption. The online tool is encouraged, not the only permitted assessment route. These facts do not establish this supplier's eligibility.

## Engagement focus

Build a reviewable chain from contract information to the systems protecting it, each applicable assessment objective, observed evidence, unresolved gaps and an authorized declaration decision. Level 1 work does not establish Level 2 or 3 results. A questionnaire answer, tool completion message or polished evidence index alone is insufficient to establish implementation.

## Roles

The contract owner records the procurement requirement and seeks authority clarification. The security lead owns the assessment plan and evidence judgments. IT, facilities and external service owners supply operational records and fix assigned gaps. A reviewer challenges coverage and conclusions. The authorized organizational signatory owns representations and submissions. AI can draft, reconcile and flag contradictions; it cannot sign, certify, decide eligibility, accept risk or change production under this guide.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Create one work item per bounded action with its owner, input links, expected output and stop condition. Confirm the correct organization, contract, assessment period, authorized evidence location and access permissions. Keep sensitive contract information, account lists and evidence out of this public repository.

Require the contract or recorded authority direction, information categories, system inventory, prior assessment if any and named decision owners. If an input is missing, label the affected work blocked and request that exact input; continue independent preparation without inventing it. Reuse existing authorization within its scope, but keep a separate explicit approval for a government submission.

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Confirm the route | Contract owner records which requirement applies, the procurement stage, governing dates and whether self-assessment or recognition of existing certification is proposed. Resolve the timing ambiguity above with the authority. | Applicability record with source clause, owner and outstanding questions. A proposed recognition route stays unconfirmed until its acceptance is evidenced. |
| 2. Draw the boundary | Security and system owners trace specified information through work locations and services. Reconcile actual information flows with the inventory. Include supporting security and administration dependencies; document exclusions with reasons. | Approved scope diagram and asset register. Every discovered information path has an owner and inclusion decision; absence from an inventory is not an exclusion. |
| 3. Establish assessment coverage | Security lead works through the complete current Level 1 criteria, recording every applicable objective by reference, its implementation owner and intended examination, interview or authorized test. | Objective register reconciled against the source. Unclear applicability or missing evidence remains visible; the examples below do not replace the register. |
| 4. Gather and examine | Owners provide dated, scoped evidence. Reviewer compares the described implementation with configuration and operation, records contradictory observations and checks external-service responsibilities. | Evidence-linked workpapers stating what was examined, period, result and limitation. A supplier contract alone does not demonstrate its configured service works. |
| 5. Correct and retest | Security lead assigns each gap an owner, corrective action and due date. Implementers follow their separately authorized change process. Reviewer rechecks the affected objective and dependencies after the change. | Retest evidence supports closure or leaves the gap open. A planned fix or accepted business risk does not become an implemented control. |
| 6. Prepare the decision | AI drafts answers from reviewed workpapers; security lead checks every answer and limitation against the complete register. Signatory receives the exact proposed declaration and evidence basis. | Versioned draft with unresolved items and the named decision owner. No unsupported affirmative response or self-invented conditional certification. |
| 7. Record the authorized result | After explicit submission approval, the authorized operator follows the current official route. Save the actual result, expiry and any required supplier-profile record; independently read back the destination. | Distinguish prepared, submitted, acknowledged and any official status. A lost response is unconfirmed until checked, not permission to submit twice. |
| 8. Maintain readiness | Program owner schedules renewal from the retained result and monitors contract, source, system, supplier and incident changes. Reopen affected scope/objectives when facts change. | Renewal calendar and change log with accountable owners; an old receipt is not evidence for a new boundary. |

## Evidence and test plan

These are original working examples. The assessment lead selects safe methods and records coverage against all official objectives; do not use this table as the control set or reduce evidence sent to an assessment scorer.

| Evidence package and owner | Verification task | Record the limitation |
| --- | --- | --- |
| Contract and scope — contract/security owners | Trace a representative information flow end to end and reconcile all discovered systems with the full inventory and diagram. Check inclusion of paper, mobile, remote and external-service paths where relevant. | A walkthrough may reveal omissions; it does not prove that undiscovered paths do not exist. Preserve the complete inventory and unresolved discrepancies. |
| Identity and access — IT owner | Compare approved access decisions with current account and permission records; inspect a completed joiner/change/leaver case and retained authentication observations. | State the systems, accounts, dates and coverage examined. Written access rules alone do not show enforcement. |
| Public content and external services — communications/service owners | Trace an approved publication through its review record; reconcile service agreements with actual data paths, security responsibilities and accessible configuration evidence. | Provider assurance for another service or period is not inherited implementation evidence. Escalate unavailable provider evidence. |
| Facilities and media — facilities/asset owners | Trace physical access removal and an actual disposal record to the relevant asset and approved handling procedure. Use retained evidence or an authorized QA exercise. | Do not erase media or bypass a physical control to prove the process. Unverified disposal remains unresolved. |
| Network and maintenance — IT/security owners | Compare the boundary design with dated enforcement evidence; trace a vulnerability through correction and retest, and inspect protective-system operation. | A diagram or installed product is not proof of effective operation. Live intrusive testing needs a separately approved plan. |
| Assessment and declaration — reviewer/signatory | Reconcile all objective outcomes, gaps, retests and source changes with each drafted answer, then compare any approved submission with its receipt. | Tool completion is not independent assessment, government acceptance or permission to represent a broader scope. |

For each workpaper preserve the evidence location, collection date, covered period, source system, collector, objective reference, expected observation, actual observation and reviewer decision. State any selected test population and untested coverage; never present limited observation as exhaustive assurance.

## Failure branches and decisions

- **Wrong organization or contract:** stop affected collection and submission work, isolate the draft and rebuild the scope record with the contract owner. Do not reuse another supplier's result.
- **Unclear specified information or excluded system:** obtain the contract/security owner's decision and trace the information path. Keep coverage unresolved until the boundary is justified.
- **CMMC certificate supplied:** validate its identity, scope and validity, then request the Canadian authority's case-specific determination through the approved route. Do not claim recognition from technical similarity.
- **Missing or conflicting evidence:** identify the precise objective, owner and missing period; record the contradiction and required follow-up. Do not turn unknown into yes or not applicable.
- **Failed control or overdue action:** retain the adverse result and escalation date. The signatory decides the next authorized representation; the agent cannot erase the gap or fabricate a passing result.
- **Portal interruption or ambiguous send:** save the last completed step, document version, pending approval and any receipt identifier. Recheck the destination and expiry before resuming; never assume a click completed an attestation.
- **Source or contract conflict:** preserve both references and the decision question, route it to the contract/security authority and block only the dependent conclusion.

## Cadence and renewal

Use the annual assessment requirement and actual recorded expiry. Schedule preparation early enough for remediation; the program owner selects and records that internal lead time. Independently review readiness as an engagement practice, not as an invented third-party Level 1 certification requirement. Reassess affected work after material information, contract, supplier, system or incident changes. Confirm current instructions before each declaration.

## Completion and handoff

The preparation packet is complete only when it contains the approved applicability/scope record, complete objective register, evidence-linked judgments, open gaps and retests, exact draft answers, source-change check, signatory decision queue and renewal owner. Label any missing element explicitly. Hand off next actions with owners and dates. An approved submission is a separate milestone requiring its own destination readback and retained result; neither milestone proves a wider certification claim.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared applicability, authority, evidence, technical-test, exception, source-change and renewal requirements.
