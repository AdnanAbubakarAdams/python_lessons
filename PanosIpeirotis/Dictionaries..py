'''Dictionaries are data structures containing key-value pairs.

Dictionaries have a set of unique keys and are used to retrieve the value information associated with these keys.

For instance, a dictionary might be used to store:

for each user (the key), that user's location (the value), or
for each product id (the key), the description associated with that product (the value).
Dictionaries are very common and are frequently used and encountered in practice.

Creating Dictionaries
Dictionaries are specified by curly braces, { }, containing zero or more comma-separated key-value pairs. In each key-value pair the keys and values are separated by a colon, :.'''

# Dictionary with four key value pairs
a_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

# The  a, b, c, d are keys
# The 1, 2, 3, 4 are values
print(a_dict)

# A key cannot be repeated
# See what happens when we repeat the key "c"
a_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "c": 4}
print(a_dict)

phones = {
    "Panos": "212-998-0803",
    "Maria": "656-233-5555",
    "John": "693-232-5776",
}
print(phones)

geoip = {"longitude": -73.9885, "latitude": 40.7317, "ip": "216.165.95.68"}
print(geoip)

# ----------Accessing Dictionary Elements-------------#
# To access elements in the dictionary we use the key in brackets, or the get() command, as follows:
print(geoip["ip"])
print(geoip.get("ip"))

print(phones["Panos"])
print(phones.get("Panos"))


# -------Adding new entries, updating existing ones, deleting entries-------- #
# We can add an entry in the dictionary by assigning a value to a particular key. If the key already exists, the value assigned to that key gets updatd.

# Add a new key, "isp", with value "New York University"
geoip["isp"] = "New York University"
print(geoip)

# Update the valye for "John"
phones["John"] = "415-794-3423"
# Add a new key, "Elena", and the corresponding value
phones["Elena"] = "212-998-0803"
print(phones)

# If we want to remove a key x from the dictionary, the command dict.pop(x) removes the key x and its associated value from the dictionary
# Remove John from the phones dictionary
phones.pop("John")
print(phones)

# -------Checking if a key appears in a dictionary-------- #
# Like the set, the easiest way to check if a particular key is in a dictionary is through the in keyword:
"Panos" in phones
"Jose" in phones

# Notice that the in will not work if we try to find a value in the dictionary.
# The in does *not* work for values
"212-998-0803" in phones

# ---------Accessing keys and values----------- #
# Some common operations on dictionaries:

# dict.keys(): returns a list containing the keys of a dictionary
# dict.values(): returns a list containing the values in a dictionary
phones = {
    "Panos": "212-998-0803",
    "Maria": "656-233-5555",
    "John": "693-232-5776",
    "Jake": "415-794-3423",
}
print(phones.keys())
print(sorted(phones.keys()))
print(phones.values())


# Exercise
# Find the common keys in a_dict and b_dict
# Find the common values in a_dict and b_dict
a_dict = {"a": 5, "b": 5, "c": 3, "c": 4}
b_dict = {"c": 5, "d": 6}

# SOLUTION #
# Lets find the common keys first
# Extract the keys from each dictionary
keys_a = a_dict.keys()
keys_b = b_dict.keys()

# Then compute the intersection
# Keys are guaranteed to be unique, so the dict_keys
# behaves like a set, and supports set operations
common_keys = keys_a & keys_b
print("Common keys", common_keys)

# Now let's repeat the process for values
values_a = a_dict.values()
values_b = b_dict.values()

# However, trying to compute the intersection of values
# will not work if we try to apply it naively.
# The values_a and values_b are not like sets, as
# they can contain duplicate values
# Uncomment the code below to try. You will get
# "TypeError: unsupported operand type(s) for &: 'dict_values' and 'dict_values'"
#
# values_a & values_b

# Instead, we have to convert the values_a and values_b
# variables into sets first, and then compute the intersection
common_values = set(values_a) & set(values_b)
print("Common values", common_values)