# Journal Manuscript Outline: Plasma-Assisted Space-Charge Neutralization for High-Current Cyclotron Axial Injection

**Target Journal**: *Physical Review Accelerators and Beams* (PRAB) / *Nuclear Instruments and Methods in Physics Research A* (NIMA)

---

## Abstract
- High-current compact cyclotron axial injection challenge (space-charge beam blowup).
- Application of a compact beam-ionized $\text{H}_2/\text{Kr}$ plasma neutralizer located upstream of the main solenoid.
- Analytical kinetics, PICMI/WarpX PIC simulations, and custom MCC ion-impact verification.
- Local volume-averaged beam-core perveance reduction $K_{\text{eff,local}}/K_0$.
- RF-bunched beam interpretation ($K_{\text{eff,peak}}/K_{0,\text{peak}} \approx 1 - \eta_{\text{avg}}/B_f$).
- Envelope transport from buncher through solenoid and quadrupole doublet to spiral inflector, demonstrating $\sim 100\%$ transmission efficiency.

---

## 1. Introduction
- Compact cyclotrons for medical isotope production and high-intensity proton beams.
- Space-charge bottleneck in axial injection lines (keV-range energy, multi-mA current).
- Baseline beamline geometry:
  $$\text{buncher} \rightarrow \text{plasma neutralizer} \rightarrow \text{solenoid} \rightarrow \text{quadrupole Q1} \rightarrow \text{quadrupole Q2} \rightarrow \text{spiral inflector}$$
- Key research question: Can a compact $20\text{ cm}$ beam-ionized plasma column effectively neutralize a $30\text{ keV}$, $10\text{ mA}$ proton beam before injection into the spiral inflector?

---

## 2. Physics & Neutralization Models
- Primary ionization processes: $p^+ + \text{H}_2 \rightarrow p^+ + \text{H}_2^+ + e^-$ and $p^+ + \text{Kr} \rightarrow p^+ + \text{Kr}^+ + e^-$.
- Ionization time constant $\tau = 1/(n_{\text{gas}} \sigma_i v_p)$.
- Distinction between global particle counts and local volume-averaged beam-core neutralization ($\eta_{\text{local,net}}$).
- Space-charge perveance scaling $K_{\text{eff}}/K_0 = 1 - \eta_{\text{net}}$.
- RF-bunched beam scaling: Peak perveance reduction $K_{\text{eff,peak}}/K_{0,\text{peak}} \approx 1 - \eta_{\text{avg}}/B_f$.

---

## 3. Simulation Methods & Numerical Verification
- WarpX PICMI configuration and analytical source benchmarking.
- Verification of custom ion-impact MCC implementation:
  - Test 1 (vacuum), Test 2 ($\sigma=0$), Test 3 ($dN_e/dt$ rate match), Test 4 ($\text{H}_2$ vs $\text{Kr}$ cross section ratio), Test 5 ($\Delta t$ convergence), Test 6 (weight conservation).

---

## 4. Simulation Results & Local Core Compensation
- Comparison of $10^{-5}\text{ Torr }\text{H}_2$ vs $10^{-6}\text{ Torr }\text{Kr}$ neutralizer columns.
- Local core density profiles $n_p(r), n_e(r), n_i(r)$.
- Time evolution of $K_{\text{eff,local}}/K_0$.
- RF-bunched beam peak vs average space-charge compensation.

---

## 5. Downstream Injection Line Optics & Inflector Acceptance
- Space-charge envelope integration $R_x(z), R_y(z)$ from buncher to inflector entrance.
- Inflector entrance aperture cut ($r_{\text{aperture}} = 5.0\text{ mm}$) and transmission efficiency comparison.
- Transverse phase-space $(x, x')$ and $(y, y')$ at inflector entrance.

---

## 6. Discussion & Limitations
- Global vs local compensation physics.
- Bunched-beam peak perveance limits.
- Gas scattering and vacuum pumping requirements.

---

## 7. Conclusions
- Summary of plasma column neutralizer performance and injection optics improvement.
