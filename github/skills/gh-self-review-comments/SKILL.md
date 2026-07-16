---
name: gh-self-review-comments
description: Add concise Korean reviewer-facing inline comments to the user's own GitHub pull request. Use for self-review annotations, Files Changed explanations, range comments, or short context for a non-obvious implementation decision.
---

# GitHub Self-Review Comments

Write annotations that help a reviewer understand the final diff quickly. They are not requests for change or a defense of the implementation.

## Workflow

1. Find the current branch PR with `gh pr view --json number,url,headRefOid,headRefName,baseRefName,title`; ask for a PR only when that fails.
2. Read changed hunks and surrounding code. Match the wording and detail level of any existing user-authored self-review comments.
3. Comment only where the diff has non-obvious reviewer value: a component role, setting group, behavior-affecting list, compatibility boundary, unusual branch, dense parsing/math, or mechanical move worth skimming.
4. Use a single line for one idea and a range for one coherent block. Skip generated files, lockfiles, formatting-only changes, and obvious code.
5. Write one concise Korean sentence; add a `<details>` block only when concrete extra context is needed.
6. Post against the PR head SHA with a JSON file. Use real line breaks, then report created comment links and any un-commentable target.

## Style

Explain visible behavior or data-flow meaning in plain language. Prefer “`basePrice`가 남아 있으면 절대 가격 기준이 우선돼 비율 UI와 어긋납니다.” over abstract architecture language. Do not praise, request a change, narrate work history, or paraphrase an identifier/test name.

## Guardrails

- Comment on final intent, not process history.
- If future maintainers need the explanation every time, improve the code or add a code comment instead.
- If the intended behavior is uncertain, ask before posting.
