# Publication-Quality Simulation and Analysis Workflow

This document provides a step-by-step guide for executing, postprocessing, analyzing, and plotting publication-quality simulations for the plasma-assisted space-charge neutralizer project.

---

## Workflow Overview

```text
[1. Environment Check] -> [2. Case/Scan Run Execution] -> [3. Postprocessing Diagnostics] -> [4. Front-End Notebook Analysis] -> [5. Figure Generation]
```

---

## Step 1: Environment Audit and Verification

Before launching production runs, activate the `warpx-dev` environment and verify WarpX C++ source bindings.

```bash
cd /home/cspark/Work/projects/plasma_column
conda activate warpx-dev

# Audit Python packages, WarpX source tree, and git status
python scripts/print_environment.py

# Verify repository file integrity and test suite
python scripts/audit_repo.py --root .
python -m pytest -q
```

---

## Step 2: Running Publication-Quality Simulation Cases

Simulations can be launched using the standardized YAML case launcher (`scripts/run_case.py`), the scan launcher (`scripts/run_scan.py`), or direct PICMI production scripts (`plasma_column_mcc_picmi_v7.py` and `plasma_column_callback_source_picmi_v3.py`).

### 2.1 Dry-Run Validation
Always validate parameters and metadata generation first using `--dry_run`:

```bash
python scripts/run_case.py --case cases/baseline_h2.yaml --dry_run
python scripts/run_case.py --case cases/baseline_kr.yaml --dry_run
python scripts/run_scan.py --matrix cases/method_comparison.yaml --dry_run
```

### 2.2 Baseline Reference & Seeded Neutralization Runs
Run the standardized case definitions:

```bash
# 1. Vacuum Reference (Uncompensated beam propagation)
python scripts/run_case.py --case cases/vacuum.yaml

# 2. Baseline H2 Neutralizer Cell (1e-5 Torr)
python scripts/run_case.py --case cases/baseline_h2.yaml

# 3. Baseline Kr Neutralizer Cell (1e-6 Torr)
python scripts/run_case.py --case cases/baseline_kr.yaml

# 4. RF-Bunched Beam H2 Case (B_f = 5)
python scripts/run_case.py --case cases/bunched_h2.yaml

# 5. RF-Bunched Beam Kr Case (B_f = 5)
python scripts/run_case.py --case cases/bunched_kr.yaml
```

### 2.3 Full C++ MCC PICMI Simulations (Self-Consistent Impact Ionization)
To execute full WarpX C++ MCC simulations:

```bash
# H2 MCC Run (1e-5 Torr)
python plasma_column_mcc_picmi_v7.py --output_dir runs/cxx_H2_mcc --gas H2 --pressure_torr 1e-5 --mcc electron_impact --run

# Kr MCC Run (1e-6 Torr)
python plasma_column_mcc_picmi_v7.py --output_dir runs/cxx_Kr_mcc --gas Kr --pressure_torr 1e-6 --mcc electron_impact --run
```

### 2.4 Dynamic Python Callback Source Simulations
To execute dynamic pair-creation callback simulations:

```bash
# H2 Dynamic Callback Run
python plasma_column_callback_source_picmi_v3.py --output_dir runs/callback_H2_dynamic --gas H2 --pressure_torr 1e-5 --run

# Kr Dynamic Callback Run
python plasma_column_callback_source_picmi_v3.py --output_dir runs/callback_Kr_dynamic --gas Kr --pressure_torr 1e-6 --run
```

---

## Step 3: Postprocessing Diagnostics

Extract global neutralization ratios ($\eta_{\text{electron\_only}}, \eta_{\text{net}}, K_{\text{eff}}/K_0$) and local core charge density metrics for each case directory:

```bash
# Postprocess individual case output directories
python scripts/postprocess_case.py --case-dir runs/vacuum_reference
python scripts/postprocess_case.py --case-dir runs/seeded_H2_baseline
python scripts/postprocess_case.py --case-dir runs/seeded_Kr_baseline
python scripts/postprocess_case.py --case-dir runs/cxx_H2_mcc
python scripts/postprocess_case.py --case-dir runs/cxx_Kr_mcc
python scripts/postprocess_case.py --case-dir runs/callback_H2_dynamic
python scripts/postprocess_case.py --case-dir runs/callback_Kr_dynamic
```

Each postprocessed directory will contain `neutralization_from_particle_number.csv`.

---

## Step 4: Notebook Analysis Workflows

Four primary Jupyter notebooks are configured for front-end analysis and figure generation:

### 1. Method Comparison Notebook
- **File**: [`run_plasma_column_method_comparison.ipynb`](file:///home/cspark/Work/projects/plasma_column/run_plasma_column_method_comparison.ipynb)
- **Role**: Compares vacuum, static seeded compensation, dynamic Python callbacks, and C++ MCC runs.
- **Outputs**: Comparative perveance reduction curves ($K_{\text{eff}}/K_0$) across methods.

### 2. Publication Plotting Notebook
- **File**: [`plasma_column_analysis_plots_v2.ipynb`](file:///home/cspark/Work/projects/plasma_column/plasma_column_analysis_plots_v2.ipynb)
- **Role**: Imports `src/plasma_column/plotting.py` functions to build publication figures for particle counts, species populations, transverse/longitudinal profiles, and beam envelopes.

### 3. Dynamic Callback Diagnostics Notebook
- **File**: [`run_python_callback_source_diagnostics_v2.ipynb`](file:///home/cspark/Work/projects/plasma_column/run_python_callback_source_diagnostics_v2.ipynb)
- **Role**: In-depth analysis of dynamic pair injection rates, ionization build-up times, and electron trapping.

### 4. Full Transport Diagnostics Notebook
- **File**: [`run_seeded_full_transport_diagnostics.ipynb`](file:///home/cspark/Work/projects/plasma_column/run_seeded_full_transport_diagnostics.ipynb)
- **Role**: Transverse beam RMS size $r_{\text{rms}}(z)$, RMS emittance $\epsilon_{\text{rms}}(z)$, and transmission loss along the $z$-axis through the solenoid.

---

## Step 5: Generating Publication-Ready Vector & Raster Figures

To generate or update all publication figures from the command line:

```bash
# Generate cross-section database comparison figure
python scripts/plot_cross_sections.py

# Generate RF-bunched beam peak space-charge reduction figure
python scripts/plot_bunched_beam_perveance.py

# Generate complete figure suite & manifest
python scripts/make_plots.py
```

### Generated Figures and Formats
All figures are saved to `plots/` in dual formats:
- **PDF**: Vector graphics for LaTeX proceedings (JACOW) and journal papers.
- **PNG**: 300 DPI raster graphics for slides and web presentation.

Figure manifest is maintained at [`plots/manifest.csv`](file:///home/cspark/Work/projects/plasma_column/plots/manifest.csv).
