# sorted function
failed_login_list = [119, 101, 99, 91, 92, 105, 108, 85, 88, 90, 264, 223]
print(sorted(failed_login_list))

# functions
def analyze_logins(username, current_logins):
    print("current logins total for", username, "is", current_logins)
analyze_logins("A.A.Adnan",  10)

# login Function
def analyze_logins(username, current_day_logins, average_day_logins):
    print("current day login total for", username, "is", current_day_logins)
    print("average logins per day for", username, "is", average_day_logins)

    login_ratio = current_day_logins / average_day_logins
    print(username, "logged in", login_ratio, "times as much as they do on an average day")

analyze_logins("Adnan", 9, 3)

# function with return statement
def analyze_logins(username, current_day_logins, average_day_logins):
    print("current day login total for", username, "is", current_day_logins)
    print("Average logins per day for", username, "is", average_day_logins)

    login_ratio = current_day_logins / average_day_logins
    return login_ratio

login_analysis = analyze_logins("adnan", 10, 3)
print("Adnan", "logged in", login_analysis, "times as much as they do on an average day.")