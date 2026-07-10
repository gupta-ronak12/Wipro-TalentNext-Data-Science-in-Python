"""
Assignment: 4
Description: Create a program that reads a file and stores its content 
             into a list, where each element represents a line.

Approach:
1. Open the file in 'r' (read mode).
2. Use the 'readlines()' method, which automatically reads all lines 
   and returns them as a list.
3. Alternatively, use a 'for' loop to append each line to a list (useful if 
   you need to strip newline characters).
4. Print the resulting list to verify.
"""

def file_to_list(filename):
    try:
        with open(filename, 'r') as file:
            # Method 1: Using readlines() (includes \n at the end of each string)
            # content_list = file.readlines()
            
            # Method 2: Using a loop to strip \n (cleaner)
            content_list = [line.strip() for line in file]
            
            return content_list
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

# Example usage:
data = file_to_list("sample.txt")
print("Content as a list:")
print(data)