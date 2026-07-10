"""
Assignment: 3
Description: Create a program that takes user input and appends it 
             to an existing text file without overwriting it.

Approach:
1. Prompt the user for the text they want to add.
2. Use the 'open()' function with 'a' (append mode) to open the file.
3. Write the user's input to the file (adding a newline character is recommended).
4. Inform the user that the operation was successful.
"""

def append_to_file(filename):
    user_text = input("Enter the text you want to append: ")
    
    try:
        # 'a' mode creates the file if it doesn't exist, or appends if it does
        with open(filename, 'a') as file:
            file.write(user_text + "\n")
            print(f"Successfully appended to '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
append_to_file("sample.txt")