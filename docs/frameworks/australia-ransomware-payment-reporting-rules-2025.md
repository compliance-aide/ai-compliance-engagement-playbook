# Australia ransomware-payment reporting — engagement guide

> Original operational guidance for reporting readiness, not legal advice, incident direction,
> payment approval or authority to submit a government report.

## Source and applicability

Use the [Rules register](https://www.legislation.gov.au/F2025L00278/asmade/versions)
and its linked Cyber Security Act 2024. Checked 2026-09-04: F2025L00278 is listed
in force. Rules sections 5–7 address scope, turnover and report information.
The ordinary threshold is $3 million, with a part-year calculation; responsible
entities for relevant Part 2B critical infrastructure have a separate scope route.

[ASD reporting guidance](https://www.cyber.gov.au/report-and-recover/recover-from/ransomware)
identifies a 72-hour payment/awareness reporting window. Keep incident occurrence,
incident awareness, payment and awareness of payment on the entity's behalf as
separate timestamps; counsel confirms the actual legal trigger and deadline.

Source conflict: the Rules' outline uses turnover exceeding the threshold, while
[Home Affairs form guidance](https://www.homeaffairs.gov.au/cyber-security-subsite/files/how-to-make-a-report-ransomware-payment-reporting.pdf)
includes equality. Escalate boundary cases to counsel against the governing Act;
do not silently automate either interpretation. The Rules allow information known
or reasonably discoverable within the reporting period: complete forensics must
not become a prerequisite to timely report preparation.
See the [author record](../refresh-reviews/australia-ransomware-payment-reporting-rules-2025.md).

## Engagement focus

Prepare an accurate, timely reporting packet and a tested route to its authorised
submitter. This is separate from incident response, payment decisions, insurer
coordination and other notification duties. No payment is recommended or enabled
by preparing a report.

## Roles

Incident command owns response and facts; finance supplies payment/turnover records;
legal decides applicability, clock and reporting interpretation. Executives retain
payment decisions; the authorised submitter owns report approval and transmission.
Records protects evidence; independent reviewers challenge workpapers. AI may
organise authorised facts and calculate dates from approved rules, but cannot
negotiate, pay, direct containment, approve legal conclusions or submit unauthorised
communications.

## Before starting

For readiness work obtain scope assumptions, current sources, incident contacts,
delegations, approved clock rules, secure evidence location and fictional cases.
For a real event escalate immediately to incident command/legal using the approved
route while preserving permitted facts. Do not wait for this checklist to finish.
Follow the [agent runbook](../agent-runbook.md).

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Resolve readiness scope | Legal/finance establish entity, period, turnover and critical-infrastructure facts. | Source-backed scope record with any threshold conflict unresolved explicitly. |
| 2. Establish event timeline | Incident command/finance validate separate incident, demand, payment and awareness records. | Facts carry provenance, timezone, uncertainty and accountable owner. |
| 3. Assign the clock | Legal approves applicable trigger/due time; AI calculates from that rule and flags approaching deadlines. | Reviewed clock record; missing facts escalate urgently rather than disabling alerts. |
| 4. Assemble report facts | AI indexes approved entity, incident, demand, payment and communication records against required fields. | Draft distinguishes known, estimated, unknown and reasonable enquiries performed. |
| 5. Review under the clock | Legal/incident/finance owners check scope, factual consistency and authorised disclosure. | Exact draft and named submitter; unresolved details remain visible without waiting for final forensics. |
| 6. Submit when authorised | Designated operator uses the approved reporting route and records receipt. | Submitted artifact/version and acknowledgment match; a filled form is not delivery. |
| 7. Reconcile and improve | Owners review later facts and any follow-up obligations; readiness lead corrects process gaps and retests. | Owned follow-up queue, protected record and observed remediation. |

## Evidence and test plan

| Evidence and custodian | Check | Expected observation | Failure or limit |
| --- | --- | --- | --- |
| Scope record, legal/finance | Trace entity, financial period and infrastructure status to evidence. | Scope rationale covers the correct entity and any part-year case. | Group assumptions cannot replace entity analysis. |
| Event timeline, incident command | Exercise direct-payment and third-party-awareness fictional cases. | Distinct timestamps drive the approved clock correctly. | Incident detection alone is not an interchangeable payment trigger. |
| Draft/fact register, records | Reconcile report assertions and unknown fields to source records/enquiries. | No invented malware attribution or payment details. | Unknown fields do not justify indefinitely delaying the packet. |
| QA reporting exercise, readiness lead | Simulate review and receipt handling without submitting a real report. | Owner can distinguish prepared, approved, submitted and acknowledged states. | A tabletop does not prove real portal availability or delivery. |

## Failure branches and decisions

Unclear payment status, contradictory timestamps or turnover boundaries go promptly
to legal/incident command; retain both accounts. A portal failure requires immediate
submitter escalation and an approved alternate-route decision, not a success label.
After interruption, inspect existing receipts before any retry. Preserve complete
authorised evidence in protected storage; no extortion communications or private
incident data belong in this public repository. Other legal clocks run separately.

## Cadence and renewal

Monitor an active event against its approved clock; quarterly readiness checks and
annual fictional exercises are planning defaults. Renew after entity, supplier,
insurer, contact, delegation or legal changes. Record failed exercises and retest
before claiming the affected readiness gap is closed.

## Completion and handoff

Deliver scope and clock decisions, protected fact/evidence register, reviewed draft,
actual receipt where authorised, uncertainties and follow-up queue. Independent
source/legal, engagement and skeptical review and named human publication approval
remain pending. This guide uses original prose and links, not reproduced law.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md).
