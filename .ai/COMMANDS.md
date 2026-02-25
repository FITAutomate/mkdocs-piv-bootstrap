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

## Git + PR
- Create branch:
  `git checkout -b chore/<change-slug>`
- Open draft PR:
  `gh pr create --draft --title "<title>" --body-file <path-to-body.md>`
