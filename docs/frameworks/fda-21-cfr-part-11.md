# FDA 21 CFR Part 11 — engagement guide

> Original operational guidance, not legal advice or an FDA conclusion. Consult [FDA Part 11 guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application).

## Engagement focus

Maintain predicate-record reliance, systems, owners, suppliers, lifecycle changes, signature events, training, incidents, exceptions, and immutable evidence pointers.

## Record and signature verification sequence

Use the [agent runbook](../agent-runbook.md). Source checkpoint, 2026-09-04:
official FDA scope-guidance indexed text connects Part 11 to applicable record
requirements and electronic reliance. Full current Part 11, predicate rules,
relevant enforcement-discretion guidance and sector-specific guidance remain to
be reviewed. Do not interpret a guidance excerpt as a blanket exemption or infer
scope simply because software is used in a regulated organization.

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

**Failure branches:** missing predicate mapping leaves scope `inconclusive`.
An unavailable archive reader makes retrieval `not_tested`. A copy that omits
required signature context is `not_supported` for the approved copy criterion,
regardless of whether the PDF opens successfully.

**Fictional desk case:** a QA report exports all measured values but drops which
record version the review signature applies to. File readability is `supported`;
signature-context preservation is `not_supported` against the approved criterion.
Adding a visible signature image without verifying the underlying linkage does
not resolve the failure. No actual regulated record or signature was created.

## Roles and annual rhythm

Quality/legal humans decide scope and submissions; independent reviewers use read-only evidence. AI creates worklists, but cannot decide exceptions, create regulated records, or make filings. Review quarterly and annually.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
