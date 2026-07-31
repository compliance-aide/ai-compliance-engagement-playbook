# CISA Secure by Design — product-security engagement guide

> Original operational guidance, not CISA endorsement or certification. See [CISA Secure by Design](https://www.cisa.gov/securebydesign/blogs).

## Engagement focus

Maintain a product-security evidence program connecting product portfolio and supported versions, secure-design decisions, development and release practice, vulnerability intake and treatment, customer-impact decisions, and substantiation for public claims. Treat a Secure by Design reference as a product-security improvement lens, not an endorsement, certification, proof that vulnerabilities are absent, or authority to ship.

## Roles and annual rhythm

Assign accountable product, engineering, security, privacy, legal, support, vulnerability-response, release, and communications roles. Operators maintain portfolio/version records, design and development artifacts, release approvals, vulnerability/case records, customer-impact decisions, remediation evidence, and claim-support records. Review material products, support commitments, open vulnerabilities, and public claims quarterly; reassess after a material architecture, release, incident, vulnerability, supplier, or customer-impact change. Product owners make release decisions; independent reviewers sample release-to-impact evidence. AI may correlate authorized artifacts and flag unsupported claims, but cannot make product assertions, determine customer notification obligations, approve releases, accept risk, or certify.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [CISA Secure by Design resource](https://www.cisa.gov/securebydesign/blogs) and product-specific legal, privacy, security, and release direction at engagement start; checked 2026-07-31. This plan is original product-security evidence guidance, not an adoption of CISA text, endorsement, certification, or customer-facing security claim.

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


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
