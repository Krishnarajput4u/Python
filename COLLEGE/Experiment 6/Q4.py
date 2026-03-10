def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def print_fibonacci_terms(terms):
    for i in range(terms):
        print(fibonacci(i), end=" ")


terms = int(input("Enter number of terms: "))
print_fibonacci_terms(terms)