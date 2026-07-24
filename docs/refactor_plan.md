# Refactoring and Modular Package Architecture Plan

## 1. Executive Summary

This plan outlines the gradual refactoring of the `plasma_column` codebase from a collection of standalone root scripts and exploratory notebooks into a structured, tested Python package `plasma_column` under `src/`.

The primary goals are:
- Decouple front-end presentation (notebooks) from physics, diagnostics, and I/O logic.
- Eliminate script duplication and clarify canonical code paths.
- Ensure all plotting and analysis routines follow deterministic, scriptable workflows.
- Maintain full backwards compatibility during the migration phase so existing scripts remain executable.

---

## 2. Codebase Audit and Dependency Mapping

### 2.1 Front-End Analysis Notebooks
- `plasma_column_analysis_plots_v2.ipynb`: Reads outputs from `runs/` and calls plotting routines.
- `run_plasma_column_method_comparison.ipynb`: Compares seeded, callback, and C++ MCC simulation methods.
- `run_python_callback_source_diagnostics_v2.ipynb`: Analyzes Python callback dynamic pair creation.
- `run_seeded_full_transport_diagnostics.ipynb`: Analyzes seeded neutralization transport cases.

### 2.2 Legacy & Duplicate Script Mapping
| Category | Archived / Older Iterations | Current Root Implementation | Target Canonical Package Module |
| :--- | :--- | :--- | :--- |
| **PICMI MCC Simulation** | `archives/old_scripts/plasma_column_mcc_picmi_v1..v6.py` | `plasma_column_mcc_picmi_v7.py` | `scripts/run_case.py` + `src/plasma_column/warpx_io.py` |
| **Python Callback PICMI** | `archives/plasma_column_callback_source_picmi.py` (v1, v2) | `plasma_column_callback_source_picmi_v3.py` | `src/plasma_column/neutralization.py` + `scripts/run_case.py` |
| **Particle Diagnostics** | `particle_number_diagnostics.py` | `particle_number_diagnostics_v2.py`, `particle_number_diagnostics_compare.py` | `src/plasma_column/diagnostics.py` |
| **Plotting & Analysis** | `archives/plasma_column_analysis_plots.py` | `plasma_column_analysis_plots_v2.py` | `src/plasma_column/plotting.py` |

---

## 3. Target Package Architecture (`src/plasma_column/`)

```text
src/plasma_column/
├── __init__.py          # Package initialization & version string
├── constants.py         # Physical constants (C, QE, ME, MP, AMU, KB, EPSILON_0) & unit conversions
├── beam.py              # Beam kinematics, relativistic beta/gamma, perveance K0, RF bunching
├── gas.py               # Gas properties (H2, Kr), neutral density n_gas, pressure/temperature formulas
├── neutralization.py    # Neutralization ratios (eta_electron_only, eta_net, K_eff/K0, peak-bunch perveance)
├── diagnostics.py       # Reduced diagnostic (ParticleNumber.txt) parsers & local core neutralization
├── plotting.py          # Deterministic figure generation (PNG + PDF export)
└── warpx_io.py          # Machine-readable metadata.json & input file reader/writer
```

---

## 4. Canonical API Specification

### `plasma_column.constants`
- Provides standard physical constants (`C`, `QE`, `ME`, `MP`, `AMU`, `KB`, `EPSILON_0`) and unit conversions (`TORR_TO_PA`, `EV_TO_JOULE`).

### `plasma_column.beam`
- `ProtonBeam`: Dataclass managing $E_{beam}$, $I_{beam}$, $r_{beam}$, $\beta$, $\gamma$, $v_{beam}$, and uncompensated perveance $K_0$.
- `RFFocusedBeam`: Extension containing RF frequency $f_{RF}$, bunching factor $B_f$, phase width $\Delta \phi$, bunch time width $\Delta t_b$, and spatial length $\Delta z_b$.

### `plasma_column.gas`
- `NeutralGas`: Dataclass calculating neutral number density $n_{gas} = p / (k_B T)$ for $H_2$ and $Kr$.
- Cross-section data lookup functions for proton-impact and electron-impact ionization.

### `plasma_column.neutralization`
- `compute_neutralization_ratios(N_p, N_e, N_i)`: Returns $\eta_{electron\_only}$, $\eta_{net}$, $K_{eff,electron\_only}/K_0$, $K_{eff,net}/K_0$.
- `compute_bunched_beam_peak_perveance(eta_avg, bunching_factor)`: Evaluates peak-bunch space charge factor $K_{eff,peak}/K_{0,peak} = 1 - \eta_{avg}/B_f$.

### `plasma_column.diagnostics`
- `load_particle_number_diagnostic(path)`: Loads and cleans WarpX `ParticleNumber.txt` data.
- `compute_local_neutralization(plotfile_path, core_radius, column_z_bounds)`: Computes volume-averaged local electron and ion densities within the beam core in the plasma cell.

### `plasma_column.plotting`
- `save_figure(fig, filepath)`: Saves figure to both `.png` and `.pdf`.
- Plotting functions for species populations, neutralization ratio evolution, transverse/longitudinal beam profiles, and summary matrices.

---

## 5. Migration Roadmap

1. **Phase 1 (Scaffolding)**: Create empty/basic package scaffolding under `src/plasma_column/` (Completed in Task 02).
2. **Phase 2 (Physics & Diagnostics)**: Populate `constants`, `beam`, `gas`, `neutralization`, and `diagnostics` with validated functions (Tasks 03, 04, 05, 06).
3. **Phase 3 (Plotting & Analysis)**: Refactor `plasma_column_analysis_plots_v2.py` logic into `src/plasma_column/plotting.py` (Task 09).
4. **Phase 4 (Notebook Integration)**: Update notebooks to import from `plasma_column` package while retaining existing outputs for reference.
