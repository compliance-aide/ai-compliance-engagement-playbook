# Australia Essential Eight — engagement guide

> Original operational guidance for assessment preparation, not an ASD maturity
> result or certification.

## Source and applicability

Use the [ASD Essential Eight maturity model](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight/essential-eight-maturity-model).
Checked 2026-09-04: the page identifies the November 2023 model. ASD describes
an internet-connected IT focus, complementary implementation across the eight
strategies, risk-based exceptions and additional safeguards where needed. Do not
assume the model covers operational technology or mobility environments without
an appropriate scope decision. The source does not impose universal independent
certification; a directive, regulator or contract may require assessment.

Rights: original workflow and source link, no model table, requirements or tests
reproduced. See the [author review](../refresh-reviews/australia-essential-eight.md).
Independent source/engagement review and publication approval remain pending.

## Engagement focus

Create a population-aware evidence plan across all eight strategies for the
approved target and environment. Identify uneven implementation, unsupported
exceptions and missing observations without manufacturing a single favorable
score. The authorized assessor determines any formal result under the applicable
method; this guide organizes the work supporting that decision.

## Roles

Leadership chooses target and risk treatment. Endpoint, identity, application and
recovery owners operate the safeguards. Independent reviewers approve methods and
challenge evidence. AI may reconcile inventories, organize results and draft gap
tasks. It cannot choose the target, grant exceptions, approve its own assessment,
change production without authority or claim maturity.

## Before starting

Obtain the charter, pinned model version, approved target, system/user inventory,
strategy owners, existing evidence, exception register, required assessment route
and authorized test setting. If a directive/contract requires a particular scope
or method, record it. Use the [agent runbook](../agent-runbook.md).

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Fix scope and target | Leadership/security owners approve the environment, target and applicable external assessment obligations. | Scope and target decision with explicit boundaries; no automatic highest-level selection. |
| 2. Build strategy/population map | Owners identify relevant devices, applications, users, administrative accounts and recovery assets for each strategy. AI reconciles expected populations. | Eight-strategy work map with owners and missing population records. |
| 3. Plan implementation and evidence | Owners compare approved expectations with current practices; reviewer defines permissible observations, period and selection. | Prioritized gap and evidence queue that exposes uneven coverage rather than averaging it away. |
| 4. Collect and observe | Authorized operators supply configuration, operation and recovery-test records; AI preserves complete evidence/reference coverage. | Dated records match the declared population and method; unavailable areas remain inconclusive. |
| 5. Challenge exceptions and adverse cases | Reviewer examines approved deviations, compensating measures, expiry and actual behavior. | Exception workpapers distinguish management approval from assessment acceptability. |
| 6. Correct and retest | Operators apply authorized improvements; reviewer checks affected populations and failure paths again. | Observed retest, still-open gaps and decision references. A deployment policy alone is not demonstrated implementation. |
| 7. Prepare the assessment handoff | Security lead assembles coverage and limitations; authorized assessor determines the result, if requested. | Evidence packet, explicit unresolved gaps and next change/review triggers; no AI maturity award. |

This is an original execution plan, not a reproduction of ASD's model or an
alternative scoring algorithm.

## Evidence and test plan

| Request and custodian | Check | Expected observation | Failure or limit |
| --- | --- | --- | --- |
| Population/strategy map from technology/security | Reconcile inventory totals, strategy scope and evidence coverage. | Unmanaged assets and unknown coverage remain visible. | A few configured devices do not prove fleet-wide implementation. |
| Endpoint/application/identity records from operators | Observe approved checks on the stated population and compare actual behavior with the chosen method. | Configuration and operating evidence agree for the period. | A management-console setting alone does not prove enforcement everywhere. |
| Recovery records from backup owners | Trace approved QA recovery to restored data/service and recorded limitations. | Recovery behavior is actually observed. | A successful backup job does not establish recoverability. |
| Exception/remediation records from security and risk | Trace deviation to scope, approval, compensating evidence, expiry and retest. | Decisions and behavior are both evidenced. | Risk acceptance does not automatically establish the assessor's maturity result. |

## Failure branches and decisions

If asset counts differ, reconcile them before describing coverage. Missing
telemetry or failed tools yield `inconclusive` or `not_tested`, not a pass. Do not
use a high result for one strategy to hide another's gaps. Keep operational
technology outside an unsupported IT conclusion. A required independent assessment
must follow its own authority/method; do not invent an ASD approval requirement
for every engagement. Restrict recovery exercises to the approved setting.

## Cadence and renewal

Set collection/test frequency from the approved model interpretation and actual
risk/contract needs. Quarterly evidence reviews and annual target review are
planning defaults, not universal ASD certification intervals. Reassess after
identity, endpoint, application, recovery, model-version or material threat
changes. Recheck expired exceptions before repeating a maturity representation.

## Completion and handoff

Deliver the approved scope/target, eight-strategy population map, evidence/test
receipts, exceptions, remediation/retests and assessment authority/next queue.
State gaps and untested populations plainly. Evidence organization does not
establish an overall maturity level or protection from every threat.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md).
