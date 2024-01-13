students = ["Joe", "Amy", "Brad", "Maria", "Sophia", "Michael"]
for name in students:
    print("Hi", name)
    print("The assignment is now posted online.")
    print("The deadline is in one week.")
    print("Cheers,\nPanos")
    print("------")
print("Done!")

# Write a program that uses a for loop to print

# One of the months of the year is January
# One of the months of the year is February
# One of the months of the year is March
# etc ...
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

for month in months:
    print("One the months of the year is", month)
    print("--------------------")
print("thats all 12 months")

count = 1
for month in months:
    print(f"{count}th " "month of the year is", month)
    count = count + 1
    print("------------------")
print("i believe we are done here")

'''
Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20

Write a loop that prints each of the numbers on a new line.
Write a loop that prints each number and its square on a new line.
'''
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# square_of_numbers = 2
for nums in numbers:
    print(nums)
    print("======")

for nums in numbers:
    print(nums, "==>", nums * nums)
    print("/////////")


#----------RANGE-------------#
print(list(range(10)))

print(list(range(10)))  # start at zero, < the specified ceiling value

for i in range(10):
    print(i, "squared is", i * i)

# from the left value, < right value
print(list(range(-5, 5)))

# range(10) is the same at range(0,10)
print(list(range(10)))
print(list(range(0, 10)))

# from the left value, to the middle value, incrementing by the right value
print(list(range(-5, 50, 5)))

# Pythonic style, use iterators
names = ["Abe", "Bill", "Chris", "Dorothy", "Ellis"]
for n in names:
    print(n)

# print your name 10 times (easy, peasy).
# print on the screen a "triangle", by printing first "#", then "##", then "###", etc. Repeat 10 times; Hint: The command print(i*'#') will print the character '#' a total of i times.
for i in range(10):
    print("Adnan")

for i in range(10):
    print((i+1) * "#")
    
for i in range(1, 11):
    print(i * "#")