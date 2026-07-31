# NIST SP 800-38G format-preserving-encryption engagement guide

> Original operational guidance, not NIST format-preserving-encryption specifications, a cryptographic design, an approval, or a compliance claim. Confirm current material through [NIST SP 800-38G](https://csrc.nist.gov/pubs/sp/800/38/g/upd1/final) and the organization’s approved cryptography, security, architecture, legal, and operational decisions.

## Engagement focus

Operate a governed lifecycle for in-scope uses of format-preserving encryption. Connect each use case to an approved purpose and scope, data format and domain context, implementation and configuration decisions, key-management and input-handling dependencies, interfaces, access, logging, validation, supplier dependencies, changes, incidents, transition planning, and retirement. A configuration extract, implementation record, supplier statement, test result, or audit log is evidence to assess; none alone proves suitable design, correct implementation, protected keying material, approved use, safe handling of the data format, secure operation, or compliance.

## Roles and annual rhythm

Assign accountable executive, security, cryptography or platform engineering, architecture, application and data owners, key-management operations where relevant, supplier-management, legal and privacy where relevant, change-management, incident-response, and records-management roles. Operators maintain scoped use inventories, approved design and configuration decisions, data-format and dependency records, implementation and validation baselines, access and audit records, supplier materials, exception and incident records, transition decisions, and retirement evidence. Reconcile uses, owners, data domains, dependencies, interfaces, and suppliers quarterly; review cryptographic alerts, implementation changes, exceptions, incidents, transition needs, and unresolved risks at least quarterly; and complete an annual management review after material cryptographic, data-format, product, provider, threat, or publication changes. Before annual renewal, an independent reviewer samples purpose-to-implementation-to-operation-to-review traceability; auditors test supplied evidence without selecting a method or parameters, accessing keying material, changing configuration, approving exceptions, accepting risk, or attesting for management.

AI may organize supplied inventory, design, implementation, test, supplier, and review evidence, identify missing owners or stale decisions, and draft workpapers for human review. AI cannot select a format-preserving-encryption method or parameters, access protected material, change configuration, approve an exception, accept risk, make a compliance conclusion, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** Use the official [NIST SP 800-38G publication record](https://csrc.nist.gov/pubs/sp/800/38/g/upd1/final) and approved organizational cryptography decisions; checked 2026-07-31. This original plan collects format-preserving-encryption implementation and usage evidence only. It does not reproduce the publication, validate an algorithm or module, prescribe an FPE method or parameters, or make a conformance claim.

### 1. Format-domain purpose and integration package

- **Request and owner:** Application, data, and cryptography owners provide an inventory of declared FPE uses, approved purpose and data-flow references, declared input format/domain descriptions that exclude live protected values, sender/receiver or service identifiers, library/provider versions, key-management dependency references, and named owners.
- **Validate and limit:** Trace one declared use from purpose and format-domain record through the identified integration, library/provider, key-management interface, and owner. This checks traceability of supplied records; it cannot determine whether the format domain, method, parameterization, data handling, or implementation is suitable or correct.
- **AI and trigger:** AI may reconcile redacted inventories and flag missing format-domain descriptions, owners, dependencies, or versions. Humans decide data treatment, scope, and cryptographic design. Refresh after a new use, format/domain change, integration, library, provider, or key-management change.

### 2. Deployment and data-path-operation package

- **Request and owner:** Platform and application owners provide approved build/release/deployment records, non-secret configuration references identifying the declared FPE integration, protected configuration-access records, change tickets, and non-secret error or incident summaries for the affected data path.
- **Validate and limit:** Link a selected deployment or data-path change to its approved change, release identity, declared integration/configuration reference, owner, and available operational evidence. This does not expose protected values, access keying material, run FPE operations, test format preservation, or establish safe data handling.
- **AI and trigger:** AI may compare supplied version and deployment metadata and prepare missing-evidence questions. It may not access production data or keys, invoke cryptographic operations, change configuration, or interpret errors as validation. Humans approve releases, exceptions, and remediation. Refresh after a release, data-flow incident, format/domain change, or provider change.

### 3. Supplier, exception, and retirement package

- **Request and owner:** Security, supplier-management, data-governance, and records owners provide component/provider provenance, support or vulnerability notices, exception and incident references, migration/retirement decisions, review minutes, and evidence-retention references.
- **Validate and limit:** Sample one component, exception, or retirement event through provenance, accountable review, decision record, corrective action, and next-review date. This supports lifecycle accountability; it cannot validate a supplier component, prove reversibility or data protection, or establish compliance.
- **AI and trigger:** AI may flag stale notices, unowned exceptions, missing migration links, or overdue review dates. Humans decide remediation, data migration, risk acceptance, and external statements. Review quarterly and after material supplier, threat, data-format, implementation, or publication changes.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
