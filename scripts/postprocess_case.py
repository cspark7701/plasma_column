#!/usr/bin/env python3
"""
scripts/postprocess_case.py

Postprocessing wrapper for simulation case directories.
Parses particle number diagnostic files, evaluates global and local neutralization indicators,
and writes neutralization summary CSV files.

Usage:
    python scripts/postprocess_case.py --case-dir runs/seeded_H2_baseline --dry_run
    python scripts/postprocess_case.py --case-dir runs/seeded_H2_baseline
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Add src to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from plasma_column.diagnostics import (
    load_particle_number_diagnostic,
    compute_particle_number_metrics,
    warn_global_count_limitation,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Postprocess plasma column simulation output directory."
    )
    parser.add_argument(
        "--case-dir",
        "--case_dir",
        required=True,
        type=Path,
        help="Path to case output directory (e.g., runs/seeded_H2_baseline).",
    )
    parser.add_argument(
        "--dry_run",
        action="store_true",
        help="Validate paths and diagnostic availability without generating output files.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    case_dir = args.case_dir

    if not case_dir.exists():
        print(f"Error: Case directory '{case_dir}' not found.", file=sys.stderr)
        sys.exit(1)

    print(f"[{'DRY RUN' if args.dry_run else 'POSTPROCESS'}] Case Directory: {case_dir}")

    # Search for particle_number reduced diagnostic file
    diag_file = case_dir / "reducedfiles" / "particle_number.txt"
    if not diag_file.exists():
        diag_file = case_dir / "particle_number.txt"

    if not diag_file.exists():
        print(f"Warning: No particle_number.txt found in {case_dir}.", file=sys.stderr)
        if args.dry_run:
            print(f"[DRY RUN SUCCESS] Directory structure validated for {case_dir}.")
            return
        sys.exit(0)

    print(f"  Found particle diagnostic: {diag_file}")

    if args.dry_run:
        print(f"[DRY RUN SUCCESS] Validated particle diagnostic in {case_dir}.")
        return

    # Process particle diagnostic
    df = load_particle_number_diagnostic(diag_file)
    metrics_df = compute_particle_number_metrics(df)

    out_csv = case_dir / "neutralization_from_particle_number.csv"
    metrics_df.to_csv(out_csv, index=False)
    print(f"  Wrote particle neutralization summary to: {out_csv}")


if __name__ == "__main__":
    main()
