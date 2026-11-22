#!/usr/bin/env python3
"""Evidence, semantic HTML, MathML, SVG, navigation and static-site release gates."""
import html
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
ALLOWED_STATUS = {"verified", "derived", "illustrative", "unverified"}
MATH_ARITY = {"mfrac": 2, "munder": 2, "mover": 2, "munderover": 3,
              "msub": 2, "msup": 2, "msubsup": 3}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr"}

class PageAudit(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.images = []
        self.figures = []
        self.figure_stack = []
        self.in_caption = False
        self.svg_depth = 0
        self.math_attrs = []
        self.math_inside_svg = 0
        self.headings = []
        self.sections = []
        self.pre_attrs = []
        self.figure_scroll_attrs = []
        self.lang = None
        self.stack = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        if a.get("id"):
            self.ids.append(a["id"])
        for key in ("href", "src"):
            if a.get(key):
                self.links.append((a[key], a))
        if tag == "img":
            self.images.append(a.get("alt"))
            if self.figure_stack:
                self.figures[self.figure_stack[-1]]["media"] = True
        if tag == "figure":
            self.figures.append({"caption": "", "media": False})
            self.figure_stack.append(len(self.figures) - 1)
        if tag == "figcaption" and self.figure_stack:
            self.in_caption = True
        if tag == "svg":
            self.svg_depth += 1
            if self.figure_stack:
                self.figures[self.figure_stack[-1]]["media"] = True
        if tag == "math":
            self.math_attrs.append(a)
            if self.svg_depth:
                self.math_inside_svg += 1
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.headings.append(int(tag[1]))
        if tag == "section" and a.get("id"):
            self.sections.append((a["id"], a.get("aria-labelledby")))
        if tag == "pre":
            self.pre_attrs.append(a)
        if tag == "div" and "figure-scroll" in a.get("class", "").split():
            self.figure_scroll_attrs.append(a)
        if tag not in VOID:
            self.stack.append(tag)

    def handle_data(self, data):
        if self.in_caption and self.figure_stack:
            self.figures[self.figure_stack[-1]]["caption"] += data

    def handle_endtag(self, tag):
        if tag == "figcaption":
            self.in_caption = False
        if tag == "figure" and self.figure_stack:
            self.figure_stack.pop()
        if tag == "svg" and self.svg_depth:
            self.svg_depth -= 1
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == tag:
                del self.stack[i:]
                break

def error(path, message):
    ERRORS.append(f"{path.relative_to(ROOT)}: {message}")

def local_target(path, raw):
    u = urlsplit(raw)
    if u.scheme or u.netloc or raw.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return None
    if not u.path:
        return path
    return (path.parent / unquote(u.path)).resolve()

def check_math(path, source, audit):
    if audit.math_inside_svg:
        error(path, "MathML must not be nested inside SVG")
    if len(audit.math_attrs) != len(re.findall(r"<math\b", source, re.I)):
        error(path, "MathML parsing count mismatch")
    for i, attrs in enumerate(audit.math_attrs, 1):
        if not (attrs.get("aria-label") or attrs.get("aria-labelledby")):
            error(path, f"MathML expression {i} has no accessible name")
    wrappers = re.findall(r"<div\b([^>]*)class=\"eq\"([^>]*)>", source, re.I)
    for i, (left, right) in enumerate(wrappers, 1):
        attrs = left + " " + right
        if "tabindex=\"0\"" not in attrs or "role=\"group\"" not in attrs or "aria-label=" not in attrs:
            error(path, f"equation region {i} must be named, focusable and grouped")
    for match in re.finditer(r"<math\b[^>]*>[\s\S]*?</math>", source, re.I):
        try:
            root = ET.fromstring(match.group(0))
        except ET.ParseError as exc:
            error(path, f"invalid MathML fragment: {exc}")
            continue
        for node in root.iter():
            tag = node.tag.rsplit("}", 1)[-1]
            if tag in MATH_ARITY and len(list(node)) != MATH_ARITY[tag]:
                error(path, f"MathML {tag} requires {MATH_ARITY[tag]} element children, got {len(list(node))}")

def check_svg(path):
    try:
        root = ET.parse(path).getroot()
        if not root.tag.endswith("svg"):
            error(path, "root element is not svg")
        view = root.get("viewBox", "").replace(",", " ").split()
        if len(view) != 4 or float(view[2]) <= 0 or float(view[3]) <= 0:
            error(path, "missing or invalid positive viewBox")
        title = next((x for x in root if x.tag.endswith("title")), None)
        desc = next((x for x in root if x.tag.endswith("desc")), None)
        if title is None or not "".join(title.itertext()).strip():
            error(path, "missing non-empty SVG title")
        if desc is None or not "".join(desc.itertext()).strip():
            error(path, "missing non-empty SVG description")
        ids = [x.get("id") for x in root.iter() if x.get("id")]
        if len(ids) != len(set(ids)):
            error(path, "duplicate SVG IDs")
        for node in root.iter():
            tag = node.tag.rsplit("}", 1)[-1].lower()
            if tag == "script":
                error(path, "script element is not allowed in a teaching SVG")
            for key in node.attrib:
                if key.lower().startswith("on"):
                    error(path, f"event-handler attribute {key} is not allowed in SVG")
    except (ET.ParseError, ValueError) as exc:
        error(path, f"invalid SVG XML/viewBox: {exc}")

def main():
    catalog_path = DOCS / "courses.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    chapters = catalog.get("chapters", [])
    if len(chapters) != 28:
        ERRORS.append("docs/courses.json must list exactly 28 chapters")
    numbers = [x.get("num") for x in chapters]
    if numbers != [f"{i:02}" for i in range(1, 29)]:
        ERRORS.append("course catalog chapter numbers must be unique, ordered 01–28")
    by_num = {x.get("num"): x for x in chapters}
    for item in chapters:
        related = item.get("related", [])
        if len(related) < 3 or len({x.get("num") for x in related}) != len(related):
            ERRORS.append(f"catalog chapter {item.get('num')}: related links must be >=3 and unique")
        for link in related:
            if link.get("num") not in by_num or link.get("num") == item.get("num") or not link.get("reason"):
                ERRORS.append(f"catalog chapter {item.get('num')}: invalid related link {link}")

    page_paths = [DOCS / "index.html"] + [
        DOCS / "chapters" / f"{i:02}.html" for i in range(1, 29)
    ]
    audits = {}
    for path in page_paths:
        if not path.is_file():
            ERRORS.append(f"missing page {path.relative_to(ROOT)}")
            continue
        source = path.read_text(encoding="utf-8")
        audit = PageAudit()
        audit.feed(source)
        audits[path.resolve()] = audit
        if audit.lang != "zh-CN":
            error(path, "html lang must be zh-CN")
        if audit.ids and len(audit.ids) != len(set(audit.ids)):
            error(path, "duplicate HTML id")
        h1_count = source.lower().count("<h1")
        if h1_count != 1:
            error(path, f"expected one H1, got {h1_count}")
        previous = 0
        for level in audit.headings:
            if previous and level > previous + 1:
                error(path, f"heading hierarchy skips from H{previous} to H{level}")
            previous = level
        for target in [label for _, label in audit.sections if label]:
            if target not in audit.ids:
                error(path, f"section aria-labelledby target #{target} does not exist")
        for i, fig in enumerate(audit.figures, 1):
            if not fig["media"] or not fig["caption"].strip():
                error(path, f"figure {i} needs media and a non-empty figcaption")
        for i, alt in enumerate(audit.images, 1):
            if alt is None or not alt.strip():
                error(path, f"image {i} has no useful alt text")
        for i, attrs in enumerate(audit.pre_attrs, 1):
            if attrs.get("tabindex") != "0" or attrs.get("role") != "region" or not attrs.get("aria-label"):
                error(path, f"pre block {i} must be a named keyboard-scrollable region")
        for i, attrs in enumerate(audit.figure_scroll_attrs, 1):
            if attrs.get("tabindex") != "0" or attrs.get("role") != "region" or not attrs.get("aria-label"):
                error(path, f"figure scroll region {i} must be named and keyboard-focusable")
        check_math(path, source, audit)

        if path.name != "index.html":
            num = path.stem
            if "<main id=\"content\"" not in source or "<article" not in source:
                error(path, "article requires main#content and article landmarks")
            if not re.search(r'<meta name="description" content="[^"]{30,}"', source):
                error(path, "missing substantive meta description")
            expected_url = f"https://1998x-stack.github.io/machine-learning-tutorial/chapters/{num}.html"
            if f'<link rel="canonical" href="{expected_url}">' not in source:
                error(path, "canonical URL missing or incorrect")
            if source.count('property="og:title"') != 1 or source.count('property="og:description"') != 1:
                error(path, "Open Graph title/description metadata missing")
            if 'class="skip-link" href="#content"' not in source:
                error(path, "skip link must target main#content")
            nav = re.search(r'<nav aria-label="文章目录">([\s\S]*?)</nav>', source)
            if not nav:
                error(path, "missing article table-of-contents nav")
            else:
                nav_ids = set(re.findall(r'href="#([^"]+)"', nav.group(1)))
                section_ids = {sid for sid, _ in audit.sections}
                missing = sorted(section_ids - nav_ids)
                if missing:
                    error(path, f"article TOC misses section anchors: {', '.join(missing)}")
            if 'id="related-concepts"' not in source:
                error(path, "missing related-concepts section")
            else:
                rel = re.search(r'<section id="related-concepts"[\s\S]*?</section>', source)
                targets = re.findall(r'href="(\d{2})\.html"', rel.group(0)) if rel else []
                expected = [x["num"] for x in by_num[num].get("related", [])]
                if targets != expected:
                    error(path, "related-concepts links do not match docs/courses.json")
            external = [url for url, _ in audit.links if url.startswith("https://") and "github.com/1998x-stack/machine-learning-tutorial" not in url]
            if len(external) < 2:
                error(path, "article should cite at least two non-repository primary/official sources")
            if not re.search(r'<nav class="article-footer"', source):
                error(path, "missing previous/home/next article navigation")
            if not re.search(r'<section[^>]*>[\s\S]*class="refs"', source):
                error(path, "missing visible references list")

        for raw, attrs in audit.links:
            target = local_target(path, raw)
            if target is None:
                if attrs.get("target") == "_blank" and "noopener" not in attrs.get("rel", "").split():
                    error(path, f"external target=_blank link lacks rel=noopener: {raw}")
                continue
            if not target.is_relative_to(DOCS.resolve()) or not target.is_file():
                error(path, f"broken local resource/link {raw}")

    # Resolve local fragment links after every target page has been parsed.
    for path in page_paths:
        if not path.is_file():
            continue
        audit = audits.get(path.resolve())
        if not audit:
            continue
        for raw, _ in audit.links:
            u = urlsplit(raw)
            if not u.fragment or u.scheme or u.netloc:
                continue
            target = local_target(path, raw)
            if not target or target.resolve() not in audits:
                continue
            if unquote(u.fragment) not in audits[target.resolve()].ids:
                error(path, f"broken fragment target {raw}")

    home = (DOCS / "index.html").read_text(encoding="utf-8")
    home_cards = re.findall(r'<a class="lesson-card"[^>]*href="chapters/(\d{2})\.html"', home)
    if sorted(home_cards) != [f"{i:02}" for i in range(1, 29)]:
        ERRORS.append("homepage must link to every chapter exactly once")
    if 'id="study-paths"' not in home or 'aria-live="polite"' not in home:
        ERRORS.append("homepage must expose goal-based paths and an announced search status")

    for i in range(1, 29):
        for legacy in (ROOT / f"{i:02}.html", DOCS / f"{i:02}.html"):
            if not legacy.is_file():
                ERRORS.append(f"missing legacy redirect {legacy.relative_to(ROOT)}")

    svgs = list((DOCS / "assets" / "svg").rglob("*.svg"))
    for svg in svgs:
        check_svg(svg)
    if len(svgs) < 94:
        ERRORS.append(f"expected >=94 standalone SVGs, found {len(svgs)}")
    for i in range(11, 29):
        chapter_svgs = list((DOCS / "assets" / "svg" / f"{i:02}").glob("*.svg"))
        if len(chapter_svgs) < (5 if i >= 26 else 3):
            ERRORS.append(f"chapter {i:02}: expected >= {5 if i >= 26 else 3} standalone SVGs")

    for i in range(1, 29):
        path = DOCS / "evidence" / f"{i:02}.json"
        if not path.is_file():
            ERRORS.append(f"missing evidence ledger {path.relative_to(ROOT)}")
            continue
        try:
            ledger = json.loads(path.read_text(encoding="utf-8"))
            claims = ledger.get("claims", [])
            if len(claims) < 4:
                error(path, "at least four claim records are required")
            seen = set()
            for claim in claims:
                required = {"id", "claim", "kind", "source_url", "locator", "status", "notes"}
                if not required.issubset(claim) or claim.get("status") not in ALLOWED_STATUS:
                    error(path, f"malformed claim {claim.get('id', '<unknown>')}")
                    continue
                if claim["id"] in seen:
                    error(path, f"duplicate claim id {claim['id']}")
                seen.add(claim["id"])
                if not all(str(claim[k]).strip() for k in ("claim", "kind", "source_url", "locator", "notes")):
                    error(path, f"incomplete claim {claim['id']}")
                if not claim["source_url"].startswith("https://"):
                    error(path, f"claim {claim['id']} source must use HTTPS")
        except (json.JSONDecodeError, AttributeError) as exc:
            error(path, f"invalid evidence JSON: {exc}")

    sitemap = DOCS / "sitemap.xml"
    if not sitemap.is_file():
        ERRORS.append("missing docs/sitemap.xml")
    else:
        try:
            urls = ET.parse(sitemap).getroot().findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url")
            if len(urls) != 29:
                ERRORS.append(f"sitemap must contain 29 canonical URLs, found {len(urls)}")
        except ET.ParseError as exc:
            ERRORS.append(f"invalid sitemap XML: {exc}")
    if not (DOCS / "robots.txt").is_file():
        ERRORS.append("missing docs/robots.txt")

    if ERRORS:
        print("\n".join("ERROR " + item for item in ERRORS))
        return 1
    print(f"PASS: 28 chapters, 28 evidence ledgers, {len(svgs)} valid SVGs, MathML/anchors/related links, canonical metadata and local assets")
    return 0

if __name__ == "__main__":
    sys.exit(main())
