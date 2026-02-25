string = input("Enter a string: ")
string = string.upper()

frequency = {}

for char in string:
    if char.isalpha():
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

for key in sorted(frequency):
    print(frequency[key], key, sep="")