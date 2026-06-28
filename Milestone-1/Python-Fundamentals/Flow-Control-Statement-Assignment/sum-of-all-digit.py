"""
Assignment
Description: Calculate the sum of all digits in an integer.

Concepts Used:
- While Loop: To process digits until the number becomes 0.
- Modulo Operator (%): To extract the last digit (num % 10).
- Integer Division (//): To remove the last digit (num // 10).
"""

num = int(input("Enter a number: "))
temp = num
total_sum = 0

while temp > 0:
    digit = temp % 10
    total_sum += digit
    temp //= 10        

print(f"The sum of the digits of {num} is {total_sum}")