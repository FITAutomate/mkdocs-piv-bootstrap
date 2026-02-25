# Tests Skill

## Goal
Standardize repository validation for PIV loops.

## Required Validation
- Primary gate: `.\venv\Scripts\mkdocs.exe build --strict`
- Record validation outcome in `.ai/reports/validation-<timestamp>.md`

## Procedure
1. Confirm Python launcher availability.
2. Ensure virtual environment exists.
3. Install/refresh docs dependencies if needed.
4. Run strict build.
5. Save PASS/FAIL report and include it in PR body.
