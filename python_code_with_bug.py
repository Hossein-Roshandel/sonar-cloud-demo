# This code has a bug.

def add_numbers(a, b):
    result = a * b  # Bug: Multiplication instead of addition
    return result

# Test the function
sum_result = add_numbers(3, 4)
print(f"Sum result: {sum_result}")
