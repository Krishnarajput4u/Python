#Q4.	Find the greatest among three numbers assuming no two values are same.
a= int(input("Enter first integer:"))
b= int(input("Enter second integer:"))
c= int(input("Enter third integer:"))
if a>b and a>c:
    print(f"{a} is the greatest among three")
elif b>a and b>c:
    print(f"{b} is the greatest among three")
else:
    print(f"{c} is the greatest among three")