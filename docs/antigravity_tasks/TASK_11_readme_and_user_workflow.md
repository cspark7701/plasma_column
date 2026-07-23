# TASK 11 — README and User Workflow

## Objective

Create a clear README that allows the project owner to run theory calculations, short WarpX tests, diagnostics, and plotting from the conda environment.

## README sections

Include:

1. project purpose,
2. baseline beamline layout,
3. physics models,
4. repository structure,
5. environment setup,
6. quick dry-run,
7. running a small simulation,
8. postprocessing,
9. generating plots,
10. interpreting `K_eff/K0`,
11. bunched-beam caveat,
12. WarpX source customization,
13. data/output policy,
14. development roadmap.

## Required commands

Document commands like:

```bash
cd /home/cspark/Work/projects/plasma_column
conda activate <env-name>
python scripts/print_environment.py
python scripts/run_case.py --case cases/baseline_h2.yaml --dry_run
python scripts/run_scan.py --matrix cases/method_comparison.yaml --dry_run
python scripts/postprocess_case.py --case-dir runs/example
python scripts/make_plots.py --case-dir runs/example
```

## Acceptance criteria

- A new agent can understand the project without reading the whole chat history.
- The README states which simulation methods are approximate and which are self-consistent.
- The workflow avoids large unintended WarpX output.
