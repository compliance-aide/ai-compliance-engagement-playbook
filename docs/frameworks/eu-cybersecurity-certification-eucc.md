# EU cybersecurity certification / EUCC readiness — engagement guide

> Original operational guidance, not a certification claim or legal interpretation. Confirm scheme scope through [ENISA certification information](https://certification.enisa.europa.eu/index_en) and the [EUCC regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R0482).

## Engagement focus

Maintain product scope, intended use, development and lifecycle evidence, configuration records, vulnerability handling, supplier evidence, assurance activities, claims, and certification-body interactions.

## Roles and annual rhythm

Product and security leaders validate evidence; certification bodies and independent reviewers make scheme decisions and test readiness. AI may link authorized artifacts and flag stale claims, but cannot certify, select an assurance level, issue a declaration, approve a release, or submit a certification artifact. Review before material releases and annually.


## Verify a certificate claim before relying on it

The [ENISA EUCC overview](https://certification.enisa.europa.eu/browse-topic/eucc_en) identifies two scheme assurance levels, substantial and high, and describes certification-body decisions following laboratory evaluation. The scheme is maintained and amended; retrieve current legal and scheme documents rather than freezing the original 2024 act. Indexed source check: 2026-09-04; full scheme review remains pending.

Follow the [agent runbook](../agent-runbook.md) and use one work item per assertion. This procedure is an original evidence-checking aid, not the scheme's evaluation method.

1. **Identify the requested assurance.** Record the exact product/version, configuration, intended deployment and claim the customer wants to rely on. Identify the approved source of the required assurance level; AI does not choose it from a marketing description.
2. **Retrieve authoritative records.** Locate the certificate, certification report and security target through official scheme/issuing-body sources. Preserve identifiers, retrieval dates, status and missing documents. A vendor badge or copied PDF alone does not establish current status.
3. **Match the evaluated boundary.** Compare the target of evaluation with actual hardware, firmware/software, enabled features, components and environment. Record each match, mismatch and unknown. Do not extend a certificate to an entire product family without evidence covering the claimed member.
4. **Read assumptions and exclusions.** Identify what the evaluated product expects from administrators, configuration and its operating environment. Assign each relevant condition to a deployment owner and observable check. Do not treat an excluded feature as evaluated.
5. **Check continuity.** Reconcile changes after evaluation, relevant maintenance records, vulnerability information and any status change with the certification body’s current records. A newer build is not automatically covered or automatically uncertified; resolve its actual status.
6. **Draft a bounded conclusion.** State exactly which requested claim the records support. A configuration mismatch contradicts a claim of an exact match; unavailable status evidence leaves current validity unresolved. Neither establishes a general claim that the product is insecure.
7. **Handoff decisions.** Send unresolved scope, assurance and maintenance questions to the designated product/certification owner. Preserve their answers and authoritative references. Procurement, deployment and public claims retain their own approval gates.

### Fictional boundary mismatch

The supplied certificate identifies firmware 3.0 with feature X disabled. The proposed QA configuration uses firmware 3.1 with X enabled. The assertion “this configuration matches the supplied evaluated configuration” is `not_supported`; whether an updated record covers it is `inconclusive` pending evidence. Request the applicable maintenance/certification record and security target. Do not downgrade the real configuration silently to make the paperwork fit or label all 3.1 deployments insecure.

### Missing records and tool failures

If the official registry cannot be queried, record `not_tested` for that query and keep the current-status conclusion `inconclusive`. Preserve any historical record with its date. If an authoritative record explicitly indicates suspension or withdrawal, retain that adverse evidence rather than treating it as a mere access gap. No agent-generated workpaper substitutes for a certification-body decision.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
