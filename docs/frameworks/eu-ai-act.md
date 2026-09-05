# EU AI Act — engagement guide

> Original operational guidance, not a legal classification, conformity determination or authorization to market an AI system.

## Source and applicability

Use the [current consolidated Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689), applicable amendments and official implementation material. Record the consolidation date and verify the operative Official Journal acts before legal sign-off. Do not use a proposal, press release or old implementation chart as the sole legal authority.

The Commission [announced entry into force of the AI Omnibus on 27 July 2026](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force). Its [implementation timeline](https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline), checked 2026-09-04, places Annex III high-risk rules at 2 December 2027 and Annex I product high-risk rules at 2 August 2028. It identifies Article 50 transparency rules as applying from 2 August 2026, with a narrower transition for certain pre-existing synthetic-content systems until 2 December 2026. These are different obligation tracks, not a blanket extension.

Article 113 specifies the phased dates; Article 111 contains legacy-system/model transitions. Legal owners must bind each claimed transition to the actual system/model, market-entry date, changes and applicable paragraph. Article 25 requires reassessing provider responsibilities for relevant rebranding, substantial modification or changed purpose; a supplier contract alone does not settle every role question. Article 50 separates obligations by actor and use and specifies exceptions. Evaluate its applicable paragraph rather than adding one generic “AI-generated” label everywhere.

## Engagement focus

Maintain a complete EU-facing inventory and a source-linked decision record for each system, model dependency, purpose, operator role, affected group, operating context and version. Connect each applicable obligation to implementation evidence and an accountable owner. Do not equate inventory completion, a policy document or vendor assurance with compliance.

## Roles

Legal/compliance owns interpretation, classification and applicable dates. Product and business owners own intended use and deployment decisions. Engineering owns version, data and evaluation records. Operations owns monitoring and incident evidence; designated oversight staff own intervention readiness. Privacy, security and accessibility specialists review their respective effects. Independent reviewers challenge source and evidence conclusions. AI drafts and reconciles records; authorized tools can collect or test within scope, but do not confer authority to classify finally, sign, file, publish or release.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Obtain system inventory, intended-use descriptions, market/deployment dates, contracts, model/version records, operating geography, affected-person context and named decision owners. Record missing inputs explicitly. Build one work item per proposed obligation, including source paragraph, role, applicability decision, effective date, evidence request, test criterion and owner. Keep protected training data and affected-person records in authorized storage.

A text-only agent prepares the request and expected observation. An agent with tools records exact configuration, procedure, output and coverage. Neither infers legal exemption from inability to access evidence.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Inventory | Business/product owners reconcile purchased, built, embedded and externally supplied AI uses. | Complete inventory with unresolved discovery gaps and distinct system/model records. |
| 2. Determine role and scope | Legal owner reviews actual activities, purpose, markets and changes. | Reasoned applicability and actor record; unresolved classifications remain open. |
| 3. Screen obligations | Legal and risk owners evaluate prohibitions, high-risk branches, transparency, model obligations and other applicable laws. | Complete obligation/disposition ledger with source locators and dates; no single risk label substitutes for all branches. |
| 4. Plan evidence | Control owners translate applicable obligations into observable criteria. | Requests tied to system/version, population, period, reviewer and expected result. |
| 5. Evaluate implementation | Authorized testers and reviewers inspect records and execute agreed QA procedures. | Original evidence, failed tests, limitations and contradictions retained; no invented observations. |
| 6. Resolve gaps | Engineering/product owners correct defects; legal resolves interpretation questions. | Retest evidence and explicit open decisions, with approved escalation for potential prohibited use or harm. |
| 7. Prepare decisions | Accountable owner assembles required release, conformity or filing package for the applicable route. | Reviewable package with prerequisites and limitations; preparation is not approval or submission. |
| 8. Monitor and renew | Operations tracks changes, feedback and incidents against the approved use. | Dated monitoring record, escalation decisions, next review and reopened obligations. |

## Obligation routing workpaper

These are planning prompts, not a replacement for the complete legal requirements. The legal owner supplies the applicable source and final disposition for every branch.

| Branch | Information needed before deciding | Evidence work to assign |
| --- | --- | --- |
| Scope and operator role | Actual activity, intended use, geography, contract and change history | Trace role assertions to operational facts; resolve conflicting vendor/customer descriptions. |
| Potential prohibited use | Real functionality, intended and observed use, affected people and any proposed exception | Escalate promptly with source and facts; avoid executing the harmful scenario merely to fill a checklist. |
| High-risk system | Product/use classification, applicable annex, version and transition basis | Assign the relevant provider/deployer and assurance workstreams; keep preparation separate from current legal applicability. |
| Transparency | Actor, interaction/content type, first exposure and claimed exception | Inspect the actual user/content path, disclosure evidence and applicable technical marking evidence separately. |
| General-purpose model | Whether the entity supplies a model or integrates one, model lineage and market date | Retrieve relevant model-provider information and assign remaining system-level responsibilities. |
| Other law and contracts | Personal-data, sector, employment, consumer and contractual context | Keep separate legal bases and owners; one framework determination does not clear the others. |

