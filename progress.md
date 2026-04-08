# Progress Tracking

This document describes how to track progress through the 100-day LLM learning plan using the CLI tool.

## Installation

Ensure dependencies are installed with uv:
```bash
uv sync
```

## CLI Commands

### View Current Progress

Show the current progress for all phases:
```bash
uv run llm-100days progress get
```

Output example:
```
Current Progress:
  LLM Building Plan (Days 1‑30): 5
  Runtime Layer (Days 31‑50): 2
  Infrastructure Layer (Days 51‑65): 0
  Tooling Layer (Days 66‑75): 0
  Deep Implementation (Days 76‑100): 0

Total: 7/100
```

### Update Progress for a Phase

Update the completed days for a specific phase:
```bash
uv run llm-100days progress update --phase "LLM Building Plan (Days 1‑30)" --completed 5
```

Available phases:
- `LLM Building Plan (Days 1‑30)`
- `Runtime Layer (Days 31‑50)`
- `Infrastructure Layer (Days 51‑65)`
- `Tooling Layer (Days 66‑75)`
- `Deep Implementation (Days 76‑100)`

### Sync Progress to README

Update the README.md file with current progress:
```bash
uv run llm-100days progress sync
```

This updates the progress table in README.md with the latest values from the progress tracker.

## Day Management

### Create a New Day Directory

Create a new day directory with notebook and solution templates:
```bash
uv run llm-100days day create --day 1
```

This creates:
- `days/day01/notebook.ipynb` – Jupyter notebook template
- `days/day01/solution.py` – Python solution template

## Data Storage

Progress is stored in `.data/progress.json` in the project root. This file is automatically created when you first run the CLI.

## Examples

### Typical Workflow

1. Complete a day's work
2. Update progress:
   ```bash
   uv run llm-100days progress update --phase "LLM Building Plan (Days 1‑30)" --completed 1
   ```
3. Sync to README:
   ```bash
   uv run llm-100days progress sync
   ```

### Create Next Day

When starting a new day:
```bash
uv run llm-100days day create --day 2
```

This creates the day02 directory with templates ready for your work.
