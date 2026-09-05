# GHG Protocol Corporate Standard — engagement guide

> Original operational guidance, not GHG Protocol text, accounting advice, verification or assurance. Draft pending independent source, skeptical and rights review.

## Source and applicability

Use the publisher's [Corporate Standard page](https://ghgprotocol.org/corporate-standard) and current applicable methodology documents. It describes a corporate emissions inventory, identifies separate Scope 2 and Scope 3 guidance, and distinguishes project accounting for offsets/credits. It does not itself prescribe the verification process or require reports to WRI/WBCSD.

The publisher page was read for this draft; the full standard, amendments, current revision status and companion guidance remain to be reviewed. Record the actual edition applicable to the reporting period. Consultation proposals are not automatically effective requirements. Obtain authorized access to protected source material; do not reproduce standards or proprietary factors here.

## Engagement focus

Produce a reproducible inventory with explicit boundaries, sources, calculations, estimates and review decisions. Keep completeness, arithmetic accuracy, methodological appropriateness and assurance conclusions separate. A correct sum of incomplete activity records is still an incomplete inventory.

## Roles

Sustainability and finance owners approve reporting scope and methodology. Operational data owners provide source records and explain gaps. Qualified methodology specialists approve factors, consolidation, estimates and base-year treatment. An independent reviewer challenges calculations, boundaries and disclosure. Authorized reporting officials approve publication; a separately appointed assurance provider owns any assurance conclusion.

AI may reconcile authorized data, reperform approved calculations, flag anomalies and draft workpapers. AI cannot select accounting treatments, approve factors or estimates, issue assurance, publish emissions claims or declare an inventory compliant. Do not confuse an automated quality check with independent assurance.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Obtain entity, reporting period, approved organizational and operational boundaries, consolidation approach, base year, source versions, owners and data-access authority. Define reporting outputs and companion standards needed for the engagement. Missing boundary or method decisions block dependent calculations; independent inventory collection may continue.

## Ordered workflow

1. **Approve the reporting contract.** Record entity coverage, period, units, boundaries, method versions and decision owners. Separately scope value-chain, project-credit or other additional claims. Output: versioned methodology decision register.
2. **Reconcile the source population.** Map entities, sites, equipment and activities to relevant source systems and owners. Compare operational and finance records for omissions, overlaps, acquisitions and disposals. Output: complete scoped population with unresolved items retained.
3. **Collect activity evidence.** Preserve original records, units, dates, provenance, revisions and coverage. Distinguish measured data, estimates and missing values. Output: source register; a blank field is not zero emissions.
4. **Bind calculation inputs.** Link each row to its owner-approved factor, factor units, geography/period applicability, conversion sequence and any approved warming-potential treatment. Output: calculation manifest. Prevent a factor already expressed in CO2-equivalent from receiving a duplicate conversion without an approved methodological basis.
5. **Reperform and reconcile.** Use the approved method to recompute every reported calculation, reconcile totals and inspect missing/duplicate records. Keep numerical checks separate from method approval. Output: calculation results, discrepancy log and coverage limitations.
6. **Review changes and comparability.** Route structural changes, method changes, source corrections and base-year questions through the approved recalculation policy. Preserve both prior and revised versions. Output: change bridge explaining movements without automatically attributing them to operational reductions.
7. **Review disclosure and hand off.** Trace every reported figure and claim to the calculation population and approved method. Preserve estimates, exclusions, uncertainty and unresolved disagreements. Output: review packet and named publication/assurance decisions; no publication or assurance is implied by delivery.

## Evidence and test plan

### Reporting boundary and methodology package

Restore the prior PR340 package with full boundary reconciliation. Owners provide the entity structure, consolidation decisions, reporting period, base year, source categories, methodology versions and approval history. Tie each included or excluded activity to a decision and justification. Do not use a supplier list alone to infer the organizational boundary, or silently change consolidation between years.

### Activity data, calculation and reconciliation package

Operational and finance owners provide activity extracts, invoice/meter provenance, unit conversions, factors, workpapers, estimates and corrections. Maintain stable source identifiers to detect overlapping invoices or duplicate imports. Record missing months and unavailable sites explicitly. Preserve precision through calculations and document reporting rounding. Reconcile the complete calculation population to disclosed totals; targeted supporting-document tests must disclose their limits and cannot substitute for population completeness.

For each calculation record input value/unit, factor value/unit/source/version, approved transformations, expected output unit, result, reviewer observation and evidence reference. If a tool fails, retain the failure rather than returning a zero or a partial total labelled complete. Estimated values require approved methods and separate identification; they are not observed measurements.

### Disclosure, uncertainty and review package

Reporting owners supply the exact draft version, source-linked figures, estimates, limitations, changes, review disagreements and approvals. Track uncertainty in inputs and methods separately from known arithmetic errors. If multiple reporting methods are applicable, preserve their labels and totals rather than adding alternative presentations together. Keep inventory emissions, credits and avoided-emissions claims distinguishable and use separately approved sources for any adjustment or additional claim.

## Failure branches and decisions

- Unknown or conflicting boundary: classify the affected completeness claim inconclusive and assign the decision; do not choose the lower-emission boundary automatically.
- Missing activity data: retain the missing population, obtain owner-approved estimation or disclose the gap. Never fill with zero merely to finish a workbook.
- Wrong factor units or duplicate conversion: mark the affected numerical result not_supported, correct under the approved method and propagate the correction to all dependent totals and disclosures.
- Correct arithmetic with an unapproved factor: arithmetic may be supported while methodological suitability remains inconclusive.
- Apparent reduction caused by changed entity scope: prepare a change bridge and seek the approved comparability treatment; do not claim operational improvement from the difference alone.

Fictional desk case: 1,000 kWh multiplied by an approved 0.4 kg CO2e/kWh factor yields 400 kg CO2e, or 0.4 metric tonnes. A report labelling the result 400 tonnes fails the unit-conversion criterion. The arithmetic example does not validate the factor or establish completeness of electricity data.

## Cadence and renewal

Use the approved reporting calendar and applicable program obligations. Refresh after acquisitions, divestitures, data corrections, source/method changes and period close. Record base-year review triggers and approvals; do not invent a universal assurance renewal or fixed quarterly review requirement. Verify corrections across current and affected historical disclosures before closure.

## Completion and handoff

Deliver the source register, approved boundary/method decisions, complete activity population, reproducible calculations, change bridge, uncertainty/limitations, reviewer disagreements and publication decisions. Classify each assertion supported, not_supported, inconclusive, not_applicable or not_tested with reasons. Keep draft delivery, final publication and assurance status separate. No customer inventory or assurance engagement was performed by authoring this guide.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) and [agent runbook](../agent-runbook.md). Keep protected source content and confidential company activity records outside this public repository.
