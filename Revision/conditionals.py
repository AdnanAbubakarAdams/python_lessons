# simple conditionals
operating_system = "Mac OS"
if operating_system == "Windows OS":
    print("the right update needed is Mac OS")
else:
    print("update your Mac OS now")

# 
system = "OS 2"
# If OS 2  is running, the  display a "no update needed" message
if system ==  "OS 2":
    print("no updates needed")

# 
system = "OS 1"
if system == "OS 2":
    print("no updates needed")
else: 
    print("updates needed")

# 
system = "OS 4"
if system == 'OS 2':
    print("no updates needed")
elif system == "OS 1":
    print("updates needed")
elif system == "OS 3":
    print("updates needed")
else: 
    print("we have nothing for  this OS")

# 
system = "OS 4"
if system == "OS 2":
    print("no updates needed")
elif system == "OS 1" or system == "OS 3":
    print("updates needed for this OS")
else:
    print("we got nothing for this pc contact linux")

# 
approved_user1 = "Adnan"
approved_user2 = "Rondo"
username = "Rondo"

if username == approved_user1 or username == approved_user2:
    print('this user has access to this device.')
else:
    print("this user does not have access to this device.")

# 
list_of_approved_users = ["adnan", "rondo", "james", "son", "hojland"]
username = "hojland"

if username in list_of_approved_users:
    print("This user is allow access to score goals in this league")
else: 
    print("This user not wanted in this league!")

# 
organization_hours = False

if organization_hours:
    print("login attempt made during organizations hours!")
else: 
    print("login attempt made outside organizations hours")

# 
list_of_approved_users = ["adnan", "rondo", "james", "son", "hojland"]
username = "adnan"
organization_hours = True

if username in list_of_approved_users and organization_hours:
    print(username, "made a login attempt during organization hours")
else:
    print(username, "made attempt to login outside the organization hours")

# 
