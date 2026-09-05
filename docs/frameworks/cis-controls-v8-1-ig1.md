# CIS Controls v8.1 Implementation Group 1 engagement guide

> Original operational guidance, not CIS Controls text, a safeguard selection, a security decision, or a compliance claim. Confirm current material through CIS’s [Implementation Group 1 resource](https://www.cisecurity.org/controls/implementation-groups/ig1).

## Engagement focus

Maintain a right-sized foundational-security engagement record that connects enterprise scope, accountable business and technology owners, asset and service evidence, prioritized improvement decisions, exceptions, remediation, operating evidence, and independent review. Center the annual rhythm on practical evidence of operating security while preventing a generated summary from being mistaken for a control assessment or implementation approval.

## Source and applicability

Source check: 2026-09-04. CIS identifies IG1 as a foundational group of 56 safeguards within Controls v8/v8.1. Use the official IG1 resource and [v8.1 record](https://www.cisecurity.org/controls/v8-1), with authorized source material. Record why the organization selected this scope; IG1 is not a certification or a guarantee that all business risks are addressed. Do not confuse implementation groups with CIS Benchmark configuration profiles.

## Roles

Leadership approves scope, priorities and resources. IT/security owners implement through separately authorized changes. Service owners provide actual populations and dependencies. Reviewers judge evidence and findings. Source owners confirm permitted use. AI reconciles metadata and drafts questions; it cannot choose the final group, accept risk, initiate scans, approve changes or make compliance claims.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Name the organization, services, period, version, owner, inputs, output and exit check. Require approved group selection, asset/service scope, evidence permissions and source rights. Record missing inputs. Keep licensed safeguard text and private evidence outside this public repository.

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Establish scope | Business/IT owners reconcile services, users, assets and suppliers against actual operations. | Approved population and discrepancies; small organization size does not justify omitting dependencies. |
| 2. Plan full coverage | Security owner accounts for the complete authorized IG1 set using permitted references and assigns owner, evidence and assessment method to each. | Coverage register reconciled to selected version; unavailable evidence is not satisfied or automatically excluded. |
| 3. Sequence work | Owners identify prerequisites and propose practical implementation batches, with resources and approvals. | Prioritized plan retaining all open items; sequencing does not shrink scope. |
| 4. Establish observations | Reviewers compare approved expectations with dated operating records across the defined populations. | Workpapers recording actual behavior, failures and untested coverage. Policy documents alone do not prove operation. |
| 5. Implement and retest | Authorized implementers make approved changes; reviewers check affected requirements and service functionality. | Finding/change/retest trail; planned fixes and closed tickets are not verified results. |
| 6. Decide exceptions | Leadership/risk owners review remaining gaps, mitigation, resources and review dates. | Recorded decisions with scope and conditions; risk acceptance does not convert failure into pass. |
| 7. Sustain | Owners monitor recurring operation and changes; reopen affected scope and evidence. | Owned review queue and current evidence, without fabricated certification. |

## Evidence and test plan

These original examples support the complete coverage register; they are not a substitute safeguard list. Preserve the full evidence corpus and never trim evidence supplied to a scorer.

| Package and owner | Verification | Limitation |
| --- | --- | --- |
| Scope — business/IT | Trace a service through owner, assets, users and suppliers; reconcile inventory discrepancies. | One trace cannot prove complete inventory. |
| Identity/administration — IT | Follow an approved personnel change through actual account and access records. | Written offboarding rules do not prove access was removed. |
| Maintenance — operators | Trace a tracked weakness or update through affected population, approved action and retest. | A successful job may leave failed or unreachable assets. |
| Recovery — service owner | Compare authorized QA recovery evidence with the service's approved objective. | Backup completion alone does not prove restoration or real-event readiness. |
| Awareness/events — security | Link a training or security-event record to owner action, coverage and follow-up. | Attendance or an empty alert list is not proof of effective behavior. |
| Improvements — reviewer | Trace deferred work to its decision, owner, due date and later verification. | Exception approval is not implementation evidence. |

Record source, collector, date, period, population, expected/observed result, evidence pointer, limitation, reviewer and next action. State selected test populations and untested coverage. Use authorized QA or retained evidence; this guide does not authorize production changes or live scans.

## Failure branches and decisions

- **Missing population or owner:** record the gap and reconcile the source inventory before claiming coverage.
- **Wrong version or unsupported exclusion:** obtain the source/scope decision; do not silently substitute another set.
- **Failed or unavailable observation:** preserve the state and affected population; never count an unassessed asset as passed.
- **Implementation breaks service:** stop further rollout and route recovery to the authorized change owner.
- **Overdue action or expired exception:** escalate to the decision owner without automatic extension.
- **Risk outgrows IG1 scope:** prepare the changed-risk facts for leadership's group/scope decision; do not discard existing foundational work.
- **Interrupted work:** preserve last completed step, versions and pending approvals; verify target or job status before retrying.

## Cadence and renewal

Use applicable safeguard frequencies from authorized source material and approved operating schedules. Quarterly evidence review and annual scope review are internal practices, not replacements for more frequent applicable activities. Reassess after material asset, service, workforce, supplier, incident or threat changes.

## Completion and handoff

The review packet contains approved scope/version, complete safeguard dispositions, operating evidence, open gaps, retests and decisions. Mark omissions. Handoff identifies next action, owner, due date and dependency. A readiness packet is not a certification or authorization to operate.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared applicability, authority, evidence, technical-test, exception, source-change and renewal requirements.
