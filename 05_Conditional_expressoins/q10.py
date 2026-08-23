# Write an if-elif-else chain that determines a person's stage of life. set a value for the variable age, and then:
'''
if the person is less than 2 years old, print a message that the person is a baby.
if the person is at least 2 years old but less than 4, print a message that the person is a toddler.
if the person is at least 4 years old but less than 13, print a message that the person is a kid.
if the person is at least 13 years old but less than 20, print a message that the person is a teenager.
if the person is at least 20 years old but less than 65, print a message that the person is an adult.
if the person is age 65 or older, print a message that the person is an elder.
'''

age = int(input("Enter your age: "))

if age<2:
    print("You are a baby.")
elif 2<=age<4:
    print("You are a toddler.")
elif 4<=age<13:
    print("You are a kid.")
elif 13<=age<20:
    print("You are a teenager.")
elif 20<=age<65:
    print("You are an adult.")
else:
    print("You are an elder.")