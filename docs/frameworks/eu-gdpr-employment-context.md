# EU GDPR employment-data context — engagement guide

> Original operational guidance, not a uniform EU employment-law conclusion. Consult [GDPR Article 88](https://eur-lex.europa.eu/legal-content/EN-PT/ALL/?uri=CELEX%3A32016R0679) and national rules.

## Engagement focus

Maintain jurisdiction, collective-agreement, worker/applicant/contractor, monitoring, health, biometric, AI-decision, purpose, rights, vendor, and transfer evidence.

## Roles

Counsel and employment owners decide legal basis and monitoring; independent reviewers test records. AI inventories issues, but cannot authorize monitoring or make legal decisions. Review quarterly and annually.


## Source and applicability

Record each employment jurisdiction, worker category, processing purpose and applicable national/collective-agreement context. Use the current GDPR and qualified employment/privacy review alongside the [general GDPR guide](eu-gdpr.md). Do not treat one country's employment interpretation, one group policy or a generic employee consent form as a uniform EU conclusion.

Assign legal decisions by purpose and data category, including additional conditions where relevant. Keep legal basis, transparency, necessity, access, retention and international transfers as separate decisions. A signed notice does not decide all of them.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Obtain the worker/applicant/contractor perimeter, systems and vendors, approved processing records, notices, retention rules, rights process and decision owners. Use synthetic or approved redacted records for QA; restrict health, biometric, disciplinary and assessment information to authorized custodians. Never copy a personnel file into public workpapers.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Establish context | HR/legal identify jurisdictions, people, purposes and applicable sources. | Approved scope and unresolved national questions with owners. |
| 2. Map lifecycle | HR/IT trace recruitment, employment changes, absence, performance and departure records. | Complete system/vendor/data-flow inventory, including derived data and archives. |
| 3. Review proposed uses | Privacy/legal evaluate each use through the workflow below. | Purpose-specific decisions and approved implementation limits. |
| 4. Specify evidence | Custodians assign records, access and observable test criteria. | Work items with population, period, method and handling rules. |
| 5. Verify operation | Authorized reviewers inspect QA collection, access, rights and retention paths. | Original observations, missing coverage and failures recorded separately. |
| 6. Resolve gaps | HR/IT implement approved corrections; legal decides exceptions and affected-person actions. | Retest evidence and outstanding decisions; no inferred legal clearance. |
| 7. Review and hand off | Accountable owners review the evidence and open risks. | Bounded internal report and separately approved communications. |
| 8. Reopen on change | Owners track jurisdiction, vendor, purpose, model and employment-status changes. | Updated decisions and exact next checks. |

## Evidence and test plan

### Purpose, notice and access

HR/privacy supply approved purposes, notices, role permissions and relevant decision records. Compare actual data fields and recipients with those limits. Verify that managers, payroll, health support and recruiting roles see only the access approved for their function. A role label alone does not prove enforced access. Reopen after role or system changes.

### Rights and record retrieval

Privacy/HR supply the approved intake, identity-check, search, review and response procedure. In synthetic QA, trace a request across relevant systems, vendors and archives; retain missing sources. Legal reviews exemptions, third-party information and disclosure decisions. A search export is not automatically a releasable response. Do not disclose a real employee's data to test the process.

### Retention, departure and vendors

Records/legal owners supply the approved schedule and any applicable hold; IT supplies operational evidence. Trace a synthetic departure through access removal, retained records, deletion schedules and vendor instructions. Disabling an account does not demonstrate deletion; departure does not mean every record should be erased immediately. Record each data class and its approved treatment separately, with evidence of execution where due.

## Failure branches and decisions

- A rights search omits a recruiting vendor: preserve the gap and request the missing source; do not call the response complete.
- A manager can retrieve restricted health information contrary to approved permissions: record `not_supported` and escalate access correction without copying that information into the finding.
- A departed employee's account is disabled but vendor records remain: compare those records with the actual retention decision; do not infer either lawful retention or unlawful retention from presence alone.
- A deletion deadline and legal hold conflict: preserve both instructions and obtain the authorized decision before destructive action.
- A tool fails before inspection: record `not_tested`; missing access is not proof of a privacy violation.
- A new model derives employment scores from previously collected data: reopen purpose, data-flow and applicable decision requirements before relying on the old approval.

## Cadence and renewal

Review at the agreed HR/privacy cadence and before changes in purpose, monitoring, location, worker category, vendor or decision systems. Keep rights/incident clocks and employee lifecycle triggers independent of the annual review. Preserve prior decisions with supersession links when circumstances change.

## Completion and handoff

Deliver the jurisdiction/purpose matrix, complete data-flow inventory, legal decisions, evidence index, QA results, unresolved coverage and remediation owners. Separate observed implementation defects from legal conclusions. Independent source, engagement, skeptical and rights review plus named human publication approval remain required. No worker decision, monitoring authorization or compliance claim follows from completing the guide.

## Review a proposed worker-data use before implementation

The [Commission's legal-basis guidance](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/legal-grounds-processing-data_en) warns that employer/employee imbalance can prevent freely given consent and that stricter national employment rules may apply. A signed form is therefore evidence of a recorded choice, not sufficient proof of a valid legal basis. Official indexed source check: 2026-09-04; obtain current national rules and qualified review for the actual processing.

Follow the [agent runbook](../agent-runbook.md). This original workflow prepares a decision and tests an approved implementation; it does not authorize worker monitoring.

1. **Describe one purpose.** HR/business owners identify the actual use, affected applicants/workers/contractors, jurisdiction, data categories, collection method and decision effects. Separate payroll, access security, health support, productivity monitoring and recruitment purposes rather than assigning one blanket basis.
2. **Map the complete flow.** Identify source systems, recipients, vendors, transfers, logs, retention and deletion paths. Include inferred scores and derived profiles, not only raw inputs. Preserve unknown recipients and unverified vendor behavior.
3. **Prepare legal questions.** Legal/privacy owners decide the applicable basis, special-category conditions where relevant, national/collective-agreement requirements, notice, consultation and assessment obligations. AI assembles facts and citations; it cannot choose a convenient basis to bypass an unresolved condition.
4. **Examine any claimed choice.** If consent is proposed, collect the actual notice, alternatives, refusal/withdrawal path and consequences. Trace whether refusal affects work access, treatment or opportunities. Do not test this by coercing a real worker; use approved synthetic QA cases and existing authorized records.
5. **Define approved limits.** Record the exact permitted attributes, users, purposes, duration and access rules. Tie each limit to a test criterion and owner. Notice acceptance does not authorize unrelated reuse.
6. **Observe implementation safely.** In QA, compare configured collection, vendor payloads, access, derived outputs and retention behavior with the approved limits. A policy or consent screen alone does not establish actual data handling.
7. **Resolve and retest.** Preserve excessive collection, unexplained scoring, inaccessible alternatives and failed withdrawal paths as distinct findings. Legal decides processing changes; engineering/HR implement approved corrections and provide retest evidence.
8. **Handoff the decision.** Save scope, legal decisions, evidence, unresolved issues and exact next action. Keep employment decisions, worker communications, system rollout and regulatory reporting under their authorized owners.

### Fictional refusal-path example

A QA onboarding flow labels an optional profile-photo use voluntary, but declining prevents access to the mandatory training portal. The assertion “refusal leaves required training access available” is `not_supported`. The legal validity of the proposed consent remains for counsel to assess using all relevant facts. The agent records the blocked path and asks the implementation owner to correct and retest the alternative; it does not infer that every photo use is unlawful or enroll real workers in the test.

If the QA system is unavailable, record `not_tested` for the test and retain legal conclusions as unresolved. If national requirements are unknown, continue permitted data mapping but do not treat the lack of a retrieved rule as permission. Keep health, biometric and employment records out of public workpapers.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
