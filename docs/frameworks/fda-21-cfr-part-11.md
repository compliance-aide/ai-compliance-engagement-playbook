# FDA 21 CFR Part 11 — engagement guide

> Original operational guidance, not legal advice or an FDA conclusion. Consult [FDA Part 11 guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application).

## Source and applicability

Use the [agent runbook](../agent-runbook.md). Source checkpoint, 2026-09-04:
official FDA scope-guidance indexed text connects Part 11 to applicable record
requirements and electronic reliance. Full current Part 11, predicate rules,
relevant enforcement-discretion guidance and sector-specific guidance remain to
be reviewed. Do not interpret a guidance excerpt as a blanket exemption or infer
scope simply because software is used in a regulated organization.


Use the [current regulatory text](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11)
with the applicable predicate rules and approved intended use. Keep guidance,
regulatory requirements and internal recommendations identified separately.

## Engagement focus

Maintain predicate-record reliance, systems, owners, suppliers, lifecycle changes, signature events, training, incidents, exceptions, and immutable evidence pointers.

## Before starting

Define the record/process population, system versions, review period, predicate
mapping owner, approved test criteria and evidence permissions. Create
[work items](../../templates/work-item.md) for separate scope, behavior, signature
and copy assertions. Use synthetic data in QA-named environments; retain regulated
records and confidential validation material only in approved repositories.

Have quality approve the test environment's representativeness and limitations.
Document which production features it reproduces and which conclusions cannot
transfer. Never silently treat a simplified demonstration as validation evidence
for a different configuration.

## Ordered workflow


1. Inventory each record category, required purpose, predicate source, owner,
   retention decision and actual electronic/paper reliance. Quality/legal approves
   scope. A paper printout does not by itself establish that the electronic
   source is irrelevant to regulated decisions.
2. Trace the record lifecycle across creation, calculation, correction, review,
   signature, export, archive and retrieval. Link system/version, interfaces and
   responsible roles. Include metadata and relationships needed to interpret the
   record, not merely the final report file.
3. Define approved assertions for the intended use: identity, permitted actions,
   record changes, signature meaning/linkage, readable copies and retrieval.
   Separate what a system supports from what the configured workflow actually
   does. A vendor's Part 11 marketing statement is not validation of local use.
4. Prepare synthetic QA records and approved tests with expected results. Do not
   create or sign real regulated records during guide development. Capture the
   exact configuration, role, input, observation and evidence location.
5. Exercise authorized creation, review and correction paths. Preserve original
   and changed values and their context where required by approved criteria.
   Test denied actions independently of successful actions; a successful reviewer
   login does not prove an unauthorized user cannot alter the record.
6. Trace a synthetic signature to the correct record/version and approved meaning.
   Check the intended readable representation and underlying linkage separately.
   An image of a signature or a “signed” label cannot alone prove identity or
   that the signature is bound to the record being reviewed.
7. Export and retrieve the synthetic record through the intended inspection or
   archive path. Compare identifiers, values, units, metadata, history and signature
   context against the approved completeness criterion. Matching page counts or
   a file hash proves neither preserved meaning nor inclusion of required context.
8. Log deviations with affected record/system scope, owner and proposed correction.
   Retest approved changes while preserving original failures. Have quality decide
   acceptance; an agent cannot close a validation deviation or approve submission.

## Failure branches and decisions

 missing predicate mapping leaves scope `inconclusive`.
An unavailable archive reader makes retrieval `not_tested`. A copy that omits
required signature context is `not_supported` for the approved copy criterion,
regardless of whether the PDF opens successfully.

**Fictional desk case:** a QA report exports all measured values but drops which
record version the review signature applies to. File readability is `supported`;
signature-context preservation is `not_supported` against the approved criterion.
Adding a visible signature image without verifying the underlying linkage does
not resolve the failure. No actual regulated record or signature was created.

## Roles

Quality/legal humans decide scope and submissions; independent reviewers use read-only evidence. AI creates worklists, but cannot decide exceptions, create regulated records, or make filings. Use the approved review schedule and change triggers below.


