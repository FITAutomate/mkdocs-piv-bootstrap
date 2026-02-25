# fit-docs Skill

## Goal / Overview
This repository is a MkDocs Material documentation platform. All updates must preserve stable navigation behavior and strict build quality.

## When To Use
Use this skill for any content, scaffolding, automation, or release workflow touching this repository.

## Prereqs
- Python 3.14 available via `py -3.14`
- Local virtual environment at `.\venv` (create if missing)
- `mkdocs` and `mkdocs-material` installed in `.\venv`

## Procedure
1. Platform baseline:
   - Use MkDocs with Material theme.
   - Treat `mkdocs.yml` as platform-level config only.
2. Validation gate:
   - Run `.\venv\Scripts\mkdocs.exe build --strict` before completing work.
3. Navigation behavior:
   - Navigation is folder-driven.
   - Avoid editing `mkdocs.yml` for normal page adds/renames.
4. Naming conventions:
   - Prefix Knowledge Base files with `📘`
   - Prefix SOP files with `📚`
   - Prefix Procedure files with `📋`
   - Library rules page pattern: `👮 <Library> Library Rules`
5. Required page metadata + headings:
   - Include the metadata table:
     `| Field | Value |`, `Title`, `Type`, `Visibility`, `Publish Ready`, `Version`, `Owner`, `Last Updated`
   - Exactly one H1 below metadata table.
   - Section structure should include:
     - `## Goal / Overview`
     - `## When to Use This`
     - `## Prereqs`
     - `## Procedure`
     - `## Troubleshooting / Resources`

## Troubleshooting / Resources
- If strict build fails, resolve warnings/errors before PR.
- Primary reference: `README.md` repository standards.
- Config reference: `mkdocs.yml` plugins/extensions/theme settings.
