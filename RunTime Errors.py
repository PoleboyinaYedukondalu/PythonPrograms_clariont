# Runtime Errors :- ZeroDivisionError, NameError, TypeError, IndexError 
                    
# simple exammple for ZeroDivisionError :

# Prompt the user to enter values
value1 = int(input("Enter value1: "))
value2 = int(input("Enter value2: "))

#defin the function for calculation with the exception handlimng concept
def calculation(value1, value2):   
    try:
        division = value1 / value2
        print(f"Division of {value1} and {value2} is: {division}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero! Please enter proper input values.")

        # Prompt the user to enter new values
        value1 = int(input("Enter value1: "))
        value2 = int(input("Enter value2: "))

        # Call the function again with the new values
        calculation(value1, value2)
    else:
        print("Done!")

calculation(value1, value2)

# ------------------------------------------------------------------------------------------------
# simple example for NameError :
def NameErr():
    try:
        result = x + 5  # This line will raise a NameError
    except NameError as e:
        print(f"NameError: {e}")
NameErr()

# ------------------------------------------------------------------------------------------------
# simple example for TypeError :
try:
    number = "5"  # A string
    result = number + 10  # This line will raise a TypeError
except TypeError as e:
    print(f"TypeError: {e}")

# -------------------------------------------------------------------------------------------------
# Simple example for IndexError :
try:
    numbers = [1, 2, 3] 
    numbers[3]=4 # This line will raise an IndexError
except IndexError as e:
    print(f"IndexError: {e}")
