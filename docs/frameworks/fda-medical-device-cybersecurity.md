# FDA medical-device cybersecurity — engagement guide

> Original operational guidance for lifecycle work, not FDA regulatory advice or a submission conclusion. See the [FDA cybersecurity resource](https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity).

## Engagement focus

Maintain product and responsibility inventory, safety-cyber risk integration, secure-development and supply-chain evidence, vulnerability triage, patch practice, release/change records, disclosure exercises, and management review.

## Device-version and vulnerability workflow

Use the [agent runbook](../agent-runbook.md). Source checkpoint, 2026-09-04:
FDA's indexed [February 2026 guidance record](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cybersecurity-medical-devices-quality-management-system-considerations-and-content-premarket)
identifies current premarket cybersecurity recommendations; the indexed PDF cover
states it supersedes the June 2025 guidance. Full guidance, section 524B scope,
postmarket requirements and submission-route rules remain unverified in this pass.
Do not treat an older resource-list entry as proof that the superseded edition is
current, or turn guidance recommendations into statutory duties without mapping.

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

**Failure branches:** unknown component version leaves applicability
`inconclusive`. An unavailable bench configuration is `not_tested`. A delivered
update with the old version still observed is `not_supported` for installation.
Neither a technical finding nor an agent's score decides a clinical action.

**Fictional desk case:** a QA update server reports all packages delivered, but
one synthetic device record still shows the vulnerable firmware after reboot.
Delivery and installation are separate assertions; installation is
`not_supported` against the approved target-version criterion. Safety impact and
field action remain owned decisions. No real medical device was tested or updated.

## Roles and annual rhythm

Product owners make safety, release, and regulatory decisions. Independent reviewers test selected lifecycle trails and escalation. AI can link evidence and detect gaps, but cannot make patient-safety, submission, clinical, vulnerability-disclosure, or release decisions.


## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
