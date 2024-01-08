# Define a function named `alert()` 
def alert():
    print("Potential security issue. Investigate further.")
# Call the `alert()` function
alert()

# 
def alert(): 
    for i in range(3):
        print("Potential security issue. Investigate further.")
alert()

# 
def list_to_string():
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]
    for i in username_list:
        print(i)

list_to_string()

# String Concatenation in a function
def list_to_string():
  username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]

  sum_variable = ""

  for i in username_list:
    sum_variable = sum_variable + i
    print(sum_variable)

list_to_string()

# 
def list_to_string():
  username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]

  sum_variable = ""

  for i in username_list:
    sum_variable = sum_variable + i + ", "
    print(sum_variable)

list_to_string()

# welcome message with parametere and argument 
def welcome_python_3(name):
   print("Welcome to the world of Python:", name)
welcome_python_3("Adnan")

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
   fail_percentatage = failed_attempts / total_attempts
   return fail_percentatage
# percentage = calculate_fails(10,2)
# print(percentage)
print(calculate_fails(10,2))

# 
def remaining_login_attempts(maximum_attempts, total_attempts):
    return maximum_attempts - total_attempts
remaining_attempts = remaining_login_attempts(4, 3)
if remaining_attempts <= 0:
    print("Your account is locked")
else:
    print(remaining_attempts)

# Local and Global variables
username = "elarson"
def identify_user():
    print(username)
identify_user()

# 
username = "elarson"
print("1:" + username)
def greet():
    username = "bmoreno"
    print("2:" + username)
greet()
print("3:" + username)

# print(type("Adnan"))