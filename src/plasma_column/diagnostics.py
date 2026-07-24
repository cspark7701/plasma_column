"""
src/plasma_column/diagnostics.py

Diagnostic parsing routines for particle numbers, species population tracking,
global neutralization metrics, local core space-charge compensation, z-resolved profiles,
and radial charge-density diagnostics.
"""

from __future__ import annotations

import warnings
from pathlib import Path
from typing import Any, Optional
import numpy as np
import pandas as pd

from plasma_column.constants import ELEMENTARY_CHARGE
from plasma_column.neutralization import compute_neutralization_ratios

GLOBAL_WARNING_MSG = (
    "WARNING: local neutralization cannot be inferred from global particle count alone."
)


def warn_global_count_limitation() -> None:
    """
    Issues an explicit warning that global particle-number ratios do not guarantee local space-charge compensation.
    """
    print(GLOBAL_WARNING_MSG)
    warnings.warn(
        "Global particle-number ratios (Ne/Np, Ni/Np) reflect domain-wide counts "
        "and DO NOT guarantee local space-charge compensation inside the beam core "
        "within the plasma column cell.",
        UserWarning,
        stacklevel=2,
    )


def load_particle_number_diagnostic(filepath: str | Path) -> pd.DataFrame:
    """
    Parses WarpX ParticleNumber reduced diagnostic text file into a structured pandas DataFrame.
    Supports both comma-separated and space-separated formats with header comments.
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Particle number diagnostic file not found: {path}")

    # Inspect header line for column names
    header_line = None
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                header_line = line.strip("# \n")
            else:
                break

    # Try space/tab whitespace delimiter first, then comma
    data = np.genfromtxt(path, comments="#")
    if data.ndim == 1 and (np.isnan(data).any() or data.size == 0):
        data = np.genfromtxt(path, comments="#", delimiter=",")

    if data.size == 0:
        return pd.DataFrame()

    if data.ndim == 1:
        data = data.reshape(1, -1)

    ncols = data.shape[1]

    # Assign default or extracted column names
    if header_line:
        clean_header = header_line.replace(",", " ").split()
        if len(clean_header) == ncols:
            cols = clean_header
        else:
            cols = [f"col_{i}" for i in range(ncols)]
    else:
        cols = [f"col_{i}" for i in range(ncols)]

    df = pd.DataFrame(data, columns=cols)

    # Standardize step and time columns
    if "step" not in df.columns and ncols >= 1:
        df.rename(columns={cols[0]: "step"}, inplace=True)
    if "time" not in df.columns and ncols >= 2:
        df.rename(columns={cols[1]: "time"}, inplace=True)

    # Extract species particle counts
    if "Np" not in df.columns:
        if ncols >= 8:
            df["Np"] = data[:, 5]
            df["Ne"] = data[:, 6]
            df["Ni"] = data[:, 7]
        elif ncols >= 5:
            df["Np"] = data[:, 2]
            df["Ne"] = data[:, 3]
            df["Ni"] = data[:, 4]

    return df


def compute_particle_number_metrics(
    df: pd.DataFrame, Np_col: str = "Np", Ne_col: str = "Ne", Ni_col: str = "Ni"
) -> pd.DataFrame:
    """
    Computes global neutralization and perveance reduction ratios from particle count DataFrame.
    """
    out = df.copy()

    if Np_col not in out.columns or Ne_col not in out.columns or Ni_col not in out.columns:
        warn_global_count_limitation()
        return out

    Np = out[Np_col].values
    Ne = out[Ne_col].values
    Ni = out[Ni_col].values

    # Prevent division by zero
    safe_Np = np.where(Np > 0, Np, np.nan)

    out["eta_electron_only"] = Ne / safe_Np
    out["eta_ion_only"] = Ni / safe_Np
    out["eta_net"] = (Ne - Ni) / safe_Np
    out["keff_over_k0"] = 1.0 - out["eta_net"]
    out["keff_over_k0_electron_only"] = 1.0 - out["eta_electron_only"]

    warn_global_count_limitation()

    return out


def compute_local_core_neutralization(
    ne_3d: np.ndarray,
    ni_3d: np.ndarray,
    np_3d: np.ndarray,
    x_coords: np.ndarray,
    y_coords: np.ndarray,
    z_coords: np.ndarray,
    z_min_col: float = 0.0,
    z_max_col: float = 0.20,
    r_core: float = 0.002,
) -> dict[str, Any]:
    """
    Computes volume-averaged local electron, ion, and proton number densities inside the beam core
    (r <= r_core) within the plasma column region (z_min_col <= z <= z_max_col).
    """
    X, Y, Z = np.meshgrid(x_coords, y_coords, z_coords, indexing="ij")
    R = np.sqrt(X**2 + Y**2)

    mask = (Z >= z_min_col) & (Z <= z_max_col) & (R <= r_core)

    if not np.any(mask):
        return {
            "ne_core_avg": 0.0,
            "ni_core_avg": 0.0,
            "np_core_avg": 0.0,
            "eta_net_local": 0.0,
            "eta_electron_only_local": 0.0,
            "keff_over_k0_local": 1.0,
            "keff_over_k0_electron_only_local": 1.0,
            "overcompensated": False,
        }

    ne_avg = float(np.mean(ne_3d[mask]))
    ni_avg = float(np.mean(ni_3d[mask]))
    np_avg = float(np.mean(np_3d[mask]))

    eta_electron_only_local = ne_avg / np_avg if np_avg > 0 else 0.0
    eta_net_local = (ne_avg - ni_avg) / np_avg if np_avg > 0 else 0.0
    keff_local = 1.0 - eta_net_local
    keff_electron_only_local = 1.0 - eta_electron_only_local
    overcompensated = bool(keff_local < 0.0)

    return {
        "ne_core_avg": ne_avg,
        "ni_core_avg": ni_avg,
        "np_core_avg": np_avg,
        "eta_net_local": eta_net_local,
        "eta_electron_only_local": eta_electron_only_local,
        "keff_over_k0_local": keff_local,
        "keff_over_k0_electron_only_local": keff_electron_only_local,
        "overcompensated": overcompensated,
    }


def compute_local_neutralization_vs_z(
    ne_3d: np.ndarray,
    ni_3d: np.ndarray,
    np_3d: np.ndarray,
    x_coords: np.ndarray,
    y_coords: np.ndarray,
    z_coords: np.ndarray,
    r_core: float = 0.002,
) -> pd.DataFrame:
    """
    Computes slice-by-slice core metrics (r <= r_core) along the z axis.
    """
    X, Y = np.meshgrid(x_coords, y_coords, indexing="ij")
    R = np.sqrt(X**2 + Y**2)
    radial_mask = R <= r_core

    records = []
    for k, z_val in enumerate(z_coords):
        if not np.any(radial_mask):
            ne_z, ni_z, np_z = 0.0, 0.0, 0.0
        else:
            ne_z = float(np.mean(ne_3d[:, :, k][radial_mask]))
            ni_z = float(np.mean(ni_3d[:, :, k][radial_mask]))
            np_z = float(np.mean(np_3d[:, :, k][radial_mask]))

        eta_net_z = (ne_z - ni_z) / np_z if np_z > 0 else 0.0
        eta_e_z = ne_z / np_z if np_z > 0 else 0.0
        keff_z = 1.0 - eta_net_z

        records.append({
            "z": float(z_val),
            "ne_core_z": ne_z,
            "ni_core_z": ni_z,
            "np_core_z": np_z,
            "eta_net_local_z": eta_net_z,
            "eta_electron_only_local_z": eta_e_z,
            "keff_over_k0_local_z": keff_z,
        })

    return pd.DataFrame(records)


def compute_radial_density_profiles(
    ne_3d: np.ndarray,
    ni_3d: np.ndarray,
    np_3d: np.ndarray,
    x_coords: np.ndarray,
    y_coords: np.ndarray,
    z_coords: np.ndarray,
    z_min_col: float = 0.0,
    z_max_col: float = 0.20,
    r_max: float = 0.015,
    n_bins: int = 50,
) -> pd.DataFrame:
    """
    Computes radially-binned average species densities within the plasma cell z-bounds.
    """
    X, Y, Z = np.meshgrid(x_coords, y_coords, z_coords, indexing="ij")
    R = np.sqrt(X**2 + Y**2)

    z_mask = (Z >= z_min_col) & (Z <= z_max_col) & (R <= r_max)

    r_edges = np.linspace(0.0, r_max, n_bins + 1)
    r_centers = 0.5 * (r_edges[:-1] + r_edges[1:])

    r_flat = R[z_mask]
    ne_flat = ne_3d[z_mask]
    ni_flat = ni_3d[z_mask]
    np_flat = np_3d[z_mask]

    records = []
    e_charge = ELEMENTARY_CHARGE

    for i in range(n_bins):
        r_low, r_high = r_edges[i], r_edges[i + 1]
        bin_mask = (r_flat >= r_low) & (r_flat < r_high)

        if np.any(bin_mask):
            ne_val = float(np.mean(ne_flat[bin_mask]))
            ni_val = float(np.mean(ni_flat[bin_mask]))
            np_val = float(np.mean(np_flat[bin_mask]))
        else:
            ne_val, ni_val, np_val = 0.0, 0.0, 0.0

        rho_net = e_charge * (np_val - ne_val + ni_val)

        records.append({
            "r": float(r_centers[i]),
            "ne_r": ne_val,
            "ni_r": ni_val,
            "np_r": np_val,
            "rho_net_r": rho_net,
        })

    return pd.DataFrame(records)


def compute_beam_core_charge_density(
    ne_3d: np.ndarray,
    ni_3d: np.ndarray,
    np_3d: np.ndarray,
    x_coords: np.ndarray,
    y_coords: np.ndarray,
    z_coords: np.ndarray,
    z_min_col: float = 0.0,
    z_max_col: float = 0.20,
    r_core: float = 0.002,
) -> dict[str, float]:
    """
    Computes volumetric beam-core charge densities (C/m^3) for protons, electrons, ions, and net charge.
    """
    core_info = compute_local_core_neutralization(
        ne_3d, ni_3d, np_3d, x_coords, y_coords, z_coords, z_min_col, z_max_col, r_core
    )
    e_charge = ELEMENTARY_CHARGE

    rho_p = e_charge * core_info["np_core_avg"]
    rho_e = -e_charge * core_info["ne_core_avg"]
    rho_i = e_charge * core_info["ni_core_avg"]
    rho_net = rho_p + rho_e + rho_i

    return {
        "rho_p": float(rho_p),
        "rho_e": float(rho_e),
        "rho_i": float(rho_i),
        "rho_net": float(rho_net),
    }


def generate_synthetic_3d_grid(
    nx: int = 31,
    ny: int = 31,
    nz: int = 50,
    x_max: float = 0.015,
    y_max: float = 0.015,
    z_min: float = 0.0,
    z_max: float = 0.30,
    n_proton_peak: float = 1.0e15,
    eta_target: float = 0.8,
    displaced_x: float = 0.0,
    overcompensated: bool = False,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Generates synthetic 3D spatial grids and species density arrays for testing local masks.
    """
    x = np.linspace(-x_max, x_max, nx)
    y = np.linspace(-y_max, y_max, ny)
    z = np.linspace(z_min, z_max, nz)

    X, Y, Z = np.meshgrid(x, y, z, indexing="ij")
    R_beam = np.sqrt(X**2 + Y**2)
    R_elec = np.sqrt((X - displaced_x)**2 + Y**2)

    sigma_r = 0.002
    np_3d = n_proton_peak * np.exp(-(R_beam**2) / (2.0 * sigma_r**2))

    multiplier = 1.25 if overcompensated else eta_target
    ne_3d = multiplier * n_proton_peak * np.exp(-(R_elec**2) / (2.0 * sigma_r**2))
    ni_3d = 0.05 * ne_3d

    return ne_3d, ni_3d, np_3d, x, y, z
