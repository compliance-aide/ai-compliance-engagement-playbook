# Universal engagement contract

This contract applies to every framework guide in this repository. It is
original operating guidance, not framework text, legal advice, an attestation,
or a certification method. A framework-specific guide adds applicability and
cadence; it does not remove these minimum traceability and authority rules.
See the [repository design research record](repository-design-research.md) for
the public design references reviewed without importing their content.

## 1. Applicability card

Record the jurisdiction or publisher, whether the material is legal,
regulatory, contractual, or voluntary, the in-scope entity/data/system trigger,
sector and localization considerations, authoritative source and license
boundary, human owner, and source-change monitor. Keep an explicit list of
assumptions, overlays, exclusions, and unresolved applicability questions.

## 2. Authority gate

For each engagement phase, record these fields before work starts:

| Field | Required record |
| --- | --- |
| AI may | Read-only research, organization, traceability checks, and non-authoritative drafts permitted for this phase. |
| AI must ask | Missing authority, sensitive evidence access, ambiguity, material conflicts, or any requested write/action. |
| Accountable human | Named owner of scope, implementation, business decision, and external statement. |
| Independent reviewer | Person or function not responsible for producing the reviewed work. |
| Evidence required | Minimum records needed to evaluate the phase assertion. |
| Prohibited action | Decisions, attestations, submissions, production changes, or risk acceptance the AI cannot make. |

AI must not choose evidence to obtain a preferred result, approve its own
output, conclude conformance, accept risk, submit a declaration, or alter a
production system. A human approval records the decision, rationale, date,
scope, and any conditions or expiry.

## 3. Evidence contract

Treat every scan, interview, configuration export, workpaper, policy, ticket,
or AI-produced draft as an evidence input, never automatic proof. For each
material claim or control objective, preserve:

| Field | Required record |
| --- | --- |
| Claim and objective | Assertion evaluated and the original control intent it supports. |
| Scope and population | System, process, data, people, supplier, or sampled population covered. |
| Source and method | Source system/custodian, collection method, tool/query and version where relevant. |
| Time and coverage | Collection timestamp, period covered, recurrence, omissions, and known blind spots. |
| Integrity and handling | Immutable/raw reference or hash where appropriate; access, sensitivity, retention, and transfer limits. |
| Validation | Test method, reviewer, result, limitations, false-positive rationale, and exception path. |
| Disposition | Finding/action/decision identifiers, accountable owner, due date, retest criteria, and next review. |

Preserve raw originals or permitted references. AI may normalize metadata and
identify missing fields, but cannot alter evidence, infer unobserved facts, or
decide sufficiency.

## 4. Technical-evidence adapter

Use an optional adapter when a technical check is useful. Define the desired
state in human-readable language, parameterized scope, check or query ID and
version, required permissions, asset universe, timestamp, raw-result pointer,
errors, normalized result, reviewer interpretation, and remediation or
false-positive rationale. A passing scanner, policy query, or pipeline check is
technical evidence only; it does not demonstrate design adequacy, complete
coverage, operating effectiveness, legal applicability, or conformance.

Adapters may reference interoperable formats such as OSCAL, policy engines, or
cloud queries, but no adapter is mandatory and this repository does not embed
third-party policy packs or restricted control mappings.

## 5. Exception and change control

Record every exception with affected claim/objective, rationale, compensating
measure, accountable owner, independent challenge where required, named human
approver, effective date, expiry/review date, and closure condition. Do not let
an AI silently suppress, waive, or close an exception.

For a material source, scope, system, supplier, data, incident, test, or
control change, use: proposal -> independent review -> accountable human
approval -> recorded implementation -> evidence refresh -> retest where needed.
Record rejected proposals and unresolved disagreements when they affect the
engagement conclusion.

## 6. Annual engagement and quality gate

Run the shared lifecycle: scope -> interpretation -> implementation/operation
-> evidence -> testing -> findings/remediation -> audit support -> monitoring
-> annual renewal. Turn recurring work into visible queues with owner,
frequency, overdue escalation, completion evidence, and re-performance date.

Before publication or renewal, confirm that the guide has an authoritative
source and date, license boundary, applicability card, authority gate, evidence
contract, exception path, source-change trigger, original-language warning,
independent review record, and fictional-only examples. Any conclusion remains
subject to the responsible human and applicable assessor method.
