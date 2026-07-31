# Repository design research record

This record preserves the public-repository research that informed the
repository-wide engagement contract. It documents design inspiration only. The
playbook does not copy code, framework text, policy packs, proprietary
crosswalks, or assessment content from these projects.

Research review date: 2026-07-31. The full top-50 popularity snapshot is kept
in the working research record; the sources below are the material design
references for this change.

## Design decisions and public references

| Design decision | Public references reviewed | Playbook decision |
| --- | --- | --- |
| Typed evidence, not pass/fail claims | [Prowler](https://github.com/prowler-cloud/prowler), [Checkov](https://github.com/bridgecrewio/checkov), [InSpec](https://github.com/inspec/inspec), [AuditKit](https://github.com/guardian-nexus/AuditKit-Community-Edition) | Require claim, scope, method, period, integrity, limitation, reviewer, and disposition fields. A check result remains evidence, not a conclusion. |
| Portable technical checks | [OPA](https://github.com/open-policy-agent/opa), [Kyverno](https://github.com/kyverno/kyverno), [Cloud Custodian](https://github.com/cloud-custodian/cloud-custodian), [CloudFormation Guard](https://github.com/aws-cloudformation/cloudformation-guard) | Support optional adapters and readable desired-state descriptions; do not require one policy language, scanner, cloud, or GRC product. |
| Evidence provenance and work queues | [Chainloop](https://github.com/chainloop-dev/chainloop), [Probo](https://github.com/getprobo/probo), [Openlane](https://github.com/theopenlane/core) | Use evidence contracts, owner/reviewer/approver separation, recurring work, escalation, re-performance, and expiry fields. |
| Agent authority boundaries | [Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit), [VerifyWise](https://github.com/verifywise-ai/verifywise), [AI SDLC](https://github.com/ai-sdlc-framework/ai-sdlc) | Make AI may, AI must ask, accountable human, independent reviewer, required evidence, and prohibited action explicit for every engagement phase. |
| Structured assessment interoperability | [NIST OSCAL](https://github.com/usnistgov/OSCAL), [Compliance Trestle](https://github.com/oscal-compass/compliance-trestle), [OpenControl schemas](https://github.com/opencontrol/schemas) | Keep Markdown guidance authoritative and readable; make machine-readable mappings optional, validated adapters rather than a repository dependency. |
| Global applicability and localization | [CISO Assistant Community](https://github.com/intuitem/ciso-assistant-community), [India Compliance](https://github.com/resilient-tech/india-compliance) | Require jurisdiction, legal/contractual/voluntary status, applicability trigger, localization, source/licensing, and renewal/change data. |
| Privacy and supply-chain evidence | [Privado](https://github.com/Privado-Inc/privado), [Hawk-Eye](https://github.com/rohitcoder/hawk-eye), [OWASP dep-scan](https://github.com/owasp-dep-scan/dep-scan) | Treat data discovery, SBOMs, and scan results as bounded inputs that require human context, review, and disposition. |

## Rejected shortcuts

- A scanner pass, generated narrative, or policy check cannot be represented as
  certification, legal compliance, or operating effectiveness.
- An AI agent cannot approve, attest, submit, accept risk, silently suppress
  exceptions, or alter a production environment.
- A source-agnostic guide cannot republish restricted framework text or import
  another repository's control mapping, policy pack, or assessment criteria.
- “Supports many frameworks” is not a quality metric. Source quality,
  applicability, evidence traceability, independent review, and maintained
  change history are required separately.

## Rollout boundary

The repository-wide contract link is present in every published guide and is
validated as an exact local link. This is a shared-methodology rollout, not a
retroactive claim that every guide has completed all new records or independent
review steps. Future guide work and guide-specific renewal audits must create
and retain that evidence separately.
