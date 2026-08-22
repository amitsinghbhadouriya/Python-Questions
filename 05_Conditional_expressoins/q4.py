# Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter your name: ")

if len(username) >= 10:
    print("This is a valid username")
else:
    print("This is not a valid username")