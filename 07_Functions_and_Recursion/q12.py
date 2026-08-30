# Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:
# "santiago, chile"
# call your function with at least three city-country pairs, and print the values that are returned

def city_country(city, country):
    return f"{city}, {country}"

print(city_country("Bangalore","India"))
print(city_country("Cairo","Egypt"))
print(city_country("Rome","Italy"))
