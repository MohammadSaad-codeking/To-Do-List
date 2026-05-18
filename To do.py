import json
import os

# File to save tasks
SAVE_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(SAVE_FILE, "w") as f:
        json.dump(tasks, f)

# Show all tasks
def show_tasks(tasks):
    if len(tasks) == 0:
        print("\n  No tasks yet!\n")
        return

    print("\n  Your Tasks:")
    print("  " + "-" * 30)
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "○"
        print(f"  {i + 1}. [{status}] {task['text']}")
    print("  " + "-" * 30)

    done_count = sum(1 for t in tasks if t["done"])
    print(f"  {len(tasks) - done_count} remaining · {done_count} completed\n")

# Add a task
def add_task(tasks):
    text = input("  Enter task: ").strip()
    if text == "":
        print("  Task cannot be empty!")
        return
    tasks.append({"text": text, "done": False})
    save_tasks(tasks)
    print(f"  ✓ Added: '{text}'")

# Complete a task
def complete_task(tasks):
    show_tasks(tasks)
    if len(tasks) == 0:
        return
    try:
        num = int(input("  Enter task number to complete: "))
        if num < 1 or num > len(tasks):
            print("  Invalid number!")
            return
        task = tasks[num - 1]
        task["done"] = not task["done"]
        status = "completed" if task["done"] else "uncompleted"
        save_tasks(tasks)
        print(f"  ✓ Marked '{task['text']}' as {status}")
    except ValueError:
        print("  Please enter a valid number!")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    if len(tasks) == 0:
        return
    try:
        num = int(input("  Enter task number to delete: "))
        if num < 1 or num > len(tasks):
            print("  Invalid number!")
            return
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"  ✓ Deleted: '{removed['text']}'")
    except ValueError:
        print("  Please enter a valid number!")

# Clear all completed tasks
def clear_completed(tasks):
    before = len(tasks)
    tasks[:] = [t for t in tasks if not t["done"]]
    after = len(tasks)
    removed = before - after
    if removed == 0:
        print("  No completed tasks to clear!")
    else:
        save_tasks(tasks)
        print(f"  ✓ Cleared {removed} completed task(s)")

# Main menu
def main():
    tasks = load_tasks()

    print("\n  ================================")
    print("         TO-DO APP")
    print("  ================================")

    while True:
        print("\n  What would you like to do?")
        print("  1. View tasks")
        print("  2. Add task")
        print("  3. Complete task")
        print("  4. Delete task")
        print("  5. Clear completed")
        print("  6. Quit")

        choice = input("\n  Enter choice (1-6): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            clear_completed(tasks)
        elif choice == "6":
            print("\n  Goodbye!\n")
            break
        else:
            print("  Please enter a number between 1 and 6")

# Run the app
main()