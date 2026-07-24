"""
tests/test_bunched_beam.py

Unit tests for RF-bunched beam calculations and peak perveance formulas.
"""

import sys
from pathlib import Path
import math
import pytest

# Ensure src/ is in sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from plasma_column.beam import ProtonBeam, RFFocusedBeam


def test_proton_beam_basics():
    beam = ProtonBeam(energy_keV=30.0, current_mA=10.0)
    assert beam.current_A == 0.010
    assert beam.beta > 0.0075 and beam.beta < 0.0085
    assert beam.perveance_K0 > 0.0


def test_rf_focused_beam():
    beam = RFFocusedBeam(
        energy_keV=30.0,
        current_mA=10.0,
        rf_frequency_hz=50.0e6,
        bunch_phase_width_deg=36.0,
        bunching_factor=5.0,
    )

    assert beam.beam_current_average_mA == 10.0
    assert beam.beam_current_peak_mA == 50.0

    # 36 deg at 50 MHz = 2 ns
    assert math.isclose(beam.bunch_duration_s, 2.0e-9, rel_tol=1e-5)

    # 2.3973e6 m/s * 2 ns ~ 4.79 mm
    assert beam.bunch_length_m > 0.004 and beam.bunch_length_m < 0.006

    # Peak perveance ratio: 1 - 0.9 / 5 = 0.82
    k_peak_ratio = beam.peak_effective_perveance_ratio(0.90)
    assert math.isclose(k_peak_ratio, 0.82, rel_tol=1e-5)


if __name__ == "__main__":
    pytest.main([__file__])
