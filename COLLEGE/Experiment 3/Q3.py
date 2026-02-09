#fibbonaci series
n=int(input("Enter the number of terms: "))
a, b = 0, 1
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to", n, ":")
    print(a)
else:
    print("Fibonacci sequence up to", n, ":")
    print(a, end=' ')
    print(b, end=' ')
    for _ in range(2, n):
        a, b = b, a + b
        print(b, end=' ')