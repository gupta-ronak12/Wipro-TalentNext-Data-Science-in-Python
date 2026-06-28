"""
Assignment
Description: Determine if an input number is odd or even.

Concepts Used:
- Modulo Operator (%): Used to find the remainder of a division.
- Conditional Statements (if, else)
- User Input (input())
- Data Type Casting (int())

"""

num = int(input("Enter a number: "))

if num % 2 == 0:            # We use the modulo operator (%). If a number divided by 2 has a remainder of 0, it is even. Otherwise, it is odd.
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")