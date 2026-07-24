"""
src/plasma_column/acceptance.py

Spiral inflector entrance acceptance cut and transmission efficiency model.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
import numpy as np
import pandas as pd


@dataclass
class InflectorAcceptance:
    """Spiral inflector entrance geometric acceptance model."""
    aperture_radius_m: float = 0.005  # 5 mm inflector aperture radius
    max_divergence_rad: float = 0.050 # 50 mrad maximum accepted divergence
    normalized_emittance_mrad: float = 1.0e-6


def compute_inflector_transmission(
    Rx_end: float,
    Ry_end: float,
    dRx_end: float,
    dRy_end: float,
    acceptance: InflectorAcceptance = InflectorAcceptance(),
) -> dict[str, float]:
    """
    Computes beam transmission efficiency and moments at spiral inflector entrance.
    """
    r_beam = math.sqrt(0.5 * (Rx_end**2 + Ry_end**2))
    r_ap = acceptance.aperture_radius_m

    # Geometric transmission factor based on aperture clipping
    if r_beam <= r_ap:
        transmission = 1.0
    else:
        transmission = (r_ap / r_beam)**2

    transmission = max(0.0, min(1.0, transmission))
    transmission_percent = transmission * 100.0

    return {
        "Rx_end_mm": Rx_end * 1000.0,
        "Ry_end_mm": Ry_end * 1000.0,
        "dRx_end_mrad": dRx_end * 1000.0,
        "dRy_end_mrad": dRy_end * 1000.0,
        "r_beam_mm": r_beam * 1000.0,
        "inflector_aperture_mm": r_ap * 1000.0,
        "transmission_fraction": transmission,
        "transmission_percent": transmission_percent,
    }


def generate_phase_space_particles(
    Rx: float,
    dRx: float,
    Ry: float,
    dRy: float,
    emittance_geom: float = 1.0e-6,
    n_particles: int = 1000,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Generates transverse phase space macroparticle coordinates (x, x') and (y, y')
    at the inflector entrance matching the beam envelope moments.
    """
    np.random.seed(42)

    # Generate Gaussian ellipse samples matching Rx and dRx
    std_x = Rx / 2.0
    std_xp = max(dRx, emittance_geom / max(Rx, 1e-6))
    x_coords = np.random.normal(0.0, std_x, n_particles)
    xp_coords = np.random.normal(0.0, std_xp, n_particles)

    std_y = Ry / 2.0
    std_yp = max(dRy, emittance_geom / max(Ry, 1e-6))
    y_coords = np.random.normal(0.0, std_y, n_particles)
    yp_coords = np.random.normal(0.0, std_yp, n_particles)

    df_xxp = pd.DataFrame({"x_mm": x_coords * 1000.0, "xp_mrad": xp_coords * 1000.0})
    df_yyp = pd.DataFrame({"y_mm": y_coords * 1000.0, "yp_mrad": yp_coords * 1000.0})

    return df_xxp, df_yyp
