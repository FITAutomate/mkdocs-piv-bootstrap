from __future__ import annotations

import argparse
from pathlib import Path
import sys


REQUIRED_DIRS = [
    ".ai",
    ".ai/scripts",
    ".ai/skills",
    ".ai/templates",
    ".ai/reports",
    ".ai/prps",
]

REQUIRED_FILES = [
    ".ai/AGENT.md",
    ".ai/COMMANDS.md",
    ".ai/piv.config.yaml",
    ".ai/scripts/prime.py",
    ".ai/scripts/piv.py",
    ".ai/skills/repo.md",
    ".ai/skills/fit-docs.md",
    ".ai/skills/tests.md",
    ".ai/skills/security.md",
    ".ai/templates/prp_feature.md",
    ".ai/templates/pr_description.md",
]

PLACEHOLDER_CONTENT = {
    ".ai/AGENT.md": "# AI Agent Rules\n",
    ".ai/COMMANDS.md": "# Commands\n",
    ".ai/piv.config.yaml": "version: 1\n",
    ".ai/scripts/prime.py": "# placeholder\n",
    ".ai/scripts/piv.py": "# placeholder\n",
    ".ai/skills/repo.md": "# Repo Skill\n",
    ".ai/skills/fit-docs.md": "# FIT Docs Skill\n",
    ".ai/skills/tests.md": "# Tests Skill\n",
    ".ai/skills/security.md": "# Security Skill\n",
    ".ai/templates/prp_feature.md": "# PRP Feature\n",
    ".ai/templates/pr_description.md": "# PR Description\n",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def cmd_init(root: Path) -> int:
    created = []

    for rel in REQUIRED_DIRS:
        path = root / rel
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created.append(rel)

    for rel in REQUIRED_FILES:
        path = root / rel
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(PLACEHOLDER_CONTENT[rel], encoding="utf-8")
            created.append(rel)

    if created:
        print("INIT_OK")
        for item in created:
            print(f"CREATED: {item}")
    else:
        print("INIT_OK")
        print("NO_CHANGES")
    return 0


def cmd_check(root: Path) -> int:
    missing = []

    for rel in REQUIRED_DIRS:
        if not (root / rel).is_dir():
            missing.append(rel)

    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            missing.append(rel)

    if missing:
        print("CHECK_FAIL")
        for item in missing:
            print(f"MISSING: {item}")
        return 1

    print("CHECK_PASS")
    print("All required .ai scaffold files and directories are present.")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prime .ai scaffold")
    parser.add_argument("--init", action="store_true", help="Create missing scaffold items")
    parser.add_argument("--check", action="store_true", help="Validate scaffold items")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = repo_root()

    if args.init and args.check:
        print("Choose exactly one: --init or --check", file=sys.stderr)
        return 2
    if args.init:
        return cmd_init(root)
    if args.check:
        return cmd_check(root)

    print("No action selected. Use --init or --check.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