## Failure branches and decisions

- High-risk work is deferred until a future date: check currently applicable transparency and other obligations separately; document the exact transition basis.
- Vendor declares “AI Act compliant” without system/version/role evidence: preserve the claim as supplier input, request its basis and leave unsupported assertions open.
- A purpose changes from drafting to ranking people: reopen classification, actor and evaluation records before relying on the old approval.
- An oversight policy exists but staff cannot intervene in the observed QA path: record the failed operational criterion as `not_supported`, even if policy existence is `supported`.
- Test access fails: record `not_tested` with the tool error and recovery owner; do not infer product behavior.
- Applicability is unresolved: record `inconclusive` for the disputed conclusion and assign legal review; do not convert it to `not_applicable`.
- Monitoring finds potential harm: preserve evidence, invoke the approved incident process and prepare the decision packet. Do not wait for an annual review or independently send a regulator report.
- Model or configuration changes after evaluation: determine affected assertions and retest scope; a unchanged product name does not preserve evidence validity.

## Worked handoff example

Fictional QA system “Applicant assistant” was approved only to draft internal notes. A new configuration ranks applicants, while its inventory still lists note drafting. The assertion “current use matches the approved purpose” is `not_supported` from the observed configuration. The legal classification remains `inconclusive` pending review; the agent does not declare it prohibited or high risk. Product supplies the current purpose and deployment record, legal reassesses the applicable route, and the tester prepares new authorized evaluation criteria. The old approval cannot close the changed-use work item.

## Evidence and test plan


**Source and rights snapshot.** Use the [European Commission AI regulatory framework](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), the applicable official EU legal text and implementation material, and qualified EU legal review; prior snapshot 2026-07-31; recheck current sources. This is original evidence-planning language, not AI Act text, a legal classification, conformity assessment, declaration, registration, or market-access conclusion. Legal and accountable product owners confirm source status, applicability, role, and permitted handling of supplied records.

### 1. AI-system role, purpose, and lifecycle package

- **Request and owner:** AI governance, product, engineering, privacy, security, and business owners provide an approved system inventory, intended purpose, provider/deployer and other declared role records, users and affected groups, deployment locations, interfaces, dependency/model records, version history, and material-change decisions.
- **Validate and limit:** Trace one selected system/version from the inventory to its accountable owner, intended-purpose record, declared role, deployment context, dependencies, and review date. This supports traceability; it cannot determine whether a system is in scope, prohibited, high risk, or properly classified.
- **AI and trigger:** AI may reconcile authorized metadata and flag absent owner, version, or change links. Humans decide role, classification, intended purpose, and release scope. Refresh before a new deployment or material purpose, model, data, interface, geography, or ownership change.

### 2. Risk, human-oversight, and release-decision package

- **Request and owner:** Product, engineering, safety/risk, quality, privacy, security, and human-oversight owners provide approved risk records, test and evaluation references, human-intervention design and training records, release criteria, limitation disclosures, change approvals, exceptions, and remediation decisions.
- **Validate and limit:** Trace a selected release or material change through its approved risk/review record, evaluation evidence reference, human-oversight readiness record, limitation, accountable decision, and follow-up. This does not establish safety, accuracy, human-control effectiveness, conformity, or authorization to release.
- **AI and trigger:** AI may index evidence and identify missing approvals, stale evaluation links, or unresolved actions. Accountable humans approve risk treatment, exceptions, deployment, and user-facing disclosures. Refresh after a significant modification, adverse finding, incident signal, or changed operating context.

### 3. Transparency, monitoring, and incident-readiness package

- **Request and owner:** Operations, product, legal, compliance, security, and support owners provide communication/version records, monitoring and feedback records, incident/escalation playbooks, event and corrective-action logs, retention/access controls, and external-reporting decision records where applicable.
- **Validate and limit:** Trace a selected monitoring alert, complaint, or exercise to the source record, owner, escalation path, decision, corrective action, and closure evidence while protecting affected-person data. This cannot determine seriousness, reporting duty, notice content, or a regulator-facing conclusion.
- **AI and trigger:** AI may organize redacted records, identify overdue follow-up, and draft review questions. Humans decide escalation, notification, corrective action, and any external statement or filing. Refresh after an incident, serious complaint trend, monitoring change, regulatory update, and at quarterly review.


## Cadence and renewal

Review at the agreed operating cadence and before material purpose, model, data, user, geography, interface or role changes. Recheck legal source and deadlines when amendments or implementation measures change. Reopen affected records after incidents, complaints or adverse evaluations. Set reminders against each obligation's actual date, not one annual compliance anniversary.

## Completion and handoff

Deliver the source/date manifest, full system and obligation inventories, role/classification decisions, evidence index, test and monitoring records, unresolved disagreements, remediation owners and exact next decisions. Separate factual evidence results from legal conclusions and market-access decisions. Independent source, engagement, skeptical and rights review plus named human publication approval remain required. No actual system evaluation, regulator filing or conformity conclusion follows merely from completing this guide.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared applicability, authority, evidence, technical testing, exceptions, source changes and renewal.
