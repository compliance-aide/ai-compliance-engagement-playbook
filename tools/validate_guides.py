#!/usr/bin/env python3
"""Check baseline safety and lifecycle coverage in framework guide Markdown."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
GUIDES = ROOT / "docs" / "frameworks"
REQUIRED = ("original operational guidance", "engagement focus", "roles")
AI_TERMS = ("ai", "artificial intelligence")

failures = []
for guide in sorted(GUIDES.glob("*.md")):
    if guide.name == "INDEX.md":
        continue
    body = guide.read_text(encoding="utf-8").lower()
    missing = [term for term in REQUIRED if term not in body]
    if not any(term in body for term in AI_TERMS):
        missing.append("AI role")
    if "independent" not in body:
        missing.append("independent review role")
    if "http" not in body:
        missing.append("official-source link")
    if missing:
        failures.append(f"{guide.relative_to(ROOT)}: missing {', '.join(missing)}")

index = (GUIDES / "INDEX.md").read_text(encoding="utf-8")
indexed = {
    Path(link).name
    for link in re.findall(r"\]\(([^)#]+\.md)\)", index)
    if "/" not in link
}
published = {guide.name for guide in GUIDES.glob("*.md") if guide.name != "INDEX.md"}
for guide_name in sorted(published - indexed):
    failures.append(f"docs/frameworks/INDEX.md: missing link to {guide_name}")
for guide_name in sorted(indexed - published):
    failures.append(f"docs/frameworks/INDEX.md: link target is absent: {guide_name}")

if failures:
    print("Guide validation failed:")
    print("\n".join(failures))
    sys.exit(1)
print(f"Validated {len(list(GUIDES.glob('*.md'))) - 1} framework guides.")
