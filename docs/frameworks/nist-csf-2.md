# NIST Cybersecurity Framework 2.0 — engagement guide

> Original operational guidance for cybersecurity risk management. This guide
> does not provide a certification or establish conformance.

## Source and applicability

Use [NIST's CSF resource center](https://www.nist.gov/cyberframework) and
[organizational profile resources](https://www.nist.gov/cyberframework/profiles).
Checked 2026-09-04: the resource center identifies CSF 2.0; the profile resources
support comparison of Current and Target Profiles. Confirm the edition and
business scope in the charter before using a legacy profile. Consult
[NIST's FAQ](https://www.nist.gov/cyberframework/faqs) when transitioning from 1.1;
do not just relabel old identifiers.

Rights: original instructions and source links only; no imported mappings,
logos or outcome catalog. See [NIST's rights notice](https://www.nist.gov/copyrights-disclaimers).
Author source check is recorded in the [refresh record](../refresh-reviews/nist-csf-2.md).
Independent publication review remains pending.

## Engagement focus

Produce a defensible Current Profile, a separately approved Target Profile,
and a prioritized improvement queue for a defined organization or service.
Connect each current-state assertion to dated operating evidence. A target is an
intention; creating a policy or completing this guide does not achieve it.

## Roles

The executive risk owner approves priorities, target state and risk decisions.
Service/control owners supply and operate the practices. A reviewer who did not
produce the work challenges evidence and conclusions. AI may reconcile records,
perform authorized read-only checks, and draft profiles and findings. It cannot
accept risk, approve its own work, certify outcomes or change production without
the required action authority.

## Before starting

Obtain the approved charter; service and dependency inventory; business/risk
priorities; existing profiles with edition and scope; evidence custodians; and
reviewer. If these do not exist, draft requests and a proposed scope for the owner.
Do not select an organization's risk priorities by guessing from its industry.
Use the [agent runbook](../agent-runbook.md) for every work item.

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Fix the boundary | Risk and service owners identify the business units, services, dependencies and time period covered. AI reconciles inventory references and lists exclusions. | Approved boundary with an owner for every included service and rationale for exclusions. Unresolved scope blocks claims about the affected service. |
| 2. Establish the Current Profile | AI assembles source-linked assertions for the selected outcomes; control owners provide actual operating records. Preserve contradictions and unknowns. | Current Profile rows link to evidence, period and result. A plan or policy alone is not recorded as demonstrated operation. |
| 3. Establish the Target Profile | AI drafts possible priorities from approved business objectives and known gaps; the risk owner decides the desired outcomes and priority. | Approved Target Profile with rationale, dependencies and decision date. Keep unapproved proposals visibly draft. |
| 4. Plan the gap work | Compare Current and Target rows within the same boundary/edition. Owners assign corrective work, resources, due dates and expected evidence. | Each gap has an accountable owner, acceptance check and dependencies; unknown current state first gets an evidence task. |
| 5. Test the assertions | The independent reviewer approves checks and coverage. AI may execute permitted observations; retain raw results and adverse evidence. | Workpapers trace selected assertions to actual service behavior and state the population/period limitations. |
| 6. Resolve and retest | Operators implement approved corrections. The reviewer verifies new evidence against the original acceptance check; the risk owner decides residual risk. | Finding history, retest receipt and authorized disposition. A merged change or closed ticket alone is insufficient. |
| 7. Maintain the profiles | The program owner reviews changes and refreshes affected assertions. AI creates evidence-refresh tasks and preserves previous profile versions. | Reviewed profile revision, remaining gaps, next review and source-change owner. |

Steps 2 and 3 may be developed iteratively; compare them only after both use an
agreed boundary. These are this playbook's execution steps, not a prescribed
NIST audit sequence.

## Evidence and test plan

| Request and custodian | Check | Expected observation | Failure or limit |
| --- | --- | --- | --- |
| Service/dependency inventory from service owners | Trace each scoped service to an owner and linked profile rows; reconcile omitted services. | No unexplained scope omission or owner gap. | A missing inventory leaves completeness inconclusive. |
| Current Profile and operational records from control owners | For reviewer-selected assertions, compare the asserted practice with dated configuration, event, access or exercise evidence. | Evidence addresses the same service, assertion and period. | A stale screenshot or future procedure cannot support current operation. |
| Target Profile and risk decisions from the risk owner | Trace each prioritized gap to a business objective and approved decision. | Priorities and dependencies have an accountable rationale. | AI-generated rankings remain recommendations. |
| Remediation/measurement records from the program owner | Reperform the approved measure and follow a corrected gap through retest. | Calculations reconcile and closure has observed evidence. | Metrics do not prove all outcomes or continuous effectiveness. |

## Failure branches and decisions

If a community profile is used, record why it fits and what the owner changed;
do not infer the organization has achieved its contents. If 1.1 and 2.0 records
are mixed, preserve their identifiers and request a reviewed transition plan.
A mapping to another framework is a research aid, not proof of equivalence.
Classify missing evidence as `inconclusive`; do not convert it to an exclusion
or average it into a favorable score. Use the runbook's result vocabulary.

## Cadence and renewal

The owner sets cadence based on risk; a quarterly gap/evidence review and annual
scope/target review are planning defaults, not NIST deadlines. Reopen affected
rows after incidents, material service/supplier changes, changed objectives or
source revisions. Preserve event-triggered work even if the next routine review
is months away.

## Completion and handoff

Deliver the approved boundary, versioned Current/Target Profiles, evidence index,
review workpapers, unresolved gaps and risk decisions, retest records, and next
review queue. State precisely which assertions were tested and which remain
unknown. Human-reviewed readiness work does not confer certification.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md).
