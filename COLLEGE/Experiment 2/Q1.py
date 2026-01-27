# Q1. Write a Python program to check if a given integer is divisible by both 3 and 5.
integer =int(input("Enter an integer:"))
if integer % 3 ==0 and integer % 5 ==0 :
    print("The number is divisible by both 3 and 5")
else:
    print("The number is not divisible by both 3 and 5") 