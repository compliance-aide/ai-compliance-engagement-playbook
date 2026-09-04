# AI RMF 1.0 refresh author record

- Date: 2026-09-04.
- Author: Codex, current refresh task; this is not independent review.
- Guide: [NIST AI RMF 1.0](../frameworks/nist-ai-rmf-1.md).
- Sources: [NIST program page](https://www.nist.gov/itl/ai-risk-management-framework)
  and [AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf).
- Retrieval: program page opened; framework governance/context sections inspected
  through the web tool on the date above. NIST still links 1.0 and describes
  revision work; the rewrite does not invent a published successor.
- Rights: [NIST notice](https://www.nist.gov/copyrights-disclaimers), public
  information except marked copyrighted material. No framework tables, outcomes
  or crosswalks imported; operational steps are original.

## What changed and why

The short use-case/risk narrative now specifies governance before action,
versioned system context, predeclared evaluation criteria, adverse-result
handling, human decisions, monitoring and retirement. PR #340's use-case,
evaluation and oversight evidence categories were read and expanded; their
previous review claims were not carried forward.

## Author walkthroughs

- Normal path: a versioned use case reaches a recorded human decision only after
  an approved evaluation protocol and actual result receipts exist.
- Missing evidence: an unrecorded prompt/model version blocks a claim that the
  evaluation represents the configured system.
- Wrong scope: performance on one population cannot be generalized to another;
  a changed intended use returns to context and risk review.
- Adverse result: a harmful case remains visible even when the average is good;
  the risk owner decides treatment with the adverse evidence intact.
- Interruption: the runbook requires readback before retry and retains the exact
  evaluated version, tool output and resume point.
- Pending decision: deployment remains unauthorized while documentation and
  other permitted checks can proceed.

## Outstanding review

Independent source review: pending. Independent engagement review: pending.
Independent skeptical review: pending. Named human publication approval: pending.
This is an author desk walkthrough, not a model benchmark, deployment test or
trustworthiness determination. Revision status must be rechecked before use.
