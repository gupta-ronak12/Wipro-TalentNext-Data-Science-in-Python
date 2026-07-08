"""
Assignment
Description: Create a script that takes two numbers as command line 
             arguments and returns their sum.

Approach:
1. Import the 'sys' module to access command line arguments.
2. Check if the correct number of arguments (3, including script name) is provided.
3. Access arguments using 'sys.argv'.
4. Convert the string arguments into integers/floats.
5. Calculate the sum and print the result.
"""

import sys

if len(sys.argv) == 3:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is: {total}")
else:
    print("Please provide exactly two numbers as arguments.")
    print("Usage: python script_name.py <num1> <num2>")