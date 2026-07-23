## Space Charge Effects in Compact H⁻ Cyclotrons

### 1. **Beam Blow-Up at Injection**

- At injection (tens of keV), the beam is non-relativistic → strong Coulomb repulsion.

- The generalized perveance describes how strong space charge is:

where:

- = beam current

- = relativistic factors

- At low injection energies, , so becomes large → strong tune shifts, emittance growth.

- **Result**: Beam bunches lengthen, transverse envelope oscillations increase, mismatch → particle loss.

---

### 2. **Longitudinal Space Charge**

- Space charge forces lengthen bunches.

- A longer bunch overlaps more RF phases → increases phase spread → particles drift out of acceleration bucket.

- At high currents, neighboring bunches can even **interact** due to overlapping Coulomb fields.

---

### 3. **Transverse Space Charge & Tune Shift**

- The focusing frequency (betatron tune) shifts downward with current:

- If the tune approaches integer or half-integer resonances, strong beam blow-up and losses occur.

- In compact cyclotrons, available focusing is limited, so this becomes a hard limit.

---

### 4. **Extraction Losses & Stripping**

- For H⁻ cyclotrons, extraction is done via **stripper foils**.

- High current → higher foil heating → faster foil degradation.

- Space charge also enlarges the orbit spread at extraction → more particles miss the foil or hit wrong spots → increased losses.

---

## ⚙️ Beam Dynamics Strategies to Mitigate Space Charge

### Injection Stage

- **Higher injection energy**: Raising injection energy (e.g., from 30 keV to 70–100 keV) reduces perveance, hence weaker space charge.

- **Good matching**: Careful design of the central region (electrode shape, spiral inflectors, RF phase) to minimize mismatch.

- **Bunching**: Pre-bunching with RF before injection reduces longitudinal blow-up inside cyclotron.

### Acceleration Stage

- **Strong RF focusing**: Higher harmonic cavities or higher dee voltage reduce bunch lengthening.

- **Large phase acceptance**: Optimized RF phase window reduces loss from longitudinal space charge blow-up.

- **Magnetic flutter / spiral sectors**: Improves transverse focusing strength.

### Extraction Stage

- **Thin stripper foils**: Minimize heating, extend lifetime under high currents.

- **Orbit separation optimization**: Strong focusing in outer orbits helps separate turns, so space charge–induced spread is less critical.

---

## 📉 Practical Beam Current Limits

- Commercial compact **medical isotope cyclotrons** (H⁻ type) typically deliver **0.5–1.5 mA** extracted beam.

- Attempts at **>2 mA** usually hit strong space charge blow-up and extraction losses.

- For comparison: **PSI’s Injector-2** is not H⁻, but with H₂⁺, they handle ~5 mA equivalent protons — showing what’s possible if stripping/extraction challenges are bypassed.

---

👉 So for compact **H⁻ cyclotrons**, the real **bottlenecks are**:

1. **Low-energy injection space charge** (limits capture efficiency).

2. **Longitudinal space charge blow-up** (limits phase acceptance).

3. **Foil heating and extraction losses** (limits extracted current).

---







# Transverse: tune depression from space charge

### 1) Generalized perveance (how “strong” space charge is)

$$
K \;=\; \frac{q\,I_{\text{peak}}}{2\pi\varepsilon_0\, m\, \gamma^3 \beta^3 c^3}
$$

* $I_{\text{peak}} = I_{\text{avg}}/B_f$ with bunching factor $B_f \equiv I_{\text{avg}}/I_{\text{peak}}$ (typ. $0.25$–$0.5$ in compact machines).
* **Scaling:** $K \propto I_{\text{peak}}/(\beta^3\gamma^3)$.
  Raising **injection energy** (↑$\beta\gamma$) or **improving bunching** (↑$B_f$ → ↓$I_{\text{peak}}$) reduces $K$ fast.

