# TASK 05 — H2/Kr Cross-Section Database and Validation

## Objective

Standardize how proton-impact, electron-impact, and charge-exchange cross sections are loaded, interpolated, validated, and documented for H2 and Kr.

## Required steps

1. Create `src/plasma_column/gas.py`.
2. Implement two-column cross-section table loading.
3. Implement interpolation at the correct collision energy.
4. Record whether the input energy is laboratory energy or center-of-mass energy.
5. Add validation plots:
   - cross section vs. energy,
   - interpolated operating point for 30 keV protons.
6. Document all required cross-section files and paths.

## Required docs

Create:
- `docs/physics_notes/h2_kr_cross_sections.md`

## Constraints

- Do not assume H2 cross-section tables are valid for Kr.
- Fail clearly if Kr tables are missing.
- If using approximate Kr data, label it as approximate.

## Deliverables

- `src/plasma_column/gas.py`
- `scripts/plot_cross_sections.py`
- `docs/physics_notes/h2_kr_cross_sections.md`
- Unit tests for table parsing and interpolation.

## Acceptance criteria

- H2 and Kr data files are discovered or missing files are clearly reported.
- Plots show the 30 keV operating point.
