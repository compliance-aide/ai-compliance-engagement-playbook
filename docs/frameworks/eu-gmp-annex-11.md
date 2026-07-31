# EU GMP Annex 11 — computerized-systems engagement guide

> Original operational guidance, not EU GMP text or a regulatory conclusion. Check [EudraLex Volume 4](https://health.ec.europa.eu/medicinal-products/eudralex/eudralex-volume-4_en).

## Engagement focus

Maintain GxP system estate, intended use, data owners, suppliers, validation, change, release, access, review, recovery, interface, deviation, and remediation evidence.

## Roles and annual rhythm

Qualified humans approve validation and batch-quality decisions; independent reviewers test lineage. AI flags risks and creates read-only packs, but cannot accept validation or make interpretations. Review quarterly and annually.


## Tailored evidence plan

**Source and rights snapshot.** Refer to the official [EudraLex Volume 4](https://health.ec.europa.eu/medicinal-products/eudralex/eudralex-volume-4_en); source status: official EU GMP collection, retrieved 2026-07-31. This original plan does not reproduce Annex 11, determine GMP compliance, approve validation, release product, or make a regulatory conclusion.

### 1. GxP computerized-system intended-use and lifecycle evidence

- **Request and owner:** Quality, system, and process owners provide the GxP system inventory, intended-use statements, process/data owners, supplier roles, lifecycle or validation plans, release history, and change-control records for in-scope systems.
- **Validate and limit:** Trace a selected system from approved intended use through accountable owner, lifecycle record, change history, and current operational boundary. This supports a clear evidence lineage; it cannot validate a system, approve intended use, or decide product-quality impact.
- **AI and trigger:** AI may organize approved metadata and flag a missing owner, change link, or stale lifecycle record. Qualified humans approve intended use, validation, and release decisions. Refresh before material configuration, interface, supplier, or use change.

### 2. Data integrity, access, and operational-record evidence

- **Request and owner:** System administration, quality, and data owners provide role/access review records, audit-trail review evidence where approved, operational logs, backup/recovery evidence, interface-monitoring records, deviation records, and retention-location details for the chosen period.
- **Validate and limit:** Inspect a selected record for source system, timestamp, accountable reviewer, protected access path, and linkage to any deviation or corrective action; do not copy regulated production data into this repository. This can test record lineage and review evidence, not prove data integrity or validated operation.
- **AI and trigger:** AI may identify incomplete metadata and draft read-only evidence requests. Human owners control access, investigate anomalies, and approve data or quality decisions. Refresh after access changes, deviations, recovery events, interface changes, and periodic review.

### 3. Supplier, deviation, and quality-governance evidence

- **Request and owner:** Quality, procurement, and system owners provide supplier qualification records, quality-agreement references, service/change notifications, deviation and CAPA records, periodic-review outputs, and management or quality-review decisions.
- **Validate and limit:** Trace a selected supplier-related change or deviation to source evidence, product/system boundary, quality owner, investigation, corrective action, and documented approval. This supports accountable follow-up; it cannot qualify a supplier, close a deviation, or accept a validation or quality risk.
- **AI and trigger:** AI may flag overdue CAPAs, unlinked supplier changes, or missed periodic reviews. Qualified humans make quality, supplier, and closure decisions. Refresh after deviations, supplier changes, planned releases, and annual quality review.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
