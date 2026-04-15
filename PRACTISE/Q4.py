try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File does not exist")

finally:
    print("Program execution completed")
