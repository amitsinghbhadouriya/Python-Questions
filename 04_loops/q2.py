# Write a program to greet all the person names stored in a list l1 and which starts with A

l1 = ["Amit", "Aman", "Abhishek", "Jeet"]

for name in l1:
    if name.startswith("A"):
        print(f"Hello, {name}")