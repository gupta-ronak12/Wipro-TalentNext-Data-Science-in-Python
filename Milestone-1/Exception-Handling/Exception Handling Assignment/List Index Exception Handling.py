"""
Description: 
Declares a list of 10 integers. Prompts the user for an index, 
checks if the element at that index is positive or negative, 
and handles invalid index or non-integer inputs using exception handling.
"""

# Declare a list with 10 integers
numbers = [15, -3, 0, 42, -10, 7, -8, 22, -1, 5]

try:
    # Ask user for an index
    index = int(input("Enter an index between 0 and 9: "))
    
    # Access the list and check if positive or negative
    value = numbers[index]
    
    if value >= 0:
        print(f"The number at index {index} is {value}, which is positive.")
    else:
        print(f"The number at index {index} is {value}, which is negative.")

# Handle invalid index or non-integer input
except IndexError:
    print("Error: Index out of range. Please enter a number between 0 and 9.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")