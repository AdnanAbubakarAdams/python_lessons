# Let's say now that we want to sum all the elements in a list.
numbers = [40, 27, 50, 15, 32, 16, 31, 38, 45, 33]
# print(sum(numbers))

# Loop way
sum_of_nums = 0

for num in numbers:
    sum_of_nums = sum_of_nums + num
    print(sum_of_nums)


numbers = [40, 27, 50, 15, 32, 16, 31, 38, 45, 33]
# 
maximum_num = -1
for num in numbers:
    print("Processing number:", num)
    if num > maximum_num:
        maximum_num = num
        print("We found a new maximum:", maximum_num)
    print("The current maximum is:", maximum_num)

# 
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

# Counting Elements
count = 0
threshold = 30

for num in numbers:
    print("Processing number:", num)
    if num > threshold:
        count = count + 1
        print("We found a number above", threshold, "and we increased count to", count)

print("We have", count, "numbers above", threshold)

# Finding an element in the list
nba_teams = [
    "Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets",
    "Chicago Bulls", "Cleveland Cavaliers", "Dallas Mavericks",
    "Denver Nuggets", "Detroit Pistons", "Golden State Warriors",
    "Houston Rockets", "Indiana Pacers", "LA Clippers", "Los Angeles Lakers",
    "Memphis Grizzlies", "Miami Heat", "Milwaukee Bucks",
    "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks",
    "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers",
    "Phoenix Suns", "Portland Trail Blazers", "Sacramento Kings",
    "San Antonio Spurs", "Toronto Raptors", "Utah Jazz", "Washington Wizards"
]
print("The list contains", len(nba_teams), "teams")

looking_for = "Brooklyn"
for team in nba_teams:
    if looking_for in team:
        print("We found the team:", team, "containing", looking_for)

# 
looking_for = "Brooklyn"

result = None
for team in nba_teams:
    if looking_for in team:
        result = team
        print("We found the team:", team, "containing", looking_for)

print("Result:", result)

# Notice that we get an incorrect result if we assume that `team` will contain the answer
# The loop will continue running
looking_for = "Brooklyn"
for team in nba_teams:
    if looking_for in team:
        print("We found the team:", team, "containing", looking_for)

print("Result:", team)

# 
looking_for = "New"
for team in nba_teams:
    if looking_for in team:
        result = team
        print("We found the team:", team, "containing", looking_for)

print("Result:", result)

# 
franchise_names = []
for team in nba_teams:
    franchise = team.split()[-1]
    # print(team, "\t ==>\t", franchise)
    franchise_names.append(franchise)
# Print the list
print(franchise_names)

# 
# Or use a loop to print each name in a separate line
print("List of NBA franchise names")
for franchise_name in franchise_names:
    print(franchise_name)