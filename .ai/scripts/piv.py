from __future__ import annotations

import argparse
from datetime import datetime
import re
from pathlib import Path
import subprocess
import sys


LOCAL_TEST_URL = "http://127.0.0.1:8001/"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=str(cwd),
        text=True,
        capture_output=True,
        check=False,
    )


def choose_python_launcher(cwd: Path) -> list[str]:
    candidates = [
        ["py", "-3.14"],
        ["py"],
        ["python"],
    ]
    for base in candidates:
        probe = run(base + ["--version"], cwd)
        if probe.returncode == 0:
            return base
    raise RuntimeError("No working Python launcher found (tried py -3.14, py, python).")


def ensure_venv_and_deps(root: Path) -> list[str]:
    log: list[str] = []
    venv_python = root / "venv" / "Scripts" / "python.exe"
    venv_mkdocs = root / "venv" / "Scripts" / "mkdocs.exe"

    if not venv_python.exists():
        launcher = choose_python_launcher(root)
        create = run(launcher + ["-m", "venv", "venv"], root)
        log.append(f"$ {' '.join(launcher + ['-m', 'venv', 'venv'])}")
        log.append(create.stdout.strip())
        if create.returncode != 0:
            log.append(create.stderr.strip())
            raise RuntimeError("Failed to create venv.")

    pip_upgrade = run([str(venv_python), "-m", "pip", "install", "--upgrade", "pip"], root)
    log.append(f"$ {venv_python} -m pip install --upgrade pip")
    log.append(pip_upgrade.stdout.strip())
    if pip_upgrade.returncode != 0:
        log.append(pip_upgrade.stderr.strip())
        raise RuntimeError("Failed to upgrade pip.")

    if not venv_mkdocs.exists():
        install = run([str(venv_python), "-m", "pip", "install", "mkdocs", "mkdocs-material"], root)
        log.append(f"$ {venv_python} -m pip install mkdocs mkdocs-material")
        log.append(install.stdout.strip())
        if install.returncode != 0:
            log.append(install.stderr.strip())
            raise RuntimeError("Failed to install mkdocs dependencies.")

    return log


def write_validation_report(
    root: Path,
    passed: bool,
    lines: list[str],
    refresh_status: str = "N/A",
    local_test_url: str = LOCAL_TEST_URL,
) -> Path:
    reports_dir = root / ".ai" / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = reports_dir / f"validation-{stamp}.md"
    result = "PASS" if passed else "FAIL"

    content = [
        "# Validation Report",
        "",
        f"- Timestamp: {datetime.now().isoformat(timespec='seconds')}",
        f"- Result: {result}",
        f"- Strict Build: {result}",
        f"- Preview Refresh: {refresh_status}",
        f"- Local Test URL: {local_test_url}",
        "",
        "## Command Log",
        "",
        "```text",
        *[line for line in lines if line is not None],
        "```",
        "",
    ]
    path.write_text("\n".join(content), encoding="utf-8")
    return path


def run_preview_refresh(root: Path) -> tuple[str, list[str]]:
    lines: list[str] = []
    script = root / "start-docs.ps1"
    if not script.exists():
        lines.append("REFRESH_SKIPPED: start-docs.ps1 not found")
        lines.append(f"LOCAL_TEST_URL: {LOCAL_TEST_URL}")
        return "SKIPPED", lines

    cmd = [
        "powershell",
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        str(script),
        "-Port",
        "8001",
    ]
    proc = run(cmd, root)
    lines.append(f"$ {' '.join(cmd)}")
    if proc.stdout:
        lines.append(proc.stdout.strip())
    if proc.stderr:
        lines.append(proc.stderr.strip())

    combined = f"{proc.stdout}\n{proc.stderr}"
    if proc.returncode == 0:
        lines.append(f"LOCAL_TEST_URL: {LOCAL_TEST_URL}")
        return "PASS", lines

    if "Port 8001 is already in use" in combined:
        lines.append("REFRESH_NOTE: Port 8001 already in use; using existing local preview process.")
        lines.append(f"LOCAL_TEST_URL: {LOCAL_TEST_URL}")
        return "PASS_ALREADY_RUNNING", lines

    lines.append("REFRESH_WARN: Failed to start local preview refresh command.")
    lines.append(f"LOCAL_TEST_URL: {LOCAL_TEST_URL}")
    return "WARN", lines


def cmd_new(root: Path, slug: str) -> int:
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug):
        print("Invalid slug. Use lowercase letters, numbers, and hyphens only.", file=sys.stderr)
        return 2

    prps_dir = root / ".ai" / "prps"
    prps_dir.mkdir(parents=True, exist_ok=True)
    template_path = root / ".ai" / "templates" / "prp_feature.md"
    if not template_path.exists():
        print("Missing template: .ai/templates/prp_feature.md", file=sys.stderr)
        return 1

    prp_path = prps_dir / f"{slug}.md"
    if not prp_path.exists():
        raw = template_path.read_text(encoding="utf-8")
        rendered = (
            raw.replace("{{slug}}", slug)
            .replace("{{title}}", slug.replace("-", " ").title())
            .replace("{{date}}", datetime.now().strftime("%Y-%m-%d"))
        )
        prp_path.write_text(rendered, encoding="utf-8")

    branch = f"feature/{slug}"
    current = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], root)
    current_name = current.stdout.strip() if current.returncode == 0 else ""

    if current_name != branch:
        exists = run(["git", "show-ref", "--verify", f"refs/heads/{branch}"], root)
        if exists.returncode == 0:
            checkout = run(["git", "checkout", branch], root)
        else:
            checkout = run(["git", "checkout", "-b", branch], root)
        if checkout.returncode != 0:
            print(checkout.stderr.strip(), file=sys.stderr)
            return 1

    print(f"PRP_CREATED: {prp_path}")
    print(f"BRANCH_READY: {branch}")
    return 0


def cmd_validate(root: Path) -> int:
    log: list[str] = []
    refresh_status = "N/A"
    try:
        log.extend(ensure_venv_and_deps(root))

        mkdocs_exe = root / "venv" / "Scripts" / "mkdocs.exe"
        build = run([str(mkdocs_exe), "build", "--strict"], root)
        log.append(f"$ {mkdocs_exe} build --strict")
        if build.stdout:
            log.append(build.stdout.strip())
        if build.stderr:
            log.append(build.stderr.strip())

        passed = build.returncode == 0
        if passed:
            refresh_status, refresh_log = run_preview_refresh(root)
            log.extend(refresh_log)

        report = write_validation_report(root, passed, log, refresh_status=refresh_status)
        print(f"VALIDATION_REPORT: {report}")
        print(f"RESULT: {'PASS' if passed else 'FAIL'}")
        if passed:
            print(f"PREVIEW_REFRESH: {refresh_status}")
            print(f"LOCAL_TEST_URL: {LOCAL_TEST_URL}")
        return 0 if passed else 1
    except Exception as exc:
        log.append(str(exc))
        report = write_validation_report(root, False, log, refresh_status="FAIL")
        print(f"VALIDATION_REPORT: {report}")
        print("RESULT: FAIL")
        print(str(exc), file=sys.stderr)
        return 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="PIV helper")
    subparsers = parser.add_subparsers(dest="command", required=True)

    new_parser = subparsers.add_parser("new", help="Create PRP and branch")
    new_parser.add_argument("slug", help="Feature slug (lowercase-hyphen)")

    subparsers.add_parser("validate", help="Run strict build and write validation report")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = repo_root()

    if args.command == "new":
        return cmd_new(root, args.slug)
    if args.command == "validate":
        return cmd_validate(root)

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
