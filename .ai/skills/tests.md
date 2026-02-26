# Tests Skill

## Goal
Standardize repository validation for PIV loops.

## Required Validation
- Primary gate: `.\venv\Scripts\mkdocs.exe build --strict`
- After strict PASS, refresh local preview: `.\start-docs.ps1 -Port 8001`
- Local test URL: `http://127.0.0.1:8001/`
- Record validation outcome in `.ai/reports/validation-<timestamp>.md`

## Procedure
1. Confirm Python launcher availability.
2. Ensure virtual environment exists.
3. Install/refresh docs dependencies if needed.
4. Run strict build.
5. If strict build passes, run `.\start-docs.ps1 -Port 8001`.
6. Confirm/test local preview at `http://127.0.0.1:8001/`.
7. Save PASS/FAIL report and include it in PR body.
