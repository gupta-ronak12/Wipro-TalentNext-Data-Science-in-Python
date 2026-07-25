"""
Description: 
Checks if a given string reads the same forwards and backwards 
by comparing the string with its reversed version using slicing.
"""

sample_str = input("Enter a string: ")


clean_str = sample_str.replace(" ", "").lower()

if clean_str == clean_str[::-1]:
    print(f"'{sample_str}' is a Palindrome.")
else:
    print(f"'{sample_str}' is not a Palindrome.")