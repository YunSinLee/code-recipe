---
name: pr-review-branch-sync
description: Align the current worktree with a GitHub pull request head branch before PR review, Files Changed inspection, local runtime checks, or PR code explanation. Use whenever local PR context must match the head branch.
---

# PR Review Branch Sync

Use this as mandatory setup before inspecting a PR locally.

## Workflow

1. Resolve the PR head with `gh pr view <PR> --json headRefName,headRefOid,url`.
2. From the current repository worktree, run this skill's installed `scripts/sync_pr_branch.py` with `--target .`. Keep the script path absolute or otherwise resolvable; `scripts/...` is not relative to the repository worktree. If another worktree owns the branch, stop unless the user explicitly asks to transfer it; only then add `--detach-owner`.
3. Verify with `git branch --show-current` and `git status --short --branch`.
4. Continue only when the current branch equals `headRefName`. Inspect diffs, files, tests, and runtime from that same worktree.

The script verifies the PR belongs to the current repository, fetches the GitHub PR ref, and checks the target worktree is clean before switching it. It never resets an existing local branch to a PR commit or changes another worktree without `--detach-owner`. If local changes or a conflicting branch prevent switching, stop and report the blocker.

## Rechecks

Before rechecking a prior finding, read its review thread and classify it as `fixed`, `deferred`, `unclear`, or `no-reply`. Then verify the current code. A deferred item remains unresolved in the PR unless code fixes it.

## Guardrails

- Do not review from detached HEAD or a different branch.
- Do not describe results from one worktree as though they came from another.
- Keep inline review comments pending unless the user explicitly asks to publish them.
