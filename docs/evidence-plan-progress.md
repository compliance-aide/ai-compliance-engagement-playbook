# Tailored evidence-plan progress

This is a transparent implementation ledger for the catalog-wide evidence-plan
goal. A plan is not ready for final publication merely because its Markdown
section exists: it must also have source and skeptical review recorded, satisfy
the strict validator, and remain within the publisher-rights boundary.

| Guide | Plan state | Source / skeptical review | Notes |
| --- | --- | --- | --- |
| UK Cyber Essentials | drafted | independently corrected against official NCSC material | Version 3.3 source snapshot; five-theme and scope/provider corrections incorporated. |
| NIST CSF 2.0 | drafted | pending | Original profile, operational-evidence, and measurement packages. |
| HIPAA Security Rule | drafted | pending | ePHI-minimizing package design; legal conclusions reserved to humans. |
| EU GDPR | drafted | pending | Privacy/legal decision boundaries explicit. |
| NIST AI RMF 1.0 | drafted | pending | Trustworthiness and release decisions reserved to humans. |
| NIST Privacy Framework 1.0 | drafted | pending | Privacy-law applicability remains outside the plan. |
| California CCPA/CPRA | drafted | pending | California scope and consumer outcomes reserved to counsel/privacy owners. |

Run `python3 tools/validate_guides.py --require-evidence-plans` to enforce
catalog-wide section completeness. It intentionally fails until every
framework guide has a complete tailored plan; this ledger never substitutes for
that check or independent review.
