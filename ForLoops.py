# 
for i in ["elarson", "bmoreno", "tshah", "sgilmore"]:
    print(i)
# 
computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    print(asset)
# 
string = "security"
for character in string:
    print(character)
# 
for i in range(0, 5, 1):
    print(i)
# 
for i in range(5):
    print(i)

# You want to print 3 numbers from a list.
for i in [8, 9, 10]:
    print (i)

# You want to print the message “Access denied” 5 times.
for i in range (5): 
    print ("Access denied" )

# You want to print out a sequence of numbers starting at 10 and ending at 30.
for i in range (10, 31):
    print (i)

# Display "Connection could not be established." three times
for i in range(3):
    print("Connection could not be established.")

# You want to welcome 3 users from a list by their name (for example, “Welcome, Emerick Larson”).
name = ["Emrick Larson","Estrella Ortiz", "Tori Shah"]
for i in name:
    print ("Welcome,", i)


# Iterative statement using `for`, `range()`, a loop variable of `i`, and `connection_attempts`
# Display "Connection could not be established." as many times as specified by `connection_attempts`
connection_attempts = 5
for i in range(connection_attempts):
    print("Connection could not be established")


# Iterative statement using `while` and `connection_attempts`
# Display "Connection could not be established." every iteration, until connection_attempts reaches a specified number
connection_attempts = 0
while connection_attempts < 7:
    print("Connection could not be established.") 
    connection_attempts = connection_attempts + 1

ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]

# For loop that displays the elements of `ip_addresses` one at a time
for ip_address in ip_addresses:
    print(ip_address)

allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71", 
              "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]

# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in



# For each IP address in the list of IP addresses from which users have tried to log in, 
# If it is among the allowed addresses, then display “IP address is allowed”
# Otherwise, display “IP address is not allowed”
allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71", "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]
ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147", "192.168.205.12", "192.168.200.48"]
for i in ip_addresses:
	if i in allow_list:
		print("IP address is allowed")
	else:
		print("IP address is not allowed")

# 
allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71", "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]

ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147", "192.168.205.12", "192.168.200.48"]

# For each IP address in the list of IP addresses from which users have tried to log in, 
# If it is among the allowed addresses, then display “IP address is allowed”
# Otherwise, display “IP address is not allowed”
               
for i in ip_addresses:
	if i in allow_list:
		print("IP address is allowed")
	else:
		print("IP address is not allowed. Further investigation of login activity required")
		break