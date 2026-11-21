"""Independent mathematical checks and HTML/Markdown/Python consistency."""
from __future__ import annotations

import math
import re
import unittest
from fractions import Fraction
from html import unescape

from scripts.validate_course import ARTICLES, ROOT


class CrossVerificationTests(unittest.TestCase):
    def test_all_article_code_is_same_as_source(self):
        for html_path, md_path, py_path, _ in ARTICLES:
            with self.subTest(article=html_path):
                html = (ROOT / html_path).read_text(encoding="utf-8")
                markdown = (ROOT / md_path).read_text(encoding="utf-8")
                source = (ROOT / py_path).read_text(encoding="utf-8").strip()
                html_match = re.search(r"<pre><code>(.*?)</code></pre>", html, re.DOTALL)
                md_match = re.search(r"\x60{3}python\s*\n(.*?)\n\x60{3}", markdown, re.DOTALL)
                self.assertIsNotNone(html_match, "HTML code block missing")
                self.assertIsNotNone(md_match, "Markdown code block missing")
                self.assertEqual(unescape(html_match.group(1)).strip(), source)
                self.assertEqual(md_match.group(1).strip(), source)

    def test_stochastic_example_exact(self):
        scenarios = (Fraction(1), Fraction(2), Fraction(4))
        mean = sum(scenarios) / len(scenarios)
        risk = lambda x: sum((x - d) ** 2 for d in scenarios) / len(scenarios)
        self.assertEqual(mean, Fraction(7, 3))
        self.assertEqual(risk(mean), Fraction(14, 9))
        self.assertEqual(risk(Fraction(2)) - risk(mean), Fraction(1, 9))

    def test_convexity_chord_gap(self):
        theta = Fraction(1, 4)
        f = lambda x: (x - 1) ** 2
        a, b = Fraction(0), Fraction(4)
        x = theta * a + (1 - theta) * b
        chord = theta * f(a) + (1 - theta) * f(b)
        self.assertEqual(x, 3)
        self.assertEqual(f(x), 4)
        self.assertEqual(chord, 7)
        self.assertEqual(chord - f(x), 3)
        self.assertEqual(16 * theta * (1 - theta), 3)

    def test_descent_and_newton_step(self):
        alpha = Fraction(1, 5)
        x0 = Fraction(0)
        gradient = 2 * (x0 - 3)
        self.assertEqual(x0 - alpha * gradient, Fraction(6, 5))
        self.assertEqual(x0 - gradient / 2, 3)
        self.assertEqual(1 - 2 * alpha, Fraction(3, 5))

    def test_central_difference_quadratic_exact_arithmetic(self):
        x, h = Fraction(5, 4), Fraction(1, 10)
        f = lambda z: (z - 2) ** 2 + 1
        derivative = (f(x + h) - f(x - h)) / (2 * h)
        self.assertEqual(derivative, Fraction(-3, 2))

    def test_infimum_not_attained_and_stationary_counterexample(self):
        self.assertGreater(math.exp(-10), 0.0)
        self.assertLess(math.exp(-10), math.exp(-5))
        cubic = lambda x: x ** 3
        self.assertEqual(3 * 0 ** 2, 0)
        self.assertLess(cubic(-0.1), cubic(0))
        self.assertLess(cubic(0), cubic(0.1))


if __name__ == "__main__":
    unittest.main()