## Evidence and test plan

These three packages retain PR #340's useful requests with full in-scope coverage.
Prior review does not approve this revision. Preserve all scoped scoring evidence.

### 1. Predicate-record, system, and intended-use evidence

- **Request and owner:** Quality, regulatory, and system owners provide predicate-record rationale, intended-use records, system inventory, data-flow and interface records, supplier roles, accountable owners, and lifecycle-change approvals.
- **Validate and limit:** Trace each in-scope electronic record process to its approved intended-use or predicate rationale, system boundary, owner, and change history. This supports a factual trace and cannot decide legal scope or validate the system.
- **AI and trigger:** AI may organize approved inventories and flag changes to systems, interfaces, or record types. Quality and regulatory humans determine applicability and intended use. Refresh before use of a new record process and after material change.

### 2. Lifecycle, access, and electronic-signature evidence

- **Request and owner:** Quality, IT, and process owners provide lifecycle/validation references, configuration and change records, access-role records, training records, signature issuance/administration records, audit-trail availability evidence, and exception logs.
- **Validate and limit:** Trace each in-scope record workflow to owner, dated source artifact, change or access context, stated limitation, and corrective action. This can identify evidence gaps; it cannot certify validation, determine signature equivalence, or create/approve a regulated record.
- **AI and trigger:** AI may prepare redacted worklists and flag missing provenance or stale access reviews. Humans perform controlled review, approve changes, and decide exceptions. Refresh on system release, role change, audit-trail issue, or signature-process change.

### 3. Quality review, supplier, and incident evidence

- **Request and owner:** Quality leadership, supplier-management, and system owners provide periodic review records, supplier/service oversight records, incidents and investigations, CAPA records, risk decisions, and management-review minutes.
- **Validate and limit:** Trace each in-scope incident, supplier, or CAPA record to its source, owner, impact assessment record, action, approval, and closure or re-review. This does not determine reportability, accept quality risk, or make an FDA filing.
- **AI and trigger:** AI may flag overdue CAPAs, supplier reviews, and unresolved evidence gaps. Authorized quality and regulatory humans decide reportability, risk acceptance, and external communication. Review at the approved cadence and after significant incidents, supplier changes, or lifecycle changes.

### Signature and archive challenge checks

Use the approved QA protocol to distinguish authorization to sign, the signing
act, the record/version signed and the meaning displayed to a reviewer. Record
what happens after an authorized record correction: the owner must define the
expected signature/history behavior before the test. Do not make a later version
appear reviewed merely by carrying forward an earlier display label.

For archive or migration tests, reconcile the complete approved record population
and its required context to the destination. Test retrieval through the intended
reader after the original application is unavailable in the approved scenario.
Preserve dependencies on software versions, keys, metadata and external links;
a backup file that exists but cannot be interpreted is not a successful retrieval.

Inspect copies for the approved required content and relationships, not only
visual similarity. A hash can compare fixed bytes to a reference, but cannot
establish that the chosen reference contained every required record or context.
Keep population completeness and byte integrity as separate assertions.

Link deviations to each affected record type and system configuration. Record
correction, approved retest and quality disposition independently. A supplier
patch or a closed CAPA ticket does not prove the original behavior was corrected
in the scoped environment.

## Cadence and renewal

Reassess after new record types, changed intended use, software/configuration
changes, signature administration changes, incidents or supplier changes. Follow
the quality-approved schedule and applicable record obligations; do not invent
universal quarterly/annual Part 11 requirements. Confirm retrieval arrangements
before retiring a dependency needed to interpret retained records.

## Completion and handoff

Deliver the complete predicate/record map, intended-use and configuration baseline,
evidence index, test observations, signature/copy checks, deviations, retests and
named quality dispositions. State the limitations of the environment and sources.
Keep missing retrieval evidence and unresolved predicate questions visible with
owners and next actions.

Describe the result as the approved engagement type, not FDA certification or
acceptance. Independent source, skeptical, rights, publication and cross-model
reviews remain pending. Structural checks do not validate systems or establish
legal adequacy of electronic records and signatures.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
