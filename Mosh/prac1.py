# we check in a patient named john smith
# he is 20 years old
# he is a new patient

solution:->
first_name = "John"
last_name = "Smith"
age = 20
status = "new patient"
print(f'{first_name} {last_name} is {age} and a {status}')

# # solution2 :-> using input
first_name = input("what is your first name? ")
# print("welcome " + first_name)
last_name = input("what is your last name? ")
age = input("how old you? ")
status = input("are you a new patient or old? ")
# print("welcome " + first_name + " " + last_name)
print("Patient name is " + first_name + " " + last_name, "and he is " + age + " years old "  + "and is a " + status + " patient")

# data types
# str()
# float()
# int()
# bool()
ghana_independence = input("in which year did Ghana gain their independece from the british? ")
current_year = 2024
ghana_age = current_year - int(ghana_independence)
print(f'Ghana is {ghana_age} years old :)')

united_states_independence = input("in which year did United States of America gain their independence? ")
current_year = 2024
USA_age = current_year - int(united_states_independence)
print(f'U.S.A is {USA_age} years old :)')

# calculator
Airpod_max = 415.99
Paid = 100
Balance = Airpod_max - Paid
print(Balance)

# real calculator
Airpod_max = input("what is the price of the airpod max? ")
Paid = input("how much did you pay upfront? ")
Balance = int(Airpod_max) - int(Paid)
print(f'Your total balance is {Balance}')


# string and string methods
action = "Refreshing python memories"
print(action.upper())
print(action.find("y")) # will return the index of the first "y" it finds in the string
print(action.replace("memories", "skills"))