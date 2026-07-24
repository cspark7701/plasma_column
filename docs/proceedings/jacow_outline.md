# JACOW Conference Proceeding Outline

**Title**: Numerical and Analytical Modeling of a Compact Plasma Neutralizer for Cyclotron Axial Injection  
**Authors**: Chong Shik Park et al.  

---

## Section Outline

### I. INTRODUCTION
- Motivation: High-current proton beam space-charge divergence in compact cyclotron axial injection.
- Baseline layout: $\text{buncher} \rightarrow \text{plasma neutralizer} \rightarrow \text{solenoid} \rightarrow \text{quadrupoles} \rightarrow \text{inflector}$.
- Role of the neutralizer: Reduce effective perveance $K_{\text{eff}}$ prior to solenoid matching.

### II. PHYSICS MODEL AND SPECIES CROSS SECTIONS
- Ionization kinetics: $p^+ + \text{Gas} \rightarrow p^+ + \text{Gas}^+ + e^-$.
- Comparison of $\text{H}_2$ ($\sigma_{\text{ion}} = 1.61\text{ Å}^2$) and $\text{Kr}$ ($\sigma_{\text{ion}} = 8.96\text{ Å}^2$) at $30\text{ keV}$.
- Gas pressure and differential pumping constraints ($10^{-5}\text{ Torr } \text{H}_2$ vs $10^{-6}\text{ Torr } \text{Kr}$).

### III. RF-BUNCHED BEAM SPACE-CHARGE DILUTION
- Impact of upstream RF bunching ($f_{\text{RF}} = 50\text{ MHz}, B_f = 5$).
- Derivation of peak-bunch perveance reduction: $K_{\text{eff,peak}}/K_{0,\text{peak}} \approx 1 - \eta_{\text{avg}}/B_f$.
- Interpretation of space-charge dilution during micro-bunch passage.

### IV. WARPX PIC SIMULATION COMPARISON
- Methodologies: Static seeded, dynamic Python callback, and C++ MCC collision tracking.
- Global species population tracking vs local beam-core charge density ratios.
- Transverse beam envelope evolution and emittance degradation analysis.

### V. CONCLUSION AND OUTLOOK
- Summary of $\text{Kr}$ performance advantage over $\text{H}_2$.
- Implications for compact cyclotron injection optics design.
