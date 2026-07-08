"""
Description: Calculate happiness based on command line arguments.

Approach:
1. Import 'sys' to access command line arguments.
2. The first three arguments (sys.argv[1], [2], [3]) are your 'like' set, 
   'dislike' set, and the input sequence.
3. Split these strings by '-' to get lists of numbers.
4. Convert these to sets for efficient lookups.
5. Iterate through the third sequence:
   - Add 1 to happiness if number is in 'like' set.
   - Subtract 1 from happiness if number is in 'dislike' set.
6. Print the final happiness.
"""

import sys

def calculate_happiness():
    
    if len(sys.argv) < 4:
        print("Usage: python script.py <string1> <string2> <string3>")
        return

  
    like_str = sys.argv[1]
    dislike_str = sys.argv[2]
    sequence_str = sys.argv[3]

    like_set = set(like_str.split('-'))
    dislike_set = set(dislike_str.split('-'))
    sequence = sequence_str.split('-')

    happiness = 0

    for num in sequence:
        if num in like_set:
            happiness += 1
        elif num in dislike_set:
            happiness -= 1
    
    print(f"Final Happiness: {happiness}")

if __name__ == "__main__":
    calculate_happiness()