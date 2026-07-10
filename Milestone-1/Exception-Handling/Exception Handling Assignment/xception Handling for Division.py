"""
Assignment: 1
Description: Division with Exception Handling.

Approach:
1. Use 'input()' to get two numbers from the user.
2. Convert them to floats.
3. Place the division operation inside a 'try' block.
4. Use 'except' blocks to catch:
   - 'ZeroDivisionError' (if the second number is 0).
   - 'ValueError' (if input is not a number).
"""

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")