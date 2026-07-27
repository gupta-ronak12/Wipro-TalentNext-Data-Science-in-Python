"""
Description: 
Creates a dictionary containing people as keys and interesting facts as values. 
Displays the initial dictionary, modifies an existing value, adds a new key-value pair, 
and prints the updated results.
"""

# 1. Create a dictionary with people and an interesting fact about each
people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

print("Initial List of People and Facts")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")

# 2. Change a fact about one of the people (e.g., Jeff's fact)
people_facts["Jeff"] = "Is afraid of heights."

# 3. Add an additional person and corresponding fact
people_facts["Jill"] = "Can hula dance."

print("\nUpdated List of People and Facts")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")