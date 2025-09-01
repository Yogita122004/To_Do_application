import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    task_name = input("Enter task: ").strip()
    if task_name:
        tasks.append({"task": task_name, "done": False})
        save_tasks(tasks)
        print("✅ Task added successfully!")
    else:
        print("⚠️ Task cannot be empty.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("📂 No tasks found.")
        return
    print("\n📋 Your To-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "✅ Done" if task["done"] else "❌ Not Done"
        print(f"{i}. {task['task']} - {status}")
    print()

# Mark task as done
def mark_task_done(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            choice = int(input("Enter task number to mark as done: "))
            if 1 <= choice <= len(tasks):
                tasks[choice - 1]["done"] = True
                save_tasks(tasks)
                print("✔️ Task marked as done!")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            choice = int(input("Enter task number to delete: "))
            if 1 <= choice <= len(tasks):
                removed = tasks.pop(choice - 1)
                save_tasks(tasks)
                print(f"🗑️ Task '{removed['task']}' deleted.")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

# Main Program
def main():
    tasks = load_tasks()

    while True:
        print("\n--- 📌 TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Exiting... Your tasks are saved.")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
