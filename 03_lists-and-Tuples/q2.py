# write a program to accept marks of 6 students and display them in a sorted manner.

mark1 = int(input("Enter mark 1: "))
mark2 = int(input("Enter mark 2: "))
mark3 = int(input("Enter mark 3: "))
mark4 = int(input("Enter mark 4: "))
mark5 = int(input("Enter mark 5: "))
mark6 = int(input("Enter mark 6: "))

marks = [mark1, mark2, mark3, mark4, mark5, mark6]
marks.sort()
print(marks)