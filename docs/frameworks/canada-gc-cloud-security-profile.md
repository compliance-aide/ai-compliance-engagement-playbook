# Canada GC cloud-security profile engagement guide

> Original operational guidance, not Government of Canada profile content, a provider certification or authorization to operate.

## Source and applicability

Read the [GC cloud security profile](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/cloud-services/government-canada-security-control-profile-cloud-based-it-services.html), including its notice to readers, and [ITSP.50.103](https://www.cyber.gc.ca/en/guidance/guidance-security-categorization-cloud-based-services-itsp50103). Checked 2026-09-04. The GC page says its Appendix A has been replaced by the Cyber Centre Medium Cloud Control Profile in ITSP.50.103 Annex B. Providers with authorizations under Appendix A version 1.1 must obtain transition information from the Cyber Centre. Do not treat that old appendix as the current control list or invent a migration deadline.

The GC page describes a Protected B, medium integrity, medium availability context and retains departmental accountability. Provider assurance is an input to the department's service assessment and authorization, not a substitute. ITSP.50.103 connects categorization with profile and cloud-model selection. Obtain the department's approved category, current profile and applicable direction; neither a provider's marketing label nor this guide selects them.

## Engagement focus

Maintain a traceable record from business information and service boundaries to approved requirements, provider/customer responsibility, operating evidence, gaps and the department's authorization decision. Preserve separate status for the provider offering, the configured tenant and the deployed departmental application. A result for one does not automatically cover the others.

## Roles

The service owner owns the business boundary and decision queue. Security and information owners confirm categorization and profile selection through departmental processes. The cloud architect and operators document the actual service and configuration. Procurement and provider relationship owners obtain contract and assurance records. Privacy and records owners address their respective obligations. Reviewers challenge evidence and inherited assumptions. The delegated authorizing official makes the operational decision. AI organizes permitted evidence and drafts questions; it cannot decide data suitability, accept risk, authorize service use or deploy production.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Name the department, service, tenant, provider offering, region, environment and decision being supported. Confirm authorized handling locations before collecting evidence. Create bounded work items with input links, owner, output and exit condition. Obtain approved categorization, profile/version, architecture, contract, responsibility assignments and any prior authorization. Record each missing input and block dependent conclusions, while continuing independent preparation. Keep restricted provider reports, customer data and credentials out of this public repository.

## Ordered workflow

| Step | Action and owner | Output and exit check |
| --- | --- | --- |
| 1. Establish category and version | Security/service owners supply the approved categorization and current profile. For legacy Appendix A evidence, obtain the applicable transition direction and record its owner. | Applicability and version record. An unresolved migration question remains visible and cannot be treated as grandfathered approval. |
| 2. Reconcile the service boundary | Architect and data owners trace data, administration, integrations, backup and external dependencies against the actual tenant/service inventory. | Versioned boundary and discrepancy list. Each included service, region and interface has an owner; omissions require investigation. |
| 3. Allocate responsibilities | Security, provider and customer owners work through the complete approved profile and identify who implements, operates and supplies evidence for each requirement. Split shared responsibilities into concrete tasks. | Complete responsibility register with accepted allocations and unresolved disputes. “Shared” alone is not an assignment. |
| 4. Examine provider evidence | Relationship owner obtains authorized assurance artifacts. Reviewer checks exact offering, service scope, period, exclusions, customer obligations and outstanding limitations against the intended dependency. | Provider reliance workpaper with evidence links and gaps. Brand-level assurance cannot establish coverage for every product or region. |
| 5. Examine customer operation | Operators supply dated configuration and operating evidence. Reviewer compares actual behavior with the customer's allocated requirements and provider assumptions. | Customer workpapers linked to every requirement disposition. Provider evidence cannot close an unimplemented customer task. |
| 6. Correct and retest | Assigned owners plan remediation; separately authorized implementers make changes. Reviewer verifies results and checks affected dependencies. | Finding/action/retest chain retaining adverse observations and remaining limitations. A promised fix is not closure. |
| 7. Prepare authorization inputs | Coordinator reconciles category, profile, provider reliance, customer assessment, open risks and proposed conditions into the exact decision packet. | Versioned packet for the named official. Missing evidence and dissent remain explicit; no generated authorization claim. |
| 8. Verify the recorded decision | Authorized owner records the actual decision and conditions in the departmental system. Coordinator reads back the scope, approved version, conditions and dates. | Decision receipt distinct from assessment completion. Production connection or deployment follows its own approved release process. |
| 9. Maintain and exit | Service owner monitors changes, incidents, evidence expiry and decision conditions. Reassess affected requirements. For retirement, obtain the approved export, retention and disposal plan and verify resulting records. | Monitoring/renewal queue or verified exit record, with unresolved dependencies and next owners. |

## Evidence and test plan

These original examples help build workpapers; they are not a substitute control catalog. Reconcile coverage against the complete approved profile. Preserve all evidence supplied to an assessment scorer; record any test population and untested coverage separately.

| Package and owner | Verification task | Limitation to retain |
| --- | --- | --- |
| Boundary and shared responsibility — architect/service owner | Trace a service interface through its data path, identity dependency, provider/customer tasks and evidence locations. Reconcile discovered dependencies with the full inventory. | A selected trace does not prove no other interface exists. Record inventory discrepancies and unowned tasks. |
| Provider assurance — relationship owner/reviewer | Compare scope and period with the actual subscribed offering and intended reliance; track exceptions and customer-side assumptions. | A current report can still exclude this service or operation. Restricted reports must stay within authorized access terms. |
| Customer configuration — operators | Compare approved configuration with observed settings and retained operation records for access, logging and other allocated requirements. | A template or screenshot from QA cannot establish the production tenant's configuration. Do not alter production under this guide. |
| Recovery and incident dependencies — service/security owners | Trace an approved exercise or actual event through provider escalation, customer response, recovery evidence and corrective actions. | A contractual recovery target does not demonstrate achieved recovery. A simulated result must be labelled as such. |
| Change and authorization conditions — coordinator | Trace one material change or breached condition through impact review, reassessment, decision and destination record. | Ticket closure cannot extend authorization or erase a condition. Verify the actual decision scope. |
| Exit and retention — records/service owners | Reconcile approved export/disposal instructions with retained export checks, provider confirmation and remaining copies/dependencies. | A cancellation notice is not evidence that data was exported successfully or all required disposal occurred. |

Each workpaper contains a requirement reference, owner, source, collection date, covered period, evidence location, expected and actual observation, limitation, reviewer decision and follow-up. Clearly distinguish a missing artifact, a failed observation, a disputed interpretation and a completed administrative task.

## Failure branches and decisions

- **Legacy profile only:** preserve its version and existing authorization scope; obtain the transition decision. Continue inventory work but leave current-profile sufficiency unresolved.
- **Wrong tenant, region or service:** stop affected collection, identify the correct boundary and reassess which evidence remains usable. Never relabel another environment's evidence.
- **Unassigned shared responsibility:** split the task into provider and customer actions and route acceptance to their accountable owners. Do not default it to satisfied.
- **Provider evidence unavailable or restricted:** record the required scope/period and request permitted access or an approved alternative from the relationship owner. Do not bypass restrictions or claim equivalence without reviewer judgment.
- **Failed customer setting or provider exception:** retain the finding, affected requirements and decision impact; assign correction and retest. Risk acceptance is separate from effective implementation.
- **Material incident or expired condition:** escalate to the service/security owner and delegated authority, preserving incident and decision clocks. Do not invent grace periods or renew authority automatically.
- **Interrupted operation or unclear write result:** preserve the last completed step, versions and pending decision; read back the destination before retrying. Do not infer deployment or approval from a click.

## Cadence and renewal

Use actual authorization conditions, evidence periods, contractual commitments and departmental requirements. The engagement owner sets internal reminders early enough to obtain replacement evidence and remediate gaps. Revisit scope/profile assumptions after material data, service, region, provider or threat changes. Do not invent a universal annual certification or transition deadline.

## Completion and handoff

A preparation packet includes approved categorization/profile version, resolved or flagged transition questions, service boundary, complete responsibility and requirement registers, provider reliance and customer workpapers, open findings, retests, decision questions and monitoring owners. List missing items explicitly. A recorded authorization and any production deployment are separate milestones with their own authority and readback. Handoff gives the next action, owner, due date and evidence pointer for every unresolved dependency.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for shared applicability, authority, evidence, technical-test, exception, source-change and renewal requirements.
