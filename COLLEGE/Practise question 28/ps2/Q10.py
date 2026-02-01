a=int(input("Enter the total price of the products :"))
if a>=5000:
    print("You get a discount of 20% and total is ",a*0.8)
elif a>=3000:
    print("You get a discount of 10% and total is ",a*0.9)
else:
    print("No discount applied and total is ",a)