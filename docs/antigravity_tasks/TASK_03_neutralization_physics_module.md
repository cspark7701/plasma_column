# TASK 03 — Analytical Neutralization Physics Module

## Objective

Implement reusable analytical calculations for ionization rate, neutralization build-up, bunched-beam interpretation, and effective perveance.

## Required functions

Create `src/plasma_column/neutralization.py` with functions for:

```python
gas_density_m3(pressure_torr: float, temperature_K: float) -> float
proton_beta_gamma_speed(kinetic_energy_keV: float) -> tuple[float, float, float]
ionization_tau_s(n_gas_m3: float, sigma_m2: float, beam_speed_m_s: float) -> float
neutralization_fraction(t_s, tau_s, eta_ss=1.0)
keff_over_k0_from_eta(eta)
bunch_length_s(rf_frequency_hz, phase_width_deg)
bunch_length_m(beam_speed_m_s, rf_frequency_hz, phase_width_deg)
peak_keff_over_k0_from_average_eta(eta_avg, bunching_factor)
```

## Required documentation

Add:
- `docs/physics_notes/neutralization_model.md`
- `docs/physics_notes/bunched_beam_neutralization.md`

Include the formulas:

```text
K_eff/K0 = 1 - eta_net
eta_net = (N_e - N_i) / N_p
I_peak = B_f I_avg
K_eff,peak/K0,peak ~= 1 - eta_avg/B_f
```

## Constraints

- Functions must be independent of WarpX.
- Include unit tests for numerical sanity.
- Clearly separate illustrative analytic estimates from simulation-derived quantities.

## Deliverables

- `src/plasma_column/neutralization.py`
- `tests/test_neutralization.py`
- Physics notes under `docs/physics_notes/`

## Acceptance criteria

- `pytest -q tests/test_neutralization.py` passes.
- Functions are used by at least one script or notebook example.
