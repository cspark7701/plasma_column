# Plasma Column Module — Axial Injection

**Purpose**: Beam‑ionized (self‑neutralizing) plasma column inside an axial solenoid to mitigate space‑charge blow‑up between the last solenoid and the spiral/electrostatic inflector of a compact cyclotron.

---

## Operating Point

- **Beam**: proton (p⁺), **30 keV**, **10 mA** DC (or long macropulse)

- **Nominal beam radius**: 1–5 mm at column entrance

- **Residual gas**: H₂ baseline (Kr optional for faster neutralization)

- **Nominal local pressure (cell)**: **1×10⁻⁵ torr** (with differential pumping to protect cyclotron tank)

- **Magnetic field (axial)**: **0.10–0.20 T** uniform over active length

**Neutralization (order‑of‑magnitude)**

- H₂ @ 1×10⁻⁵ torr → **τ ≈ 0.06 ms** to reach ~nₑ ≈ n_b

- Kr @ 1×10⁻⁵ torr → **τ ≈ 0.013 ms** (≈5× faster)

- Electron gyroradius at 1 eV: **~17–34 μm** for 0.2–0.1 T → strongly magnetized

> This is a **neutralizing transport** section (space‑charge compensation, mild ion‑focusing), **not** a current‑carrying plasma lens.

---

## Mechanical & Magnetic

- **Overall length (flange‑to‑flange)**: **260 mm** (fits 100–300 mm active column variants)

- **Active column length L**: configurable **100 / 200 / 300 mm** (spacer rings)

- **Clear beam aperture (ID)**: **≥ 16 mm** (recommend **Ø 20 mm beam tube**, smooth, non‑magnetic SS 316L or Al 6061‑T6, Ra ≤ 0.8 μm)

- **Solenoid**: water‑cooled, **Bz = 0.10–0.20 T**, effective magnetic length ≈ L, bore **Ø ≥ 40 mm**
  
  - **Uniformity**: ΔB/B ≤ **±2%** over Ø 10 mm × L
  
  - **Fringe‑field trim**: auxiliary Helmholtz/trim coils (±5% correction)

- **Alignment**: beamline fiducials, mechanical axis to beam axis ≤ **±0.2 mm**, tilt ≤ **0.3 mrad**

---

## Vacuum & Differential Pumping

- **Cell pressure setpoint**: **1×10⁻⁵ torr (H₂)**; optional **Kr seeding** up to **1×10⁻⁵ torr** via MFC

- **Upstream isolation**: **Ø 6–8 mm orifice** + **TMP ≥ 500 L/s** (H₂ equivalent)

- **Downstream isolation (toward inflector)**: **Ø 4–6 mm orifice** + **TMP ≥ 700 L/s** + cryopanel (if available)

- **Cyclotron tank target**: **≤ 1×10⁻⁷ torr** during operation

- **Materials**: all‑metal UHV seals (CF), vented screws, low‑outgassing cables; **no organics** in beam path

---

## Electrodes & Biasing (Electron Containment)

- **End electrodes**: two axial “cups”/grids, **Ø ≥ 18 mm** clear, edge‑rounded; mounted flush with column ends
  
  - **Bias**: **+5 to +30 V** w.r.t. beam pipe (optimize in situ)
  
  - Purpose: set plasma potential, reduce axial e⁻ loss, speed up neutralization

- **Guard sleeves**: floating/grounded sleeves along the inner wall to suppress secondary electrons; optional **+5 V** bias

- **HV compatibility**: insulation to 200 V, < 10 nA leakage at vacuum

---

## Diagnostics & Controls

- **Ports**: 2× mini‑ConFlat viewports (plasma light), 2× Langmuir‑pin feedthroughs (optional), 1× B‑dot/flux probe feedthrough

- **Beam**: retractable **scintillator/OTR screen** at exit (Ø 20 mm), **DCCT/Faraday cup** upstream

- **Pressure**: 2× nude Bayard–Alpert gauges (cell & downstream), 1× RGA port (shared manifold)

- **Interlocks**: close Kr MFC and ramp solenoid to **<0.05 T** on cyclotron vacuum trip; inhibit beam if cell pressure > **5×10⁻⁵ torr**

---

## Electrical & Thermal

- **Solenoid PS**: 0–200 A, <10 mA ripple (50/60 Hz); field stability **≤ 0.1%** over minutes

- **Cooling**: 1–2 L/min DI water, ΔT < 10 °C; bakeable to 150 °C (solenoid removed)

- **Electrodes PS**: 0–50 V, 100 mA max, floating or ground‑referenced, bandwidth ≥ 1 kHz

---

## Expected Performance (30 keV, 10 mA p⁺)

- **Neutralization fraction**: >90% steady‑state at 1×10⁻⁵ torr (H₂); faster onset with Kr

