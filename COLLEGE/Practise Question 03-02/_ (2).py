# Bitwise Q2: toggle the ith bit of a number
num = int(input("Enter a number: "))
i = int(input("Enter bit position to toggle (0-based): "))

mask = 1 << i
result = num ^ mask

print("Result after toggle:", result)
