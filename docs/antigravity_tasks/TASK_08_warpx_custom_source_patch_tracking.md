# TASK 08 — WarpX Custom Source Patch Tracking

## Objective

Document and stabilize the locally modified WarpX source code used for the plasma-column simulation.

## Required steps

1. Inspect the WarpX git diff.

   ```bash
   cd /home/cspark/Work/simulation_codes-working/warpx
   git diff --stat
   git diff --name-only
   ```

2. Save a patch file from the current local modifications:

   ```bash
   mkdir -p /home/cspark/Work/projects/plasma_column/docs/warpx_patches
   git diff > /home/cspark/Work/projects/plasma_column/docs/warpx_patches/warpx_plasma_column_current.patch
   ```

3. Write a plain-English summary:
   - `docs/warpx_customization.md`

4. Identify:
   - files changed,
   - new collision/source terms,
   - species assumptions,
   - H2/Kr handling,
   - whether the implementation is proton-impact ionization, electron-impact ionization, charge exchange, or seeded source injection,
   - required compile flags or build steps.

5. Add a script to record WarpX state into simulation metadata.

## Constraints

- Do not commit the full WarpX source tree.
- Do not modify WarpX further in this task unless needed to compile.
- Do not claim self-consistent proton-impact MCC unless the code actually creates `p + gas -> p + ion + electron` events with correct rates and weights.

## Deliverables

- `docs/warpx_customization.md`
- `docs/warpx_patches/warpx_plasma_column_current.patch`
- metadata function recording WarpX git commit and dirty status

## Acceptance criteria

- The project can identify exactly which WarpX source modifications were used for a result.
- The patch can be reviewed independently.
