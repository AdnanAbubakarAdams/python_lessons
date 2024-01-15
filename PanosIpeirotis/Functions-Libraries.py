# Built-in functions
# Python provides a set of functions that already built-in. You are already familiar with some functions:
# len, sum, max, and min
numbers = [3, 41, 12, 9, 74, 15]
# len() takes as a parameter a string (and returns its length in characters)
# or a list/set/dictionary/... (and returns the number of elements)
print("Length:", len(numbers))

# max(sassasssssjajsksncnfja) / min() takes as a parameter a *list* and returns
# the maximum or minimum element
print("Max:", max(numbers))
print("Min:", min(numbers))

# sum() gets as input a list of numbers and returns their sum
print("Sum:", sum(numbers))

'''So, notice how a function works. It has input and output. In all the examples above, the input is a list of numbers (numbers).

What is the output?

For len(), the output is a number corresponding to the length of the list.
For max() the output is a number corresponding to the maximum element of the list.
For min() the output is a number corresponding to the minimum element of the list.
For sum() the output is a number corresponding to the sum of all the elements in the list.'''

# round ------
# At its simplest form, rounds gets one input: a number. It returns an integer as the output, which is the integer closest to the input number (aka "rounded" number)
print(round( 4.6692))
# The round() function can also take two inputs. The first input is the number, and the second input is the number of decimal digits that we want to keep.
print(round( 4.6692 , 2))
print(round( 4.6692 , 0 ))
print(round( 867.5309, 1))
print(round( 867.5309, 0))
print(round( 867.5309, -1))

# sorted -------
# Consider now the sorted function. This function takes as input as list, and returns as output the sorted version of the list.
numbers = [3, 41, 12, 9, 74, 15]
print(sorted(numbers))
names = ['George', 'James', 'Alex', 'Mary', 'Helen', 'Zoe']
print(sorted(names))

# --------- Functions from Libraries ----------- #
import math
# Square root
math.sqrt(14641)

# 
# Same as above, but with variables
x = 14641
y = math.sqrt(x)
print(y)

# 
x = 18
y = 60
print(math.gcd(x, y))

# 
x = 49
y = 56
print(math.gcd(x, y))

'''
Use the math.sqrt function to get the square root of the numbers:
121
12321
1234321
123454321
'''
print(math.sqrt(121))
print(math.sqrt(12321))
print(math.sqrt(1234321))
print(math.sqrt(123454321))

# 
import random
print(random.random())

# generate 10 random values
for i in range(10):
    x = random.random() # random.random() returns random values from 0 to 1
    print(f"The number is {x:.3f}") # print the number with 3 decimal digits

t = [ 'Angela', 'Pamela', 'Sandra', 'Rita']
random.choice(t)

# Create a list of 8 random integer numbers. (Hint: You can multiply random.random() by 100, and then use round() to get numbers between 0 and 100.)
# Using a for loop
result = []  # the list where we will store the results
for i in range(8):  # repeat the process 8 times
    n = random.random()  # create a random number between 0 and 1
    n = 100 * n  # multiply by 100, to get a random number between 0 and 100
    n = round(n)  # get the rounded version, which gives back an integer
    result.append(n)

print(result)

# Using a list comprehension
result = [round(100 * random.random()) for i in range(8)]
print(result)