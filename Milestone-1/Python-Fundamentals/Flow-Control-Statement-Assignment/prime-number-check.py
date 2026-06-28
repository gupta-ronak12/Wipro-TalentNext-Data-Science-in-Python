"""
Assignment
Description: Determine if a user-provided number is a prime number.

Concepts Used:
- For Loop: To check for divisors.
- Conditional Statements: if, else, and flag variables.
- Modulo Operator (%): To check divisibility.

"""

num = int(input("Enter a number: "))

if num <= 1:       # A prime number must be greater than 1
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    
    for i in range(2, num):     # We loop from 2 up to num - 1 as num is not included in the range.
        if num % i == 0:
            is_prime = False
            break               # Exit the loop as soon as we find a divisor
    
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")