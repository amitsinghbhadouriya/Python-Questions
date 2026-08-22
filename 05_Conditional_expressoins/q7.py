# Write a program to calculate the grade of a student from his marks from the following scheme.
''' 
90-100 -> O
80-90 -> A
70-80 -> B
60-70 -> C
50-60 -> D
40-50 -> E
<40 -> F
'''

Math = int(input("Enter math marks: "))
English = int(input("Enter english marks: "))
Hindi = int(input("Enter hindi marks: "))
Physics = int(input("Enter physics marks: "))
Chemistry = int(input("Enter chemistry marks: "))
marks = (Math + English + Hindi + Physics + Chemistry)/5

if marks == 100 or marks > 90:
    grade = "O"
elif marks == 90 or marks > 80:
    grade = "A"
elif marks == 80 or marks > 70:
    grade = "B"
elif marks == 70 or marks > 60:
    grade = "C"
elif marks == 60 or marks > 50:
    grade = "D"
elif marks == 50 or marks > 40:
    grade = "E"
else:
    grade = "F"
    
print(f"Your marks are {marks} and you got grade {grade}")