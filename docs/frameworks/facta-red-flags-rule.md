# FACTA Red Flags Rule engagement guide

> Original operational guidance, not FTC rule text or a legal conclusion. Confirm scope and current duties through the [FTC Red Flags Rule resources](https://www.ftc.gov/business-guidance/privacy-security/red-flags-rule).

## Source and applicability

Use the [agent runbook](../agent-runbook.md). This is an original execution
recommendation. The [FTC business guide](https://www.ftc.gov/business-guidance/resources/fighting-identity-theft-red-flags-rule-how-guide-business)
was identified through indexed official text on 2026-09-04: it distinguishes
entity coverage from covered-account analysis and describes identifying, detecting,
responding to and updating red flags. Full current rule text and applicable
regulator jurisdiction still require verification before legal conclusions.


Keep entity/regulator jurisdiction and account classification as separate approved
decisions. This workflow concerns identity-theft prevention; do not assume it
resolves separate address-discrepancy, card-issuer, privacy or breach duties.

## Engagement focus

Maintain a risk-based identity-theft prevention record: covered-account scope, accountable owners, identified patterns, detection and response evidence, vendor dependencies, program updates, incidents, and management review.

## Before starting

Define the full account/product/channel population, review period, provider paths,
program version, approved criteria and reviewer roles. Use
[work items](../../templates/work-item.md) to separate signal generation, delivery,
response decision and action verification. Identify the systems of record and
who may access restricted case evidence. Store only non-sensitive references here.

Have the program owner approve synthetic test inputs and expected outcomes.
Include relevant negative cases so ordinary activity is not automatically treated
as theft. Do not invent precision, recall or acceptable error thresholds; obtain
the owner's criteria and retain any limitations of the test design.

## Ordered workflow


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

## Failure branches and decisions

 an unavailable test environment means detection is
`not_tested`. A generated warning that fails to reach the required queue makes
routing `not_supported`, even when detection is `supported`. Program effectiveness
remains unproven when material response evidence is missing. Record each assertion
separately from work status and legal determinations.

**Fictional desk case:** a synthetic address-change warning is generated, but a
provider webhook is rejected and no case reaches the response queue. Detection
is `supported` against the approved signal criterion; delivery is `not_supported`
against the approved routing criterion. The absence of a local case is not proof
that no warning occurred. No actual person or account is implicated.

## Roles

Business and compliance owners determine covered-account scope; operational teams preserve detection and response evidence; legal counsel confirms obligations; independent reviewers test program records. AI can organize approved evidence, surface aging reviews, and draft questions, but cannot determine coverage, decide a response, or make regulatory representations. Review the program periodically and after material fraud-pattern or service changes with human approval.


## Evidence and test plan

These three packages retain PR #340's useful evidence requests, with full in-scope
coverage. Earlier review does not approve this revised guide.

### 1. Covered-account and risk-assessment record

- **Request and owner:** Product/account inventory, customer and transaction channels, documented covered-account scope decisions, identity-theft risk assessment, accountable owner assignments, and approval/review records from business, compliance, fraud, and legal owners.
- **Validate and limit:** Trace each in-scope account product or channel to its scope rationale, risk record, owner, and approval/review date. This supports a bounded evidence trail; it cannot decide covered-account status, establish all risks were identified, or replace legal advice.
- **AI and trigger:** AI may compare approved inventories and flag missing owners, stale risk reviews, or inconsistent channel descriptions. Humans determine scope, risk tolerance, and legal applicability. Refresh after a new product/channel, material customer-identification change, acquisition, fraud-pattern shift, or legal/regulatory update.

### 2. Detection, response, and service-provider operations

- **Request and owner:** Red-flag identification/detection procedures, monitoring or case records, authentication/verification process evidence, response/escalation decisions, service-provider oversight records, incident records, and corrective-action tracking from fraud operations, security, customer operations, and supplier owners.
- **Validate and limit:** Trace each in-scope alert or case to the underlying signal, human investigation/decision, customer or provider action, escalation, and closure. This can demonstrate the reviewed operating trails; it cannot adjudicate identity theft, validate detection effectiveness, or decide notification obligations.
- **AI and trigger:** AI may organize authorized case metadata in its controlled location and flag missing handoffs, owners, or closure dates; it may not make a fraud decision, freeze an account, contact a customer, or alter a response workflow. Humans authorize interventions, investigations, communications, and remediation. Recollect after a material incident, failed response, vendor change, or detection-process change.

### 3. Program-update and management-challenge packet

- **Request and owner:** Periodic program review, training/awareness evidence, trend analysis, internal review/audit observations, exception register, management decisions, remediation evidence, and closure/retest records from compliance, fraud leadership, training, and independent-review owners.
- **Validate and limit:** Trace each in-scope finding or program update to its evidence, accountable decision, implementation owner, due date, and retest. This supports management transparency; it cannot approve a program, accept residual risk, or make a regulator-facing assertion.
- **AI and trigger:** AI may prepare factual trend summaries and challenge questions from approved records. Humans approve program updates, resources, risk acceptance, closure, and external statements. Review periodically and following a significant identity-theft event, fraud trend, product/service change, or review finding.


### Detection coverage and case reconciliation

For each approved pattern/channel pair, record the test or observation that can
show the pattern is detectable. A review of generated alerts alone cannot expose
warnings the detector never generated. Reconcile synthetic input events to output
signals, and output signals to delivered cases, before reviewing case dispositions.
Keep false alarms, expected non-alerts and missing alerts separate.

For the review period, reconcile provider totals and identifiers to local intake,
including rejects, retries and duplicate records. Counts alone cannot show that
the same cases arrived. Link each case to source identifiers, ownership, approved
decision and observed action. Investigate unmatched items rather than deleting
them from the denominator or assuming the provider handled them.

When correcting a missed warning, preserve the original scenario and repeat it
against the changed version. Recheck related approved negative cases to identify
new false alarms. Record observed behavior without claiming statistical detection
performance from a few synthetic examples. No test result authorizes action on a
real customer account.

## Cadence and renewal

Use the approved periodic review schedule and recheck after new products,
identification methods, channels, provider changes or fraud patterns. Link each
program revision to supporting evidence, the human decision and affected staff
training or procedures. Keep incident/case deadlines separate from the next
scheduled program review; do not invent a uniform statutory interval.

## Completion and handoff

Provide the complete scope and pattern/channel registers, program/source versions,
evidence index, test results, unmatched signals/cases, approved decisions,
remediation/retests and accountable owners. Distinguish documentation readiness,
observed operation and legal acceptance. A remaining routing or response gap must
stay visible even if all policies have been approved.

Independent source, skeptical, rights and publication reviews remain pending.
Neither structural checks nor fictional desk cases prove legal compliance,
detection effectiveness or consistent execution across AI models.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
