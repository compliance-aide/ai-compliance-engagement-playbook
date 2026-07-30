# NIST SP 800-204D DevSecOps supply-chain engagement guide

> Original operational guidance, not NIST text, a software-release approval, a supplier assurance conclusion, or a compliance claim. Confirm current material through the [NIST SP 800-204D publication record](https://csrc.nist.gov/pubs/sp/800/204/d/final).

## Engagement focus

Maintain a traceable supply-chain assurance record for DevSecOps delivery pipelines. Connect each material component, build input, supplier or repository, build environment, pipeline version, verification evidence, artifact provenance, release decision, exception, vulnerability response, and retirement or replacement action to accountable owners. Do not treat an automated pipeline result, a signature, or a supplier statement as a complete assurance conclusion without reviewing its scope, integrity, and current relevance.

## Roles and annual rhythm

Product, development, platform, security, supply-chain, procurement, legal, privacy, operations, risk, and release owners retain accountable decisions. Engineering owners preserve build and dependency evidence; platform owners control authorized pipeline operation; supply-chain owners govern supplier records; release authorities approve deployment; and risk owners decide exceptions within mandate. Independent reviewers sample selected releases from source and dependency context through pipeline evidence, artifact provenance, exceptions, vulnerability handling, and production decision, then challenge unverified inputs and missing owner attestations.

AI may organize authorized dependency and evidence metadata, detect incomplete provenance fields, summarize approved pipeline records, draft questions, and prepare non-authoritative workpapers. AI cannot modify source or pipeline configuration, create or approve credentials, approve a supplier, waive a verification failure, authorize release, accept risk, or claim compliance. Use AI only with permitted, minimized artifacts. Reassess after material pipeline, component, supplier, vulnerability, build-environment, or release-process changes; review exceptions quarterly and complete an annual independent readiness review.
