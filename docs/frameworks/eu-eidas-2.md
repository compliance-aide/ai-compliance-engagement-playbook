# EU eIDAS 2.0 — engagement guide

> Original operational guidance, not an identity-assurance or trust-status claim. Confirm role-specific requirements under the [European Digital Identity Framework](https://eur-lex.europa.eu/legal-content/en/LSU/?uri=CELEX%3A32024R1183).

## Engagement focus

Determine declared organizational role, identity and data flows, accountable owners, onboarding, authentication, consent, interoperability, incident, and service-change evidence.

## Roles and annual rhythm

Identity owners operate the service; independent reviewers test flow diagrams and sample access and incident handling. AI maps evidence and identifies stale integrations, but cannot approve assurance, assert legal trust status, or alter credentialing decisions. Review changes quarterly and scope annually.


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
