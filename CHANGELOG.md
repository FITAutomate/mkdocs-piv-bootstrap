# Changelog

## 2026-02-26 Template Refresh

- Synced latest `.ai` validation refresh behavior from `fit-docs`:
  - post-strict local refresh step
  - local test URL surfaced in validation output
- Added starter `mkdocs.yml` baseline to template.
- Added starter stylesheets:
  - `docs/stylesheets/extra.css`
  - `docs/stylesheets/blog-index.css`
- Added `docs/index.md` starter page.
- Added README guidance to review `mkdocs.yml` and stylesheets before production launch.

## 2026-02-25 Bootstrap Baseline

This repository captures the reusable baseline extracted from one full setup session in `FITAutomate/fit-docs`.

### Included merged work

- PR #1: https://github.com/FITAutomate/fit-docs/pull/1
  - Added `.ai` scaffold, scripts, skills, templates, and PR/issue templates.
- PR #2: https://github.com/FITAutomate/fit-docs/pull/2
  - Added CI workflow for `mkdocs build --strict` on PRs.
- PR #3: https://github.com/FITAutomate/fit-docs/pull/3
  - Added `requirements.txt`, updated CI to install from it, enabled Dependabot.
- PR #4: https://github.com/FITAutomate/fit-docs/pull/4
  - Tuned Dependabot grouping and added GitHub Actions ecosystem updates.
- PR #5: https://github.com/FITAutomate/fit-docs/pull/5
  - Aligned README setup with `requirements.txt` and added PIV workflow reference page.
