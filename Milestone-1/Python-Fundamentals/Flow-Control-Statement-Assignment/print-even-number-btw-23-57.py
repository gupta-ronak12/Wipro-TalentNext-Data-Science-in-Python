"""
Assignment
Description: Print all even numbers in the range 23 to 57 (inclusive).

Concepts Used:
- For Loop: Using range() to iterate through the numbers.
- Conditional Statement (if): To check if a number is divisible by 2.
- Modulo Operator (%): To verify parity.

"""

for i in range(23, 58):       # The range(23, 58) covers 23 up to 57.
    
    if i % 2 == 0:            # Check if the number is even
        print(i)