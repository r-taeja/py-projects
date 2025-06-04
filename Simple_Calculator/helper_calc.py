#Functions required for the main program
def add(x, y):
    """
    This is a function to add two numbers.
    """
    ans = x + y
    return ans

def subtract(x, y):
    """
    This is a function to subtract two numbers.
    """
    ans = x - y
    return ans

def multiply(x, y):
    """
    This is a function to multiply two numbers.
    """
    ans = x * y
    return ans

def divide(x, y):
    """
    This is a function to divide two numbers.
    """
    ans  = x / y
    return ans

def get_number(prompt):
    """
    This is a function to get a valid number from the user.
    """
    while True:
        try:
            return float(input(prompt))
        except (ValueError):
            print("Oops! That was not a number.\n")

def get_operation():
    """
    This is a function to get the operation (1/2/3/4) from the user.
    """
    while True:
        try:
            operation = int(input("Enter the number (1/2/3/4) from the above list : "))
            if operation not in [1, 2, 3, 4]:
                print("Oops! Invalid input entered. Please enter 1/2/3/4.")
                continue
            else:
                print(f"\nYou have chosen operation number {operation}.")
                return operation
        except (ValueError):
            print("Oops! Invalid input entered. Please enter 1/2/3/4.")