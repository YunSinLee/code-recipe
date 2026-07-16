---
name: gh-pr-review-korean
description: Review GitHub pull requests in Korean with a synced PR worktree, plain-language explanation, and actionable inline comments only. Use for Korean PR review requests, pending inline comments, or review-thread replies.
---

# Korean GitHub PR Review

Review from the PR head branch and report only issues that merit a change. Use `pr-review-branch-sync` before reading local files.

## Workflow

1. Resolve the PR number or URL. If the user asks, rename the thread to `[리뷰] <PR_NUMBER> 리뷰`.
2. Sync the current worktree with `pr-review-branch-sync`, then verify the branch.
3. Read `gh pr view <PR> --json number,title,body,baseRefName,headRefName,author,url`, the changed-file list, relevant hunks, surrounding code, and relevant tests.
4. Explain the PR briefly in Korean before deep review. For non-trivial changes, group the code explanation by user flow, file, state, API, or event path.
5. Check correctness, user flows, data and permission safety, regression risk, performance, and risky missing tests. Run targeted checks when practical.
6. Create Korean inline comments only for actionable findings. Keep them clear, line-specific, and explain the failure and smallest fix direction.
7. Keep review creation pending by default. Publish only when the user explicitly requests it. Use real line breaks in every GitHub body.

## Rechecks

Read existing inline comments and maintainer replies before re-reviewing. Report both reply status and actual code/runtime status.

## Output

Use `PR 쉽게 설명`, `코드별 변경 설명`, `리뷰 결과`, and `작업 내용`. State findings first. Do not leave praise, style-only comments, or top-level findings when the user requested inline comments.

## Guardrails

- Do not inspect or review before branch sync succeeds.
- Do not modify code unless the user asks for a fix.
- Do not submit `COMMENT`, `REQUEST_CHANGES`, or `APPROVE` without explicit permission.
