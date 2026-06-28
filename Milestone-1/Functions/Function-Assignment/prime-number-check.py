"""
Assignment
Description: Create a function that determines if a given integer is a prime number.

Approach:
1. Define a function that accepts an integer 'n'.
2. Handle base cases: Numbers less than or equal to 1 are not prime.
3. Use a 'for' loop to check for divisibility from 2 up to the square root of 'n'.
4. If 'n' is divisible by any number in this range, it is not prime.
5. If no divisors are found, the number is prime.
"""

import math

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

num = 11
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")