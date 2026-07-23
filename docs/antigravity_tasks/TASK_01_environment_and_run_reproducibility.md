# TASK 01 — Environment and Run Reproducibility

## Objective

Create a reproducible local run environment description and lightweight execution wrappers for the plasma-column simulations.

## Required steps

1. Create or update:
   - `README.md`
   - `docs/environment.md`
   - `scripts/print_environment.py`
   - `scripts/run_case.py`

2. `scripts/print_environment.py` must print:
   - Python executable,
   - Python version,
   - conda environment name,
   - `pywarpx` import status,
   - NumPy/Pandas/Matplotlib versions if available,
   - project git commit,
   - WarpX source path and git status summary.

3. `scripts/run_case.py` must support:
   ```bash
   python scripts/run_case.py --case cases/vacuum.yaml --dry_run
   python scripts/run_case.py --case cases/baseline_h2.yaml --dry_run
   python scripts/run_case.py --case cases/baseline_kr.yaml --dry_run
   ```

4. Create initial YAML case files:
   - `cases/vacuum.yaml`
   - `cases/baseline_h2.yaml`
   - `cases/baseline_kr.yaml`

5. Include metadata writing for every case.

## Constraints

- Do not change physics behavior yet.
- Do not move existing notebooks.
- Do not require long WarpX runs.

## Deliverables

- `docs/environment.md`
- `scripts/print_environment.py`
- `scripts/run_case.py`
- `cases/vacuum.yaml`
- `cases/baseline_h2.yaml`
- `cases/baseline_kr.yaml`

## Acceptance criteria

- `python scripts/print_environment.py` runs successfully.
- All three cases complete `--dry_run`.
- The scripts explain clearly how to activate the expected conda environment.
