"""
src/plasma_column/plotting.py

Deterministic plotting pipeline for plasma column analysis figures.
Generates publication- and presentation-ready plots for notebooks, proceedings, and slides.
Always exports both PNG (300 DPI) and PDF formats.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any, Optional, Sequence
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def setup_publication_style() -> None:
    """Configures Matplotlib default rcParams for publication-quality figures."""
    plt.rcParams.update({
        "font.size": 11,
        "axes.labelsize": 12,
        "axes.titlesize": 13,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "figure.titlesize": 14,
        "axes.grid": True,
        "grid.linestyle": "--",
        "grid.alpha": 0.5,
    })


def save_figure(fig: plt.Figure, output_path_basename: str | Path) -> tuple[Path, Path]:
    """
    Saves matplotlib figure to both .png and .pdf formats as required by project guidelines.
    """
    base_path = Path(output_path_basename).with_suffix("")
    base_path.parent.mkdir(parents=True, exist_ok=True)

    png_path = base_path.with_suffix(".png")
    pdf_path = base_path.with_suffix(".pdf")

    fig.savefig(png_path, dpi=300, bbox_inches="tight")
    fig.savefig(pdf_path, bbox_inches="tight")

    return png_path, pdf_path


def plot_particle_counts(
    df: pd.DataFrame,
    output_dir: str | Path,
    case_name: str = "simulation_case",
    title: Optional[str] = None,
) -> tuple[Path, Path]:
    """Plots species particle populations N_p(t), N_e(t), N_i(t) vs time."""
    fig, ax = plt.subplots(figsize=(8, 5))

    time_ns = df["time"].values * 1.0e9 if "time" in df.columns else np.arange(len(df))

    if "Np" in df.columns:
        ax.plot(time_ns, df["Np"], label=r"Protons $N_p$", color="tab:blue", lw=2)
    if "Ne" in df.columns:
        ax.plot(time_ns, df["Ne"], label=r"Electrons $N_e$", color="tab:green", lw=2)
    if "Ni" in df.columns:
        ax.plot(time_ns, df["Ni"], label=r"Ions $N_i$", color="tab:red", lw=2)

    ax.set_xlabel("Time [ns]", fontsize=12)
    ax.set_ylabel("Particle Count", fontsize=12)
    ax.set_title(title or f"Species Populations — {case_name}", fontsize=13)
    ax.grid(True, ls="--", alpha=0.5)
    ax.legend(fontsize=10)

    out_basename = Path(output_dir) / f"{case_name}_particle_counts"
    return save_figure(fig, out_basename)


def plot_neutralization_evolution(
    df: pd.DataFrame,
    output_dir: str | Path,
    case_name: str = "simulation_case",
    title: Optional[str] = None,
) -> tuple[Path, Path]:
    """Plots neutralization fractions eta_electron_only and eta_net vs time."""
    fig, ax = plt.subplots(figsize=(8, 5))

    time_ns = df["time"].values * 1.0e9 if "time" in df.columns else np.arange(len(df))

    if "eta_electron_only" in df.columns:
        ax.plot(time_ns, df["eta_electron_only"], label=r"$\eta_{\text{electron\_only}} = N_e / N_p$", color="tab:green", lw=2)
    if "eta_net" in df.columns:
        ax.plot(time_ns, df["eta_net"], label=r"$\eta_{\text{net}} = (N_e - N_i) / N_p$", color="tab:purple", lw=2)

    ax.set_xlabel("Time [ns]", fontsize=12)
    ax.set_ylabel("Neutralization Fraction", fontsize=12)
    ax.set_ylim(-0.05, 1.1)
    ax.set_title(title or f"Neutralization Fraction Evolution — {case_name}", fontsize=13)
    ax.grid(True, ls="--", alpha=0.5)
    ax.legend(fontsize=10)

    out_basename = Path(output_dir) / f"{case_name}_neutralization_evolution"
    return save_figure(fig, out_basename)


def plot_keff_over_k0(
    df: pd.DataFrame,
    output_dir: str | Path,
    case_name: str = "simulation_case",
    title: Optional[str] = None,
) -> tuple[Path, Path]:
    """Plots effective perveance reduction ratio K_eff / K0 vs time."""
    fig, ax = plt.subplots(figsize=(8, 5))

    time_ns = df["time"].values * 1.0e9 if "time" in df.columns else np.arange(len(df))

    if "keff_over_k0" in df.columns:
        ax.plot(time_ns, df["keff_over_k0"], label=r"$K_{\text{eff}}/K_0 = 1 - \eta_{\text{net}}$", color="tab:red", lw=2)

    ax.set_xlabel("Time [ns]", fontsize=12)
    ax.set_ylabel(r"Perveance Reduction Ratio $K_{\text{eff}}/K_0$", fontsize=12)
    ax.set_ylim(-0.05, 1.1)
    ax.set_title(title or f"Effective Perveance Ratio — {case_name}", fontsize=13)
    ax.grid(True, ls="--", alpha=0.5)
    ax.legend(fontsize=10)

    out_basename = Path(output_dir) / f"{case_name}_keff_over_k0"
    return save_figure(fig, out_basename)


def write_plot_manifest(manifest_entries: list[dict[str, str]], output_file: str | Path) -> Path:
    """Writes manifest.csv recording generated figures, titles, and descriptions."""
    path = Path(output_file)
    path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = ["filename_png", "filename_pdf", "figure_title", "description"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for entry in manifest_entries:
            writer.writerow(entry)

    return path
