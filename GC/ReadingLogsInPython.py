import_file = "login.txt"
# The `with` statement
# Use `open()` to import security log file and store it as a string
with open(import_file, "r") as file:
  # Use `.read()` to read the imported file and store the result in a variable named `text`
  text = file.read()
# Display the contents of `text`
print(text)

# -------------------------
import_file = "login.txt"
# The `with` statement
# Use `open()` to import security log file and store it as a string
with open(import_file, "r") as file:
  # Use `.read()` to read the imported file and store the result in a variable named `text`
  text = file.read()
text_split = text.split(",")
# Display the contents of `text` split into separate lines 
print(text_split)


# ----------------------------
import_file = "login.txt"
# Assign `missing entry` to a log that was not recorded in the log file
missing_entry = "jrafael,192.168.243.140,4:56:27,2022-05-09"
# Use `open()` to import security log file and store it as a string
# Pass in "a" as the second parameter to indicate that the file is being opened for appending purposes
with open(import_file, "a") as file:
    # Use `.write()` to append `missing_entry` to the log file
    appended_file = file.write(missing_entry)
# Use `open()` with the parameter "r" to open the security log file for reading purposes
with open(import_file, "r") as file:
    # Use `.read()` to read in the contents of the log file and store in a variable named `text`
    text = file.read()
# Display the contents of `text`
print(text)

# ------------------------
import_file = "allow_list.txt"
# Assign `ip_addresses` to a list of IP addresses that are allowed to access the restricted information
ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"
# Display `import_file`
print(import_file)
# Display `ip_addresses`
print(ip_addresses)

# -----------------------------
import_file = "allow_list.txt"
# Assign `ip_addresses` to a list of IP addresses that are allowed to access the restricted information
ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"
# Create a `with` statement to write to the text file 
with open(import_file, "w") as file:
  # Write `ip_addresses` to the text file
  write_ip_adds = file.write(ip_addresses)


# --------------------------------
import_file = "allow_list.txt"
# Assign `ip_addresses` to a list of IP addresses that are allowed to access the restricted information
ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"
# Create a `with` statement to write to the text file 
with open(import_file, "w") as file:
    # Write `ip_addresses` to the text file
    file.write(ip_addresses)
# Create a `with` statement to read in the text file 
with open(import_file, "r") as file:
    # Read the file and store the result in a variable named `text`
    text = file.read()
# Display the contents of `text`
print(text)

# ---------EXAMPLE FROM VIDEO--------------
# Open, read, and split a text file
with open("login_attempts.txt", "f") as file:
    file_text = file.read()
    usernames = file_text.split()
# Create a function that counts a user's failed login attempts
def login_check(login_list, current_user):
    counter = 0
    for i in login_list:
        if i == current_user:
            counter = counter + 1
    if counter >= 3:
        return "You have tried to login three or more times. Your account has been locked."
    else:
        return "Youcan 10g in!"
login_check(usernames, "eraab")