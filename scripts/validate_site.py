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

def check_page(path, require_article=False):
    html = path.read_text(encoding="utf-8")
    parsed = Links()
    parsed.feed(html)
    if parsed.h1 != 1:
        ERRORS.append(f"{path.relative_to(ROOT)}: expected one H1, got {parsed.h1}")
    if require_article and (parsed.figures < 2 or "<article" not in html or "<main" not in html):
        ERRORS.append(f"{path.relative_to(ROOT)}: article missing >=2 figures or semantic article/main")
    for link in parsed.links:
        u = urlsplit(link)
        if u.scheme or u.netloc or link.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
            continue
        dest = (path.parent / unquote(u.path)).resolve()
        if not dest.is_relative_to(ROOT.resolve()) or not dest.is_file():
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
        if i <= 5:
            check_page(p, require_article=True)
        if not (ROOT / f"{i:02}.html").is_file():
            ERRORS.append(f"missing legacy redirect {i:02}.html")
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
    if len(svgs) < 10:
        ERRORS.append(f"expected >=10 diagrams for first five lessons, found {len(svgs)}")
    if ERRORS:
        print("\n".join("ERROR " + s for s in ERRORS))
        return 1
    print(f"PASS: 28 lessons, 5 updated article pages, {len(svgs)} valid standalone SVGs, local assets resolved")
    return 0

if __name__ == "__main__":
    sys.exit(main())
