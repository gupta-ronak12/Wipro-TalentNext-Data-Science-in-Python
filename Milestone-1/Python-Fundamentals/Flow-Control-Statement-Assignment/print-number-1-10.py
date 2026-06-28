"""
Assignment
Description: Print numbers 1 through 10 in a single row, separated by tabs.

Concepts Used:
- For Loop: Using range() to generate a sequence of numbers.
- Print Function Arguments: Using 'end' to control the termination character.

"""

for i in range(1, 11):   # The range(1, 11) function generates numbers starting from 1 up to (but not including) 11.
    
    print(i, end="\t")  # The 'end="\t"' argument replaces the default newline with a tab space.

print()    # This final print() is best practice to move the cursor to a new line after the loop finishes, ensuring your terminal prompt starts on a fresh line.