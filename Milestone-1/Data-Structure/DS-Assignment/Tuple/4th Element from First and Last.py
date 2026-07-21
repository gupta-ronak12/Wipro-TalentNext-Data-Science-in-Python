"""
Description: 
Creates a tuple with sufficient elements, then accesses and prints 
the 4th element from the beginning (index 3) and the 4th element 
from the end (negative index -4).
"""

my_tuple = (10, 20, 30, 40, 50, 60, 70, 80)

# 4th element from the first (index 3)
fourth_from_first = my_tuple[3]

# 4th element from the last (index -4)
fourth_from_last = my_tuple[-4]

print(f"4th element from the first: {fourth_from_first}")
print(f"4th element from the last: {fourth_from_last}")