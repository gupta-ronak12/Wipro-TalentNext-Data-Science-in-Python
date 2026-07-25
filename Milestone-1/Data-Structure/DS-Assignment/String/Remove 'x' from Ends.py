"""
Description: 
Checks if a string starts or ends with the character 'x'. 
If so, strips 'x' from the beginning and/or end; otherwise, returns the original string.
"""

sample_str = input("Enter a string: ")

result = sample_str

if result.startswith('x'):
    result = result[1:]
if result.endswith('x'):
    result = result[:-1]

print("Output:", result)