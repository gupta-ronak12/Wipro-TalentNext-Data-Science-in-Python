"""
Assignment: 6
Description: Create a program that prompts the user for a word and 
             counts how many times it appears in a text file.

Approach:
1. Open the file in 'r' (read mode).
2. Read the content and convert it to a common case (e.g., lowercase) 
   to ensure the count is case-insensitive.
3. Use the 'split()' method to break the text into a list of words.
4. Prompt the user for the word they want to count.
5. Use the 'count()' method on the list to find the frequency.
6. Display the result.
"""

def count_word_frequency(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().lower()  # Make search case-insensitive
            words = content.split()
            
            search_word = input("Enter the word you want to count: ").lower()
            frequency = words.count(search_word)
            
            print(f"The word '{search_word}' appears {frequency} times in '{filename}'.")
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage:
count_word_frequency("sample.txt")