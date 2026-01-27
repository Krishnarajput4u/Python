a= int(input("Enter first integer:"))
b= int(input("Enter second integer:"))

if a>b:
    print(f"{a} is greater than {b}")
elif b>a:
    print(f"{b} is greater than {a}")
else:
    print("Both are equal")