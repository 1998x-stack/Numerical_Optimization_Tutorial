#!/usr/bin/env python3
"""Static validation for the authored Numerical Optimization course modules."""
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ARTICLES = [
    ("01._Introduction/00_1.1._Mathematical_Formulation.html",
     "01._Introduction/00_1.1._Mathematical_Formulation.md",
     "01._Introduction/00_1.1._Mathematical_Formulation.py",
     "evidence/chapter-01-1-1.json"),
    ("01._Introduction/01_1.2._Example:_A_Transportation_Problem.html",
     "01._Introduction/01_1.2._Example:_A_Transportation_Problem.md",
     "01._Introduction/01_1.2._Example:_A_Transportation_Problem.py",
     "evidence/chapter-01-1-2.json"),
    ("01._Introduction/02_1.3._Continuous_vs._Discrete_Optimization.html",
     "01._Introduction/02_1.3._Continuous_vs._Discrete_Optimization.md",
     "01._Introduction/02_1.3._Continuous_vs._Discrete_Optimization.py",
     "evidence/chapter-01-1-3.json"),
    ("01._Introduction/03_1.4._Constrained_and_Unconstrained_Optimization.html",
     "01._Introduction/03_1.4._Constrained_and_Unconstrained_Optimization.md",
     "01._Introduction/03_1.4._Constrained_and_Unconstrained_Optimization.py",
     "evidence/chapter-01-1-4.json"),
    ("01._Introduction/04_1.5._Global_and_Local_Optimization.html",
     "01._Introduction/04_1.5._Global_and_Local_Optimization.md",
     "01._Introduction/04_1.5._Global_and_Local_Optimization.py",
     "evidence/chapter-01-1-5.json"),
    ("01._Introduction/05_1.6._Stochastic_and_Deterministic_Optimization.html",
     "01._Introduction/05_1.6._Stochastic_and_Deterministic_Optimization.md",
     "01._Introduction/05_1.6._Stochastic_and_Deterministic_Optimization.py",
     "evidence/chapter-01-1-6.json"),
    ("01._Introduction/06_1.7._Convexity.html",
     "01._Introduction/06_1.7._Convexity.md",
     "01._Introduction/06_1.7._Convexity.py",
     "evidence/chapter-01-1-7.json"),
    ("01._Introduction/07_1.8._Optimization_Algorithms.html",
     "01._Introduction/07_1.8._Optimization_Algorithms.md",
     "01._Introduction/07_1.8._Optimization_Algorithms.py",
     "evidence/chapter-01-1-8.json"),
    ("01._Introduction/08_1.9._Notes_and_References.html",
     "01._Introduction/08_1.9._Notes_and_References.md",
     "01._Introduction/08_1.9._Notes_and_References.py",
     "evidence/chapter-01-1-9.json"),
    ("02._Fundamentals_of_Unconstrained_Optimization/00_2.1._What_Is_a_Solution?.html",
     "02._Fundamentals_of_Unconstrained_Optimization/00_2.1._What_Is_a_Solution?.md",
     "02._Fundamentals_of_Unconstrained_Optimization/00_2.1._What_Is_a_Solution?.py",
     "evidence/chapter-02-2-1.json"),
]


class ArticleParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.anchor_targets: list[str] = []
        self.local_resources: list[str] = []
        self.h1 = 0
        self.h2 = 0
        self.math = 0
        self.math_without_label = 0
        self.figures = 0
        self.figcaptions = 0
        self.figure_depth = 0
        self.figure_has_caption = False
        self.figure_has_image_alt = False
        self.figure_errors: list[str] = []
        self.demo_roots = 0
        self.external_assets: list[str] = []
        self.heading_stack: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.h1 += 1
        elif tag == "h2":
            self.h2 += 1
        elif tag == "math":
            self.math += 1
            if not attrs.get("aria-label") and not attrs.get("aria-labelledby"):
                self.math_without_label += 1
        elif tag == "figure":
            self.figures += 1
            self.figure_depth += 1
            self.figure_has_caption = False
            self.figure_has_image_alt = False
        elif tag == "figcaption" and self.figure_depth:
            self.figcaptions += 1
            self.figure_has_caption = True
        elif tag == "img" and self.figure_depth:
            self.figure_has_image_alt = bool(attrs.get("alt", "").strip())
        elif tag == "a" and attrs.get("href"):
            self.anchor_targets.append(attrs["href"])
        elif tag == "link" and "stylesheet" in attrs.get("rel", "").lower() and attrs.get("href"):
            self.local_resources.append(attrs["href"])
            if urlsplit(attrs["href"]).scheme in {"http", "https"}:
                self.external_assets.append(attrs["href"])
        elif tag == "script" and attrs.get("src"):
            self.local_resources.append(attrs["src"])
            if urlsplit(attrs["src"]).scheme in {"http", "https"}:
                self.external_assets.append(attrs["src"])
        if attrs.get("data-demo") is not None:
            self.demo_roots += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "figure" and self.figure_depth:
            if not self.figure_has_caption:
                self.figure_errors.append("figure has no figcaption")
            if not self.figure_has_image_alt:
                self.figure_errors.append("figure image has no non-empty alt text")
            self.figure_depth -= 1


