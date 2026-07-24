# Downstream Injection-Line Transport and Optics Model

## 1. Beamline Layout

The compact-cyclotron axial injection line layout is:

$$\text{buncher exit} \rightarrow \text{plasma neutralizer} \rightarrow \text{solenoid} \rightarrow \text{quadrupole Q1} \rightarrow \text{quadrupole Q2} \rightarrow \text{spiral inflector entrance}$$

The baseline neutralizer MUST NOT be placed downstream of the main solenoid.

---

## 2. Space-Charge Envelope Equations

Transverse beam envelope evolution $R_x(z)$ and $R_y(z)$ is calculated using the envelope ODEs:

$$\frac{d^2 R_x}{dz^2} + k_x^2(z) R_x - \frac{2 K_{\text{eff}}}{R_x + R_y} - \frac{\epsilon_{x,n}^2}{\beta^2 \gamma^2 R_x^3} = 0$$

$$\frac{d^2 R_y}{dz^2} + k_y^2(z) R_y - \frac{2 K_{\text{eff}}}{R_x + R_y} - \frac{\epsilon_{y,n}^2}{\beta^2 \gamma^2 R_y^3} = 0$$

where:
- $K_{\text{eff}} = K_0 (1 - \eta_{\text{net}})$ is the net effective space-charge perveance.
- $k_x(z), k_y(z)$ are magnetic focusing strengths from the solenoid ($B_z = 0.15\text{ T}$) and quadrupole doublet Q1 ($G_1 = 5\text{ T/m}$) and Q2 ($G_2 = -4.5\text{ T/m}$).
- $\epsilon_{x,n}, \epsilon_{y,n}$ are normalized transverse emittances ($1.0\text{ mm mrad}$).

---

## 3. Inflector Acceptance Cut and Transmission Efficiency

The spiral inflector entrance is modeled with an aperture radius $r_{\text{aperture}} = 5.0\text{ mm}$.

Transmission efficiency is evaluated as:

$$T = \min\left(1.0, \frac{r_{\text{aperture}}^2}{0.5(R_x^2 + R_y^2)}\right) \times 100\%$$

### Case Comparison:
1. **Vacuum Reference ($\eta = 0.0$)**: Uncompensated space-charge blowup causes envelope expansion, leading to aperture clipping at the inflector entrance.
2. **$\text{H}_2$ Neutralized ($\eta = 0.90$)**: Reduced perveance $K_{\text{eff}}/K_0 = 0.10$ allows downstream solenoid and quadrupole doublet to focus the beam tightly within the $5\text{ mm}$ inflector entrance aperture ($T \approx 100\%$).
3. **$\text{Kr}$ Neutralized ($\eta = 0.95$)**: $95\%$ neutralization provides tight envelope control and low divergence.
