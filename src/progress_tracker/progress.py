"""Progress tracking for 100 Days of LLM Inference."""

import json
from pathlib import Path
from typing import Dict


class ProgressTracker:
    """Track progress through the 100-day plan."""
    
    def __init__(self, data_dir: Path = None):
        """Initialize progress tracker.
        
        Args:
            data_dir: Directory to store progress data. Defaults to .data/ in project root.
        """
        if data_dir is None:
            # Find project root (where pyproject.toml is)
            project_root = Path(__file__).parent.parent.parent
            data_dir = project_root / ".data"
        
        self.data_dir = data_dir
        self.data_dir.mkdir(exist_ok=True)
        self.progress_file = self.data_dir / "progress.json"
        
        # Initialize progress if not exists
        self._init_progress()
    
    def _init_progress(self):
        """Initialize progress data with default values."""
        if not self.progress_file.exists():
            default_progress = {
                "LLM Building Plan (Days 1‑60)": 0,
                "Runtime Layer (Days 61‑78)": 0,
                "Infrastructure Layer (Days 79‑86)": 0,
                "Tooling Layer (Days 87‑89)": 0,
                "Deep Implementation (Days 90‑100)": 0,
            }
            self._save_progress(default_progress)
    
    def _load_progress(self) -> Dict[str, int]:
        """Load progress from file."""
        with open(self.progress_file, 'r') as f:
            return json.load(f)
    
    def _save_progress(self, progress: Dict[str, int]):
        """Save progress to file."""
        with open(self.progress_file, 'w') as f:
            json.dump(progress, f, indent=2)
    
    def get_progress(self) -> Dict[str, int]:
        """Get current progress for all phases."""
        return self._load_progress()
    
    def update_phase(self, phase: str, completed: int) -> None:
        """Update progress for a specific phase.
        
        Args:
            phase: Phase name
            completed: Number of completed days
        """
        progress = self._load_progress()
        if phase not in progress:
            raise ValueError(f"Unknown phase: {phase}")
        progress[phase] = completed
        self._save_progress(progress)
    
    def get_total(self) -> int:
        """Get total completed days across all phases."""
        progress = self._load_progress()
        return sum(progress.values())
    
    def update_readme(self, readme_path: Path = None) -> None:
        """Update README.md with current progress.
        
        Args:
            readme_path: Path to README.md. Defaults to project root.
        """
        if readme_path is None:
            project_root = Path(__file__).parent.parent.parent
            readme_path = project_root / "README.md"
        
        progress = self._load_progress()
        
        # Update README using regex
        import re
        content = readme_path.read_text(encoding="utf-8")
        
        for phase, completed in progress.items():
            pattern = rf"(\| {re.escape(phase)} \| )\d+"
            replacement = rf"\g<1>{completed}"
            content = re.sub(pattern, replacement, content)
        
        # Update total
        total = self.get_total()
        total_pattern = r"(\| \*\*Total\*\* \| \*\*)\d+"
        content = re.sub(total_pattern, rf"\g<1>{total}", content)
        
        readme_path.write_text(content, encoding="utf-8")
