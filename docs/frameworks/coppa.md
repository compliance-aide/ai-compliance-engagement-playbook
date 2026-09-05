# COPPA — engagement guide

> Original operational guidance, not FTC guidance or a compliance conclusion. Check the [FTC children’s privacy resource](https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy).

## Engagement focus

Maintain service/data-flow, purpose, retention, third-party, parental notice/consent, withdrawal/deletion, advertising/SDK, incident, complaint, and feature-change evidence.

## Roles

Operators own service configuration and consent execution; independent reviewers sample evidence and scope. AI indexes evidence and drift, but cannot decide applicability, validate a parent, make disclosure decisions, or certify. Review after material change and annually.

## Source and applicability

Use the amended 16 CFR Part 312 and the [FTC compliance plan](https://www.ftc.gov/business-guidance/resources/childrens-online-privacy-protection-rule-six-step-compliance-plan-your-business), updated May 2026. The FTC identifies separate verifiable parental consent for third-party disclosures unless integral to the service. Its [final-rule announcement](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-changes-childrens-privacy-rule-limiting-companies-ability-monetize-kids-data) identifies expanded personal-information definitions and purpose-limited retention. Do not reuse a pre-amendment SDK or consent checklist unchanged.

Counsel decides child-directed, mixed-audience or actual-knowledge applicability and any exception from actual service facts. Screen connected services, plug-ins and third-party collection, not only the operator's forms. The [FTC February 2026 age-verification policy statement announcement](https://www.ftc.gov/news-events/news/press-releases/2026/02/ftc-issues-coppa-policy-statement-incentivize-use-age-verification-technologies-protect-children) describes conditional enforcement discretion; it is not blanket permission for new collection. Verify its full conditions and current status before relying on it.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Identify legal, product, parent-support, security and vendor owners. Use synthetic child/parent scenarios in a QA environment. Keep real children's records and identity evidence in authorized systems, outside public artifacts or unapproved models. Create one work item per applicable obligation, service, purpose and recipient; separate preparation observations from legal decisions and actual consent records.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Resolve coverage | Legal and product owners review audience, knowledge, features and applicable exceptions. | Dated source-linked determination with unknowns assigned; an age field alone does not decide scope. |
| 2. Inventory collection | Engineering maps forms, identifiers, media, SDKs, telemetry, advertising and backend recipients. | Complete purpose/data/recipient inventory showing collection timing, including before any permission step. |
| 3. Reconcile notices and permissions | Privacy owner maps each purpose and disclosure to approved notice and consent design or a documented exception. | Versioned decision matrix distinguishing collection/use consent from separately applicable third-party disclosure consent. |
| 4. Test permission boundaries | Authorized testers exercise synthetic pending, granted, refused and revoked states across interfaces and backend paths. | Expected and observed collection/disclosure behavior with scope and gaps; a checked box does not prove enforcement. |
| 5. Test parental rights | Support and engineering trace approved parent-review, withdrawal and deletion scenarios through verification, records and recipients. | Safe identity/authority process and execution evidence; no agent independently validates a real parent or contacts a child. |
| 6. Verify security and retention | Security and data owners document safeguards, recipient assurances, purpose-specific retention and actual disposal operation. | Evidence of protection and deletion with unresolved copies visible; indefinite retention is not justified by vague future analytics. |
| 7. Remediate and retest | Operational owners correct approved failures and review affected historical collection or disclosure with counsel. | Retest plus separate incident/legal follow-up; fixing the interface does not resolve prior data handling automatically. |
| 8. Review and sustain | Independent reviewers challenge coverage and execution; accountable leaders approve representations and changes. | Complete evidence package, open decisions and renewal triggers; no automatic certification claim. |

## Failure branches and decisions

- **SDK sends data before permission:** record the actual recipient, fields and timing; assign blocking/configuration remediation through authorized change control and legal review of prior events.
- **Parent declines non-integral disclosure:** test the legally approved service behavior and prevent a general consent flag from enabling that disclosure.
- **Age-verification vendor claims an exemption:** request evidence against every applicable policy condition; a vendor label cannot supply the legal conclusion.
- **Deletion job succeeds but copies remain:** identify backups, logs and recipient-held data, retain limitations and obtain the required retention/legal decision before closure.
- **Changed purpose or recipient:** reopen notice, consent and provider review before relying on the previous permission record.

## Evidence and test plan

**Source and rights snapshot.** Use the [FTC children’s privacy resource](https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy) and qualified U.S. privacy/legal review; prior snapshot dated 2026-07-31; revalidate current amended rule and guidance. This original plan does not reproduce COPPA requirements or decide whether a service is directed to children, has actual knowledge, needs parental consent, qualifies for an exception, or meets a regulatory obligation.

### 1. Service audience, data-flow, and third-party package

- **Request and owner:** Service and feature inventory; human-approved audience/scope analysis inputs; data-flow and SDK/tag register; data categories, purposes, collection points, recipients, retention settings, and accountable product, privacy, engineering, and ad-tech owners.
- **Validate and limit:** Trace a selected child-facing or age-neutral feature from interface and collection event through system, purpose record, SDK/recipient, and retention setting. This supports a factual operating map; it cannot establish child-directed status, actual knowledge, applicability, or permitted collection/disclosure.
- **AI and trigger:** AI may reconcile approved telemetry, inventory, and vendor metadata and flag new collection paths. Legal/privacy humans decide scope and classifications. Refresh for a feature, audience, SDK, advertising, or data-flow change.

### 2. Notice, parental-permission, and lifecycle-operation package

- **Request and owner:** Notice/version history; consent or permission workflow configuration where used; parent-contact and withdrawal/deletion procedures; redacted case records; identity/authority verification design; retention/deletion outputs; and training records owned by privacy, support, records, and engineering.
- **Validate and limit:** Independently reperform a non-production or de-identified workflow trace from notice/entry point to recorded human review, system action, and closure. This can show a documented workflow produces evidence; it cannot validate a parent, decide consent sufficiency, determine an exception, or prove all requests were handled correctly.
- **AI and trigger:** AI may create de-identified sampling lists and identify incomplete records; it cannot verify a parent, contact a child or parent, alter consent, or decide a request. Recheck after a notice, collection, permission, retention, or workflow change.

### 3. Provider, advertising, incident, and governance package

- **Request and owner:** Vendor/SDK register; contractual/instruction and due-diligence records; advertising or analytics configuration evidence; complaint/escalation and incident/exercise records; material-change approvals; remediation/retest log; and management-review record.
- **Validate and limit:** Trace a selected provider, ad-tech change, complaint, or incident to its factual evidence, accountable human, decision record, corrective action, and retest. This supports accountable oversight; it cannot determine provider compliance, notification duties, risk acceptance, or an enforcement outcome.
- **AI and trigger:** AI may flag unreviewed vendors and aging actions in approved metadata. Privacy, security, legal, and communications humans decide contracts, external communications, risk treatment, and closure. Refresh after a provider, advertising, incident, or annual review.


## Cadence and renewal

Annual program review is an engagement convention; apply the amended rule's specific security, retention and other frequencies after source verification. Recheck every material SDK, audience, collection, advertising, model-use, permission or provider change. Preserve historical notice and consent versions so later changes do not obscure which processing was authorized at the time.

## Completion and handoff

Deliver coverage decisions, complete obligation and data-flow registers, notice/permission mappings, synthetic test evidence, provider safeguards, retention/deletion records and unresolved issues. State what was drafted, approved, executed and verified. Identify the next action, owner and required evidence without earlier chat history; preparation completion is not proof that every child or parent interaction complied.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
