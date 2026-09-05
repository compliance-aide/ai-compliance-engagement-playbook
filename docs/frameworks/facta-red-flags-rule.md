# FACTA Red Flags Rule engagement guide

> Original operational guidance, not FTC rule text or a legal conclusion. Confirm scope and current duties through the [FTC Red Flags Rule resources](https://www.ftc.gov/business-guidance/privacy-security/red-flags-rule).

## Engagement focus

Maintain a risk-based identity-theft prevention record: covered-account scope, accountable owners, identified patterns, detection and response evidence, vendor dependencies, program updates, incidents, and management review.

## Detection-to-response workflow

Use the [agent runbook](../agent-runbook.md). This is an original execution
recommendation. The [FTC business guide](https://www.ftc.gov/business-guidance/resources/fighting-identity-theft-red-flags-rule-how-guide-business)
was identified through indexed official text on 2026-09-04: it distinguishes
entity coverage from covered-account analysis and describes identifying, detecting,
responding to and updating red flags. Full current rule text and applicable
regulator jurisdiction still require verification before legal conclusions.

1. Have legal identify the relevant entity, regulator and account-coverage basis.
   Reconcile existing and proposed account types, opening channels and access paths.
   Do not assume a business account is excluded or that every organization offering
   delayed payment is automatically covered. Record unresolved classifications.
2. For each approved in-scope account/channel, link plausible warning patterns to
   the approved program, detection method, evidence source and response owner.
   A generic list of fraud risks does not show how any signal will be detected.
3. Define an observable test criterion before execution: synthetic input, expected
   signal, destination queue, responder and authorized response behavior. Use
   QA-named workspaces and synthetic identities. Do not create real credit accounts,
   forge identity documents, contact customers or block access during this review.
4. Exercise each approved scenario end to end. Record source event, detector
   output, routing, responder acknowledgment and action evidence. Retain failed
   delivery, suppressed alerts and not-run scenarios; never equate zero alerts
   with zero identity-theft risk when detection coverage is unknown.
5. Keep suspicion separate from confirmed identity theft. An authorized owner
   decides the proportionate response using the approved program and case facts.
   AI must not deny service, accuse a person, freeze an account or choose a legal
   reporting outcome from a warning alone.
6. Verify the approved action in its actual system of record. A case marked closed
   does not demonstrate that a required action occurred. Preserve legitimate
   no-action decisions with their rationale instead of inventing a mandatory
   account closure for every alert.
7. Trace provider-generated signals across the organizational boundary: provider
   event, delivery, local ingestion, assigned owner and disposition. A supplier's
   contract promise is distinct from observed routing. Identify responsibility
   gaps and report failures explicitly.
8. Reconcile the complete in-scope scenario and case population to results and
   owners. Feed observed gaps, changed account channels and new patterns into an
   approved program update, then retest affected paths. Preserve the original
   failure as well as the later correction; do not truncate scoring evidence.

**Failure branches:** an unavailable test environment means detection is
`not_tested`. A generated warning that fails to reach the required queue makes
routing `not_supported`, even when detection is `supported`. Program effectiveness
remains unproven when material response evidence is missing. Record each assertion
separately from work status and legal determinations.

**Fictional desk case:** a synthetic address-change warning is generated, but a
provider webhook is rejected and no case reaches the response queue. Detection
is `supported` against the approved signal criterion; delivery is `not_supported`
against the approved routing criterion. The absence of a local case is not proof
that no warning occurred. No actual person or account is implicated.

## Roles and annual rhythm

Business and compliance owners determine covered-account scope; operational teams preserve detection and response evidence; legal counsel confirms obligations; independent reviewers test program records. AI can organize approved evidence, surface aging reviews, and draft questions, but cannot determine coverage, decide a response, or make regulatory representations. Review the program periodically and after material fraud-pattern or service changes with human approval.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
