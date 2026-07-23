# TASK 04 — Particle Number and Local Neutralization Diagnostics

## Objective

Replace ad-hoc particle-number parsing with robust diagnostics that compute both global and local neutralization metrics.

## Required steps

1. Create `src/plasma_column/diagnostics.py`.
2. Implement robust reading of WarpX `ParticleNumber` reduced diagnostics.
3. Preserve species-order metadata.
4. Compute:
   - global `N_e/N_p`,
   - global `N_i/N_p`,
   - global `(N_e-N_i)/N_p`,
   - global `K_eff/K0`,
   - local neutralization in the plasma column and beam-core region when particle or charge-density data are available.
5. Create:
   - `scripts/postprocess_case.py`
6. Add warnings when only global counts are available.

## Important physics note

Global particle-number ratios are not enough to claim local space-charge compensation. The key quantity is the charge-density ratio inside the beam volume in the plasma cell.

## Deliverables

- `src/plasma_column/diagnostics.py`
- `scripts/postprocess_case.py`
- `tests/test_diagnostics_particle_number.py`
- Updated documentation in `docs/physics_notes/neutralization_model.md`

## Acceptance criteria

- Existing `particle_number.txt` files can be parsed.
- The output CSV includes both electron-only and net-charge indicators.
- The script refuses to silently infer local compensation from global counts.
