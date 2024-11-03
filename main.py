from functions import add_task, update_task, view_tasks, delete_task
run = True

while run:
    options = input("""
        type the option you want to perform
        1. Add task
        2. update task
        3. view tasks
        4. Delete task
        5. Exit

        """)

    if options.lower() == "add task":
        add_task()
    elif options.lower() == "update task":
        update_task()
    elif options.lower() == "view tasks":
        view_tasks()
    elif options.lower() == "delete task":
        delete_task()
    else:
        run = False
