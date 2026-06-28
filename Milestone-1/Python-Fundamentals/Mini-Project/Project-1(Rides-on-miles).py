"""
Project: 1
Description: Create a python program that asks the user how far they want to travel.
- Less than 3 miles: Ride Bicycle.
- 3 to 299 miles: Ride Motor-Cycle.
- 300+ miles: Drive Super-Car.
"""


distance = float(input("How far would you like to travel in miles?"))  #because distance can be a decimal value

if distance < 3:
    print("I suggest Bicycle to your destination")
elif 3 <= distance < 300:
    print("I suggest Motor-Cycle to your destination")
else:
    print("I suggest Super-Car to your destination")



"""
Concepts Used:
- Conditional Statements (if, elif, else)
- User Input (input())
- Data Type Casting (float()) 

"""