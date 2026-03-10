movies = {}

n = int(input("Enter number of movies: "))

for i in range(n):
    name = input("Movie name: ")
    year = int(input("Year: "))
    director = input("Director: ")
    cost = float(input("Production cost: "))
    collection = float(input("Collection: "))

    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    }

# a) Print all movie details
for name, details in movies.items():
    print(name, details)

# b) Movies before 2015
for name in movies:
    if movies[name]["year"] < 2015:
        print("Before 2015:", name)

# c) Movies with profit
for name in movies:
    if movies[name]["collection"] > movies[name]["cost"]:
        print("Profitable:", name)

# d) Movies by particular director
d = input("Enter director name: ")

for name in movies:
    if movies[name]["director"] == d:
        print("Directed by", d, ":", name)
