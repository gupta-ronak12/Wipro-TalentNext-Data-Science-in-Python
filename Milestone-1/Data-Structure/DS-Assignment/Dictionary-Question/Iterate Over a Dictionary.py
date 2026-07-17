"""
Description: 
Demonstrates three ways to iterate over a dictionary: accessing 
keys only, values only, and both simultaneously using the '.items()' method.
"""

data = {'Name': 'Alice', 'Age': 25, 'City': 'New York'}

print("Keys:")
for key in data:
    print(key)

print("\nValues:")
for value in data.values():
    print(value)

print("\nKeys and Values:")
for key, value in data.items():
    print(f"{key}: {value}")