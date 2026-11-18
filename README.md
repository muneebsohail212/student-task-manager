# Student Task Manager

A small Python console application for students to add, view, complete and delete study tasks. Built as part of **CSC418 – DevOps for Cloud Computing, Lab Assignment 4** to practise Git, GitHub, pull requests, merge conflicts, GitHub Actions and releases.

Project status: Stable (v1.0.0)

## Features

- Add a task (empty or blank titles are rejected)
- Show all tasks with a `[ ]` / `[x]` completion marker
- Mark a task as completed (unknown ids and already-completed tasks give a clear error)
- Delete a task using a valid task id
- Tasks are saved automatically in a local `tasks.json` file
- Automated unit tests run on every push and pull request to `main` (GitHub Actions)

## Requirements

- Python 3.8 or newer (no external packages needed)
- Git

## Setup

```bash
git clone https://github.com/muneebsohail212/student-task-manager.git
cd student-task-manager
python --version
```

## Usage

```bash
python main.py
```

Menu options:

| Option | Action |
|--------|--------|
| 1 | Add a task |
| 2 | Show all tasks |
| 3 | Complete a task by id |
| 4 | Delete a task by id |
| 5 | Exit |

Example session:

```
Choose an option: 1
Task title: Finish DevOps lab
Added task 1: Finish DevOps lab
Choose an option: 3
Task id to complete: 1
Completed: Finish DevOps lab
```

See the full [user guide](docs/user-guide.md) for more details.

## Running the tests

```bash
python -m unittest discover -s tests -v
```

## Project structure

```
student-task-manager/
├── main.py                 # console menu
├── task_manager.py         # core task logic and JSON storage
├── tests/
│   └── test_task_manager.py
├── docs/
│   └── user-guide.md
├── .github/workflows/tests.yml
├── lab-evidence/           # screenshots of key steps
├── LAB-REPORT.md
├── LICENSE
└── README.md
```

## Development workflow

- One feature branch per feature (`feature/add-task`, `feature/complete-task`, `feature/delete-task`)
- Each feature is linked to a GitHub Issue and merged through a reviewed Pull Request
- GitHub Actions runs the unit tests on every push and pull request to `main`

## License

Released under the [MIT License](LICENSE).
