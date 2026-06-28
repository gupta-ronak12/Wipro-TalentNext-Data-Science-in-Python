"""
Assignment
Description: Check if an integer is a palindrome (reads the same forward and backward).

Concepts Used:
- While Loop: To process the number.
- Modulo Operator (%): To extract digits.
- Integer Division (//): To reduce the number.
- Variable Comparison: Comparing the original number with its reversed form.
"""

num = int(input("Enter a number: "))
original_num = num
reversed_num = 0

temp = num
while temp > 0:
    digit = temp % 10
    reversed_num = (reversed_num * 10) + digit
    temp //= 10


if original_num == reversed_num:                 # Check if original is equal to reversed
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")