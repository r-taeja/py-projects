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


#Main body of the program
print("======================================================================")
print("WELCOME TO ROHIT'S CALCULATOR!\n\nGiven two numbers, this calculator can do the following :")
print("1. Add the given two numbers,")
print("2. Subtract the given two numbers,")
print("3. Multiply the given two numbers,")
print("4. Divide the given two numbers.")
print("======================================================================\n")

#Getting the numbers from the user
num1 = get_number("Enter the first number : ")
num2 = get_number("Enter the second number : ")
print(f"\nThe first number given is {num1} and the second number given is {num2}.")
print("======================================================================\n")

#getting the operation from the user
print("From the following list, choose the operation you'd like to perform :")
print("1. Add the two numbers,\n" \
"2. Subtract the two numbers,\n" \
"3. Multiply the two bnumbers,\n" \
"4. Divide the two numbers.\n")
operation = get_operation()
print("======================================================================\n")

#PPerforming the computation and showing results
if operation == 1:
    print(f"{num1} + {num2} = {add(num1, num2)}\n")

elif operation == 2:
    print(f"{num1} - {num2} = {subtract(num1, num2)}\n")

elif operation == 3:
    print(f"{num1} * {num2} = {multiply(num1, num2)}\n")

elif operation == 4:
    try:
        print(f"{num1} / {num2} = {divide(num1, num2)}\n")
    except (ZeroDivisionError):
        print(f"Oops! You cannot divide a number by 0. :(\n")
        
print("======================================================================\n")
