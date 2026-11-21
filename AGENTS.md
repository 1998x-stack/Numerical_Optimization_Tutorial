# Agent instructions

This repository is a numerical optimization learning course. Treat the Olah-style-posts workflow as a teaching and validation standard, not as permission to copy prose, diagrams, CSS, or code.

## Content contract

- Every new article must be independently understandable to a reader who opens that page first. Define the problem, symbols, assumptions, constraints, and all terms used in the derivation.
- Do not write meta-prose such as “the textbook introduces…” or “this chapter discusses…”. Explain the mathematical idea directly, with its own complete context.
- Prefer a concrete decision problem, then geometry, equations, a worked example, a runnable minimal implementation, failure modes, and exercises.
- Distinguish definitions, theorem assumptions, derived results, illustrative values, algorithm heuristics, and empirical evidence. Never invent numerical results or imply that a toy example is a benchmark reproduction.
- Keep notation consistent across prose, MathML, SVG, Markdown, Python, and evidence records. State sign conventions explicitly, especially for inequality constraints and KKT multipliers.
- Explain what an example program does and what it does not do. Do not call grid search, enumeration, or a teaching snippet a general-purpose solver.

## Olah-style teaching and design

- Use progressive explanation: question → model → mechanism → equation → worked example → executable check → limitations.
- One figure should answer one question. Use original SVG with viewBox, title, desc, stable IDs, readable labels, and a meaningful caption.
- Use native MathML for substantive equations; no CDN MathJax, external font or script dependencies in new articles.
- Use semantic HTML, one H1, ordered heading levels, keyboard-visible focus, responsive layout, reduced-motion support, and print styles.
- Keep diagrams understandable without JavaScript. Interactions are progressive enhancements and must expose accessible live output.
- Do not add production notes, toolchain claims, format boasts, AI-generated claims, or style references to article hero, byline, or footer.

## Source and evidence discipline

- Use the official textbook bibliographic record and primary sources when making source-dependent claims.
- Each article needs an evidence/*.json ledger with id, claim, kind, source_url, locator, status, and notes.
- Allowed statuses: verified, derived, illustrative, unverified. Mark algebraic/numerical results derived only after checking them independently.
- Do not reproduce copyrighted textbook paragraphs, figures, tables, or solution-manual content. Write original explanations and construct original toy data.

## Repository and release discipline

- Preserve existing chapter paths unless a migration plan updates every inbound link.
- Keep HTML, Markdown, and Python versions aligned: headings, symbols, worked-example values, conclusions, and code must agree.
- Update the course homepage and README when adding a batch. Keep completion status precise; directory entries are not evidence that an article is complete.
- The old recursive main.py scaffold generator is retired because it overwrote authored README, Markdown, and Python files. Do not reintroduce destructive generation; update curated files explicitly and validate them.
- Run python scripts/validate_course.py, python -m unittest discover -s tests -v, and python scripts/browser_check.py --output reports/course after relevant changes.
- Browser QA must cover 1440, 768, 390, and 360 pixel widths, print mode, console/page errors, local links, MathML geometry, and at least one meaningful interaction per interactive article.
- Use a topic branch and Pull Request. Inspect the diff and CI results before merging. Verify the Pages deployment and actual site before claiming that it is live.
