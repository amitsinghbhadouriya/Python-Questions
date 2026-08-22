# Write a program to find out whether a student is pass or fail, if it requires total 40%  and at least 33% in each subject to pass. Assume 3 Subjects and take marks as an input from the user

Math = int(input("Enter math marks: "))
Physics = int(input("Enter Physics marks: "))
Chemistry = int(input("Enter Chemistry marks: "))
total = (Math + Physics + Chemistry)/3

if total >= 40 and Math >= 33 and Physics >= 33 and Chemistry >= 33:
    print("You are pass")
else:
    print("You are fail")