"""
Description: 
Prompts the user for a value and uses the 'remove()' method 
to delete the first instance of that value found in the list.
"""

my_list = [10, 20, 30, 20, 40]

target = int(input("Enter the value to remove: "))

if target in my_list:
    my_list.remove(target)
    print("List after removal:", my_list)
else:
    print("Value not found in the list.")