import helper_todo_list as hlp

#Main body of to-do list.

#Informing user what this is, and their options.
print("\n===================================================")
print("Welcome to your To-Do List!")
print("===================================================")
print("\nIn order to : ")
print("     View tasks, enter 1.")
print("     Add a task, enter 2.")
print("     Remove a task, enter 3.")
print("     Exit, enter 4.")

#Loop to perfrom tasks until user exits.
while True:
    #Getting user input on what they'd like to do.
    choice = hlp.get_choice("\nEnter your choice (1/2/3/4) : ")

    #Performing the task specified by the user.
    if choice == 1:
        hlp.view_all_tasks()

    elif choice == 2:
        task = input("Enter the task you'd like to add : ")
        hlp.add_task(task)

    elif choice == 3:
        task = input("Enter the task you'd like to remove : ")
        hlp.remove_task(task)

    else:
        break