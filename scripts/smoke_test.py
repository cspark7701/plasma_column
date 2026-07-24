#!/usr/bin/env python3
"""
scripts/smoke_test.py

Local smoke test script for repo hardening and CI verification.
Executes syntax compilation, unit tests, and dry-runs of standard simulation cases and scans.

Usage:
    python scripts/smoke_test.py
"""

from __future__ import annotations

import argparse
import sys
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def run_cmd(cmd: list[str]) -> None:
    print(f"\n=> Running: {' '.join(cmd)}")
    res = subprocess.run(cmd, cwd=PROJECT_ROOT)
    if res.returncode != 0:
        print(f"FAILED: Command {' '.join(cmd)} exited with code {res.returncode}", file=sys.stderr)
        sys.exit(res.returncode)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run local smoke test suite for plasma_column project.")
    parser.parse_args()

    print("=== Plasma Column Smoke Test ===")
    
    # 1. Compile Python files
    run_cmd([sys.executable, "-m", "compileall", "src", "scripts", "."])

    # 2. Run pytest suite
    run_cmd([sys.executable, "-m", "pytest", "-q"])

    # 3. Run dry-run for baseline_h2 case
    run_cmd([sys.executable, "scripts/run_case.py", "--case", "cases/baseline_h2.yaml", "--dry_run"])

    # 4. Run dry-run for method_comparison scan
    run_cmd([sys.executable, "scripts/run_scan.py", "--matrix", "cases/method_comparison.yaml", "--dry_run"])

    print("\n=== SMOKE TEST PASSED SUCCESSFULLY ===")


if __name__ == "__main__":
    main()
