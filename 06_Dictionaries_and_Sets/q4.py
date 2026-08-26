# Create an empty dictionary. Allow 4 friends to enter their favorite languages as values and use keys as their names. Assume that the names are unique.

fav_langs = {}

a = input("Enter your fav language: ")
b = input("Enter your fav language: ")
c = input("Enter your fav language: ")
d = input("Enter your fav language: ")

fav_langs['Abhay'] = a
fav_langs['Aman'] = b
fav_langs['Naitik'] = c
fav_langs['Dev'] = d

print(fav_langs)