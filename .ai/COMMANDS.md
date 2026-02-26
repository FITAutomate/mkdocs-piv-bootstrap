# PIV Commands (Windows First)

## Prime
- Initialize scaffold (create missing files/directories):
  `python .ai/scripts/prime.py --init`
- Verify scaffold structure:
  `python .ai/scripts/prime.py --check`

## Feature PRP Flow
- Create PRP draft and branch:
  `python .ai/scripts/piv.py new <slug>`
- Validate repository and write report:
  `python .ai/scripts/piv.py validate`

## Manual Validation
- Strict build gate:
  `.\venv\Scripts\mkdocs.exe build --strict`
- Refresh local preview after strict PASS:
  `.\start-docs.ps1 -Port 8001`
- Local testing URL:
  `http://127.0.0.1:8001/`

## Git + PR
- Create branch:
  `git checkout -b chore/<change-slug>`
- Open draft PR:
  `gh pr create --draft --title "<title>" --body-file <path-to-body.md>`
