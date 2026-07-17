"""
Description: 
Creates three separate dictionaries and merges them into a single 
new dictionary using the 'update()' method or dictionary unpacking.
"""

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}


new_dict = {}
for d in (dic1, dic2, dic3):
    new_dict.update(d)

print("Concatenated dictionary:", new_dict)