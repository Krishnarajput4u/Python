total_area = 0

with open("city.txt", "r") as file:
    for line in file:
        city, pop, area = line.split()
        total_area += float(area)

print("Total Area:", total_area)