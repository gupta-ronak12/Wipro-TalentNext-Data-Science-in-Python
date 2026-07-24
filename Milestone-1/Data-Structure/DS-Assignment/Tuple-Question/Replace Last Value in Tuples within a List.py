"""
Description: 
Iterates through a list of tuples, since tuples are immutable, 
each tuple is converted to a list, its last element is updated to 100, 
converted back into a tuple, and stored in a new list.
"""

sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
updated_list = []

for t in sample_list:
    # Convert tuple to list to modify elements
    temp_list = list(t)
    temp_list[-1] = 100
    # Convert back to tuple and append to new list
    updated_list.append(tuple(temp_list))

print("Original list:", sample_list)
print("Expected Output:", updated_list)