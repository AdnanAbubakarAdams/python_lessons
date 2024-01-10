
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