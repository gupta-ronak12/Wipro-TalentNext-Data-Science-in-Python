"""
Description: 
Creates a set of items and removes a specified element using the 
'remove()' or 'discard()' method.
"""

my_set = {10, 20, 30, 40, 50}
item_to_remove = 30

# Using discard() to prevent KeyError if the item doesn't exist
my_set.discard(item_to_remove)

print("Set after removal:", my_set)