# CMS MARS-E engagement guide

> Original operational guidance, not CMS framework text, a federal authorization, or a compliance conclusion. Confirm current use and scope through the [CMS MARS-E program page](https://security.cms.gov/learn/mars-e).

## Engagement focus

Maintain a year-round system-assurance record: service boundary, data context, owners, security and privacy evidence, assessment materials, significant changes, authorization conditions, incidents, remediation, and oversight communications.

## Roles

System and business owners establish scope; security and privacy teams retain evidence; independent reviewers assess the engagement trail; authorizing officials make decisions. AI prepares evidence inventories and change-impact questions, but cannot authorize operation, interpret federal obligations, or submit an official package. Update records after material change and retain dated human approvals.

## Source and applicability

**Historical baseline and transition guide.** [CMS regulations and guidance](https://www.cms.gov/marketplace/resources/regulations-guidance) lists ARC-AMPE as effective March 4, 2025, with a March 4, 2026 compliance date. [ARC-AMPE Volume I](https://www.cms.gov/files/document/arc-ampe-vol-1-v102-508-5cr-04112025.pdf), section 2.2 footnote 75, states that it supersedes MARS-E and the NEE GRC Framework. Do not start a current assessment against MARS-E merely because an old contract package or template names it.

For Medicaid work, the [CMS MES security and privacy guidance](https://cmsgov.github.io/CMCS-DSG-DSS-Certification/Conditions%20for%20Enhanced%20Funding/Security%20and%20Privacy/) distinguishes E&E systems connected to the Federal Data Services Hub from non-E&E modules. Verify the actual module, state direction and CMS authority before choosing the baseline. Do not make ARC-AMPE mandatory for every Medicaid module by inference.

Use MARS-E for historical assessment-period reconstruction where justified. For current work, obtain the applicable ARC-AMPE source bundle and templates, current CMS instructions and accountable applicability decision. Record actual artifact versions: filenames, landing-page labels and internal revision text may differ. This transition workflow does not replace a full ARC-AMPE control assessment.

## Before starting

Apply the [agent runbook](../agent-runbook.md). Identify the entity/module, data flows, historical assessment period, current requested decision and governing authority. Confirm authorized evidence repositories and recipients. Keep beneficiary data, tax information and protected security artifacts out of public workpapers and unapproved models. Evidence redaction for agent handling must not silently reduce a separately required official assessment package.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Resolve historical or current use | Program and authorization owners verify assessment period, module, agreements and current CMS direction. | Source-linked baseline decision; old template names do not decide applicability. |
| 2. Preserve the old record | Custodians retain MARS-E scope, versions, evidence, findings and authorization conditions with original dates. | Immutable historical references; do not relabel old findings as ARC-AMPE results. |
| 3. Reconcile current scope | System and privacy owners map present services, data, suppliers, integrations and shared controls. | Approved current boundary and explicit differences from the historical assessment. |
| 4. Build the migration register | Agent indexes the complete adopted successor requirement set and maps old evidence where supported. | Each current requirement has an owner, source reference, evidence need and migration state; new or changed items remain visible. |
| 5. Evaluate and test | Authorized owners and testers obtain current security and privacy evidence against the applicable objectives. | Dated observations, methods and coverage; an unchanged control identifier does not prove unchanged requirements or operation. |
| 6. Reconcile findings | Security lead links old unresolved findings and all new assessment results to corrective actions, owners and dates. | Traceable POA&M with source references; consolidation retains individual provenance and does not erase low-risk findings. |
| 7. Review the package | Independent reviewers challenge scope, evidence, privacy coverage, remediation and decision readiness. | Reviewed package with unresolved limitations and the correct CMS route; an assessment report is not authorization. |
| 8. Obtain and maintain decisions | Named authority makes authorization/risk decisions; approved submitter uses the designated repository. | Verify receipt and actual decision separately. Track conditions and future reviews from authoritative instructions. |

## Failure branches and decisions

- **Legacy template presented as current:** preserve it as historical input, obtain the successor sources and assign the applicability decision before current conclusions.
- **Crosswalk has no evidence:** treat it as a mapping hypothesis, not implementation proof; test the current requirement and retain unmapped items.
- **Provider evidence covers only part of the service:** identify the provider and customer duties, remaining system boundary and missing privacy coverage.
- **Vulnerability scan offered as penetration test:** retain its actual method and seek the required assessment; these artifacts are not interchangeable under CMS MES guidance.
- **Wrong repository or missing receipt:** confirm the actual program-specific route before transmission. Prepared or uploaded does not mean accepted or authorized.

## Evidence and test plan

**Source and rights snapshot.** Use the official [CMS MARS-E program page](https://security.cms.gov/learn/mars-e), current CMS direction, applicable agreement terms, and the organization’s authorized system context; prior snapshot dated 2026-07-31; historical source context, not confirmation of current applicability. This is original evidence-planning language, not CMS framework text, a package template, an assessment result, an authorization decision, or a claim of federal compliance. CMS and organizational authorities decide use, scope, release, risk, and any external representation.

### 1. System boundary, data context, and authorization-governance package

- **Request and owner:** Business, system, privacy, security, contracts, and authorization-support owners provide the service/boundary narrative, approved data-flow and integration records, user and hosting context, agreement/applicability records, accountable-owner roster, authorization milestones, and documented assumptions.
- **Validate and limit:** Trace one selected data-supported service or integration to its owner, approved boundary/data-context record, dependency, decision date, and authorization-status evidence. This supports bounded traceability; it cannot determine MARS-E applicability, categorize data, or authorize operation.
- **AI and trigger:** AI may organize approved metadata and flag missing ownership, stale diagrams, or unresolved dependencies. Humans approve scope, data handling, contract interpretation, and authorization decisions. Refresh after a material data flow, boundary, hosting, integration, contract, or mission change.

### 2. Security, privacy, and operating-evidence package

- **Request and owner:** Control, platform, application, operations, incident, privacy, and supplier owners provide original implementation narratives, configuration/change references, access and monitoring evidence, test observations, incident/remediation records, privacy review inputs, and supplier evidence permitted for use.
- **Validate and limit:** Sample an evidence claim through a dated source artifact, system/process context, owner, observation period, limitation, corrective action, and retest or follow-up record. This can support evidence-quality review; it cannot validate every safeguard, decide privacy obligations, or make a compliance conclusion.
- **AI and trigger:** AI may index authorized records, identify missing provenance, and draft evidence requests. Humans select tests, interpret outcomes, approve technical changes, and control incident or privacy communications. Recollect after a material change, incident, failed test, supplier change, or remediation milestone.

### 3. Assessment, change, and decision-trail package

- **Request and owner:** System, security, change-management, executive, and authorization-support owners provide assessment workpapers, open-item/remediation records, exception and risk-decision records, significant-change analyses, management reviews, source-change watch, and independent-review observations.
- **Validate and limit:** Trace one selected finding, change, or exception from source evidence through accountable review, named decision authority, action/expiry, and follow-up. This supports a governed readiness discussion; it cannot accept risk, close an authorization action, submit an official package, or replace independent review.
- **AI and trigger:** AI may flag overdue actions, expiring decisions, or incomplete review trails and prepare non-authoritative workpapers. Humans approve risk treatment, package content, external communications, and authorization actions; independent reviewers challenge evidence without making those decisions. Review quarterly, annually, and after material change or source update.


## Cadence and renewal

Derive assessment, POA&M, authorization-condition and reporting dates from the applicable program and current CMS instructions. Do not carry a historical MARS-E cadence into the successor by default. Reassess after data-flow, hosting, supplier, privacy, incident, significant-change or source changes. Preserve old and new periods so migration cannot create an artificial improvement by dropping scope or findings.

## Completion and handoff

Deliver the historical/current baseline decision, scope comparison, full successor coverage register, safe evidence references, findings, corrective actions and authorization/submission states. Identify the next action, owner and missing evidence without chat history. Historical MARS-E review and successor readiness remain separate deliverables, with current controls and decisions still requiring their own evidence.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
