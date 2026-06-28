"""
Assignment
Description: Create a function that calculates the factorial of a number.

Approach:
1. Define a function that accepts a non-negative integer.
2. Handle the base case: if the number is 0 or 1, the factorial is 1.
3. Use a loop to multiply numbers from 1 up to the given number.
4. Return the calculated product.
"""

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = 5
print(f"The factorial of {num} is: {factorial(num)}")