# Full-catalog refresh records

Tracking issue: [#341](https://github.com/compliance-aide/ai-compliance-engagement-playbook/issues/341).
Scope: every framework guide present at the start of this refresh, plus shared
execution instructions, templates, source tracking, navigation and validation.
A new runbook alone is not a completed catalog refresh.

`catalog.json` records every guide and its baseline content hash. Each guide must
receive a full content review, current official-source check, tailored rewrite,
scenario walkthrough and the independent review required by the repository.
Process the whole catalog in traceable batches, never a representative sample.

Statuses are `pending`, `drafted`, `reviewed`, and `approved`. `drafted` means the
content has been rewritten and the author has a source/check record. `reviewed`
requires independent source, engagement and skeptical review. `approved` also
requires the named human publication approval. Every non-pending status is bound
to the guide's exact SHA-256, so later edits require another review. Neither a
status label nor a successful checker proves substantive accuracy.

Each review record must identify the source title/edition/status, retrieval date,
URLs, supported facts, rights boundary, before/after workflow differences, normal
and failure-path walkthroughs, unresolved issues and actual reviewers/decisions.
Do not invent a reviewer or inherit approval from an older version of a guide.
Use `pending` explicitly for work that has not occurred.

Run `python3 tools/validate_refresh.py` to check inventory and draft structure.
Run `python3 tools/validate_refresh.py --require-complete` to check the recorded
completion gates for **all** guides. The latter must fail while any guide remains
pending, drafted or awaiting approval. Inspect review substance before claiming
completion even when that command passes.

## Existing draft work

[PR #340](https://github.com/compliance-aide/ai-compliance-engagement-playbook/pull/340)
contains a separate unfinished evidence-plan effort. Its inspected head was
`eda2a64678c93f97181f878dbaab772d81ca764b` on 2026-09-04. This refresh does not
change that branch or import its old review claims. The three NIST core plans
were read as design context; their evidence categories are retained and expanded
into explicit execution steps and checks, with fresh author source checks.
Remaining PR #340 content must be reconciled during each affected guide review.

## Completion criteria

- Every baseline guide remains accounted for; a rename or retirement needs an
  explicit reviewed migration, not deletion to reduce the denominator.
- Every guide identifies current source/edition status and the conditions in
  which a pinned or historical edition is used.
- Each workflow has prerequisites, ordered actions, accountable roles, tangible
  outputs, exit checks, tailored evidence/tests, failure branches and renewal.
- Every material factual statement has primary-source support. Cadence defaults
  are distinguished from binding deadlines; drafts, laws, voluntary guidance,
  product specifications and certification programs are not conflated.
- Sensitive-data handling, independent review and consequential decisions remain
  bounded; existing valid authorization is reused instead of repeated pings.
- Scenario review covers missing evidence, wrong scope/version, an adverse result,
  interrupted execution and a pending human decision.
- Shared links, catalog coverage and validators are checked, and checker output
  distinguishes structural integrity from completion and factual accuracy.
- All publication approvals are recorded against the final guide versions.

The catalog starts with no completed refresh reviews. Initial inspection covered
the first 20 alphabetical guides plus the three NIST core guides; inspection is
not a refresh completion credit. Other guides remain to be read in full.
