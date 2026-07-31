#!/usr/bin/env python3
"""Check baseline safety and lifecycle coverage in framework guide Markdown."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
GUIDES = ROOT / "docs" / "frameworks"
REVIEWS = ROOT / "docs" / "evidence-plan-reviews"
REQUIRED = (
    "original operational guidance",
    "engagement focus",
    "roles",
)
CONTRACT_LINK = "[universal engagement contract](../universal-engagement-contract.md)"
AI_TERMS = ("ai", "artificial intelligence")
EVIDENCE_HEADING = "## tailored evidence plan"
EVIDENCE_MARKERS = (
    "source and rights snapshot",
    "request and owner:",
    "validate and limit:",
    "ai and trigger:",
)

failures = []
evidence_ready = []
evidence_reviewed = []
for guide in sorted(GUIDES.glob("*.md")):
    if guide.name == "INDEX.md":
        continue
    body = guide.read_text(encoding="utf-8").lower()
    missing = [term for term in REQUIRED if term not in body]
    if CONTRACT_LINK not in body:
        missing.append("universal engagement contract link")
    if not any(term in body for term in AI_TERMS):
        missing.append("AI role")
    if "independent" not in body:
        missing.append("independent review role")
    if "cannot" not in body:
        missing.append("AI authority boundary")
    if "https://" not in body:
        missing.append("HTTPS official-source link")
    if EVIDENCE_HEADING in body:
        evidence_missing = [marker for marker in EVIDENCE_MARKERS if marker not in body]
        if evidence_missing:
            missing.append("incomplete tailored evidence plan: " + ", ".join(evidence_missing))
        else:
            evidence_ready.append(guide.name)
            if "**plan status:** independently reviewed" in body:
                receipt = REVIEWS / guide.name
                receipt_body = receipt.read_text(encoding="utf-8").lower() if receipt.exists() else ""
                receipt_markers = (
                    "official source:",
                    "source status and edition:",
                    "rights result:",
                    "source reviewer:",
                    "skeptical reviewer:",
                    "review method and result",
                    "review boundary",
                )
                absent = [marker for marker in receipt_markers if marker not in receipt_body]
                if absent:
                    missing.append("valid independent-review receipt: " + ", ".join(absent))
                else:
                    evidence_reviewed.append(guide.name)
    if missing:
        failures.append(f"{guide.relative_to(ROOT)}: missing {', '.join(missing)}")

index = (GUIDES / "INDEX.md").read_text(encoding="utf-8")
index_links = [
    Path(link).name
    for link in re.findall(r"\]\(([^)#]+\.md)\)", index)
    if "/" not in link
]
indexed = set(index_links)
for guide_name in sorted({name for name in index_links if index_links.count(name) > 1}):
    failures.append(f"docs/frameworks/INDEX.md: duplicate link to {guide_name}")
published = {guide.name for guide in GUIDES.glob("*.md") if guide.name != "INDEX.md"}
for guide_name in sorted(published - indexed):
    failures.append(f"docs/frameworks/INDEX.md: missing link to {guide_name}")
for guide_name in sorted(indexed - published):
    failures.append(f"docs/frameworks/INDEX.md: link target is absent: {guide_name}")

if failures:
    print("Guide validation failed:")
    print("\n".join(failures))
    sys.exit(1)
total = len(list(GUIDES.glob('*.md'))) - 1
print(f"Validated {total} framework guides.")
print(f"Valid tailored evidence-plan sections: {len(evidence_ready)}/{total}.")
print(f"Independently reviewed evidence plans: {len(evidence_reviewed)}/{total}.")
if "--require-evidence-plans" in sys.argv and len(evidence_ready) != total:
    print("Evidence-plan completeness failed: every published guide requires a complete tailored evidence plan.")
    sys.exit(1)
if "--require-reviewed-evidence-plans" in sys.argv and len(evidence_reviewed) != total:
    print("Evidence-plan review completeness failed: every published guide requires independent source and skeptical review receipts.")
    sys.exit(1)
