#!/usr/bin/env python3
"""Playwright QA for the new course portal and ten standalone articles."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLES = [
    "01._Introduction/00_1.1._Mathematical_Formulation.html",
    "01._Introduction/01_1.2._Example:_A_Transportation_Problem.html",
    "01._Introduction/02_1.3._Continuous_vs._Discrete_Optimization.html",
    "01._Introduction/03_1.4._Constrained_and_Unconstrained_Optimization.html",
    "01._Introduction/04_1.5._Global_and_Local_Optimization.html",
    "01._Introduction/05_1.6._Stochastic_and_Deterministic_Optimization.html",
    "01._Introduction/06_1.7._Convexity.html",
    "01._Introduction/07_1.8._Optimization_Algorithms.html",
    "01._Introduction/08_1.9._Notes_and_References.html",
    "02._Fundamentals_of_Unconstrained_Optimization/00_2.1._What_Is_a_Solution?.html",
]
VIEWPORTS = [(1440, 900), (768, 1024), (390, 844), (360, 800)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="reports/course")
    args = parser.parse_args()
    output = ROOT / args.output
    output.mkdir(parents=True, exist_ok=True)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright is not installed. Install requirements-dev.txt and Chromium.")
        return 2

    report = {"pages": [], "summary": {"page_errors": 0, "overflow_failures": 0, "interaction_failures": 0}}
    failures = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        home = browser.new_page(viewport={"width": 1440, "height": 900})
        home_errors = []
        home.on("pageerror", lambda error: home_errors.append(str(error)))
        home.goto((ROOT / "index.html").as_uri(), wait_until="load")
        search = home.locator("[data-course-search]")
        search.fill("trust region")
        visible = home.locator("[data-chapter-card]:visible").count()
        if visible != 1:
            failures.append(f"homepage search expected one Trust Region result, found {visible}")
        search.fill("")
        home.screenshot(path=str(output / "home-1440.png"), full_page=True)
        report["pages"].append({"path": "index.html", "console_errors": home_errors, "search_visible": visible})
        report["summary"]["page_errors"] += len(home_errors)

        for relative in ARTICLES:
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            errors = []
            page.on("pageerror", lambda error, bucket=errors: bucket.append(str(error)))
            page.on("console", lambda message, bucket=errors: bucket.append(message.text) if message.type == "error" else None)
            page.goto((ROOT / relative).as_uri(), wait_until="load")
            dimensions = []
            for width, height in VIEWPORTS:
                page.set_viewport_size({"width": width, "height": height})
                page.wait_for_timeout(80)
                metrics = page.evaluate("""() => ({
                    viewport: document.documentElement.clientWidth,
                    document: document.documentElement.scrollWidth,
                    body: document.body.scrollWidth,
                    formulas: [...document.querySelectorAll('math')].map(node => {
                      const r = node.getBoundingClientRect();
                      return {width: r.width, height: r.height};
                    }),
                    images: [...document.querySelectorAll('figure img')].map(img => ({
                      alt: img.alt, loaded: img.complete && img.naturalWidth > 0
                    }))
                })""")
                dimensions.append({"width": width, **metrics})
                if metrics["document"] > metrics["viewport"] + 1:
                    failures.append(f"{relative}: horizontal overflow at {width}px ({metrics['document']} > {metrics['viewport']})")
                    report["summary"]["overflow_failures"] += 1
                if not metrics["formulas"] or any(item["width"] <= 0 or item["height"] <= 0 for item in metrics["formulas"]):
                    failures.append(f"{relative}: MathML has no visible geometry at {width}px")
                if any(not image["loaded"] or not image["alt"] for image in metrics["images"]):
                    failures.append(f"{relative}: figure image missing, unloaded, or has no alt text")

                if width in (1440, 390):
                    safe_name = re.sub(r"[^A-Za-z0-9._-]+", "-", Path(relative).stem).strip("-")
                    page.screenshot(path=str(output / f"{safe_name}-{width}.png"), full_page=True)

            demo = page.locator("[data-demo] input").first
            before = page.locator("[data-output]").inner_text()
            current = demo.input_value()
            minimum = demo.get_attribute("min")
            maximum = demo.get_attribute("max")
            next_value = minimum if current != minimum else maximum
            demo.evaluate("(el, value) => { el.value = value; el.dispatchEvent(new Event('input', {bubbles:true})); }", next_value)
            after = page.locator("[data-output]").inner_text()
            if not after or after == before:
                failures.append(f"{relative}: interaction did not change the accessible output")
                report["summary"]["interaction_failures"] += 1

            # Print media represents a paper-sized viewport, not the last 360 px mobile viewport.
            page.set_viewport_size({"width": 1024, "height": 768})
            page.emulate_media(media="print")
            print_overflow = page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth + 1")
            if print_overflow:
                failures.append(f"{relative}: horizontal overflow in print emulation")
            report["pages"].append({
                "path": relative,
                "console_errors": errors,
                "viewports": dimensions,
                "interaction_changed_output": before != after,
                "print_horizontal_overflow": print_overflow,
            })
            report["summary"]["page_errors"] += len(errors)
            if errors:
                failures.append(f"{relative}: browser console/page errors: {errors}")
            page.close()

        browser.close()

    report["failures"] = failures
    (output / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    if failures:
        print("Browser QA failed:")
        for failure in failures:
            print("-", failure)
        return 1
    print("PASS: homepage search, ten article interactions, 1440/768/390/360 px viewports, MathML geometry, figures and print emulation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
