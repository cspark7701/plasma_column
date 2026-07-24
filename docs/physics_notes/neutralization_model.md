# Space-Charge Neutralization Model

## 1. Physical Mechanisms

A $30\text{ keV}$ proton beam propagating through a background gas cell (e.g., $\text{H}_2$ or $\text{Kr}$) ionizes neutral gas molecules via proton-impact collisions:

$$p^+ + \text{Gas} \rightarrow p^+ + \text{Gas}^+ + e^-$$

The generated secondary electrons are trapped in the beam's attractive space-charge potential, while secondary ions are expelled radially.

---

## 2. Key Physics Metrics

The charge state of the plasma-beam column is characterized by:

$$\eta_{\text{electron\_only}} = \frac{N_e}{N_p}$$

$$\eta_{\text{net}} = \frac{N_e - N_i}{N_p}$$

$$\frac{K_{\text{eff}}}{K_0} = 1 - \eta_{\text{net}}$$

where:
- $N_p$: Total beam proton count
- $N_e$: Total plasma electron count
- $N_i$: Total plasma ion count
- $K_0$: Uncompensated beam perveance
- $K_{\text{eff}}$: Effective space-charge perveance after neutralization

---

## 3. Ionization Time Constant $\tau$

The characteristic space-charge neutralization time constant $\tau$ is given by:

$$\tau = \frac{1}{n_{\text{gas}} \sigma_{\text{ion}} v_{\text{beam}}}$$

where:
- $n_{\text{gas}} = \frac{p}{k_B T}$: Neutral gas number density
- $\sigma_{\text{ion}}$: Ionization cross section for $30\text{ keV}$ protons
- $v_{\text{beam}} = \beta c$: Proton beam velocity ($\approx 2.40 \times 10^6\text{ m/s}$ for $30\text{ keV}$)

Analytical neutralization build-up follows:

$$\eta(t) = \eta_{\text{ss}} \left(1 - e^{-t/\tau}\right)$$

where $\eta_{\text{ss}}$ is the steady-state equilibrium neutralization fraction.

---

## 4. Caution and Interpretation Limits

1. **Global vs Local Neutralization**: A global ratio $N_e / N_p$ calculated over the full domain does not guarantee local space-charge compensation inside the beam core in the plasma cell.
2. **MCC vs Seeded Models**: Particle-In-Cell simulations with pre-seeded compensation or dynamic Python callback sources are analytical approximations of the steady-state ion-electron pair density. Fully self-consistent impact ionization requires C++ MCC collision tracking with validated cross sections.

---

## 5. Diagnostic Requirements and Implementation

To ensure rigorous physics interpretation:

1. **Global Particle Count Diagnostics**:
   - `ParticleNumber` reduced diagnostics track total particle counts ($N_p, N_e, N_i$) across the full simulation grid.
   - Outputs include both $\eta_{\text{electron\_only}}$ and net neutralization $\eta_{\text{net}} = (N_e - N_i)/N_p$.
   - **Enforced Constraint**: Analysis tools explicitly issue warnings when evaluating only global counts to prevent false claims of local core compensation.

2. **Local Beam-Core Diagnostic**:
   - Evaluates volume-averaged particle densities $n_e, n_i, n_p$ strictly inside $r \le r_{\text{core}}$ within $z \in [z_{\text{min}}, z_{\text{max}}]$ of the plasma cell.
   - Evaluates local effective perveance reduction $K_{\text{eff,local}} / K_0 = 1 - (n_e - n_i)/n_p$.
