# Publication Frozen Result Set

## 1. Frozen Simulation Cases

| Case ID | Method Category | Gas | Pressure [Torr] | Description |
|---|---|---|---|---|
| `vacuum_reference` | Baseline | None | $0.0$ | Reference $30\text{ keV}$ proton transport without gas |
| `h2_baseline` | Seeded / MCC | $\text{H}_2$ | $1.0 \times 10^{-5}$ | Baseline $\text{H}_2$ plasma neutralizer |
| `kr_assisted` | Seeded / MCC | $\text{Kr}$ | $1.0 \times 10^{-6}$ | High cross-section $\text{Kr}$ neutralizer |
| `h2_bunched` | RF Bunched | $\text{H}_2$ | $1.0 \times 10^{-5}$ | RF-bunched beam ($B_f=5$) in $\text{H}_2$ |
| `kr_bunched` | RF Bunched | $\text{Kr}$ | $1.0 \times 10^{-6}$ | RF-bunched beam ($B_f=5$) in $\text{Kr}$ |
| `custom_mcc_h2_verified` | Custom MCC | $\text{H}_2$ | $1.0 \times 10^{-5}$ | Verified ion-impact MCC in $\text{H}_2$ |
| `custom_mcc_kr_verified` | Custom MCC | $\text{Kr}$ | $1.0 \times 10^{-6}$ | Verified ion-impact MCC in $\text{Kr}$ |

---

## 2. Primary Frozen Results

1. **Local Core Neutralization**:
   - $\text{H}_2$ ($10^{-5}\text{ Torr}$): $\eta_{\text{net,local}} = 0.90 \implies K_{\text{eff,local}}/K_0 = 0.10$.
   - $\text{Kr}$ ($10^{-6}\text{ Torr}$): $\eta_{\text{net,local}} = 0.95 \implies K_{\text{eff,local}}/K_0 = 0.05$.

2. **RF-Bunched Beam Peak Perveance**:
   - For $B_f = 5$ and $\eta_{\text{avg}} = 0.90$, $K_{\text{eff,peak}}/K_{0,\text{peak}} \approx 0.82$.

3. **Inflector Entrance Transmission**:
   - Vacuum: $25.0\%$ transmission ($75\%$ beam loss at $5\text{ mm}$ aperture).
   - $\text{H}_2$ Neutralized ($90\%$): $100.0\%$ transmission.
   - $\text{Kr}$ Neutralized ($95\%$): $100.0\%$ transmission.
