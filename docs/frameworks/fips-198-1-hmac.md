# FIPS 198-1 HMAC engagement guide

> Original operational guidance, not FIPS content, HMAC implementation instructions, a cryptographic approval, a validation claim, or a compliance claim. Confirm current status and successor guidance through [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) and the organization’s approved security, cryptography, architecture, legal, and operational decisions.

## Engagement focus

Manage the approved use of keyed-hash message authentication across in-scope applications, interfaces, APIs, services, devices, and suppliers. Maintain traceability from business purpose and protected message flow to owner, implementation or module, key lifecycle reference, verification behavior, deployment environment, change history, exceptions, and current standards-status review. A passing test, successful verification, or provider statement is evidence to assess; it does not prove secure implementation, correct key handling, complete coverage, validation, or compliance.

## Source and applicability

The [NIST publication record](https://csrc.nist.gov/pubs/fips/198-1/final), read 2026-09-04, contains a June 2025 notice of a proposed withdrawal and movement of content to SP 800-224. That notice alone does not prove withdrawal or a successor's final effective status. Verify both publication histories and current algorithm guidance before making migration decisions. Full standard and successor-status reconciliation remain pending. HMAC authenticates messages using a shared secret; it does not encrypt their content or independently establish which key holder created a message.

## Roles

Cryptography and security owners approve design and parameters. Application/API owners define authenticated content and replay policy. Key-management owners control secret lifecycle. Independent reviewers challenge source and evidence coverage. AI may reconcile authorized metadata and draft workpapers; it cannot create or access secrets, change production cryptography, approve exceptions, decide migration timing or attest to compliance.

## Before starting

Record each message flow, producer, verifier, purpose, approved hash/tag parameters, key identifier, implementation build and input encoding. Define what content and context the tag covers and what happens on verification failure. Use the [agent runbook](../agent-runbook.md) and authorized synthetic QA messages; real shared secrets and sensitive payloads stay outside this repository.

## Ordered workflow

1. **Map uses and trust boundaries.** Reconcile every in-scope producer/verifier pair and its approved purpose. Output a use register. A verified tag is not automatic permission to execute any action named in the message.
2. **Define authenticated bytes and context.** Record serialization, field ordering, encoding, method/path/context coverage and any truncation. Output an input contract. Required fields outside the authenticated content must not silently inherit protection.
3. **Trace implementation and key selection.** Match actual builds, algorithm/tag configuration and key-version identifiers to approved baselines. Output a deployment map without key material. Shared key possession is a separate access-governance concern from mathematical tag correctness.
4. **Evaluate computation in QA.** Use authoritative vectors appropriate to the approved parameters, plus application-specific cases for altered content, wrong key, malformed or missing tags. Preserve expected/actual results and untested paths. Output a test matrix; a valid tag from one test does not prove full implementation correctness.
5. **Observe acceptance and replay handling.** Test the complete consuming decision against the approved policy, including duplicate or stale messages where replay prevention is required. Output distinct tag-verification and freshness/authorization outcomes. A replayed message can have a valid tag while violating the application's acceptance rule.
6. **Check lifecycle and failure behavior.** Trace key rotation, accepted key versions, retirement and unavailable key-service behavior to owner-approved rules. Record producer/verifier coordination and explicit errors. Output gaps; a secret lookup failure must not become an empty/default key or unauthenticated success.
7. **Review changes and hand off.** Reconcile updated serialization, keys, parameters or libraries with every affected peer. Preserve failures and assign retests. Output bounded conclusions separating computation, content coverage, freshness, key governance and authorization.

## Failure branches and decisions

Unavailable runtime evidence is `not_tested`; uncertain successor applicability is `inconclusive`. An observed duplicate execution contrary to a defined replay criterion is `not_supported` even when tag verification succeeds. Preserve both outcomes and route design changes to qualified owners.

Fictional desk case: an approved QA request is delivered twice with the same valid tag, and the application executes an operation twice despite its defined single-execution policy. Tag verification is `supported`; replay handling is `not_supported`. The agent records both executions without claiming HMAC itself failed or changing a real account.

## Cadence and renewal

Reassess after source-status, parameter, producer/verifier, key-policy, input-contract or provider changes and after authentication incidents. Use approved organizational schedules rather than invented quarterly checks or annual FIPS renewal. Assign an owner for successor-source verification and coordinated migration.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
