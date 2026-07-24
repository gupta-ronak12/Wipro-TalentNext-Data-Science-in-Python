"""
Description: 
Uses the 'index()' method to find the position (index) 
of a specific element within a tuple.
"""

my_tuple = ('apple', 'banana', 'cherry', 'date')
item = 'cherry'

try:
    index = my_tuple.index(item)
    print(f"The index of '{item}' in the tuple is: {index}")
except ValueError:
    print(f"'{item}' is not found in the tuple.")