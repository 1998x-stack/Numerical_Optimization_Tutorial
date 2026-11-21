"""Regression tests for all eighteen authored course modules."""
from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

from scripts.validate_course import ARTICLES, ROOT, validate_article, validate_repository


class CourseContentTests(unittest.TestCase):
    def test_all_authored_articles_pass_static_checks(self):
        for html_path, _, _, _ in ARTICLES:
            with self.subTest(article=html_path):
                self.assertEqual(validate_article(html_path), [])

    def test_repository_contract(self):
        self.assertEqual(validate_repository(), [])

    def test_python_examples_execute_and_assert(self):
        for _, _, py_path, _ in ARTICLES:
            with self.subTest(example=py_path):
                result = subprocess.run(
                    [sys.executable, str(ROOT / py_path)],
                    cwd=ROOT,
                    text=True,
                    capture_output=True,
                    check=False,
                )
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_markdown_and_html_share_article_identity(self):
        for html_path, md_path, _, _ in ARTICLES:
            with self.subTest(article=html_path):
                html = (ROOT / html_path).read_text(encoding="utf-8")
                markdown = (ROOT / md_path).read_text(encoding="utf-8")
                title = markdown.splitlines()[0].lstrip("# ").strip()
                self.assertIn(title.split(" ", 1)[1], html)


if __name__ == "__main__":
    unittest.main()
