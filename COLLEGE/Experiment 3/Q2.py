n = int(input("Enter the number: "))
x = n
arm = 0
digits = len(str(n))

while x > 0:
    arm += (x % 10) ** digits
    x //= 10

if arm == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