> Quick feel: at 30 keV, $I_{\text{avg}}=1\,\mathrm{mA}$, $B_f=0.3 \Rightarrow I_{\text{peak}}\approx3.3\,\mathrm{mA}$
> $K$ is about $4\times$ larger than with the same current at 100 keV.

---

### 2) KV envelope & tune depression (smooth approximation)

For an rms beam radius $R$ (round beam, KV-like),

$$
R'' + \kappa(s)\,R \;-\; \frac{\varepsilon^2}{R^3} \;-\; \frac{K}{R} \;\approx\; 0,
$$

with external focusing $\kappa$ and transverse (unnormalized) rms emittance $\varepsilon$.

Averaging over one cell (smooth focusing), the **depressed tune** satisfies roughly

$$
\nu_\perp \;\approx\; \sqrt{\nu_{0}^2 \;-\; C_\perp\,\frac{K}{\varepsilon/R^2}},
$$

where $C_\perp$ is an $\mathcal{O}(1)$ geometry factor that depends on sector shape/edge focusing and the actual envelope solution. The precise coefficient needs a lattice-specific calculation, but the **scaling** is robust:

* **Tune shift magnitude** $|\Delta\nu_\perp| \;\propto\; \dfrac{I_{\text{peak}}}{\beta^3\gamma^3}\;\dfrac{R^2}{\varepsilon}\;\;(\times\hbox{geometry}).$

**Takeaways**

* At fixed emittance, **doubling injection energy (in keV)** typically reduces $|\Delta\nu_\perp|$ by $\sim 30$–$50\%$ in the tens-of-keV regime (because $\beta^3$ rises quickly).
* At fixed energy, $|\Delta\nu_\perp|$ grows **linearly** with **peak** current and **quadratically** with beam size (since weaker external focusing → larger $R$, which hurts).
* At fixed $I_{\text{avg}}$, increasing **$B_f$** (more uniform current) **helps** by cutting $I_{\text{peak}}$.

---

### 3) Laslett-style form (aperture/image terms)

With a beam inside a round pipe of radius $b$ and rms radius $a$, image forces amplify the shift. A common heuristic (from rings/coasting-beam theory, adapted for bunched beams) is

$$
\Delta\nu_\perp \;\sim\; -\,\frac{I_{\text{peak}}}{\beta^3\gamma^3}\,
\frac{G_\perp(b/a)}{\varepsilon_N}\,
\Big(\text{machine length scale}\Big),
$$

where $G_\perp\!\sim\!1+2\ln(b/a)$ for a round pipe and $\varepsilon_N=\beta\gamma\,\varepsilon$ is the normalized emittance. The exact length-scale coefficient depends on your focusing lattice and where in the machine you evaluate it. The **scaling** messages remain:

* Worse when **beam is large** vs **pipe** (small $b/a$ → bigger $G_\perp$).
* Improves with **normalized emittance** and with **$\beta^3\gamma^3$**.

> **Rule of thumb for limits:** try to keep $|\Delta\nu_\perp|\lesssim 0.2$–$0.3$ to avoid resonance overlap in compact cyclotrons. That target, plugged into the scalings above, gives a quick **$I_{\max}$** estimate.

---

# Longitudinal: bunch lengthening from space charge

In an isochronous cyclotron, “synchrotron motion” is weak; **RF phase focusing** and the finite **RF gap transit-time factor** provide the restoring force. Space charge produces an **inductive** longitudinal impedance that **lengthens** the bunch (potential-well distortion).

### 1) Effective space-charge impedance (low frequency)

For a round beam in a conducting pipe, the effective **longitudinal** space-charge impedance per harmonic $n$ scales like

$$
\left|\frac{Z_\parallel}{n}\right| \;\propto\; \frac{Z_0}{2\pi}\,\frac{G_\parallel(b/a)}{\beta\,\gamma^2},
\quad Z_0=377~\Omega,
$$

with $G_\parallel(b/a)\sim 1+2\ln(b/a)$.
**Scaling:** $\propto I_{\text{peak}}/(\beta\gamma^2)$, i.e., softer than transverse’s $1/(\beta^3\gamma^3)$ but still very sensitive at low energy.

