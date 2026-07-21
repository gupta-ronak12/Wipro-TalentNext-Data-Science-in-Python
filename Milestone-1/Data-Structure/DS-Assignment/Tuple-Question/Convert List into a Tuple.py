"""
Description: 
Takes a standard Python list, converts it into a tuple 
using the built-in 'tuple()' constructor, and displays the result.
"""

my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

my_tuple = tuple(my_list)

print("Converted tuple:", my_tuple)
print("Data type:", type(my_tuple))