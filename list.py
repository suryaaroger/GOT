# To-Do List Manager

# Initialize an empty list to store tasks
tasks = []

def view_tasks():
    print("To-Do List:")
    if not tasks:
        print("No tasks yet.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def mark_task():
    view_tasks()
    if tasks:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            print(f"Marked task '{tasks[index]}' as done.")
            tasks.pop(index)
        else:
            print("Invalid task number.")
    else:
        print("No tasks to mark.")

def remove_task():
    view_tasks()
    if tasks:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            print(f"Removed task '{tasks[index]}' from list.")
            tasks.pop(index)
        else:
            print("Invalid task number.")
    else:
        print("No tasks to remove.")

# Main loop to display menu and handle user input
while True:
    print("\nMenu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_task()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
        