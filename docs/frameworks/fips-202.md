# FIPS 202 SHA-3 engagement guide

> Original operational guidance, not FIPS SHA-3 content, an algorithm-selection decision, an approval, or a compliance claim. Confirm current material through [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) and the organization’s approved cryptography, security, architecture, legal, and operational decisions.

## Engagement focus

Operate a governed lifecycle for in-scope SHA-3 and extendable-output-function uses. Connect each use case to an approved purpose and scope, protected data and system context, implementation and configuration decisions, protocol, signature, derivation, or randomness dependencies where relevant, interfaces, access, logging, validation, supplier dependencies, changes, incidents, transition planning, and retirement. A configuration extract, implementation record, supplier statement, test result, or audit log is evidence to assess; none alone proves suitable function use, correct implementation, protected data, approved use, secure operation, or compliance.

## Source and applicability

The [NIST publication record](https://csrc.nist.gov/pubs/fips/202/final), read 2026-09-04, identifies four fixed-output SHA-3 hash functions and SHAKE128/SHAKE256 extendable-output functions. It records a March 2025 update decision and an Appendix B typographical correction; neither is evidence of a replacement edition already in force. Full standard, current update status and use-specific guidance remain to be verified. Record the exact function rather than treating every Keccak-related implementation as interchangeable.

## Roles

Cryptography and security owners approve function, parameters and purpose. Application owners define exact inputs, output-length contracts and consuming behavior. Platform and supplier owners provide implementation evidence. Independent reviewers challenge source applicability and conclusions. AI indexes authorized records; it cannot select cryptographic parameters, change production configuration, accept risk or attest to compliance.

## Before starting

Record use case, exact function, required output length and units, input encoding, implementation version and consumer. Identify the governing approved design and evidence access. Use the [agent runbook](../agent-runbook.md) with synthetic QA inputs; sensitive source data and secrets stay outside this repository. A longer output alone does not establish suitability for an arbitrary security purpose.

## Ordered workflow

1. **Inventory the actual uses.** Reconcile all in-scope producers and consumers with purpose and owner. Output a use register, including unreviewed dependencies. A library's SHA-3 support does not prove the application invokes the intended function.
2. **Define inputs and outputs.** Record binary encoding, preprocessing, function identity, output length and serialization. For an XOF, specify the requested length explicitly rather than relying on defaults. Output a contract; bits, bytes and encoded characters must not be conflated.
3. **Trace the executed implementation.** Link the operation to its build, library and configured function. Output a baseline map. Do not infer equivalence from similar function names, output sizes or a shared permutation family.
4. **Evaluate QA computation.** Use authoritative vectors for the selected function and output length, then check application preprocessing and streaming behavior separately. Preserve expected/actual results and all untested cases. Output a test matrix; vector success does not confer algorithm or module validation.
5. **Check the consumer.** Verify the exact expected length, encoding and acceptance rule, including malformed, missing and mismatched outputs. Identify the source and trust basis of any reference digest. Output application results; an unkeyed digest alone does not establish sender authority or confidentiality.
6. **Reconcile changes.** Map function, output-length, serialization and provider updates to every affected producer and consumer. Preserve historical function/length metadata. Output transition actions; a renamed field does not migrate stored values or downstream expectations.
7. **Review bounded conclusions.** Separate computation, input/output contract, reference trust and approved purpose. Assign unresolved design questions to qualified owners. Output a draft evidence packet without claiming whole-system security from a successful digest comparison.

## Evidence and test plan

### Function use and input/output contract

Application, data and cryptography owners provide the complete scoped producer/consumer inventory, approved purpose, exact function identifiers, input contracts and output requirements. Reconcile every flow to its responsible owner and design reference. Preserve missing function or length metadata as an unresolved decision, not an invitation to choose a convenient default.

Record input byte length, encoding and preprocessing separately from output byte length and encoded representation. For each XOF use, identify who specifies the output length and how both ends enforce it. A digest-looking string cannot by itself establish the function, requested length or trustworthiness of the originating data.

### Implementation and verification evidence

Engineering and quality owners provide actual build/library versions, executed function references, authoritative vector identifiers, application cases and observed outcomes. Match evidence to the precise function and length tested. Keep vector correctness separate from application serialization, consumer parsing and security-purpose suitability.

Under approved QA conditions, record empty/binary and relevant boundary or streaming inputs alongside malformed output cases. Preserve expected results independently of the implementation under test. A matching producer and consumer can share the same defect. Retain all scoped failures and unperformed cases; do not trim the evidence population to passing examples or silently normalize incompatible results.

### Changes, dependencies and historical records

Platform, supplier and risk owners provide releases, source-status reviews, parameter changes, incidents and approved exceptions. Reconcile each change to affected stored values and downstream consumers. Preserve function, length and input-contract version with historical results so later verification uses the right interpretation.

Record migration planned, producer changed, consumer changed and stored-data treatment as separate outcomes. Verify actual deployed versions before reusing earlier tests. Do not rewrite historical digests from unverified current data to conceal incompatibility. Assign unresolved legacy interpretation and source-update questions to named owners with review triggers.

## Failure branches and decisions

An unobserved implementation path is `not_tested`; uncertain approved purpose is `inconclusive`. A known output-length mismatch against the contract is `not_supported` even if each implementation computes correctly for its requested length. Do not silently truncate or pad outputs to make a test pass.

Fictional desk case: the approved QA interface requires 32 output bytes from SHAKE256, but a producer interprets 32 as bits and returns four bytes. Computation for that request can be correct while the interface contract is `not_supported`. The agent records requested units and actual byte length and routes correction to engineering without changing cryptographic requirements.

## Cadence and renewal

Reassess after source, function, output-length, input-contract, implementation or consumer changes and after consequential failures. Use approved organizational review schedules rather than invented quarterly checks or annual FIPS renewal. Assign ownership for legacy-data interpretation and transition gaps.

## Completion and handoff

Deliver the complete use map, input/output contracts, implementation manifest, vector and application evidence, change reconciliation and open exceptions. State separately what the evidence supports about computation, data representation, consumer acceptance and approved purpose. Identify untested combinations and unresolved source issues with next owners and actions.

Independent source, skeptical and rights review remain required before publication. Qualified owners retain function/parameter selection, migration, exceptions and compliance decisions. This draft has not validated a cryptographic implementation or established secure use in a real system.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
