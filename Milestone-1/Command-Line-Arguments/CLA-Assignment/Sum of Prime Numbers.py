"""
Assignment
Description: Accept 10 numbers via command line and sum the primes.

Approach:
1. Define a helper function to check for primality.
2. Ensure at least 10 numbers are provided via 'sys.argv'.
3. Iterate through the first 10 arguments, convert to int.
4. Check each using the prime helper and add to a total sum.
5. Display the final sum.
"""

import sys

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

if len(sys.argv) >= 11:
    prime_sum = 0
    for i in range(1, 11):
        try:
            num = int(sys.argv[i])
            if is_prime(num):
                prime_sum += num
        except ValueError:
            continue 
    print(f"The sum of prime numbers among the 10 provided is: {prime_sum}")
else:
    print("Please provide exactly 10 numbers as command line arguments.")