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
