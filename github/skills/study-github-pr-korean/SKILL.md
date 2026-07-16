---
name: study-github-pr-korean
description: Teach a GitHub pull request in Korean as a structured learning walkthrough. Use when a user wants to understand a PR step by step, asks for a syllabus, or wants code changes explained without receiving a code review.
---

# Study GitHub PR in Korean

Turn a PR into a small Korean lesson. This is for comprehension, not code review.

## Workflow

1. Resolve the PR, then read its metadata, changed-file list, and diff stat before the full diff.
2. Use `pr-review-branch-sync` only when surrounding source context is needed. If sync is blocked, continue from GitHub diff context when possible.
3. Group files by user flow, subsystem, or concept; do not narrate them in diff order.
4. Create a syllabus before the walkthrough. If the user asked for a syllabus first, stop after it and ask whether to begin lesson 1.
5. Explain each lesson in Korean: goal, important files/functions/state, the flow from action to result, and a short checkpoint.
6. Run checks only when they clarify the behavior being taught. State what was actually run.

## Output

Start with `PR 한 줄 요약`, then `실라버스`. Use short lessons with `목표`, `코드 흐름`, and `체크포인트`. Use before/after tables only when behavior, API, state, or UI differences are clearer that way.

## Guardrails

- Do not leave GitHub comments, submit reviews, approve, request changes, or edit code.
- Explain the product goal before line-by-line details.
- Distinguish a learning note from a review finding.
