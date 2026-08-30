# Write a python function which converts inches to cms.

def inch_to_cms(inch):
    cms = inch * 2.54
    return cms

inch = int(input("Enter a value: "))
print(f"The {inch} inches in cms are: {inch_to_cms(inch)}")