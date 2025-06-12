#Helper functions
tasks = []

def add_task(task): 
    """
    This function adds a task to the to-do list.
    In case of entering duplicates, the user is prompted for confirmation before adding it.
    This function is case-sensitive. Tasks entered with different cases will be treated as different tasks.
    """
    if task not in tasks:
        tasks.append(task)
        print(f"\"{task}\" added to the list!")
    
    else:
        #Check if user enters valid choice
        while True:
            try:
                YesOrNo = str(input(f"{task} already exists in the to-do list. Are you sure you want to add it again (Yes/No)? "))
            
                #If choice is valid datatype :
                if YesOrNo.lower() in ["yes", "no"]:
                
                    #If user enters yes, i.e., wants to add the task :
                    if YesOrNo.lower() == "yes":
                        tasks.append(task)
                        print(f"\"{task}\" added to the list!")
                        return
                
                    #If user enters no, i.e., does not want to add the task :
                    else:
                        return
            
                #If user choice is not a yes/no :
                else:
                    print("Oops! Invalid input entered. Please enter Yes/No.\n")

            #If user choice is an invalid datatype :
            except (ValueError):
                print("Oops! Invalid input entered. Please enter Yes/No.\n")


def remove_task(task):
    """
    This function removes a task from the to-do list.
    Only tasks that are already present in the to-do list are to be removed.
    In case the task does not exist already, it raises an error.
    This function is case-sensitive.
    If a task is entered that is of different case than th eone in the list, it cannot be removed. 
    In case of duplicates, the function removes the most recently added task of the task.
    """
    #Check and remove task only if it is present already in the list.
    try:
        tasks.remove(task)
        print(f"\"{task}\" removed from the list!")

    except (ValueError):
        print(f"Oops! Since {task} is not present in the list, you cannot remove it. :(")


def view_all_tasks():
    """
    This function shows all tasks that are currently present in the to-do list.
    """
    for task in tasks:
        print(f"[ ] {task}")


def get_choice(prompt):
    """
    This function gets the user's choice on what action they'd like to perform
    next in the to-do list (add a task/remove a task/view current tasks/exit).
    """
    while True:
        try:
            choice = int(input(prompt))
            if choice not in [1, 2, 3, 4]:
                print("Oops! Invalid input. Please enter a valid choice - (1/2/3/4).")
            else:
                return choice
            
        except (ValueError):
            print("Oops! Invalid input. Please enter a valid choice - (1/2/3/4).")