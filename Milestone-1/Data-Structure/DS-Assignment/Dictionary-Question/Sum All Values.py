"""
Description: 
Extracts all values from a dictionary using the '.values()' 
method and calculates their total sum using the built-in 'sum()' function.
"""

my_dict = {'a': 100, 'b': 200, 'c': 300}

total = sum(my_dict.values())

print(f"The sum of all values in the dictionary is: {total}")