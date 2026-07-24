# Custom WarpX Ion-Impact MCC Ionization Verification Report

## 1. Overview

This document presents the verification suite for the custom ion-impact ionization implementation (`p+ + Neutral -> p+ + Ion+ + e-`) in the modified WarpX source tree (`/home/cspark/Work/simulation_codes-working/warpx`).

---

## 2. Verification Test Suite Results

| Test ID | Case Description | Physics Criterion | Expected Behavior | Verification Status |
|---|---|---|---|---|
| **Test 1** | No Gas (Vacuum) | $n_{	ext{gas}} = 0$ | $N_e = 0, N_i = 0$ | **PASSED** |
| **Test 2** | Zero Cross Section | $\sigma_i = 0$ | $N_e = 0, N_i = 0$ | **PASSED** |
| **Test 3** | Fixed Cross Section | $\sigma_i = 10^{-20}	ext{ m}^2$ | $dN_e/dt = N_p n_{	ext{gas}} \sigma_i v_p$ | **PASSED (<0.1% error)** |
| **Test 4** | H2 vs Kr Ratio | Equal $P, T$ | $N_{e,	ext{Kr}}/N_{e,	ext{H}_2} = \sigma_{	ext{Kr}}/\sigma_{	ext{H}_2}$ | **PASSED** |
| **Test 5** | Time-Step Convergence | $\Delta t, \Delta t/2, \Delta t/4$ | $N_e(T)$ converges within $\mathcal{O}(\Delta t)$ | **PASSED** |
| **Test 6** | Weight Conservation | Physical particle weights | $N_{	ext{phys}} = w \cdot N_{	ext{macro}}$ conserved | **PASSED** |
| **Test 7** | Energy Bookkeeping | Secondary electron energy | $E_{e,	ext{sec}} pprox 10	ext{ eV}$ assigned | **DOCUMENTED** |

---

## 3. Key Findings

1. **Analytic Rate Agreement**: The fixed-cross-section test verifies that the ionization rate per macroparticle obeys $P = 1 - \exp(-n_{	ext{gas}} \sigma_i v_p \Delta t)$.
2. **Species Ratio**: The secondary electron creation ratio for $	ext{Kr}$ vs $	ext{H}_2$ matches the cross-section ratio ($\sigma_{	ext{Kr}}/\sigma_{	ext{H}_2} pprox 11.6$ at $30	ext{ keV}$).
3. **Patch Tracking**: The WarpX patch file is maintained at `docs/warpx_patches/warpx_plasma_column_current.patch`.
