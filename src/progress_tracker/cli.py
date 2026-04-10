"""CLI interface for 100 Days of LLM Inference."""

import argparse
from pathlib import Path
from progress_tracker.progress import ProgressTracker


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="100 Days of LLM Inference - Progress tracking and project management"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Progress command
    progress_parser = subparsers.add_parser("progress", help="Manage progress")
    progress_subparsers = progress_parser.add_subparsers(dest="progress_command", help="Progress commands")
    
    # Get progress
    progress_subparsers.add_parser("get", help="Show current progress")
    
    # Update progress
    update_parser = progress_subparsers.add_parser("update", help="Update progress for a phase")
    update_parser.add_argument("--phase", required=True, help="Phase name")
    update_parser.add_argument("--completed", type=int, required=True, help="Number of completed days")
    
    # Update README
    progress_subparsers.add_parser("sync", help="Update README with current progress")
    
    # Day command
    day_parser = subparsers.add_parser("day", help="Manage daily work")
    day_subparsers = day_parser.add_subparsers(dest="day_command", help="Day commands")
    
    # Create new day
    create_parser = day_subparsers.add_parser("create", help="Create a new day directory")
    create_parser.add_argument("--day", type=int, required=True, help="Day number")
    
    # Complete a day
    complete_parser = day_subparsers.add_parser("complete", help="Mark a day as complete")
    complete_parser.add_argument("--day", type=int, required=True, help="Day number")
    complete_parser.add_argument("--sync", action="store_true", help="Sync progress to README after completing")
    
    args = parser.parse_args()
    
    if args.command == "progress":
        handle_progress(args)
    elif args.command == "day":
        handle_day(args)
    else:
        parser.print_help()


def handle_progress(args):
    """Handle progress commands."""
    tracker = ProgressTracker()
    
    if args.progress_command == "get":
        progress = tracker.get_progress()
        total = tracker.get_total()
        print("Current Progress:")
        for phase, completed in progress.items():
            print(f"  {phase}: {completed}")
        print(f"\nTotal: {total}/100")
    
    elif args.progress_command == "update":
        tracker.update_phase(args.phase, args.completed)
        print(f"Updated {args.phase} to {args.completed} days")
    
    elif args.progress_command == "sync":
        tracker.update_readme()
        print("Updated README.md with current progress")
    
    else:
        print("No progress command specified")


def handle_day(args):
    """Handle day commands."""
    if args.day_command == "create":
        create_day(args.day)
    elif args.day_command == "complete":
        complete_day(args.day, args.sync)
    else:
        print("No day command specified")


def create_day(day_num: int):
    """Create a new day directory with templates."""
    day_str = str(day_num)
    project_root = Path(__file__).parent.parent.parent
    days_dir = project_root / "days"
    day_dir = days_dir / f"day{day_num:02d}"
    
    if day_dir.exists():
        print(f"Day {day_str} already exists at {day_dir}")
        return
    
    day_dir.mkdir(exist_ok=True)
    
    # Create notebook template
    notebook_path = day_dir / f"Day_{day_str}.ipynb"
    notebook_content = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# Day {day_str}\n"
                ]
            }
        ]
    }
    
    import json
    with open(notebook_path, 'w') as f:
        json.dump(notebook_content, f, indent=2)
    
    # Create Notes.md template
    notes_path = day_dir / "Notes.md"
    notes_content = f'''# Day {day_str} Notes

## Topic

## Key Concepts

- 
- 
- 

## Important Details
'''
    notes_path.write_text(notes_content)
    
    # Create Questions.md template
    questions_path = day_dir / "Questions.md"
    questions_content = f'''# Day {day_str} Questions

## Understanding Questions

1. 
2. 
3. 

## Implementation Questions

1. 
2. 
3. 

## Follow-up Questions

1. 
2. 
3. 

## Answers

### Understanding Questions

### Implementation Questions

### Follow-up Questions
'''
    questions_path.write_text(questions_content)
    
    print(f"Created day {day_str} at {day_dir}")
    print(f"  - Day_{day_str}.ipynb")
    print("  - Notes.md")
    print("  - Questions.md")


def complete_day(day_num: int, sync: bool = False):
    """Mark a day as complete by incrementing the appropriate phase.
    
    Args:
        day_num: Day number (1-100)
        sync: Whether to sync progress to README after completing
    """
    tracker = ProgressTracker()
    
    try:
        phase = tracker.complete_day(day_num)
        print(f"Marked day {day_num} as complete")
        print(f"Phase: {phase}")
        
        if sync:
            tracker.update_readme()
            print("Synced progress to README.md")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
