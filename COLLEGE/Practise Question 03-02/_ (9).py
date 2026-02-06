# Q4: swap two numbers using assignment operators
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# simple swap using a temporary variable
temp = x
x = y
y = temp

print("After swap:")
print("x =", x)
print("y =", y)
