"""
Assignment
Description: Determine if two non-negative numbers have the same last digit.

Concepts Used:
- Modulo Operator (%): Used with 10 to isolate the last digit.
- Conditional Statements (if, else)
- User Input (input())
- Data Type Casting (int())

"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


if num1 % 10 == num2 % 10:               # Logic: A number % 10 always gives the last digit. We compare the results of both modulo operations.
    print("True")
else:
    print("False")