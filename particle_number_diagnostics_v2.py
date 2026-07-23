import numpy as np
from pathlib import Path

case = "cxx_H2_mcc_20k_physical"
#case = "cxx_Kr_mcc_20k_physical"
p = Path(f"runs/{case}/reducedfiles/particle_number.txt")

d = np.genfromtxt(p, comments="#", delimiter=",")
if d.ndim == 1:
    d = d.reshape(1, -1)

n_species = 3
phys_offset = 2 + 1 + n_species

step = d[:, 0].astype(int)
time = d[:, 1]

Np = d[:, phys_offset + 1]
Ne = d[:, phys_offset + 2]
Ni = d[:, phys_offset + 3]

valid = Np > 0.0

print("First row:")
print("  step =", step[0])
print("  Np, Ne, Ni =", Np[0], Ne[0], Ni[0])

print("Last row:")
print("  step =", step[-1])
print("  Np, Ne, Ni =", Np[-1], Ne[-1], Ni[-1])

if not np.any(valid):
    raise RuntimeError("No diagnostic row has Np > 0. Beam protons are not entering the domain.")

i0 = np.where(valid)[0][0]

print("\nFirst nonzero-proton row:")
print("  step =", step[i0])
print("  time =", time[i0])
print("  Np, Ne, Ni =", Np[i0], Ne[i0], Ni[i0])

delta_Np = Np[-1] - Np[i0]
delta_Ne = Ne[-1] - Ne[i0]
delta_Ni = Ni[-1] - Ni[i0]

print("\nChanges from first valid proton row:")
print("  Delta Np =", delta_Np)
print("  Delta Ne =", delta_Ne)
print("  Delta Ni =", delta_Ni)

print("\nRatios:")
print("  Np final / first_valid_Np =", Np[-1] / Np[i0])
print("  Delta Ne / Delta Ni =", delta_Ne / (delta_Ni + 1e-300))
print("  Ne final / Np final =", Ne[-1] / Np[-1] if Np[-1] > 0 else np.nan)
print("  Ni final / Np final =", Ni[-1] / Np[-1] if Np[-1] > 0 else np.nan)
print("  global net neutralization =", (Ne[-1] - Ni[-1]) / Np[-1] if Np[-1] > 0 else np.nan)
