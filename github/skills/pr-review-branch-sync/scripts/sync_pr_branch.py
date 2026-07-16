#!/usr/bin/env python3
"""Align the current worktree with a PR head branch."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse


@dataclass
class WorktreeEntry:
    path: Path
    branch: str | None = None


def run(cmd: list[str], cwd: Path | None = None) -> str:
    result = subprocess.run(cmd, cwd=str(cwd) if cwd else None, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "command failed")
    return result.stdout.strip()


def parse_worktrees(repo_root: Path) -> list[WorktreeEntry]:
    entries: list[WorktreeEntry] = []
    current: WorktreeEntry | None = None
    for line in run(["git", "worktree", "list", "--porcelain"], cwd=repo_root).splitlines():
        if not line:
            if current:
                entries.append(current)
                current = None
            continue
        key, _, value = line.partition(" ")
        if key == "worktree":
            current = WorktreeEntry(path=Path(value).resolve())
        elif current and key == "branch":
            current.branch = value.removeprefix("refs/heads/")
    if current:
        entries.append(current)
    return entries


def require_clean_worktree(target: Path) -> None:
    changes = run(["git", "status", "--short"], cwd=target)
    if changes:
        raise RuntimeError(f"Target worktree has local changes; cannot switch safely:\\n{changes}")


def fetch_pr_head(repo_root: Path, number: int) -> str:
    run(["git", "fetch", "origin", f"pull/{number}/head"], cwd=repo_root)
    return run(["git", "rev-parse", "FETCH_HEAD"], cwd=repo_root)


def local_branch_head(repo_root: Path, branch: str) -> str | None:
    result = subprocess.run(
        ["git", "rev-parse", "--verify", f"refs/heads/{branch}"],
        cwd=str(repo_root),
        text=True,
        capture_output=True,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def github_repository_from_remote(remote_url: str) -> str:
    normalized = remote_url.removesuffix(".git").rstrip("/")
    if normalized.startswith("git@github.com:"):
        return normalized.removeprefix("git@github.com:")
    parsed = urlparse(normalized)
    if parsed.hostname == "github.com":
        return parsed.path.lstrip("/")
    raise RuntimeError(f"Origin is not a recognizable GitHub remote: {remote_url}")


def verify_pr_url(pr_url: str, repository: str) -> None:
    parsed = urlparse(pr_url)
    parts = parsed.path.strip("/").split("/")
    if parsed.hostname != "github.com" or "/".join(parts[:2]) != repository or parts[2:3] != ["pull"]:
        raise RuntimeError("The PR URL does not match the current GitHub repository.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pr", help="GitHub PR URL or number")
    parser.add_argument("--target", default=".", help="Target worktree path. Defaults to the current directory.")
    parser.add_argument("--detach-owner", action="store_true", help="Detach another clean worktree that owns the PR branch.")
    args = parser.parse_args()
    target = Path(args.target).resolve()
    repo_root = Path(run(["git", "rev-parse", "--show-toplevel"], cwd=target))
    target = repo_root
    origin_repo = github_repository_from_remote(run(["git", "remote", "get-url", "origin"], cwd=repo_root))
    meta = json.loads(
        run(
            ["gh", "pr", "view", args.pr, "--json", "number,headRefName,headRefOid,url,baseRepository"],
            cwd=repo_root,
        )
    )
    if meta["baseRepository"]["nameWithOwner"] != origin_repo:
        raise RuntimeError("The PR base repository does not match the current worktree origin.")
    verify_pr_url(meta["url"], origin_repo)
    branch = meta["headRefName"]
    pr_head = fetch_pr_head(repo_root, meta["number"])
    require_clean_worktree(target)

    existing_head = local_branch_head(repo_root, branch)
    if existing_head and existing_head != pr_head:
        raise RuntimeError(
            f"Local branch '{branch}' does not match the PR head. "
            "Resolve it manually instead of resetting the branch."
        )

    owner = next((entry for entry in parse_worktrees(repo_root) if entry.branch == branch), None)
    if owner and owner.path != target:
        if not args.detach_owner:
            raise RuntimeError(
                f"PR branch is owned by another worktree: {owner.path}. "
                "Re-run with --detach-owner only after explicit user approval."
            )
        require_clean_worktree(owner.path)
        print(f"Detaching branch owner worktree: {owner.path}")
        run(["git", "switch", "--detach"], cwd=owner.path)
    if run(["git", "branch", "--show-current"], cwd=target) != branch:
        print(f"Switching target worktree to branch: {branch}")
        if existing_head:
            run(["git", "switch", branch], cwd=target)
        else:
            run(["git", "switch", "--create", branch, pr_head], cwd=target)
    final_branch = run(["git", "branch", "--show-current"], cwd=target)
    print(f"Target worktree: {target}\nPR url: {meta['url']}\nCurrent branch: {final_branch}")
    return 0 if final_branch == branch else 1


if __name__ == "__main__":
    sys.exit(main())
