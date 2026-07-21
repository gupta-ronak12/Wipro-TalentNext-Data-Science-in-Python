"""
Description: 
Checks if a user-specified element exists inside a tuple 
using the 'in' operator and displays the result.
"""

my_tuple = (5, 10, 15, 20, 25)
element = int(input("Enter an element to search: "))

if element in my_tuple:
    print(f"The element {element} exists in the tuple.")
else:
    print(f"The element {element} does not exist in the tuple.")