"""
Assignment: 5
Description: Create a program that identifies and prints the longest word 
             found in a text file.

Approach:
1. Open the file in 'r' (read mode).
2. Read the entire content or iterate line by line.
3. Split the text into individual words using 'split()'.
4. Use the 'max()' function with the 'key=len' argument to find the longest word.
5. Display the longest word to the user.
"""

def find_longest_word(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            
            if not words:
                print("The file is empty.")
                return

            longest_word = max(words, key=len)
            print(f"The longest word in '{filename}' is: {longest_word}")
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage:
find_longest_word("sample.txt")