longest = ""

with open("name.txt", "r") as file:
    for name in file:
        name = name.strip()
        if len(name) > len(longest):
            longest = name

print("Longest name:", longest)