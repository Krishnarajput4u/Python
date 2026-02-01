a=input("INPUT :")
if a.isdigit(): #check if the input is an integer
    print("Integer")
elif(a.isalpha()): #check if the input is an alphabet
    print("Alphabet")
else:
    print("Special Character")