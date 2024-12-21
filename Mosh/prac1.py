# we check in a patient named john smith
# he is 20 years old
# he is a new patient

# solution:->
# first_name = "John"
# last_name = "Smith"
# age = 20
# status = "new patient"
# print(f'{first_name} {last_name} is {age} and a {status}')

# # # solution2 :-> using input
# first_name = input("what is your first name? ")
# # print("welcome " + first_name)
# last_name = input("what is your last name? ")
# age = input("how old you? ")
# status = input("are you a new patient or old? ")
# # print("welcome " + first_name + " " + last_name)
# print("Patient name is " + first_name + " " + last_name, "and he is " + age + " years old "  + "and is a " + status + " patient")

# # data types
# # str()
# # float()
# # int()
# # bool()
# ghana_independence = input("in which year did Ghana gain their independece from the british? ")
# current_year = 2024
# ghana_age = current_year - int(ghana_independence)
# print(f'Ghana is {ghana_age} years old :)')

# united_states_independence = input("in which year did United States of America gain their independence? ")
# current_year = 2024
# USA_age = current_year - int(united_states_independence)
# print(f'U.S.A is {USA_age} years old :)')

# # calculator
# Airpod_max = 415.99
# Paid = 100
# Balance = Airpod_max - Paid
# print(Balance)

# # real calculator
# Airpod_max = input("what is the price of the airpod max? ")
# Paid = input("how much did you pay upfront? ")
# Balance = int(Airpod_max) - int(Paid)
# print(f'Your total balance is {Balance}')


# # string and string methods
# action = "Refreshing python memories"
# print(action.upper())
# print(action.find("y")) # will return the index of the first "y" it finds in the string
# print(action.replace("memories", "skills"))

# conditionals
# temperature = 30

# if temperature < 30:
#     print("it's so cold today, stay warm")
# elif temperature > 20:
#     print("it's getting warm")
# else:
#     print("it's so hot, stay hydrated")

# # 1lb = 0.45kg and 1kg = 2.20lb
# your_weight = float(input("how much do you weigh? "))
# measurement = input("is it in K or L? ")

# pound = your_weight / 2.20
# kilogram = your_weight * 2.20

# if measurement == "l" or measurement == "L":
#     print(f'here is how you measure {pound}kg')
# elif measurement == "k" or measurement == "K":
#     print(f'here is how you {kilogram}lbs')
# else:
#     print('please enter your weight again')

# his solution
# weight = int(input("enter your weight: "))
# unit = input("(K)g or (L)bs: ")
# if unit.upper() == "K":
#     converted = weight / 0.45
#     print("weight in Lbs: " + str(converted))
# else:
#     converted = weight * 0.45
#     print("weight in Kgs: " + str(converted))

# LOOPs
i = 1
while i <= 4:
    print(i)
    i += 1

i = 1
while i <= 5:
    print(i * "#")
    i += 1

# arrays or list
names = ["united", "is", "the", "only", "way"]
print(names)
print(names[-1])
names[0] = "unity"
print(names)

nums = [1,2,3,4,5]
nums.append(6)
print(nums)
nums.insert(2,"-")
print(nums)
nums.remove("-")
print(nums)
print(len(nums))


numbers = [1,2,3,4,5]
for num in numbers:
    print(num)


numbers = range(5)
for num in numbers:
    print(num)

numbers = range(5, 10)
for num in numbers:
    print(num)

numbers = range(5, 10, 2)
for num in numbers:
    print(num)

