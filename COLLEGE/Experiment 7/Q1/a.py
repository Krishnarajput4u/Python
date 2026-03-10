with open("name.txt", "r") as file:
    names = file.readlines()
    print("Total names:", len(names))