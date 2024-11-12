# To-do-list
tasks = []

def show_tasks():
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['name']} (Added on: {task['date']})")

while True:
    action = input("Choose an action: [add, remove, view, quit]: ").strip().lower()
    if action == "add":
        task_name = input("Enter a task: ").strip()
        task_date = input("Enter the date for this task (DD-MM-YYYY): ").strip()
        
        task = {
            "name": task_name,
            "date": task_date
        }
        
        tasks.append(task)
    elif action == "remove":
        show_tasks()
        task_num = int(input("Enter the task number to remove: "))
        if 0 < task_num <= len(tasks):
            tasks.pop(task_num - 1)
        else:
            print("Invalid task number.")
    elif action == "view":
        show_tasks()
    elif action == "quit":
        break
    else:
        print("Invalid action.")
