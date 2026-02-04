n = int(input("Enter number: ")) 
total = 0 
 
while True: 
    digit = n % 10 
    total += digit 
    n //= 10 
 
    if n == 0: 
        break 
 
print("Sum of digits:", total)