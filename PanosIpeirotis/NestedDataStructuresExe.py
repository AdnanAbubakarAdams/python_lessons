# Exercise
# You are given the following data structure.
data = {
    "Panos": {
        "Job":"Professor",
        "YOB": "1976",
        "Children": ["Gregory", "Anna"]
    },
    "Joe": {
        "Job":"Data Scientist",
        "YOB": "1981"
    }
}
'''You need to write code that
Prints the job of Joe
Prints the year of birth of Panos; prints the age of Panos
Prints the children of Panos
Prints the second child of Panos
Prints the number of people entries in the data. (Notice that it is much harder to find all the people in the data, eg the children)
Checks if Maria is in the data
Checks if Anna is in the data
Checks if Panos has children.
Checks if Joe has children. How can you handle the lack of the corresponding key? Would your code work when the list of children is empty, instead of missing?'''

# ------SOLUTION------- #
# Prints the job of Joe
job_of_joe = data["Joe"]["Job"]
print("joe work as a", job_of_joe)
# Prints the year of birth of Panos;
year_of_birth_Panos = data["Panos"]["YOB"]
print("panos was born in the year", year_of_birth_Panos)
# Prints the children of Panos
children_of_panos = data["Panos"]["Children"]
print("the children of panos are", children_of_panos)
# Prints the second child of Panos
second_child_of_panos = data["Panos"]["Children"][1]
print("the second child of panos is named", second_child_of_panos)
# Checks if Maria is in the data
"Maria" in data.keys()
# Prints the number of people entries in the data.
# Checks if Maria is in the data, simpler
"Maria" in data
# Checks if Anna is in the data
"Anna" in data
# Notice that the in command *will not* look into the values
# We need to use much more complex code to check all the data, beyond the keys
# Checks if Panos has children
"Children" in data["Panos"]
# Checks if Joe has children
"Children" in data["Joe"]
# If the "Children" entry under Joe had an empty list, instead of being non-existence then we need to augment
# our condition, and write something like:
"Children" in data["Joe"] and len(data["Joe"]["Children"]) > 0