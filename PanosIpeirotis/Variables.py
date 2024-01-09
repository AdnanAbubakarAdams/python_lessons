food = 75
tax = 8.875 / 100
tip = 20 / 100
cost = food + food * tax + food * tip
print("The cost of the meal will be:", cost)
# print(cost)

message = "I love Python..."
print(message)
print(message)
print(message)
print(message)

males = 7
females = 10
fraction = males / (males + females)
print("Percentage of men:")
print(100 * fraction)

# ---------------
# Upon taking this class, you are recruited in a new hot startup. They offer you a starting salary of $150K, a promised 25% bonus, and an equity package currently worth $400K, vesting over a period of 4 years. You want to examine the true value of this package, so you write the following program:
# A small example to start
base_salary = 150000
expected_bonus = 0.25
equity = 400000
years_vesting = 4
# Base scenario
yearly_value = base_salary + expected_bonus * base_salary + equity / years_vesting
print("The yearly value of this offer is", yearly_value)