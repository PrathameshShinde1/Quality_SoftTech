import random
from datetime import datetime

tasks = [
    "Go for Cycling",
    "Eat breakfast",
    "Do study",
    "Go to Class"
]

completed_tasks = {}

def ToDoTask():
    today_tasks = random.sample(tasks, min(3, len(tasks)))
    while True:

        print("\n<========= Welcome to To Do Task =========>")
        choice = input(
            "Enter what you want to do?\n"
            "(View/Task/Add/Mark/Exit): "
        ).lower()

        match choice:

            case "view":
                if not tasks:
                    print("No tasks available.")
                else:
                    print("\n--- Task List ---")
                    for index, task in enumerate(tasks, start=1):
                        if task in completed_tasks:
                            print(
                                f"{index}. {task} ✅ "
                                f"Completed : {completed_tasks[task]}"
                            )
                        else:
                            print(f"{index}. {task} ❌")

            case "task":
                if len(tasks) >= 3:
                    today_tasks = random.sample(tasks, 3)
                else:
                    today_tasks = tasks

                print("\nToday's Tasks:")
                for index, task in enumerate(today_tasks, start=1):
                    print(f"{index}. {task}")

            case "add":
                new_task = input("Enter new task: ")

                if new_task.strip():
                    tasks.append(new_task)
                    print("Task added successfully!")
                else:
                    print("Task cannot be empty.")

            case "mark":
                if not tasks:
                    print("No tasks available.")
                    continue

                print("\nSelect task number to mark as completed:")

                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

                try:
                    task_no = int(input("Enter task number: "))

                    if 1 <= task_no <= len(tasks):
                        task_name = tasks[task_no - 1]
                        complete_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                        completed_tasks[task_name] = complete_time

                        print(f"Task Marked as Complete ✅")
                        print(f"Completed at {complete_time}")
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid number.")

            case "exit":
                print("Thank you for using To Do Task!")
                break

            case _:
                print("Please enter a valid option.")

ToDoTask()