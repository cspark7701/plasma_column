# TASK 02 — Project Structure and Refactor Plan

## Objective

Create a safe refactor plan that separates reusable physics/diagnostics logic from notebooks while preserving all current working files.

## Required steps

1. Inspect all Python scripts and notebooks.
2. Create a dependency map:
   - which notebook calls which script,
   - which script reads which output file,
   - which scripts are duplicate or older versions.
3. Create target module layout under:
   ```text
   src/plasma_column/
   ```
4. Add empty package scaffolding only:
   - `src/plasma_column/__init__.py`
   - `src/plasma_column/constants.py`
   - `src/plasma_column/beam.py`
   - `src/plasma_column/gas.py`
   - `src/plasma_column/neutralization.py`
   - `src/plasma_column/diagnostics.py`
   - `src/plasma_column/plotting.py`
   - `src/plasma_column/warpx_io.py`
5. Write a migration plan in:
   ```text
   docs/refactor_plan.md
   ```

## Constraints

- Do not delete existing scripts.
- Do not rewrite notebooks in this task.
- Keep old scripts runnable.

## Deliverables

- `docs/refactor_plan.md`
- Package scaffold under `src/plasma_column/`

## Acceptance criteria

- The plan identifies duplicated scripts and recommends one canonical path forward.
- The plan defines a stable API for beam, gas, neutralization, diagnostics, and plotting functions.
