"""
Assignment: 1
Description: Create a function that calculates the sum of all elements in a list.

Approach:
1. Define a function that accepts a list as an argument.
2. Initialize a variable (e.g., 'total') to 0.
3. Use a 'for' loop to iterate through each number in the list.
4. Add each number to the 'total' variable.
5. Return the final 'total'.
"""

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

sample_list = [8, 2, 3, 0, 7]
result = sum_of_list(sample_list)

print(f"Sample List: {sample_list}")
print(f"Expected Output: {result}")