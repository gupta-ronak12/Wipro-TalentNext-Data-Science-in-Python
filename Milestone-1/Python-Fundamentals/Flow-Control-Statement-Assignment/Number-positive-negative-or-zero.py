"""
Assignment
Description: Check if a number is positive, negative, or zero.

Concepts Used:
- Conditional Statements (if, elif, else)
- User Input (input())
- Data Type Casting (int())

"""

num = int(input("Enter a number: "))


if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print("The number is Zero")