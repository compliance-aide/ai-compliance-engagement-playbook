# FIPS 203 post-quantum key-encapsulation engagement guide

> Original operational guidance, not FIPS content, ML-KEM implementation instructions, a cryptographic approval, a validation claim, or a compliance claim. Confirm current requirements and errata through [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) and the organization’s approved security, cryptography, architecture, legal, and operational decisions.

## Engagement focus

Operate a governed inventory-and-migration process for in-scope key-establishment uses that may adopt FIPS 203. Connect business and data-protection needs, protocols and applications, dependencies, cryptographic-module and provider versions, migration design, interoperability and performance testing, rollout approvals, exceptions, rollback readiness, and lifecycle evidence to accountable owners. A vendor announcement, lab result, or enabled setting is evidence to assess; it does not prove a deployment is suitable, interoperable, validated, quantum-safe in context, or compliant.

## Source and applicability

The [NIST publication record](https://csrc.nist.gov/pubs/fips/203/final), read 2026-09-04, identifies ML-KEM as a key-encapsulation mechanism for establishing a shared secret, with ML-KEM-512, -768 and -1024 parameter sets. It also links a November 2025 potential-correction notice. Full standard, errata, current KEM-use guidance and applicable protocol specifications remain to be verified. Key establishment is not itself data encryption, a digital signature or proof of peer authorization.

## Roles

Cryptography and architecture owners approve parameter sets and protocol integration. Application, platform and supplier owners provide actual implementation and interoperability evidence. Security and business owners define migration scope and risk. Independent reviewers challenge claims. AI organizes authorized metadata; it cannot generate or access secret keys, design cryptography, approve migration, deploy production changes or attest to compliance.

## Before starting

Record the protected use, data lifetime, peers, actual protocol, parameter set, implementation versions, module claims and approved migration design. Separate experimental, QA and production scope. Use the [agent runbook](../agent-runbook.md) with authorized synthetic tests and no real key material in public workpapers. Define expected negotiation, failure and rollback behavior before observing results.

## Ordered workflow

1. **Inventory key-establishment dependencies.** Reconcile every in-scope client, server, intermediary and provider with its use, owner and current mechanism. Output a dependency map; a vendor's support announcement does not establish deployed use.
2. **Approve the integration contract.** Obtain exact protocol/version, parameter set, peer-authentication method and any hybrid construction from qualified owners and authoritative specifications. Output a design/source register. Do not invent a hybrid combiner or treat a prerelease implementation as interchangeable with the final standard.
3. **Identify the executed baseline.** Link binaries, libraries, settings and peer capabilities to actual environments. Output a manifest. Configuration offering ML-KEM is distinct from a connection negotiating it.
4. **Prepare layered QA evidence.** Separate algorithm-level vectors, protocol interoperability and application outcomes. Define positive, unsupported-peer, malformed-input and interrupted-exchange cases under the approved specifications. Output a full test matrix; do not prescribe a generic decapsulation error behavior without checking the standard's handling requirements.
5. **Observe negotiated protection.** Record the mechanism and parameters actually used, peer-authentication outcome and successful protected application exchange. Preserve failures and fallback paths without logging secrets. Output session-specific evidence; an established shared secret alone does not prove the intended peer or application policy.
6. **Check migration and rollback.** Test approved behavior across old/new peers and relevant network constraints. Record which paths fall back and whether policy permits it. Output bounded compatibility results; service availability after fallback does not establish post-quantum protection on that path.
7. **Review claims and next actions.** Reconcile all scoped peers, exceptions, version changes and observed outcomes. Assign remaining gaps and required retests. Output a draft rollout packet for the authorized owner, not a blanket quantum-safe or validated-system claim.

## Failure branches and decisions

Unobserved negotiation is `not_tested`; unresolved protocol or errata applicability is `inconclusive`. A connection falling back against a predefined ML-KEM-required policy is `not_supported` even if its application request succeeds. Keep functional availability and required mechanism use separate.

Fictional desk case: a QA server offers the approved mechanism, but a client negotiates a legacy path and completes its request. Server capability and request completion are `supported`; required-mechanism use for that session is `not_supported`. The agent records negotiation evidence without disabling fallback or changing production policy itself.

## Cadence and renewal

Reassess after standard/errata, protocol, parameter, implementation, peer or provider changes and consequential failures. Use approved organizational review schedules rather than invented quarterly checks or annual FIPS renewal. Assign owners for remaining legacy paths and migration exceptions.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
