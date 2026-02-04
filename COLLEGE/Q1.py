a=input("Enter the character : ")

if a.isalpha():
    print("The entered character is a alphabet")  
elif(a.isdigit()):
    print("The entered character is a digit")
else:
    print("The entered character is a special character")