"""
Assignment:
Description: Create a function that counts and prints the number of uppercase 
             and lowercase letters in a given string.

Approach:
1. Define a function that accepts a string as an argument.
2. Initialize two counters: 'upper_count' and 'lower_count' at 0.
3. Use a 'for' loop to iterate through each character in the string.
4. Use the .isupper() method to check for uppercase and .islower() for lowercase.
5. Increment the respective counters for each match.
6. Print the results.
"""

def count_case(s):
    upper_count = 0
    lower_count = 0
    
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
            
    print(f"Original String: {s}")
    print(f"No. of Uppercase characters: {upper_count}")
    print(f"No. of Lowercase characters: {lower_count}")

sample_str = "The quick Brown Fox"
count_case(sample_str)