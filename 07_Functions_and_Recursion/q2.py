# Write a python program using function to convert celsius to fahrenheit.

def cel_to_fer(c):
    far = (c*9/5) + 32
    return far

c = int(input("Enter a value: "))
print(f"The {c} celsius in fahrenheit is {cel_to_fer(c)}")
