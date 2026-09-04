# BSI Standard 200-2 — IT-Grundschutz methodology guide

> Original operational guidance, not BSI methodology text or a certification result.

## Source and applicability

Use the [official BSI 200-2 publication](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Grundschutz/International/bsi-standard-2002_en_pdf.pdf?__blob=publicationFile&v=2).
Checked 2026-09-04: indexed official material identifies methodology version 1.0
and describes Core Protection as focused on critical assets, with structural
analysis, protection needs, modelling, checks and additional risk treatment.
Direct retrieval returned 403; full source and current-edition verification remain
pending. Obtain the applicable methodology and Compendium editions before detailed
requirement mapping. See the [author record](../refresh-reviews/bsi-standard-200-2.md).

Record the selected approach and its actual boundary. A focused critical-asset
engagement cannot establish protection of the entire organisation. Management and
qualified security leadership choose the approach; AI must not select it merely
to reduce the work needed for a favourable result.

## Engagement focus

Connect the approved information domain to its objects, protection decisions,
applicable requirements, observed gaps and verified implementation. Keep the
methodology edition separate from the Compendium edition and system version.

## Roles

Management owns scope, resources and residual risk. Security leadership owns the
method and modelling decisions. Business owners provide protection-impact facts;
operators supply actual evidence and perform authorised changes. Independent
reviewers challenge coverage. AI may reconcile metadata and draft mappings, but
cannot approve protection needs, exceptions, risk acceptance or certification.

## Before starting

Obtain approach/scope approval, source editions, business-process and object
inventory, dependency map, protection-impact inputs, existing model, test authority
and evidence permissions. If a source is unavailable, organise factual inventory
while keeping requirement conclusions pending. Follow the [agent runbook](../agent-runbook.md).

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Pin approach and scope | Management/security record the intended approach, information domain and exclusions. | Approved scope and source editions; no implied organisation-wide conclusion. |
| 2. Reconcile structure | Owners identify processes, information, applications, systems, connections and infrastructure. AI checks relationships. | Object/dependency register with unexplained omissions visible. |
| 3. Determine protection needs | Business/security evaluate impacts and dependencies under the approved method. | Owned protection decisions and rationale; AI suggestions remain draft. |
| 4. Model requirements | Security selects applicable source references and records adaptations or exclusions for each object/group. | Reviewed mapping with version and rationale; no invented module text. |
| 5. Check actual implementation | Authorised reviewers compare expected requirements with observed evidence. | Per-claim results distinguish implemented, absent, partial and untested states. |
| 6. Resolve additional risk | Security/risk identify where the chosen method requires further analysis; management decides treatment. | Risk-analysis references, decisions and additional work, without silent omission. |
| 7. Implement and retest | Operators perform approved changes; reviewer repeats affected checks. | Gap/change/retest trail and unresolved items. |
| 8. Maintain the model | Security evaluates changes; management reviews remaining risk and next work. | Updated model and evidence queue with prior decisions retained. |

The exact method depends on the approved approach and source. This coordination
sequence does not replace approach-specific instructions or a certification audit.

## Evidence and test plan

| Evidence and custodian | Check | Expected observation | Failure or limit |
| --- | --- | --- | --- |
| Structure map, architecture | Reconcile a process with supporting objects and dependencies. | Objects have stable IDs and owners. | An incomplete inventory cannot support complete modelling. |
| Protection/grouping decisions, security | Compare group membership with approved protection needs and relevant properties. | Grouping has a substantive rationale. | Grouping solely to reduce record count conceals differences. |
| Mapping/check records, reviewer | Trace an object to source reference and actual observation. | Edition, applicability and observed state are explicit. | A copied checklist is not implementation evidence. |
| Risk/treatment/retest trail, risk/operators | Follow a gap through decision, change and verification. | Retest addresses the original condition. | A completed change ticket cannot establish effectiveness. |

## Failure branches and decisions

Missing methodology or Compendium text blocks detailed conclusions, not permitted
inventory. A new dependency requires impact review before reusing a prior mapping.
Contradictory implementation evidence remains an unresolved finding. Higher-impact
objects must not inherit a lower-impact group's conclusion without review. After
interruption, check the actual object version and prior changes before retesting.

## Cadence and renewal

Review after material process, object, dependency, threat, incident or source changes.
Quarterly evidence review and annual management renewal are planning defaults.
Source updates require a recorded delta and approved migration; do not silently
replace references in completed workpapers.

## Completion and handoff

Deliver approach/scope, structure and protection records, reviewed model, checks,
risk/treatment decisions, retests and next queue. Name unmodelled objects, untested
requirements and source-access gaps. Independent source, engagement and skeptical
review and named human publication approval remain pending. Original instructions
and links only; no source modules or private evidence reproduced.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md).
