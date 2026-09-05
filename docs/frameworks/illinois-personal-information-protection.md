# Illinois Personal Information Protection Act engagement guide

> Original operational guidance, not legal advice, a breach determination, an approved notice or a compliance claim.

## Source and applicability

Use the [official Illinois statute, 815 ILCS 530](https://www.ilga.gov/Legislation/ILCS/Articles?ActID=2702&ChapterID=67&Print=True). The complete displayed act was read on 2026-09-04. The site warns that enactments and effective dates can differ from the compiled display; current Public Acts and relevant interpretations must be checked by counsel before legal conclusions. This guide is an operational draft, not an exhaustive current-law opinion.

Section 5 supplies definitions; sections 10 and 12 distinguish general and State-agency notification routes. Sections 25, 30, 40, 45 and 50 add reporting, disposal, security and conditional HIPAA-related treatment. Do not transfer a condition or exemption from one section to every obligation. Separate data owner/licensee and maintainer roles by dataset; an organization may perform both.

## Engagement focus

Build a usable chain from data ownership and safeguards to incident facts, applicable decision paths, approved communications, verified recovery and remaining actions. Preserve the original discovery timeline as investigation scope changes. A draft notice is not a sent notice; restored availability is not proof that exposed information is secure.

## Roles

Privacy and data owners maintain scope. Security and incident response preserve evidence and establish technical facts. Procurement obtains vendor cooperation. Counsel determines coverage, breach status, recipients, timing and exceptions. Authorized communications and agency officials approve and send notices or reports. An independent reviewer challenges completeness and reasoning. AI may reconcile authorized records and apply an approved calculation rule, but cannot decide legal duties, transmit personal information, alter forensic evidence, send notices, submit government reports or accept risk.

## Before starting

Record entities, systems, Illinois-resident datasets, owner/licensee/maintainer roles, State-agency status, vendors and review period. Obtain approved data-flow, encryption/key, contract, disposal and incident records. Identify reachable primary and backup decision owners before an event. Store sensitive evidence privately; use de-identified references here. Missing coverage or contacts must generate an assigned action rather than a success-shaped empty register.

## Ordered workflow

1. **Reconcile the population.** Account for all known scoped datasets, systems, physical materials, vendors and flows against authoritative inventories. Preserve unknowns. Record data elements, residency basis, encryption/redaction state and key access as separate facts. Do not presume that encryption excludes an event when keys may also be affected.
2. **Establish preventive evidence.** Map safeguards, disclosure-contract security provisions and disposal arrangements to owners and current artifacts. Check actual operation, supplier responsibilities and remaining copies against approved expectations. A contract can support an obligation record; it does not prove supplier performance. Assign failures and unavailable evidence separately.
3. **Open and preserve an incident record.** Record discovery, receipt of third-party notice, suspected acquisition, affected systems and initial scope with timestamps and timezones. Preserve authorized originals, provenance and access history. Incident leaders authorize containment; avoid destructive evidence changes. Escalate immediately to the designated team while facts are incomplete; do not wait for an AI-generated final report.
4. **Resolve each applicable legal route.** Counsel reviews facts against the decision table below. Record applicable section, trigger, recipient, timing rule, required content, delivery method, approver and evidence. Keep parallel routes separate and allow several to apply. Unknown population size does not become zero. Update the count and reasoning without resetting discovery time.
5. **Prepare and verify communication readiness.** Build separate drafts for residents, owners/licensees, Attorney General and other applicable recipients. Validate content and recipient lists against the approved route. Section 10 resident notices exclude the affected-resident count, while its Attorney General notice includes that count; do not reuse one draft uncritically. Obtain approval before sending and preserve dispatch, acceptance, failure and follow-up records. Approval alone is not delivery.
6. **Reconcile recovery and remaining duties.** Confirm authorized containment and recovery results, exposed credential/key actions, vendor cooperation and failed communications. Track additional facts and supplemental reporting requirements. A reopened investigation keeps the existing decision history; an exception needs its authority, scope and end condition recorded.
7. **Close only the supported work.** Deliver evidence references, legal decisions, communication receipts, recovery verification and owned corrective actions. Have the authorized incident owner decide closure with unresolved obligations explicit. Test changed controls and contact paths through an approved synthetic exercise before treating readiness defects as resolved.

## Notification decision table

This table identifies routes for counsel verification, not automatic filing instructions. Apply the full cited sections, including content, method and exception conditions.

| Route | Timing and boundary to preserve |
| --- | --- |
| Owner/licensee resident notice — section 10(a) | Expedient notice without unreasonable delay, consistent with necessary scope and system-restoration measures; no generic 30-day or 72-hour substitute |
| Maintainer to owner/licensee — section 10(b) | Immediately after discovery when the specified acquisition condition is met; cooperation is separately required |
| General Attorney General notice — section 10(e) | More than 500 Illinois residents required to be notified from a single breach; no later than consumer notice and without unreasonable delay; qualifying section 50 entities have a different route |
| State-agency notices — section 12 | Evaluate resident notice; more-than-1,000-person consumer-reporting-agency route; more-than-250-resident Attorney General route with earlier-of-45-days-or-consumer-notice rule and specified exceptions |
| Additional State-agency reports — sections 12(f), 12(g), 25 | Preserve separate five-day actor-identification, qualifying Governor-responsible agency 72-hour, five-business-day General Assembly and annual reporting triggers; none is a universal incident deadline |
| Qualifying HIPAA route — section 50 | Requires the stated compliance conditions; where HHS breach notification is required, notify the Attorney General within five business days after notifying the Secretary |

Counsel must record written law-enforcement delay authority where required and monitor when delay ends. An ordinary investigation or an unsigned request does not automatically establish that exception. Check other jurisdictions and contractual duties separately without importing their deadlines into this Act.

## Evidence and test plan

Preserve the three tailored packages from the earlier draft, expanded to the complete known scoped population rather than selected paths.

| Package | Minimum evidence | Challenge |
| --- | --- | --- |
| Personal-information boundary and safeguards | Data/system/vendor register, roles, encryption and keys, contracts, disposal and safeguard evidence | Are ownership, copies and actual protections known? |
| Investigation and preservation | Original timeline, preserved evidence references, custody, scope changes, factual uncertainties and containment approvals | Can another authorized reviewer reconstruct what was known at each decision? |
| Notification and recovery assurance | Route decisions, clocks, approvals, separate drafts, delivery receipts, recovery tests and corrective actions | Were the right duties tracked and actual outcomes verified? |

Follow the [agent runbook](../agent-runbook.md): use `supported`, `not_supported`, `inconclusive`, `not_applicable` and `not_tested` for individual assertions. Do not erase a known failure with an aggregate uncertainty label. Preserve all available scoped evidence without silent sampling or caps; inventory completeness does not prove every technical combination was tested.

Fictional author case: a general section 10 incident initially has 480 Illinois residents requiring notice, then the reconciled count becomes 520 before consumer notices are sent. Reopen the Attorney General route using the original timeline; do not restart the clock or keep the earlier below-threshold decision unchanged. Counsel approves the route; AI neither sends notices nor declares a violation.

## Failure branches and decisions

Missing logs limit scope conclusions; they do not prove no acquisition. Vendor silence requires an escalated request and a visible evidence gap. A rejected notification remains open with retry or alternative-delivery ownership. Conflicting preservation and disposal instructions require prompt legal direction before destruction. A HIPAA or financial-sector label alone does not establish the conditional treatment of the relevant section.

## Cadence and renewal

Exercise readiness on an owner-approved risk-based schedule and reopen after data, vendor, contact, system, incident or legal changes. Preserve actual statutory event-driven and annual State-agency reporting duties where applicable; do not replace them with a generic annual readiness review.

## Completion and handoff

Hand off the complete scoped registers, private evidence index, decisions, delivery/recovery receipts and open actions to named owners. Independent source, skeptical and rights review remain pending before guide publication. A fictional desk exercise is not an independent review, breach assessment or cross-model usability trial.

## Universal engagement contract

Apply the [universal engagement contract](../universal-engagement-contract.md) with the runbook for authority, evidence, exceptions and source changes.
