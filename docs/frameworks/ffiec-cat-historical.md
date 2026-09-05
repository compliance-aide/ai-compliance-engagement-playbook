# FFIEC Cybersecurity Assessment Tool — historical migration guide

> Original operational guidance for legacy records only. The [FFIEC sunset notice](https://www.ffiec.gov/cyberassessmenttool.htm) announced the voluntary tool’s August 31, 2025 sunset; do not use it as a current framework.

## Engagement focus

Inventory legacy artifacts, preserve retention-required records, identify lingering references, and move active governance and evidence to a currently authorized approach. Make migration decisions explicit, dated, owned, and independently challengeable.

## Source and applicability

The [official sunset statement](https://www.ffiec.gov/sites/default/files/media/press-releases/2024/cat-sunset-statement-ffiec-letterhead.pdf) announced August 31, 2025 as the CAT sunset date. Official indexed material checked 2026-09-04 also states that FFIEC does not endorse a particular tool and that assessment tools are not examination programs. Verify current supervisory communications and the institution's approved successor approach. A reference to NIST, CISA or another resource is not evidence of a mandated replacement or an automatic equivalence.

## Roles

Records owners preserve historical artifacts and custody. Risk and compliance owners select the successor approach and approve applicability. System and policy owners implement migration changes. Independent reviewers challenge coverage and closure. AI inventories authorized metadata and drafts mappings; humans retain retention, disposal, risk and regulator-facing decisions.

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

## Failure branches and decisions

Use `not_tested` for inaccessible repositories or unobserved workflow behavior; use `inconclusive` for unresolved successor applicability or conflicting evidence. A live dashboard demonstrably claiming current CAT maturity contradicts an approved removal criterion and is `not_supported`, even if other references were fixed. Separate successful historical preservation from unsuccessful migration.

Fictional desk case: the policy is updated, but the next scheduled report still reads an old CAT workbook and publishes its score as current. Policy revision is `supported`; operational migration is `not_supported`. The agent records the specific job, input and output for the owner, preserves the old assessment and does not convert its score into a successor rating.

## Cadence and renewal

Set migration checkpoints and subsequent reviews with named owners from approved institutional policy and current sources. Recheck after repository moves, hold notices, reporting changes, new questionnaires and supervisory changes. Sunset does not itself authorize deletion or cancel an existing finding. There is no CAT renewal to perform under this historical guide.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
