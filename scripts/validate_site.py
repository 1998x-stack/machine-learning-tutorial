#!/usr/bin/env python3
"""Offline static-site and chapter/figure integrity checks."""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ERRORS = []

class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.h1 = 0
        self.figures = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "h1":
            self.h1 += 1
        if tag == "figure":
            self.figures += 1
        for k in ("href", "src"):
            if a.get(k):
                self.links.append(a[k])

def check_page(path, require_article=False, min_figures=2):
    html = path.read_text(encoding="utf-8")
    parsed = Links()
    parsed.feed(html)
    if parsed.h1 != 1:
        ERRORS.append(f"{path.relative_to(ROOT)}: expected one H1, got {parsed.h1}")
    if require_article and (parsed.figures < min_figures or "<article" not in html or "<main" not in html):
        ERRORS.append(f"{path.relative_to(ROOT)}: article missing required figures or semantic article/main")
    for link in parsed.links:
        u = urlsplit(link)
        if u.scheme or u.netloc or link.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
            continue
        dest = (path.parent / unquote(u.path)).resolve()
        if not dest.is_relative_to(DOCS.resolve()) or not dest.is_file():
            ERRORS.append(f"{path.relative_to(ROOT)}: broken link {link}")

def main():
    catalog = json.loads((DOCS / "courses.json").read_text(encoding="utf-8"))
    if len(catalog.get("chapters", [])) != 28:
        ERRORS.append("catalog must list 28 lessons")
    check_page(DOCS / "index.html")
    for i in range(1, 29):
        p = DOCS / "chapters" / f"{i:02}.html"
        if not p.is_file():
            ERRORS.append(f"missing {p}")
            continue
        if i <= 28:
            check_page(p, require_article=True, min_figures=5 if i >= 26 else (3 if i >= 11 else 2))
        if not (ROOT / f"{i:02}.html").is_file():
            ERRORS.append(f"missing root legacy redirect {i:02}.html")
        if not (DOCS / f"{i:02}.html").is_file():
            ERRORS.append(f"missing Pages legacy redirect {i:02}.html")
    svgs = list((DOCS / "assets" / "svg").rglob("*.svg"))
    for f in svgs:
        try:
            root = ET.parse(f).getroot()
            if not root.tag.endswith("svg") or not root.get("viewBox"):
                ERRORS.append(f"{f.relative_to(ROOT)}: missing SVG viewBox")
            if not any(x.tag.endswith("title") for x in root):
                ERRORS.append(f"{f.relative_to(ROOT)}: missing SVG title")
            if not any(x.tag.endswith("desc") for x in root):
                ERRORS.append(f"{f.relative_to(ROOT)}: missing SVG desc")
        except ET.ParseError as e:
            ERRORS.append(f"{f.relative_to(ROOT)}: invalid SVG {e}")
    for i in range(11, 29):
        chapter_svgs = list((DOCS / "assets" / "svg" / f"{i:02}").glob("*.svg"))
        if len(chapter_svgs) < (5 if i >= 26 else 3):
            ERRORS.append(f"chapter {i:02}: expected >= {5 if i >= 26 else 3} standalone SVG files")
    if len(svgs) < 94:
        ERRORS.append(f"expected >=93 chapter diagrams plus homepage map (94 SVGs), found {len(svgs)}")
    for i in range(16, 29):
        evidence = DOCS / "evidence" / f"{i:02}.json"
        if not evidence.is_file():
            ERRORS.append(f"missing evidence ledger {evidence.relative_to(ROOT)}")
            continue
        try:
            ledger = json.loads(evidence.read_text(encoding="utf-8"))
            claims = ledger.get("claims", [])
            if not claims:
                ERRORS.append(f"{evidence.relative_to(ROOT)}: empty claims")
            for claim in claims:
                required = {"id", "claim", "kind", "source_url", "locator", "status", "notes"}
                if not required.issubset(claim) or claim.get("status") not in {"verified", "derived", "illustrative", "unverified"}:
                    ERRORS.append(f"{evidence.relative_to(ROOT)}: malformed claim {claim.get('id', '<unknown>')}")
        except (json.JSONDecodeError, AttributeError) as exc:
            ERRORS.append(f"{evidence.relative_to(ROOT)}: invalid evidence JSON {exc}")
    if ERRORS:
        print("\n".join("ERROR " + s for s in ERRORS))
        return 1
    print(f"PASS: 28 lessons, 28 updated article pages, {len(svgs)} valid standalone SVGs, local assets resolved")
    return 0

if __name__ == "__main__":
    sys.exit(main())
