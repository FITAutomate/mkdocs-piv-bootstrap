| Field | Value |
| --- | --- |
| Title | AI PIV Loop (Template) |
| Type | Project Workflow |
| Visibility | Internal |
| Publish Ready | Yes |
| Version | 1.0 |
| Owner | FIT Docs Maintainers |
| Last Updated | 2026-02-25 |

# AI PIV Loop (Template)

## Goal / Overview
Define the default small-change loop for this repository: Issue -> PR -> Validate -> Merge.

## When to Use This
Use this flow for any focused docs/platform update where you want deterministic validation and a small reviewable PR.

## Prereqs
- Local branch from `main`
- `gh` authenticated for PR operations
- Local docs dependencies installed from `requirements.txt`

## Procedure
1. Create or update a tracking item.
   - `gh issue create --title "<title>" --body "<structured body>"`
2. Create a focused branch and make minimal edits.
   - `git checkout main`
   - `git pull`
   - `git checkout -b chore/<change-slug>`
3. Validate locally with strict mode.
   - `.\venv\Scripts\mkdocs.exe build --strict`
4. Commit and push.
   - `git add <changed-files>`
   - `git commit -m "<focused message>"`
   - `git push -u origin chore/<change-slug>`
5. Open a Draft PR with scope and validation evidence.
   - `gh pr create --draft --title "<title>" --body-file <path>`
6. Merge after checks pass.
   - `gh pr ready <number>`
   - `gh pr merge <number> --squash --delete-branch`

## Troubleshooting / Resources
- If strict build fails, resolve all errors before opening/merging.
- Keep PR scope tight and avoid unrelated edits.
- Use `.ai/AGENT.md` and `.github/pull_request_template.md` as your default operating standard.

