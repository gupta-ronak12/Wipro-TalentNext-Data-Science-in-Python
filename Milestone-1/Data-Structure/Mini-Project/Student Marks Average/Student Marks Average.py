"""
Description: 
Stores student records in a dictionary where the name is the key 
and a list of marks (Math, Physics, Chemistry) is the value. 
Accepts a student's name from the user and calculates their average percentage marks.
"""

# Sample student records dictionary
student_records = {
    "Krishna": [67.0, 68.0, 69.0],
    "Arjun": [70.0, 98.0, 63.0],
    "Malika": [52.0, 56.0, 60.0]
}

# Ask user for a student's name
name = input("Enter a name: ")

if name in student_records:
    marks = student_records[name]
    # Calculate average percentage marks
    average = sum(marks) / len(marks)
    print(f"Average percentage mark: {average:.0f}")
else:
    print(f"Error: Student '{name}' not found in records.")