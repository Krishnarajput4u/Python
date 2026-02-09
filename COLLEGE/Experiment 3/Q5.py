x = int(input("Enter the number: "))
temp = x
y = 0

for i in range(len(str(x))):
    y = (y * 10) + (x % 10)
    x //= 10

if temp == y:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
