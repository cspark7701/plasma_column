# Repository Hardening, Packaging, and CI

## 1. Overview

This document describes the repository hardening, packaging structure, dependency specifications, unit testing, and Continuous Integration (CI) configuration for the plasma column neutralizer simulation project.

The goal of repository hardening is to ensure that the codebase is installable, reproducible from a clean checkout, and easily verifiable using lightweight tests without requiring full PIC simulation runs or external WarpX binaries.

---

## 2. Package Setup and Dependencies

The project is structured as a standard Python package under `src/plasma_column`.

### Dependency Configuration Files
- **`pyproject.toml`**: Defines build system (`setuptools`), project metadata, dependencies (`numpy`, `scipy`, `matplotlib`, `pandas`, `pyyaml`), package discovery under `src/`, and `pytest` settings.
- **`environment.yml`**: Conda environment specification for `warpx-dev`, pinning channels (`conda-forge`, `defaults`) and Python 3.10+ dependencies.
- **`requirements-dev.txt`**: Flat requirements file for development environment setup and CI.

### Editable Installation
To install the package in editable mode within your Python/Conda environment:

```bash
conda activate warpx-dev
python -m pip install -e .
```

---

## 3. Unit Tests and Verification

All unit tests are located in `tests/` and test physics functions, data structures, and configuration files without triggering long PIC calculations.

### Test Modules
- `tests/test_basic_physics.py`: Validates 30 keV proton kinematics ($\beta, \gamma, v_p$), ideal-gas density conversions ($n_{\text{gas}}$ from Torr to $\text{m}^{-3}$), bunch duration/length calculations, effective perveance formula $K_{\text{eff}}/K_0 = 1 - \eta$, and WarpX-free matplotlib plotting imports.
- `tests/test_case_files.py`: Ensures all YAML case files under `cases/` parse without syntax errors.
- `tests/test_neutralization.py`: Tests analytic neutralization rates, time constants, and bunched-beam peak perveance equations.
- `tests/test_diagnostics_particle_number.py`: Tests local neutralization and particle counting routines.
- `tests/test_gas_cross_sections.py`: Verifies cross section database loading and energy interpolations for $\text{H}_2$ and $\text{Kr}$.

---

## 4. Local Smoke Test Workflow

A dedicated smoke test script is provided at `scripts/smoke_test.py` for rapid pre-commit validation.

### Running Smoke Tests
To run the full smoke test suite locally:

```bash
python scripts/smoke_test.py
```

This script executes four sequential validation steps:
1. `python -m compileall src scripts .`: Ensures all Python files compile cleanly.
2. `pytest -q`: Executes all lightweight unit tests.
3. `python scripts/run_case.py --case cases/baseline_h2.yaml --dry_run`: Validates simulation parameters and metadata generation for `baseline_h2`.
4. `python scripts/run_scan.py --matrix cases/method_comparison.yaml --dry_run`: Validates parameter scan parsing and execution plan generation across 9 cases.

---

## 5. Continuous Integration (CI)

Continuous Integration is configured via GitHub Actions in `.github/workflows/ci.yml`.

### Key CI Principles
- **Lightweight Execution**: CI runs strictly unit tests, syntax checks, and dry-run case validations.
- **No WarpX Dependency**: CI does not compile WarpX or execute long PIC simulations.
- **Matrix Testing**: Validated across Python 3.10, 3.11, and 3.12 environments.
