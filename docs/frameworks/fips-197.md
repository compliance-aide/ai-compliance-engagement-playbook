# FIPS 197 AES engagement guide

> Original operational guidance, not FIPS AES content, a cryptographic design, an approval, or a compliance claim. Confirm current material through [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) and the organization’s approved cryptography, security, architecture, legal, and operational decisions.

## Engagement focus

Operate a governed lifecycle for in-scope implementations of the Advanced Encryption Standard. Connect each use case to an approved purpose and scope, protected data and system context, implementation and configuration decisions, key-management dependencies, mode and protocol interfaces, access, logging, validation, supplier dependencies, changes, incidents, transition planning, and retirement. A configuration extract, implementation record, vendor statement, test result, or audit log is evidence to assess; none alone proves suitable algorithm use, correct implementation, protected keying material, approved use, secure operation, or compliance.

## Source and applicability

The [NIST publication record](https://csrc.nist.gov/pubs/fips/197/final), read 2026-09-04, states that the May 2023 update made editorial improvements without technical algorithm changes. It identifies AES-128, AES-192 and AES-256, all with 128-bit blocks; their suffixes specify key lengths. Retrieve the full standard and applicable mode, key-management and validation guidance before assessing a design. Those additional sources remain unverified here. AES use alone is not a complete secure-storage or secure-transport design.

## Roles

Cryptography and security owners approve the algorithm, mode and parameter requirements. Application owners define protected data and consuming behavior. Key-management and platform owners provide controlled evidence. Independent reviewers challenge coverage and claims. AI organizes authorized metadata; it cannot access production keys, select cryptographic parameters, change settings, approve exceptions or attest to compliance.

## Before starting

Record system, purpose, data boundaries, actual implementation version, approved mode and parameter references, key identifiers and recovery dependencies. Use the [agent runbook](../agent-runbook.md) and synthetic QA data. Identify the exact security properties required: successful encryption/decryption alone does not establish authenticity, authorization or protected key custody.

## Ordered workflow

1. **Inventory protected flows.** Reconcile all in-scope storage, transport, export, backup and recovery paths with owners and approved designs. Output a coverage map. A database encryption setting does not establish coverage of exports or logs.
2. **Identify actual implementation.** Link each operation to the executed library/module and configuration, including mode and key-length metadata. Output a baseline manifest. A package name or vendor claim is not proof of the invoked operation.
3. **Check design dependencies.** Have qualified owners confirm applicable mode, initialization/nonce rules, integrity requirements and key lifecycle controls from authoritative sources. Output an applicability matrix. Do not derive mode-specific rules solely from FIPS 197 or generalize one mode's requirements to another.
4. **Evaluate computation in QA.** Use relevant authoritative vectors and separately test application input/output handling. Record expected and actual outcomes for the approved scope. Output a test matrix; a round trip with the same implementation can conceal matching defects and does not establish validation.
5. **Test failure handling.** Under the approved design, test malformed input, unavailable key service, unauthorized access and integrity failures where applicable. Observe the application's action, not only a library return code. Output separate computation and policy results; failure must not silently cause plaintext storage or release of unverified data.
6. **Trace key and data lifecycle.** Reconcile authorized key creation/use/rotation references with data versions and recovery needs without collecting key material. Output lifecycle evidence. A rotation job's success message does not establish that historical data remains recoverable or that new writes use the intended key.
7. **Review changes and conclusions.** Match release and provider changes to affected paths and retest requirements. Preserve open exceptions with owners. Output a bounded draft separating algorithm behavior, configuration, key protection, data coverage and organizational approval.

## Evidence and test plan

### Encryption use and protection boundary

Data, application and infrastructure owners provide the complete use inventory, approved protection boundaries, data classifications and component associations. Reconcile every scoped data path with its actual implementation and owner. Include temporary files, exports, backups and recovery copies where they are in scope. An encrypted primary store does not establish that these other copies are protected.

Record the evidence for each boundary separately from the intended design. Use synthetic data to observe application outputs under approved QA conditions; retain non-sensitive identifiers and results instead of real plaintext or key material. Preserve untested paths explicitly. A tool's encryption flag is not proof of complete data coverage or authorized access enforcement.

### Key-management dependencies and configuration

Key-management, platform and supplier owners provide approved configuration identifiers, key-service dependencies, access decisions and lifecycle metadata. Match the actual deployed baseline to the approved design. Preserve mode and parameter references without turning this guide into an unsourced configuration recipe.

Reconcile key rotation with both new writes and historical recovery requirements. Verify the intended key-version selection through authorized metadata and approved tests; distinguish rotation requested, key created, application updated and data migration completed. Test unavailable-service handling against the approved policy. A provider availability statement does not establish that the application handles its outage safely.

### Changes, assurance and exceptions

Engineering, quality, security and risk owners provide the complete scoped change population, test evidence, supplier notices, incidents and exception decisions. Match observations to the build, environment and affected data path. Preserve failed tests and unperformed combinations; successful round trips do not replace appropriate independent expected results.

For each gap, define the acceptance criterion before retesting. Record implementation, rollout and observed behavior separately. Check that exceptions have an authorized owner, exact scope, conditions and review trigger; a pending exception cannot justify a supported result. Keep algorithm testing, module-validation evidence where required, key protection and application security as separate claims.

## Failure branches and decisions

Missing runtime evidence is `not_tested`; uncertain mode applicability is `inconclusive`. An observed plaintext fallback contrary to the approved criterion is `not_supported` even if AES vectors pass. Keep successful cryptographic checks and failed application behavior separate.

Fictional desk case: the QA implementation passes its AES vectors, but an unavailable key service causes the export route to write plaintext while reporting success. Vector results are `supported`; required encrypted-export behavior is `not_supported`. The agent preserves the failure and routes correction to engineering without accessing production keys or weakening the requirement.

## Cadence and renewal

Reassess after mode, implementation, provider, key-policy, data-flow or source changes and after consequential failures. Set scheduled review from approved organizational requirements; do not invent quarterly reviews or annual FIPS renewal. Assign ownership for legacy data, recovery and retirement decisions.

## Completion and handoff

Deliver the complete data-flow/protection map, implementation and configuration inventory, key-dependency records, QA results, change reconciliation and open exceptions. State what was observed about encryption, data coverage, failure behavior and recovery, including untested environments and uncertain source requirements. Assign each gap an owner and next action.

Require independent source, skeptical and rights review before publication. Human authorities retain algorithm/mode selection, key lifecycle, production changes and risk decisions. This draft has not validated a real implementation or demonstrated protection of customer data.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) for the shared applicability, authority, evidence, technical-test, exception, source-change, and renewal requirements that govern this framework engagement.
