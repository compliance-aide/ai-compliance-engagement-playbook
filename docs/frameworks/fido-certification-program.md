# FIDO certification program — engagement guide

> Original operational guidance, not FIDO criteria or certification claim. Consult [FIDO certification](https://fidoalliance.org/fido-certification-/).

## Engagement focus

Maintain authentication product, exact certification claim, product/version, procurement, directory validation, enrollment, recovery, loss, phishing, test, vendor, and claim evidence.

## Source and applicability

Start at the [current certification collection](https://fidoalliance.org/fido-certification/) and select the exact product/program path before collecting evidence. Official indexed [functional certification guidance](https://fidoalliance.org/certification/functional-certification/) checked 2026-09-04 distinguishes conformance testing, interoperability, applicable authenticator security requirements, submission and trademark permissions. Full current program policy, product-specific requirements and directory records remain to be verified. Do not apply an authenticator process to every server, identity-verification or device-onboarding product.

## Roles

Product and engineering owners identify the implementation and test baseline. Certification owners coordinate with FIDO and any applicable laboratory. Procurement owners verify acquired products; identity owners validate deployment behavior. Legal and marketing approve claims and marks. Independent reviewers challenge source applicability, evidence completeness and unsupported claims. AI organizes evidence and flags mismatches; it cannot sign agreements, spend money, submit certification requests, grant account access or assert certification.

## Before starting

Record whether this is vendor certification preparation or buyer/deployer verification. Identify legal manufacturer, product/model, firmware/software build, program, intended claim, supported configuration and owner. Obtain current policy and source identifiers. Use the [agent runbook](../agent-runbook.md) with approved QA accounts and synthetic identities; keep credentials, private keys and identifiable recovery records out of this repository.

## Ordered workflow

1. **Select the exact route.** Map product function to the applicable current program and requirements. Output a source/scope record. Resolve uncertain program applicability before scheduling dependent certification activity.
2. **Freeze the evidence baseline.** Link product identifiers, build, hardware/configuration where relevant, test tooling versions and intended deployment. Output a baseline manifest. A later build is not automatically covered by results from an earlier build.
3. **Verify claimed status.** For a buyer, reconcile the exact product with authoritative directory/certificate evidence and lookup date. For a vendor, distinguish planned, tested, submitted and granted states. Output a claim register; passing a test tool does not grant certification.
4. **Prepare required evaluation evidence.** Under the selected program's current rules, identify prerequisites, authorized test routes, evaluation owners and submission artifacts. Preserve all required cases, failures and exclusions. Output a readiness packet; no legal signature, payment or external submission occurs merely because the packet is ready.
5. **Test deployment separately.** In approved QA, define expected enrollment, authentication, credential loss, recovery and fallback behavior. Record the relying party, browser/platform, authenticator, policy and observed result. Output a deployment matrix. Product certification does not establish the security of the organization's recovery process.
6. **Reconcile changes and failures.** Link each failed case to its cause, owner, correction and retest on the relevant baseline. Assess firmware, platform, relying-party and recovery-policy changes against both certification scope and deployment tests. Output open actions rather than silently inheriting older results.
7. **Review the exact claim.** Match proposed wording to the product, program, level if applicable and current evidence. Verify trademark permission separately. Output an approved claim only through the named human process; an evidence index or submitted application is not a certificate.

## Evidence and test plan

### Product, version and claim package

Product, procurement, security and legal owners provide the complete in-scope product inventory, manufacturer/model identifiers, build records, configuration boundaries, proposed claim wording and authoritative status evidence. Reconcile every claimed product and version. Record the lookup date and exact returned entry; a search snippet, vendor logo or similarly named product is insufficient to resolve a scope mismatch.

Separate the source evidence from its interpretation. Record whether an entry explicitly covers a version, whether coverage is ambiguous or whether supplied evidence names a different version. An inaccessible directory does not establish absence of certification. Keep the claim awaiting review until the authorized owner resolves its scope. Record trademark authorization separately from certification status.

### Enrollment, recovery and loss package

Identity, help-desk, security and privacy owners provide approved binding and recovery procedures, roles, exception rules and redacted support evidence. Define a synthetic QA matrix covering each in-scope enrollment, authentication, loss, recovery and fallback path. Record expected authorization, actual behavior, evidence identifiers and unperformed cases. Reconcile all routes; success on the usual login path does not cover recovery or privileged exceptions.

Trace the recovered account, newly bound credential and previous credential state separately. Verify the intended post-recovery access outcome against approved policy rather than assuming every recovery must produce the same revocation behavior. Keep account recovery approval distinct from observed implementation. Clean up QA credentials through the authorized test owner and preserve a non-secret cleanup receipt.

### Deployment, supplier and release package

Engineering, endpoint and supplier owners provide relying-party/application inventories, supported platform combinations, release manifests, integration results, advisories and retirement decisions. Connect each observation to the actual product and policy baseline. When a release changes a relevant component, identify which prior results remain applicable and which require fresh evidence; do not copy an earlier passing row solely because the product name stayed the same.

Reconcile advisories and support changes with deployed inventory and assigned remediation. A vendor release announcement does not prove rollout. A successful installation does not prove the relying party accepts the intended authentication behavior. Preserve separate installation, interoperability and policy-enforcement assertions, including observed failures and provider evidence gaps.

## Failure branches and decisions

Missing authoritative coverage makes certification applicability `inconclusive`; an unperformed integration test is `not_tested`. A demonstrated prohibited fallback under the approved QA criterion is `not_supported` even when the product has a valid certificate. Keep source status, deployment behavior and marketing approval as separate assertions.

Fictional desk case: a listed authenticator is used successfully for QA login, but a lost-device drill permits an unauthorized actor to replace it through a weak help-desk route. The observed login is `supported`; the defined recovery authorization check is `not_supported`. The agent escalates the recovery defect without claiming the product certificate is revoked or the whole deployment is phishing-resistant.

## Cadence and renewal

Use current program maintenance rules and approved institutional schedules; do not invent annual certification renewal or quarterly testing requirements. Recheck after product, configuration, platform, policy, directory-status or vendor changes and before claims or purchases. Record the next owner and trigger.

## Completion and handoff

Deliver the source/program register, product/build manifest, claim-to-status evidence, full QA route matrix, release/advisory reconciliation and open-action register. Identify every unverified directory entry, untested platform and unresolved policy exception. Assign the next owner and review trigger for each gap. Vendor preparation packets must list unmet prerequisites without implying submission or issuance.

Require independent source, skeptical and rights review before publication. Certification decisions belong to the applicable program authority; human owners approve agreements, fees, submissions and marks. State explicitly which deployment outcomes were actually observed. This draft grants no certification and has not evaluated a real product or account.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
