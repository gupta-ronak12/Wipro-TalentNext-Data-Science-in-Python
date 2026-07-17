"""
Description: 
Uses a dictionary comprehension to generate a dictionary where 
each key 'x' (from 1 to 15) maps to its square 'x*x'.
"""

squares = {x: x**2 for x in range(1, 16)}

print("Dictionary of squares (1-15):")
print(squares)