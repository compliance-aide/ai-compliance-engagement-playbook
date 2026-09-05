# Illinois Biometric Information Privacy Act — engagement guide

> Original operational guidance, not legal advice, a litigation assessment or a compliance determination.

## Source and applicability

Read the [official BIPA statute](https://www.ilga.gov/Legislation/ILCS/Articles?ActID=3004&ChapterID=5), particularly sections 10, 15, 20 and 25. The full displayed act was checked 2026-09-04. Its database warns that recent enactments and effective dates require separate checking. Counsel must confirm current Public Acts, relevant decisions, historical periods and exclusions before making an applicability or liability conclusion. This draft does not establish a complete case-law review.

Section 10 defines covered identifiers and information and recognizes electronic signatures in written releases; section 25 includes entity/activity exclusions. Do not classify a process from its marketing label or assume that an exclusion for one activity covers the whole organization. Obtain a counsel-approved decision for each disputed process and retain the rationale, source and applicable period.

## Engagement focus

Reconcile biometric processing, notices, releases, disclosures, security and destruction against actual system records. A signed vendor agreement or consent-form template does not prove the collection workflow followed it. Work with approved metadata and evidence references; never copy biometric templates, signatures or identifiable subject lists into this public repository.

## Roles

Legal owns statutory interpretation, exceptions and litigation decisions. Privacy owns notices, releases and the processing register; product and HR own collection channels; security and IT own safeguards and lifecycle evidence; procurement owns supplier follow-up. An independent reviewer challenges traceability and conclusions. AI may organize approved records and flag discrepancies but cannot collect biometrics, obtain consent, authorize disclosures, decide legal validity, delete records or determine liability.

## Before starting

Record the engagement period, legal entities, locations, employee/customer uses, systems, vendors and responsible owners. Obtain approved access to process diagrams, policy versions, notice/release metadata, collection/disclosure logs, retention rules, security evidence and complaints. Keep sensitive workpapers in the approved private evidence system. Missing source or access permissions block the affected activity, not unrelated authorized inventory work.

## Ordered workflow

1. **Reconcile the full known population.** Compare product, HR, procurement and system inventories. Give every scoped process, channel, vendor and version a stable ID. Record what is collected, how it is transformed, its identifying use, recipients and storage locations. Preserve unknown coverage and assign an owner. Do not silently sample, trim or cap evidence.
2. **Resolve coverage and purpose.** Send each process and its factual evidence to legal for an applicability decision. Record purpose, term, covered population, exclusions and effective period. Technical facts remain separate from legal conclusions; converting a scan to a template does not by itself settle coverage. Exit with approved scope or explicit unresolved questions.
3. **Check the collection gate.** Section 15(b) requires written information about collection/storage, purpose and term, followed by the required release before obtaining covered data. Trace each available scoped event to the notice version, release reference, signer authority and timestamps. Reconcile unmatched events and clock uncertainties. A form created later cannot prove an earlier gate was satisfied; preserve historical failures when improving future behavior.
4. **Check recipient and commercial-use paths.** Section 15(c) prohibits selling, leasing, trading or otherwise profiting from covered biometrics. Section 15(d) separately limits disclosures. Map every recipient, onward transfer and purpose to a legal-owner decision and operational record. Do not treat collection authorization as blanket disclosure permission. Escalate unexplained transfers or business uses; AI does not approve them.
5. **Check retention and safeguards.** Section 15(a) requires a public retention/destruction policy using the earlier of purpose completion or three years after last interaction, with its specified court-process exception. Have the legal owner approve trigger interpretations and any exception. Reconcile scheduled and actual destruction across systems and vendors, including backups and restoration paths. Under section 15(e), review industry care and comparison with other sensitive-information protections. Preserve failed jobs and unverified copies; a deletion ticket is not deletion evidence.
6. **Validate behavior with approved evidence.** Compare designed controls with actual configuration and logs. For authorized synthetic QA, define expected results before execution: a missing release must not proceed through the collection gate; the wrong notice version must be flagged; overdue lifecycle actions must surface visibly. Use no real biometric capture. Record tested versions, results and limitations. Inventory reconciliation is not proof that every technical combination was tested.
7. **Remediate and hand off.** Assign each discrepancy an owner, due date and required verification evidence. Retest affected configurations after approved changes and retain the original finding. Prepare a decision package with the scope, evidence index, unresolved issues and counsel decisions. Complaints, preservation conflicts and potential violations go to legal through the approved process; AI must not calculate definitive damages or send legal responses.

## Evidence and test plan

These three original packages preserve and expand the earlier tailored plan.

| Package | Required records | What it can establish |
| --- | --- | --- |
| Biometric-use, person and purpose boundary | Complete known process/vendor inventory, private population references, data flow, period, owners and legal scope decisions | Accountable scope; not legal coverage without the decision |
| Notice, authorization and disclosure trail | Versioned notices, release references, authority metadata, event times, recipients, approved bases and unmatched-event list | Traceable sequencing and gaps; not individual understanding or blanket authorization |
| Retention, destruction, vendor and incident accountability | Trigger inputs, public policy reference, approved deadlines/exceptions, job results, copy reconciliation, security comparisons and incident actions | Lifecycle and safeguard evidence within stated limits; not proof of unknown supplier copies |

Use the [agent runbook](../agent-runbook.md) statuses `supported`, `not_supported`, `inconclusive`, `not_applicable` and `not_tested` for individual assertions. Split compound claims and keep task completion separate from control results. Missing logs may make one assertion inconclusive; they do not erase a failure established by other evidence.

Fictional author desk case: collection occurs Monday, but the first release record is Tuesday. The Tuesday record cannot support prior authorization for Monday. If complete records establish that no earlier release existed, record the timing failure; if earlier records are missing, preserve that uncertainty and escalate. Do not backdate a release or mark the historical event fixed after changing the form.

## Failure branches and decisions

- Unknown vendor storage or onward use: retain the gap and assign supplier follow-up; do not infer absence from silence.
- Conflicting deletion and preservation instructions: prevent an autonomous destructive action and obtain prompt counsel direction with a recorded deadline and rationale.
- Claimed exemption lacks entity/activity evidence: leave applicability unresolved rather than excluding the process automatically.
- Incident or complaint: preserve authorized evidence and route it to the designated legal/security owner. This guide invents no BIPA-specific breach-notification deadline; assess other applicable obligations separately.

## Cadence and renewal

Owners set review dates from law, policy, risk and approved plans; no unsupported annual mandate is imposed here. Reopen affected records after collection-method, notice, purpose, vendor, recipient, retention, system or law changes and after complaints or incidents. Track lifecycle deadlines independently of the review calendar.

## Completion and handoff

Deliver reconciled registers, private evidence references, test limits, open actions and named legal decisions. No unresolved event disappears from the handoff. Independent source, skeptical and rights reviews remain required before guide publication. Author desk checks are not independent review, a legal opinion or cross-model usability validation.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) alongside the runbook for authority, evidence, exceptions and source changes.
