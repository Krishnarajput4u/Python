volume_cone = lambda r, h: (1/3) * 3.14 * r**2 * h

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("Volume of cone:", volume_cone(r, h))