### 2) Balance with RF phase focusing

Let the **RF focusing constant** (small-amplitude) scale as

$$
k_\phi \;\propto\; \frac{h\,q\,V_{\text{rf}}\,|\cos\phi_s|}{E_{\text{kin}}}\,,
$$

with harmonic $h$, dee voltage $V_{\text{rf}}$, synchronous phase $\phi_s$, and kinetic energy $E_{\text{kin}}$.

In a **potential-well** picture, the **equilibrium rms bunch length** (radians) approximately follows a **1/3-power law**:

$$
\sigma_\phi \;\propto\;
\Bigg[\;
\frac{I_{\text{peak}}}{\beta\,\gamma^2}\,G_\parallel(b/a)
\;\Bigg/ \;
\frac{h\,q\,V_{\text{rf}}\,|\cos\phi_s|}{E_{\text{kin}}}
\Bigg]^{\!1/3}.
$$

**Scaling highlights**

* $\sigma_\phi \uparrow$ with $I_{\text{peak}}$ and with $G_\parallel$ (tighter aperture makes it worse).
* $\sigma_\phi \downarrow$ with $V_{\text{rf}}$, $|\cos\phi_s|$, $h$, and $E_{\text{kin}}$.
* Because of the $1/3$ power, **doubling** $I_{\text{peak}}$ increases the **bunch length** by only $\approx 26\%$, but that’s enough to spill particles outside the stable RF phase window and seed losses.

---

# Coupling: why longer bunches hurt transverse limits

Longer bunches → **smaller bunching factor $B_f$** → **larger $I_{\text{peak}}$** → **bigger $K$** → **more transverse tune depression**. This **positive feedback** is why compact machines often hit a **sharp current wall**: once bunches lengthen past the RF bucket edges, both transverse and longitudinal losses snowball.

---

# Practical “dials” and their math

* **Raise injection energy** $E_{\text{inj}}$:
  $|\Delta\nu_\perp|\sim I_{\text{peak}}/(\beta^3\gamma^3)$ and $\sigma_\phi\sim (I_{\text{peak}}/(\beta\gamma^2))^{1/3}$.
  Even modest $E_{\text{inj}}$ increases (30 → 70 keV) can **halve** transverse tune shift and **shrink** longitudinal impedance meaningfully.

* **Improve $B_f$** (pre-buncher, better central-region capture):
  $\Downarrow I_{\text{peak}}$ → linear relief to both transverse and longitudinal space charge.

* **Increase $V_{\text{rf}}$** or operate nearer **$\phi_s\simeq 0$** (as allowed by capture/extraction):
  $\sigma_\phi \propto (1/V_{\text{rf}})^{1/3}$. Also higher $V_{\text{rf}}$ raises turn-to-turn energy gain, improving turn separation at extraction.

* **Keep beam small vs aperture** (large $b/a$, better matching):
  Both $G_\perp$ and $G_\parallel$ decrease with larger $b/a$.

* **Preserve normalized emittance $\varepsilon_N$** (good matching through the spiral inflector, avoid mismatch oscillations):
  Larger $\varepsilon_N$ tolerates more current before $|\Delta\nu_\perp|$ reaches danger.

---

# Worked “feel” numbers (just to anchor intuition)

Consider **H⁻**, $I_{\text{avg}}=1~\mathrm{mA}$, $B_f=0.3\Rightarrow I_{\text{peak}}\approx3.3~\mathrm{mA}$.

* **Perveance $K$:**
  
  * **30 keV** → $K \approx 4.1\times10^{-4}$
  * **70 keV** → $K \approx 1.2\times10^{-4}$
    (i.e., **\~3.5× lower** by 70 keV at the same average current and $B_f$)

