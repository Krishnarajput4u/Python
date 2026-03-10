with open("city.txt", "r") as file:
    for line in file:
        city, pop, area = line.split()
        if float(pop) > 10:
            print(city)