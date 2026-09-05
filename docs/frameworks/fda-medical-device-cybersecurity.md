# FDA medical-device cybersecurity — engagement guide

> Original operational guidance for lifecycle work, not FDA regulatory advice or a submission conclusion. See the [FDA cybersecurity resource](https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity).

## Source and applicability

Use the [agent runbook](../agent-runbook.md). Source checkpoint, 2026-09-04:
FDA's indexed [February 2026 guidance record](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cybersecurity-medical-devices-quality-management-system-considerations-and-content-premarket)
identifies current premarket cybersecurity recommendations; the indexed PDF cover
states it supersedes the June 2025 guidance. Full guidance, section 524B scope,
postmarket requirements and submission-route rules remain unverified in this pass.
Do not treat an older resource-list entry as proof that the superseded edition is
current, or turn guidance recommendations into statutory duties without mapping.


## Engagement focus

Maintain product and responsibility inventory, safety-cyber risk integration, secure-development and supply-chain evidence, vulnerability triage, patch practice, release/change records, disclosure exercises, and management review.

## Before starting

Define manufacturer role, intended use, lifecycle stage, exact device/configuration
population, evidence permissions and safety/quality/regulatory decision owners.
Record each assertion and approved criterion in
[work items](../../templates/work-item.md). Keep patient data, exploit details and
restricted product evidence in approved repositories rather than this public guide.

Distinguish source review, vulnerability triage, authorized bench testing and field
verification. Document the bench setup's representativeness and omissions. An
unavailable device variant remains untested; another model's passing test cannot
silently fill its evidence gap.

## Ordered workflow


1. Record manufacturer responsibility, product/model, intended use, lifecycle stage,
   hardware/firmware/software versions, deployment configuration and support status.
   Regulatory and quality owners determine applicable device and submission scope.
2. Reconcile architecture and component records to the exact build. Link network,
   cloud, mobile, update and third-party dependencies where present. An SBOM for a
   related model or older release cannot establish the current component inventory.
3. Trace each vulnerability observation to component identity/version, configuration,
   exposure path and evidence. Distinguish a package-name match from verified
   affected behavior. Unknown reachability is uncertainty, not proof of safety.
4. Have security and safety owners connect the technical scenario to the device's
   intended operation and safety analysis. Keep technical severity, exploitability,
   clinical consequences and regulatory reportability as distinct decisions.
   A low generic score cannot settle patient-safety impact.
5. Define an approved QA test with a representative nonclinical setup, synthetic
   records and explicit stop conditions. Never probe a patient-connected device
   or operational clinical network during this guide work. Record untested device
   configurations and dependencies rather than extrapolating from one bench result.
6. For a proposed correction, identify all affected supported releases and the
   approved update path. Check authenticity, compatibility, interruption handling,
   resulting version and intended function against owner-approved criteria. A
   downloaded update or successful transfer does not prove installation.
7. Preserve the before/after vulnerability evidence and relevant regression results.
   Quality, safety and regulatory owners decide release and remaining actions.
   A security fix cannot be accepted solely because an exploit no longer works
   if the approved device-function criteria fail.
8. Prepare labeling, support, disclosure and field-action materials only within
   authorized scope. Keep draft, approval, distribution and deployment verification
   separate. Do not notify researchers, clinicians, customers or FDA without
   explicit authorization for that action.
9. Reconcile the complete affected-version population to corrected, unresolved,
   unsupported or otherwise human-dispositioned states. Preserve every limitation
   and owner; no trimming of evidence bound for scoring. A new release does not
   prove the installed fleet received it.

## Failure branches and decisions

 unknown component version leaves applicability
`inconclusive`. An unavailable bench configuration is `not_tested`. A delivered
update with the old version still observed is `not_supported` for installation.
Neither a technical finding nor an agent's score decides a clinical action.

**Fictional desk case:** a QA update server reports all packages delivered, but
one synthetic device record still shows the vulnerable firmware after reboot.
Delivery and installation are separate assertions; installation is
`not_supported` against the approved target-version criterion. Safety impact and
field action remain owned decisions. No real medical device was tested or updated.

## Roles

