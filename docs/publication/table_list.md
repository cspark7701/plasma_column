# Publication Table List

All publication tables are generated as standardized CSV files under `paper/tables/`:

1. **`table_beam_parameters.csv`**: Beam species, kinetic energy ($30\text{ keV}$), average current ($10\text{ mA}$), radius ($2\text{ mm}$), velocity, perveance $K_0$, RF frequency ($50\text{ MHz}$), phase width ($36^\circ$), bunching factor ($B_f=5$), and peak current ($50\text{ mA}$).
2. **`table_gas_parameters.csv`**: Gas species ($\text{H}_2$ vs $\text{Kr}$), molecular weights, pressures ($10^{-5}$ and $10^{-6}\text{ Torr}$), number densities ($n_{\text{gas}}$), cross sections ($\sigma_i$), and build-up times ($\tau$).
3. **`table_simulation_parameters.csv`**: Numerical grid resolution ($32 \times 32 \times 256$), domain extents, time step ($10^{-11}\text{ s}$), particles per cell, field solver, and collision algorithm.
4. **`table_result_summary.csv`**: Performance comparison table for `vacuum_reference`, `h2_baseline`, and `kr_assisted` cases showing local $\eta_{\text{net}}$, $K_{\text{eff}}/K_0$, peak perveance, and inflector transmission.
5. **`table_validation_summary.csv`**: Custom ion-impact MCC verification test matrix (Tests 1–7) showing physics conditions, expected behavior, relative errors, and pass status.
