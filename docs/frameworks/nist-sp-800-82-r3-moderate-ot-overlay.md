# NIST SP 800-82 Revision 3 moderate-impact OT overlay engagement guide

> Original operational guidance, not NIST overlay or control text, a system-impact decision, an OT safety decision, a tailoring decision, or a compliance claim. Confirm current material through the [NIST SP 800-82 Revision 3 OT overlay](https://csrc.nist.gov/projects/risk-management/sp800-53-controls/overlay-repository/nist-developed-overlay-submissions/operational-technology) and applicable authority direction.

## Engagement focus

Use this engagement only after accountable owners document the OT system boundary, the moderate-impact determination, process and service dependencies, safety constraints, and the authority context for applying the overlay. Maintain a controlled record of physical processes, assets, communications, suppliers, shared services, access paths, maintenance windows, emergency procedures, inherited capabilities, tailoring rationale, exceptions, and material changes. The overlay supports partial tailoring; it does not authorize operation, set safety tolerances, or replace engineering and operations judgment.

## Roles and annual rhythm

Assign accountable leadership for impact and risk decisions, OT engineering and operations owners for process evidence, safety owners for safety constraints, security owners for cybersecurity evidence, and supplier owners for external dependencies. Operators preserve architecture, asset, interconnection, access, maintenance, change, test, incident, safety-escalation, supplier, and remediation evidence. Review scope, impact, overlay rationale, exceptions, safety constraints, dependencies, and open findings quarterly and before material operational changes. Before annual renewal, an independent reviewer samples the overlay record and critical operating evidence; auditors test decision support without classifying the system, tailoring the overlay, directing operations, accepting risk, or making safety decisions.

AI may organize supplied evidence, reconcile asset and dependency records, flag missing ownership or conflicts, summarize remediation, and draft workpapers for human review. AI cannot classify OT impact, select or tailor an overlay, approve operational or safety changes, determine authorization readiness, accept risk, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** At engagement start, retain the retrieved version and applicable use terms for the official [NIST SP 800-82 Revision 3 OT overlay](https://csrc.nist.gov/projects/risk-management/sp800-53-controls/overlay-repository/nist-developed-overlay-submissions/operational-technology), the related [NIST OT security publication](https://csrc.nist.gov/pubs/sp/800/82/r3/final), and the authority direction used for the moderate-impact designation. The packages are original evidence-planning guidance, not overlay text or a determination of impact, safety, tailoring, authorization, or compliance.

### 1. Moderate-impact process and dependency package

- **Request and owner:** OT engineering, operations, safety, asset, network, and service owners provide the approved moderate-impact rationale, physical-process and asset boundary, interconnection and shared-service map, critical communications, recovery dependencies, safety constraints, maintenance windows, and emergency procedures.
- **Validate and limit:** Trace one material process through supporting assets, an external or shared dependency, safety constraint, named owner, and stated recovery or emergency assumption. This can test whether a material dependency record is coherent; it cannot determine impact, completeness, safe operation, or recovery success.
- **AI and trigger:** AI may reconcile supplied asset and dependency records and identify conflicts for human review. Humans approve impact, process scope, dependency treatment, and safety constraints. Refresh before material architecture, process, supplier, connectivity, or authority change.

### 2. Tailoring, access, and maintenance-control package

- **Request and owner:** Security, OT engineering, operations, safety, identity, supplier, and change owners provide overlay-use and tailoring rationale, inherited-capability assumptions, access pathways and approvals, remote-support conditions, maintenance/change records, exceptions, and compensating-measure decisions.
- **Validate and limit:** Sample one remote-support or maintenance path from approved operating condition through access authorization, change or work record, safety constraint, and documented exception where relevant. This can evaluate evidence traceability; it cannot authorize access, decide tailoring, or demonstrate that every pathway is secure.
- **AI and trigger:** AI may flag missing approvals, expired exceptions, or inconsistent owners without accessing operational systems. Humans authorize access, maintenance, and changes and approve exceptions. Recollect after an access-path, supplier, maintenance, or exception change.

### 3. Authorized assurance and remediation package

- **Request and owner:** OT operations, safety, security, incident, supplier, risk, and independent-review owners provide safe-test authorizations, non-disruptive verification outputs, incident and safety escalation records, corrective-action tracking, retest or rationale, and quarterly management review.
- **Validate and limit:** Trace a selected issue or approved check from safety authorization through result, responsible owner, remediation evidence, retest or documented limitation, and human review. This can support a reviewable improvement record; it cannot prove comprehensive security, establish safety, or accept residual risk.
- **AI and trigger:** AI may prepare source-linked review packets and flag overdue actions. Humans authorize testing, evaluate safety effects, approve closure, and accept risk. Review quarterly and after a failed check, incident, safety escalation, material change, or supplier event.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