Product owners make safety, release, and regulatory decisions. Independent reviewers challenge the complete scoped lifecycle record and escalation evidence. AI can link evidence and detect gaps, but cannot make patient-safety, submission, clinical, vulnerability-disclosure, or release decisions.


## Evidence and test plan

Retain these three PR #340 packages with full in-scope coverage. Prior review
of another revision does not approve this guide. Preserve all evidence for scoring.

### 1. Product boundary and safety-cyber risk package

- **Request and owner:** The product and safety owners provide the released-product/version inventory, intended environment and interfaces, software bill-of-material inputs, hazard/risk records, and the human-approved product boundary for the review period.
- **Validate and limit:** Trace all in-scope released versions and interfaces to their risk record, accountable owner, and safety escalation path. This supports lifecycle traceability; it cannot establish that every safety hazard was identified or that a benefit-risk decision is appropriate.
- **AI and trigger:** AI may reconcile supplied inventories and flag a version without a linked owner or risk trail. Product and safety authorities decide scope and safety conclusions. Refresh after a material design, dependency, vulnerability, clinical-use, or field-event change.

### 2. Secure development, supplier, and release package

- **Request and owner:** Engineering and quality owners provide approved development/change records, security test outputs, supplier component assurance inputs, release approvals, and unresolved-security decision records for the approved in-scope release population.
- **Validate and limit:** Inspect provenance, dates, access restrictions, and each in-scope trail from change through test and human release approval. This supports that an accountable trail exists; it cannot prove secure operation, supplier quality, or regulatory sufficiency.
- **AI and trigger:** AI may index authorized records and identify missing joins; it may not change code, approve release, select a test conclusion, or accept a security exception. Recollect before release and following a material supplier, test failure, or design change.

### 3. Vulnerability response and postmarket package

- **Request and owner:** Security, quality, and incident owners provide intake/triage records, impact analyses, coordinated-disclosure records where applicable, remediation and communication decisions, field monitoring, and management review minutes.
- **Validate and limit:** Trace each in-scope vulnerability or field signal to time-stamped intake, assigned authority, evidence, decision, and follow-up. This supports response governance; it cannot decide exploitability, patient impact, reporting, notification, or corrective-action closure.
- **AI and trigger:** AI may de-duplicate authorized tickets and prepare a human review packet. Authorized humans decide disclosure, communications, regulatory contact, and closure. Refresh on a significant vulnerability, incident, recall-related signal, or annual review.


### Component-to-field traceability

Match component identities and versions to the actual build manifest and device
configuration. Preserve aliases, vendor forks and unresolved matches rather than
merging similarly named packages. A vulnerability-database match starts triage;
it does not establish the device's exposure or safety consequence.

Link each risk treatment to an approved requirement, implemented control and
observation. Check the relevant configured interface and update path, not only a
generic component test. Preserve failed and not-run cases alongside passing
results. Have the owner define the permissible inference across configurations.

For authorized update exercises, verify the intended installed version and
approved functional criteria after interruption/recovery scenarios. Record which
security and device-function assertions were tested. A corrected package can
still be unsuitable for an older supported hardware revision; keep compatibility
and vulnerability remediation separate.

Reconcile field-status evidence against the complete affected population defined
by the responsible owner. Distinguish distributed packages, scheduled updates,
verified installations and devices without current observations. Unknown field
status remains visible; absence of incoming complaints does not prove deployment
or absence of risk.

## Cadence and renewal

Recheck after new versions, components, intended environments, threat information,
field signals or changes in support. Use the approved lifecycle and monitoring
schedule rather than inventing universal intervals. Keep unsupported versions and
unreachable field devices in an owned disposition process; an end-of-support date
does not itself prove devices stopped operating.

## Completion and handoff

Deliver the exact product/version boundary, source register, component evidence,
risk/control/test links, findings, authorized decisions, release records and
field-status limitations. Each unresolved item needs an owner and next action.
Separate premarket documentation readiness from postmarket operation and actual
field remediation. Neither is demonstrated by the other alone.

State the evidence scope and untested configurations. Safety, quality and
regulatory authorities retain acceptance, communication and submission decisions.
Independent source, skeptical, rights, publication and cross-model reviews remain
pending; structural checks cannot establish clinical safety or regulatory sufficiency.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
