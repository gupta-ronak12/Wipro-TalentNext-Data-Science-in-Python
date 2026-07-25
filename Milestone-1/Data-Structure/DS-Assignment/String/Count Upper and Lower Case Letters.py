"""
Description: 
Accepts a string from the user and counts the total number of 
uppercase and lowercase letters using built-in string methods.
"""

sample_str = input("Enter a string: ")

upper_count = 0
lower_count = 0

for char in sample_str:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print(f"No. of Upper case characters: {upper_count}")
print(f"No. of Lower case characters: {lower_count}")