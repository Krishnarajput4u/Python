a=int(input("Enter the number of units consumed : "))
if a<=100:
    print("Charge :",a*2)
elif a>100 and a<=200:
    print("Charge :",100*2+(a-100)*3)
else:
    print("Charge :",100*2+100*3+(a-200)*5)