from datetime import datetime, date

today = date.today()

tasks = []

categories = {
    1: "Assignments",
    2: "Projects",
    3: "Examinations",
    4: "Activities",
    5: "Meetings"
}

priorities = {
    1: "Low",
    2: "Medium",
    3: "High"
} 

statuses = {
    1: "Pending",
    2: "In Progress",
    3: "Completed"
}

def add_task():
    title = input("Task title: ")

    while True:
        deadline = input("Deadline (MM/DD/YYYY): ")

        try:
            deadline_date = datetime.strptime(
                deadline, "%m/%d/%Y"
            ).date()

            if deadline_date.year not in (2026, 2027):
                print("Invalid year! Only 2026 or 2027 is allowed.")
                continue

            if deadline_date.strftime("%m/%d/%Y") != deadline:
                print("Invalid format! Please use MM/DD/YYYY.")
                continue

            break

        except ValueError:
            print(
                "Invalid date! Please use a valid MM/DD/YYYY "
                "with a valid month (1-12), day, and year (2026 or 2027)."
            )

    while True:
        time = input("Time (HH:MM AM/PM): ")

        try:
            valid_time = datetime.strptime(time, "%I:%M %p")
            time = valid_time.strftime("%I:%M %p")
            break

        except ValueError:
            print("Invalid time! Please use the 12-hour format (e.g., 09:30 AM or 02:45 PM).")

    print("Categories:", categories)

    try:
        category_choice = int(input("Choose category: "))
        category = categories.get(category_choice)

        if category is None:
            print("Invalid category!")
            return

    except ValueError:
        print("Invalid category!")
        return

    print("Priorities:", priorities)

    try:
        priority_choice = int(input("Choose priority: "))
        priority = priorities.get(priority_choice)

        if priority is None:
            print("Invalid priority!")
            return

    except ValueError:
        print("Invalid priority!")
        return

    tasks.append({
        "title": title,
        "deadline": deadline,
        "time": time,
        "category": category,
        "priority": priority,
        "status": "Pending"
    })

    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, 1):
        deadline = datetime.strptime(
            task["deadline"], "%m/%d/%Y"
        ).date()

        if task["status"] == "Completed":
            print(
                i,
                task["title"],
                "-",
                task["deadline"],
                "-",
                task["time"],
                "-",
                task["status"]
            )
        else:
            if deadline < today:
                deadline_status = "OVERDUE"
            elif deadline == today:
                deadline_status = "DUE TODAY"
            else:
                deadline_status = "Upcoming"

            print(
                i,
                task["title"],
                "-",
                task["deadline"],
                "-",
                task["time"],
                "-",
                deadline_status,
                "-",
                task["priority"],
                "-",
                task["status"]
            )

def mark_as_done():
    view_tasks()

    if tasks:
        try:
            num = int(input("Task number to mark as done: "))

            if 1 <= num <= len(tasks):
                tasks[num - 1]["status"] = "Completed"
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid task number.")

def delete_task():
    view_tasks()

    if tasks:
        try:
            num = int(input("Task number to delete: "))

            deleted_task = tasks[num - 1]
            tasks[:] = [
                task for i, task in enumerate(tasks, 1)
                if i != num
            ]
            print("Deleted:", deleted_task["title"])
            

        except ValueError:
            print("Please enter a valid task number.")

def update_task():
    view_tasks()

    if tasks:
        try:
            num = int(input("Task number to update: "))

            if not 1 <= num <= len(tasks):
                print("Invalid task number.")
                return

            task = tasks[num - 1]

            print(
                "\nLeave blank if you don't want "
                "to change the information."
            )

            title = input("New task title: ")
            if title:
                task["title"] = title

            while True:
                deadline = input("New deadline (MM/DD/YYYY): ")

                if not deadline:
                    break

                try:
                    deadline_date = datetime.strptime(
                        deadline, "%m/%d/%Y"
                    ).date()

                    if deadline_date.year not in (2026, 2027):
                        print("Invalid year! Only 2026 or 2027 is allowed.")
                        continue

                    if deadline_date.strftime("%m/%d/%Y") != deadline:
                        print("Invalid format! Please use MM/DD/YYYY.")
                        continue

                    task["deadline"] = deadline
                    break

                except ValueError:
                    print("Invalid date! Please use MM/DD/YYYY.")

            while True:
                time = input("New time (HH:MM AM/PM): ")

                if not time:
                    break

                try:
                    valid_time = datetime.strptime(time, "%I:%M %p")
                    task["time"] = valid_time.strftime("%I:%M %p")
                    break

                except ValueError:
                    print("Invalid time! Use the 12-hour format (e.g., 09:30 AM or 02:45 PM).")

            print("Categories:", categories)
            category = input("Choose new category: ")

            if category:
                try:
                    category_choice = int(category)

                    if category_choice in categories:
                        task["category"] = categories[category_choice]
                    else:
                        print("Invalid category. Keeping the previous value.")

                except ValueError:
                    print("Invalid category. Keeping the previous value.")

            print("Priorities:", priorities)
            priority = input("Choose new priority: ")

            if priority:
                try:
                    priority_choice = int(priority)

                    if priority_choice in priorities:
                        task["priority"] = priorities[priority_choice]
                    else:
                        print("Invalid priority. Keeping the previous value.")

                except ValueError:
                    print("Invalid priority. Keeping the previous value.")

            print("Statuses:", statuses)
            status = input("Choose new status: ")

            if status:
                try:
                    status_choice = int(status)

                    if status_choice in statuses:
                        task["status"] = statuses[status_choice]
                    else:
                        print("Invalid status. Keeping the previous value.")

                except ValueError:
                    print("Invalid status. Keeping the previous value.")

            print("Task updated!")

        except ValueError:
            print("Please enter a valid task number.")

def task_summary():
    total = len(tasks)

    completed = sum(
        task["status"] == "Completed"
        for task in tasks
    )

    rate = (completed / total * 100) if total else 0.0

    print("Total Tasks:", total)
    print("Completed:", completed)
    print("Completion Rate:", round(rate, 2), "%")

def main():
    while True:
        print("\n====== TASK-TRACK CAMPUS MANAGEMENT SYSTEM ======")
        print("\n============ Console Based Tracker ==============")
        print("\n=================================================")

        print("1. Add Task")
        print("2. View Tasks")
        print("3. Task Summary")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Mark as Done")
        print("7. Exit")

        print("\n=================================================")

        try:
            choice = int(input("Choose: "))

            if choice == 1:
                add_task()

            elif choice == 2:
                view_tasks()

            elif choice == 3:
                task_summary()

            elif choice == 4:
                update_task()

            elif choice == 5:
                delete_task()

            elif choice == 6:
                mark_as_done()

            elif choice == 7:
                print("Thank you!")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Invalid input! Please enter a number from 1 to 7.")

main()