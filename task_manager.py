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


def next_id(tasks):
    """Return the next unused task id."""
    return max((task["id"] for task in tasks), default=0) + 1


def add_task(tasks, title):
    """Add a new task to the list and return it."""
    task = {"id": next_id(tasks), "title": title, "done": False}
    tasks.append(task)
    return task


def format_task(task):
    """Return a one-line text version of a task for display."""
    mark = "x" if task["done"] else " "
    return f"[{mark}] {task['id']}. {task['title']}"


def complete_task(tasks, task_id):
    """Mark the task with the given id as completed."""
    for task in tasks:
        if task["id"] == task_id:
            if task["done"]:
                raise ValueError(f"Task {task_id} is already completed.")
            task["done"] = True
            return task
    raise ValueError(f"Task {task_id} not found.")


def delete_task(tasks, task_id):
    """Delete the task with the given id."""
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            return tasks.pop(index)
    return None
