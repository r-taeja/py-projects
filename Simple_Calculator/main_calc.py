import helper_calc as hc

#Main body of the program
print("======================================================================")
print("WELCOME TO ROHIT'S CALCULATOR!\n\nGiven two numbers, this calculator can do the following :")
print("1. Add the given two numbers,")
print("2. Subtract the given two numbers,")
print("3. Multiply the given two numbers,")
print("4. Divide the given two numbers.")
print("======================================================================\n")

#Getting the numbers from the user
num1 = hc.get_number("Enter the first number : ")
num2 = hc.get_number("Enter the second number : ")
print(f"\nThe first number given is {num1} and the second number given is {num2}.")
print("======================================================================\n")

#getting the operation from the user
print("From the following list, choose the operation you'd like to perform :")
print("1. Add the two numbers,\n" \
"2. Subtract the two numbers,\n" \
"3. Multiply the two bnumbers,\n" \
"4. Divide the two numbers.\n")
operation = hc.get_operation()
print("======================================================================\n")

#PPerforming the computation and showing results
if operation == 1:
    print(f"{num1} + {num2} = {hc.add(num1, num2)}\n")

elif operation == 2:
    print(f"{num1} - {num2} = {hc.subtract(num1, num2)}\n")

elif operation == 3:
    print(f"{num1} * {num2} = {hc.multiply(num1, num2)}\n")

elif operation == 4:
    try:
        print(f"{num1} / {num2} = {hc.divide(num1, num2)}\n")
    except (ZeroDivisionError):
        print(f"Oops! You cannot divide a number by 0. :(\n")
        
print("======================================================================\n")