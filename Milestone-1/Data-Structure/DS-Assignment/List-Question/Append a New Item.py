"""
Description: 
Creates a list, prompts the user for a new item, appends it 
to the end of the list using the 'append()' method, and 
displays the updated list.
"""

my_list = [10, 20, 30]

new_item = int(input("Enter an integer to append: "))
my_list.append(new_item)

print("Updated list:", my_list)