"""
Assignment: 1
Description: Create a program that reads and prints the full content 
             of a text file.

Approach:
1. Specify the filename or get it from the user.
2. Use the 'open()' function with 'r' (read mode) to access the file.
3. Use the '.read()' method to load the entire content into a string.
4. Print the content to the console.
5. Ensure the file is closed automatically using the 'with' statement.
"""

def display_file_content(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("--- File Content ---")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage:
# Assuming a file named 'sample.txt' exists in the same directory
file_name = "sample.txt"
display_file_content(file_name)