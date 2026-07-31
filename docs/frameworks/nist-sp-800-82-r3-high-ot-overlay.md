# NIST SP 800-82 Revision 3 high-impact OT overlay engagement guide

> Original operational guidance, not NIST overlay or control text, a system-impact decision, an OT safety decision, a tailoring decision, or a compliance claim. Confirm current material through the [NIST SP 800-82 Revision 3 OT overlay](https://csrc.nist.gov/projects/risk-management/sp800-53-controls/overlay-repository/nist-developed-overlay-submissions/operational-technology) and applicable authority direction.

## Engagement focus

Use this engagement only after accountable owners document the OT system boundary, the high-impact determination, critical process and service dependencies, safety constraints, and the authority context for applying the overlay. Maintain a controlled record of physical processes, assets, interconnections, suppliers, shared services, access paths, maintenance windows, emergency operations, inherited capabilities, tailoring rationale, exceptions, and material changes. The overlay is partial tailoring support; it does not settle authorization, safety tolerances, operational priorities, or risk acceptance.

## Roles and annual rhythm

Assign accountable leadership for impact and risk decisions, OT engineering and operations owners for process evidence, safety owners for safety constraints, security owners for cybersecurity evidence, and supplier owners for external dependencies. Operators retain current architecture, asset, interconnection, access, maintenance, change, test, incident, safety-escalation, supplier, and remediation records. Review scope, impact, overlay rationale, safety constraints, dependencies, exceptions, and open findings quarterly and before material operational changes. Before annual renewal, an independent reviewer samples the overlay record and critical operating evidence; auditors test decision support without classifying the system, tailoring the overlay, directing operations, accepting risk, or making safety decisions.

AI may organize supplied evidence, reconcile asset and dependency records, flag missing ownership or conflicts, summarize remediation status, and draft workpapers for human review. AI cannot classify OT impact, select or tailor an overlay, approve operational or safety changes, determine authorization readiness, accept risk, attest for management, or replace independent review.

## Tailored evidence plan

**Source and rights snapshot.** At engagement start, retain the retrieved version and applicable use terms for the official [NIST SP 800-82 Revision 3 OT overlay](https://csrc.nist.gov/projects/risk-management/sp800-53-controls/overlay-repository/nist-developed-overlay-submissions/operational-technology), the related [NIST OT security publication](https://csrc.nist.gov/pubs/sp/800/82/r3/final), and the authority direction used for the high-impact designation. This is original evidence-planning guidance, not reproduced overlay text or a high-impact, safety, tailoring, authorization, or compliance decision.

### 1. High-impact process, consequence, and continuity package

- **Request and owner:** Accountable leadership, OT engineering, operations, safety, asset, service, and continuity owners provide the approved high-impact rationale, physical-process and critical-service boundary, consequence and safety constraints, asset/interconnection map, single points of dependency, emergency operations assumptions, recovery priorities, and accountable-owner record.
- **Validate and limit:** Trace a selected critical process through its supporting asset and interconnection, stated safety constraint, continuity dependency, recovery-owner assignment, and high-impact rationale. This can test whether criticality evidence is traceable; it cannot classify the system, establish operational safety, or prove continuity under real conditions.
- **AI and trigger:** AI may organize supplied dependency and ownership records and flag conflicts for human review. Humans approve designation, recovery priorities, safety constraints, and scope. Refresh before material process, consequence, architecture, emergency-plan, supplier, or authority change.

### 2. Overlay-tailoring and privileged-path package

- **Request and owner:** Security, OT engineering, operations, safety, identity, network, supplier, and change owners provide overlay-use rationale, approved tailoring and inherited-capability assumptions, privileged and remote-access paths, segmented-boundary evidence, maintenance approvals, exception register, and supplier support conditions.
- **Validate and limit:** Sample one privileged or supplier-support path from stated operational purpose through authorization, stated safety and maintenance condition, technical boundary evidence, exception if any, and accountable owner. This can test a bounded evidence chain; it cannot approve access, decide control applicability, or prove all privileged access is appropriately constrained.
- **AI and trigger:** AI may identify missing owner, approval, or expiration metadata in supplied records. Humans authorize access, approve tailoring and exceptions, and decide operational change. Recollect after a privileged-path, segmentation, supplier, exception, or maintenance change.

### 3. Safety-gated assurance, response, and independent-review package

- **Request and owner:** OT operations, safety, security, incident-command, supplier, risk, and independent-review owners provide safety-gated verification approvals, non-disruptive check outputs, incident and safety-escalation handoffs, containment/recovery decision records, remediation and retest evidence, and quarterly review minutes.
- **Validate and limit:** Trace a selected approved assurance activity, incident, or finding from safety gate through result or handoff, human decision authority, assigned corrective action, retest or rationale, and independent review. This can support evidence of governed follow-through; it cannot direct response, establish resilience, or accept residual risk.
- **AI and trigger:** AI may index approved records and flag unassigned or overdue remediation. Humans authorize assurance activity, direct operations and incident response, approve closure, and accept risk. Review quarterly and after an incident, safety concern, failed check, recovery exercise, or material operational change.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
