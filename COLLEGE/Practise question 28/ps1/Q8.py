a=int(input("Enter the temperature (Celsius): "))
if(a<0):
    print("Very Cold")
elif(a>=1 or a<=15):
    print("Cold")
elif(a>=16 or a<=25):
    print("Moderate")
else:
    print("Hot")