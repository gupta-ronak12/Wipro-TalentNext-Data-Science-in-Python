"""
Description: 
Accepts a string of words and counts how many times the name 
'Alex' appears within the string.
"""

# Sample input string
input_str = "Hi Alex WelcomeAlex Bye Alex."

# Count occurrences of the substring "Alex"
count = input_str.count("Alex")

print(f"Sample input: {input_str}")
print(f"Sample output: {count}")