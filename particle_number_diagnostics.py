import numpy as np
from pathlib import Path

p = Path("runs/cxx_H2_mcc_2k/reducedfiles/particle_number.txt")
d = np.genfromtxt(p, comments="#", delimiter=",")

if d.ndim == 1:
    d = d.reshape(1, -1)

print("shape:", d.shape)
print("first row:", d[0])
print("last row:", d[-1])

# Expected species order:
# beam_protons, plasma_electrons, h2_ions

n_species = 3
phys_offset = 2 + 1 + n_species

step = d[:, 0]
time = d[:, 1]
Np = d[:, phys_offset + 1]
Ne = d[:, phys_offset + 2]
Ni = d[:, phys_offset + 3]

print("Initial Np, Ne, Ni:", Np[0], Ne[0], Ni[0])
print("Final   Np, Ne, Ni:", Np[-1], Ne[-1], Ni[-1])
print("Delta Ne:", Ne[-1] - Ne[0])
print("Delta Ni:", Ni[-1] - Ni[0])
print("Delta Ne / Delta Ni:", (Ne[-1] - Ne[0]) / (Ni[-1] - Ni[0] + 1e-300))
print("Np final / initial:", Np[-1] / (Np[0] + 1e-300))
