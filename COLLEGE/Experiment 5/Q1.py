n = int(input("Enter number of values: "))
values = []

for i in range(n):
    values.append(int(input()))

for i in range(4):   # 0 to 3
    print(i, "occurred", values.count(i), "times")
