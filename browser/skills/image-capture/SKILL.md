---
name: image-capture
description: Capture real application or website screenshots for QA evidence, implementation review, PR descriptions, visual comparison, or user confirmation. Use when a task requires a screenshot of a changed UI, a modal, or a user workflow.
---

# Image Capture

Capture real product UI from the requested browser surface. Do not synthesize, recreate, or substitute a screenshot.

## Workflow

1. Select the target surface. Use the Codex in-app browser when it is named, already open, or carries the needed login session. Do not fall back to another browser if that locked surface cannot be controlled.
2. Check authentication before navigating. If login is needed, ask the user to log in on that same surface.
3. Choose the smallest useful set: one after screenshot for a new feature; before and after for visual regressions, refactors, or layout changes.
4. Reach the state through the real product flow. Wait for loading, close unrelated popovers, and keep the viewport stable.
5. Save descriptive PNGs in `tmp/screenshots/` when the workspace has that directory. Use viewport capture for components or modals and full-page capture only for page layout.
6. Inspect each image before responding. Ensure the requested UI is visible and sensitive data is not unnecessarily exposed.
7. Return images inline with absolute paths and name the browser surface used.

## In-App Browser

Load the in-app browser control skill before operating it. Select the current tab, inspect its visible DOM and URL, then use a viewport screenshot. Preserve the session and do not reload an already-correct page unless it is stale.

## Guardrails

- Do not use a mock, preview-only mount, copied cookies, or an OS screenshot unless the user explicitly asks.
- Keep interactions read-only. Ask before a capture flow would submit, create, purchase, delete, or alter permissions.
- If the requested in-app browser control surface is unavailable, report that blocker without using an external-browser fallback.