* **Bunch length trend:**
  With unchanged RF, $\sigma_\phi \propto (I_{\text{peak}}/(\beta\gamma^2))^{1/3}$, so going 30 → 70 keV cuts the **space-charge drive** by roughly a factor $\sim$ $(\beta\gamma^2)^{-1/3}$ → expect **\~20–30% shorter** equilibrium bunch length solely from the energy term, before any RF changes.

*(Coefficients depend on your exact central region, aperture, harmonic, and RF focusing; use these as **scalings**, not hard predictions.)*

---

# How to use these scalings to set an $I_{\max}$

1. **Pick an acceptable tune depression**, e.g. $|\Delta\nu_\perp|\lesssim 0.25$.
2. Use the transverse scaling $|\Delta\nu_\perp|\propto (I_{\text{peak}}/(\beta^3\gamma^3))\,(R^2/\varepsilon)\,G_\perp$ to solve for $I_{\text{peak,max}}$.
3. Check **longitudinal**: with that current, compute $\sigma_\phi$ from the $1/3$ law; ensure it still fits in your **stable RF phase window** and doesn’t degrade $B_f$ so much that step 2 breaks.
4. Iterate with **$E_{\text{inj}}$**, **$V_{\text{rf}}$**, **$B_f$**, **matching**.

---

## (what grows fastest and what helps most)

* Bad guys: $I_{\text{peak}}$, small $E_{\text{inj}}$ (low $\beta\gamma$), tight aperture $b$, large beam $a$, low $V_{\text{rf}}$, poor capture (small $B_f$).
* Good guys: raise $E_{\text{inj}}$ (huge win; transverse scales as $1/(\beta^3\gamma^3)$), improve $B_f$, increase $V_{\text{rf}}$, keep $b/a$ big, preserve $\varepsilon_N$.

# Transmission Efficiency

For typical compact H⁻ cyclotrons with axial injection, **the stand-alone spiral-inflector transmission is often only a few–tens of percent**; a realistic back-of-the-envelope gives **\~5–15%**, and after including central-region capture it can drop to **\~1–5% overall** from source current to first accelerated turns.

# Quick estimate (order-of-magnitude)

Take representative numbers for a 30 keV H⁻ beam:

* rms **normalized emittance** from the source & LEBT:
  $\varepsilon_{N,\mathrm{rms}} \sim 5\ \pi\,\mathrm{mm\,mrad}$ (often 5–15)
* $\beta\gamma\simeq 0.008$ at 30 keV → **geometric** emittance
  $\varepsilon_{\mathrm{rms}}=\varepsilon_N/(\beta\gamma)\approx
  5/0.008\approx 625\ \pi\,\mathrm{mm\,mrad}$.
* A compact spiral inflector with \~5 mm gap, length ≈ 3–5 cm, |V|≈10–20 kV in $B\sim1.1$–1.4 T has a **geometric acceptance** typically of order
  $A_{\text{inf}}\sim 30\text{–}80\ \pi\,\mathrm{mm\,mrad}$ (machine-dependent).

Transmission (emittance-limited) $\;\approx A_{\text{inf}}/\varepsilon_{\mathrm{rms}}$:

$$
T_{\text{inflector}}\sim \frac{30\text{–}80}{625}\ \approx\ 5\%\text{–}13\%.
$$

Even if your source/LEBT is excellent (e.g., $\varepsilon_{N,\mathrm{rms}}\!=\!3\ \pi$), you still get only $\sim 10\%\text{–}20\%$.

Once you include **RF phase acceptance** of the first turns (often only 20–40° out of 360°) and central-region losses, **source-to-capture** efficiency can fall to $\sim$1–5%.

# Why the transmission is intrinsically small

1. **Emittance vs. small aperture (hard acceptance mismatch)**
   
   * The **spiral-inflector gap is tiny** (3–6 mm) and its length is short.
   * That sets a **small transverse acceptance** compared with the **large geometric emittance** you get when you divide a modest normalized emittance by tiny $\beta\gamma$ at 30 keV.
   * Bottom line: most particles simply don’t fit the accepted phase-space volume.

