"""
Assignment
Description: Print all prime numbers in the range 10 to 99 (inclusive).

Concepts Used:
- Nested Loops: An outer loop for the range and an inner loop for checking divisors.
- Conditional Statements: To verify if a number is prime.
- Modulo Operator (%): To check divisibility.
"""

for num in range(10, 100):
    is_prime = True
    
    for i in range(2, int(num**0.5) + 1):      # The inner loop checks for divisors from 2 up to the square root of the number
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=" ")

print()