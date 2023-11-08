# Simple example for logical error :

numbers = [1, 2, 3, 4, 5]
def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total -= number  # This line contains a semantic error (subtracting instead of adding)
    return total

result = calculate_sum(numbers)
print(f"The sum of numbers is: {result}")  # This will produce an incorrect result



