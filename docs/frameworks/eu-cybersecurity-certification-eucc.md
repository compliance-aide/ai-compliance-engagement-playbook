# EU cybersecurity certification / EUCC readiness — engagement guide

> Original operational guidance, not a certification claim or legal interpretation. Confirm scheme scope through [ENISA certification information](https://certification.enisa.europa.eu/index_en) and the [EUCC regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R0482).

## Engagement focus

Maintain product scope, intended use, development and lifecycle evidence, configuration records, vulnerability handling, supplier evidence, assurance activities, claims, and certification-body interactions.

## Roles

Product and security leaders validate evidence; certification bodies and independent reviewers make scheme decisions and test readiness. AI may link authorized artifacts and flag stale claims, but cannot certify, select an assurance level, issue a declaration, approve a release, or submit a certification artifact. Review before material releases and annually.


## Source and applicability

Retrieve the current EUCC implementing regulation and amendments, applicable scheme documents, evaluation-method editions and certification-body instructions. Record the required assurance level and its approved basis. Keep provider readiness, independent evaluation and customer verification as separate activities. A generic Common Criteria certificate is not automatically a current EUCC certificate; establish the actual scheme and status from the issuing records.

## Before starting

Use the [agent runbook](../agent-runbook.md). Identify the product and target-of-evaluation boundary, intended use, configuration, life-cycle records, sponsor, evaluation laboratory and certification-body route where selected. Obtain permitted evidence locations and an agreed test plan. Preserve confidential design information outside public workpapers. If a method or source is unavailable, prepare exact evidence requests rather than inventing criteria.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Define objective | Sponsor identifies readiness, evaluation support or certificate due diligence. | Approved purpose and boundary; customer reliance is not certification authority. |
| 2. Establish scheme basis | Qualified owner confirms editions, assurance target and applicable route. | Source manifest and open interpretation questions. |
| 3. Freeze evaluation scope | Engineering aligns product/build, security target and operating assumptions. | Versioned scope record with excluded functions and unresolved mismatches. |
| 4. Map evidence | Evaluation lead inventories all required evidence and assigns owners. | Complete request ledger, dependencies and accepted handling rules. |
| 5. Collect and check | Custodians supply records; authorized testers perform the agreed checks. | Original evidence, procedure/output references and coverage limitations. |
| 6. Resolve findings | Engineering addresses defects; evaluators review affected evidence and tests. | Fresh retest and impact records; the author does not approve their own certification conclusion. |
| 7. Prepare decision package | Sponsor reconciles scope, evidence and outstanding questions. | Reviewable package for the proper decision maker; no inferred certificate issuance. |
| 8. Maintain and verify claims | Product owner tracks versions, vulnerabilities and certificate status. | Dated authoritative references and change/renewal actions. |

## Evidence and test plan

### Product and security-target alignment

Engineering supplies build identifiers, configuration, interfaces, dependencies, intended use and the agreed security target. Compare each claimed feature and environment condition with those records. Preserve mismatches and omissions; do not silently rewrite a target to match whatever evidence was easiest to obtain. Reopen after product or environment changes.

### Development, evaluation and findings

Custodians supply the evidence requested under the applicable method, with provenance, version and ownership. Link each evaluator question or finding to its response, changed artifact and retest. Record the full inventory and every unresolved item even where the approved method selects particular tests. A clean vulnerability scan is not a substitute for the complete evaluation method.

### Continuity and customer reliance

Product/security owners supply change records, vulnerability handling and available maintenance/certification decisions. Compare the customer's requested use with the actual certified boundary and current status. Distinguish an engineering fix, an evaluator's acceptance and a certification-body decision. None can be inferred solely from another.

## Failure branches and decisions

- Security target and build identifiers conflict: preserve both and resolve the evaluated version before claiming a match.
- Environment assumption has no deployment owner: leave that condition unresolved and assign an observable check.
- Evaluation evidence is missing: name the required artifact and custodian; do not fabricate design details from a product brochure.
- Test fails before observation: record `not_tested`; a tool error is not a security finding.
- Fix changes another evaluated function: assess the affected scope and obtain the required re-evaluation decision rather than retesting only the original symptom.
- Certificate issuance is claimed without an authoritative record: retain pending status and request the issuing reference.

## Cadence and renewal

Follow the actual certificate and scheme conditions, not an invented universal renewal interval. Reopen affected records after release, vulnerability, configuration, environment or scheme changes. Review public claims whenever their referenced scope or status changes.

## Completion and handoff

Deliver the source/method manifest, exact evaluated boundary, complete evidence ledger, unresolved questions, findings/retests and authoritative decisions. For due diligence, state the limits of certificate reliance; for readiness, state remaining evaluation work. Independent source, engagement, skeptical and rights review plus named human publication approval remain required. Structural checks do not establish certification readiness or security effectiveness.

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
