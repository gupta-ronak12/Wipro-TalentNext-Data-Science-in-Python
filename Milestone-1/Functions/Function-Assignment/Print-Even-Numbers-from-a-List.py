"""
Assignment
Description: Create a function that filters and returns even numbers from a list.

Approach:
1. Define a function that accepts a list as an argument.
2. Initialize an empty list (e.g., 'even_numbers') to store the results.
3. Use a 'for' loop to iterate through each element in the input list.
4. Use the modulo operator (%) to check if the number is divisible by 2 (num % 2 == 0).
5. If true, append the number to the 'even_numbers' list.
6. Return or print the resulting list.
"""

def get_even_numbers(input_list):
    even_numbers = []
    for num in input_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = get_even_numbers(sample_list)

print(f"Sample List: {sample_list}")
print(f"Expected Result: {result}")