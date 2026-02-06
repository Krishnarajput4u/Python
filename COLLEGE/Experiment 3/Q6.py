x=int(input("Enter the number : "))
sum=0
while(x>0):
    sum+=x%10
    x//=10
print("Sum of digits is : ",sum)
