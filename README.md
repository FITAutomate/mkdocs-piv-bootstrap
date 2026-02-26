# MkDocs PIV Bootstrap

Reusable bootstrap template for running disciplined PIV loops in MkDocs repositories with deterministic validation.

This template packages the working patterns proven in `FITAutomate/fit-docs` PRs #1 through #5.

## What This Template Provides

- AI scaffolding under `.ai/` for repeatable PIV loops
- Draft-ready PR and issue templates under `.github/`
- GitHub Actions CI gate for `mkdocs build --strict`
- Dependabot automation for pip + workflow dependencies
- Pinned `requirements.txt` for deterministic docs tooling
- A reference page for the Issue -> PR -> Validate -> Merge loop

## Included Files

### AI workflow core

- `.ai/AGENT.md`
- `.ai/COMMANDS.md`
- `.ai/piv.config.yaml`
- `.ai/scripts/prime.py`
- `.ai/scripts/piv.py`
- `.ai/skills/repo.md`
- `.ai/skills/fit-docs.md` (sample repo-specific rules; rename/customize per repo)
- `.ai/skills/tests.md`
- `.ai/skills/security.md`
- `.ai/templates/prp_feature.md`
- `.ai/templates/pr_description.md`

### GitHub automation

- `.github/workflows/docs-build.yml`
- `.github/dependabot.yml`
- `.github/pull_request_template.md`
- `.github/ISSUE_TEMPLATE/piv_feature_request.yml`

### Dependency + reference docs

- `requirements.txt`
- `mkdocs.yml` (starter baseline)
- `docs/stylesheets/extra.css` (starter tokens)
- `docs/stylesheets/blog-index.css` (starter placeholder)
- `docs/project/AI PIV Loop (Template).md`

## Provenance: Source PRs (fit-docs)

This template is the extracted result of these merged PRs:

1. `#1` `chore: prime repo for PIV loops`
2. `#2` `chore: add CI mkdocs strict build`
3. `#3` `chore: add requirements + dependabot for docs CI`
4. `#4` `chore: tune dependabot (pip grouping + github-actions)`
5. `#5` `docs: align setup with requirements.txt + add PIV workflow page`

Links:

- https://github.com/FITAutomate/fit-docs/pull/1
- https://github.com/FITAutomate/fit-docs/pull/2
- https://github.com/FITAutomate/fit-docs/pull/3
- https://github.com/FITAutomate/fit-docs/pull/4
- https://github.com/FITAutomate/fit-docs/pull/5

## Intended Usage Modes

### Mode A: Start a new docs repo from this template (recommended)

Use this repository as a GitHub template and create a new repository from it.

Then review starter config and add your MkDocs project content:

- `mkdocs.yml`
- `docs/stylesheets/extra.css`
- `docs/stylesheets/blog-index.css`
- `docs/` pages and folders
- optional hooks/overrides/assets

### Mode B: Apply to an existing MkDocs repo

Copy these paths into your existing repository:

- `.ai/**`
- `.github/workflows/docs-build.yml`
- `.github/dependabot.yml`
- `.github/pull_request_template.md`
- `.github/ISSUE_TEMPLATE/piv_feature_request.yml`
- `requirements.txt`
- optional: `docs/project/AI PIV Loop (Template).md`

## Bootstrap Checklist For A New Repo

1. Create local venv:
   - `py -3.14 -m venv .\venv`
2. Install deterministic dependencies:
   - `.\venv\Scripts\python.exe -m pip install --upgrade pip`
   - `.\venv\Scripts\python.exe -m pip install -r requirements.txt`
3. Confirm strict build gate locally:
   - `.\venv\Scripts\mkdocs.exe build --strict`
4. Initialize/verify AI scaffold:
   - `.\venv\Scripts\python.exe .ai/scripts/prime.py --init`
   - `.\venv\Scripts\python.exe .ai/scripts/prime.py --check`
5. Run loop validation report:
   - `.\venv\Scripts\python.exe .ai/scripts/piv.py validate`

## Standard PIV Loop

1. Create issue with structured scope and acceptance criteria.
2. Create focused branch:
   - `git checkout main`
   - `git pull`
   - `git checkout -b chore/<slug>`
3. Implement small, single-purpose change-set.
4. Validate strict build:
   - `mkdocs build --strict`
5. Commit and push.
6. Open Draft PR using template sections and validation evidence.
7. Merge with squash after checks pass.

## CI Behavior

Workflow file: `.github/workflows/docs-build.yml`

- Trigger: `pull_request`, `workflow_dispatch`
- Runner: `ubuntu-latest`
- Python: `3.12`
- Install source: `requirements.txt`
- Gate: `mkdocs build --strict`

Important: This workflow assumes your repository has a valid `mkdocs.yml` and docs source tree.

## Dependabot Behavior

Config file: `.github/dependabot.yml`

- Weekly pip updates at repository root
- Weekly GitHub Actions updates for `/.github/workflows`
- Grouping to reduce PR noise:
  - `python-docs`
  - `github-actions`

## Repo-Specific Customization Required

Before first production use, update:

1. `.ai/skills/fit-docs.md`
   - Rename to match your repo/domain
   - Encode your folder conventions and naming rules
2. `.ai/AGENT.md`
   - Adjust install/build commands to your environment
3. `.ai/piv.config.yaml`
   - Confirm local commands and validation sequence
4. `docs/project/AI PIV Loop (Template).md`
   - Replace org-specific references
5. `mkdocs.yml` and stylesheets
   - Review palette, features, extensions, and plugin set
   - Tune `docs/stylesheets/extra.css` and `docs/stylesheets/blog-index.css` before launch

## Security Guardrails

- Never commit secrets in docs, templates, scripts, or PR bodies.
- Keep workflow permissions minimal.
- Treat strict build as required gate for merge.

## Troubleshooting

### CI fails at dependency install

- Ensure `requirements.txt` is present at repo root.
- Ensure package names/versions are valid.

### CI fails at strict build

- Reproduce locally with:
  - `.\venv\Scripts\mkdocs.exe build --strict`
- Resolve link warnings/errors and configuration issues before merge.

### `prime.py --check` fails

- Run:
  - `.\venv\Scripts\python.exe .ai/scripts/prime.py --init`
- Re-run check and commit missing scaffold files.

### `piv.py validate` reports preview refresh skipped

- This template may not include `start-docs.ps1` in every target repo.
- Strict build validation still runs; add your own local preview start script if desired.

## Minimal Adoption Command Set (Windows)

```powershell
py -3.14 -m venv .\venv
.\venv\Scripts\python.exe -m pip install --upgrade pip
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe .ai\scripts\prime.py --init
.\venv\Scripts\python.exe .ai\scripts\prime.py --check
.\venv\Scripts\python.exe .ai\scripts\piv.py validate
.\venv\Scripts\mkdocs.exe build --strict
```

## License

No license is included by default. Add one before broad external reuse if needed.
