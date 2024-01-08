# 
i = 1
while i < 5:
    print(i)
    i = i + 1
# 
login_attempts = 0
while login_attempts < 5:
    print("Login attempts:", login_attempts)
    login_attempts = login_attempts + 1
# 
count = 0
login_status = True
while login_status == True:
    print("Try again.")
    count = count + 1
    if count == 4:
        login_status = False
# 
computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    if asset == "desktop20":
        print(asset)
        break
# 
computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    if asset == "desktop20":
        continue
    print(asset)
# You want to print a message that tells the user to “try again” as long as the value of the attempt variable is 5 or less, and you want to increase the value of this variable by 1 each time it passes through the loop.
attempt = 1
while attempt <= 5:
    print ("Try again.")
    attempt = attempt + 1
# You want to print out the numbers 20, 19, 18, 17, and 16.
i = 20
while i > 15:
    print (i)
    i = i - 1