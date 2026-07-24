"""
src/plasma_column/warpx_io.py

WarpX plotfile / openPMD diagnostic reader wrappers and metadata I/O utilities.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def save_metadata(metadata: dict[str, Any], output_path: str | Path) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
    return path
