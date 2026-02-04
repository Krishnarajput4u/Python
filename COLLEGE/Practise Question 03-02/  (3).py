# Bitwise Q3: count number of 1s in binary
num = int(input("Enter a number: "))
count = 0

while num > 0:
    if num & 1 == 1:
        count += 1
    num = num >> 1

print("Number of 1s:", count)
