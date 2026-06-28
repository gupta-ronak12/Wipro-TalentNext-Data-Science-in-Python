"""
Module Name: string_analyzer.py
Description: Contains functions to analyze strings for palindromes,vowels, and character frequency.

Approach:
1. is_palindrome: Reverse the string and compare it to the original.
2. count_the_vowels: Iterate through the string and count matches in 'aeiouAEIOU'.
3. frequency_of_letters: Use a dictionary to store and increment counts for each character.
"""

def is_palindrome(name):
    return name == name[::-1]   # Check if string equals its reverse

def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    return count

def frequency_of_letters(name):
    freq = {}
    for char in name:
        if char == " ":      # space 
            continue
        freq[char] = freq.get(char, 0) + 1
    return freq