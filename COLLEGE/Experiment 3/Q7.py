total=0
for i in range(1, 101):
    if(i%5==0 and i%7==0):
        print(i,end=" ")
        total+=1
print("\nTotal numbers divisible by 5 and 7 are : ",total)