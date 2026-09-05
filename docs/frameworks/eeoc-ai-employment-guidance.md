# EEOC AI and employment guidance — engagement guide

> Original operational guidance, not an EEOC standard or discrimination conclusion. Consult [EEOC AI publications](https://www.eeoc.gov/index.php/eeoc-publications).

## Engagement focus

Maintain recruiting, selection, monitoring, productivity, pay, promotion, termination, vendor, accommodation, accessibility, provenance, outcome, and remediation evidence.

## Roles

HR, counsel, accessibility, and qualified reviewers make employment decisions; independent reviewers test evidence. AI cannot make employment decisions, determine discrimination, or replace expert review. Review quarterly and annually.

## Source and applicability

Use current [EEOC disability/AI resources](https://www.eeoc.gov/eeoc-disability-related-resources/artificial-intelligence-and-ada) and counsel-selected employment-law sources for each jurisdiction and process. The [EEOC visual-disability guidance](https://www.eeoc.gov/laws/guidance/visual-disabilities-workplace-and-americans-disabilities-act) identifies algorithmic screen-out risks and reasonable-accommodation duties, including alternative testing where appropriate absent undue hardship. It distinguishes suggested transparency practices from obligations; preserve that distinction.

Inventory all employment uses, including tools that influence rather than make the final decision. Record actual function, job context, decision stage, version, data sources and human reliance. Qualified counsel and assessment specialists determine applicable law, validation methods and evidence needs. Vendor assurances or a human final click do not establish lawful operation.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Name HR, employment counsel, accessibility, validation/statistical, privacy and vendor owners. Use synthetic scenarios for workflow tests. Keep identifiable applicant, employee, medical and complaint records in authorized systems. Do not infer protected traits or collect sensitive data merely to populate an AI analysis; qualified humans approve lawful data access and methodology.

## Ordered workflow

| Step | Action and accountable owner | Output and exit condition |
| --- | --- | --- |
| 1. Define use and authority | HR and counsel identify jobs, decisions, affected populations and legal scope. | Complete use-case register with accountable human decision-makers and unresolved legal questions. |
| 2. Examine selection design | Qualified specialists review job-related criteria, inputs, outputs and vendor claims. | Documented evaluation plan tied to actual job/process and tool version; no generic fairness certificate substitution. |
| 3. Verify access and accommodation | Accessibility and HR owners review barriers, assistance and alternative assessment routes. | Approved process with contact, decision owner and protected handling; AI does not decide accommodations. |
| 4. Trace workflow behavior | Authorized reviewers exercise synthetic application, assessment, escalation and human-review journeys. | Expected/observed routing, timeouts and failure treatment; inaccessible or incomplete attempts remain visible. |
| 5. Evaluate outcomes | Qualified reviewers apply approved methods to lawfully accessed evidence. | Population/denominator definitions, missing-data limits, subgroup/period context and uncertainty; no automated discrimination conclusion. |
| 6. Investigate concerns | HR/counsel trace complaints, overrides and vendor changes with appropriate confidentiality. | Human decisions and evidence of affected uses, including historical cases requiring review. |
| 7. Remediate and retest | Owners implement authorized changes and specialists repeat affected evaluation and accessibility checks. | Version-specific results and unresolved limitations; changed thresholds require fresh review. |
| 8. Approve and monitor | Independent reviewers challenge evidence; responsible leaders approve continued use. | Scoped approval and monitoring triggers, with employment decisions retained by authorized humans. |

## Failure branches and decisions

- **Assessment confuses assistive-technology use with low productivity:** record the measurement mismatch and route accommodation/validation review; do not rank the person from that signal.
- **Applicant cannot complete the interface:** preserve the access barrier separately from ability to perform the job; test the approved assistance route.
- **Vendor reports an acceptable aggregate metric:** request job-, stage-, version- and population-specific support; averages cannot resolve every relevant concern.
- **Missing or withdrawn applications vanish from analysis:** reconcile the population and reason codes before interpreting results.
- **Human reviewer always follows the tool:** inspect actual override authority and decision evidence; nominal oversight is not demonstrated scrutiny.
- **Tool changes during recruitment:** retain versions and affected decision periods; do not combine results as though one unchanged procedure was used.

## Evidence and test plan

**Source and rights snapshot.** Consult current [EEOC AI publications](https://www.eeoc.gov/index.php/eeoc-publications); prior snapshot 2026-07-31; verify current source status. This is original operational planning, not EEOC guidance, legal advice, a validation protocol, or a discrimination conclusion. Qualified employment counsel confirms legal scope, jurisdictions, and permissible use before each engagement.

### 1. Employment-use boundary and human-authority record

- **Request and owner:** Approved inventory of AI-assisted recruiting, selection, monitoring, productivity, pay, promotion, termination, accommodation, and vendor uses; job/process boundary; affected populations; named HR, counsel, accessibility, privacy, security, and business authorities; and supplier roles.
- **Validate and limit:** Trace a selected use to the human decision-maker, business purpose, affected employment process, vendor/system version, accessibility/accommodation path, and counsel-reviewed question. This supports an accountable scope record; it cannot determine legality, job relatedness, or discriminatory impact.
- **AI and trigger:** AI may organize approved, de-identified metadata and flag missing owners or change reviews. Humans decide use, employment actions, scope, and legal questions. Refresh before a new or materially changed tool, job/process, vendor, model, data source, accommodation workflow, or jurisdiction.

### 2. Design, validation, and operating-evidence trace

- **Request and owner:** Human-approved requirements, data/provenance summaries, vendor representations, accessibility/usability evidence, test or monitoring-method descriptions, outcome-review records where lawful and appropriate, escalation/appeal process records, and change approvals from HR, counsel, accessibility, privacy, security, and product/vendor owners.
- **Validate and limit:** Inspect a selected employment use through its approved purpose, version, documented human oversight, evidence source, change record, and escalated concern. Preserve access controls and avoid using identifiable applicant/employee content in AI workpapers. This can support traceability of the stated process; it cannot prove nondiscrimination, statistical validity, accessibility, or lawful use.
- **AI and trigger:** AI may index authorized metadata and flag missing provenance, reviewer, or version links; it cannot screen applicants, rank employees, infer protected traits, decide an accommodation, change a model, or interpret results as a legal conclusion. Qualified humans approve methods, changes, and remediation. Refresh after an outcome concern, complaint, model/data/vendor change, accessibility issue, or process failure.

### 3. Concern, remediation, and governance review record

- **Request and owner:** Complaint/concern intake references, investigation and escalation records under appropriate privilege/access controls, vendor issue records, remediation/retest evidence, training/oversight records, exception decisions, and quarterly/annual governance review from HR, counsel, accessibility, and independent reviewers.
- **Validate and limit:** Trace a selected concern to protected handling, accountable reviewer, decision authority, remediation or rationale, follow-up, and governance oversight. This supports accountable response tracking; it cannot resolve a complaint, determine discrimination, waive rights, or substitute for legal or expert review.
- **AI and trigger:** AI may prepare restricted, non-authoritative evidence indexes and flag overdue follow-up; it cannot access protected records without authorization, contact individuals, make employment decisions, approve settlements, or publish conclusions. Humans approve investigations, communications, risk decisions, and closure. Review quarterly and annually, and after a material allegation, enforcement development, or tool/process change.


## Worked example: inaccessible assessment

This fictional workpaper illustrates the runbook; it is not an executed test or a legal finding. The [DOJ hiring-technology guidance](https://www.ada.gov/resources/ai-guidance/) explains that tests should measure relevant job abilities and that accessible alternatives or adjustments may be required. It also warns against unlawful medical inquiries. Review disability barriers separately; success for one assistive technology does not prove coverage of other needs.

**Approved assertion:** the QA application preserves an unfinished assessment and routes an accessibility request to HR without recording a failed skills result. **Fixture:** synthetic application QA-17, assessment version A, approved keyboard/screen-reader configuration, simulated support request. No diagnosis or real applicant record is needed.

| Observation supplied by the tester | Agent result and next action |
| --- | --- |
| The assessment's controls are unreachable and the workflow records a failed skills result. | `not_supported` for the approved workflow assertion. Preserve UI and event evidence; assign the product defect to engineering and the accommodation decision to HR. Do not infer the applicant lacks skills. |
| The browser test tool crashes before opening the assessment. | `not_tested`. Save the tool error and assign rerun; this does not establish an accessibility defect. |
| Support confirms receipt, but downstream application status cannot be retrieved. | `inconclusive`. Request status evidence; a support acknowledgment does not prove absence of adverse processing. |
| Authorized QA retest shows preserved status and successful HR routing. | `supported` only for this configuration and case. Retain prior failure, link the fix and seek reviewer acceptance; no general nondiscrimination conclusion. |

Handoff: product owner supplies the corrected QA build and event records; HR confirms the approved routing expectation; independent reviewer checks the retest. Separate investigation of any real historical impact belongs to authorized HR/counsel, not this fictional example.

## Cadence and renewal

Quarterly and annual reviews are planning conventions, not universal legal intervals. Reopen review before material tool, job, threshold, input, population, vendor or accommodation-process changes and after credible concerns. Record source status and jurisdiction-specific requirements; historical guidance availability alone does not establish current legal interpretation.

## Completion and handoff

Deliver the use/authority register, approved evaluation method, accessibility/accommodation evidence, outcome-review limits, concern decisions and remediation retests. State what was designed, tested and approved. Identify the next owner, action and evidence without prior chat. No claim of nondiscrimination, legal compliance or statistical validity follows merely from completed paperwork.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
