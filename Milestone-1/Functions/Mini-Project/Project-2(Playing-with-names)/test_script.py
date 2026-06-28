"""
Script: test_script.py
Description: Imports string_analyzer and tests functions with user input.
"""

import string_analyzer

name = input("Enter a name: ")

if string_analyzer.is_palindrome(name):      
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")

vowel_count = string_analyzer.count_the_vowels(name)
print(f"No of vowels: {vowel_count}")


freq = string_analyzer.frequency_of_letters(name)
freq_str = ", ".join([f"{char}-{count}" for char, count in freq.items()])
print(f"Frequency of letters: {freq_str}")