print("addition:")
print(1 + 1)
print(1.5 + 1)

print("subtraction:")
print(1 - 1)
print(1 - 1.0)

print("negation:")
print(-5)

print("multiplication:")
print(3 * 3)  # integer
print(3 * 3.0)  # floating point

print("division:")
print(4 / 2)
print(5 / 2)

print("integer division:")
print(4 // 2)
print(5 // 2)

print("modulo:")  # modulo is a fancy term for remainder of a division
print(4 % 2)
print(5 % 2)
print(5.5 % 2)
print(75 % 4)
print(10 % 3)

print("power:")
print(10 ** 3)
print(2 ** 5)

# Exercise
# Assume that you go to a restaurant, and you order $50 worth of food. Then you need to add the NY Sales Tax (8.875%) and add a tip (say, 20%). Write down the calculation that will print the total cost of the food.
print("The total cost of the meal, with tip on the pre-tax amount is:")
print(50 + 50 * 8.875 / 100 + 50 * 20 / 100)

print("The total cost of the meal, with tip on the post-tax amount is:")
print(50 + 50 * 8.875 / 100 + (50 + 50 * 8.875 / 100) * 20 / 100)

# You have a stock that closed at $550 on Monday, and then closed at $560 on Tuesday. Calculate its daily return: the daily return is defined as the difference in the closing prices, divided by the closing price the day before.
print("The daily return on my stocks is:")
print((560 - 550) / 550)
# percentage
print("The daily return is:")
print(100 * (560 - 550) / 550)