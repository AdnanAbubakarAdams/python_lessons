# WRITING CONDITIONAL STATEMENTS
operating_system = "0S 3"
if operating_system == "0S 2":
    print("Updates needed")
else:
    print ("No updates needed" )

# Assign a variable named `system` to a specific operating system, represented as a string
# This variable indicates which operating system is running
# Feel free to run this cell multiple times; each time try assigning `system` to different values ("OS 1", "OS 2", "OS 3") and observe the result
system = "OS 2"
# If OS 2 is running, then display a "no update needed" message
if (system == "OS 2"):
    print("no update needed")
# -------------------------- 
system = "OS 1"
if system == "OS 2":
    print("no update needed")
else:
    print("update needed")
# -----------------------------
system = "OS 3"
if system == "OS 2":
    print("no update needed")
elif system == "OS 1":
    print("update needed")
elif system == "OS 3":
    print("updates needed")
# -----------------------------
system = "OS 4"
if system == "OS 2":
    print("no update needed")
elif (system == "OS 1" or system == "OS 3"):
    print("update needed")

# ----------------------------
approved_user1 = "elarson"
approved_user2 = "bmoreno"

username = "bmoreno"

if username == approved_user1 or username == approved_user2:
    print("This user has access to this device.")
else:
    print("This user does not have access to this device.")
    
# ------------------------------
approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

username = "bmoreno"

if username in approved_list:
    print("This user has access to this device.")
else:
    print("This user does not have access to this device.")

# -------------------------------
organization_hours = False

if organization_hours:
   print("Login attempt made during organization hours.")
else: 
   print("Login attempt made outside of organization hours.")

# ---------------------------------