a=input("Enter your password :")
b=len(a)
if b<6:
    print("Weak Password")
elif(b>=6 or b<=10):
    print("Moderate Password")
else:
    print("Strong Password")