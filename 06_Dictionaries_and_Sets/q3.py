# Can we have a set with 18(int) and "18"(str) as a values in it?

values = {18, "18"}
print(values)
print(type(values))
for value in values:
    print(type(value))

# What will be the length of following set s:

s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))