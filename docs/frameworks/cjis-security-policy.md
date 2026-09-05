# CJIS Security Policy — engagement guide

> Original operational guidance, not CJIS content or an audit finding. Confirm current material at the [FBI CJIS resource center](https://le.fbi.gov/cjis-division/cjis-security-policy-resource-center/requirement-companion-document-pdf).

## Engagement focus

Establish CJI boundary and agreements; maintain authorized-user, device, service, vendor, access, training, event, and evidence records; track policy/state-agency changes.

## Roles

Operators own CJI-safe evidence; independent reviewers sample records without designing fixes. AI cannot ingest CJI into unapproved tools, change access, make dissemination decisions, or represent a CJIS audit finding. Use an owner-approved review calendar tied to applicable requirements and change triggers.

## Source and applicability

Do not assume the newest published policy is the applicable audit baseline. [Texas DPS policy documents](https://www.dps.texas.gov/section/crime-records/cjis-documents) identify v6.1, released June 25, 2026, for modernization planning while stating that Texas audits through March 31, 2027 use v5.9.5. This is a dated Texas example, not authority for another jurisdiction. Obtain the responsible CJIS Systems Agency's current audit, implementation and transition instructions; record separate versions and dates where they differ. Check companion-document versions against the actual policy instead of trusting a page label.

Use the full adopted FBI policy, applicable state supplement, agreements and agency instructions as the requirement set. The companion document is an indexing aid, not permission to omit requirements or interpret a policy conflict. Resolve ambiguous applicability, effective dates and contractor obligations with the designated authority. This guide does not supply a complete control list or numerical technical settings.

## Before starting

Apply the [agent runbook](../agent-runbook.md). Record the agency, assessment period, policy version, authority, permitted evidence environment and named evidence custodians. Work with approved metadata or safe pointers; do not paste CJI, raw personnel screening records, credentials or protected logs into public repositories or an unapproved model. A redacted label does not by itself establish handling authorization.

Maintain one work item per requirement and applicable system or population: source reference, owner, applicability decision, evidence, test, observed result, limitation and next action. Use the shared result vocabulary separately from work status. Missing records are inconclusive; an observed unmet requirement is not_supported. Only the authorized reviewer issues official findings.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Confirm authority and versions | Agency security lead obtains current CSA instructions, audit basis, transition dates and applicable agreements. | Version register with decision references; unresolved conflicts block the affected conclusion, not unrelated evidence collection. |
| 2. Establish the CJI boundary | System, records and vendor owners trace receipt, processing, storage, transmission, backup, support and disposal, including remote administrators and shared services. | Owned data-flow and asset register, approved boundary and documented gaps; encryption alone does not remove a service from scope. |
| 3. Build full coverage | Agent indexes the adopted policy and supplements; responsible owners assign every applicable requirement and justify exclusions. | Complete requirement register with population and evidence plans. Keep future-version gap assessment separate from current audit results. |
| 4. Collect safe evidence | Custodians supply approved references for agreements, access authorization, personnel prerequisites, training, technical operation, physical safeguards and incident procedures. | Dated evidence tied to each requirement and scope; restricted artifacts remain in their authorized repository. |
| 5. Test operation | Authorized reviewers select methods and populations; approved testers compare expected and observed access, account lifecycle, device/configuration status, logs and handling behavior. Use synthetic data in QA for demonstrations. | Traceable results with coverage and limitations; one passing account or vendor attestation cannot establish the whole population. |
| 6. Resolve gaps and incidents | Agency lead assigns findings, uncertainties, corrective actions and due dates; incident owners use the applicable escalation procedure immediately when triggered. | Owned action record and human decisions; assessment work does not delay an existing incident duty or invent an extension. |
| 7. Correct and retest | Operational owners perform authorized changes, preserve recovery options and collect evidence; reviewers retest the affected requirements and related systems. | Closure rationale based on observed correction. Ticket closure and internal risk acceptance do not by themselves satisfy an external requirement. |
| 8. Review and hand off | Independent reviewer challenges scope, applicability, evidence and exceptions; designated authority controls formal audit and disclosure decisions. | Draft package with current and future-version results separated, open items, decision owners and next review dates. |

## Failure branches and decisions

- **Wrong version or companion mismatch:** preserve prior results, identify changed requirements and obtain the applicable baseline. Do not relabel old evidence as satisfying new controls without comparison.
- **Vendor says it is CJIS compliant:** request the exact service, jurisdiction, contract, responsibility allocation and agency acceptance evidence. A marketing statement cannot substitute for these records.
- **CJI appears in an unapproved destination:** stop further transfer, preserve safe incident metadata and invoke the authorized incident process. Do not copy the content into a remediation ticket or independently destroy potential evidence.
- **Training is current but authorization is missing:** record the missing prerequisite separately; training completion does not grant system or dissemination access.
- **Collection permission fails:** report the affected evidence gap and request an authorized custodian output. Do not attempt alternate protected-system access or record a pass.

## Evidence and test plan

**Source and rights snapshot.** Use the current [FBI CJIS Security Policy resource center](https://le.fbi.gov/cjis-division/cjis-security-policy-resource-center/requirement-companion-document-pdf), applicable CJIS Systems Agency direction, executed agreements, and authorized handling environments; prior evidence-plan snapshot dated 2026-07-31; revalidate policy and agency direction before use. This plan is original evidence-planning guidance, not reproduced CJIS policy, a dissemination decision, an audit finding, or a compliance conclusion. The CJIS Systems Agency and designated authorities confirm applicability, handling, and release boundaries.

### 1. CJI boundary, agreement, and authorized-actor package

- **Request and owner:** CJIS security officer, agency, legal, records, and service owners provide approved CJI boundary records, system/service inventory, data-flow and storage context, access-role roster, executed agreement/authorization references, vendor/shared-service register, and scope-change log. Retain only approved metadata or redacted pointers in this engagement record.
- **Validate and limit:** In an authorized environment, trace a selected system or service to its accountable owner, approved CJI boundary, relevant agreement/authorization reference, access-role record, and review date. This supports a bounded scope observation; it cannot determine dissemination authority, prove complete CJI discovery, or grant access.
- **AI and trigger:** AI may organize non-CJI metadata only after a human verifies the tool and handling authorization; it may flag missing ownership or review dates. Humans determine CJI handling, scope, access, agreements, and release decisions. Refresh after new system, supplier, data flow, role, agreement, or state/CJIS direction change.

### 2. Authorized-access, device, and operational-assurance package

- **Request and owner:** Access, identity, endpoint, network, application, training, and operations owners provide approved role/access evidence, authorization and training records, device/service status evidence, event-review metadata, configuration/change records, incident/escalation records, and documented limitations. Collect CJI only where the approved environment and authority permit it.
- **Validate and limit:** Using a human-approved, CJI-safe method, sample one authorized role, device, or service from accountable ownership through dated authorization, operation, review, and recorded exception. This can support evidence traceability; it cannot prove ongoing security, perform an audit, authorize access, or alter a system.
- **AI and trigger:** AI may index approved non-sensitive evidence metadata and draft questions; it cannot receive CJI in an unapproved tool, query protected systems, modify access, or make a security conclusion. Humans approve collection, testing, access changes, and remediation. Recollect after access, device, service, training, incident, or material configuration change.

### 3. Exception, incident, and independent-review package

- **Request and owner:** CJIS governance, security, system, and incident owners provide authorized exception or variance records, compensating-action evidence, incident/escalation references, corrective-action plans, target dates, retest records, state/CJIS communications where releasable, and independent-review workpapers.
- **Validate and limit:** Trace a selected exception or incident follow-up from authorized source reference through accountable assignment, human decision, corrective action, retest, and remaining limitation. This supports accountable oversight; it cannot accept risk, determine reportability, close an incident, or represent an official CJIS audit result.
- **AI and trigger:** AI may flag overdue actions or expiry dates from approved metadata and prepare a non-authoritative packet within the authorized environment. Humans approve risk, reportability, disclosure, corrective-action closure, and external statements; independent reviewers sample records without directing operational fixes. Refresh after a material incident, exception expiry, missed review, source/state change, quarterly check, and annual review.


## Cadence and renewal

Derive requirement-specific training, access review, testing, reporting and retention dates from the adopted policy and CSA instructions. Quarterly checks and annual management review in this engagement are planning conventions unless a cited requirement establishes them. Reopen affected work after a policy transition, personnel or vendor change, new data flow, incident, failed test or expired exception. Preserve audit-period evidence and historical version mappings.

## Completion and handoff

Deliver safe evidence pointers, full coverage register, scope and version decisions, observed results, unresolved gaps, corrective actions and reviewer decisions. Identify the next action, its owner and required evidence without reliance on chat history. A draft package is ready for review only when omissions are visible; it is not an official CJIS audit result, access approval or certification.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
