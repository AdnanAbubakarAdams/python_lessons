# This is just to use the time.sleep function
# We will use the time.sleep function to slow
# down the execution of loops, only for
# instructional purposes. In reality, we add
# such delays only in special cases.
import time

i = 0
while i <= 5:  # check if i<=5. If yes, execute the nested block of code
    print(i)  # print the current value of i
    time.sleep(1.0)  # Wait for 1 sec
    i = i + 1  # increase i
    # Now go to the beginning of the loop

temperature = 115
while temperature > 110:  # Execute the loop code if temperature > 110
    print(temperature)
    time.sleep(1.0)  # Wait for 1 sec
    temperature = temperature - 1  # Decrease the value of temperature by one
    # Now go back to the beginning of the loop
print("The tea is cool enough.")

money_in_bank = 1000
interest = 6
year = 2017
widthdrawal_per_period = 200

while money_in_bank > 0:
    print(f"At the beginning of {year} you have ${money_in_bank:.2f} in the bank.")
    money_in_bank = money_in_bank - widthdrawal_per_period
    money_in_bank = money_in_bank * (1 + interest / 100)
    year = year + 1
    print(f"At the end of {year} you have ${money_in_bank:.2f} in the bank.")
    print("-----------------")

print("You have no money left!")