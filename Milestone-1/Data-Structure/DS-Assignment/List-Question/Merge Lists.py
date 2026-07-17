"""
Description: 
Takes two lists and inserts all elements of list1 into the 
beginning of list2 using list slicing or the 'extend()' method 
(or index insertion). Here, we use list addition to prepend.
"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]


result = list1 + list2

print("Combined list:", result)