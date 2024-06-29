# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

manchester_united = 20
liverpool = 19
if manchester_united > liverpool:
    print(manchester_united)

a = 24
b = 21
if a <= 0:
    print(a)
else:
    print(b)

# all three conditionals
if a <= b:
    print("a is less than or equal to b")
elif a == b:
    print("a is equal to b")
else:
    print("we coding")

a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")

a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")

a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

# True	and	True	True
# True	and	False	False
# False	and	True	False
# False	and	False	False
# True	or	True	True
# True	or	False	True
# False	or	True	True
# False	or	False	False

object_size = 10
proximity = 9000

if object_size > 5 and proximity < 1000:
    print('Evasive maneuvers required')
else:
    print('Object poses no threat')