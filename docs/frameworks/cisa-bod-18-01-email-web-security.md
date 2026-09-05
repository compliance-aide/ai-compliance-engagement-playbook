# CISA BOD 18-01 email-and-web-security engagement guide

> Original operational guidance, not directive text, an applicability determination, a configuration command, or a federal compliance claim.

## Source and applicability

Start with [CISA's directive index](https://www.cisa.gov/news-events/directives), the [original BOD 18-01](https://www.cisa.gov/sites/default/files/bod-18-01.pdf), its [published exception](https://www.cisa.gov/sites/default/files/18-01-exception.pdf), and current agency direction. The original directive was issued October 16, 2017 and addresses federal email and publicly accessible web services. Its implementation clocks ran from issuance or specified events; starting this engagement does not restart them. Agency authority must resolve applicability, amendments, exceptions and current reporting channels. Do not assume a private provider is directly subject merely because it hosts a federal service; record its contractual responsibilities separately.

The original required-action areas include mail transport protection, domain authentication and reporting, and HTTPS/HSTS and protocol/cipher treatment for web services. The original DMARC rollout progressed from monitoring to rejection; monitoring alone is not the final target. Exact technical criteria and any exception must be verified from current authorized direction before judging or changing a service. Full source and exception retrieval was unavailable during drafting; do not treat this guide as a verified configuration baseline.

## Engagement focus

Establish every owned domain and relevant service, determine its approved requirements, observe its actual behavior, correct authorized gaps safely, and preserve independent validation. Keep DNS publication, email authentication, message transport and web protection as separate evidence questions.

## Roles

Agency authority confirms applicability and reporting. Domain, DNS, mail and web owners maintain inventories and implement approved changes. Provider managers obtain hosted-service responsibilities and evidence. Security reviewers validate observations; risk authority decides permissible exceptions. AI organizes authorized evidence and drafts questions and work items. It cannot change production settings, accept risk, submit official reports or declare compliance without the required human authority.

## Before starting

Use the [agent runbook](../agent-runbook.md). Obtain current directive/exception material, agency baseline, domain and service inventories, sending-provider list, public web endpoints, prior validation, change records and decision contacts. Identify receiving, sending and non-mail domains rather than treating absence of an MX record as proof that a domain needs no review. Keep protected mail reports and message data in authorized storage. Reuse valid read-only authorization.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Resolve authority | Agency owner verifies current directive status, exception scope and applicable agency instructions. | Source-pinned requirement register with historical deadlines distinguished from current remediation dates; unresolved interpretation assigned to authority. |
| 2. Reconcile scope | DNS, mail and web owners compare domain registries, hosting inventories, sending providers and public endpoints. | Complete declared population, owners and provider dependencies; unknown or retired-looking services remain open until disposition is verified. |
| 3. Assign criteria | Security and service owners link each relevant service to approved email, DNS or web criteria. | Per-service evidence needs and decision owners. A provider assertion does not replace customer-side verification. |
| 4. Observe present state | Authorized operators collect DNS records, mail transport and authentication evidence, web connection/header/certificate observations and monitoring records using approved methods. | Dated observations tied to endpoint, method and vantage point. Missing, failed and unassessed checks remain distinct. |
| 5. Plan remediation | Owners identify legitimate senders and dependent subdomains before policy enforcement, HSTS changes or protocol retirement. Prepare acceptance and recovery plans through change control. | Approved bounded change items with impact, provider coordination and recovery contacts. Do not publish an enforcement policy from an AI guess. |
| 6. Implement and retest | Authorized operators validate changes in approved QA conditions, execute approved production changes and obtain independent readback. | Actual DNS/service behavior and legitimate delivery or application checks recorded. A saved control-panel setting alone does not close a finding. |
| 7. Resolve exceptions | Security and agency authority review failures, published exception relevance, remediation and residual risk. | Explicit decision with scope, authority, expiry or review trigger. A historical temporary exception is not presumed permanent or universal. |
| 8. Handoff | Agency lead assembles evidence and any required reporting packet for authorized review/submission. | Review receipt, unresolved items and next dates. Prepared reporting is distinct from submitted and acknowledged reporting. |

## Evidence and test plan

Maintain three linked packages:

- **Domain and service boundary:** inventories, registration/provider relationships, ownership, hosting and routing dependencies, purpose and disposition. Reconcile the full declared population before tracing individual services. Preserve unexplained inventory differences.
- **Email, DNS and web operation:** approved baseline, dated configuration observations, mail report references, certificate and web-protection results, changes and provider evidence. Follow a service from requirement to observation and any correction. Separate a published authentication policy from evidence of legitimate sender alignment and delivery. Separate an HTTPS response from the required redirect, HSTS and protocol checks. Treat these as planning distinctions, not a substitute for source-specific tests.
- **Monitoring, exceptions and challenge:** alert records, assigned actions, authority decisions, expiry, independent objections and retests. Follow each failure to disposition without hiding it in an aggregate score. Reconcile provider and agency closure when responsibilities cross boundaries.

Preserve all evidence intended for an assessment scorer without trimming, sampling or capping. Any approved inspection selection must identify population and limits; it cannot prove every endpoint conforms. Record collection errors and untested endpoints explicitly. Do not publish mail content, personal data, credentials or confidential service details in this repository.

## Failure branches and decisions

If current source or exception text is unavailable, continue authorized inventory work but hold affected technical conclusions. If an endpoint cannot be reached, retain the error and classify the check as unassessed. If legitimate delivery or service access fails after a change, stop expansion and follow the approved recovery plan; do not assume every DNS or preload change can be reversed immediately. If provider responsibility is disputed, assign escalation and keep the gap open. On interruption, preserve source versions, observations, pending approvals and next safe action.

## Cadence and renewal

Use current agency monitoring and reporting direction. Quarterly coordination and annual independent review are optional management rhythms, not replacements for directive obligations. Revalidate affected services after domain, provider, routing, certificate, application or security-policy changes. Review exception expiry and material monitoring failures promptly under the approved escalation plan.

## Completion and handoff

Deliver source/applicability decisions, full domain/service register, approved baseline, observations and limits, change/readback evidence, exceptions, open actions and review schedule. Include actual submission and acknowledgement receipts only when observed. Independent source review and named human approval remain necessary for final conclusions and official reporting.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared authority, evidence, technical-test, exception, source-change and renewal requirements.
