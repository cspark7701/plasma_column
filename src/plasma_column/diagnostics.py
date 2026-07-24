"""
src/plasma_column/diagnostics.py

Diagnostic parsing routines for particle numbers, species population tracking,
global neutralization metrics, and local core space-charge compensation.
"""

from __future__ import annotations

import warnings
from pathlib import Path
from typing import Any, Optional
import numpy as np
import pandas as pd

from plasma_column.neutralization import compute_neutralization_ratios


def warn_global_count_limitation() -> None:
    """
    Issues an explicit warning that global particle-number ratios do not guarantee local space-charge compensation.
    """
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
) -> dict[str, float]:
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
            "keff_over_k0_local": 1.0,
        }

    ne_avg = float(np.mean(ne_3d[mask]))
    ni_avg = float(np.mean(ni_3d[mask]))
    np_avg = float(np.mean(np_3d[mask]))

    eta_net_local = (ne_avg - ni_avg) / np_avg if np_avg > 0 else 0.0
    keff_local = 1.0 - eta_net_local

    return {
        "ne_core_avg": ne_avg,
        "ni_core_avg": ni_avg,
        "np_core_avg": np_avg,
        "eta_net_local": eta_net_local,
        "keff_over_k0_local": keff_local,
    }