2. **Space-charge blow-up in the inflector (no neutralization)**
   
   * In the LEBT you often have partial neutralization; **inside the inflector** the beam is between electrodes → **neutralization is lost**.
   * At 30 keV, $\beta,\gamma\ll1$ → generalized perveance $K\propto I/(\beta^3\gamma^3)$ is large; the bunch **expands** and scrapes the plates.

3. **Strong, nonlinear fields and tight tolerances**
   
   * The superposed **E (inflector)** and **B (cyclotron)** fields generate curved 3D trajectories; fringe fields at entrance/exit add **nonlinear focusing**.
   * **Plate edges** and finite gap produce field errors; 100 µm misalignments can cause mm-level orbit shifts → scraping.

4. **Mismatch into the median-plane optics**
   
   * The beam exiting the inflector is usually **astigmatic** with significant **x–z/y–z coupling**.
   * The very first gaps offer little focusing/phase control → envelope oscillations → losses on posts, dees, or puller.

5. **Energy and phase spread from the inflector**
   
   * Path-length and fringe-field variations convert into **energy/phase spread**, reducing the fraction that lands inside the **RF phase bucket**.

6. **H⁻-specific issues**
   
   * **Lorentz stripping margins** limit how high you can push $B$ and plate voltage (E-field), which in turn caps the compactness/acceptance of the device.
   * Any grazing contact with metal or residual gas collision can **strip** H⁻ → immediate loss.

# What helps (in order of impact)

* **Raise injection energy** (e.g., 30 → 60–80 keV): geometric emittance shrinks as $1/(\beta\gamma)$ and space-charge weakens as $1/(\beta^3\gamma^3)$.
* **Reduce source emittance** (better extraction optics, solenoid matching, apertures).
* **Pre-bunch & match** to the inflector using LEBT optics; keep bunching factor high to lower peak current.
* **Larger gap / optimized 3D inflector** (field-mapped design, shaped electrodes) to increase acceptance without exceeding E-field limits.
* **Precise alignment** (≤50–100 µm) and smooth edges to cut nonlinearities.
* **Central-region redesign** for stronger early focusing and larger RF phase acceptance.

Estimate for a **compact proton (H⁺) cyclotron** with **axial injection** and a **neutralizing plasma column** just upstream of the spiral inflector.

* **Energy** $E=30\ \text{keV}$ → $\beta\simeq0.007996,\ \gamma\simeq1.000032$.
* **Normalized rms emittance** $\varepsilon_{N,\text{rms}}=5\,\pi\ \text{mm-mrad}$
  ⇒ geometric rms emittance $\varepsilon_{\text{rms}}=\varepsilon_N/(\beta\gamma)\approx 625\,\pi\ \text{mm-mrad}$.
* **Column length** $L=0.2\!-\!0.3\ \text{m}$, **pressure** $\approx10^{-5}$ torr.
* **Current** $I=1$–$10\ \text{mA}$.
* Use a **typical spiral-inflector** acceptance $A_{\text{inf}}\sim 60\,\pi\ \text{mm-mrad}$ and geometry (few-mm gap, $|V|\sim 10\!-\!20$ kV).

---

# 1) What neutralization changes (and doesn’t)

Neutralization fraction $\eta$ reduces the **effective perveance**:

$$
K_{\text{eff}}=(1-\eta)\,K.
$$

In the space-charge dominated regime, the **matched envelope** (size and divergence) scales roughly as

$$
R,\ R' \ \propto\ \sqrt{\,1-\eta\,}.
$$

The **normalized emittance itself is not improved**; you are removing space-charge defocus so the **projected beam** entering the inflector is smaller and better matched.

A very good rule of thumb for **inflector transmission gain** is

$$
\boxed{\text{gain} \ \approx\ \frac{1}{\sqrt{\,1-\eta\,}}}
$$

(until you hit the inflector’s hard aperture and central-region limits).

---

# 2) How much neutralization at your gas/length?

