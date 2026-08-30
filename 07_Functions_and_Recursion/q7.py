# Write a python function to print multiplication table of a given number.

def table(n):
    for i in range(1,11):
        mul = n * i
        print(f"{n} x {i} = {mul}")   

n = int(input("Enter a number: "))
print(f"The table of {n}: ")
table(n)

    