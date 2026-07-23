# TASK 00 — Repository and WarpX Audit

## Objective

Examine the local project repository and the locally modified WarpX source tree before changing any code. Produce a concise audit document describing the current files, scripts, notebooks, run outputs, and WarpX modifications.

## Context

Project repository:

```bash
/home/cspark/Work/projects/plasma_column
```

WarpX source tree:

```bash
/home/cspark/Work/simulation_codes-working/warpx
```

The public repository currently contains mostly notebooks plus Python scripts for particle-number diagnostics, PICMI/WarpX plasma-column simulation, method comparison, and analysis plotting. The local repository may contain additional files and uncommitted changes.

## Required steps

1. Inspect git state.

   ```bash
   cd /home/cspark/Work/projects/plasma_column
   git status --short
   git branch --show-current
   git log --oneline -10
   git remote -v
   ```

2. List files without expanding large output directories.

   ```bash
   find . -maxdepth 3 \
     -not -path './.git/*' \
     -not -path './runs/*' \
     -not -path './diags/*' \
     -not -path './plotfiles/*' \
     -not -path './checkpoints/*' \
     -print | sort
   ```

3. Identify notebooks and scripts.

   ```bash
   find . -name '*.ipynb' -o -name '*.py' -o -name '*.sh' | sort
   ```

4. Inspect conda and Python/WarpX availability.

   ```bash
   conda info --envs
   which python
   python --version
   python - <<'PY'
import sys
print(sys.executable)
try:
    import pywarpx
    print("pywarpx import: OK")
except Exception as exc:
    print("pywarpx import: FAILED", repr(exc))
PY
   ```

5. Inspect the WarpX source tree.

   ```bash
   cd /home/cspark/Work/simulation_codes-working/warpx
   git status --short
   git branch --show-current
   git log --oneline -5
   ```

6. Identify all local WarpX modifications.

   ```bash
   git diff --stat
   git diff --name-only
   ```

7. Search for plasma-column-specific modifications in WarpX.

   ```bash
   grep -RIn "plasma\|column\|ionization\|MCC\|Kr\|H2\|H_2\|proton" Source Examples Python 2>/dev/null | head -200
   ```

8. Create the audit document:

   ```text
   docs/warpx_customization.md
   docs/repo_audit_YYYYMMDD.md
   ```

## Deliverables

- `docs/repo_audit_YYYYMMDD.md`
- `docs/warpx_customization.md`
- No code changes except documentation unless needed to run the audit.

## Acceptance criteria

- The audit lists all important notebooks and scripts.
- The audit clearly identifies which files are production scripts, exploratory notebooks, diagnostics, generated outputs, and documentation.
- The audit reports whether the local WarpX source tree has uncommitted changes.
- The audit states whether `pywarpx` is importable from the active conda environment.
