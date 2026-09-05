# FIPS 204 post-quantum digital-signature engagement guide

> Original operational guidance, not implementation instructions, certification, legal advice or authorization to sign. Draft: independent source, skeptical and rights review remain pending.

## Source and applicability

Use the [NIST publication record](https://csrc.nist.gov/pubs/fips/204/final) and [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf). The record identifies the August 13, 2024 standard and a July 31, 2026 potential-update notice. Check the linked errata before specifying tests; a future-correction notice is not itself a replacement edition.

Sections 5.2–5.4 distinguish ML-DSA and pre-hash HashML-DSA, including context inputs. Context is limited to 255 bytes, not 255 displayed characters. Preserve the selected variant and, for pre-hash use, the hash/XOF and applicable output length in the integration contract. Do not equate signing an arbitrary digest with following HashML-DSA.

This draft read the publication record and selected section 5 passages. Full-standard, errata, current protocol and validation-policy review remains required before a technical conformance conclusion. The procedures below are original engagement methods, not additional NIST mandates.

## Engagement focus

Establish whether each approved signature use actually produces, transports and verifies the intended signed content under its approved identity and authorization rules. Keep algorithm behavior, implementation validation, application acceptance and legal effect as separate claims. A successful signature check alone cannot establish all four.

## Roles

The service owner defines purpose, population and acceptance criteria. A qualified cryptography owner approves the parameter set, variant, protocol and implementation. Operators supply build and QA evidence. Identity and business owners approve signer permissions; legal owners decide legal-effect questions. An independent reviewer challenges source interpretation and evidence coverage. A named change authority approves rollout and exceptions.

AI may reconcile inventories, inspect non-secret supplied evidence and draft tests and findings. AI cannot select cryptography, obtain private keys, sign on behalf of a person, accept risk, approve production changes, certify compliance or replace independent review. Execution uses only explicitly authorized QA identities and fixtures through approved tooling.

## Before starting

Create a work item using the [agent runbook](../agent-runbook.md). Record the approved scope, source editions, owners, permitted tools, QA environment, evidence location and stopping conditions. If an input is unknown, assign its owner and continue only independent work; never invent a parameter or treat absence as exemption.

Inventory every in-scope signing and verification route, including external consumers, batch jobs, archives and recovery paths. Record exclusions with an accountable decision. Inventory completeness and technical test coverage are separate fields; do not silently sample either away.

## Ordered workflow

1. **Define the signed transaction.** For each route, identify the message representation, encoding, context, signer identity, intended recipient and authorized action. Output: a versioned transaction contract approved by the relevant owners. Stop dependent testing if the intended bytes or purpose are ambiguous.
2. **Bind the implementation.** Record the exact application build, provider/module, parameter set, variant, identifiers, pre-hash details when applicable and public-key reference. Match both producer and consumer. Output: an integration matrix; an installed library is not proof the route uses it.
3. **Review supporting claims.** Inspect applicable official validation records and their precise version/environment scope when validation is required. Record algorithm testing separately from module validation and deployed application behavior. Output: claim-by-claim source references, unresolved mismatches and owners.
4. **Prepare QA cases.** A qualified owner selects authoritative vectors and application cases with expected results before execution. Cover approved messages and changes to message, context, signature, public key and authorization state. Include malformed inputs and service errors. Output: a case manifest with every untested route explicit.
5. **Observe actual processing.** Record the cryptographic result, wrapper/API result and resulting business action separately. Confirm the content verified is the content acted on. Do not convert exceptions, timeouts or unsupported algorithms into valid signatures. Output: dated build-bound results and artifact references without secrets.
6. **Check lifecycle and compatibility.** Test approved peer combinations, key transitions, historical verification and failure/rollback behavior. For any multi-signature or hybrid design, use the approved protocol's acceptance rule; do not invent an “either signature passes” rule. Output: rollout matrix with supported and untested combinations and owners.
7. **Classify and hand off.** Split compound assertions. Use supported, not_supported, inconclusive, not_applicable or not_tested with the evidence and criterion for each. Preserve known failures when another subclaim is uncertain. Output: reviewer packet and an explicit decision request to the authorized owner.

## Evidence and test plan

### Package A — complete signature-use population

Maintain one row per route: owner, purpose, producer/consumer versions, signed-content contract, context representation, variant/parameters, key reference, authorization rule, evidence period, dependencies and coverage state. Reconcile against application configuration, job inventories and owner records. Preserve unresolved population differences rather than claiming completeness from a supplier list.

### Package B — layered verification results

For each case retain its requirement, approved expected result, fixture reference, actual implementation, observed cryptographic/API/business outcomes and reproducible non-secret evidence. A same-library sign/verify round trip can share the same defect; supplement it with owner-approved external expected results and interoperability cases. Record byte-length boundaries for context and transport limits, including multi-byte encoding, without constructing cryptography yourself. A vector pass does not substitute for the integration cases.

### Package C — migration and ongoing operation

Record peer readiness, payload-size and workload assumptions, operational monitoring, failure ownership, key-transition states and approved rollback conditions. Distinguish new signing behavior from verification of historical artifacts. Preserve the metadata and authority evidence needed for historical decisions; a current permissions roster alone does not prove past signer authority. Keep private keys, seeds and sensitive signed content out of this public repository.

## Failure branches and decisions

- Wrong context or variant: record the mismatch and stop the affected acceptance claim; do not retry silently with an empty context or alternative variant.
- Valid signature but unauthorized signer/action: report the cryptographic check separately and fail the application authorization criterion when evidence demonstrates that violation.
- Verification unavailable: preserve the error and follow the approved application failure policy; never record “valid” because no rejection was returned.
- Unready peer or oversized payload: record the affected route and actual failure. Do not claim migration from a configuration toggle or conceal legacy fallback.
- Missing source or deployment evidence: mark the specific claim inconclusive or not_tested as appropriate; assign an owner and retain unrelated verified results.

Fictional desk case: QA verifies a signature correctly, but the application processes a payment signed by an identity authorized only for status reports. The mathematical check is supported; the payment authorization criterion is not_supported. This is a reasoning example, not an executed cryptographic test.

## Cadence and renewal

The owner records a cadence justified by applicable obligations, contracts and operational risk. Reopen affected work after changes to source/errata, build, provider, key policy, protocol, peer population or acceptance rules, and after relevant incidents. Do not invent a FIPS-mandated annual renewal or quarterly audit. Track dated decisions and verify remediation on the actual affected route.

## Completion and handoff

Deliver the source register, complete population, integration contract, test manifest/results, coverage gaps, exceptions, remediation owners and reviewer disagreements. Identify each proposed rollout decision and its named approver. Delivery of a packet does not mean approval, deployment or certification. Keep this guide drafted until independent review and rights confirmation are recorded; actual engagement conclusions require their own evidence and authority.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) and [agent runbook](../agent-runbook.md). Keep task completion distinct from evidence status and from authorization to act.
