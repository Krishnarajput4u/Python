# Store values in tuple and find average

n = int(input("Enter number of values: "))

values = []

for i in range(n):
    values.append(int(input()))

t = tuple(values)

average = sum(t) / len(t)

print("Tuple:", t)
print("Average:", average)

