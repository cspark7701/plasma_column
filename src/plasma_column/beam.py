"""
src/plasma_column/beam.py

Beam physics calculations, relativistic kinematics, perveance formulas,
and RF bunched beam model definitions.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from plasma_column.constants import C, QE, MP, EPSILON_0


@dataclass
class ProtonBeam:
    """Proton beam physics parameters for continuous (DC) beam."""
    energy_keV: float = 30.0
    current_mA: float = 10.0
    radius_m: float = 2.0e-3
    rms_divergence: float = 0.0

    @property
    def energy_joules(self) -> float:
        return self.energy_keV * 1000.0 * QE

    @property
    def gamma(self) -> float:
        return 1.0 + (self.energy_joules / (MP * C**2))

    @property
    def beta(self) -> float:
        g = self.gamma
        return math.sqrt(1.0 - 1.0 / (g**2))

    @property
    def velocity(self) -> float:
        return self.beta * C

    @property
    def current_A(self) -> float:
        return self.current_mA * 1.0e-3

    @property
    def perveance_K0(self) -> float:
        """Generalized uncompensated beam perveance K0."""
        b = self.beta
        g = self.gamma
        return (QE * self.current_A) / (2.0 * math.pi * EPSILON_0 * MP * (b * C)**3 * (g**3))


@dataclass
class RFFocusedBeam(ProtonBeam):
    """
    RF-bunched proton beam model downstream of the upstream buncher.
    """
    rf_frequency_hz: float = 50.0e6
    bunch_phase_width_deg: float = 36.0
    bunching_factor: float = 5.0

    @property
    def beam_current_average_mA(self) -> float:
        return self.current_mA

    @property
    def beam_current_peak_mA(self) -> float:
        return self.current_mA * self.bunching_factor

    @property
    def bunch_duration_s(self) -> float:
        """Bunch temporal width Delta_t_b [s]."""
        return (self.bunch_phase_width_deg / 360.0) / self.rf_frequency_hz

    @property
    def bunch_length_m(self) -> float:
        """Bunch spatial length Delta_z_b [m]."""
        return self.velocity * self.bunch_duration_s

    @property
    def peak_perveance_K0(self) -> float:
        """Uncompensated peak perveance K0,peak."""
        return self.perveance_K0 * self.bunching_factor

    def peak_effective_perveance_ratio(self, eta_avg: float) -> float:
        """
        Computes peak-bunch effective perveance ratio:
        K_eff,peak / K0,peak ~= 1 - eta_avg / B_f
        """
        if self.bunching_factor <= 0:
            raise ValueError("bunching_factor must be positive")
        return 1.0 - (eta_avg / self.bunching_factor)
