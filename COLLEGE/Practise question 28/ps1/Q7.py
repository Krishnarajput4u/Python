a=int(input("Enter the total number of classes held : "))
b=int(input("Enter the total number of classes attended : "))
c=(b/a)*100
if c>=75:
    print("You are allowed to sit in exam")
else:
    print("You are not allowed to sit in exam")