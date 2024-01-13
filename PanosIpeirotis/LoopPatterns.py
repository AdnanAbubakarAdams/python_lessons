# Let's say now that we want to sum all the elements in a list.
numbers = [40, 27, 50, 15, 32, 16, 31, 38, 45, 33]
# print(sum(numbers))

# Loop way
sum_of_nums = 0

for num in numbers:
    sum_of_nums = sum_of_nums + num
    print(sum_of_nums)

numbers = [40, 27, 50, 15, 32, 16, 31, 38, 45, 33]

maximum_num = -1
for num in numbers:
    print("Processing number:", num)
    if num > maximum_num:
        maximum_num = num
        print("We found a new maximum:", maximum_num)
    print("The current maximum is:", maximum_num)


minimum = None
for num in numbers:
    print("Processing number:", num)
    if minimum == None:
        minimum = num
        print("We found a new minimum:", minimum)
    if num < minimum:
        minimum = num
        print("We found a new minimum:", minimum)
    print("The current minimum is:", minimum)