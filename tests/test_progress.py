"""Tests for progress tracking."""

import pytest
from progress_tracker.progress import ProgressTracker


@pytest.fixture
def temp_tracker(tmp_path):
    """Create a temporary progress tracker for testing."""
    return ProgressTracker(data_dir=tmp_path)


def test_initialization(temp_tracker):
    """Test that progress tracker initializes with default values."""
    progress = temp_tracker.get_progress()
    assert "LLM Building Plan (Days 1‑60)" in progress
    assert "Runtime Layer (Days 61‑78)" in progress
    assert progress["LLM Building Plan (Days 1‑60)"] == 0


def test_update_phase(temp_tracker):
    """Test updating a phase's progress."""
    temp_tracker.update_phase("LLM Building Plan (Days 1‑60)", 5)
    progress = temp_tracker.get_progress()
    assert progress["LLM Building Plan (Days 1‑60)"] == 5


def test_get_total(temp_tracker):
    """Test getting total completed days."""
    temp_tracker.update_phase("LLM Building Plan (Days 1‑60)", 5)
    temp_tracker.update_phase("Runtime Layer (Days 61‑78)", 2)
    total = temp_tracker.get_total()
    assert total == 7


def test_invalid_phase(temp_tracker):
    """Test that updating an invalid phase raises an error."""
    with pytest.raises(ValueError, match="Unknown phase"):
        temp_tracker.update_phase("Invalid Phase", 5)
