# Taking number of test cases
n = int(input("Enter number of test cases: "))
for i in range(n):
    try:
        # Taking input for a and b
        a, b = input("Enter two values: ").split()
        
        # Converting values to integers
        a = int(a)
        b = int(b)

        # Performing integer division
        result = a // b
        print(result)

    except ZeroDivisionError as e:
        print("Error Code:", e)

    except ValueError as e:
        print("Error Code:", e)
