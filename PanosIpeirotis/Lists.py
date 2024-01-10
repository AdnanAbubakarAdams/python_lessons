number_list = [1, 2, 3, 0, 5, 10, 11]
print(number_list)

# 
name_list = ["Panos", "Maria", "Anna", "James"]
print(name_list)

# 
mixed_list = ["Panos", 42, "Anna", 22]
print(mixed_list)

# 
my_string = "Wow these data structures make for exciting dinner conversation"
list_of_words = my_string.split(" ")
print(list_of_words)

# You are given a list of names as one big, multiline string. Each line contains one name.
# Use the split command, appropriately configured, to separate names into a list of names.
# Extract the 3rd name from the list
# Extract the second from the last name, using negative indexing
# Retrieve the 6th to 8th names from the list (inclusive, we want a list of 3 names, 6th, 7th, and 8th)
# Retrieve the last 3 names.
names_string = """Jacob Adams
Emily Brown
Michael Campbell
Madison Davis
Andrew Edwards
Olivia Flores
David Garcia
Sophia Ingram
Nathan Jones
Natalie King"""
# 
seperated_list = names_string.split("\n")
print(seperated_list)
# 
third_name_from_list = seperated_list[2]
print(third_name_from_list)
# 
second_from_last = seperated_list[-2]
print(second_from_last)
# 
sixth_to_eighth = seperated_list[6:9]
print(sixth_to_eighth)
# 
# the_last_three_names = seperated_list[-3:]
the_last_three_names = seperated_list[7:]
print(the_last_three_names)


# ------- FUNCTIONS THAT APPLY TO LIST ------- #
"""
len: The function len(list) returns the number of elements in a list.
sorted: The function sorted(list) Returns the list sorted
max: Returns the maximum element of a list
min: Returns the minimum element of a list
sum: The function sum(list) sums up all the (numeric) elements of a list
"""
# len
names = ["Adnan", "Laila", "Fauzia", "Taju", "Baba", "Muba"]
print("the length of this family is:", len(names))

# sorted
names = ["Adnan", "Laila", "Fauzia", "Taju", "Baba", "Muba"]
print("sorted list for family:", sorted(names))
numbers = [3, 41, 12, 9, 74, 15]
print("sorted numbers:", sorted(numbers))

# max
numbers = [3, 41, 12, 9, 74, 15]
print("maximum number from list:", max(numbers))

# min
numbers = [3, 41, 12, 9, 74, 15]
print("minimum number from list:", min(numbers))

# sum
numbers = [3, 41, 12, 9, 74, 15]
print("the sum of all numbers =", sum(numbers))

# Min and max also operate on strings
# print("Min name:", min(names))
# print("Max name:", max(names))

# Write code that computes the average value of a list of numbers
# Write code that computes the median value of a list of numbers (for simplicity, assume the list contains an odd number of items)
# 
numbers = [3, 41, 12, 9, 74, 15, 5]
length_of_list = len(numbers)
sum_of_nums = sum(numbers)
average_of_nums = sum_of_nums / length_of_list
print("the average of the numbers:", average_of_nums)

# 
sorted_list = sorted(numbers)
# Notice that we use integer division below
# as the index value needs to be an integer
middle = len(numbers) // 2
median = sorted_list[middle]
print("Sorted List:", sorted_list)
print("The median is at position ", middle)
print("The value of the median is", median)

# -------- ADDING AND REMOVING ELEMENTS FROM LISTS -------- #
# list.append(x): add an element ot the end of a list
# list_1.extend(list_2): add all elements in the second list to the end of the first list. Alternatively, it is possible to use the + and concatenate two lists.

# Example of append
name_list = ["Panos", "John", "Chris", "Josh", "Mary", "Anna"]
name_list.append("Elena")
name_list.append("Sofia")
print(name_list)

# Example of extend
name_list = ["Panos", "John", "Chris", "Josh", "Mary", "Anna"]
names_to_add = ["Elena", "Sofia"]
name_list.extend(names_to_add)
print(name_list)
print("Length of list:", len(name_list))

# List concatenation. This is similar to "extend"
name_list = ["Panos", "John", "Chris", "Josh", "Mary", "Anna"]
names_to_add = ["Elena", "Sofia"]
new_list = name_list + names_to_add
print(new_list)

# ------- INSERTING AND REMOVING ELEMENTS -------- #
# list.insert(index, x): insert element x into the list at the specified index. Elements to the right of this index are shifted over
# list.pop(index): remove the element at the specified position
# Insert Jose Hernandez in position 7
names_list = [
    "Jacob Adams",
    "Emily Brown",
    "Michael Campbell",
    "Madison Davis",
    "Andrew Edwards",
    "Olivia Flores",
    "David Garcia",
    "Sophia Ingram",
    "Nathan Jones",
    "Natalie King",
]
# 
names_list.insert(7, "Jose Hernandez")
print(names_list)
# It is there
print(names_list[7])
# We can retrieve the element with pop, and then delete it from the list
names_list.pop(7)
# Name at position 7 changed
print(names_list[7])

# ----- COMMON FUNCTIONS ----- #
# x in list: checks if x appears in the list
# list.index(x): looks through the list to find the specified element, returning it's position if it's found, else throws an error
# list.count(x): counts the number of occurrences of the input element
names = ["Panos", "John", "Chris", "Josh", "Mary", "Anna", "John"]
print("Chris" in names)
print("peter" in names)

name = "Chris"
print("Location of", name, "in the list:", names.index(name))

# Count
print("# of John  in the list", names.count("John"))
print("# of Panos in the list", names.count("Panos"))
print("# of Peter  in the list", names.count("Peter"))