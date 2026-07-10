"""
Assignment: 2
Description: Create a program that reads and prints the first 'n' lines 
             of a text file based on user input.

Approach:
1. Prompt the user to enter the number of lines 'n'.
2. Open the file in 'r' (read mode).
3. Use a loop to iterate 'n' times or use the 'itertools.islice()' 
   method for efficiency.
4. Print each line found.
5. Include error handling for invalid input or if 'n' exceeds the file length.
"""

def read_first_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            print(f"--- First {n} lines of {filename} ---")
            for i in range(n):
                line = file.readline()
                if not line: # Stop if end of file is reached
                    break
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for 'n'.")

# Example usage:
try:
    num_lines = int(input("Enter the number of lines to read: "))
    read_first_n_lines("sample.txt", num_lines)
except ValueError:
    print("Please enter a numeric value.")