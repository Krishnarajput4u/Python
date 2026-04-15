try:
    filename = input("Enter file name: ")

    file = open(filename, "r")

    print(file.read())

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Other error occurred:", e)

finally:
    print("File operation completed.")
