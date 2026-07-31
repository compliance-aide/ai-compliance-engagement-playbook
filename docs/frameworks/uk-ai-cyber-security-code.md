# UK AI Cyber Security Code of Practice engagement guide

> Original operational guidance, not UK government text, a security determination, a legal interpretation, or a compliance claim. Confirm current material through the [UK AI Cyber Security Code of Practice](https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice) and applicable authority.

## Engagement focus

Maintain an AI-system security lifecycle record that connects intended use, accountable owners, model and data dependencies, environments, supplier and component context, security risks, design and operating evidence, monitoring, incidents, vulnerability handling, changes, retirement decisions, and review dates. Keep model behavior, product claims, and security evidence separate. Record sources, scope, limitations, and human decisions so an assessment can test the system’s security posture without treating an AI-generated analysis as authoritative.

## Roles and annual rhythm

Product, engineering, security, privacy, data, model-risk, legal, procurement, operations, and executive owners retain accountable decisions. System owners maintain lifecycle context; security owners coordinate assurance; data and model owners maintain approved evidence; incident authorities decide escalation; and auditors evaluate evidence in their independent role. Independent reviewers sample lifecycle paths from intended use through dependencies, design, deployment, monitoring, incident handling, change, and retirement, challenging unclear ownership, unmanaged suppliers, stale threat assumptions, and unsupported security claims.

AI may organize authorized metadata, identify missing lifecycle or review fields, compare approved records with retained evidence, draft questions, and prepare non-authoritative workpapers. AI cannot determine model suitability, authorize deployment, select or approve safeguards, decide an incident outcome, make a product-security claim, accept risk, alter evidence, or claim compliance. Reassess before material model, data, component, supplier, deployment, incident, threat, or legal changes; monitor relevant evidence routinely and conduct an annual independent readiness review.


## Tailored evidence plan

**Source and rights snapshot.** Use the current [UK AI Cyber Security Code of Practice record](https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice); checked 2026-07-31. This is original operational planning, not government text, a security conclusion, or a compliance claim. Keep supplier material, exploit detail, credentials, personal data, and production telemetry in approved protected systems; retain only permitted references or redactions here.

### 1. AI security ownership and boundary package

- **Request and owner:** Approved intended-use/misuse records, model/data/component inventories, deployment-boundary diagrams, dependency and supplier records, threat/risk decisions, and accountable assignments from product, engineering, security, data, and procurement owners.
- **Validate and limit:** Trace one selected AI service from intended use through dependencies, environment boundary, threat decision, and review date. This supports bounded traceability; it cannot establish model safety, inventory completeness, or acceptable risk.
- **AI and trigger:** AI may index authorized metadata and flag missing owners, review dates, or dependency links. Humans approve architecture, safeguards, and risk treatment. Refresh after material model, data, component, supplier, deployment, or threat change.

### 2. Secure lifecycle and response package

- **Request and owner:** Authorized design/security reviews, change/release approvals, test outputs, access/configuration evidence, vulnerability and incident records, and remediation/retest evidence from engineering, security, and operations owners.
- **Validate and limit:** Follow one selected change, vulnerability, or incident through human triage, authorization, corrective action, and retest. This demonstrates that path only; it cannot prove continuous effectiveness or incident closure.
- **AI and trigger:** AI may create a read-only index and flag missing timestamps or retests. Humans authorize releases, validate findings, declare incidents, and close remediation. Recollect after a material vulnerability, incident, failed test, or emergency change.

### 3. Monitoring, supplier, and assurance package

- **Request and owner:** Monitoring and alert-review records, supplier assurance/change notices, exception register, assurance results, management decisions, and independent-review observations from security, operations, procurement, risk, and audit owners.
- **Validate and limit:** Trace one monitoring exception or supplier change to assessment, escalation, decision, mitigation, and independent challenge. This cannot certify supplier security, approve an exception, or replace assurance.
- **AI and trigger:** AI may identify stale exceptions and draft factual questions. Humans approve supplier decisions, exceptions, external claims, and risk acceptance. Review routinely and conduct an annual independent readiness challenge.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
