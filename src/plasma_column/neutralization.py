"""
src/plasma_column/neutralization.py

Core neutralization physics module providing analytical calculations for:
- Gas density and ionization time constants
- Beam relativistic velocity (beta, gamma, speed)
- Neutralization buildup fraction eta(t)
- Effective perveance reduction ratios K_eff / K0
- Bunched-beam peak perveance and phase/length calculations
"""

from __future__ import annotations

import math
from typing import Union
import numpy as np

from plasma_column.constants import C, QE, MP, KB, TORR_TO_PA

ArrayOrFloat = Union[float, np.ndarray]


def gas_density_m3(pressure_torr: float, temperature_K: float = 300.0) -> float:
    """
    Computes ideal gas number density n_gas [m^-3] from pressure in Torr and temperature in K.
    Formula: n_gas = p_pa / (k_B * T)
    """
    if pressure_torr <= 0:
        return 0.0
    pressure_pa = pressure_torr * TORR_TO_PA
    return pressure_pa / (KB * temperature_K)


def proton_beta_gamma_speed(kinetic_energy_keV: float = 30.0) -> tuple[float, float, float]:
    """
    Computes relativistic beta, gamma, and beam speed [m/s] for a proton of given kinetic energy in keV.
    Returns (beta, gamma, v_beam_m_s).
    """
    e_joules = kinetic_energy_keV * 1000.0 * QE
    m_p_c2 = MP * C**2
    gamma = 1.0 + (e_joules / m_p_c2)
    beta = math.sqrt(1.0 - 1.0 / (gamma**2))
    speed_m_s = beta * C
    return beta, gamma, speed_m_s


def ionization_tau_s(n_gas_m3: float, sigma_m2: float, beam_speed_m_s: float) -> float:
    """
    Computes characteristic ionization buildup time tau [s]:
    Formula: tau = 1 / (n_gas * sigma * v_beam)
    """
    if n_gas_m3 <= 0 or sigma_m2 <= 0 or beam_speed_m_s <= 0:
        return float("inf")
    return 1.0 / (n_gas_m3 * sigma_m2 * beam_speed_m_s)


def neutralization_fraction(
    t_s: ArrayOrFloat, tau_s: float, eta_ss: float = 1.0
) -> ArrayOrFloat:
    """
    Analytic neutralization fraction build-up curve:
    Formula: eta(t) = eta_ss * (1 - exp(-t / tau))
    """
    if math.isinf(tau_s) or tau_s <= 0:
        if isinstance(t_s, np.ndarray):
            return np.zeros_like(t_s, dtype=float)
        return 0.0
    if isinstance(t_s, np.ndarray):
        return eta_ss * (1.0 - np.exp(-t_s / tau_s))
    return eta_ss * (1.0 - math.exp(-t_s / tau_s))


def keff_over_k0_from_eta(eta: ArrayOrFloat) -> ArrayOrFloat:
    """
    Computes effective perveance ratio K_eff / K0 from net neutralization fraction eta_net.
    Formula: K_eff / K0 = 1 - eta_net
    """
    return 1.0 - eta


def bunch_length_s(rf_frequency_hz: float, phase_width_deg: float) -> float:
    """
    Computes RF bunch temporal width Delta_t_b [s] from RF frequency in Hz and phase width in degrees.
    Formula: Delta_t_b = phase_width_deg / (360.0 * f_RF)
    """
    if rf_frequency_hz <= 0:
        raise ValueError("rf_frequency_hz must be positive")
    return (phase_width_deg / 360.0) / rf_frequency_hz


def bunch_length_m(
    beam_speed_m_s: float, rf_frequency_hz: float, phase_width_deg: float
) -> float:
    """
    Computes RF bunch spatial width Delta_z_b [m] from beam speed, RF frequency, and phase width in degrees.
    Formula: Delta_z_b = v_beam * Delta_t_b
    """
    dt_b = bunch_length_s(rf_frequency_hz, phase_width_deg)
    return beam_speed_m_s * dt_b


def peak_keff_over_k0_from_average_eta(
    eta_avg: ArrayOrFloat, bunching_factor: float
) -> ArrayOrFloat:
    """
    Computes approximate peak-bunch effective perveance ratio:
    Formula: K_eff,peak / K0,peak ~= 1 - eta_avg / B_f
    """
    if bunching_factor <= 0:
        raise ValueError("bunching_factor must be positive")
    return 1.0 - (eta_avg / bunching_factor)


def compute_neutralization_ratios(
    N_p: float, N_e: float, N_i: float
) -> tuple[float, float, float, float]:
    """
    Computes neutralization metrics:
    - eta_electron_only = N_e / N_p
    - eta_net = (N_e - N_i) / N_p
    - K_eff_electron_only / K0 = 1 - eta_electron_only
    - K_eff_net / K0 = 1 - eta_net
    """
    if N_p <= 0:
        return 0.0, 0.0, 1.0, 1.0

    eta_electron_only = N_e / N_p
    eta_net = (N_e - N_i) / N_p

    k_ratio_electron_only = 1.0 - eta_electron_only
    k_ratio_net = 1.0 - eta_net

    return eta_electron_only, eta_net, k_ratio_electron_only, k_ratio_net
