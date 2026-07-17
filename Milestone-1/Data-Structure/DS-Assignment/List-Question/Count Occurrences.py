"""
Description: 
Prompts the user for a number, searches the list for that value, 
and uses the 'count()' method to determine how many times 
it appears in the list.
"""

my_list = [10, 20, 30, 20, 40, 20, 50]


target = int(input("Enter the number to count: "))

count = my_list.count(target)

print(f"The number {target} appears {count} times in the list.")