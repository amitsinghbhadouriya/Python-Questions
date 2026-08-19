# Write a program to find weather a given number is prime or not.

n = int(input("Enter a number: "))
prime = True

for a in range(2, n):
    if(n%a==0):
        prime = False
        
if prime:
    print("This is a prime number")
else:
    print("This is not a prime number")