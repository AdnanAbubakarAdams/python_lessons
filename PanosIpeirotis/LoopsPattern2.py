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

# 
franchise_names = [] # We create an empty list
for team in nba_teams: # We iterate over all elements of the list
    # Do some operation on the list element "team"
    # and get back the result "franchise"
    franchise = team.split()[-1]
    # Append the "franchise" element in the list that we created before  the loop
    franchise_names.append(franchise)
print(franchise_names)
# 
franchise_names = [ team.split()[-1] for team in nba_teams]

# Defining List Comprehensions
'''The syntax of list comprehensions is based on the way mathematicians define sets and lists, a syntax that leaves it clear what the contents should be.
For example S is a set of the square of all integer numbers from 0 to 9. In math notation, we write:
S = {x² : x in {0 ... 9}}
Python's list comprehensions give a very natural way to write statements just like these. It may look strange early on, but it becomes a very natural and concise way of creating lists, without having to write for-loops.
Let's see again the comparison with for loops:'''

# This code below will create a list with the squares
# of the numbers from 0 to 9
S = [] # we create an empty list
for i in range(10): # We iterate over all numbers from 0 to 9
    S.append(i*i) # We add in the list the square of the number i
print(S )# we print(the list)

S = [i*i for i in range(10)]
print(S)

# 
V=[] # Create a list
for i in range(13): # Change i to be from 0 to 12
    V.append(2**i) # Add 2**i in the new list
print(V)

# And rewritten as a list comprehension:
V = [2**i for i in range(13)]
print(V)

# from the NBA teams up the file
franchise_names = []
look_for = 'B' #looking
for team in nba_teams:
    franchise = team.split()[-1]
    if franchise.startswith(look_for):
        franchise_names.append(franchise)
print(franchise_names)

# 
look_for = 'B'
franchise_names = [team.split()[-1] for team in nba_teams if team.split()[-1].startswith(look_for)]
print(franchise_names)

# 
# Alternatively, you can even break the lines within a comprehension
# This may help with readability
franchise_names = [team.split()[-1]
                   for team in nba_teams
                   if team.split()[-1].startswith(look_for)]
print(franchise_names)

# 
M = []
for i in S: # iterate through all elements in S
    if i%2 == 0: # if i is an event number
        M.append(i) # ..add it to the list
print(M)

M = [x for x in S if x%2 == 0]
print(M)

# IN REAL TIMES
sentence = 'The quick brown fox jumps over the lazy dog'
words = [(w.upper(), w.lower(), len(w)) for w in sentence.split()]
print(words)

# SETS AND DICTIONARY COMPREHENSIONS------------
# Creating a set instead of a list.
S = {i*i for i in range(10)}
print(S)

# Dictionary comprehension, where team name becomes the key, and franchise name the value
teams_franchise = {team:team.split()[-1] for team in nba_teams}
print(teams_franchise)

# Dictionary comprehension, where team name becomes the key, and franchise name the value
words = {w:len(w) for w in sentence.split()}
print(words)