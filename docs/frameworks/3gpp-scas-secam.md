# 3GPP SCAS / SECAM — telecom assurance guide

> Original operational guidance for preparing a product assurance engagement,
> not a test specification, laboratory result or certification.

## Source and applicability

Use the [3GPP specification portal](https://portal.3gpp.org/Specifications.aspx)
to identify the applicable product-class specification and release. The
[virtualized-product work item](https://portal.3gpp.org/Specifications.aspx?WiUid=810037&q=1)
was accessible on 2026-09-04 and lists distinct SCAS and SECAM documents. It is
an example catalog entry, not a universal specification selection. The former
[SCAS overview](https://www.3gpp.org/technologies/scas-cert) returned HTTP 403 in
this author check. A link failure does not establish that a specification is
withdrawn.

Record the selected document numbers, release/version, publication status and
customer/lab acceptance criteria. Obtain authorized access and rights confirmation
before using detailed specification text. This guide imports no requirements,
test cases or evaluation procedures. See the
[author review record](../refresh-reviews/3gpp-scas-secam.md); independent review
and publication approval remain pending.

## Engagement focus

Build a traceable evaluation packet for a particular network product build and
configuration. Keep vendor evidence, laboratory evaluation and customer/operator
acceptance distinct. A product family name or an unrelated release report does
not identify the exact subject of assurance.

## Roles

Product and engineering owners identify the build and supported configuration.
The assurance lead coordinates the selected evaluation route with the customer
and laboratory. Authorized evaluators define and perform the assessment under
that route; an independent reviewer challenges the packet. AI may reconcile
versions, evidence requests and findings. It cannot choose a binding evaluation
scope, claim laboratory approval, accept product risk or issue a certificate.

## Before starting

Obtain the charter, product/build manifest, enabled functions/interfaces,
deployment assumptions, component dependencies, customer request, selected source
versions, lab contact and evidence-sharing permissions. If the class or route is
unresolved, prepare the product facts for the assurance lead; do not invent test
requirements. Execute work items with the [agent runbook](../agent-runbook.md).

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Identify the evaluation subject | Engineering supplies model, build, enabled functions, hardware/virtualization context and dependency versions. AI compares these with the proposed handoff. | Frozen subject manifest; inconsistent build IDs block evaluation claims. |
| 2. Resolve the evaluation route | Assurance lead and customer/lab confirm product class, relevant sources/releases, method and responsibilities. | Approved scope and source register; public catalog metadata alone does not authorize a method. |
| 3. Prepare the evidence request map | AI connects each authorized lab request to a custodian, artifact/version, due date and disclosure permission. | Complete request ledger with explicit unavailable items; no copied restricted test content in this repository. |
| 4. Establish the permitted test setting | Lab and engineering record environment, access, production separation, configuration and operational limits. | Approved test plan and matched build; a live operator network is not a default test target. |
| 5. Retain evaluation evidence | Authorized evaluators perform the agreed work. AI indexes reports, raw-result references and exclusions without rewriting outcomes. | Results match the subject and source version; failed or unperformed checks remain visible. |
| 6. Correct and retest | Engineering fixes approved findings; evaluators confirm retest scope and results. | Finding-to-change-to-retest chain tied to the new build; earlier results are not silently reused. |
| 7. Hand off for acceptance | Assurance lead assembles the versioned packet; the authorized customer/operator or scheme decision maker decides acceptance. | Recorded receipt and decision scope. A packet upload is not product acceptance. |

This is an original coordination sequence; the selected evaluation method governs
actual testing and any scheme-specific decisions.

## Evidence and test plan

| Request and custodian | Check | Expected observation | Failure or limit |
| --- | --- | --- | --- |
| Subject/build manifest from engineering | Compare manifest, test environment and report identifiers. | Exact build and configuration are reconciled. | A matching marketing name does not establish identity. |
| Source and scope decision from assurance lead | Trace every requested evaluation area to the selected document/version and authorized method. | Scope references are complete and approved. | An inaccessible source leaves method verification unresolved. |
| Finding/change/retest records from engineering and evaluator | Follow an adverse observation through correction and observed retest. | All three records reference the relevant builds and test conditions. | A patch commit does not prove remediation or evaluation success. |
| Handoff and acceptance records from assurance/customer owners | Read back the delivered packet manifest and resulting decision. | Recipient, version and disposition are explicit. | Delivery, technical evaluation and acceptance are separate outcomes. |

## Failure branches and decisions

A changed interface, hypervisor, component or release triggers an impact decision
by the evaluator before reusing results. Missing lab evidence is `inconclusive`,
not an implied pass. If a report excludes functions the customer expects, flag
the mismatch before handoff. If detailed sources are restricted, retain authorized
references; do not reconstruct their test cases from another publication. Keep
external claims within the exact decision and build covered by evidence.

## Cadence and renewal

Review on release candidates, security findings, dependency changes, method
revisions and customer scope changes. An annual review of marketed-product claims
is an engagement default, not a universal 3GPP recertification deadline. Record
any actual scheme/customer validity period separately with its source and owner.

## Completion and handoff

Deliver the subject manifest, source/scope decisions, evidence request ledger,
permitted result references, findings and retests, disclosure approval, receipt
and acceptance status. Name unresolved tests, unsupported configurations and the
next version-change review. Do not turn readiness work into an assurance award.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md).
