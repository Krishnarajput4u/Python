#14.	Using membership operator find whether a given number is in sequence (10,20,56,78,89)
a=[10,20,56,78,89]
x=int(input("Enter the number to search in array [10,20,56,78,89] : "))
if x in a:
    print(f"{x} is present in the array")
else:
    print(f"{x} is not present in the array")
