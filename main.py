"""Safe entry point retained for compatibility with the original repository.

The former script recursively recreated the chapter scaffold and overwrote
README.md plus existing Markdown/Python article files. That destructive
bootstrap has been retired so authored course material cannot be lost.

To preview the course locally, run:
    python -m http.server 8000

For content checks, run:
    python scripts/validate_course.py
"""
from __future__ import annotations


def main() -> int:
    print("The old destructive scaffold generator is retired.")
    print("No files were created or overwritten.")
    print("Run 'python -m http.server 8000' to preview the course.")
    print("Run 'python scripts/validate_course.py' to validate authored content.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
