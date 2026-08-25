# Write a program to input eight numbers from the user and display all the unique numbers(once).
i = 1
numbers = set()
while (i<=8):
    num = input("Enter the number: ")
    numbers.add(num)
    i = i + 1
    
Unique_numbers = (numbers)
print(f"Unique_numbers are: {Unique_numbers}")
