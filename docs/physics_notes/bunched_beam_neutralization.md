# Bunched-Beam Neutralization Physics

## 1. Overview

In cyclotron axial injection lines, the proton beam passes through an upstream RF buncher prior to entering the plasma neutralizer cell:

$$\text{buncher} \rightarrow \text{plasma neutralizer} \rightarrow \text{solenoid} \rightarrow \text{quadrupoles} \rightarrow \text{inflector}$$

RF bunching concentrates beam current into periodic micro-bunches, creating a high peak current $I_{\text{peak}}$ relative to the time-averaged current $I_{\text{avg}}$.

---

## 2. Definitions and Kinematics

- $I_{\text{avg}}$: Time-averaged beam current
- $B_f$: Bunching factor ($B_f = I_{\text{peak}} / I_{\text{avg}} \ge 1$)
- $I_{\text{peak}} = B_f \cdot I_{\text{avg}}$
- $f_{\text{RF}}$: RF frequency (e.g. $50\text{ MHz}$)
- $\Delta \phi$: Bunch phase width in degrees
- $\Delta t_b = \frac{\Delta \phi}{360^{\circ} \cdot f_{\text{RF}}}$: Bunch time width
- $\Delta z_b = v_{\text{beam}} \cdot \Delta t_b = \beta c \Delta t_b$: Bunch spatial length

---

## 3. Effective Peak-Bunch Perveance

If a plasma column provides an average neutralization $\eta_{\text{avg}}$ over the RF period, the plasma electron density $n_e$ responds primarily to the DC component if the electron plasma period or response time exceeds the bunch length.

Under this steady-state background approximation, the instantaneous peak-bunch space charge perveance ratio is given by:

$$\frac{K_{\text{eff,peak}}}{K_{0,\text{peak}}} \approx 1 - \frac{\eta_{\text{avg}}}{B_f}$$

### Physical Implications

1. **Space-Charge Dilution**: Even if the plasma cell achieves high average neutralization ($\eta_{\text{avg}} \approx 0.90$), a high bunching factor (e.g., $B_f = 5$) reduces the effective peak neutralization to:

$$\frac{K_{\text{eff,peak}}}{K_{0,\text{peak}}} \approx 1 - \frac{0.90}{5} = 0.82$$

This means $82\%$ of the uncompensated peak space charge remains active during bunch passage.
2. **Design Requirement**: High-current axial injection systems must evaluate space charge optics at peak bunch current rather than assuming $100\%$ DC space-charge cancellation.
