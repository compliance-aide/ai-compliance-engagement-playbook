# HHS HICP 2023 — healthcare cybersecurity engagement guide

> Original operational guidance, not HHS content, clinical advice or cybersecurity assurance. Draft pending independent source, skeptical and rights review.

## Source and applicability

Use the [HHS HICP resource](https://hhscyber.hhs.gov/cornerstone-hicp.html) and its authorized publication links. Official indexed material describes the 2023 edition's main publication and two technical volumes, addressing organizations of different sizes. HHS describes HICP as voluntary recommendations; do not equate participation with HIPAA compliance or certification.

Source limitation: official resource descriptions were located; the full 2023 main document, technical volumes, subsequent updates and applicable organizational obligations remain unverified. Confirm the correct edition and technical guidance for the actual organization before mapping practices. The following are original evidence-management procedures, not clinical instructions or reproduced HICP requirements.

## Engagement focus

Connect adopted cybersecurity practices to actual care-delivery dependencies and operating evidence. Separate restored infrastructure from usable clinical services, and cybersecurity observations from patient-safety decisions. A successful backup job does not establish that care can resume.

## Roles

Clinical leadership owns care priorities and safety decisions. IT, biomedical engineering, facilities and security own their respective systems and evidence. Incident command directs response. Privacy/legal authorities determine notifications and obligations. An independent reviewer challenges evidence and exercises; leadership approves risk, resources and final decisions.

AI may reconcile authorized records, flag gaps and draft workpapers. AI cannot diagnose, operate medical devices, direct clinical or incident response, authorize disruption, decide notifications or certify safety. Use synthetic data and approved QA/exercise environments; production device testing requires separately authorized clinical and technical scope.

## Before starting

Apply the [agent runbook](../agent-runbook.md). Record organization/services, locations, adopted source versions, owners, evidence permissions and exercise boundaries. Obtain clinical-approved critical dependencies, downtime arrangements, escalation contacts and test stopping conditions. Missing safety authority blocks dependent testing, not independent record review.

## Ordered workflow

1. **Define scope and practices.** Owners select applicable guidance and distinguish voluntary adoption, internal policy and legal/contractual duties. Output: source/practice register with explicit owners and unresolved applicability.
2. **Map care dependencies.** Reconcile services with IT, devices, identity, communications, facilities and suppliers. Include downtime and recovery dependencies. Output: complete scoped dependency register; AI does not assign clinical priority.
3. **Bind operational evidence.** Link each adopted practice to actual implementations, workforce responsibilities, vendors, period and evidence. Output: manifest with missing systems and unavailable records retained.
4. **Prepare approved tests.** Define expected operational outcomes, safe fixtures, observers, escalation and stop conditions. Output: signed or otherwise authorized test/exercise plan. A tabletop establishes discussion evidence, not restored-system performance.
5. **Observe service outcomes.** Record detection, escalation, technical recovery and the designated clinical owner's service-acceptance observation separately. Output: timed results with explicit untested dependencies and no unsupported safety claim.
6. **Reconcile improvements.** Track findings through accountable decisions, funding, action and retest. Preserve blocked remediation and compensating measures without changing failures to passes. Output: current improvement register.
7. **Review and hand off.** Give the reviewer full results and disagreements. Route clinical, incident, legal and resource decisions to their designated owners. Output: bounded readiness report with next actions and evidence limits.

## Evidence and test plan

### Care-delivery dependency and risk package

Restore PR340's package with complete scoped service coverage. Clinical operations, biomedical engineering, facilities and IT provide service maps, assets, owners, downtime assumptions, supplier dependencies and escalation records. Reconcile all included locations and shifts. One department's successful exercise cannot establish hospital-wide resilience.

### Protective operations and incident-readiness package

Security, IT, biomedical and incident owners supply access/change records, maintenance evidence, monitoring coverage, exercises, vendor arrangements and corrective actions. Trace alerts to actual receipt and accountable action. Track unreachable systems separately from clean results. For recovery, retain required data-point/time criteria, restored dependencies and observed service outcome; do not infer recovery from server startup alone.

### Governance, workforce and improvement package

Leadership, HR, privacy/legal and review owners provide adopted practices, training populations, exercise observations, risk decisions and remediation/retests. Reconcile workforce coverage including relevant contractors and changing roles. Course completion proves participation, not operational competence by itself. Preserve each known action and service impact, including deferred work and its decision owner.

For each test record criterion/source, approved expectation, environment, scope, actual outcome, time, observer and limitation. Maintain the complete known service/asset population and all gaps; technical test selection cannot silently remove untested services from the record. Keep patient information and confidential incident records out of this public project.

## Failure branches and decisions

- Clinical or device testing authority absent: do not perform the dependent action; record the owner and continue safe evidence review.
- Systems restored but critical dependency unavailable: keep infrastructure success separate from failed service-restoration criteria.
- Exercise contact cannot be reached: record the failed handoff and fallback outcome, not a completed notification.
- Medical-device change requires vendor/clinical review: retain the remediation constraint and escalation; do not force an unsafe patch to close a finding.
- Legal duty unclear: preserve known facts and promptly route to counsel/incident authority; voluntary guidance does not settle a statutory obligation.

Fictional desk case: an exercise restores a records server, but the approved end-to-end test cannot retrieve records because identity service remains down. Server recovery is supported; the service-restoration criterion is not_supported. Patient safety is not determined by this example.

## Cadence and renewal

Use documented obligations, owner-approved operating schedules and risk-based exercise plans. Reopen affected work after service redesign, new devices, supplier changes, incidents, failed exercises or updated guidance. Do not invent a universal HICP quarterly assessment or annual certification cycle. Verify remediation against the affected service before closing it.

## Completion and handoff

Deliver the adopted-practice register, complete dependency population, operational evidence, approved exercises/results, findings, constraints, disagreements and named next owners. Classify assertions supported, not_supported, inconclusive, not_applicable or not_tested. Keep clinical acceptance, legal compliance and cybersecurity evidence separate. No actual clinical exercise, medical-device operation or patient assessment occurred in drafting this guide.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) and [agent runbook](../agent-runbook.md). Clinical and external decisions require explicit authority and their own verified records.
