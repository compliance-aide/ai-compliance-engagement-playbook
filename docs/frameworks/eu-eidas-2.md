# EU eIDAS 2.0 — engagement guide

> Original operational guidance, not an identity-assurance or trust-status claim. Confirm role-specific requirements under the [European Digital Identity Framework](https://eur-lex.europa.eu/legal-content/en/LSU/?uri=CELEX%3A32024R1183).

## Engagement focus

Determine declared organizational role, identity and data flows, accountable owners, onboarding, authentication, consent, interoperability, incident, and service-change evidence.

## Roles

Identity owners operate the service; independent reviewers test flow diagrams and sample access and incident handling. AI maps evidence and identifies stale integrations, but cannot approve assurance, assert legal trust status, or alter credentialing decisions. Review changes quarterly and scope annually.


## Source and applicability

Establish the organization's actual role and intended service before assigning requirements. Retrieve the amended eIDAS Regulation, current implementing acts, applicable national rules and the technical framework/profile used by the implementation. Record each version, legal status, application date and owner decision. Keep wallet provision, attribute issuance, relying-party acceptance and trust services distinct; one role's approval does not establish another's status.

This guide covers identity/wallet workflow evidence. Use the [trust-services guide](eidas-trust-services.md) for service-specific trust-status work where relevant. Do not import a trust-service claim into a wallet deployment merely because both use eIDAS terminology.

## Before starting

Follow the [agent runbook](../agent-runbook.md). Obtain the actor inventory, approved flow diagrams, source and profile versions, trust-source configuration, data attributes, lifecycle policies, QA access and named legal/identity/security owners. Define the permitted test identities, endpoints and recovery boundaries. Do not use real identity documents or production credentials for demonstrations.

## Ordered workflow

| Step | Action and owner | Output and exit condition |
| --- | --- | --- |
| 1. Define roles and use | Legal/identity owners identify actors, service purpose and applicable obligations. | Approved role/source record and unresolved interpretations. |
| 2. Map complete flows | Engineering traces onboarding, issuance, presentation, verification, revocation and recovery. | Versioned data/trust/dependency map with owners for every boundary. |
| 3. Define evidence checks | Security/privacy and service owners state expected observations under the approved method. | Work items with profile, target, period, acceptance criteria and limits. |
| 4. Test authorized QA paths | Testers use synthetic identities and preserved inputs. | Original request, response, user-choice and verifier evidence; failed tools recorded separately. |
| 5. Challenge lifecycle assumptions | Owners evaluate expiration, revocation, device loss, recovery and trust-source changes. | Results for each applicable path; success on issuance does not close recovery or revocation. |
| 6. Remediate and retest | Engineering corrects defects and checks affected flows. | Fresh evidence tied to the changed build/profile and remaining limitations. |
| 7. Review claims and decisions | Authorized owners assess trust/certification and deployment prerequisites. | Reviewable decision package; no inferred legal status from interoperability success. |
| 8. Maintain and hand off | Service owners track incidents, dependencies and source changes. | Exact next checks, status evidence and remediation owners. |

## Evidence and test plan

### Role, trust and configuration

Legal/identity owners supply applicable source decisions; engineering supplies endpoints, profiles, version identifiers and configured trust sources. Compare declared actors and relationships with the observed QA configuration. Record when a trust lookup was performed and what its scope establishes. Do not expose keys or tokens, or treat a reachable endpoint as an authenticated issuer.

### Lifecycle and interoperability

Owners supply approved issuance, presentation, expiration, revocation and recovery procedures. Trace their inputs, state changes and verifier outcomes using synthetic records. Test the applicable profile combinations and disclose untested combinations. A single successful exchange cannot establish cross-border or ecosystem-wide interoperability.

### Incident, change and assurance

Operations supplies event records, escalation decisions, changed trust/configuration records and corrective actions. Reconcile prior tests with changes and reopen affected assertions. Preserve assurance/certification records separately from operational observations. AI can draft the packet; humans approve regulated communications, real credential actions and public claims.

## Failure branches and decisions

- Credential is accepted after its synthetic revocation under a test requiring rejection: retain an adverse result and investigate status freshness and verification logic.
- Revocation service is unavailable: record the observed fallback and compare it with the approved rule; do not invent a fail-open or fail-closed policy.
- Recovery recreates access without the required approved checks: preserve the failure; successful login alone does not establish valid recovery.
- Technical profile changes: identify affected issuer/wallet/verifier combinations and retest them before transferring old results.
- Trust source is stale or inaccessible: keep current trust status unresolved; do not equate historical trust with current authorization.
- Consent screen and transmitted attributes differ: follow the presentation workflow below and preserve both observations.

## Cadence and renewal

Review on the agreed service cadence and after issuer, trust-source, profile, credential-lifecycle, device, security or legal changes. Track certification and operational renewal conditions separately. Maintain event-triggered escalation independently of periodic review.

## Completion and handoff

Deliver the actor/source manifest, complete flow and requirement inventory, profile/configuration records, QA observations, lifecycle limitations, authoritative status references and open actions. Identify exactly which identities and combinations were tested. Independent source, engagement, skeptical and rights review plus named human publication approval remain required. This guide is not proof of certification, legal acceptance or identity assurance.

## Check a wallet presentation from request to received data

The [Commission's EUDI overview](https://digital-strategy.ec.europa.eu/en/policies/eudi-regulation) describes user control over attributes shared with third parties. Treat that as context; retrieve the applicable legal and technical provisions before setting formal acceptance criteria. The [architecture framework](https://digital-strategy.ec.europa.eu/en/library/european-digital-identity-wallet-architecture-and-reference-framework) is a technical reference whose version must match the implementation. A working demo is not evidence of certification or legal trust status.

Use the [agent runbook](../agent-runbook.md). This is an original QA workflow for an approved test environment, not an identity-proofing procedure.

1. **Name the actors and claim.** Identify wallet provider, issuer, relying party, verifier and user-facing service. Record exact versions and the assertion being checked. Legal/identity owners approve role, required attributes and trust basis.
2. **Prepare synthetic credentials.** Use approved QA identities and test credentials with no real identity documents, signing keys or production identifiers in workpapers. Define permitted endpoint interactions, evidence capture and cleanup.
3. **Record the request.** Capture what the relying party asks for, its authenticated identity as observed under the approved method, the transaction context and the intended purpose. Preserve missing or unexpected attributes for review.
4. **Observe the user's choice.** Compare the request with what the wallet displays and what the user is allowed to approve or decline. Record the actual behavior; a screenshot of a consent screen does not prove what is transmitted.
5. **Inspect the received result.** In the authorized QA environment, compare the presentation received by the relying party with the approved attribute set and user selection. Check the configured verification outcome and its evidence rather than accepting HTTP success as credential validity.
6. **Exercise adverse paths.** Under the approved method, test cancellation, missing required attributes, expired test credentials and unavailable verification dependencies. Define expected outcomes first. Do not manufacture a real identity or bypass production trust checks.
7. **Check downstream handling.** Trace approved logs and storage for the synthetic transaction. Identify unexpected retained attributes or sensitive payload logging and route correction. Successful data minimisation in transit does not establish downstream deletion.
8. **Reconcile and hand off.** Save request, user-visible choice, received attributes, verifier result and downstream observations as linked assertions. Assign defects and retests. Trust/certification, deployment and real credentialing decisions remain with authorized owners.

### Fictional over-disclosure example

The approved QA use case requires only a test age-threshold assertion. The wallet displays that selection, but the relying party's received payload also contains the synthetic full date of birth. The assertion “received only the approved attributes” is `not_supported`; the visible screen alone cannot support it. Engineering traces request construction, presentation generation and receiver processing, then retests. This is a test of the agreed boundary, not a universal rule that every age-related use case must use the same attributes.

If the receiver cannot be inspected, the transmission-content conclusion remains `inconclusive`; a failed inspection tool is `not_tested`. If credentials are rejected, preserve the actual reason and distinguish a correct rejection from a broken verification dependency. Do not label the wallet uncertified or the user fraudulent from an isolated test failure.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
