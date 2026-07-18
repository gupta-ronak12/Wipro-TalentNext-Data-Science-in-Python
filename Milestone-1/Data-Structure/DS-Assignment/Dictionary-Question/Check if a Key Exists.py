"""
Description: 
Checks for the presence of a specific key in a dictionary 
using the 'in' operator and prints an appropriate message.
"""

my_dict = {'a': 1, 'b': 2, 'c': 5}
key_to_check = 'b'

if key_to_check in my_dict:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist.")