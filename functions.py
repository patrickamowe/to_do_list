import json
import os
from datetime import datetime

# the path to the json file where the tasks will be stored
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'tasks.json')


def read_tasks(filename=file_path):
    """
    Read tasks from the specified JSON file.

    Parameters:
    filename (str): The path to the JSON file containing tasks.

    Returns:
    list: A list of tasks read from the JSON file.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            if content:
                tasks = json.loads(content)
            else:
                tasks = []
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks


def write_tasks(tasks, filename=file_path):
    """
    Write tasks to the specified JSON file.

    Parameters:
    tasks (list): A list of tasks to write to the JSON file.
    filename (str): The path to the JSON file to write tasks to.
    """
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task():
    """
    Add a new task to the tasks list and write it to the JSON file.

    Prompts the user for task description and due date, sets the status to 'pending',
    and adds the new task to the tasks list. The updated tasks list is then written
    back to the JSON file.
    """
    current_date = datetime.now()

    tasks = read_tasks()
    description = input("Task description: ")
    created_date = current_date.strftime("%B %d, %Y")
    due_date = input("Due date: ")
    status = "pending"
    task = {'description': description, 'created_date': created_date, 'due_date': due_date, 'status': status}
    tasks.append(task)
    write_tasks(tasks)
    print("Task added successfully!")


def update_task():
    """
    Update the description of an existing task.
    """
    tasks = read_tasks()
    description = input("Enter the description of the task you want to update: ")
    updated_description = input("Enter the updated description: ")
    found = False
    for task in tasks:
        if task['description'].lower() == description.lower():
            task['description'] = updated_description
            found = True
            break
    if found:
        write_tasks(tasks)
        print("Task updated successfully!")
    else:
        print("Task not found.")


def view_tasks():
    """
    Display all the tasks in the task list.
    """
    tasks = read_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print("-" * 20)
        print(f"Description: {task['description']}")
        print(f"Created Date: {task['created_date']}")
        print(f"Due Date: {task['due_date']}")
        print(f"Status: {task['status']}")
        print("-" * 20)


def delete_task():
    """
    Delete a task from the task list.
    """
    tasks = read_tasks()
    description = input("Enter the description of the task you want to delete: ")
    updated_tasks = [task for task in tasks if task['description'] != description]
    if len(updated_tasks) < len(tasks):
        write_tasks(updated_tasks)
        print("Task deleted successfully!")
    else:
        print("Task not found.")
