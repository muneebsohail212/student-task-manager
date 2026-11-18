"""Core logic for the Student Task Manager: loading and saving tasks."""

import json
import os

DATA_FILE = "tasks.json"


def load_tasks(path=DATA_FILE):
    """Load tasks from a JSON file. Return an empty list if none exist."""
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks, path=DATA_FILE):
    """Save the list of tasks to a JSON file."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)
