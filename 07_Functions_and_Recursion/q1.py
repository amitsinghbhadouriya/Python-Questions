# Write a program using Function to find greatest of three numbers

def greater(a,b,c):
    if a > b and a > c:
        return f"{a} is greater"
    elif b > a and b > c:
        return f"{b} is greater"
    else:
        return f"{c} is greater"
    
print(greater(3,4,5))