# Make a list that includes at least three people you'd like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
# Add a print() call at the end of your program, stating the name of the guest who can't make it.
# Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.
# Add a print() call to the end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# use insert() to add one new guest to the middle of your list.
# use append() to add one new guest to the end of your list.
# Print a new set of invitation message, one for each person in your list
# use len() to print a message indicating the number of people you're inviting to dinner.
# Add a new line that prints a message saying that you can invite only two people for dinner
# Use pop() to remove guests from your list one at a time until only two names remain in you list. Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they're still invited
# Use del to remove the last two names from your list, so you have an empty list. print your list to make sure you actually have an empty list at the end of your program.

Friends = ['Aman', 'Ajay', 'Dev']

message = 'You are invited for a dinner: '
for friend in Friends:
    print(f"{message}{friend}")

print(f"{Friends[1]} can't make it to dinner.")

Friends[1] = 'Rahul'

for friend in Friends:
    print(f"{message}{friend}")

print("I found a bigger dinner table.")

Friends.insert(0, 'Vikas')
Friends.insert(2, 'Rohit')
Friends.append('Karan')

for friend in Friends:
    print(f"{message}{friend}")

print(f"I am inviting {len(Friends)} people to dinner.")

print("I can invite only two people for dinner.")

while len(Friends) > 2:
    removed_friend = Friends.pop()
    print(f"Sorry {removed_friend}, I can't invite you to dinner.")

for friend in Friends:
    print(f"{friend}, you are still invited to dinner.")

del Friends[1]
del Friends[0]

print(Friends)