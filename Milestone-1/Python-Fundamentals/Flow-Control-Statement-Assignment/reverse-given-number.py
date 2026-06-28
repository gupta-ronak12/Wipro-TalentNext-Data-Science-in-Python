"""
Assignment
Description: Reverse the digits of a given integer.

Concepts Used:
- While Loop: To process digits until the number is exhausted.
- Modulo Operator (%): To extract the last digit.
- Integer Division (//): To remove the last digit.
- Mathematical Reversal: Building the new number by multiplying the current
  result by 10 and adding the extracted digit.
"""

num = int(input("Enter a number: "))
temp = num
reverse_num = 0

while temp > 0:
    digit = temp % 10
    reverse_num = (reverse_num * 10) + digit
    temp //= 10

print(f"Original: {num}")
print(f"Reversed: {reverse_num}")