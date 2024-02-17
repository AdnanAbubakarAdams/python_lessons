# Iterative statement using `while` and `connection_attempts`
# Display "Connection could not be established." every iteration, until connection_attempts reaches a specified number
connection_attempts = 0
while connection_attempts < 7:
    print("Connection could not be established!")
    connection_attempts = connection_attempts + 1

# For each IP address in the list of IP addresses from which users have tried to log in, 
# If it is among the allowed addresses, then display “IP address is allowed”
# Otherwise, display “IP address is not allowed”
# ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232",