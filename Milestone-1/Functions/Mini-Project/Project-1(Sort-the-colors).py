"""
Project: Functions
Description: Sort a hyphen-separated sequence of colors alphabetically.

Approach:
1. Accept a hyphen-separated string from the user.
2. Use the split('-') method to convert the string into a list of individual colors.
3. Use the sort() method to alphabetize the list.
4. Use the join('-') method to combine the sorted list back into a single 
   hyphen-separated string.
5. Print the final result.
"""

def sort_colors(color_sequence):
    
    color_list = color_sequence.split('-')
    
    color_list.sort()
    

    return '-'.join(color_list)        # Join list back to string

user_input = input("Enter hyphen-separated colors: ")

result = sort_colors(user_input)
print(f"Sorted output: {result}")