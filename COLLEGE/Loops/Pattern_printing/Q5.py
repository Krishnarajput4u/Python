x=int(input("Enter the number of rows: "))

for i in range(0, x):
    for j in range(x-i-1, 0, -1):
        print(" ", end="")
    for j in range(0, i+1):
        print("* ", end="")
    print()

for i in range(0,x):
    for j in range(0,x):
        print("* ", end="")
    print()