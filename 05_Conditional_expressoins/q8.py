# Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

name = "Amit"

# True tests
print("Is name == 'Amit'? I predict True.")
print(name == "Amit")

print("\nIs name.lower() == 'amit'? I predict True.")
print(name.lower() == "amit")

print("\nIs len(name) == 4? I predict True.")
print(len(name) == 4)

print("\nIs name.startswith('A')? I predict True.")
print(name.startswith("A"))

print("\nIs name.endswith('t')? I predict True.")
print(name.endswith("t"))


# False tests
print("\nIs name == 'Abhay'? I predict False.")
print(name == "Abhay")

print("\nIs name == 'amit'? I predict False.")
print(name == "amit")

print("\nIs len(name) == 5? I predict False.")
print(len(name) == 5)

print("\nIs name.startswith('B')? I predict False.")
print(name.startswith("B"))

print("\nIs name.endswith('n')? I predict False.")
print(name.endswith("n"))