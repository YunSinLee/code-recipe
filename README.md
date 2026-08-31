# code-recipe

Personal Codex skills, grouped by the work they support.

## Install

Install every skill globally for Codex:

```sh
npx @solaqua/skul@latest add --global --agent codex YunSinLee/code-recipe --all
```

Install a single skill by selecting its `SKILL.md` directory through the same tool.

## Skills

- `browser/skills/image-capture`: capture real UI as review or QA evidence.
- `github/skills/git-gh-default-workflow`: use native Git locally and `gh` for GitHub operations.
- `github/skills/pr-review-branch-sync`: align the current worktree to a PR head branch.
- `github/skills/gh-pr-review-korean`: review a PR in Korean and prepare only actionable findings.
- `github/skills/study-github-pr-korean`: turn a PR into a Korean learning walkthrough.
- `github/skills/gh-self-review-comments`: leave short reviewer-facing annotations on your own PR.
- `github/skills/write-pr-with-images`: add verified GitHub-hosted screenshots to a Korean PR body.

`write-pr-with-images` uses `image-capture` for the capture policy. PR review and PR study use `pr-review-branch-sync` before inspecting local code.

## Conventions

- Keep `SKILL.md` focused on the workflow; add scripts only for repeatable, fragile operations.
- Use real line breaks in all GitHub bodies.
- Keep screenshots outside Git history and use GitHub `user-attachments` URLs in PR bodies.
