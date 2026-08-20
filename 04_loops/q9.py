# Write a program to print following star pattern for n = 3
# ***
# * *
# ***

n = 3
for i in range(3):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n-2) + "*")