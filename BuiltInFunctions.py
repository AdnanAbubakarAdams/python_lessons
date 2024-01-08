# 
failed_login_list = [119, 101, 99, 91, 92, 105, 108, 85, 88, 90, 264, 223]
print(sorted(failed_login_list))

# 
def analyze_logins(username, current_day_logins):
    print("Current day login total for", username, "is", current_day_logins)

analyze_logins("A.A.Adnan", 9)

# 
def analyze_logins(username, current_day_logins, average_day_logins):

    print("Current day login total for", username, "is", current_day_logins)
    print("Average logins per day for", username, "is", average_day_logins)

    login_ratio = current_day_logins / average_day_logins
    print(username, "logged in", login_ratio, "times as much as they do on an average day.")

analyze_logins("ejones", 9, 3)

# 
def analyze_logins(username, current_day_logins, average_day_logins):

    print("Current day login total for", username, "is", current_day_logins)
    print("Average logins per day for", username, "is", average_day_logins)

    login_ratio = current_day_logins / average_day_logins
    return login_ratio

login_analysis = analyze_logins("ejones", 9, 3)

print("ejones", "logged in", login_analysis, "times as much as they do on an average day.")

# 
def analyze_logins(username, current_day_logins, average_day_logins):

    print("Current day login total for", username, "is", current_day_logins)
    print("Average logins per day for", username, "is", average_day_logins)

    login_ratio = current_day_logins / average_day_logins
    return login_ratio

login_analysis = analyze_logins("ejones", 9, 3)

if login_analysis >= 3:
    print("Alert! This account has more login activity than normal.")