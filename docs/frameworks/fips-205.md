# FIPS 205 post-quantum hash-based signature engagement guide

> Original operational guidance, not SLH-DSA implementation instructions, certification, legal advice or permission to sign. Draft pending independent source, skeptical and rights review.

## Source and applicability

Start with the [NIST publication record](https://csrc.nist.gov/pubs/fips/205/final) and [FIPS 205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf), published August 13, 2024. Read current updates and the applicable contract before concluding this algorithm is required for a particular system.

SLH-DSA is a stateless hash-based signature scheme. Section 10 distinguishes pure and pre-hash signing and verification; the context maximum is 255 bytes. Section 11 distinguishes parameter sets designed for smaller signatures (s) or faster signing (f). Record the exact approved choice, not merely “post-quantum.” These observations do not establish a performance guarantee or equivalence to an older SPHINCS+ implementation.

This draft used the publication record, announcement and selected sections 10–11 passages. Full-standard, current implementation-validation and protocol review remain outstanding. The following evidence procedures are original recommendations for an engagement, not additional FIPS requirements.

## Engagement focus

Verify that the approved signature mechanism reaches every intended consumer and protects the exact content the consumer acts on. Assess suitability, algorithm behavior, deployed implementation, signer authorization and migration completion as separate claims. Keep unsupported claims visible even when a request completes successfully.

## Roles

A service owner owns the use inventory and business criteria. A qualified cryptography owner selects parameters, variant and implementation. Platform and application operators collect QA evidence. Identity owners confirm signer permissions. Legal and change authorities own their respective decisions. An independent reviewer challenges scope, source interpretation and results.

AI may reconcile non-secret inventories and supplied results, draft workpapers and flag missing evidence. AI cannot design cryptography, select parameters, access private keys, sign as a user, accept risk, approve production changes, attest or replace independent review. Tests use approved tools and authorized QA identities only.

## Before starting

Use the [agent runbook](../agent-runbook.md) to record authority, source editions, environment, evidence handling, owners and stop conditions. Identify all signing and verification routes, including external recipients, offline verification, software distribution, queues, archives and recovery. Do not assume all these routes exist; reconcile the actual population and document exclusions.

Obtain the approved message/encoding contract, context, algorithm identifiers, parameter set, pure/pre-hash choice, applicable pre-hash details, public-key references and recipient authorization rules. Unknown choices block dependent tests, not unrelated inventory work.

## Ordered workflow

1. **Establish the purpose and population.** Map each signed artifact to its producer, consumers, owners and authorized action. Reconcile inventory differences. Output: complete route register with unresolved entries retained.
2. **Bind the deployed implementation.** Record actual build, provider/module, configuration and algorithm identifiers on both sides. Separate installed capability from observed use. Output: build-bound integration matrix and evidence for any required validation claim.
3. **Approve the test contract.** Record exact signed content, context bytes, expected interpretation and acceptance/rejection criteria. A qualified owner supplies authoritative vectors and independent expected results. Output: case manifest; never infer conformance solely from a same-library round trip.
4. **Test the signature path.** In authorized QA, exercise valid fixtures and alterations to content, context, public key and signature. Record verification result, API result and business action separately. Confirm the bytes verified correspond to the content displayed or executed. Output: reproducible evidence per case and explicit missing coverage.
5. **Test operational suitability.** Exercise the approved workload and actual transport/storage chain. Measure payload size, encoding expansion, latency, queue behavior and resource limits against owner-approved criteria. Include errors, timeouts and unsupported consumers. Output: route-specific results; the s/f label alone cannot prove suitability.
6. **Test transition and recovery.** Distinguish new signing from historical verification. Exercise approved peer combinations and key transitions, preserving identifiers and evidence needed for old artifacts. Observe any fallback and verify rollback under the approved policy. Output: migration states per route, not a single organization-wide toggle.
7. **Classify and prepare decisions.** Use supported, not_supported, inconclusive, not_applicable or not_tested for each bounded assertion. Keep failures separate from uncertain neighboring claims. Output: review packet and named decision owners; delivery is not approval.

## Evidence and test plan

### Package A — signature route and dependency register

For every route retain purpose, owner, artifact representation, context, variant/parameters, producer/consumer builds, public-key reference, required authority, dependencies, source references, period and coverage status. Reconcile application, job and distribution records against owner attestations. No silent evidence sampling or deletion; record every known gap and its impact.

### Package B — cryptographic and application results

Each case records criterion, fixture reference, independently approved expected outcome, implementation identity, actual result at each layer and evidence location. Include malformed or truncated input, context byte-length boundaries, wrong-purpose signatures and service failures. Distinguish an invalid signature from inability to run verification. Keep private keys, seeds, sensitive content and customer records out of this public repository.

### Package C — operational migration and lifecycle

Maintain the peer/workload matrix, transport limits, retries, monitoring, failure ownership, key-transition decisions and rollback evidence. “Stateless” does not excuse key custody, access management or operational records. Do not import a stateful-signature counter procedure without an applicable source. Preserve historical artifact metadata; current signer permissions alone do not establish historical authority. Record actual readiness and untested combinations without silently capping the population.

## Failure branches and decisions

- A signature is generated but rejected by a gateway limit: classify the delivery criterion as not_supported; do not claim migration completion from signing success.
- A consumer accepts only a legacy fallback: record that actual mechanism and compare it with the approved acceptance policy. Successful business processing is not proof SLH-DSA was used.
- Variant, identifier or context mismatch: stop the affected acceptance claim. Do not silently change the context, retry alternate algorithms or invent a multi-signature acceptance rule.
- Verification errors or times out: retain the error and test the approved failure behavior. Absence of rejection is not a valid signature result.
- A valid signature triggers an unauthorized action: separate cryptographic validity from failed authorization. Route the latter to its accountable owner.

Fictional desk case: signing passes approved vectors, but a distribution service truncates the signature and labels the package delivered. Algorithm-test evidence remains bounded to its vectors; end-to-end distribution is not_supported. Recipient verification is not_tested until it is actually observed. This example is not an executed test.

## Cadence and renewal

Record an owner-approved cadence based on obligations and risk, with event-driven review for source, build, provider, key, protocol, consumer or workload changes and incidents. Do not invent a FIPS annual renewal or quarterly assessment requirement. Recheck affected routes after remediation; a ticket closure is not proof of recovery.

## Completion and handoff

Deliver source versions, full inventory, approved integration/test contracts, results, gaps, exceptions, remediation owners, reviewer disagreements and requested decisions. State precisely which routes support which claims. Keep this guide drafted until independent review and rights confirmation are recorded. No certification, deployment, legal effect or risk acceptance follows from a completed workpaper.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) and [agent runbook](../agent-runbook.md). Preserve the distinction between task progress, evidence status and permission to act.
