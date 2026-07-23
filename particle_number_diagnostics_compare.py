import numpy as np
from pathlib import Path

for case in ["cxx_H2_mcc_20k_physical", "cxx_Kr_mcc_20k_physical"]:
    p = Path(f"runs/{case}/reducedfiles/particle_number.txt")
    d = np.genfromtxt(p, comments="#", delimiter=",")
    if d.ndim == 1:
        d = d.reshape(1, -1)

    n_species = 3
    phys_offset = 2 + 1 + n_species
    Np = d[:, phys_offset + 1]
    Ne = d[:, phys_offset + 2]
    Ni = d[:, phys_offset + 3]

    print("\n", case)
    print("Delta Ne:", Ne[-1] - Ne[0])
    print("Delta Ni:", Ni[-1] - Ni[0])
    print("Delta Ne / Delta Ni:", (Ne[-1] - Ne[0]) / (Ni[-1] - Ni[0] + 1e-300))

