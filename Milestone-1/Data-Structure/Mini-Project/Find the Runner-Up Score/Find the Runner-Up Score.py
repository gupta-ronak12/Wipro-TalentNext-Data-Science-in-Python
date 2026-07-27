"""
Description: 
Takes a list of participant scores from University Sports Day, 
removes duplicates, sorts them in descending order, and finds 
the runner-up (second highest) score.
"""

# Given list of scores
scores = [2, 3, 6, 6, 5]

# Remove duplicates using set, then convert back to a sorted list
unique_scores = sorted(list(set(scores)), reverse=True)

# The runner-up score is at index 1
runner_up = unique_scores[1]

print(f"Given list: {scores}")
print(f"Runner-up score: {runner_up}")