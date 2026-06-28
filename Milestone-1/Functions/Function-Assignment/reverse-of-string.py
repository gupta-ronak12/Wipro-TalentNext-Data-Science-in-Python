"""
Assignment
Description: Create a function that reverses a given string.

Approach:
1. Define a function that accepts a string as an argument.
2. Use Python's slicing feature [::-1] to reverse the string.
3. Return the reversed string.
"""

def reverse_string(s):
    return s[::-1]

sample_str = "1234abcd"
result = reverse_string(sample_str)

print(f"Sample String: {sample_str}")
print(f"Expected Output: {result}")