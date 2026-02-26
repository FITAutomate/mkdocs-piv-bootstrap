# AI Agent Operating Rules (fit-docs)

## Scope Discipline
- Keep pull requests small and focused on one change set.
- Do not mix scaffolding, content rewrites, and platform changes in the same PR.
- For docs edits, prefer changes inside one library area per PR.

## Security
- Never commit secrets, tokens, API keys, passwords, or private certificates.
- Do not paste credentials into markdown, scripts, issue templates, or PR descriptions.
- Use environment variables or local secure stores when credentials are required.

## Validation Gate
- Always run validation before claiming done.
- Repository release gate is strict build: `.\venv\Scripts\mkdocs.exe build --strict`.
- After strict PASS, refresh local preview with `.\start-docs.ps1 -Port 8001`.
- Share local test link: `http://127.0.0.1:8001/`.

## Local Commands (Windows)
1. Create virtual environment:
   `py -3.14 -m venv .\venv`
2. Upgrade pip:
   `.\venv\Scripts\python.exe -m pip install --upgrade pip`
3. Install doc dependencies:
   `.\venv\Scripts\python.exe -m pip install mkdocs mkdocs-material`
4. Run strict validation build:
   `.\venv\Scripts\mkdocs.exe build --strict`

## PR Hygiene
- Include validation evidence in PR body.
- Call out any mkdocs.yml changes explicitly (platform-level only).
- Keep generated reports under `.ai/reports/`.
