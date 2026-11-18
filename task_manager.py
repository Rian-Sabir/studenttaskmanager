tasks = []
next_id = 1


def add_task(title):
    global next_id

    if not title.strip():
        print("Error: Task title cannot be empty.")
        return
    title = title.strip()

    task = {
        "id": next_id,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    next_id += 1

    print("Task added successfully!")


def display_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"

        print(f"ID: {task['id']}")
        print(f"Task: {task['title']}")
        print(f"Status: {status}")
        print("-" * 30)


def main():
    while True:
        print("\n===== STUDENT TASK MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)

        elif choice == "2":
            display_tasks()

        elif choice == "3":
            print("Exiting application.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()