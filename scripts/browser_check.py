#!/usr/bin/env python3
"""Playwright QA for the course portal and fifty standalone articles."""
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
    "02._Fundamentals_of_Unconstrained_Optimization/01_2.2._Recognizing_a_Local_Minimum.html",
    "02._Fundamentals_of_Unconstrained_Optimization/02_2.3._Nonsmooth_Problems.html",
    "02._Fundamentals_of_Unconstrained_Optimization/2.4._Overview_of_Algorithms/00_2.4.1._Two_Strategies:_Line_Search_and_Trust_Region.html",
    "02._Fundamentals_of_Unconstrained_Optimization/2.4._Overview_of_Algorithms/01_2.4.2._Search_Directions_for_Line_Search_Methods.html",
    "02._Fundamentals_of_Unconstrained_Optimization/2.4._Overview_of_Algorithms/02_2.4.3._Models_for_Trust_Region_Methods.html",
    "02._Fundamentals_of_Unconstrained_Optimization/2.4._Overview_of_Algorithms/03_2.4.4._Scaling.html",
    "02._Fundamentals_of_Unconstrained_Optimization/04_2.5._Exercises.html",
    "03._Line_Search_Methods/00_3.1._Step_Length.html",
    "03._Line_Search_Methods/01_3.1.1._The_Wolfe_Conditions.html",
    "03._Line_Search_Methods/02_3.1.2._The_Goldstein_Conditions.html",
    "03._Line_Search_Methods/03_3.1.3._Sufficient_Decrease_and_Backtracking.html",
    "03._Line_Search_Methods/04_3.2._Convergence_of_Line_Search_Methods.html",
    "03._Line_Search_Methods/05_3.3._Rate_of_Convergence.html",
    "03._Line_Search_Methods/06_3.3.1._Convergence_Rate_of_Steepest_Descent.html",
    "03._Line_Search_Methods/07_3.3.2._Newton’s_Method.html",
    "03._Line_Search_Methods/08_3.3.3._Quasi_Newton_Methods.html",
    "03._Line_Search_Methods/09_3.4._Newton’s_Method_with_Hessian_Modification.html",
    "03._Line_Search_Methods/10_3.4.1._Eigenvalue_Modification.html",
    "03._Line_Search_Methods/11_3.4.2._Adding_a_Multiple_of_the_Identity.html",
    "03._Line_Search_Methods/12_3.4.3._Modified_Cholesky_Factorization.html",
    "03._Line_Search_Methods/13_3.4.4._Modified_Symmetric_Indefinite_Factorization.html",
    "03._Line_Search_Methods/14_3.5._Step_Length_Selection_Algorithms.html",
    "03._Line_Search_Methods/15_3.5.1._Interpolation.html",
    "03._Line_Search_Methods/16_3.5.2._Initial_Step_Length.html",
    "03._Line_Search_Methods/17_3.5.3._A_Line_Search_Algorithm_for_the_Wolfe_Conditions.html",
    "03._Line_Search_Methods/18_3.6._Notes_and_References.html",
    "03._Line_Search_Methods/19_3.7._Exercises.html",
    "04._Trust_Region_Methods/4.1._Algorithms_Based_on_the_Cauchy_Point/00_4.1.1._The_Cauchy_Point.html",
    "04._Trust_Region_Methods/4.1._Algorithms_Based_on_the_Cauchy_Point/01_4.1.2._Improving_on_the_Cauchy_Point.html",
    "04._Trust_Region_Methods/4.1._Algorithms_Based_on_the_Cauchy_Point/02_4.1.3._The_Dogleg_Method.html",
    "04._Trust_Region_Methods/4.1._Algorithms_Based_on_the_Cauchy_Point/03_4.1.4._Two_Dimensional_Subspace_Minimization.html",
    "04._Trust_Region_Methods/4.2._Global_Convergence/00_4.2.1._Reduction_Obtained_by_the_Cauchy_Point.html",
    "04._Trust_Region_Methods/4.2._Global_Convergence/01_4.2.2._Convergence_to_Stationary_Points.html",
    "04._Trust_Region_Methods/02_4.3._Iterative_Solution_of_the_Subproblem.html",
    "04._Trust_Region_Methods/03_4.3.1._The_Hard_Case.html",
    "04._Trust_Region_Methods/04_4.3.2._Proof_of_Theorem_4.1.html",
    "04._Trust_Region_Methods/05_4.3.3._Convergence_of_Algorithms_Based_on_Nearly_Exact_Solutions.html",
    "04._Trust_Region_Methods/06_4.4._Local_Convergence_of_Trust_Region_Newton_Methods.html",
    "04._Trust_Region_Methods/4.5._Other_Enhancements/00_4.5.1._Scaling.html",
    "04._Trust_Region_Methods/4.5._Other_Enhancements/01_4.5.2._Trust_Regions_in_Other_Norms.html",
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
    print("PASS: homepage search, fifty article interactions, 1440/768/390/360 px viewports, MathML geometry, figures and print emulation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
