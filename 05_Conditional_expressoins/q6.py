# Write a program to find out whether a given name is present in a list or not

names = ["Amit", "Dev", "Naitik", "Karan"]
name = input("Enter a name: ")

if name in names:
    print(f"Name {name} is present in a list")
else:
    print(f"Name {name} is not present in a list")