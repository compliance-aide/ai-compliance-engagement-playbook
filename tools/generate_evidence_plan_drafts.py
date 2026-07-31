#!/usr/bin/env python3
"""Create original, clearly-marked draft evidence plans from each guide's own scope.

This is intentionally a drafting aid, not a source-review or approval mechanism.
It never imports framework text, crosswalks, assessment questions, or customer
evidence. A separate reviewer must approve every generated plan before release.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDES = ROOT / "docs" / "frameworks"
SENTINEL = "<!-- evidence-plan: generated-draft -->"


def section(body: str, heading: str) -> str:
    match = re.search(rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    return " ".join(match.group(1).split()) if match else ""


def family(title: str, focus: str) -> tuple[str, str, str, str]:
    text = f"{title} {focus}".lower()
    if any(term in text for term in ("privacy", "personal data", "personal information", "gdpr", "pdpa", "pipl", "lgpd", "popia")):
        return ("processing, people, purpose, recipient, and location", "data-flow, notice/version, rights, retention, vendor, and incident records", "privacy, product, records, and vendor owners", "new data use, purpose, recipient, transfer, rights channel, or incident")
    if re.search(r"\bai\b|artificial intelligence|\bmodel\b|algorithm", text):
        return ("use case, intended purpose, deployment context, affected people, and model/data dependency", "inventory, evaluation, monitoring, oversight, release, feedback, and incident records", "AI governance, product, model, and risk owners", "model, data, provider, use-case, geography, release, or incident change")
    if any(term in text for term in ("financial", "bank", "insurance", "aml", "money laundering", "payment", "sox", "audit")):
        return ("business activity, product, customer, system, third-party, and decision boundary", "governance, transaction/process, access/change, exception, supervisory-review, and remediation records", "business, risk, compliance, finance, and operational owners", "product, customer, supplier, material event, regulatory update, or control change")
    if any(term in text for term in ("safety", "medical", "device", "automotive", "aviation", "rail", "industrial", "ot", "ics", "manufactur")):
        return ("product or operational boundary, asset/process population, safety constraint, supplier, and change window", "design/operating records, asset/configuration, maintenance, test/exercise, supplier, and corrective-action records", "engineering, safety, operations, and supplier owners", "product, asset, supplier, safety condition, maintenance window, or incident change")
    if any(term in text for term in ("environment", "sustainability", "carbon", "ghg", "energy", "climate")):
        return ("organizational boundary, activity source, reporting period, estimation method, and accountable owner", "activity-data, calculation, factor/version, reconciliation, approval, and change records", "sustainability, finance, operations, and data owners", "boundary, source-data, calculation method, reporting-period, or assurance change")
    if any(term in text for term in ("continuity", "resilience", "recovery", "disaster", "incident")):
        return ("service/process priority, disruption scenario, dependency, recovery target, and accountable owner", "impact analysis, plan/version, exercise, communications, recovery, supplier, and corrective-action records", "resilience, service, incident, and supplier owners", "disruption, exercise result, dependency, recovery target, or material service change")
    return ("organization, service, system, data, supplier, location, and applicable boundary", "scope/inventory, policy/procedure, operating, technical, change, exception, and review records", "business, security, service, and supplier owners", "source update, material system/service/supplier change, incident, exception expiry, or annual renewal")


def plan(title: str, focus: str, source: str) -> str:
    boundary, artifacts, owners, trigger = family(title, focus)
    return f'''\n{SENTINEL}
## Tailored evidence plan

**Plan status:** Draft generated from this guide's existing engagement focus; it requires independent source and skeptical review before a final catalog claim.

**Source and rights snapshot.** Use the guide's cited publisher source ({source}) and check its current edition or status before use. This plan uses original operational language and does not reproduce protected requirements, assessment questions, mappings, or branded templates. A named human engagement owner confirms applicability and source rights.

**Guide-specific planning input.** {focus}

### 1. Applicability and boundary evidence

- **Request and owner:** A dated record of the applicable {boundary}, exclusions, inherited responsibilities, and accountable human owners, maintained by {owners}.
- **Validate and limit:** Trace a human-approved selection from the declared boundary to source systems or operating records; preserve population, period, access restriction, and unresolved-boundary notes. This can support a bounded engagement scope. It cannot decide legal applicability, publisher acceptance, certification, or completeness beyond the documented population.
- **AI and trigger:** AI may organize approved metadata and flag inconsistent boundaries. Humans approve scope and exclusions. Refresh after {trigger}.

### 2. Operating evidence for {title}

- **Request and owner:** Time-bounded {artifacts}, selected because this guide focuses on {focus.lower()}, from {owners}.
- **Validate and limit:** Inspect provenance and freshness, then trace a human-approved sample to its source record, accountable owner, and exception or follow-up path. This can support that the stated practice has observable evidence. It cannot prove continuous effectiveness, satisfy an assessor by itself, or support an unreviewed conformance claim.
- **AI and trigger:** AI may create a read-only evidence index, identify gaps, and draft questions; it may not alter systems, close findings, or create external representations. Recollect after {trigger}.

### 3. Decisions, exceptions, and renewal evidence

- **Request and owner:** Approved risk or exception decisions, corrective-action and retest records, source-change watch, and annual review or renewal record from {owners}.
- **Validate and limit:** Trace a selected exception or remediation item to a named human decision, due date, expiry, evidence source, and retest result. This can support accountable follow-through. It cannot accept residual risk, make a legal decision, or replace an independent assessment.
- **AI and trigger:** AI may flag stale approvals and assemble a review packet. Humans approve risk treatment, submissions, attestations, and closure. Revisit on {trigger}.
'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write missing draft sections")
    parser.add_argument("--rewrite-generated", action="store_true", help="replace only plans carrying the generated-draft sentinel")
    args = parser.parse_args()
    generated = []
    skipped = []
    for guide in sorted(GUIDES.glob("*.md")):
        if guide.name == "INDEX.md":
            continue
        body = guide.read_text(encoding="utf-8")
        if "## Tailored evidence plan" in body:
            if args.rewrite_generated and SENTINEL in body:
                body = re.sub(r"\n" + re.escape(SENTINEL) + r".*?(?=\n## Universal engagement contract\n)", "", body, flags=re.S)
            else:
                skipped.append(guide.name)
                continue
        title = re.search(r"^# (.+)$", body, re.M)
        focus = section(body, "Engagement focus")
        source = re.search(r"https://[^)\s]+", body)
        if not title or not focus or not source:
            raise SystemExit(f"Cannot safely draft {guide}: title, focus, or source missing")
        guide_title = re.sub(r" — engagement guide$", "", title.group(1), flags=re.I)
        guide_title = re.sub(r" engagement guide$", "", guide_title, flags=re.I)
        insertion = plan(guide_title, focus, source.group(0))
        updated = body.replace("\n## Universal engagement contract\n", insertion + "\n## Universal engagement contract\n", 1)
        if updated == body:
            raise SystemExit(f"Cannot find contract insertion point in {guide}")
        if args.write:
            guide.write_text(updated, encoding="utf-8")
        generated.append(guide.name)
    action = "Generated" if args.write else "Would generate"
    print(f"{action} {len(generated)} draft plans; skipped {len(skipped)} existing plans.")


if __name__ == "__main__":
    main()
