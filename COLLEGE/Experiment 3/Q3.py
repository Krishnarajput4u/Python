def fibbonaci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibbonaci(n-1)+fibbonaci(n-2)
    
n=int(input("Enter the number of terms: "))
for i in range(n):
    print(fibbonaci(i),end=" ")