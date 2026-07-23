# TASK 09 — Plotting Pipeline for Notebooks, Proceedings, and Slides

## Objective

Create a clean plotting pipeline that can be called from notebooks and scripts to generate figures for the conference talk and JACOW proceeding.

## Required figures

Simulation-result figures:

1. particle counts vs. time,
2. neutralization fraction vs. time,
3. `K_eff/K0` vs. time,
4. beam envelope vs. z or time,
5. H2 vs. Kr comparison,
6. bunched-beam peak compensation interpretation,
7. parameter-scan summary.

Schematic/derived figures:

1. axial injection layout:
   `buncher -> plasma neutralizer -> solenoid -> Q1 -> Q2 -> inflector`,
2. plasma neutralizer module,
3. space-charge neutralization concept,
4. modeling workflow.

## Required steps

1. Move reusable plotting functions to:
   - `src/plasma_column/plotting.py`
2. Create:
   - `scripts/make_plots.py`
3. Save figures as both PNG and PDF.
4. Include a plot manifest:
   - `plots/manifest.csv`
5. Ensure labels use correct terminology:
   - baseline neutralizer before solenoid,
   - H2 and Kr gas cases,
   - global vs local neutralization,
   - average vs peak-bunch compensation.

## Acceptance criteria

- All plots can be regenerated from command line.
- Notebook only calls the same plotting functions, not duplicate code.
- No artificially rescaled physics curve is presented without explicit label.
