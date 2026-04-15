try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))

    result = a / b

except ZeroDivisionError:
    print("Division by zero error")

else:
    print("Result =", result)
