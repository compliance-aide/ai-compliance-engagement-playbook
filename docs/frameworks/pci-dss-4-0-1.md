# PCI DSS v4.0.1 — engagement guide

> Original operational guidance, not a PCI SSC publication or validation claim.
> Check the current [PCI DSS library](https://www.pcisecuritystandards.org/document_library/?class=pcidss&doc=pci_dss),
> payment brands, and acquirer directions before each milestone.

## Engagement focus

Establish the payment-data and connected-system boundary, responsibility
allocation, payment flows, and relevant service providers. Maintain evidence
for access, configuration, change, vulnerabilities, monitoring, incident
readiness, and operational safeguards; test effectiveness; resolve exceptions;
and retain validation outputs separately.

## Roles

The entity operates its card-data environment and evidence program. Qualified
assessors independently perform work where required. AI may build the authorized evidence
calendar, find scope drift and unowned evidence, and draft questions; it cannot
select a validation route, approve a scope or compensating-control decision, or attest to a result.

## Annual rhythm

Refresh payment-flow and supplier inventories; review boundary changes; gather
time-bounded evidence; test critical operations; track remediation; and confirm
the appropriate validation path with the responsible human parties.

## Tailored evidence plan

**Source and rights snapshot.** Use the current [PCI DSS library](https://www.pcisecuritystandards.org/document_library/?class=pcidss&doc=pci_dss), payment-brand, and acquirer direction; checked 2026-07-31. PCI materials and validation routes have program conditions. This is original planning language, not a substitute for a PCI SSC document, SAQ, ROC, compensating-control decision, or attestation.

**Plan status:** Independently reviewed; see the [review receipt](../evidence-plan-reviews/pci-dss-4-0-1.md).

### 1. Payment-data boundary and responsibility evidence

- **Request and owner:** Payment-flow diagrams, card-data environment and connected-system inventory, account-data location/retention records, service-provider responsibility matrix, and human-selected validation route inputs, from payment, security, architecture, and vendor owners.
- **Validate and limit:** Trace a selected payment flow to systems, providers, data boundary, and responsibility records; identify undocumented connections and inherited services. This can support a scoped readiness view. It cannot select an SAQ/ROC route, approve scope, or prove all connected systems are known.
- **AI and trigger:** AI may reconcile authorized inventories and flag scope drift. Authorized human parties approve scope and validation path. Revisit after a payment flow, provider, integration, network, or stored-data change.

### 2. Security-operation evidence for the declared card-data environment

- **Request and owner:** Time-bounded access/privilege, configuration/change, vulnerability/remediation, monitoring/log-review, incident-readiness, and operational-safeguard records, from the responsible technical owners.
- **Validate and limit:** Inspect source/time/coverage and trace an approved selection to the declared environment and documented exception. This can support that evidence exists for selected practices; it cannot prove continuous effectiveness, compensate for scope error, or produce a validation result.
- **AI and trigger:** AI may create a non-destructive evidence index and escalate gaps; it may not change card-data systems, decide a compensating control, or attest. Refresh after critical changes, incidents, failed tests, or evidence-period rollover.

### 3. Validation, exception, and provider-change workpaper

- **Request and owner:** Authorized test/assessment workpapers, unresolved exceptions, remediation/retest record, provider-attestation inputs where applicable, and external-validation output retained separately, maintained by the engagement lead.
- **Validate and limit:** Trace a selected exception to owner, approval authority, expiry, evidence, and retest. This can support readiness governance; it cannot create an attestation, bind an acquirer, or replace qualified-assessor work.
- **AI and trigger:** AI may draft traceability and identify missing inputs. Humans approve exceptions, submissions, and external claims. Revisit before formal validation, annually, and on provider or program-rule change.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
