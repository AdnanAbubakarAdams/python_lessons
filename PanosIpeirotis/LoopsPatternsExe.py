wsj = """
Yahoo Inc. disclosed a massive security breach by a “state-sponsored actor” affecting at least 500 million users, potentially the largest such data breach on record and the latest hurdle for the beaten-down internet company as it works through the sale of its core business.
Yahoo said certain user account information—including names, email addresses, telephone numbers, dates of birth, hashed passwords and, in some cases, encrypted or unencrypted security questions and answers—was stolen from the company’s network in late 2014 by what it believes is a state-sponsored actor.
Yahoo said it is notifying potentially affected users and has taken steps to secure their accounts by invalidating unencrypted security questions and answers so they can’t be used to access an account and asking potentially affected users to change their passwords.
Yahoo recommended users who haven’t changed their passwords since 2014 do so. It also encouraged users change their passwords as well as security questions and answers for any other accounts on which they use the same or similar information used for their Yahoo account.
The company, which is working with law enforcement, said the continuing investigation indicates that stolen information didn't include unprotected passwords, payment-card data or bank account information.
With 500 million user accounts affected, this is the largest-ever publicly disclosed data breach, according to Paul Stephens, director of policy and advocacy with Privacy Rights Clearing House, a not-for-profit group that compiles information on data breaches.
No evidence has been found to suggest the state-sponsored actor is currently in Yahoo’s network, and Yahoo didn’t name the country it suspected was involved. In August, a hacker called “Peace” appeared in online forums, offering to sell 200 million of the company’s usernames and passwords for about $1,900 in total. Peace had previously sold data taken from breaches at Myspace and LinkedIn Corp.
"""
# ------------------------------------------
'''We will work now on a more challenging exercise. This will not only require the use of comprehensions, but will also ask you to put together things that we learned earlier in the course, especially when we studied strings.

Question 1: You are given the wsj article below. Write a list comprehension for getting the words that appear more than once. * Use the .split() command for splitting, without passing a parameter. * When counting words, case does not matter (i.e., YAHOO is the same as Yahoo).

Question 2: Find all the characters in the article that are not letters or numbers. You can use the isdigit() and isalpha() functions, which work on strings. (e.g, "Panos".isalpha() and "1234".isdigit() return True)'''
words = wsj.lower().split()
recurring  = [w for w in words if words.count(w)>1]
print(recurring)
print(sorted(set(recurring)))

# 
# Let's use a set comprehension here, to eliminate duplicates
nonalphanumeric = {c for c in wsj if not c.isdigit() and not c.isalpha()}
print(nonalphanumeric)