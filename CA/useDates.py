from datetime import date

print(date.today())

print("Today's date is: " + str(date.today()))

parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")

parsecs_input = input("Enter number of parsecs:")
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs
print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")