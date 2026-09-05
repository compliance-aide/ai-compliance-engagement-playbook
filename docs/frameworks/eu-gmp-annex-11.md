# EU GMP Annex 11 — computerized-systems engagement guide

> Author draft. Original operational guidance, not regulatory approval, accepted
> validation, or authority to release a medicinal-product batch.

## Source and applicability

Source check, 2026-09-04: the official [EudraLex Volume 4 collection](https://health.ec.europa.eu/medicinal-products/eudralex/eudralex-volume-4_en)
still lists Annex 11 as the January 2011 revision. Read the complete five-page
[official Annex 11](https://health.ec.europa.eu/document/download/8d305550-dd22-4dad-8463-2ddb4a1345f1_en).
A newer consultation document is not evidence of an operative replacement;
recheck the official collection and adoption/applicability record before use.
The collection separately identifies veterinary regulations applicable from
16 July 2026. A quality/regulatory owner must verify the applicable legal route;
do not apply the historical PDF's veterinary legal references without that check.

Annex 11 distinguishes application validation from infrastructure qualification.
It covers lifecycle risk, traceable user requirements, testing, operational
controls, change, incidents and retirement. Sections 4.8, 7, 16 and 17 address
migration meaning, storage/recovery, continuity and archiving. Section 15 reserves
computerized batch certification/release to Qualified Persons. These source
anchors do not substitute for an engagement-specific quality interpretation.
Related chapters, annexes, current EMA questions and answers, national inspection
expectations and veterinary correspondence remain to be verified for each scope.

## Engagement focus

Build a traceable argument from approved intended use to the exact deployed
configuration, test observations and owned quality decisions. A vendor validation
pack may be useful input, but its version and assumptions must match the local
use. Keep documentation existence, technical behavior and accepted validation
as three separate assertions.

## Roles

The process owner describes the regulated activity and intended use. The system
owner supplies configuration and operational evidence. Quality owns the approved
validation approach, deviations and acceptance decisions. IT and suppliers carry
out authorized technical work; reviewers check lineage and unresolved failures.
The Qualified Person retains the batch role identified by the applicable rules.
AI organizes approved evidence and drafts comparisons. It cannot sign validation,
accept quality risk, close a deviation or certify/release a batch.

## Before starting

Use the [agent runbook](../agent-runbook.md) and
[work-item template](../../templates/work-item.md). Record site, product/process,
system/version, interfaces, data owners, GMP applicability decision, review period
and full population. Distinguish initial validation, change assessment, periodic
review, migration and retirement. Record authorized access and a QA-named test
workspace with synthetic records. Keep regulated records, secrets and actual
batch data outside this repository.

Have quality approve test criteria, environment suitability, execution authority
and stop conditions before testing. A generic script is not an approved protocol.
If safe representative testing is unavailable, collect authorized documentation
and mark the unexecuted tests explicitly; do not improvise in production.

## Ordered workflow

1. **Reconcile the estate.** Match the system inventory to process maps,
   application/configuration records and supplier services. Include spreadsheets,
   interfaces, instruments, infrastructure dependencies and archived systems when
   they participate in the approved scope. Record exclusions with an owner and
   rationale; an unlisted dependency is a gap to resolve.
2. **Freeze intended use and configuration.** Link each function to its process
   owner, approved user requirement, risk rationale and current build/configuration.
   Separate supplier defaults from site-specific configuration. Do not reuse a
   conclusion for a new configuration merely because the product name is unchanged.
3. **Build requirement-to-evidence traceability.** Give each approved requirement
   its own acceptance criterion, protocol step, expected observation, evidence
   location and reviewer. Reconcile all in-scope requirements and tests, including
   not-run and failed items. Quality determines justified validation scope; never
   trim evidence already bound for a scorer or relabel omitted tests as passed.
4. **Execute the approved protocol.** Capture inputs, environment/version,
   observed outputs, timestamps and deviations. Preserve first-run failures as
   well as later retests. Compare observations to criteria established beforehand;
   a script exit code alone does not establish the required process behavior.
5. **Exercise data paths.** Apply the transfer/recovery sequence below to each
   relevant interface or migration. Test approved access, change-history and
   record-output assertions independently. A readable report may omit underlying
   context; a complete database may still have an unusable application view.
6. **Resolve deviations and changes.** Link each discrepancy to the affected
   requirements, system versions and quality owner. Record investigation, proposed
   correction, change approval, retest and residual limitations. Keep open
   deviations visible in the acceptance packet; the agent cannot close them.
7. **Prepare the operational handoff.** Link user/admin procedures, training,
   supplier responsibilities, monitoring, recovery and review plans to their
   owners. Verify that handoff artifacts address the actual configuration and
   unresolved restrictions, not only the original project baseline.
8. **Obtain the quality disposition.** Present the complete traceability matrix,
   observations and deviation record for independent review and authorized
   acceptance. Store the exact approved version. Preparation of this packet is
   neither system release nor product release.

### Transfer and recovery execution sequence

The following is an original test-design recommendation. Quality selects and
approves the assertions and methods appropriate to the intended use.

1. Define the source and destination versions, complete record population,
   approved transformation rules, data dictionary and retention boundary. Record
   units, precision, time zones, identifiers, relationships and status meanings.
2. Establish a reproducible pre-transfer inventory and protected evidence
   reference. Execute only the authorized QA transfer or restoration. Capture
   job errors, rejects and retries; do not rely on a success banner.
3. Reconcile counts and identifiers for missing, duplicate and unexpected records.
   Then compare values, units, relationships, status and required history against
   the approved rules. Matching row counts do not prove preserved meaning.
4. Open the restored information through the intended user path. Check authorized
   readers can interpret the record and unauthorized roles cannot perform the
   prohibited action. Treat permissions, readability and content preservation as
   separate tests, each with an expected result.
5. Exercise the approved alternative-process and return-to-service procedure.
   Measure the business-process availability criterion, not merely server startup.
   Reconcile records created during the alternative procedure before handback.
6. Record every discrepancy and quality disposition. Retest changes against the
   original criterion. Preserve both pre-correction and post-correction evidence,
   and verify cleanup of synthetic test residue under the approved plan.

## Evidence and test plan

Retain these three packages from PR #340, expanded to full in-scope coverage.
A prior review of an earlier artifact does not approve this revised workflow.

### 1. GxP computerized-system intended-use and lifecycle evidence

- **Request and owner:** Quality, system, and process owners provide the GxP system inventory, intended-use statements, process/data owners, supplier roles, lifecycle or validation plans, release history, and change-control records for in-scope systems.
- **Validate and limit:** Trace each in-scope system from approved intended use through accountable owner, lifecycle record, change history, and current operational boundary. This supports a clear evidence lineage; it cannot validate a system, approve intended use, or decide product-quality impact.
- **AI and trigger:** AI may organize approved metadata and flag a missing owner, change link, or stale lifecycle record. Qualified humans approve intended use, validation, and release decisions. Refresh before material configuration, interface, supplier, or use change.

### 2. Data integrity, access, and operational-record evidence

- **Request and owner:** System administration, quality, and data owners provide role/access review records, audit-trail review evidence where approved, operational logs, backup/recovery evidence, interface-monitoring records, deviation records, and retention-location details for the chosen period.
- **Validate and limit:** Inspect each in-scope record for source system, timestamp, accountable reviewer, protected access path, and linkage to any deviation or corrective action; do not copy regulated production data into this repository. This can test record lineage and review evidence, not prove data integrity or validated operation.
- **AI and trigger:** AI may identify incomplete metadata and draft read-only evidence requests. Human owners control access, investigate anomalies, and approve data or quality decisions. Refresh after access changes, deviations, recovery events, interface changes, and periodic review.

### 3. Supplier, deviation, and quality-governance evidence

- **Request and owner:** Quality, procurement, and system owners provide supplier qualification records, quality-agreement references, service/change notifications, deviation and CAPA records, periodic-review outputs, and management or quality-review decisions.
- **Validate and limit:** Trace each in-scope supplier-related change or deviation to source evidence, product/system boundary, quality owner, investigation, corrective action, and documented approval. This supports accountable follow-up; it cannot qualify a supplier, close a deviation, or accept a validation or quality risk.
- **AI and trigger:** AI may flag overdue CAPAs, unlinked supplier changes, or missed periodic reviews. Qualified humans make quality, supplier, and closure decisions. Refresh after deviations, supplier changes, planned releases, and annual quality review.

## Failure branches and decisions

Use the runbook's assertion results independently of work status.

- Approved protocol exists but execution evidence is absent: execution is
  `not_tested`; accepted validation remains unproven. Request the missing record
  or an authorized run instead of treating approval as a passing test.
- Supplier evidence concerns a different configuration: local applicability is
  `inconclusive` until the configuration difference is resolved. Preserve any
  independently observed local failure as `not_supported`.
- An operator can perform a prohibited action in the approved QA test: that
  access-control assertion is `not_supported`. Escalate the observed role/action
  and scope; do not test additional production permissions without authorization.
- A correction fixes output but destroys required history: preserve the history
  failure. Do not accept the correction because the displayed final value matches.
- Required evidence is inaccessible: mark the affected check `not_tested` and
  assign recovery; inaccessible data does not establish absent data.

**Fictional desk case:** A QA migration transfers all 100 synthetic records. One
source measurement is 2.5 mg; the destination displays 2.5 g. Count reconciliation
is `supported`, but preservation under an approved same-unit/same-value criterion
is `not_supported`. If history retrieval also fails authorization, history is
`not_tested`. Fixing the unit mapping does not resolve the history gap or authorize
validation acceptance. No real migration or product decision is represented.

## Cadence and renewal

Use a quality-approved, risk-based review schedule rather than declaring a
universal quarterly or annual Annex 11 deadline. Reassess after changes in use,
configuration, interfaces, supplier services, incidents, recovery or source rules.
For retirement, confirm the owned archive/retrieval plan before decommissioning
the only system capable of interpreting retained records.

## Completion and handoff

Deliver the versioned scope, sources, requirement/test matrix, complete evidence
index, deviations, retests, operational owners and signed human dispositions where
actually obtained. State what was examined and what remains untested. Record the
next review trigger and owner for every limitation. Independent source, skeptical,
rights and publication reviews remain pending for this guide; no structural
validator proves regulatory accuracy, accepted validation or cross-model usability.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md)
for shared authority, evidence, technical-test, exception and renewal requirements.