- **Emittance growth**: reduced vs vacuum‑only transport; minimal additional scattering over 0.1–0.3 m at 10⁻⁵ torr

- **Matching**: choose **L = 0.2 m** and **Bz ≈ 0.15–0.20 T** to minimize divergence into inflector; tune end‑electrode bias for max transmission

---

## Integration Notes

- Place module **as close as mechanically possible** to the inflector entrance while keeping the **downstream orifice** ahead of the inflector to shield tank vacuum

- Provide **straight‑through line of sight** for alignment laser to median plane fiducials

- Commissioning sequence: pump‑down → solenoid at 0.15 T → beam at low current → set biases (+10 V start) → raise to 10 mA → optimize Larmor confinement & pressure

---

## Optional Krypton (Kr) Seeding — “Fast‑Start” Plasma Column Mode

**Goal:** accelerate neutralization build‑up and improve stability by adding a small **Kr partial pressure** within the module while protecting the cyclotron tank with differential pumping.

### Operating Envelope

- **Kr partial pressure (cell):** **(3–10)×10⁻⁶ torr** (with H₂ making up the balance to ~1×10⁻⁵ torr total), or **Kr‑only** at **1×10⁻⁵ torr** during commissioning tests.

- **Expected neutralization time (30 keV p⁺):** with σₖᵣ≈1×10⁻¹⁹ m² → **τ ≈ 0.013 ms** at 1×10⁻⁵ torr (≈5× faster than H₂ at same pressure).

- **Recommended active length:** **L = 0.2 m**; **Bz = 0.15–0.20 T** for strong electron magnetization.

### Gas Handling & Hardware

- **Injection location:** **mid‑cell** side port, facing upstream to minimize gas line‑of‑sight into the inflector region.

- **Flow control:** **MFC (0–1 sccm Kr)** + **fast piezo valve** for pulsed puffs (1–50 ms), both behind a **conductance‑limiting orifice (Ø 0.2–0.5 mm)**.

- **Valving:** all‑metal right‑angle valve at the module inlet; **sector gate valve** downstream toward the cyclotron tank for isolation.

- **Sensing:** add **second nude gauge** dedicated to Kr read‑back (cal‑factor adjusted), and use **RGA** for partial‑pressure confirmation during setup.

### Vacuum & Differential Pumping Adjustments

- Keep **downstream orifice** small (Ø 4–6 mm) and pair with **TMP ≥ 700 L/s** on the downstream stage; optional **LN₂ cryopanel** if available.

- Interlock **Kr MFC/valve** closed if: tank pressure > **1×10⁻⁷ torr**, cell pressure > **5×10⁻⁵ torr**, or inflector HV trips.

- For steady operation, aim **Kr‑only** or **Kr‑dominant** during the **first 100–300 ms** of beam, then taper to **H₂‑dominant** to reduce scattering and pump load.

### Electrode Bias with Kr

- Start with **+10 V** end‑cup bias; scan **+5 → +30 V** to minimize electron end losses. Kr typically yields a slightly **higher plasma potential**, so optimum may shift **+2–5 V** vs H₂.

### Beam‑Physics Notes (30 keV, 10 mA p⁺)

- **Faster neutralization:** Kr’s larger ionization cross‑section yields rapid build‑up; beneficial for macropulsed operation or quick turn‑on.

- **Scattering & loss:** Heavier Kr increases small‑angle scattering and energy‑loss per path length vs H₂. At **≤1×10⁻⁵ torr** over **0.1–0.3 m**, this remains **small**, but keep Kr as **low as needed** to meet transmission goals.

- **Tuning strategy:** Commission with **Kr‑only @ 1×10⁻⁵ torr** to establish electrode bias and B‑field setpoints; then reduce Kr (or switch to H₂‑only) and verify that transmission/emittance remain within spec.

### Controls & Sequencing (example)

1. Pump‑down to base (<1×10⁻⁷ torr tank; <5×10⁻⁷ torr cell).

2. Ramp solenoid to **0.15–0.20 T**.

3. Enable Kr **pulsed puff** (10–50 ms) just before beam; maintain **(3–10)×10⁻⁶ torr** during first **100–300 ms** of beam.

4. Set end‑cup **+10–20 V**; optimize for minimum beam size on exit screen.

5. Taper Kr (hold H₂ at ~few×10⁻⁶ torr or off); confirm tank ≤1×10⁻⁷ torr and stable inflector HV.

6. Record setpoints; enable interlocks for auto‑revert to H₂‑only on any trip.

### Safety & Materials

- Kr cylinder with **two‑stage regulator**, **VCR‑type** stainless lines, **baked/vented** to UHV standards.

- No polymers inside vacuum; shield viewports from direct beam/UV.

- Ensure **oxygen deficiency hazard (ODH)** assessment if venting to enclosed spaces (Kr is inert but heavy).
