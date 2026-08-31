# Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that's being ordered. call the function three times, using a different number of arguments each time.

sandwich = ['corn', 'cheese', 'panner', 'mayo']

def sandwich(*toppings):
    print(toppings)
    
sandwich('corn')
sandwich('corn', 'cheese')
sandwich('corn', 'panner', 'mayo')