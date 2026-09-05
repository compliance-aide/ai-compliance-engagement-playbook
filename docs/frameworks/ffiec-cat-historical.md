# FFIEC Cybersecurity Assessment Tool — historical migration guide

> Original operational guidance for legacy records only. The [FFIEC sunset notice](https://www.ffiec.gov/cyberassessmenttool.htm) announced the voluntary tool’s August 31, 2025 sunset; do not use it as a current framework.

## Engagement focus

Inventory legacy artifacts, preserve retention-required records, identify lingering references, and move active governance and evidence to a currently authorized approach. Make migration decisions explicit, dated, owned, and independently challengeable.

## Source and applicability

The [official sunset statement](https://www.ffiec.gov/sites/default/files/media/press-releases/2024/cat-sunset-statement-ffiec-letterhead.pdf) announced August 31, 2025 as the CAT sunset date. Official indexed material checked 2026-09-04 also states that FFIEC does not endorse a particular tool and that assessment tools are not examination programs. Verify current supervisory communications and the institution's approved successor approach. A reference to NIST, CISA or another resource is not evidence of a mandated replacement or an automatic equivalence.

## Roles

Records owners preserve historical artifacts and custody. Risk and compliance owners select the successor approach and approve applicability. System and policy owners implement migration changes. Independent reviewers challenge coverage and closure. AI inventories authorized metadata and drafts mappings; it cannot approve disposal, accept risk, certify an institution or represent a regulator. Humans retain those decisions.

## Before starting

Record institution, business scope, legacy assessment periods, repositories, approved evidence access and responsible owners. Obtain retention and legal-hold decisions before changing historical material. Define the successor source/version and approval record; if none exists, keep selection awaiting the risk owner while continuing inventory work. Use the [agent runbook](../agent-runbook.md) to record inputs, expected results and next actions.

## Ordered workflow

1. **Preserve the historical baseline.** Inventory all legacy assessments, evidence indexes, approvals, findings and working files. Record version, date, custodian, access boundary and retention status. Keep originals intact; relabeling a historical assessment as current would change its meaning.
2. **Find active dependencies on CAT.** Review the full authorized policy, dashboard, questionnaire, training, contract and reporting populations. Use searches as discovery aids and reconcile against the repository inventory, including unsearchable files and failed access. Output a reference register; zero keyword hits do not prove complete discovery.
3. **Classify each reference by use.** Separate historical quotations, live decision rules, contractual language, recurring jobs and public claims. Assign an owner and action to each. Historical references may remain with clear dates; an active claim needs separate review. Do not edit executed contracts as if they were ordinary templates.
4. **Approve the successor scope.** Link the institution's decision to the current source, version, risk context and accountable owner. Record gaps and exceptions. Output an approved transition boundary; do not select a replacement merely because a vendor offers a conversion tool.
5. **Map evidence without inheriting conclusions.** For every successor assertion, identify relevant prior evidence, scope/time limitations and fresh observations needed. Preserve partial and absent mappings. A renamed CAT score does not establish successor achievement; reassess the actual criterion against evidence.
6. **Update the active workflow.** Prepare revised instructions, dashboards, evidence requests and scheduled jobs. Owners approve changes and verify the artifact used by operators. Keep draft, deployed and observed behavior separate; editing a source document does not prove an automated report stopped using CAT.
7. **Reconcile findings and close migration gaps.** Transfer every open legacy finding to an owned successor action or documented disposition. Preserve adverse facts and original deadlines. Retest changed workflows and collect readback. Output a closure packet with unresolved items, not a blanket certification.

## Evidence and test plan

### Legacy records and retention package

Records, security and compliance owners provide the complete artifact inventory, custodians, authorized locations, assessment dates, retention decisions, legal holds and access restrictions. Reconcile the inventory with the repositories in scope, including inaccessible folders and unreadable formats. Keep missing items visible; a copied directory does not establish that linked evidence was preserved.

For each moved artifact, verify destination readability, identity and associated evidence links. A matching file hash supports byte preservation, not completeness of the original assessment. Keep historical approvals attached to their original assessment versions. Human records/legal owners resolve retention and disposal questions; do not infer a new retention period from the sunset date.

### Active references and remediation package

Policy, vendor, reporting and technology owners provide the complete population of policies, questionnaires, templates, jobs, dashboards, training and contracts in scope. Record each reference's actual use, owner, required change, approval and observed result. Preserve legitimate historical references with clear dates rather than treating every occurrence as a defect.

For an automated report, identify the scheduler, actual input path, transformation and recipient-facing output. In an authorized test environment, observe the revised run and confirm its displayed framework/version and evidence basis. A changed template is insufficient if the job still reads another copy. Record skipped or failed jobs separately from successful runs. Do not send test reports to real recipients or delete historical source files to make a migration test pass.

### Successor governance and independent challenge package

Risk, compliance and successor-framework owners provide the selection decision, current source/version, applicability rationale, migration milestones, evidence mapping and unresolved findings. Reconcile all successor assertions and all legacy open findings. Mark one-to-many mappings, unsupported mappings and evidence outside the relevant period explicitly; matching titles do not prove equivalent criteria.

For each migration claim, distinguish transferred evidence, newly collected evidence, criterion evaluation and approval. Preserve original adverse findings even when their identifiers change. Require an owner-approved disposition for findings that do not map directly; absence from the successor checklist does not resolve the underlying risk. Independent reviewers challenge both evidence coverage and the claim that the new workflow operates as described.

## Failure branches and decisions

Use `not_tested` for inaccessible repositories or unobserved workflow behavior; use `inconclusive` for unresolved successor applicability or conflicting evidence. A live dashboard demonstrably claiming current CAT maturity contradicts an approved removal criterion and is `not_supported`, even if other references were fixed. Separate successful historical preservation from unsuccessful migration.

Fictional desk case: the policy is updated, but the next scheduled report still reads an old CAT workbook and publishes its score as current. Policy revision is `supported`; operational migration is `not_supported`. The agent records the specific job, input and output for the owner, preserves the old assessment and does not convert its score into a successor rating.

## Cadence and renewal

Set migration checkpoints and subsequent reviews with named owners from approved institutional policy and current sources. Recheck after repository moves, hold notices, reporting changes, new questionnaires and supervisory changes. Sunset does not itself authorize deletion or cancel an existing finding. There is no CAT renewal to perform under this historical guide.

## Completion and handoff

Deliver the preserved legacy inventory, retention/hold decisions, complete active-reference register, successor approval and source record, assertion-to-evidence mapping, open-finding reconciliation and observed workflow results. Assign each unresolved item a next owner and due date. Keep unavailable repositories and unobserved jobs visible in the completion decision.

Separate archive preservation, active-reference cleanup and successor assessment readiness: completion of one does not establish the others. Require independent source, skeptical and rights review before publication. Human owners approve disposal, risk acceptance and external statements; no institution or regulator acceptance has been established by this draft.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
