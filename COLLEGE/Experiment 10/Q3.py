import numpy as np

n = int(input("Enter size of matrix (n): "))

print("Enter first matrix:")
A = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    A.append(row)

print("Enter second matrix:")
B = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    B.append(row)

A = np.array(A)
B = np.array(B)

result = np.dot(A, B)

print("Matrix Multiplication Result:")
print(result)