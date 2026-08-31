---
name: git-gh-default-workflow
description: Use native Git for local repository workflow and GitHub CLI for GitHub operations, including branches, commits, pushes, pull requests, reviews, and checks. Use whenever work in a Git repository needs a standard GitHub workflow.
---

# Git and GitHub CLI Default Workflow

Use `git` for local repository state and history. Use `gh` for GitHub resources such as pull requests, reviews, issues, and Actions.

## Default Choices

- Inspect `git status` and the relevant `git diff` before staging or committing. Stage only files within the requested scope.
- Create and switch branches with `git switch -c <branch>`; switch existing branches with `git switch <branch>`.
- Commit intended staged changes with `git commit -m "<message>"`.
- Before a requested trunk update, determine the repository's default branch, fetch `origin`, and fast-forward that branch. Do not rebase or merge the current feature branch unless the user requests it or the workflow requires it.
- Publish a branch with `git push -u origin HEAD`. If published history must be rewritten, use `git push --force-with-lease` only when that rewrite is intended.
- Create or update GitHub pull requests with `gh pr create`, `gh pr edit`, `gh pr view`, `gh pr review`, and `gh pr merge` as appropriate. A push automatically updates an existing pull request for that branch.

## Guardrails

- Use only native Git branch and history metadata.
- Treat dependent branches as ordinary Git branches. When their parent changes, rebase each affected branch explicitly and resolve conflicts before pushing.
- Do not push, force-push, create a pull request, merge, or delete branches unless the user has requested that external change.
