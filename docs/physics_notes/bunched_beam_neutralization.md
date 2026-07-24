# RF-Bunched Beam Space-Charge Neutralization

## 1. Physics Context and Geometry Constraint

In the baseline axial-injection beamline for the compact cyclotron:

$$\text{buncher} \rightarrow \text{plasma neutralizer} \rightarrow \text{solenoid} \rightarrow \text{quadrupole Q1} \rightarrow \text{quadrupole Q2} \rightarrow \text{spiral inflector}$$

The buncher is situated **upstream** of the plasma neutralizer.

Consequently, the neutralizer receives an already RF-bunched proton beam. The plasma response time $\tau_{\text{plasma}} = 1/\omega_{pe}$ is short compared to the macro-pulse, but plasma ions and background electrons form a quasi-steady background over many RF cycles ($f_{\text{RF}} \approx 50\text{ MHz}$, $T_{\text{RF}} \approx 20\text{ ns}$).

---

## 2. RF Bunching Parameters and Formulas

For a bunched proton beam with average beam current $I_{\text{avg}}$ and RF frequency $f_{\text{RF}}$:

- **Bunch Phase Width**: $\Delta \phi$ [degrees]
- **Bunch Duration**: $\Delta t_b = \frac{\Delta \phi}{360^\circ f_{\text{RF}}}$
- **Bunch Length**: $\Delta z_b = v_p \Delta t_b = \beta c \Delta t_b$
- **Bunching Factor**: $B_f = \frac{I_{\text{peak}}}{I_{\text{avg}}}$
- **Peak Current**: $I_{\text{peak}} = B_f \cdot I_{\text{avg}}$
- **Uncompensated Peak Perveance**: $K_{0,\text{peak}} = B_f \cdot K_0$

---

## 3. Average vs Peak-Bunch Space-Charge Compensation

If the plasma column reaches steady-state average neutralization $\eta_{\text{avg}} = N_e / N_p$, the average effective perveance is:

$$\frac{K_{\text{eff,avg}}}{K_0} = 1 - \eta_{\text{avg}}$$

However, during peak-bunch passage, the instantaneous space-charge charge density in the core is $B_f$ times higher than the average charge density. Thus, the effective peak perveance reduction ratio is:

$$\frac{K_{\text{eff,peak}}}{K_{0,\text{peak}}} \approx 1 - \frac{\eta_{\text{avg}}}{B_f}$$

### Interpretation Limits:
- For $B_f = 5$ and $\eta_{\text{avg}} = 0.90$, $\frac{K_{\text{eff,peak}}}{K_{0,\text{peak}}} \approx 1 - \frac{0.90}{5} = 0.82$.
- Although average space-charge force is reduced by $90\%$, peak-bunch space-charge force is reduced by only $18\%$.
- Journal papers must clearly distinguish between average and peak-bunch perveance reduction to avoid overstating space-charge compensation for RF-bunched beams.