At $10^{-5}$ torr and $L=0.2\!-\!0.3\ \text{m}$, the beam’s own ionization readily supplies electrons; build-up times are tens of µs (faster for Kr). Reasonable steady $\eta$ ranges:

* **Hydrogen (H₂):** $\eta\approx 0.70$–0.85
* **Krypton (Kr):** $\eta\approx 0.85$–0.95

(Heavier Kr has larger ionization cross-section and holds electrons more effectively, pushing $\eta$ higher. At these pressures and path lengths, multiple scattering is negligible.)

**Current dependence:** at higher beam current the **residual** space charge $(1-\eta)I$ is larger; $\eta$ can sag slightly with $I$ if electrons are over-cleared. Below, I assume a mild trend with current.

---

# 3) Envelope “focusing” before the inflector

Relative *shrink* of beam size/divergence vs. un-neutralized:

$$
\frac{R_\eta}{R_0}=\sqrt{1-\eta}.
$$

| Gas | $\eta$ (low–high) | Size/divergence shrink $R_\eta/R_0$ |
| --- | ----------------- | ----------------------------------- |
| H₂  | 0.70 → 0.85       | 0.548 → 0.387                       |
| Kr  | 0.85 → 0.95       | 0.387 → 0.224                       |

So with **Kr** you can expect the projected envelope at the inflector entrance to be **\~2.6–4.5× smaller area** (since area ∝ $R^2$) than without neutralization.

---

# 4) Transmission improvement through the inflector

Baseline, **un-neutralized** acceptance estimate:

$$
T_0 \approx \frac{A_{\text{inf}}}{\varepsilon_{\text{rms}}}
\approx \frac{60}{625} \approx 9.6\% \quad(\text{order of magnitude}).
$$

Improved transmission $T \approx T_0 \times \text{gain}$, with
$\text{gain}=1/\sqrt{1-\eta}$. I also show a gentle $\eta(I)$ trend:

### H₂ column (30 keV)

| Beam current | assumed $\eta$ | gain  | $T \approx T_0\times$gain |
| ------------:| --------------:| -----:| -------------------------:|
| 1 mA         | 0.80           | 2.236 | **21%**                   |
| 5 mA         | 0.75           | 2.000 | **19%**                   |
| 10 mA        | 0.70           | 1.826 | **18%**                   |

### Kr column (30 keV)

| Beam current | assumed $\eta$ | gain  | $T \approx T_0\times$gain |
| ------------:| --------------:| -----:| -------------------------:|
| 1 mA         | 0.92           | 3.536 | **34%**                   |
| 5 mA         | 0.90           | 3.162 | **30%**                   |
| 10 mA        | 0.85           | 2.582 | **25%**                   |

> These are **stand-alone inflector transmission** estimates; **overall source→capture** will be lower once RF phase acceptance and central-region losses are included. Also, if the inflector’s **hard aperture** becomes the limiter, transmissions will **saturate** around **\~30–50%** even if $\eta$ is increased further.

---

# 5) Sanity checks (your conditions)

* **Neutralization time:** with $10^{-5}$ torr and 30 keV protons, build-up times $\sim 25$–130 µs (Kr faster than H₂) — easily fast enough for CW beams.
* **Scattering/emittance growth:** negligible at $10^{-5}$ torr over 0.2–0.3 m.
* **Downstream matching:** once neutralized, **re-match LEBT optics** so the smaller envelope actually lands in the inflector gap; otherwise you leave performance on the table.

---

## Bottom line

* Expect **envelope shrink** by a factor **0.55 → 0.39 (H₂)** and **0.39 → 0.22 (Kr)** relative to un-neutralized, at your pressure/length.
* That translates to about **2× (H₂)** up to **3–4.5× (Kr)** **gain** in **inflector transmission**, i.e., **\~18–21% (H₂)** and **\~25–34% (Kr)** for your 30 keV, 1–10 mA range — assuming a typical inflector acceptance and good matching.
