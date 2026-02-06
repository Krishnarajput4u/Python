def rev(x):
    rev=0
    while(x>0):
        rev=rev*10+x%10
        x//=10
    return rev
x=int(input("Enter the number : "))
y=rev(x)
if(x==y):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")