#5.	Check whether the quadratic equation has real roots or imaginary roots. Display the roots.
b= int(input("Enter the coefficient of x:"))
c= int(input("Enter the constant term:"))
a= int(input("Enter the coefficient of x^2:"))
discriminant= b**2 - 4*a*c
if discriminant>0:
    print("The equation has real and distinct roots")
elif discriminant==0:
    print("The equation has real and equal roots") 
else:
    print("The equation has imaginary roots")