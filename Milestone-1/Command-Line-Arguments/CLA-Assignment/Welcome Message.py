"""
Assignment
Description: Display the script name and a user-provided welcome message.

Approach:
1. Use 'sys.argv[0]' to get the filename.
2. Use 'sys.argv[1:]' to capture the entire welcome message, even if it has spaces.
3. Join the arguments into a single string.
4. Print the filename and the joined message.
"""

import sys

if len(sys.argv) > 1:
    filename = sys.argv[0]
    message = " ".join(sys.argv[1:]) 
    print(f"File Name: {filename}")
    print(f"Message: {message}")
else:
    print("Please provide a welcome message as an argument.")