fact = "The Moon has no atmosphere"
two_facts = fact + ", No sound can be heard on the moon"
print(two_facts)

multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

print("i love manchester united".title())

heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)

# USING split()
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)

temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split('\n')
print(temperatures_list)