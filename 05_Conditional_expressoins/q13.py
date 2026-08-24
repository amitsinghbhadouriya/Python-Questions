# Add an if test to make sure the list of users is not empty. if the list is empty, print the message we need to find some users!

usernames = ['abhay', 'akash', 'dev']

if usernames:
    for username in usernames:
        print(f"Hello {username}, Welcome back")
else:
    print("We need to find some users.")
    
    
    
# Remove all of the usernames from your list, and make sure the correct message is printed.
    
usernames = []

if usernames:
    for username in usernames:
        print(f"Hello {username}, Welcome back")
else:
    print("We need to find some users.")