"""
Description: 
Extracts the last 'n' characters from a string and repeats 
them 'n' times based on user input.
"""

sample_str = input("Enter a string: ")
n = int(input("Enter an integer n: "))

if 0 <= n <= len(sample_str):
    last_n_chars = sample_str[-n:]
    result = last_n_chars * n
    print("Output:", result)
else:
    print("Error: n must be between 0 and the length of the string.")