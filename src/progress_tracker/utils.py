"""Utility functions for progress tracker."""

from pathlib import Path


def get_project_root() -> Path:
    """Get the project root directory (where pyproject.toml is located)."""
    current = Path(__file__).parent
    while current != current.parent:
        if (current / "pyproject.toml").exists():
            return current
        current = current.parent
    raise FileNotFoundError("Could not find project root (pyproject.toml)")


def get_days_dir() -> Path:
    """Get the days directory."""
    return get_project_root() / "days"


def get_data_dir() -> Path:
    """Get the data directory (.data/)."""
    data_dir = get_project_root() / ".data"
    data_dir.mkdir(exist_ok=True)
    return data_dir
