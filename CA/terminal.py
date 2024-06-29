# we give out commands to the computer by writing them in text file using programming language. These files are called programs. Running a program means telling a computer to read a text file, translate it to the set of operations that it understands, and perform those actions.
my_name = 'rondo'
print('Hello and welcome ' + my_name + '!')

# working with numbers
x = 10
print(x) # 10
print(type(x)) # int

y = 11.01
print(y) # 11.01
print(type(y)) # float

a = True
print(a) # True
print(type(a)) # bool

x = 'This is a string'
print(x) # This is a string
print(type(x)) # str

enter = str(input('What is your name?: '))
print('welcome to united states of America', enter)
print(type(enter))

lucky_number = int(input('Enter a number: '))
print('Your lucky number is:', lucky_number)
print(type(lucky_number))

john_age = 12
print('john is ', str(john_age))

# working with inputs
name = input("chicharito")
print(name)

name = input("Enter your name:")
print(name)

first_number = int(input("enter the first number: "))
second_number = int(input("enter the second number: "))
print('The sum is: ', first_number + second_number)