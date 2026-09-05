# CISA Secure by Design — product-security engagement guide

> Original operational guidance, not CISA endorsement or certification. See [CISA Secure by Design](https://www.cisa.gov/securebydesign/blogs).

## Engagement focus

Maintain a product-security evidence program connecting product portfolio and supported versions, secure-design decisions, development and release practice, vulnerability intake and treatment, customer-impact decisions, and substantiation for public claims. Treat a Secure by Design reference as a product-security improvement lens, not an endorsement, certification, proof that vulnerabilities are absent, or authority to ship.

## Roles

Assign accountable product, engineering, security, privacy, legal, support, vulnerability-response, release, and communications roles. Operators maintain portfolio/version records, design and development artifacts, release approvals, vulnerability/case records, customer-impact decisions, remediation evidence, and claim-support records. Review material products, support commitments, open vulnerabilities, and public claims quarterly; reassess after a material architecture, release, incident, vulnerability, supplier, or customer-impact change. Product owners make release decisions; independent reviewers sample release-to-impact evidence. AI may correlate authorized artifacts and flag unsupported claims, but cannot make product assertions, determine customer notification obligations, approve releases, accept risk, or certify.

## Source and applicability

CISA's [updated joint-guide announcement](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/3761d70) emphasizes manufacturer responsibility for customer outcomes, transparency and executive leadership. Pin the actual joint guidance and relevant product-security updates rather than treating a blog index as a complete standard. Detailed current guidance review remains pending. Keep this improvement program separate from the [voluntary pledge](cisa-secure-by-design-pledge.md), procurement attestations and certification claims.

## Before starting

Apply the [agent runbook](../agent-runbook.md). Obtain product/version inventory, supported deployment modes, architecture and threat records, customer pain/failure evidence, vulnerability history, release authority and claim inventory. Reuse valid evidence authorization. Identify all supported surfaces before proposing a shared fix; record explicit deferrals rather than assuming parity.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Define customer outcomes | Executive and product owners identify security failures customers currently must prevent or repair themselves. | Owned outcome statement, affected products and baseline evidence. A list of features alone is not an outcome. |
| 2. Map defaults and boundaries | Engineering/security owners inspect default setup, upgrades, privileges, trust boundaries and dependencies. | Design-risk register with supported versions and unknowns; distinguish secure capability from secure default behavior. |
| 3. Choose structural improvement | Owners compare design alternatives, compatibility, customer effort and recurring defect classes. | Approved decision with acceptance criteria and resources. Repeated bugs trigger review of the shared cause, not only another local patch. |
| 4. Implement through release controls | Engineering owners make authorized changes and validate in approved QA. | Build/test evidence covering affected surfaces and migration paths. Release approval remains a separate decision. |
| 5. Verify delivered behavior | Operators/reviewers check the actual delivered version, fresh setup and upgrade behavior. | Observed defaults and customer-impact evidence. A merge or passing unit test alone does not prove delivered security. |
| 6. Handle residual vulnerabilities | Response owners validate reports, coordinate fixes and preserve limitations. | Tracked findings, retests and authorized communications; no assumption of vulnerability absence. |
| 7. Substantiate claims | Product/legal/communications owners compare proposed claims with scope and observed results. | Evidence-linked statement and approval record; draft language is not published communication. |
| 8. Learn and renew | Independent reviewer challenges outcomes and leadership reviews systemic failures. | Owned follow-up, measured progress and next review triggers. |

## Evidence and test plan

**Source and rights snapshot.** Use the official [CISA Secure by Design resource](https://www.cisa.gov/securebydesign/blogs) and product-specific legal, privacy, security, and release direction at engagement start; prior locator snapshot 2026-07-31; detailed current-guidance review pending. This plan is original product-security evidence guidance, not an adoption of CISA text, endorsement, certification, or customer-facing security claim.

### 1. Product portfolio, support, and secure-design-decision package

- **Request and owner:** Product, engineering, security, and support owners provide product/service inventory, supported-version records, intended-use and dependency context, design-review decisions, threat/risk artifacts, security requirements, accountable owners, and review history.
- **Validate and limit:** Trace a selected supported product/version from portfolio record through owner, documented design/security decision, dependency context, and current support status. This cannot prove secure design, validate every dependency, or make a release decision.
- **AI and trigger:** AI may organize supplied design evidence and flag unsupported versions, missing owners, or stale decisions. Authorized humans set product scope, support commitments, and design tradeoffs. Refresh after material feature, architecture, dependency, support, or ownership change.

### 2. Development, release, and vulnerability-treatment package

- **Request and owner:** Engineering, security, release, vulnerability-response, platform, and supplier owners provide development/review evidence, build or test records, release approvals, vulnerability intake/triage, remediation tickets, retest evidence, exceptions, and supplier handoffs.
- **Validate and limit:** Sample one release or vulnerability record from accountable product/version through approved development or treatment decision, test/retest evidence, release/exception approval, and current status. This does not validate all code, authorize deployment, or establish absence of vulnerabilities.
- **AI and trigger:** AI may link supplied artifacts and flag missing approval, retest, or ownership records. Humans approve releases, remediation priority, exceptions, and risk acceptance. Refresh after release, material vulnerability, failed test, supplier change, or incident.

### 3. Customer-impact, claims, and independent-assurance package

- **Request and owner:** Product, support, legal, privacy, communications, security, and independent-review owners provide customer-impact assessments, communication/notification decisions, public claim inventories, evidence citations, review approvals, limitations, corrective actions, and reviewer workpapers.
- **Validate and limit:** Trace a selected public security claim or customer-impact decision to product/version evidence, authorized review, documented limitation, communication decision, and follow-up. This cannot determine notification obligations, make a binding customer representation, or attest for management.
- **AI and trigger:** AI may compare supplied claims to approved evidence and flag unsupported or stale references. Authorized humans approve claims, communications, legal positions, and external statements. Refresh before publication, after material product/security change, and during annual independent review.


## Failure branches and decisions

A default that requires undocumented customer repair remains an open product issue. A fix reaching only one supported surface retains explicit remaining work. Failed upgrade or access checks stop expansion and invoke approved recovery. Missing deployed-version evidence prevents a delivered-fix claim. Preserve full scorer-bound evidence without trimming, sampling or capping; any approved inspection selection must disclose limits. Route legal notification questions to authority without delaying authorized technical preparation. On interruption, save versions, decisions, verified surfaces and next safe action.

## Cadence and renewal

Quarterly coordination and annual program review are management choices, not universal CISA deadlines. Review design risks before material changes and verify each relevant release. Reopen affected decisions after recurring defect classes, incidents, dependency changes or customer failure reports.

## Completion and handoff

Deliver product/surface scope, outcome baseline, design decisions, release and delivered-behavior evidence, remaining vulnerabilities, explicit deferrals and approved claim records. Independent source and skeptical review and named human approval remain necessary for final public conclusions; a secure-design program is not a certification.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
