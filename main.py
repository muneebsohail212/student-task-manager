"""Console interface for the Student Task Manager."""

from task_manager import (
    add_task,
    complete_task,
    delete_task,
    format_task,
    load_tasks,
    save_tasks,
)


def show_menu():
    print("\n=== Student Task Manager ===")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def handle_add(tasks):
    title = input("Task title: ")
    try:
        task = add_task(tasks, title)
    except ValueError as error:
        print(f"Error: {error}")
        return
    save_tasks(tasks)
    print(f"Added task {task['id']}: {task['title']}")


def handle_show(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        print(format_task(task))


def handle_complete(tasks):
    raw_id = input("Task id to complete: ").strip()
    if not raw_id.isdigit():
        print("Error: please enter a valid numeric task id.")
        return
    try:
        task = complete_task(tasks, int(raw_id))
    except ValueError as error:
        print(f"Error: {error}")
        return
    save_tasks(tasks)
    print(f"Completed: {task['title']}")


def handle_delete(tasks):
    task_id = int(input("Task id to delete: "))
    task = delete_task(tasks, task_id)
    if task is None:
        print("Task not found.")
    else:
        save_tasks(tasks)
        print(f"Deleted: {task['title']}")


def main():
    tasks = load_tasks()
    actions = {
        "1": handle_add,
        "2": handle_show,
        "3": handle_complete,
        "4": handle_delete,
    }
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid option, please choose 1-5.")
        else:
            action(tasks)


if __name__ == "__main__":
    main()
