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
- `days/day01/Day_1.ipynb` – Jupyter notebook template
- `days/day01/Notes.md` – Markdown file for notes, key concepts, and code snippets
- `days/day01/Questions.md` – Markdown file for understanding questions, implementation questions, and answers

You can create any day number (1-100):
```bash
uv run llm-100days day create --day 5
uv run llm-100days day create --day 42
```

### Complete a Day

1. **Create the day directory** (if not already created):
   ```bash
   uv run llm-100days day create --day 1
   ```

2. **Open the Jupyter notebook**:
   ```bash
   uv run jupyter notebook
   ```
   Navigate to `days/day01/Day_1.ipynb`

3. **Work through the day's topic**:
   - Read the relevant book chapter(s)
   - Add notes to the notebook markdown cells
   - Write code in the notebook code cells
   - Document results and findings
   - Implement the solution in `solution.py` if needed

4. **Mark the day as complete**:
   ```bash
   uv run llm-100days day complete --day 1
   ```
   This automatically determines which phase the day belongs to and increments the progress counter.

5. **Sync progress to README**:
   ```bash
   uv run llm-100days progress sync
   ```
   
   Or use the `--sync` flag to complete and sync in one command:
   ```bash
   uv run llm-100days day complete --day 1 --sync
   ```

## Data Storage

Progress is stored in `.data/progress.json` in the project root. This file is automatically created when you first run the CLI.

## Examples

### Typical Workflow

**Starting a new day:**
```bash
# Create the day directory
uv run llm-100days day create --day 1

# Start Jupyter
uv run jupyter notebook
```

**After completing the day's work:**
```bash
# Mark day as complete (auto-detects phase)
uv run llm-100days day complete --day 1

# Sync progress to README
uv run llm-100days progress sync
```

**Or combine complete and sync:**
```bash
uv run llm-100days day complete --day 1 --sync
```

**Check your overall progress:**
```bash
uv run llm-100days progress get
```

### Example: Completing Days 1-3

```bash
# Day 1
uv run llm-100days day create --day 1
# Work through the notebook...
uv run llm-100days day complete --day 1 --sync

# Day 2
uv run llm-100days day create --day 2
# Work through the notebook...
uv run llm-100days day complete --day 2 --sync

# Day 3
uv run llm-100days day create --day 3
# Work through the notebook...
uv run llm-100days day complete --day 3 --sync
```

### Moving Between Phases

When you complete all 30 days of the LLM Building Plan, the `day complete` command automatically detects the new phase:
```bash
# Day 31 automatically increments Runtime Layer
uv run llm-100days day create --day 31
# Work through day 31...
uv run llm-100days day complete --day 31 --sync
```

No manual phase tracking needed - the command handles phase detection automatically.
