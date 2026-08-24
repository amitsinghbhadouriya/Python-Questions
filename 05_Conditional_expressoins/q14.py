# Make a list of five or more usernames called current_users.
# Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
# Loop through the new_users list to see if each new username has already been used. if it has, print a message that the person will need to enter a new username. if a username has not been used, print a message saying that the username is available.
# Make sure your comparison is case insensitive. if 'john' has been used, 'JOHN' should not be accepted.

current_users = ['abhay', 'akash', 'aman', 'jeet', 'dev']
new_users = ['naitik', 'abhay', 'karan', 'AMAN', 'abhishek']
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"You need to enter a new username, because {new_user} is already in use.")
    else:
        print(f"The username {new_user} is available")