count = 0
vowels = "AEIOUaeiou"

with open("name.txt", "r") as file:
    for name in file:
        if name[0] in vowels:
            count += 1

print("Names starting with vowel:", count)