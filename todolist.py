# Simple To-Do List
todo_list = []

while True:
    print("\n1. Add Task lets enhance our self ")
    print("2. View Tasks")
    print("3. Exit")
    choice = input("Choose an option  from (1/2/3): ").strip()

    if choice == "1":
        task = input("Enter a task: ").strip()
        if task:  # Ensure the task is not empty
            todo_list.append(task)
            print(f"Task '{task}' added.")
        else:
            print(" oops....Task cannot be empty! Please try again.")
    elif choice == "2":
        if todo_list:  # Check if there are tasks to display
            print("\nYour To-Do List:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks yet!")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")