# TASK 06 — RF-Bunched Beam Source Model

## Objective

Add a bunched-beam source model and analysis layer because the buncher is upstream of the plasma neutralizer.

## Required features

1. Case parameters:
   - `rf_frequency_hz`,
   - `bunch_phase_width_deg`,
   - `bunching_factor`,
   - `beam_current_average_mA`,
   - `beam_current_peak_mA`.

2. Analytical calculations:
   - bunch duration,
   - bunch length,
   - peak current,
   - peak generalized perveance,
   - expected peak-bunch effective perveance for average plasma neutralization.

3. Optional PICMI source mode:
   - start with an analysis-only model,
   - add time-dependent injection only if the current WarpX/PICMI interface supports it robustly.

## Required documentation

Update:
- `docs/physics_notes/bunched_beam_neutralization.md`

## Key formula

```text
K_eff,peak/K0,peak ~= 1 - eta_avg/B_f
```

This formula is valid only for average plasma neutralization. If local plasma electron density reaches peak-bunch density, use a separate model and document the overcompensation risk between bunches.

## Deliverables

- bunched-beam functions in `src/plasma_column/beam.py` or `neutralization.py`
- `cases/bunched_h2.yaml`
- `cases/bunched_kr.yaml`
- notebook or script plot showing expected `K_eff/K0` vs bunching factor

## Acceptance criteria

- The code reports realistic bunch length and peak-current values.
- Slides/proceeding text no longer imply that nanosecond bunches are neutralized within a single pass.
