"""
Description: 
Extracts the first 2 characters of a string and repeats them 
n times, where n is equal to the length of the string.
"""

sample_str = input("Enter a string (length >= 2): ")

if len(sample_str) >= 2:
    first_two = sample_str[:2]
    n = len(sample_str)
    result = first_two * n
    print("Output:", result)
else:
    print("Error: String length must be at least 2.")