"""
Project: 2
Description: Calculate cloud server costs based on a rate of $0.51 per hour.
- Calculate cost per day, per week, and per month.
- Calculate how many days of operation are possible with a $918 budget.

Concepts Used:
- Arithmetic Operators (*, /)
- Variable Assignment
- User Output (print())
- F-string Formatting (:.2f)

"""

hourly_rate = 0.51        # we put the hourly rate in a variable for easy modification in the future if needed

cost_per_day = hourly_rate * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30 
days_with_budget = 918 / cost_per_day


# We use :.2f inside the f-string to format the numbers to 2 decimal places, 
# ensuring they look like standard currency (e.g., 12.24 instead of 12.240000000000001).

print(f"Cost per day: ${cost_per_day:.2f}")
print(f"Cost per week: ${cost_per_week:.2f}")
print(f"Cost per month: ${cost_per_month:.2f}")
print(f"Days of operation with $918: {days_with_budget:.1f} days")