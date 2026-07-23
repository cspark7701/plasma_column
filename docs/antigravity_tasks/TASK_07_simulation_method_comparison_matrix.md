# TASK 07 — Simulation Method Comparison Matrix

## Objective

Create a systematic comparison among vacuum, seeded H2, seeded Kr, Python-callback source, and C++/MCC/custom-source methods.

## Required cases

At minimum:
- `vacuum_reference`
- `seeded_H2_1e-6Torr`
- `seeded_H2_1e-5Torr`
- `seeded_Kr_1e-6Torr`
- `seeded_Kr_1e-5Torr`
- `callback_H2_dynamic`
- `callback_Kr_dynamic`
- `cxx_H2_mcc_or_custom`
- `cxx_Kr_mcc_or_custom`

## Required outputs

For each case, produce:
- `metadata.json`
- `neutralization_from_particle_number.csv`
- `local_neutralization.csv`, if available
- `beam_envelope.csv`
- `plots/Keff_over_K0.png`
- `plots/particle_counts.png`
- `plots/beam_envelope.png`

## Required script

Create:
- `scripts/run_scan.py`

It must support:

```bash
python scripts/run_scan.py --matrix cases/method_comparison.yaml --dry_run
python scripts/run_scan.py --matrix cases/method_comparison.yaml --run
```

## Constraints

- Use short small-test runs first.
- Avoid huge plotfiles unless explicitly requested.
- Keep C++/custom WarpX runs separate from pure-Python seeded runs.

## Deliverables

- `cases/method_comparison.yaml`
- `scripts/run_scan.py`
- `docs/method_comparison.md`

## Acceptance criteria

- Dry-run prints all commands without launching long jobs.
- Each case has a unique output directory.
- The comparison table clearly states which method is physical, approximate, seeded, or diagnostic-only.
