#Question: Write a program to accept the file name to be opened from the user; if the file exists, print the contents of the file in title case or else handle the exception and print an error message.
"""
Description: 
Prompts the user for a filename, attempts to open and read it, 
and prints the content in Title Case. Handles 'FileNotFoundError' 
if the file is not found.
"""

filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\n--- File Content in Title Case ---")
        print(content.title())
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")