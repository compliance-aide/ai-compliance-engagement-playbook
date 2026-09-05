# EU GDPR employment-data context — engagement guide

> Original operational guidance, not a uniform EU employment-law conclusion. Consult [GDPR Article 88](https://eur-lex.europa.eu/legal-content/EN-PT/ALL/?uri=CELEX%3A32016R0679) and national rules.

## Engagement focus

Maintain jurisdiction, collective-agreement, worker/applicant/contractor, monitoring, health, biometric, AI-decision, purpose, rights, vendor, and transfer evidence.

## Roles and annual rhythm

Counsel and employment owners decide legal basis and monitoring; independent reviewers test records. AI inventories issues, but cannot authorize monitoring or make legal decisions. Review quarterly and annually.


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
