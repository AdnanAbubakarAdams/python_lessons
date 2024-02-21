def alert():
    print("We have a potential security issue. Investigate further!")
alert()

# 
def alert():
    for i in range(3):
        print("I see security issues here, let's investigate.")
alert()

# 
def list_to_string():
    username_list =  ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]
    for username in username_list:
        print(username)
list_to_string()

# 
def list_to_string():
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]

    sum_variable = ""

    for username in username_list:
        sum_variable = sum_variable + username + ", "
        print(sum_variable)
list_to_string()

# functions with parameter
def welcome_greetings(name):
    print("Welcome to coding in python3", name)

welcome_greetings("Adnan")

# 
def display_investigation_message():
    print("investigate activity")
application_status = "potential concern"
email_status = "okay"
if application_status == "potential concern":
    print("application_log:")
    display_investigation_message()
if email_status == "potential concern":
    print("email log:")
    display_investigation_message()

# 
def calculate_fails(total_attempts, failed_attempts):
    fail_percentage = failed_attempts / total_attempts
    return fail_percentage
print(calculate_fails(10, 2))

# 
def remaining_login_attempts(maximum_attempts, total_attempts):
    return maximum_attempts - total_attempts
remaining_attempts = remaining_login_attempts(4, 3)
if remaining_attempts <= 0:
    print("Your accout is locked")
else: 
    print(remaining_attempts)