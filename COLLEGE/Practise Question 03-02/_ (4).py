# Bitwise Q4: check if number is divisible by 4
num = int(input("Enter a number: "))

if num & 3 == 0:
    print("Divisible by 4")
else:
    print("Not divisible by 4")
