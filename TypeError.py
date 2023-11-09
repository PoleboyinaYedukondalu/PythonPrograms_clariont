# Runtime Errors :- ZeroDivisionError, NameError, TypeError 
# simple example for TypeError :
try:
    number = "5"  # A string
    result = number + 10  # This line will raise a TypeError
except TypeError as e:
    print(f"TypeError: {e}")