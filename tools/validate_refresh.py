#!/usr/bin/env python3
"""Validate full-catalog refresh records; not a factual or legal assessment."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HEADINGS = (
    "Source and applicability", "Engagement focus", "Roles", "Before starting",
    "Ordered workflow", "Evidence and test plan", "Failure branches and decisions",
    "Cadence and renewal", "Completion and handoff", "Universal engagement contract",
)
STATES = {"pending", "drafted", "reviewed", "approved"}


def validate(root, require_complete=False):
    """Return errors and status counts. No network access or file mutation."""
    errors = []
    catalog_path = root / "docs/refresh-reviews/catalog.json"
    try:
        catalog = json.loads(catalog_path.read_text())
    except (OSError, ValueError) as exc:
        return [f"Cannot read refresh catalog: {exc}"], Counter()
    if not isinstance(catalog, dict) or not isinstance(catalog.get("guides"), list):
        return ["Refresh catalog must contain a guides list"], Counter()
    rows = catalog["guides"]
    actual = {p.name for p in (root / "docs/frameworks").glob("*.md") if p.name != "INDEX.md"}
    names = [r.get("guide") for r in rows if isinstance(r, dict)]
    if len(names) != len(rows) or any(not isinstance(n, str) for n in names):
        return ["Each catalog row must be an object with a guide name"], Counter()
    counts = Counter(r.get("status", "missing") for r in rows)
    for name, count in Counter(names).items():
        if count != 1:
            errors.append(f"Duplicate catalog guide: {name}")
    for name in sorted(actual - set(names)):
        errors.append(f"Guide missing from refresh catalog: {name}")
    for name in sorted(set(names) - actual):
        errors.append(f"Catalog guide absent from disk: {name}")
    if not actual or not rows:
        errors.append("Empty guide catalog cannot establish coverage")
    baseline_names = catalog.get("baseline_guides", [])
    if not isinstance(baseline_names, list) or not baseline_names:
        errors.append("Missing baseline guide inventory")
    elif not all(isinstance(n, str) for n in baseline_names):
        errors.append("Baseline guide inventory must contain strings")
    else:
        if len(set(baseline_names)) != len(baseline_names):
            errors.append("Duplicate baseline guide")
        for name in sorted(set(baseline_names) - set(names)):
            errors.append(f"Baseline guide dropped from refresh: {name}")
    for row in rows:
        name = row["guide"]
        if Path(name).name != name or not name.endswith(".md"):
            errors.append(f"Unsafe or invalid guide name: {name}")
            continue
        if not re.fullmatch(r"[0-9a-f]{64}", str(row.get("baseline_sha256", ""))):
            errors.append(f"{name}: missing baseline content hash")
        status = row.get("status")
        if status not in STATES:
            errors.append(f"{name}: invalid refresh status {status!r}")
            continue
        if require_complete and status != "approved":
            errors.append(f"{name}: refresh incomplete ({status})")
        if name not in actual or status == "pending":
            continue
        guide = root / "docs/frameworks" / name
        digest = hashlib.sha256(guide.read_bytes()).hexdigest()
        if row.get("reviewed_sha256") != digest:
            errors.append(f"{name}: review hash is stale or absent")
        body = guide.read_text()
        for heading in HEADINGS:
            if f"## {heading}\n" not in body:
                errors.append(f"{name}: missing workflow section {heading}")
        if "../agent-runbook.md" not in body:
            errors.append(f"{name}: missing agent runbook link")
        ref = row.get("review_record", "")
        review = (root / ref).resolve()
        review_dir = (root / "docs/refresh-reviews").resolve()
        if not ref or review.parent != review_dir or review.suffix != ".md" or not review.is_file():
            errors.append(f"{name}: missing or invalid review record")
        reviews = row.get("independent_reviews", {})
        if status in {"reviewed", "approved"}:
            for role in ("source", "engagement", "skeptical"):
                record = reviews.get(role, {}) if isinstance(reviews, dict) else {}
                if not isinstance(record, dict) or not all(record.get(f) for f in ("reviewer", "date", "receipt")):
                    errors.append(f"{name}: missing independent {role} review receipt")
        if status == "approved":
            approval = row.get("human_approval", {})
            if not isinstance(approval, dict) or not all(approval.get(f) for f in ("approver", "date", "receipt")):
                errors.append(f"{name}: missing human publication approval")
    return errors, counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-complete", action="store_true")
    args = parser.parse_args()
    errors, counts = validate(ROOT, args.require_complete)
    print("Refresh statuses: " + ", ".join(f"{s}={counts[s]}" for s in sorted(STATES)))
    if errors:
        print("\n".join(errors))
        return 1
    print("Inventory and recorded structure checks passed; source accuracy and review quality require substantive review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
