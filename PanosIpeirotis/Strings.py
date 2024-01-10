
str1 = "hello"
str2 = "world"
message = str1 + " " + str2 + "!"
print(message)
# 
# You are given a variable name = 'Panos' and variable phone = '212-998-0803'. Use the values of these variables to create and print the message Call Panos at 212-998-0803.
name = "Panos"
phone = "212-998-0803"
message = "call" + " " + name + " " + "at" +" "+ phone
message = "call " + name  + " at " + phone
print(message)

# string length
# len(str): length of a string, number of characters
word = "Python is the word. And on and on and on...."
print(len(word))

# SLICING AND INDEXING
word = "Python"
print(word[0]) # character in the first position
print(word[1]) # char in the 2nd position
print(word[5]) # last char in the variable

# NEGATIVE INDEXING
word = "Python"
print(word[-1]) # starting at the last word or starting backwards
print(word[-2]) # starting at the last word or starting backwards
print(word[-6]) # starting at the last word or starting backwards

# SLICING
word = "Python"
print(word[0:2]) # start at 0 index stop at 2 index but 2 is exclusive === "Py"
print(word[2:5]) # start at 2 index stop at 5 index but 5 is exclusive === "tho"
print(word[2:]) # start at 2 index all the way to the end === "thon"
print(word[:3]) # start at 0 index stop at 3 index but 3 is exclusive === "Pyt"
print(word[-3:]) # start at 0 index stop at 3 index but 3 is exclusive === "hon"
print(word[-3:-1]) # start at -3 index stop at -1 index but -1 is exclusive === "ho"
print(word[1:-1]) # start at 1 index stop at -1 index but -1 is exclusive === "ytho"

univ = "New York University"
print(univ[:3]) # 'New'
print(univ[4:8]) # 'York'
print(univ[-10:]) # 'University'
print(univ[1:-3]) # 'ew York Univers'

""" 
    Assign the string 'Dealing with Data' to a Python variable.
    Print the word 'Dealing' by using the indexing/slicing approach.
    Print the word 'Data' by using the negative indexing/slicing approach.
"""
action_done = "Dealing with Data"
print(action_done[:7])
print(action_done[-4:])

# ---------- COMPARISONS----ORDERING----FINDING TEXT --------- #
str1 = 'hello'
print(str1 == 'hello')
print(str1 == 'Hello')

print(str1.lower() == 'Hello'.lower())

email1 = "panos@nyu.edu"
email2 = "peter@nyu.edu"
print("Are the emails different?", email1 != email2)

name1 = "Abraham"
name2 = "Bill"
# Abraham is lexicographically before Bill
print(name1 < name2)

name1 = "Panos"
name2 = "Bill"
# Panos is lexicographically after Bill
print(name1 < name2)

# --------- # ---------- #
"""
Consider the string billgates@microsoft.com. Write code that finds the username of the email address and the domain of the email address. You will need to use the .find() command, and also use your knowledge of indexing and slicing for this exercise. Hint: You will need to search for the @ character using find, and then use the result to get the parts of the string before and after the @ character. (Do not worry if this seems tedious, this is mainly for practice; later on, we will see how to do this in an easier way.)
"""
# your code here
email = "billgates@microsoft.com"
postion_of_domain = email.find("@")
domain_of_email = email[9:] # we can also use position_of_domain instead of 9
username_of_email = email[:9]
print("position:", postion_of_domain)
print("username:", username_of_email)
print("domain:", domain_of_email)

# count function str_1.count(str_2): counts the number of occurrences of one string in another.
word = "Python is the word. And on and on and on and on..."
lookfor = "on"
count = word.count(lookfor)
print("We see the string '", lookfor, "' that many times: ", count)

word = "Python is the word. And on and on and on and on..."
lookfor = "PYTHON"
count = word.lower().count(lookfor.lower())
print("We see the string '", lookfor, "' that many times: ", count)

"""
startswith and endswith functions
Finally, we can also check if a particular string starts or ends with a another substring
haystack.startswith(needle): does a the haystack string start with the needle string?
haystack.endswith(needle): does a the haystack string end with the needle string?
"""
name = "New York University"
prefix = "New York"
print("Does ", name, " starts with", prefix, "?")
print(name.startswith(prefix))

name = "New York University"
prefix = "University"
print("Does ", name, " starts with", prefix, "?")
print(name.startswith(prefix))

name = "New York University"
suffix = "University"
print("Does ", name, " ends with", suffix, "?")
print(name.endswith(suffix))