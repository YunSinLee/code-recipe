---
name: write-pr-with-images
description: Create or update a Korean GitHub pull request with a Conventional Commit-style title and verified GitHub user-attachment screenshots in its body. Use when a PR needs screenshots, a reviewer-oriented body, or a title/body update.
---

# Write PR With Images

Use `image-capture` for capture policy. This skill owns PR title/body composition, GitHub attachment upload, and rendered-body validation.

## Workflow

1. Identify a writable target PR. Create a draft first if an upload target does not exist.
2. Ensure the title has a Conventional Commit-style prefix and Korean text: `feat:`, `fix:`, `chore:`, `docs:`, `refactor:`, `test:`, `build:`, or `ci:`.
3. Capture the requested real UI with `image-capture`. For localhost, confirm the server belongs to the current worktree. Prefer a verified light-mode capture when appearance matters.
4. Upload current-run image files in the target PR conversation through the GitHub web composer. Confirm each result is a `https://github.com/user-attachments/assets/...` URL. Do not add image files to Git or use a CLI attachment uploader.
5. Read the repository PR template. Write a reviewer-oriented body to a file, including reason, grouped behavior changes, actual tests, and a screenshot table.
6. Update with `gh pr edit <PR> --body-file <file>` (or API file input), then open the PR and verify the uploaded images render.

## Body Shape

```markdown
## 변경 이유

## 변경사항

### <reviewer-facing behavior>

- <change and impact>

## 테스트

- [x] `<actually run command>`

## 스크린샷

| 화면 | 설명 |
| --- | --- |
| ![capture](https://github.com/user-attachments/assets/...) | <short description> |
```

## Guardrails

- Do not update a PR body until current-run files and user-attachment URLs are confirmed.
- Do not create an asset-only branch, worktree, or PR.
- Never send literal `\\n` in a GitHub body.