def _resolve_local(source: Path, value: str) -> Path | None:
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc or value.startswith("mailto:"):
        return None
    path = unquote(parsed.path)
    if not path:
        return source
    return (source.parent / path).resolve()


def validate_article(relative_path: str) -> list[str]:
    path = ROOT / relative_path
    errors: list[str] = []
    if not path.exists():
        return [f"missing article: {relative_path}"]
    text = path.read_text(encoding="utf-8")
    parser = ArticleParser()
    parser.feed(text)
    if parser.h1 != 1:
        errors.append(f"{relative_path}: expected exactly one h1, found {parser.h1}")
    if parser.h2 < 5:
        errors.append(f"{relative_path}: expected at least five h2 sections, found {parser.h2}")
    if parser.math < 1:
        errors.append(f"{relative_path}: no MathML equations found")
    if parser.math_without_label:
        errors.append(f"{relative_path}: {parser.math_without_label} MathML elements lack an accessible label")
    if parser.figures < 1:
        errors.append(f"{relative_path}: no explanatory figure found")
    errors.extend(f"{relative_path}: {message}" for message in parser.figure_errors)
    if parser.demo_roots < 1:
        errors.append(f"{relative_path}: no interactive teaching demo found")
    if parser.external_assets:
        errors.append(f"{relative_path}: external CSS/JS dependency found: {parser.external_assets}")

    for resource in parser.local_resources:
        resolved = _resolve_local(path, resource)
        if resolved is not None and not resolved.exists():
            errors.append(f"{relative_path}: missing local asset {resource}")
    for target in parser.anchor_targets:
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or target.startswith("mailto:"):
            continue
        resolved = _resolve_local(path, target)
        if resolved is not None and not resolved.exists():
            errors.append(f"{relative_path}: broken local link {target}")
        if parsed.fragment and (resolved is None or resolved == path):
            if unquote(parsed.fragment) not in parser.ids:
                errors.append(f"{relative_path}: missing anchor target #{parsed.fragment}")
    if "cdnjs.cloudflare.com" in text or "cdn.jsdelivr.net" in text or "polyfill.io" in text:
        errors.append(f"{relative_path}: new article must not depend on a CDN")
    if "Lecture:" in text or "Content:" in text:
        errors.append(f"{relative_path}: placeholder metadata remains")
    return errors


def validate_repository() -> list[str]:
    errors: list[str] = []
    for html_path, md_path, py_path, evidence_path in ARTICLES:
        errors.extend(validate_article(html_path))
        for rel in (md_path, py_path, evidence_path):
            if not (ROOT / rel).exists():
                errors.append(f"missing paired artifact: {rel}")
        md = (ROOT / md_path).read_text(encoding="utf-8") if (ROOT / md_path).exists() else ""
        if len(md.strip()) < 700:
            errors.append(f"{md_path}: Markdown source is too short to stand alone")
        if (ROOT / py_path).exists():
            source = (ROOT / py_path).read_text(encoding="utf-8")
            try:
                compile(source, py_path, "exec")
            except SyntaxError as exc:
                errors.append(f"{py_path}: Python syntax error: {exc}")
        if (ROOT / evidence_path).exists():
            try:
                ledger = json.loads((ROOT / evidence_path).read_text(encoding="utf-8"))
                if not isinstance(ledger, list) or not ledger:
                    errors.append(f"{evidence_path}: evidence ledger must be a non-empty list")
                for item in ledger:
                    required = {"id", "claim", "kind", "source_url", "locator", "status", "notes"}
                    missing = required - set(item)
                    if missing:
                        errors.append(f"{evidence_path}: missing evidence fields {sorted(missing)}")
                    if item.get("status") not in {"verified", "derived", "illustrative", "unverified"}:
                        errors.append(f"{evidence_path}: invalid status {item.get('status')!r}")
            except (json.JSONDecodeError, OSError) as exc:
                errors.append(f"{evidence_path}: invalid JSON: {exc}")

    for rel in ("index.html", "README.md", "README.html", "AGENTS.md",
                "assets/course.css", "assets/course.js"):
        if not (ROOT / rel).exists():
            errors.append(f"missing project file: {rel}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "第一章 1.1–1.9 与第二章 2.1 共十篇已重构" not in readme:
        errors.append("README.md: scope/status statement is missing")
    index = (ROOT / "index.html").read_text(encoding="utf-8")
    if index.count('data-chapter-card') < 20:
        errors.append("index.html: expected 19 chapters plus Appendix A")
    if index.count('class="featured-card"') != 10:
        errors.append("index.html: expected exactly ten featured modules (two batches)")
    return errors


def main() -> int:
    errors = validate_repository()
    if errors:
        print("Course validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS: {len(ARTICLES)} authored articles, paired Markdown/Python/evidence files, local assets and course navigation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
