# simple exammple for ZeroDivisionError(RunTime Error) :

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