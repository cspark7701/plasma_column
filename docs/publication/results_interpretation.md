# Physics Interpretation of Simulation Results

## 1. Local Space-Charge Neutralization in Beam Core

The core physical result of this study is that a compact $20\text{ cm}$ beam-ionized plasma cell can achieve $>90\%$ space-charge neutralization ($\eta_{\text{local,net}} \ge 0.90$) within the proton beam core ($r \le 2\text{ mm}$).

- **$\text{H}_2$ Neutralizer at $10^{-5}\text{ Torr}$**: Builds up a compensation plasma on a $\sim 0.26\text{ ms}$ time scale, reducing effective perveance to $K_{\text{eff,local}}/K_0 = 0.10$.
- **$\text{Kr}$ Neutralizer at $10^{-6}\text{ Torr}$**: Due to a $5.5\times$ larger ionization cross section ($\sigma_{i,\text{Kr}} \approx 8.96 \times 10^{-20}\text{ m}^2$), Krypton achieves $95\%$ neutralization ($\eta_{\text{local,net}} = 0.95$) at a tenfold lower pressure ($10^{-6}\text{ Torr}$), significantly reducing neutral gas load on downstream vacuum pumps.

---

## 2. RF-Bunched Beam Interpretation

Because the buncher is located **upstream** of the plasma cell, the plasma forms a steady-state background density over many RF periods rather than a transient single-bunch plasma.

During peak-bunch passage, the instantaneous space-charge density is $B_f = 5$ times higher than the average beam charge density. The effective peak-bunch perveance is:

$$\frac{K_{\text{eff,peak}}}{K_{0,\text{peak}}} \approx 1 - \frac{\eta_{\text{avg}}}{B_f} = 1 - \frac{0.90}{5} = 0.82$$

Thus, while the average space-charge force is reduced by $90\%$, peak-bunch space-charge force is reduced by $18\%$. This is an essential distinction for journal publication.

---

## 3. Downstream Injection Optics Improvement

 envelope integration through the downstream optics line (`solenoid -> Q1 -> Q2 -> inflector`) demonstrates:
- **Vacuum Reference**: Severe space-charge expansion forces envelope radius to $R_{\text{end}} \approx 10\text{ mm}$ at inflector entrance, causing $75\%$ beam loss at the $5\text{ mm}$ inflector entrance aperture ($25.0\%$ transmission).
- **$\text{H}_2/\text{Kr}$ Plasma Column**: Neutralization before the main solenoid allows tight envelope focusing ($R_{\text{end}} \le 3.5\text{ mm}$), yielding $100.0\%$ transmission into the spiral inflector.
