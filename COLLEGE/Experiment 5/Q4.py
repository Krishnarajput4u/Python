# Create dictionary of persons

n = int(input("Enter number of persons: "))

people = {}

for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    people[name] = city

# a) Display all names
print("Names:", people.keys())

# b) Display all cities
print("Cities:", people.values())

# c) Display name and city
for name, city in people.items():
    print(name, "->", city)

# d) Count students per city
city_count = {}

for city in people.values():
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

print("Students per city:", city_count)
