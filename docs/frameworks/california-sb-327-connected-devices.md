# California SB 327 connected-device engagement guide

> Original operational guidance, not California legal text or an enforcement conclusion. Confirm scope and current law through the [California SB 327 legislative record](https://leginfo.legislature.ca.gov/faces/billCompareClient.xhtml?bill_id=201720180SB327).

## Engagement focus

Maintain an accountable lifecycle record for connected devices offered in California: intended function, security and authentication design decisions, data and service dependencies, release changes, vulnerability handling, supplier evidence, and remediation.

## Roles and annual rhythm

Product owners define intended use; engineering maintains release evidence; security reviews changes; legal counsel confirms legal scope; independent reviewers assess traceability. AI organizes approved design and operating records and flags missing owners or change reviews, but cannot decide legal applicability, approve a device release, or assert legal compliance. Reassess at design changes, releases, and material vulnerabilities; preserve human decisions and rationale.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [California SB 327 legislative record](https://leginfo.legislature.ca.gov/faces/billCompareClient.xhtml?bill_id=201720180SB327) and have legal counsel confirm current statutory status, applicability, and effective requirements before each product decision. Retrieved 2026-07-31. This guide is original operational planning, not California legal text, legal advice, a device-security specification, or an enforcement conclusion.

### 1. Connected-device product and California-offer boundary

- **Request and owner:** Product/device model and firmware/service inventory, intended-function description, connectivity and account/authentication design summary, California offer/distribution inputs, data/service dependency record, and named product, engineering, privacy, and legal owners. Cover each device or materially distinct release proposed for the approved boundary.
- **Validate and limit:** Trace a selected device/release to its product owner, intended-function record, connectivity/dependency context, release identifier, and counsel-reviewed applicability question. Use design metadata rather than customer data. This can support an accountable scope record; it cannot decide statutory coverage, consumer status, or legal sufficiency.
- **AI and trigger:** AI may compare approved inventory and release metadata and flag missing owner or scope reviews. Legal counsel decides applicability; human product leaders approve scope. Refresh before a new device, new California offer channel, material connectivity/authentication change, or annual legal review.

### 2. Security-design and release-decision trace

- **Request and owner:** Human-approved security-design decisions in original language, architecture/release review records, authentication/credential-handling decision evidence, threat/vulnerability inputs, test references, release approval, and change/rollback records from engineering, security, and product owners. Cover the defined release population and material patches.
- **Validate and limit:** Inspect a selected release from its intended function and design decision through approved test reference, reviewer, release authorization, and subsequent change record. Preserve confidential engineering details and do not convert test output into a legal conclusion. This can support traceability of the stated release process; it cannot prove device security, defect absence, or compliance.
- **AI and trigger:** AI may index approved review metadata, identify stale test/review links, and draft questions; it cannot approve a release, choose a security design, modify devices, or make a legal conclusion. Humans approve design and release decisions. Trigger on a material firmware, application, cloud-service, credential, or architecture change.

### 3. Vulnerability, supplier, and post-release response record

- **Request and owner:** Vulnerability intake and triage records, remediation and customer/support decision references, supplier component/service responsibility records, update availability evidence, incident/change communications approvals, and closure/retest records from security response, engineering, supplier-management, legal, and product owners.
- **Validate and limit:** Trace a selected material vulnerability or supplier change to the affected release boundary, accountable owners, triage decision, remediation/update path, communications approval, and retest or documented rationale. This can support an accountable post-release response trail; it cannot establish timeliness, product safety, legal notification duties, supplier conformance, or effectiveness for every device.
- **AI and trigger:** AI may organize sanitized case metadata and flag missing owner, status, or retest links. Humans decide severity, customer communications, supplier escalation, legal duties, and closure. Trigger on a reported vulnerability, exploited issue, supplier change, unavailable update path, or annual review.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
