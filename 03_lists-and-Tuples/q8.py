# Think of at least five places in the world you'd like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don't worry about printing the list neatly; just print it as a raw python list.
# use sorted() to print your list in alphabetical order without modifying the actual list.
# show that your list is still in its original order by printing it.
# use sorted() to print you list in reverse-alphabetical order without changing the order of the original list.
# show that your list is still in its original order by printing it again.
# use reverse() to change the order of your list. print the list to show that its order has changed.
# use reverse() to change the order of your list again. Print the list to show it's back to its original order.
# use sort() to change your list so it's stored in alphabetical order. print the list to show that its order has been changed.
# use sort() to change your list so it's stored in reverse-alphabetical order. print the list to show that its order has changed.

Places = ['switzerland', 'hongkong', 'paris', 'france', 'amsterdam']
print(Places)
print(sorted(Places))
print(Places)
print(sorted(Places, reverse=True))
print(Places)
Places.reverse()
print(Places)
Places.reverse()
print(Places)
Places.sort()
print(Places)
Places.sort(reverse=True)
print(Places)