# User Guide – Student Task Manager

## 1. Starting the program

Open a terminal in the project folder and run:

```bash
python main.py
```

(On some systems use `python3 main.py`.) The main menu appears:

```
=== Student Task Manager ===
1. Add task
2. Show tasks
3. Complete task
4. Delete task
5. Exit
```

Type the number of an option and press Enter.

## 2. Adding a task

Choose `1` and type a title, for example `Prepare for viva`. The program assigns a unique id and saves the task. If you press Enter without typing anything (or type only spaces), the task is rejected with `Error: Task title cannot be empty.`

## 3. Showing tasks

Choose `2`. Each task is shown on one line:

```
[ ] 1. Prepare for viva
[x] 2. Submit lab report
```

`[ ]` means pending and `[x]` means completed.

## 4. Completing a task

Choose `3` and enter the task id. Possible messages:

- `Completed: <title>` – success
- `Error: Task 7 not found.` – no task has that id
- `Error: Task 2 is already completed.`
- `Error: please enter a valid numeric task id.` – you typed letters or left it blank

## 5. Deleting a task

Choose `4` and enter the task id. A deleted task is removed permanently. Invalid or unknown ids show an error and nothing is deleted.

## 6. Exiting

Choose `5`. All changes are saved automatically after each action.

## 7. Where is my data stored?

Tasks are stored in `tasks.json` in the folder where you run the program. Delete that file to start with an empty list. The file is ignored by Git, so it is never uploaded to GitHub.

## 8. Troubleshooting

| Problem | Fix |
|---------|-----|
| `python` not recognised | Install Python 3 and tick "Add to PATH", or try `python3` |
| `ModuleNotFoundError: task_manager` | Run the program from the project root folder |
| Tasks disappeared | Check that you are in the same folder as before (`tasks.json` is per folder) |
