# China Cybersecurity Law engagement guide

> Original operational guidance, not statutory text, Chinese legal advice, a regulatory filing, or a compliance claim. Confirm the current law and implementing measures through the [National Laws and Regulations Database record](https://flk.npc.gov.cn/detail?fileId=&id=021e7d7684474107b8f3febbb1c4f8b5&title=%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E6%B3%95&type=) and qualified local counsel.

## Engagement focus

Maintain a jurisdiction-aware cybersecurity operating record for in-scope networks, systems, services, operators, suppliers, and data flows. Preserve scope determinations, accountable roles, asset and service inventories, security-operating evidence, incident records, change decisions, supplier dependencies, and escalation history. Treat interactions with other China data, privacy, sectoral, and implementing rules as a legal and operational coordination problem, not as an automated mapping exercise.

## Source and applicability

Source check: 2026-09-04. The [NPC amendment decision](https://www.npc.gov.cn/npc/c1773/c1848/c21114/wlaqfxz/wlaqfxz002/202511/t20251103_449242.html) identifies amendments effective January 1, 2026. Record the current consolidated law and applicable implementing measures, not only the original 2016 text. Detailed current statutory and sector-rule review remains an engagement input requiring qualified China counsel. Do not reuse old article numbers without verifying them.

Legal owners decide operator status, jurisdiction, critical-infrastructure questions, applicable protection requirements and interaction with data/privacy rules. A foreign-facing service, hosting location or supplier contract alone is not a legal classification. Record the authority and evidence for each determination.

## Roles

Business and system owners establish factual service boundaries. Security and operations owners supply implementation and incident evidence. Procurement tracks suppliers. China-qualified legal owners determine obligations and communications; designated management owns risk decisions. Reviewers challenge evidence. AI organizes permitted metadata and drafts questions; it cannot classify critical infrastructure, approve transfers, notify authorities, accept risk or authorize technical changes.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Name the entity, network/service, location, period, source version, owner, inputs, output and exit check. Require approved scope, obligation register, inventory and evidence-handling permissions. If a requirement is unclear, record the precise legal question and continue independent fact gathering. Do not copy sensitive network or personal information into this public repository.

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Confirm governing scope | Legal/business owners record entity and operator context, source versions, implementing measures and unresolved determinations. | Approved applicability register; unresolved classifications are not assumed negative. |
| 2. Reconcile the network | System owners compare services, hosting, connections, administration, suppliers and data flows with actual inventory. | Boundary/dependency record and discrepancies with owners. |
| 3. Assign obligations | Security/legal owners link each applicable requirement to responsible teams, required evidence, deadlines and approval authority. | Complete scoped coverage register; vague “security compliant” labels cannot replace requirements. |
| 4. Examine operation | Reviewers compare approved procedures with dated access, monitoring, vulnerability, change and recovery evidence. | Workpapers with expected/actual observations and untested coverage. Written intent is not operational proof. |
| 5. Verify incident routing | Incident/security owners provide approved escalation procedures and authorized exercise records. Trace facts, timestamps, decisions and follow-up. | Incident workpaper with legal notification questions routed to their owner; no invented reporting timer. |
| 6. Address suppliers and gaps | Procurement/security owners obtain scoped supplier evidence and assign corrective work. Separately authorized implementers make changes; reviewers retest. | Dependency/finding/action/retest chain, preserving adverse evidence and unresolved limitations. |
| 7. Record decisions | Coordinator prepares the exact review packet for management/legal owners and reads back authorized decisions from the system of record. | Decision scope, conditions and dates distinguish preparation from actual approval or submission. |
| 8. Maintain coverage | Owners monitor service, location, supplier, incident and legal changes and reopen affected obligations. | Owned change/review queue with historical source versions retained. |

## Evidence and test plan

Use the complete approved coverage register. These original examples do not reproduce the law or substitute for applicable assessment procedures. Preserve all evidence supplied to a scorer without trimming.

| Package and owner | Verification | Limitation |
| --- | --- | --- |
| Boundary/accountability — system/legal owners | Trace a service to its operator decision, deployment, dependencies and current scope record; reconcile inventory discrepancies. | A selected trace does not prove legal scope or complete discovery. |
| Security operation — security/operations | Follow an alert, access review or vulnerability through affected service, action, approval and retest. | Missing logs are a visibility gap, not proof of no incidents. |
| Change/recovery — engineering/service owner | Compare authorized change or exercise expectations with actual results and remaining dependencies. | QA results do not establish production state; no intrusive test is authorized by this guide. |
| Suppliers — procurement | Trace a supplier change to affected systems, obligations, evidence and decision. | Contract promises do not establish implementation or legal sufficiency. |
| Governance — reviewer | Reconcile findings, due dates, decisions and retests with the exact proposed claim. | A closed ticket or accepted risk is not a compliance determination. |

Record source, collector, date, covered period, environment, obligation reference, evidence pointer, expected/observed result, limitation, reviewer and next action. Record selected test populations and untested scope separately.

## Failure branches and decisions

- **Old law or article reference:** preserve its historical version and obtain current interpretation before using it for present conclusions.
- **Unresolved operator or critical-infrastructure status:** route the factual packet to qualified legal owners; do not decide from an AI-generated classification.
- **Wrong network or missing supplier:** isolate affected evidence and reconcile the true boundary before reusing conclusions.
- **Failed control or missing telemetry:** retain the adverse result, assign action and record its effect on the decision packet.
- **Incident with possible reporting duty:** follow approved incident escalation, preserving original timing. Legal/incident authorities decide and authorize communications.
- **Unapproved location or data-flow change:** flag the proposed change for its applicable decision owners; do not infer transfer permission.
- **Interrupted work or uncertain filing/update:** preserve last completed step, versions and pending approval; read back the destination before retrying.

## Cadence and renewal

Use applicable legal obligations and actual decision conditions. Owners select internal review intervals and distinguish them from legal deadlines. Reassess after material network, service, supplier, location, data-flow, incident or source changes. An annual review is not a universal substitute for event-driven obligations.

## Completion and handoff

The preparation packet contains approved applicability, current source versions, boundary, complete obligation coverage, operating and incident evidence, supplier gaps, retests and decision questions. Mark omissions. Filings, notices and production changes are separate authorized milestones with destination evidence. Handoff identifies next action, owner, due date and dependency.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared applicability, authority, evidence, technical-test, exception, source-change and renewal requirements.
