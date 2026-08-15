# Store the names of a few of your friends in a list called names. Print each person's name by accessing each element in the list, one at a time.
# print a message to them. The text of each message should be the same, but each message should be personalized with the person's name.

names = ['Dev', 'Aman', 'Jeet', 'Akash', 'Sahil']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

message = "Hi how are you"
print(f"{message} {names[0]}")
print(f"{message} {names[1]}")
print(f"{message} {names[2]}")
print(f"{message} {names[3]}")
print(f"{message} {names[4]}")