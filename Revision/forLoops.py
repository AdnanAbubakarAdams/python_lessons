# loop through the list
for i in ["adnan", "rondo", "james", "son", "hojland"]:
    print(i)
# another way
list_of_approved_users = ["adnan", "rondo", "james", "son", "hojland"]
for username in list_of_approved_users:
    print(username)

# loop through a string
string = "cybersecurity"
for character in string:
    print(character)

# in range start at 0, end at 5 at 1 intervals remenber the end is always exclusive
for i in range(0, 5, 1):
    print(i)

# start at 1, end at 8 at 1 intervals, remenber the end is always exclusive
for i in range(1, 8, 1):
    print(i)

# 
for i in range(2, 10, 2):
    print(i)

# 
for i in range(6):
    print(i)

# print 3 numbers
for i in [9, 10, 11]:
    print(i)

# print access denied 4 times
for i in range(4):
    print("Access Denied")

# print range of nnumbers
for nums in range(10, 31):
    print(nums)

# print connections could not be established 5 times'
for i in range(5):
    print("connection to network could not be established")

# welcome list of players by their names
new_signings = ["rasmus", "onana", "anthony", "mount"]

for player in new_signings:
    print("welcome to manchester united", player)

# print out all IP addresses one at a time
ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]

for ip in ip_addresses:
    print(ip)

# # For each IP address in the list of IP addresses from which users have tried to log in, 
# If it is among the allowed addresses, then display “IP address is allowed”
# Otherwise, display “IP address is not allowed”
ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]

allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71", "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]

for ip_add in ip_addresses:
    if ip_add in allow_list:
        print("This IP address is allowed to access the internal resources!")
    else: 
        print("This IP is not allowed access")