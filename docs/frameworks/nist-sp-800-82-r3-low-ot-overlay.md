# NIST SP 800-82 Revision 3 low-impact OT overlay engagement guide

> Original operational guidance, not NIST overlay or control text, a system-impact decision, an OT safety decision, a tailoring decision, or a compliance claim. Confirm current material through the [NIST SP 800-82 Revision 3 OT overlay](https://csrc.nist.gov/projects/risk-management/sp800-53-controls/overlay-repository/nist-developed-overlay-submissions/operational-technology) and applicable authority direction.

## Engagement focus

Use this engagement only after accountable owners document the OT system boundary, the low-impact determination, operational dependencies, and the authority context for applying the overlay. Maintain a controlled record of physical process relationships, assets, communications, suppliers, shared services, safety constraints, maintenance windows, emergency procedures, inherited capabilities, tailoring rationale, and material changes. Treat the overlay as partial tailoring support, not an automatic authorization or a replacement for safety, engineering, and operations decisions.

## Roles and annual rhythm

Assign accountable leadership for impact and risk decisions, OT operations and engineering owners for process evidence, safety owners for safety constraints, security owners for cybersecurity evidence, and supplier owners for external dependencies. Operators retain architecture and asset records, operating and maintenance evidence, access and change records, test outcomes, incidents, safety-related escalation evidence, supplier records, and remediation proof. Review scope, impact, overlay rationale, safety constraints, exceptions, and open findings quarterly and before material operational changes. Before annual renewal, an independent reviewer samples the overlay record and operational evidence; auditors examine decision support without classifying the system, tailoring the overlay, directing operations, accepting risk, or making safety decisions.

AI may organize supplied evidence, reconcile asset and dependency records, flag missing ownership or conflicts, and draft workpapers for human review. AI cannot classify OT impact, select or tailor an overlay, approve operational or safety changes, determine authorization readiness, accept risk, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** At engagement start, retain the retrieved version and applicable use terms for the official [NIST SP 800-82 Revision 3 OT overlay](https://csrc.nist.gov/projects/risk-management/sp800-53-controls/overlay-repository/nist-developed-overlay-submissions/operational-technology), the related [NIST OT security publication](https://csrc.nist.gov/pubs/sp/800/82/r3/final), and the authority direction used for the low-impact designation. This is original evidence-planning guidance; it does not reproduce the overlay or determine impact, tailoring, safety, authorization, or compliance.

### 1. Low-impact scope and process-boundary package

- **Request and owner:** OT operations, engineering, safety, asset, and service owners provide the approved low-impact rationale, process and asset boundary, communications and shared-service map, named owners, safety constraints, maintenance windows, emergency procedures, and stated exclusions.
- **Validate and limit:** Trace a selected process-to-asset path through its named owner, communication dependency, safety constraint, and documented boundary decision. This can test whether the low-impact evidence trail is internally coherent; it cannot classify impact, prove all dependencies are known, or establish a safe operating state.
- **AI and trigger:** AI may reconcile supplied inventories and identify missing owners or stale dependencies. Accountable humans approve scope, designation, safety limits, and exclusions. Refresh before material process, connectivity, supplier, maintenance, or authority change.

### 2. Overlay-use and operating-safeguard package

- **Request and owner:** Security, OT engineering, operations, safety, and change owners provide the overlay-use rationale, local tailoring record, inherited-service assumptions, approved operating safeguards, access and maintenance records, exceptions, and change approvals.
- **Validate and limit:** Sample one stated safeguard dependency from its overlay-use rationale through the local implementation or inherited-service record, approved exception where applicable, and operating owner confirmation. This can assess traceability of planned use; it cannot select controls, validate all implementations, authorize a change, or replace safety review.
- **AI and trigger:** AI may organize documents and flag unmatched assumptions or exception dates. Humans approve tailoring, changes, exceptions, and compensating measures. Recollect after a material change, exception, failed check, or inherited-service change.

### 3. Safe verification, incident, and renewal package

- **Request and owner:** OT operations, safety, security, incident, supplier, and independent-review owners provide authorized non-disruptive verification records, maintenance/test approvals and results, incident or safety-escalation handoffs, supplier support evidence, corrective actions, and quarterly review records.
- **Validate and limit:** Trace a selected approved check or event from safety authorization through observed result, operational handoff, corrective action or rationale, and review. This can support a reviewable operating record; it cannot authorize testing, determine safety, prove resilience, or accept residual risk.
- **AI and trigger:** AI may index supplied results and flag overdue actions. Humans authorize checks, interpret operational effects, approve closure, and accept risk. Review quarterly and after an incident, safety concern, supplier change, failed check, or material operational change.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
