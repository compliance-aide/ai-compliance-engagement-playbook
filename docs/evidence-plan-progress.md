# Tailored evidence-plan progress

This is a transparent implementation ledger for the catalog-wide evidence-plan
goal. All 537 guides now have a source-linked, original-language **draft**
section generated from their own engagement focus and publisher link. A draft
is not ready for final publication: it must have source and skeptical review
recorded, satisfy the strict validator, and remain within the publisher-rights
boundary.

| Guide | Plan state | Source / skeptical review | Notes |
| --- | --- | --- | --- |
| UK Cyber Essentials | drafted | independently corrected against official NCSC material | Version 3.3 source snapshot; five-theme and scope/provider corrections incorporated. |
| NIST CSF 2.0 | drafted | pending | Original profile, operational-evidence, and measurement packages. |
| HIPAA Security Rule | drafted | pending | ePHI-minimizing package design; legal conclusions reserved to humans. |
| EU GDPR | drafted | pending | Privacy/legal decision boundaries explicit. |
| NIST AI RMF 1.0 | drafted | pending | Trustworthiness and release decisions reserved to humans. |
| NIST Privacy Framework 1.0 | drafted | pending | Privacy-law applicability remains outside the plan. |
| California CCPA/CPRA | drafted | pending | California scope and consumer outcomes reserved to counsel/privacy owners. |
| Remaining 530 guides | generated draft | pending | Each section derives its scope, evidence family, and trigger from the guide's own engagement focus; all remain subject to individual source and skeptical review. |

Run `python3 tools/validate_guides.py --require-evidence-plans` to enforce
catalog-wide section completeness. Run `python3 tools/validate_guides.py
--require-reviewed-evidence-plans` before a completion claim. This ledger never
substitutes for that check or independent review.
