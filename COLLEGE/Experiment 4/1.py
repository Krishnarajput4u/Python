string = input("Enter a string: ")
count = 0

for char in string:
    if char.isupper():
        count += 1

print("Number of capital letters:", count)