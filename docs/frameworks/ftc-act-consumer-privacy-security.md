# FTC Act consumer privacy and security engagement guide

> Original operational guidance, not legal advice, an enforcement prediction or a compliance claim. Draft pending independent source, skeptical and rights review.

## Source and applicability

Use the [FTC Act record](https://www.ftc.gov/legal-library/browse/statutes/federal-trade-commission-act), [FTC privacy and security guidance](https://www.ftc.gov/business-guidance/privacy-security), applicable orders and qualified counsel. The Act record identifies the statute and the Commission's authority concerning unfair or deceptive practices. The privacy guidance emphasizes honoring privacy promises and protecting sensitive information; its links to other laws are applicability leads, not proof every linked rule applies.

This draft read those two official pages. Full statutory text, relevant interpretations, entity-specific orders and applicable sector rules remain unverified. The more detailed Start with Security resource timed out during retrieval. Do not treat this evidence-management workflow as a legal test for unfairness, deception, jurisdiction or notification duties.

## Engagement focus

Connect what consumers are told to what the product and its service providers actually do with their information. Preserve both the historical representation and the corresponding behavior, audience and period. Assess security practices even when no explicit public promise was found; absence of marketing language is not evidence that no security duties exist.

## Roles

Legal counsel determines applicability and legal conclusions. Product, marketing and privacy owners approve representations and data uses. Engineering, security and vendor owners provide operating evidence. Support and incident teams preserve complaints and timelines. An independent reviewer challenges coverage, contradictions and stale assumptions. Named officials approve changes, remedies and communications.

AI may inventory authorized records, compare claims against supplied evidence, identify gaps and draft workpapers. AI cannot decide legal liability, approve public claims, contact consumers or regulators, make notification decisions, accept risk or change production systems. Independent review and accountable human decisions remain required.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Record product/version, audience, jurisdictions, period, authorized evidence access, QA environment, owners and source limitations. Identify the full in-scope surface population: website, app, notices, settings, onboarding, support scripts, sales materials and partner-facing statements where consumers receive them. Retain an explicit coverage state for each surface; do not silently select only favorable statements.

## Ordered workflow

1. **Define scope and authority.** Obtain counsel's applicable-obligation and order register and the product owner's surface/data inventory. Output: versioned scope with unresolved applicability questions assigned, not assumed away.
2. **Capture representations.** Preserve exact approved wording, placement, audience, effective dates, surrounding context and consumer journey. Distinguish express statements from possible implications needing review. Output: statement register tied to historical versions and owners.
3. **Map actual practices.** Trace collection, purpose, storage, access, sharing, retention and disposal through the product and providers. Include behavior before and after relevant consumer choices. Output: data-flow register with actual implementation evidence and unknowns.
4. **Compare claim to behavior.** For each assertion, define a factual test and expected result before examining outcomes. Match scope, population and period. Test authorized QA journeys and inspect supplied operational records. Output: assertion-level result; a notice screenshot alone cannot prove enforcement.
5. **Evaluate security evidence.** Map owner-approved safeguards and provider responsibilities to actual configuration, monitoring, change and incident evidence. Record boundaries and uncovered systems. Output: factual observations for qualified review; do not turn a checklist count into a legal reasonableness conclusion.
6. **Reconcile complaints and changes.** Link every known relevant complaint, incident and change to affected statements, data practices, decisions and corrective actions. Preserve original intake and trigger times. Output: action register with owners, deadlines from verified sources and unresolved communications decisions.
7. **Review and verify correction.** Give the reviewer the complete packet and disagreements. Prepare changes for authorized owners, then verify approved implementation across affected surfaces and periods. Output: factual closure evidence and remaining decisions. A drafted rewrite is not a corrected live practice.

## Evidence and test plan

### Consumer representations and data-practice package

Product, marketing, privacy and legal owners provide statement versions, notice placement, consent/choice journeys, data flows and change records. Reconcile every in-scope statement against the practice it describes. For a deletion promise, distinguish request receipt, processing, downstream copies and any disclosed retention exceptions. Record unverified providers and historic populations; never infer deletion from an empty user interface.

### Security and service-provider package

Security, engineering and vendor owners provide inventory, risk/change records, responsibility assignments, actual safeguard evidence and exceptions. Trace each known in-scope flow to recipient, purpose, approved use, relevant settings and evidence period. A contract term is evidence of a commitment, not proof of provider behavior. Distinguish observed transmission from unknown downstream retention or use.

### Complaint, incident and corrective-action package

Support, incident, privacy and legal owners provide the complete authorized intake population, relevant timelines, investigations, approvals and remediation records. Reconcile duplicates without deleting distinct events. Complaint clusters help prioritize review but do not prove prevalence, harm or legal violation. Preserve original metadata and record missing channels; an empty queue proves nothing if intake failed.

For every case record criterion, fixture or source reference, scope/date/build, expected and observed results, limitations and accountable owner. Keep raw consumer information, confidential incident details and credentials outside this public repository. Use redacted references and authorized synthetic QA fixtures.

## Failure branches and decisions

- Confirmed factual contradiction: mark the affected assertion not_supported, preserve evidence and route correction to product/privacy/legal owners. Do not assert a legal violation from that result alone.
- Missing provider or historical evidence: mark the precise claim inconclusive or not_tested; do not extend a current test to earlier versions.
- Choice displayed but not enforced: separate successful UI interaction from failed downstream behavior. Check every affected route before closure.
- New notice but unchanged historical handling: keep prior representations and populations in scope; counsel determines what changes or communications are permitted or required.
- Incident or regulator contact: preserve the timeline and escalate to the authorized officials. Do not wait for the next periodic review or send a response autonomously.

Fictional desk case: a QA user switches off an optional sharing setting; the screen confirms success, but the same event still goes to the configured analytics recipient contrary to the approved factual criterion. The setting-display claim is supported and the no-transmission claim is not_supported. Recipient retention and legal conclusions remain unproven.

## Cadence and renewal

Set a documented cadence from applicable obligations, orders and business risk. Reopen affected work before material representation, product, provider or data-use changes, and after incidents, significant complaints or new legal direction. Do not invent universal quarterly or annual FTC requirements. Recheck actual behavior after remediation and preserve the version history.

## Completion and handoff

Deliver the source/applicability register, complete surface and data-flow inventories, assertion tests, evidence gaps, complaint/incident links, proposed corrections, reviewer disagreements and named decision owners. Use supported, not_supported, inconclusive, not_applicable or not_tested per assertion. Keep factual evidence status distinct from legal conclusions and task completion. Public changes, notifications, remedies and risk acceptance require their own authorization and verified receipts.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) and [agent runbook](../agent-runbook.md). A completed workpaper does not prove compliance or confer authority to communicate externally.
