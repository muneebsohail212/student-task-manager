"""Unit tests for the Student Task Manager core logic."""

import os
import tempfile
import unittest

import task_manager


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        self.tasks = []

    def test_add_task(self):
        task = task_manager.add_task(self.tasks, "Finish DevOps lab")
        self.assertEqual(len(self.tasks), 2)
        self.assertEqual(task["title"], "Finish DevOps lab")
        self.assertFalse(task["done"])

    def test_add_task_rejects_empty_title(self):
        with self.assertRaises(ValueError):
            task_manager.add_task(self.tasks, "   ")
        self.assertEqual(self.tasks, [])

    def test_complete_task(self):
        task = task_manager.add_task(self.tasks, "Read chapter 3")
        task_manager.complete_task(self.tasks, task["id"])
        self.assertTrue(self.tasks[0]["done"])

    def test_complete_missing_task_raises(self):
        with self.assertRaises(ValueError):
            task_manager.complete_task(self.tasks, 99)

    def test_delete_task(self):
        task = task_manager.add_task(self.tasks, "Submit assignment")
        task_manager.delete_task(self.tasks, task["id"])
        self.assertEqual(self.tasks, [])

    def test_delete_invalid_id_raises(self):
        task_manager.add_task(self.tasks, "Keep me")
        with self.assertRaises(ValueError):
            task_manager.delete_task(self.tasks, 0)
        with self.assertRaises(ValueError):
            task_manager.delete_task(self.tasks, 42)

    def test_save_and_load_round_trip(self):
        task_manager.add_task(self.tasks, "Persist me")
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "tasks.json")
            task_manager.save_tasks(self.tasks, path)
            self.assertEqual(task_manager.load_tasks(path), self.tasks)


if __name__ == "__main__":
    unittest.main()
