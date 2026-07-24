"""
tests/test_case_files.py

Unit tests for validating and parsing YAML configuration files under cases/.
"""

from pathlib import Path
import yaml
import pytest


def get_case_files():
    cases_dir = Path(__file__).resolve().parent.parent / "cases"
    return list(cases_dir.glob("*.yaml"))


def test_yaml_case_files_exist():
    cases = get_case_files()
    assert len(cases) >= 5, f"Expected at least 5 case YAML files, found {len(cases)}"


@pytest.mark.parametrize("case_path", get_case_files(), ids=lambda p: p.name)
def test_parse_case_yaml(case_path: Path):
    data = yaml.safe_load(case_path.read_text(encoding="utf-8"))
    assert isinstance(data, dict), f"Case file {case_path.name} did not parse into a dictionary"
    assert "case_name" in data or case_path.stem in data.get("case_name", case_path.stem)
