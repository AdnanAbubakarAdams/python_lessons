# 
employee_id = 4186
print(type(employee_id))

employee_id = str(4186)
print(type(employee_id))

# 
employee_id = 4186
employee_id = str(employee_id)
if len(employee_id) < 5:
    print("This employee ID has less than five digits. It does not meet length requirements.")

# 
employee_id = 4186
employee_id = str(employee_id)
print(employee_id)
if len(employee_id) < 5:
    employee_id = "E" + employee_id
print(employee_id)

# 
device_id = "r262c36"
# Extract the fourth character in `device_id` and display it
print(device_id[3])

# 
device_id = "r262c36"
# Extract the first through the third characters in `device_id` and display the result
print(device_id[0:3])

# 
url = "https://exampleURL1.com"
# Extract the protocol of `url` along with the syntax following it, display the result
print(url[0:8])

# 
url = "https://exampleURL1.com"
# Display the index where the domain extension ".com" is located in `url`
print(url.index(".com"))

# 
url = "https://exampleURL1.com"
# Assign `ind` to the output of applying `.index()` to `url` in order to extract the starting index of ".com" in `url` 
ind = url.index(".com")

# 
url = "https://exampleURL1.com"
ind = url.index(".com")
# Extract the domain extension in `url` and display it
print(url[ind:ind+4])

# 
url = "https://exampleURL1.com"
ind = url.index(".com")
# Extract the website name in `url` and display it
print(url[8:ind])